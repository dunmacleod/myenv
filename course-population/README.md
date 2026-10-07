# Course population — Anatomy of an AI Application (Module B)

Target LMS course: `04a68c69-34a2-4bad-ad4a-df814fef79e4` (version 1.1)
Backoffice editor: `https://lms.masterschool.com/course-edit/<courseId>?majorVersion=1&editorTab=content`

## What this is

`ls-manifest.csv` is the populate-ready payload for the 16 live sessions of this
course: one row per LS, with the fields the MS BackOffice content editor expects.

| column | maps to editor field |
|---|---|
| `ls` | ordering only (not entered) |
| `sprint` | which sprint block the element belongs to |
| `name` | element title |
| `duration_min` | renders as `Live Session · 45 mins` |
| `deck` | Google Slides link |
| `plan` | Notion LS (lesson plan) link |

## Field shape

Confirmed against the already-populated sibling course
(`d1da346c-4f30-4f96-87b4-99998aa8abfe`), whose elements read back as:

```
{"name": "...", "deck": "https://docs.google.com/presentation/d/...",
 "plan": "https://www.notion.so/masterschool/...", "t": "45"}
```

Notes carried over from that course:
- `plan` uses the `www.notion.so/masterschool/...` host, not `app.notion.com/p/...`.
- Deck URLs are stored clean — no `?usp=drivesdk` or `ouid=` query parameters.
- Sessions without a deck (there, `Code Clinic`) leave `deck` empty rather than
  pointing at a placeholder. Here that applies to LS15 and LS16.

## Consistency checks

- 16 rows, 16 unique Notion plan links, 14 unique deck links.
- 4 sprints x 4 sessions x 45 min = **3h 0m per sprint**, matching the
  `Live sessions / 3h 0m` subtotals rendered in the sibling course.

## Provenance

- Deck links: Google Drive, native Slides in folder
  `1FJ1RpgMSLhZJeG3JPw8cNJikcmET_Hd3`. The `.pptx` exports (EN/DE) live
  elsewhere in Drive and are **not** what the editor links to.
- Plan links: the LS list for this course.
- LS15 (Presentation Day) and LS16 (Code Clinic) have no deck in Drive.
  Treated as intentional, per the sibling course. Confirm before entering.

## Still to confirm

- Whether LS15/LS16 should carry a deck in this course.
- The `appnotion` flag seen on the sibling course's LS1 (`false`) — purpose
  unknown, not represented here.
- Whether sprint blocks already exist in the target course or need creating.
