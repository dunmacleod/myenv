import json, os, sys, time, tempfile, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import notionmig
from notionmig import api, tree, norm, Builder, to_md

PLAN   = sys.argv[1]
OUTDIR = sys.argv[2]
STATEF = sys.argv[3]
REMAPF = sys.argv[4] if len(sys.argv) > 4 else None
REMAP  = json.load(open(REMAPF)) if REMAPF else {}

os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(os.path.join(OUTDIR, "backup"), exist_ok=True)
state = json.load(open(STATEF)) if os.path.exists(STATEF) else {}
def save(): json.dump(state, open(STATEF, "w"), indent=1)

def log(*a):
    print(*a, flush=True)

def safe(s):
    return "".join(c if c.isalnum() or c in " -_" else "_" for c in s)[:70].strip()

plan = json.load(open(PLAN))
work = [p for p in plan if p["action"] == "rewrite"]
tmp = tempfile.mkdtemp()
log(f"=== migrating {len(work)} pages ===")

for n, p in enumerate(work, 1):
    tgt, src = p["tgt"], p["src"]
    st = state.setdefault(tgt, {})
    log(f"\n[{n}/{len(work)}] {p['module']} {p['lang']} {p['src_title'][:60]}")
    try:
        # 1. backup -------------------------------------------------------
        if not st.get("backup"):
            old = tree(tgt)
            fn = f"{p['module']}-{p['lang']}-{safe(p['tgt_title'] or p['src_title'])}"
            json.dump(old, open(os.path.join(OUTDIR, "backup", fn + ".json"), "w"), indent=1)
            open(os.path.join(OUTDIR, "backup", fn + ".md"), "w").write(
                f"# {p['tgt_title']}\n\nNotion page: {p['tgt_url']}\nBacked up before n8n migration\n\n"
                + "\n".join(to_md(old)))
            st["old_ids"] = [b["id"] for b in old]
            st["backup"] = fn
            save()
            log(f"   backed up {len(st['old_ids'])} top-level blocks -> {fn}")

        # 2. build + append ----------------------------------------------
        if not st.get("appended_done"):
            # a partial append from a crashed run must be undone first
            for bid in st.get("new_ids", []):
                api("DELETE", f"/blocks/{bid}")
            st["new_ids"] = []
            s = tree(src)
            notionmig.UNRESOLVED = []
            b = Builder(tmp, log=log, remap=REMAP)
            payload = b.page(s)
            st["images"] = b.uploaded
            st["unresolved_mentions"] = list(notionmig.UNRESOLVED)
            if notionmig.UNRESOLVED:
                log(f"   !! unresolved mentions: {notionmig.UNRESOLVED}")
            st["image_failures"] = b.image_failures
            if b.image_failures:
                log(f"   !! image failures: {b.image_failures}")
            log(f"   built {len(payload)} blocks ({b.uploaded} images re-uploaded)")
            for i in range(0, len(payload), 100):
                r = api("PATCH", f"/blocks/{tgt}/children", {"children": payload[i:i + 100]})
                if r.get("object") == "error":
                    raise RuntimeError(f"append: {r.get('message')}")
                st["new_ids"] += [x["id"] for x in r.get("results", [])]
                save()
            st["appended_done"] = True
            save()
            log(f"   appended {len(st['new_ids'])} blocks")

        # 3. delete the old content --------------------------------------
        if not st.get("deleted_done"):
            remaining = []
            for bid in st.get("old_ids", []):
                r = api("DELETE", f"/blocks/{bid}")
                if r.get("object") == "error" and "Could not find block" not in str(r.get("message")):
                    remaining.append(bid)
            st["delete_failures"] = remaining
            st["deleted_done"] = True
            save()
            log(f"   deleted {len(st['old_ids']) - len(remaining)}/{len(st['old_ids'])} old blocks")

        # 4. title --------------------------------------------------------
        if p["title_change"] and not st.get("title_done"):
            sp = api("GET", f"/pages/{src}")
            rt = sp["properties"]["Lesson"]["title"]
            clean = [{"type": "text",
                      "text": {"content": x["plain_text"],
                               **({"link": {"url": x["href"]}} if x.get("href") else {})},
                      "annotations": {k: v for k, v in x["annotations"].items()}}
                     for x in rt]
            r = api("PATCH", f"/pages/{tgt}", {"properties": {"Lesson": {"title": clean}}})
            if r.get("object") == "error":
                raise RuntimeError(f"title: {r.get('message')}")
            st["title_done"] = True
            save()
            log(f"   title -> {p['src_title'][:60]}")

        # 5. verify -------------------------------------------------------
        got = tree(tgt)
        exp = tree(src)
        ng, ne = norm(got), norm(exp, REMAP)
        st["verify_blocks"] = [len(ne), len(ng)]
        st["verified"] = (ne == ng)
        if not st["verified"]:
            diffs = []
            def cmp(a, b, path=""):
                if len(a) != len(b):
                    diffs.append(f"{path}: count {len(a)} vs {len(b)}")
                for i, (x, y) in enumerate(zip(a, b)):
                    q = f"{path}[{i}]{x.get('type')}"
                    if x.get("type") != y.get("type"):
                        diffs.append(f"{q}: type != {y.get('type')}"); continue
                    for k in set(x) | set(y):
                        if k == "children": continue
                        if x.get(k) != y.get(k):
                            diffs.append(f"{q}.{k}: {json.dumps(x.get(k), ensure_ascii=False)[:90]} != {json.dumps(y.get(k), ensure_ascii=False)[:90]}")
                    cmp(x.get("children", []), y.get("children", []), q + ">")
            cmp(ne, ng)
            st["diffs"] = diffs[:30]
            log(f"   VERIFY MISMATCH ({len(diffs)}): {diffs[:3]}")
        else:
            log(f"   verified OK ({len(ng)} blocks)")
        save()
    except Exception as e:
        st["error"] = f"{e}"
        save()
        log(f"   ERROR: {e}")
        traceback.print_exc()

log("\n=== done ===")
ok = sum(1 for p in work if state.get(p["tgt"], {}).get("verified"))
log(f"verified {ok}/{len(work)}")
