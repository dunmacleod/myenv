import json,sys,tempfile
sys.path.insert(0,'../mig')
from notionmig import api, tree, norm, Builder

B="/home/user/myenv/notion-migration/sprint4/backup"
p=json.load(open("subm_pages.json"))
LIVE_DE=p['de']['tgt']

# German for the six blocks whose English changed (Flowise/Agentflow -> n8n).
# Register follows the page's own voice: informal "du", house standard.
NEW_DE={
 9:  "Das Design als n8n-Workflows implementieren und gegen die Fehlermodi testen, "
     "für die du es entworfen hast",
 21: "Die finalen JSON-Exporte des Parent- und der Spezialisten-Workflows in n8n, erstellt nach "
     "der Testarbeit, zusammen mit einer Abhängigkeitsliste (Modelle, Credentials, Services und "
     "Sub-Workflows). Importierte Workflows benötigen weiterhin gültige Credentials und eine "
     "umgebungsspezifische Konfiguration. Behalte deine früheren Exporte als Backups.",
 47: "Ein Live-Lauf der neu entworfenen n8n-Workflows. Zeige, welche Nodes ausgeführt wurden, wie "
     "die Klassifizierung und der Handoff an die Spezialisten funktioniert haben, und die "
     "relevanten Execution-Daten. Zeige bei separaten Sub-Workflows deren Executions, anstatt den "
     "Eindruck zu erwecken, alles sei auf einer einzigen Canvas gelaufen.",
 77: "JSON-Exporte des Parent- und der Spezialisten-Workflows auf Importierbarkeit geprüft, mit "
     "dokumentierten Abhängigkeiten und ohne Credentials",
 91: "Heruntergeladene n8n-JSON-Exporte aller beteiligten Workflows, oder ein Link auf eine "
     "n8n-Instanz, die für den Reviewer zugänglich ist. Eine localhost-URL ist von außen nicht "
     "erreichbar.",
 109:"Erscheint jedes Feld, das zwischen Workflows übergeben wird, in deiner Spezifikation — mit "
     "festgelegtem Schreiber und Leser?",
}

de=json.load(open(f"{B}/A-DE-Anleitung zur Projektabgabe.json"))
n=[0]
def apply(bs):
    for b in bs:
        i=n[0]; n[0]+=1
        if i in NEW_DE:
            v=b[b['type']]
            old=''.join(x['plain_text'] for x in v['rich_text'])
            v['rich_text']=[{"type":"text","text":{"content":NEW_DE[i],"link":None},
                             "annotations":{"bold":False,"italic":False,"strikethrough":False,
                                            "underline":False,"code":False,"color":"default"},
                             "plain_text":NEW_DE[i],"href":None}]
            print(f"  block {i} ({b['type']}) replaced")
            print(f"     was: {old[:95]}")
            print(f"     now: {NEW_DE[i][:95]}")
        apply(b.get('_children') or [])
apply(de)
assert n[0]==117, n[0]
missing=[k for k in NEW_DE if k>=117]
assert not missing

tmp=tempfile.mkdtemp()
b=Builder(tmp)
payload=b.page(de)
print(f"\nbuilt {len(payload)} top-level blocks (images: {b.uploaded}, failures: {b.image_failures})")

old_ids=[x['id'] for x in tree(LIVE_DE)]
print(f"live page currently has {len(old_ids)} top-level blocks (the short draft version)")
new_ids=[]
for i in range(0,len(payload),100):
    r=api("PATCH",f"/blocks/{LIVE_DE}/children",{"children":payload[i:i+100]})
    if r.get("object")=="error":
        print("APPEND ERROR:",r.get("message")[:400]); sys.exit(1)
    new_ids+=[x['id'] for x in r['results']]
print(f"appended {len(new_ids)} blocks")
for bid in old_ids:
    api("DELETE",f"/blocks/{bid}")
print(f"deleted {len(old_ids)} old blocks")

got=tree(LIVE_DE)
exp=norm(de); act=norm(got)
print(f"\nverification: expected {len(exp)} top-level, got {len(act)} -> {'MATCH' if exp==act else 'MISMATCH'}")
if exp!=act:
    diffs=[]
    def cmp(a,bb,path=""):
        if len(a)!=len(bb): diffs.append(f"{path}: {len(a)} vs {len(bb)}")
        for j,(x,y) in enumerate(zip(a,bb)):
            q=f"{path}[{j}]{x.get('type')}"
            if x.get('type')!=y.get('type'): diffs.append(f"{q} vs {y.get('type')}"); continue
            for k in set(x)|set(y):
                if k=='children': continue
                if x.get(k)!=y.get(k): diffs.append(f"{q}.{k}")
            cmp(x.get('children',[]),y.get('children',[]),q+">")
    cmp(exp,act); print("diffs:",diffs[:10])
json.dump({'live_de':LIVE_DE,'new_ids':new_ids,'old_ids':old_ids,'replaced':list(NEW_DE)},open("retranslate_state.json","w"))
