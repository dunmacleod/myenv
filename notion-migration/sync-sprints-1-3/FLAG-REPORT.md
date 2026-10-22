# Sprints 1–3 sync — both modules, both courses

**Status: in sync.** Every lesson page in sprints 1, 2 and 3 of both courses now carries the
content of its `(new, n8n)` draft counterpart. Verified by re-reading all 270 pages from Notion
after the copy and comparing them block by block against the draft: **0 pages differ.**

No pages were created, deleted or re-parented. All 270 page IDs and URLs are unchanged and live
row counts are untouched (Building AI Agents A 100 / B 88, Advanced Agent Systems A 74 / B 73).

## Verification matrix (after the copy)

| Course | Module | Sprint | Pages | Identical | Icon-only | Section pages | Differ |
|---|---|---|---|---|---|---|---|
| Advanced Agent Systems | A | 1 | 27 | 23 | 2 | 2 | **0** |
| Advanced Agent Systems | A | 2 | 18 | 13 | 1 | 4 | **0** |
| Advanced Agent Systems | A | 3 | 17 | 14 | 0 | 3 | **0** |
| Advanced Agent Systems | B | 1 | 18 | 15 | 0 | 3 | **0** |
| Advanced Agent Systems | B | 2 | 20 | 15 | 2 | 3 | **0** |
| Advanced Agent Systems | B | 3 | 20 | 14 | 2 | 4 | **0** |
| Building AI Agents | A | 1 | 32 | 27 | 1 | 4 | **0** |
| Building AI Agents | A | 2 | 28 | 15 | 8 | 5 | **0** |
| Building AI Agents | A | 3 | 21 | 6 | 10 | 5 | **0** |
| Building AI Agents | B | 1 | 24 | 20 | 0 | 4 | **0** |
| Building AI Agents | B | 2 | 22 | 14 | 4 | 4 | **0** |
| Building AI Agents | B | 3 | 23 | 18 | 1 | 4 | **0** |
| **Total** | | | **270** | **194** | **31** | **45** | **0** |

"Icon-only" means the page matches the draft except that icon-less callouts show Notion's default
💡 — the API cannot create a callout without an icon. "Section pages" are grouping rows with no body.

## What this run changed

- **82 pages** had their body replaced (the rest already matched)
- **131 images** re-hosted in the live workspace
- **27 titles** renamed to the draft's n8n names
- 10 internal cross-links remapped to their live equivalents
- 0 errors, 0 image failures, 0 unresolved links

Most of the work was sprint 3, which the curriculum team converted to n8n after my 13 Oct run
(on 13 Oct it was still Flowise content, byte-identical to live).

---

## 1. Quiz embeds removed — re-add in the LMS

29 campus quiz embeds across 19 lessons, on pages whose draft version carries none.

