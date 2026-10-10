"""Notion content migration: copy page bodies verbatim into existing pages, preserving page IDs."""
import json, os, subprocess, sys, time

NV = "Notion-Version: 2022-06-28"
BASE = "https://api.notion.com/v1"

# ---------------------------------------------------------------- http

def _curl(args, retries=6):
    last = None
    for a in range(retries):
        p = subprocess.run(["curl", "-sS", "--max-time", "120"] + args,
                           capture_output=True, text=True)
        if p.returncode != 0:
            last = {"object": "error", "message": f"curl rc={p.returncode} {p.stderr[:200]}"}
            time.sleep(1.5 * (a + 1)); continue
        try:
            d = json.loads(p.stdout)
        except Exception:
            last = {"object": "error", "message": f"bad json: {p.stdout[:200]}"}
            time.sleep(1.5 * (a + 1)); continue
        if d.get("object") == "error":
            if d.get("status") in (409, 429, 500, 502, 503, 504):
                last = d; time.sleep(2.0 * (a + 1)); continue
            return d
        return d
    return last or {"object": "error", "message": "retries exhausted"}

def api(method, path, body=None):
    args = ["-X", method, BASE + path, "-H", NV]
    if body is not None:
        args += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    return _curl(args)

def download(url, dest):
    p = subprocess.run(["curl", "-sS", "--max-time", "180", "-o", dest, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    return p.stdout.strip() == "200" and os.path.getsize(dest) > 0

# ---------------------------------------------------------------- read

def children(bid):
    out, cur = [], None
    while True:
        q = f"/blocks/{bid}/children?page_size=100" + (f"&start_cursor={cur}" if cur else "")
        d = api("GET", q)
        if d.get("object") == "error":
            raise RuntimeError(f"read {bid}: {d.get('message')}")
        out += d["results"]
        if not d.get("has_more"):
            return out
        cur = d["next_cursor"]

def tree(bid):
    ks = children(bid)
    for k in ks:
        if k.get("has_children") and k["type"] not in ("child_page", "child_database"):
            k["_children"] = tree(k["id"])
    return ks

# ---------------------------------------------------------------- normalise (for comparison)

def norm_rt(rts, remap=None):
    """Canonical form of a rich-text array. A page mention is compared by the page it
    points at (remapped to its destination) rather than by the title Notion renders,
    because the destination page may legitimately carry a different title."""
    out = []
    for r in rts or []:
        t = r["type"]
        e = {"t": t, "a": dict(r.get("annotations", {}))}
        if t == "mention":
            m = r["mention"]; e["m"] = m["type"]
            if m["type"] == "page":
                pid = m["page"]["id"]
                e["ref"] = (remap or {}).get(pid, pid)
            else:
                e["x"] = r.get("plain_text", "")
        else:
            e["x"] = r.get("plain_text", "")
        if t == "text" and (r.get("text") or {}).get("link"):
            e["l"] = r["text"]["link"]["url"]
        if t == "equation":
            e["eq"] = r["equation"]["expression"]
        out.append(e)
    return out

HEADINGS = ("heading_1", "heading_2", "heading_3", "heading_4")

def norm(blocks, remap=None):
    res = []
    for b in blocks:
        t = b["type"]; v = b.get(t) or {}
        e = {"type": t}
        if isinstance(v, dict):
            if "rich_text" in v:   e["rt"] = norm_rt(v["rich_text"], remap)
            if v.get("caption"):   e["cap"] = norm_rt(v["caption"], remap)
            if v.get("color") and v["color"] != "default": e["color"] = v["color"]
            if t == "to_do":       e["checked"] = bool(v.get("checked"))
            if t in HEADINGS:      e["tog"] = bool(v.get("is_toggleable"))
            if t == "callout":
                ic = v.get("icon")
                e["icon"] = ic.get("emoji") if ic and ic.get("type") == "emoji" else (ic.get("type") if ic else None)
            if t == "code":        e["lang"] = v.get("language")
            if t == "embed":       e["url"] = v.get("url")
            if t == "bookmark":    e["url"] = v.get("url")
            if t == "table":
                e["tw"] = v.get("table_width"); e["ch"] = bool(v.get("has_column_header")); e["rh"] = bool(v.get("has_row_header"))
            if t == "table_row":   e["cells"] = [norm_rt(c, remap) for c in v.get("cells", [])]
            if t == "image":       e["img"] = True
        kids = b.get("_children") or []
        if kids:
            e["children"] = norm(kids, remap)
        res.append(e)
    return res

# ---------------------------------------------------------------- build payloads

UNRESOLVED = []

def build_rt(rts, remap=None):
    out = []
    for r in rts or []:
        t = r["type"]
        if t == "mention" and r["mention"]["type"] == "page":
            pid = r["mention"]["page"]["id"]
            new = (remap or {}).get(pid)
            if new:
                out.append({"type": "mention", "mention": {"type": "page", "page": {"id": new}}})
                continue
            # no destination equivalent: keep the words, drop the dangling link
            UNRESOLVED.append((pid, r.get("plain_text")))
            out.append({"type": "text", "text": {"content": r.get("plain_text", "")}})
            continue
        if t == "text":
            item = {"type": "text", "text": {"content": r["text"]["content"]}}
            if (r["text"] or {}).get("link"):
                item["text"]["link"] = {"url": r["text"]["link"]["url"]}
        elif t == "equation":
            item = {"type": "equation", "equation": {"expression": r["equation"]["expression"]}}
        else:
            # mentions etc: degrade to plain text so nothing is silently dropped
            item = {"type": "text", "text": {"content": r.get("plain_text", "")}}
        ann = {k: v for k, v in (r.get("annotations") or {}).items()
               if k in ("bold", "italic", "strikethrough", "underline", "code", "color")}
        if ann:
            item["annotations"] = ann
        out.append(item)
    return out

TEXTY = ("paragraph", "quote", "bulleted_list_item", "numbered_list_item",
         "to_do", "toggle", "callout", "heading_1", "heading_2", "heading_3", "heading_4")

class Builder:
    """Converts a source block tree into create payloads, re-uploading images on the way."""

    def __init__(self, tmpdir, log=print, remap=None):
        self.tmpdir = tmpdir; self.log = log; self.remap = remap or {}
        self.uploaded = 0; self.image_failures = []

    def upload_image(self, block):
        v = block["image"]; kind = v.get("type")
        if kind == "external":
            return {"type": "external", "external": {"url": v["external"]["url"]}}
        url = (v.get("file") or {}).get("url")
        if not url:
            self.image_failures.append((block["id"], "no url")); return None
        name = url.split("?")[0].rsplit("/", 1)[-1] or "image.png"
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else "png"
        ctype = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif",
                 "webp": "image/webp", "svg": "image/svg+xml"}.get(ext, "image/png")
        path = os.path.join(self.tmpdir, f"{block['id']}.{ext}")
        if not download(url, path):
            self.image_failures.append((block["id"], "download failed")); return None
        c = api("POST", "/file_uploads", {"filename": name, "content_type": ctype})
        if c.get("object") == "error" or not c.get("upload_url"):
            self.image_failures.append((block["id"], f"create: {c.get('message')}")); return None
        s = _curl(["-X", "POST", c["upload_url"], "-H", NV, "-F", f"file=@{path};type={ctype}"])
        if s.get("status") != "uploaded":
            self.image_failures.append((block["id"], f"send: {s.get('message')}")); return None
        os.remove(path); self.uploaded += 1
        return {"type": "file_upload", "file_upload": {"id": c["id"]}}

    def block(self, b):
        t = b["type"]; v = b.get(t) or {}
        kids = b.get("_children") or []

        if t == "image":
            src = self.upload_image(b)
            if src is None:
                return None
            payload = dict(src)
            if v.get("caption"):
                payload["caption"] = build_rt(v["caption"], self.remap)
            return {"object": "block", "type": "image", "image": payload}

        if t == "divider":
            return {"object": "block", "type": "divider", "divider": {}}

        if t == "embed":
            p = {"url": v.get("url")}
            if v.get("caption"): p["caption"] = build_rt(v["caption"], self.remap)
            return {"object": "block", "type": "embed", "embed": p}

        if t == "bookmark":
            p = {"url": v.get("url")}
            if v.get("caption"): p["caption"] = build_rt(v["caption"], self.remap)
            return {"object": "block", "type": "bookmark", "bookmark": p}

        if t == "code":
            p = {"rich_text": build_rt(v.get("rich_text"), self.remap), "language": v.get("language") or "plain text"}
            if v.get("caption"): p["caption"] = build_rt(v["caption"], self.remap)
            return {"object": "block", "type": "code", "code": p}

        if t == "equation":
            return {"object": "block", "type": "equation", "equation": {"expression": v.get("expression", "")}}

        if t == "table":
            rows = [self.block(r) for r in kids]
            rows = [r for r in rows if r]
            return {"object": "block", "type": "table", "table": {
                "table_width": v.get("table_width") or (len(kids[0]["table_row"]["cells"]) if kids else 1),
                "has_column_header": bool(v.get("has_column_header")),
                "has_row_header": bool(v.get("has_row_header")),
                "children": rows}}

        if t == "table_row":
            return {"object": "block", "type": "table_row",
                    "table_row": {"cells": [build_rt(c, self.remap) for c in v.get("cells", [])]}}

        if t == "column_list":
            cols = [self.block(c) for c in kids]
            cols = [c for c in cols if c]
            return {"object": "block", "type": "column_list", "column_list": {"children": cols}}

        if t == "column":
            inner = [self.block(c) for c in kids]
            inner = [c for c in inner if c]
            p = {"children": inner}
            if v.get("width_ratio"):
                p["width_ratio"] = v["width_ratio"]
            return {"object": "block", "type": "column", "column": p}

        if t in TEXTY:
            p = {"rich_text": build_rt(v.get("rich_text"), self.remap)}
            if v.get("color"): p["color"] = v["color"]
            if t == "to_do":  p["checked"] = bool(v.get("checked"))
            if t in HEADINGS and v.get("is_toggleable"): p["is_toggleable"] = True
            if t == "callout" and v.get("icon"):
                ic = v["icon"]
                if ic.get("type") == "emoji":
                    p["icon"] = {"type": "emoji", "emoji": ic["emoji"]}
                elif ic.get("type") == "external":
                    p["icon"] = {"type": "external", "external": {"url": ic["external"]["url"]}}
            if kids:
                inner = [self.block(c) for c in kids]
                p["children"] = [c for c in inner if c]
            return {"object": "block", "type": t, t: p}

        self.log(f"      !! unsupported block type skipped: {t}")
        return None

    def page(self, blocks):
        out = []
        for b in blocks:
            p = self.block(b)
            if p:
                out.append(p)
        return out

# ---------------------------------------------------------------- markdown backup

def to_md(blocks, depth=0):
    lines = []
    pad = "  " * depth
    for b in blocks:
        t = b["type"]; v = b.get(t) or {}
        txt = "".join(r.get("plain_text", "") for r in (v.get("rich_text") or [])) if isinstance(v, dict) else ""
        if t.startswith("heading_"):
            lines.append(pad + "#" * int(t[-1]) + " " + txt)
        elif t == "paragraph":          lines.append(pad + txt)
        elif t == "bulleted_list_item": lines.append(pad + "- " + txt)
        elif t == "numbered_list_item": lines.append(pad + "1. " + txt)
        elif t == "to_do":              lines.append(pad + ("- [x] " if v.get("checked") else "- [ ] ") + txt)
        elif t == "quote":              lines.append(pad + "> " + txt)
        elif t == "callout":
            ic = (v.get("icon") or {}).get("emoji", "")
            lines.append(pad + f"> {ic} {txt}")
        elif t == "code":
            lines.append(pad + "```" + (v.get("language") or ""))
            lines.append(txt); lines.append(pad + "```")
        elif t == "image":
            src = v.get("external", {}).get("url") if v.get("type") == "external" else "(notion-hosted file)"
            lines.append(pad + f"![image]({src})")
        elif t == "embed":   lines.append(pad + f"[EMBED] {v.get('url')}")
        elif t == "bookmark":lines.append(pad + f"[BOOKMARK] {v.get('url')}")
        elif t == "divider": lines.append(pad + "---")
        elif t == "table":   lines.append(pad + "[TABLE]")
        elif t == "table_row":
            lines.append(pad + "| " + " | ".join("".join(r.get("plain_text", "") for r in c) for c in v.get("cells", [])) + " |")
        elif t in ("column_list", "column"): lines.append(pad + f"[{t.upper()}]")
        else: lines.append(pad + f"[{t}] {txt}")
        if b.get("_children"):
            lines += to_md(b["_children"], depth + 1)
    return lines
