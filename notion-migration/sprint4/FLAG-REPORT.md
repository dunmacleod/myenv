# Sprint 4 migration + full sync check (all sprints, both modules, both courses)

## Part 1 — Sprint 4 migrated

Sprint 4 was ready in both drafts (zero "Flowise" mentions, 334 "n8n"), unlike on 13 Oct.

| | |
|---|---|
| Lessons in scope | 65 |
| Bodies replaced | 50 |
| Already identical / section pages | 4 / 11 |
| Verified identical to source | 32 of 50 (18 differ only by the forced 💡) |
| Images re-hosted | 25 |
| Titles renamed | 6 |
| Quiz embeds removed | 24 |
| Errors | 0 |

Two things needed handling that had not come up before:

- **A synced block.** `Den Baseline-Projektagenten neu entwerfen` (AAS A4 DE) contains an *original*
  synced block. Deleting an original breaks every page mirroring it, so before touching the page I
  scanned all 335 live pages in both courses for mirrors — found **none** — then recreated it as an
  original with its 6 children intact. A mirror pointing into the draft would have been copied as
  inline content instead, never as a live→draft link.
- **A column-width bug.** Two pages have columns whose `width_ratio` reads back as `1`, which the
  API rejects on create. The append is atomic, so both pages were left untouched rather than half
  written; I fixed the builder to omit a ratio outside (0,1) and re-ran them successfully.

---

## Part 2 — Full sync check

All 335 lesson pages across sprints 1–4, both modules, both courses, re-read from Notion and
compared block by block against their draft counterpart. **Titles: 335/335 match the draft.**

| Course | Module | Sprint | Pages | Identical | Icon-only | Section | **Out of sync** |
|---|---|---|---|---|---|---|---|
| Advanced Agent Systems | A | 1 | 27 | 23 | 2 | 2 | **0** |
| Advanced Agent Systems | A | 2 | 18 | 8 | 0 | 4 | **6** |
| Advanced Agent Systems | A | 3 | 17 | 14 | 0 | 3 | **0** |
| Advanced Agent Systems | A | 4 | 12 | 4 | 6 | 2 | **0** |
| Advanced Agent Systems | B | 1 | 18 | 15 | 0 | 3 | **0** |
| Advanced Agent Systems | B | 2 | 20 | 5 | 0 | 3 | **12** |
| Advanced Agent Systems | B | 3 | 20 | 14 | 0 | 4 | **2** |
| Advanced Agent Systems | B | 4 | 15 | 10 | 2 | 3 | **0** |
| Building AI Agents | A | 1 | 32 | 16 | 0 | 4 | **12** |
| Building AI Agents | A | 2 | 28 | 5 | 0 | 5 | **18** |
| Building AI Agents | A | 3 | 21 | 6 | 0 | 5 | **10** |
| Building AI Agents | A | 4 | 19 | 12 | 4 | 3 | **0** |
| Building AI Agents | B | 1 | 24 | 20 | 0 | 4 | **0** |
| Building AI Agents | B | 2 | 22 | 14 | 4 | 4 | **0** |
| Building AI Agents | B | 3 | 23 | 18 | 1 | 4 | **0** |
| Building AI Agents | B | 4 | 19 | 10 | 6 | 3 | **0** |
| **Total** | | | **335** | **194** | **25** | **56** | **60** |

**Sprint 4 is fully in sync in all four modules.** So are BAA module B (all sprints), AAS A1, A3, A4,
B1 and B4. The 60 out-of-sync pages are all in sprints 1–3 and have one cause, below.

---

## Part 3 — Why 60 pages drifted: the draft is replacing campus quizzes with inline toggles

These pages were in sync on 22 Oct. The drafts were edited on **27 Oct** — after the last run — and
the change is systematic: each Masterschool campus quiz embed is being replaced by an inline
**"Expected answer"** toggle inside the same callout.

```
DRAFT  callout → toggle  "Expected answer: Conversation memory is absent, disconnected, …"
LIVE   callout → embed   app.masterschool.com/campus/multi-choice-question/82fea941-…
```

Scale across all 335 pages:

| | Live now | Draft |
|---|---|---|
| Campus quiz embeds | 108 | 8 |
| "Expected answer" toggles | 21 | 121 |

The draft's conversion is all but finished — only **8 campus embeds remain on 5 draft pages**
(Building AI Agents module B, sprints 2 and 3).

**Syncing these 60 pages would remove 100 graded campus quizzes from the two live courses and add
102 self-check toggles in their place, 1:1.** That is a change to how students are assessed, not a
wording fix, so I have not done it. It is one run away if you want it:

| Group | Pages | Campus quizzes removed | Answer toggles added |
|---|---|---|---|
| AAS A 2 | 6 | 18 | 18 |
| AAS B 2 | 12 | 12 | 12 |
| AAS B 3 | 2 | 10 | 10 |
| BAA A 1 | 12 | 22 | 24 |
| BAA A 2 | 18 | 28 | 28 |
| BAA A 3 | 10 | 10 | 10 |

