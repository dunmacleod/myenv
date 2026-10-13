# Building AI Agents — Sprint 2 migration (Modules A + B)

Copied verbatim from **Building AI Agents (new, n8n)** into the live **Building AI Agents**, in place.
No pages created, deleted or re-parented — all 50 lesson pages kept their Notion IDs and URLs.
Row counts unchanged (Module A 100, Module B 88).

| | |
|---|---|
| Lessons in scope | 50 (Module A 28, Module B 22) |
| Bodies replaced | 31 |
| Skipped — already identical | 10 |
| Skipped — section pages with no body | 9 |
| Verified identical to source | 19 of 31 (the other 12 differ only by the 💡 below) |
| Images re-hosted | 33 |
| Titles renamed | 13 |
| Quiz embeds removed | 8 |
| Errors | 0 |

---

## 1. Sprints 3 and 4 were NOT migrated — they are still Flowise

You asked for sprints 2–4; only Sprint 2 was ready, so only Sprint 2 was copied. In the draft,
sprints 3 and 4 still hold the old Flowise content, byte-identical to what is already live:

| Module | Sprint | Pages | Differ from live | Draft "Flowise" | Draft "n8n" |
|---|---|---|---|---|---|
| A | 3-Tool Use and Agent Architectures | 21 | 2 | 26 | 0 |
| A | 4-Project Integration and Evaluation | 19 | 2 | 63 | 3 |
| B | 3-Debugging Agents and Platform Landscape | 23 | 0 | 27 | 0 |
| B | 4-Project Finalisation and Comparison | 19 | 1 | 82 | 0 |

Module B Sprint 3 does not differ on a single page. The 5 pages that do differ across sprints 3–4
are not migration work — four differ by exactly one line of text, one is an unrelated content
revision. Re-run this migration for sprints 3–4 once the draft is actually converted.

Two draft titles there still say Flowise and will need fixing at source first:
`Final Flowise and AI Agent Refinement`, `Finales Flowise- und Gemini-Agent-Refinement`.

---

## 2. Quiz embeds removed — re-add in the LMS

