import json,os,sys,tempfile,traceback
sys.path.insert(0,'../mig')
from notionmig import api, tree, norm, Builder, to_md

OUT="/home/user/myenv/notion-migration/ihk-data-analyst"
LIVE_DB="38b94183-19f3-8014-85f3-e8fa36ac14cd"
os.makedirs(f"{OUT}/backup",exist_ok=True)
state=json.load(open("ihk_state.json")) if os.path.exists("ihk_state.json") else {}
def save(): json.dump(state,open("ihk_state.json","w"),indent=1)
def safe(s): return "".join(c if c.isalnum() or c in " -_" else "_" for c in (s or ""))[:70].strip()
plan=json.load(open("ihk_plan.json")); dele=json.load(open("ihk_delete.json"))
tmp=tempfile.mkdtemp()

# ---- phase 0: back up every live page, including the ones being removed
print("=== phase 0: backing up all live pages ===",flush=True)
for row in [p for p in plan if p['tgt']] + dele:
    pid=row['tgt'] if 'tgt' in row and row.get('tgt') else row['id']
    key=f"backup:{pid}"
    if state.get(key): continue
    pg=api("GET",f"/pages/{pid}")
    blocks=tree(pid)
    title=''.join(x['plain_text'] for x in pg['properties']['Lesson']['title'])
    fn=safe(("DELETED-" if 'id' in row and not row.get('tgt') else "")+title) or pid
    json.dump({'page':pg,'blocks':blocks},open(f"{OUT}/backup/{fn}.json","w"),indent=1,ensure_ascii=False)
    open(f"{OUT}/backup/{fn}.md","w").write(f"# {title}\n\n{pg['url']}\n\n"+"\n".join(to_md(blocks)))
    state[key]={'file':fn,'blocks':len(blocks)}; save()
    print(f"   backed up {title[:52]!r} ({len(blocks)} blocks)",flush=True)

def props_for(p):
    pr={"Lesson":{"title":[{"type":"text","text":{"content":p['src_title']}}]}}
    if p.get('sprint'): pr["Sprint"]={"select":{"name":p['sprint']}}
    if p.get('lang'):   pr["Language"]={"select":{"name":p['lang']}}
    return pr

# ---- phase 1: rewrite the matched pages
print("\n=== phase 1: updating matched pages ===",flush=True)
for p in [x for x in plan if x['action']=='rewrite']:
    st=state.setdefault(p['tgt'],{})
    if st.get("done"): continue
    try:
        for bid in st.get("new_ids",[]): api("DELETE",f"/blocks/{bid}")
        st["new_ids"]=[]
        old=[b['id'] for b in tree(p['tgt'])]
        b=Builder(tmp); payload=b.page(tree(p['src']))
        st["uploads"]=b.uploaded; st["upload_failures"]=b.image_failures
        for i in range(0,len(payload),100):
            r=api("PATCH",f"/blocks/{p['tgt']}/children",{"children":payload[i:i+100]})
            if r.get("object")=="error": raise RuntimeError(f"append: {r.get('message')}")
            st["new_ids"]+=[x['id'] for x in r['results']]; save()
        for bid in old: api("DELETE",f"/blocks/{bid}")
        r=api("PATCH",f"/pages/{p['tgt']}",{"properties":props_for(p)})
        if r.get("object")=="error": raise RuntimeError(f"props: {r.get('message')}")
        st["done"]=True; save()
        print(f"   {p['src_title'][:50]:52} {len(payload):3} blocks (replaced {len(old)}), {b.uploaded} file(s)",flush=True)
    except Exception as e:
        st["error"]=str(e); save(); print(f"   ERROR {p['src_title'][:40]}: {e}",flush=True); traceback.print_exc()

# ---- phase 2: create the pages that exist only in NOV
print("\n=== phase 2: creating new pages ===",flush=True)
for p in [x for x in plan if x['action']=='create']:
    st=state.setdefault("create:"+p['src'],{})
    if st.get("done"): continue
    try:
        b=Builder(tmp); payload=b.page(tree(p['src']))
        r=api("POST","/pages",{"parent":{"database_id":LIVE_DB},"properties":props_for(p),
                               "children":payload[:100]})
        if r.get("object")=="error": raise RuntimeError(f"create: {r.get('message')}")
        new=r['id']; st["new_page"]=new; save()
        for i in range(100,len(payload),100):
            rr=api("PATCH",f"/blocks/{new}/children",{"children":payload[i:i+100]})
            if rr.get("object")=="error": raise RuntimeError(f"append: {rr.get('message')}")
        st["done"]=True; st["uploads"]=b.uploaded; save()
        print(f"   created {p['src_title'][:48]:50} {len(payload):3} blocks -> {r['url']}",flush=True)
    except Exception as e:
        st["error"]=str(e); save(); print(f"   ERROR {p['src_title'][:40]}: {e}",flush=True)

# ---- phase 3: remove the live pages NOV does not have
print("\n=== phase 3: removing live pages with no NOV counterpart ===",flush=True)
for d in dele:
    st=state.setdefault("del:"+d['id'],{})
    if st.get("done"): continue
    r=api("PATCH",f"/pages/{d['id']}",{"in_trash":True})
    if r.get("object")=="error":
        st["error"]=r.get('message'); print(f"   ERROR {str(d['title'])[:44]}: {r.get('message')}",flush=True)
    else:
        st["done"]=True; print(f"   archived {str(d['title'])[:60]}",flush=True)
    save()
print("\n=== done ===",flush=True)