---

## Part 4 — Sprint 4 follow-ups

### A German page that is not a translation of its English counterpart

`Project submission instructions` / `Anweisungen zur Projektabgabe` (AAS A4):

| | EN | DE |
|---|---|---|
| Draft | 2243 words, 19 headings | **755 words, 9 headings** |
| Live before this run | 2247 words, 19 headings | 2118 words, 19 headings |

The live German page mirrored the English structure heading for heading. The draft's German page is
a different, much shorter document. Copied as instructed, so German students now see the shorter
version. Say the word and I will restore the previous page from the backup in one step:
`notion-migration/sprint4/backup/A-DE-Anweisungen zur Projektabgabe.json`.

### Quiz embeds removed in sprint 4

| Group | Lang | Lesson | Live page | Removed quiz URL |
|---|---|---|---|---|
| BAA A4 | EN | Memory failure modes | [open](https://app.notion.com/p/Memory-failure-modes-3689418319f38038a198f71f24e73b97) | `https://app.masterschool.com/campus/multi-choice-question/8aa70d13-eda3-4353-9080-314102a78ce5` |
| BAA A4 | DE | Memory-Fehlermodi | [open](https://app.notion.com/p/Memory-Fehlermodi-3779418319f380228235d01653b2ccb6) | `https://app.masterschool.com/campus/multi-choice-question/7a61dd91-7c71-40b6-9765-f8e96a143807` |
| BAA A4 | EN | Context drift and content exhaustion | [open](https://app.notion.com/p/Context-drift-and-content-exhaustion-3689418319f3802086c3db115a057add) | `https://app.masterschool.com/campus/multi-choice-question/f7cfc817-3fd5-46d1-a0c9-38470991ad6d` |
| BAA A4 | DE | Context Drift und Content Exhaustion | [open](https://app.notion.com/p/Context-Drift-und-Content-Exhaustion-3779418319f380bc9051d53cee09bb6a) | `https://app.masterschool.com/campus/multi-choice-question/b4e0fe40-67ac-4a34-895d-ffd339abca8e` |
| BAA A4 | EN | Observability and system monitoring | [open](https://app.notion.com/p/Observability-and-system-monitoring-3689418319f38081b3d7ef6aecb87e05) | `https://app.masterschool.com/campus/multi-choice-question/8bc261ae-db3c-4c44-b9fd-3ddd0f610db5` |
| BAA A4 | DE | Observability und System-Monitoring | [open](https://app.notion.com/p/Observability-und-System-Monitoring-3779418319f38082a41ed363c770b3cb) | `https://app.masterschool.com/campus/multi-choice-question/9a613b62-933a-4b64-a90a-62af242f1e10` |
| BAA B4 | EN | From Self-Hosted Prototype to Business Use | [open](https://app.notion.com/p/From-Self-Hosted-Prototype-to-Business-Use-3669418319f380f0a769ed717428a0cb) | `https://app.masterschool.com/campus/multi-choice-question/6793a920-9d85-4892-ae0f-7f65261f469e` |
| BAA B4 | DE | Vom selbst gehosteten Prototyp zur Business-Nutzung | [open](https://app.notion.com/p/Vom-selbst-gehosteten-Prototyp-zur-Business-Nutzung-3789418319f380a6beb0c485db48fab7) | `https://app.masterschool.com/campus/multi-choice-question/6f20925d-9839-4fb9-b0f3-e9dc4ac53d65` |
| BAA B4 | EN | Security, Privacy, and Validity in Agent Design | [open](https://app.notion.com/p/Security-Privacy-and-Validity-in-Agent-Design-3669418319f380fda07ee8379fc625de) | `https://app.masterschool.com/campus/multi-choice-question/8a5ca417-7e56-4867-9472-88e996288bbe` |
| BAA B4 | DE | Security, Privacy und Validity im Agent Design | [open](https://app.notion.com/p/Security-Privacy-und-Validity-im-Agent-Design-3789418319f38092959df9a7262eacce) | `https://app.masterschool.com/campus/multi-choice-question/3c0179c0-8e98-44c5-9545-ada581b1cd38` |
| BAA B4 | EN | Final n8n Agent Refinement | [open](https://app.notion.com/p/Final-n8n-Agent-Refinement-3689418319f380b795cfcdc8121fc01a) | `https://app.masterschool.com/campus/multi-choice-question/a165dd15-e308-484d-b13c-909a03b6f678` |
| BAA B4 | DE | Finales n8n-Agent-Refinement | [open](https://app.notion.com/p/Finales-n8n-Agent-Refinement-3789418319f38092aeb2e5f36bfad5bf) | `https://app.masterschool.com/campus/multi-choice-question/b7bf43f1-e18b-49e3-838e-daa0917e349e` |
| BAA B4 | EN | Business Readiness Checklist | [open](https://app.notion.com/p/Business-Readiness-Checklist-37d9418319f3802685fbdf88a52be4dd) | `https://app.masterschool.com/campus/multi-choice-question/e6d2648c-f9ae-42cb-9f82-ab2f9a761a9a` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/f22f6255-0a2a-4ba9-aeab-9ea302152cc4` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/bce9c482-6bdb-4fdb-9b47-1fa79b85b2f3` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/e9eaea9b-a5d5-4e4c-b832-589846ad3f38` |
| BAA B4 | DE | Business-Readiness-Checkliste | [open](https://app.notion.com/p/Business-Readiness-Checkliste-3829418319f3802fb41acad446f3f576) | `https://app.masterschool.com/campus/multi-choice-question/3399902e-02c5-43a4-87e8-cf752383465c` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/8529c2fa-c306-4c9b-88d0-9186e246a3a6` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/b2a38d37-2be3-4b4a-a32e-6a078e7496ec` |
|  |  |  |  | `https://app.masterschool.com/campus/multi-choice-question/8de67070-5436-4f75-9a1e-dc9156ba7a1e` |
| AAS A4 | EN | Testing the new architecture | [open](https://app.notion.com/p/Testing-the-new-architecture-3849418319f38076bd78ec162aaa9e53) | `https://app.masterschool.com/campus/multi-choice-question/22197d44-c088-4541-88eb-66027537237c` |
| AAS A4 | DE | Die neue Architektur testen | [open](https://app.notion.com/p/Die-neue-Architektur-testen-e079418319f382adaf44812c29641c55) | `https://app.masterschool.com/campus/multi-choice-question/95bd7017-0be5-46c8-92ca-874dd2bd545a` |
| AAS B4 | EN | End-to-end failure analysis | [open](https://app.notion.com/p/End-to-end-failure-analysis-38b9418319f380b0a53cd100ab6dc356) | `https://app.masterschool.com/campus/multi-choice-question/4f6e2a84-6afc-4ccf-a0f7-e284056c58b8` |
| AAS B4 | DE | End-to-End-Fehleranalyse | [open](https://app.notion.com/p/End-to-End-Fehleranalyse-3969418319f38376a6e801ed03b0b4af) | `https://app.masterschool.com/campus/multi-choice-question/0a2b5430-6522-4a87-b519-d975b88ef232` |

### Titles renamed in sprint 4

| Group | Lang | Was | Now |
|---|---|---|---|
| BAA A4 | EN | Making your Chatflow Public | **Making your n8n Agent Public** |
| BAA A4 | DE | Deinen Chatflow öffentlich machen | **Deinen n8n-Agenten öffentlich machen** |
| BAA A4 | EN | Polishing the Chatflow | **Polishing the n8n Agent** |
| BAA B4 | EN | Final Flowise and AI Agent Refinement | **Final n8n Agent Refinement** |
| BAA B4 | DE | Finales Flowise- und Gemini-Agent-Refinement | **Finales n8n-Agent-Refinement** |
| AAS A4 | DE | Anleitung zur Projektabgabe | **Anweisungen zur Projektabgabe** |

---

## Part 5 — Still outstanding

- **Module B Sprint field** (Building AI Agents) still reads `1-Setting up Flowise and Gemini Stack`
  and `2-Memory Retrieval and Tools in Flowise`. The Notion API cannot rename a select option —
  2 clicks in the Notion UI.
- **Three draft lessons have no live page** and so cannot be synced without creating pages:
  - BAA A 2 [DE] [RAG mit dem Projektagenten verbinden](https://app.notion.com/p/RAG-mit-dem-Projektagenten-verbinden-3ff9418319f381419dcae2d22ea09b07) — added 2026-10-20
  - AAS A 3 [EN] [Starting architecture: Vela after Sprint 2](https://app.notion.com/p/Starting-architecture-Vela-after-Sprint-2-4009418319f381abbbdcec8ef4b227cb) — added 2026-10-21
  - AAS A 3 [DE] [Ausgangsarchitektur: Vela nach Sprint 2](https://app.notion.com/p/Ausgangsarchitektur-Vela-nach-Sprint-2-4009418319f381a28492d55b460fa2a9) — added 2026-10-21
- **"Chatflow"** still appears 21 times on 3 Building AI Agents A1 pages; identical in the draft,
  so it needs fixing at source.
- **25 pages** show Notion's default 💡 on callouts that have no icon in the draft (API limit).

## What I did not change

- The 60 drifted pages in sprints 1–3 (awaiting your call on the quiz change)
- No pages created, deleted, moved or re-parented; all 335 page IDs and URLs unchanged
- Live row counts unchanged; Sprint / Language / Notes / Translation-review fields untouched
- Neither draft course was modified