| Lang | Lesson | Live page | Removed quiz URL |
|---|---|---|---|
| EN | Knowledge, Routing, and Tool Checkpoint | [open](https://app.notion.com/p/Knowledge-Routing-and-Tool-Checkpoint-3669418319f38029b9d2d38d5810a090) | `https://app.masterschool.com/campus/multi-choice-question/d2e397fd-7cd8-4a6b-b009-9a174bdcde58` |
| EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/dcdf168b-d10d-466f-9844-75122e7371aa` |
| EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/bbf437e5-a345-4223-b038-6b5aad5eb70c` |
| EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/cae71420-03e0-4816-aba3-2615347b6a05` |
| DE | Knowledge-, Routing- und Tool-Checkpoint | [open](https://app.notion.com/p/Knowledge-Routing-und-Tool-Checkpoint-3789418319f380bba119e61b67428cfc) | `https://app.masterschool.com/campus/multi-choice-question/a2d793da-1cdc-4491-bc73-4e23bc27a394` |
| DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/cf122919-e2a5-4017-b4ee-2676196127dc` |
| DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/4f051afc-a81c-43ea-8031-35ebfba3286c` |
| DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/6bfb0274-91f2-419d-87df-591fb169f478` |

Module A Sprint 2 lost none — these 8 are all on the Module B checkpoint lesson.

---

## 3. Titles renamed

Page IDs unchanged, so links still resolve; the URL slug now reflects the new title.

| Module | Lang | Was (live) | Now |
|---|---|---|---|
| A | EN | How the Conversational Retrieval QA Chain Improves on Basic RAG | **How Conversational Retrieval Improves Basic RAG** |
| A | DE | Wie die Conversational Retrieval QA Chain Basic RAG verbessert | **Wie konversationelles Retrieval einfaches RAG verbessert** |
| B | EN | Building Meridian's Document Store | **Building Meridian's Retrieval Knowledge Base** |
| B | DE | Meridians Document Store bauen | **Meridians Retrieval-Wissensbasis aufbauen** |
| B | EN | Retrieval in Flowise | **Retrieval in n8n** |
| B | EN | Connecting the Document Store to the Agent Node    | **Connecting Qdrant Retrieval to the n8n AI Agent** |
| B | DE | Den Document Store mit dem Agent Node verbinden | **Qdrant-Retrieval mit dem n8n AI Agent verbinden** |
| B | EN | Conditional Routing with the Condition Node | **Deterministic Routing with Switch** |
| B | DE | Bedingtes Routing mit dem Condition Node | **Deterministisches Routing mit Switch** |
| B | EN | AI-Driven Routing with the Condition Agent Node | **AI-Driven Routing with Basic LLM Chain** |
| B | DE | AI-gestütztes Routing mit dem Condition Agent Node | **KI-gestütztes Routing mit Basic LLM Chain** |
| B | EN | Connecting the HTTP Node for Live Data Lookup  | **Connecting HTTP Request for Mock Status Data** |
| B | DE | Den HTTP Node für Live-Datenabfragen verbinden | **HTTP Request für Mock-Statusdaten verbinden** |

---

## 4. Module B Sprint field could not be renamed — needs 2 clicks in Notion

The live Module B `Sprint` options still read:

- `1-Setting up Flowise and Gemini Stack` → should be `1-Setting up n8n and OpenRouter Stack`
- `2-Memory Retrieval and Tools in Flowise` → should be `2-Memory Retrieval and Tools in n8n`

**The Notion API cannot rename an existing select option.** It accepts the request and silently
ignores the new name. Please rename both in the Notion UI (click the Sprint property → edit the
option name); that relabels every row in the sprint at once.

While establishing this I omitted the two other options from a schema update, which deleted them
and cleared the Sprint value on 41 rows (all of sprints 3 and 4). I restored the options and every
row's original value from the pre-change snapshot and matched the option colours to the draft;
a row-by-row comparison against the snapshot shows 0 differences. No page content was involved.

---

## 5. Remaining "Flowise" in live Sprint 2 — intentional, no action

A full re-scan of all 50 live Sprint 2 pages (titles, body, tables, captions, link URLs) found
4 mentions, all deliberate contrasts with the old tool, copied as written:

- [B EN] [What is a Document Store?](https://app.notion.com/p/What-is-a-Document-Store-3669418319f3804497d0d4e89886eea3) — "…In n8n, a searchable knowledge base is built from connected components rather than a single Flowise Document S…"
- [B DE] [Was ist ein Document Store?](https://app.notion.com/p/Was-ist-ein-Document-Store-3789418319f3803fbd05f2757fec58e8) — "…In n8n entsteht eine durchsuchbare Wissensbasis aus mehreren verbundenen Komponenten, nicht über eine zentrale…"
- [B EN] [Connecting Qdrant Retrieval to the n8n AI Agent](https://app.notion.com/p/Connecting-Qdrant-Retrieval-to-the-n8n-AI-Agent-3669418319f38072beffe31abfa04d3b) — "…Open the n8n instance and the Sprint 1 workflow Meridian Base Agent. Preserve its trigger, configured model, c…"
- [B DE] [Qdrant-Retrieval mit dem n8n AI Agent verbinden](https://app.notion.com/p/Qdrant-Retrieval-mit-dem-n8n-AI-Agent-verbinden-3789418319f380d498f5e9d78796669d) — "…Öffne Meridian Base Agent aus Sprint 1 in n8n. Behalte Trigger, Modell, Credentials, Session-Konfiguration und…"

---

## 6. Known cosmetic deviation (Notion API limit)

14 callouts across 12 pages had no icon in the draft; the API cannot create an icon-less callout and
forces the default 💡. Everything else on these pages matched the source exactly.

- A EN [Embeddings and vector search](https://app.notion.com/p/Embeddings-and-vector-search-3669418319f380d79dc8ccf39464760e) — 1 callout(s)
- A DE [Embeddings und Vektorsuche](https://app.notion.com/p/Embeddings-und-Vektorsuche-3779418319f38013997fe17ca65932d7) — 1 callout(s)
- A EN [Evidence-aware answers](https://app.notion.com/p/Evidence-aware-answers-3669418319f38001a4a2eeee3cca18a2) — 2 callout(s)
- A DE [Evidenzbewusste Antworten](https://app.notion.com/p/Evidenzbewusste-Antworten-3779418319f3803fb21dd4f050ded665) — 2 callout(s)
- A EN [RAG pipeline end to end](https://app.notion.com/p/RAG-pipeline-end-to-end-3669418319f38049a2bbf927ce4674fc) — 1 callout(s)
- A DE [RAG-Pipeline Ende-zu-Ende](https://app.notion.com/p/RAG-Pipeline-Ende-zu-Ende-3779418319f380fcb1e3f471e340e2d6) — 1 callout(s)
- A EN [How Conversational Retrieval Improves Basic RAG](https://app.notion.com/p/How-Conversational-Retrieval-Improves-Basic-RAG-3669418319f3803c83e4e02a37a62745) — 1 callout(s)
- A DE [Wie konversationelles Retrieval einfaches RAG verbessert](https://app.notion.com/p/Wie-konversationelles-Retrieval-einfaches-RAG-verbessert-3779418319f380e981a3d7b1f5a3c303) — 1 callout(s)
- B EN [What is a Document Store?](https://app.notion.com/p/What-is-a-Document-Store-3669418319f3804497d0d4e89886eea3) — 1 callout(s)
- B DE [Was ist ein Document Store?](https://app.notion.com/p/Was-ist-ein-Document-Store-3789418319f3803fbd05f2757fec58e8) — 1 callout(s)
- B EN [System Prompt Best Practices for a Multi-Capability Agent](https://app.notion.com/p/System-Prompt-Best-Practices-for-a-Multi-Capability-Agent-3669418319f38017aac3cc562b931472) — 1 callout(s)
- B DE [System-Prompt-Best-Practices für einen Multi-Capability-Agenten](https://app.notion.com/p/System-Prompt-Best-Practices-f-r-einen-Multi-Capability-Agenten-3789418319f3805aaabdeebd26fa7da6) — 1 callout(s)

## What I did not change

- Sprints 1, 3 and 4 page content untouched
- No pages created, deleted, moved or re-parented; no page IDs or URLs changed
- Sprint/Language/Notes/Translation-review fields untouched (beyond the restore described above)
- The draft (new, n8n) course was not modified
