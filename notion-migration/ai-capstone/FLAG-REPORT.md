# AI Capstone Project & Certificate — NOV → live

Source of truth: **AI Capstone Project & Certificate (NOV)**. Destination: the live
**AI Capstone Project & Certificate**. Content only; page IDs and URLs untouched.

| | |
|---|---|
| Lessons in scope | 115 (Module A 83, Module B 32) |
| Bodies replaced | 3 |
| Already identical | 91 |
| Section pages with no body | 21 |
| Verified identical to NOV | **115 / 115** |
| Titles matching NOV | **115 / 115** |
| Pages created / removed | 0 / 0 |
| Errors | 0 |

## Structure: already a 1:1 match

You said pages could be added or removed this time. None were needed — the two courses align
exactly: Module A 83 rows across 4 sprints, Module B 32 rows, every lesson matched by title and
language, and **no** differences in the `Type`, `Order` or `Microsoft Learn` properties or in any
page title. Only three page bodies had actually changed.

| Module | Sprint | Pages | Identical | Section | Replaced |
|---|---|---|---|---|---|
| A | 1 | 25 | 22 | 3 | 1 |
| A | 2 | 17 | 14 | 3 | 0 |
| A | 3 | 27 | 22 | 5 | 0 |
| A | 4 | 14 | 12 | 2 | 2 |
| B | - | 32 | 24 | 8 | 0 |

## The three pages that changed

| Lang | Lesson | Live page | What changed in NOV |
|---|---|---|---|
| EN | What makes a good capstone problem | [open](https://app.notion.com/p/What-makes-a-good-capstone-problem-3e59418319f380c9b37adfa96277b6a5) | The "go to this list" link now points at the live course's own *8 Project Options* page |
| EN | Project submission information | [open](https://app.notion.com/p/Project-submission-information-3f09418319f381539574ea2c09ac3da8) | Capstone broadened from n8n-specific to tool-agnostic; group-project section added; Codio/deadline wording updated |
| DE | Informationen zur Projektabgabe | [open](https://app.notion.com/p/Informationen-zur-Projektabgabe-7669418319f3821da62101eb282bd28a) | Same broadening, plus a full retranslation (`Tutor` for `Instructor`, `Geheimnisse` for `Secrets`, …) |

The submission pages move the capstone from "the exported n8n workflow .json" to "source code,
workflow export or equivalent executable artefact", and add a **Group projects** section stating
that every member submits the same shared package. Worth knowing if the LMS text repeats any of
the old n8n-specific wording.

## Two new cases the tooling had not met before

- **An internal link that is not a mention.** `What makes a good capstone problem` links the words
  "go to this list" to a page by relative URL (`/p/<id>`). Mentions were already remapped to the
  live course; a plain text link was not, so copying it verbatim would have sent live learners into
  the NOV course. Link targets are now remapped too, and the one occurrence resolves to
  *8 Project Options* inside the live course. All 115 pages were scanned: that was the only one,
  and every Microsoft Learn URL is left untouched.
- **Notion rejects its own relative links on create.** The API returns `/p/<id>` on read but
  refuses it on write ("Invalid URL for link"), so links are written as
  `https://app.notion.com/p/<id>` — same destination. The append is atomic, so the page sat
  untouched until the retry. Verification now compares links by target page id, so the URL's
  shape cannot cause a false mismatch.

## Checks

- Row counts unchanged: NOV A 83 / live A 83, NOV B 32 / live B 32
- All 115 live page IDs resolve, none in trash, no URL changed
- On the three rewritten pages nothing was dropped: 0 embeds, 0 bookmarks, 0 images before and after
- No campus quiz embeds anywhere in this course, so none were lost
- No callout-icon deviation on any page — the usual 💡 caveat does not apply here

## What I did not change

- No pages created, deleted, moved or re-parented (none needed)
- Sprint / Language / Notes / Translation review / Type / Order / Microsoft Learn left as they were
- The NOV source course was not modified