| Group | Lang | Lesson | Live page | Removed quiz URL |
|---|---|---|---|---|
| BAA A3 | DE | Tools zu einem einzelnen Agenten hinzufügen | [open](https://app.notion.com/p/Tools-zu-einem-einzelnen-Agenten-hinzuf-gen-3779418319f3803b9ef9d5b760708a19) | `https://app.masterschool.com/campus/multi-choice-question/a3d41697-73fe-4f60-85a9-23d2edd4275e` |
| BAA A3 | DE | Tool-Auswahl in der Praxis | [open](https://app.notion.com/p/Tool-Auswahl-in-der-Praxis-3779418319f380f9b613ca4478a2cc5b) | `https://app.masterschool.com/campus/multi-choice-question/7312ae6b-b883-488d-84dd-302c1a7c8e53` |
| BAA A3 | DE | Tool-Fehler und Endlosschleifen behandeln | [open](https://app.notion.com/p/Tool-Fehler-und-Endlosschleifen-behandeln-3779418319f380099057cc7c61cfc543) | `https://app.masterschool.com/campus/multi-choice-question/2178ed17-5d4f-4303-9c64-0b2cf853050e` |
| BAA B3 | EN | n8n Orchestration Checkpoint | [open](https://app.notion.com/p/n8n-Orchestration-Checkpoint-3789418319f3806c8a60ecb4a2e8338c) | `https://app.masterschool.com/campus/multi-choice-question/db64256a-841b-4414-be38-fb0fdeebeceb` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/d382fe32-e13b-467d-bda3-83b4b81b138f` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/ae5728dd-ee2c-4844-91ab-2ed1d4f66d34` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/283cf756-b1d1-4bb9-bce0-56dc45018b7f` |
| BAA B3 | DE | n8n Orchestrierung: Checkpoint | [open](https://app.notion.com/p/n8n-Orchestrierung-Checkpoint-3829418319f3801fa6a2de246ce16d65) | `https://app.masterschool.com/campus/multi-choice-question/ddc37ddf-d184-4eec-bc6c-af814a03ac97` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/819ba9da-c37f-4d3f-86d4-d7637f5a6d3f` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/5b23400e-f177-44bf-838a-d11b39c9ed95` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/9223997d-6ed9-49d4-a9b0-942b470a4377` |
| BAA B3 | EN | What Is MCP? Connecting MCP Tools in n8n | [open](https://app.notion.com/p/What-Is-MCP-Connecting-MCP-Tools-in-n8n-3669418319f380d39e71ffede85a6202) | `https://app.masterschool.com/campus/multi-choice-question/0acaa5be-684a-45ac-9654-7df3e7f8ecfa` |
| BAA B3 | DE | Was ist MCP? MCP-Tools in n8n verbinden | [open](https://app.notion.com/p/Was-ist-MCP-MCP-Tools-in-n8n-verbinden-3789418319f380a68d99f8aaa2b5d19b) | `https://app.masterschool.com/campus/multi-choice-question/8b1e062d-8df7-4a1f-970b-021bbd010a66` |
| BAA B3 | EN | Custom Logic with the n8n Code Node | [open](https://app.notion.com/p/Custom-Logic-with-the-n8n-Code-Node-3669418319f380c5b881e1093a363bbe) | `https://app.masterschool.com/campus/multi-choice-question/cd9e6ff6-d775-4ae0-aacd-b28526a7470d` |
| BAA B3 | DE | Eigene Logik mit dem n8n Code Node | [open](https://app.notion.com/p/Eigene-Logik-mit-dem-n8n-Code-Node-3789418319f380659b21ce4ecb757363) | `https://app.masterschool.com/campus/multi-choice-question/33e68568-49e1-47c5-83f4-16224eef9ee3` |
| BAA B3 | EN | Modular Workflows with Execute Sub-workflow | [open](https://app.notion.com/p/Modular-Workflows-with-Execute-Sub-workflow-37d9418319f38001b832e57f35275540) | `https://app.masterschool.com/campus/multi-choice-question/605eb436-34c0-4f26-8904-1abd637cf0cf` |
| BAA B3 | DE | Modulare Workflows mit Execute Sub-workflow | [open](https://app.notion.com/p/Modulare-Workflows-mit-Execute-Sub-workflow-3819418319f380249c4cda756926d5d1) | `https://app.masterschool.com/campus/multi-choice-question/05540576-106f-4813-9f03-7a5c407ba00e` |
| BAA B3 | EN | Failure Points in n8n Agent Workflows | [open](https://app.notion.com/p/Failure-Points-in-n8n-Agent-Workflows-3669418319f3801f9c87f2dbf7041ddb) | `https://app.masterschool.com/campus/multi-choice-question/830a1d35-bf13-4019-8248-1fae4817685b` |
| BAA B3 | DE | Fehlerquellen in visuellen n8n-Workflows | [open](https://app.notion.com/p/Fehlerquellen-in-visuellen-n8n-Workflows-3789418319f3800190efff70943ef15c) | `https://app.masterschool.com/campus/multi-choice-question/a65adbc7-37b9-45c2-960b-5ed2860ae044` |
| BAA B3 | EN | Reading and Debugging n8n Execution Graphs | [open](https://app.notion.com/p/Reading-and-Debugging-n8n-Execution-Graphs-3669418319f380f0a73ae561f909579a) | `https://app.masterschool.com/campus/multi-choice-question/024e308c-563c-432a-9cd0-d841a8d2d1c3` |
| BAA B3 | DE | n8n-Agenten-Executions lesen und debuggen | [open](https://app.notion.com/p/n8n-Agenten-Executions-lesen-und-debuggen-3789418319f380b5ab69c631970542c0) | `https://app.masterschool.com/campus/multi-choice-question/3ad4810d-8c7e-4506-bbe5-ce3d8073e38a` |
| AAS A3 | EN | From implementation to architecture | [open](https://app.notion.com/p/From-implementation-to-architecture-3849418319f380d487d7ed3b08bbe930) | `https://app.masterschool.com/campus/multi-choice-question/78874726-b1b3-4849-9d34-05cb2f477ad8` |
| AAS A3 | DE | Von der Implementierung zur Architektur | [open](https://app.notion.com/p/Von-der-Implementierung-zur-Architektur-8079418319f3828888ad01c1a02b87cf) | `https://app.masterschool.com/campus/multi-choice-question/ddf7bbc7-2073-4c49-b13c-cdb3cbe4c47a` |
| AAS A3 | EN | Memory and state architecture for the project agent | [open](https://app.notion.com/p/Memory-and-state-architecture-for-the-project-agent-3849418319f380668e31dcae8df69ddf) | `https://app.masterschool.com/campus/multi-choice-question/38babb19-92b3-42b1-8009-bdb33065c098` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/9b0a483c-1200-4f52-acfb-60e0e0ee5e58` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/a76dda8a-9288-430b-8302-346b68a188ef` |
| AAS A3 | DE | Memory- und State-Architektur für den Projektagenten | [open](https://app.notion.com/p/Memory-und-State-Architektur-f-r-den-Projektagenten-e069418319f3822d981b013d9f44d59d) | `https://app.masterschool.com/campus/multi-choice-question/bdfb2cb8-f4dd-4164-8c6a-b14f8713319e` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/299017fa-696d-4573-ae2d-da6a1a0d9335` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/8df46cb0-a9ac-4de3-89ae-3c436cae5831` |

---

## 2. Three draft lessons have no live page

Added to the draft on 20–21 Oct, after the live course was built. Copying content cannot create
them without adding pages, which is outside the rules we agreed, so they are **not** in the live course:

| Group | Lang | New draft lesson | Created |
|---|---|---|---|
| BAA A 2 | DE | [RAG mit dem Projektagenten verbinden](https://app.notion.com/p/RAG-mit-dem-Projektagenten-verbinden-3ff9418319f381419dcae2d22ea09b07) | 2026-10-20 |
| AAS A 3 | EN | [Starting architecture: Vela after Sprint 2](https://app.notion.com/p/Starting-architecture-Vela-after-Sprint-2-4009418319f381abbbdcec8ef4b227cb) | 2026-10-21 |
| AAS A 3 | DE | [Ausgangsarchitektur: Vela nach Sprint 2](https://app.notion.com/p/Ausgangsarchitektur-Vela-nach-Sprint-2-4009418319f381a28492d55b460fa2a9) | 2026-10-21 |

Tell me if you want these created in the live course and I'll add them in the right tree position.

---

## 3. Stale "Chatflow" wording — fix at source

A scan of all 270 live pages for Flowise-era terms found one genuine leftover: **"Chatflow"**,
21 times on 3 pages. These pages are identical in the draft, so the draft never updated them
and the wording needs fixing in both places:

| Group | Lang | Lesson | Hits |
|---|---|---|---|
| BAA A 1 | EN | [Project Introduction](https://app.notion.com/p/Project-Introduction-3669418319f380728775d90452b11fc5) | 8 |
| BAA A 1 | DE | [Projekteinführung](https://app.notion.com/p/Projekteinf-hrung-3779418319f380ba9ff7efc6eaca55d8) | 8 |
| BAA A 1 | DE | [Worauf das hinausläuft — der Contigo-Agent, drei Sprints von jetzt](https://app.notion.com/p/Worauf-das-hinausl-uft-der-Contigo-Agent-drei-Sprints-von-jetzt-3dd9418319f3818fb565fdd3bce7c984) | 5 |

### Checked and fine

- **"Flowise" (11 hits)** — all deliberate contrasts, e.g. *"Do not submit a Flowise canvas"*,
  *"import the saved n8n JSON rather than rebuilding a Flowise canvas"*. Correct as written.
- **"Gemini" (52 hits)** — legitimate: the n8n stack uses the *Embeddings Google Gemini* node and
  `google/gemini-2.5-flash` through OpenRouter. Several hits are explicitly about this
  (*"Using OpenRouter instead of Gemini"*).
- **"Agentflow" (2 hits)** — inside the same deliberate "no Flowise Agentflow is required" sentence.

---

## 4. Still outstanding from earlier runs

- **Module B Sprint field** in Building AI Agents still reads `1-Setting up Flowise and Gemini Stack`
  and `2-Memory Retrieval and Tools in Flowise`. The Notion API cannot rename a select option, so
  this needs 2 clicks in the Notion UI.
- **31 pages** show the default 💡 on callouts that have no icon in the draft (API limit).

## What I did not change

- Sprint 4 in either course
- No pages created, deleted, moved or re-parented; no page IDs or URLs changed
- Sprint / Language / Notes / Translation-review fields untouched
- Neither draft course was modified
