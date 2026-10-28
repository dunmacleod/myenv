# Quiz-format sync + German retranslation — final state

Follows the sprint 4 migration. Two things were asked for and both are done; the whole
corpus was then re-verified end to end.

## Final sync state — all 335 pages, sprints 1–4, both modules, both courses

| Course | Module | Sprint | Pages | Identical | Icon-only | Section | Differ |
|---|---|---|---|---|---|---|---|
| Advanced Agent Systems | A | 1 | 27 | 23 | 2 | 2 | 0 |
| Advanced Agent Systems | A | 2 | 18 | 8 | 6 | 4 | 0 |
| Advanced Agent Systems | A | 3 | 17 | 14 | 0 | 3 | 0 |
| Advanced Agent Systems | A | 4 | 12 | 3 | 6 | 2 | 1 |
| Advanced Agent Systems | B | 1 | 18 | 15 | 0 | 3 | 0 |
| Advanced Agent Systems | B | 2 | 20 | 5 | 12 | 3 | 0 |
| Advanced Agent Systems | B | 3 | 20 | 14 | 2 | 4 | 0 |
| Advanced Agent Systems | B | 4 | 15 | 10 | 2 | 3 | 0 |
| Building AI Agents | A | 1 | 32 | 16 | 12 | 4 | 0 |
| Building AI Agents | A | 2 | 28 | 5 | 18 | 5 | 0 |
| Building AI Agents | A | 3 | 21 | 6 | 10 | 5 | 0 |
| Building AI Agents | A | 4 | 19 | 12 | 4 | 3 | 0 |
| Building AI Agents | B | 1 | 24 | 20 | 0 | 4 | 0 |
| Building AI Agents | B | 2 | 22 | 14 | 4 | 4 | 0 |
| Building AI Agents | B | 3 | 23 | 18 | 1 | 4 | 0 |
| Building AI Agents | B | 4 | 19 | 10 | 6 | 3 | 0 |
| **Total** | | | **335** | **193** | **85** | **56** | **1** |

**334 of 335 pages carry the draft's content. Titles match the draft 335/335.**

"Icon-only" means the page matches except that icon-less callouts show Notion's default 💡,
which the API cannot omit — 85 pages, up from 25, because the new answer-toggle callouts
have no icon in the draft.

The single remaining difference is deliberate — see part 2.

---

## Part 1 — Campus quizzes replaced by inline answer toggles

Approved: sync all 60 drifted pages. The drafts had replaced each Masterschool campus quiz
embed with an inline **"Expected answer"** toggle in the same callout; that is now live.

| Group | Pages | Campus quizzes removed | Answer toggles added |
|---|---|---|---|
| AAS A2 | 6 | 18 | 18 |
| AAS B2 | 12 | 12 | 12 |
| AAS B3 | 2 | 10 | 10 |
| BAA A1 | 12 | 22 | 22 |
| BAA A2 | 18 | 28 | 28 |
| BAA A3 | 10 | 10 | 10 |
| **Total** | **60** | **100** | **100** |

A clean 1:1 swap: 100 out, 100 in, 80 images re-hosted, 0 errors, and no deviation beyond
the forced 💡. **Every removed quiz URL is recorded** in `removed-campus-quizzes.json` and in
the per-page backups, so the decision is reversible.

Campus quiz embeds across the two live courses: **108 before → 8 now**. The remainder sit on
pages the drafts have not converted yet (8 of them are still campus embeds in the draft itself,
on 5 Building AI Agents module B pages), so they will come across when the drafts are finished.

---

## Part 2 — `Anweisungen zur Projektabgabe` retranslated

Approved: retranslate the German page to par with the current English, rather than keep the
draft's shorter document.

| | EN (draft) | DE (live, now) | DE (draft) |
|---|---|---|---|
| Blocks | 117 | **117** | 39 |
| Words | 2246 | **2145** | 755 |
| Headings | 19 | **19** | 9 |

Method: the previous live German page was a faithful translation of this lesson, so it was
restored from the migration backup and only the blocks whose **English** had changed were
retranslated. The English delta between the old live version and the current draft is exactly
**six blocks**, all Flowise/Agentflow → n8n rewrites; everything else was already at par. That
preserves the approved translation instead of regenerating 2200 words.

Done under the `ms-lesson-translate` house standard, with the full self-check and a term log in
`notion-migration/translations/AAS-A4-Anweisungen-zur-Projektabgabe.md`. Result: block-type
identical to the English page, zero `Flowise`/`Agentflow`/`Chatflow` left, `du` throughout,
no `KI`, and terminology swept for split forms (Workflow, Credentials, Reviewer, Execution).

**The skill said the house standard was formal `Sie`.** Per your correction it now reads
informal **du**, in `SKILL.md` and in the two SQL UI strings in `dictionary.md` that encoded
the formal form. Note it is an org-synced skill, so a future sync may overwrite that edit.

**This page is now intentionally out of sync with the draft** — it is the one `Differ` above.
The draft still holds the 755-word document, so the next sprint 4 sync would overwrite the
German page again unless the draft is updated first. I have not touched either draft course.

---

## Still outstanding

- **Module B Sprint field** (Building AI Agents) still reads `1-Setting up Flowise and Gemini
  Stack` and `2-Memory Retrieval and Tools in Flowise`. The Notion API cannot rename a select
  option — 2 clicks in the Notion UI.
- **Three draft lessons have no live page**, so they cannot be synced without creating pages:
  - BAA A 2 [DE] [RAG mit dem Projektagenten verbinden](https://app.notion.com/p/RAG-mit-dem-Projektagenten-verbinden-3ff9418319f381419dcae2d22ea09b07) — added 2026-10-20
  - AAS A 3 [EN] [Starting architecture: Vela after Sprint 2](https://app.notion.com/p/Starting-architecture-Vela-after-Sprint-2-4009418319f381abbbdcec8ef4b227cb) — added 2026-10-21
  - AAS A 3 [DE] [Ausgangsarchitektur: Vela nach Sprint 2](https://app.notion.com/p/Ausgangsarchitektur-Vela-nach-Sprint-2-4009418319f381a28492d55b460fa2a9) — added 2026-10-21
- **"Chatflow"** still appears 21 times on 3 Building AI Agents A1 pages; identical in the draft,
  so it needs fixing at source.
- **The draft's German `Anweisungen zur Projektabgabe`** needs the real translation applied at
  source; say the word and I will push the version now live into the draft.
- **85 pages** show the default 💡 on icon-less callouts (Notion API limit).

## What I did not change

- No pages created, deleted, moved or re-parented; all 335 page IDs and URLs unchanged
- Live row counts unchanged; Sprint / Language / Notes / Translation-review fields untouched
- Neither draft course was modified
