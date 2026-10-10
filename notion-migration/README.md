# n8n course migration (Notion)

Copies lesson content from the **(new, n8n)** draft courses into the corresponding **live** courses,
in place, so that the live courses keep their page addressing.

| Draft (source) | Live (target) | Sprint |
|---|---|---|
| Building AI Agents (new, n8n) | Building AI Agents | Module A `1-How Agents Remember`, Module B `1-Setting up Flowise and Gemini Stack` |
| Advanced Agent Systems (new, n8n) | Advanced Agent Systems | Module A `Sprint 1: Agent Architecture Foundations`, Module B `Sprint1: Agent Communication & Integration Protocols` |

See [FLAG-REPORT.md](FLAG-REPORT.md) for what needs follow-up in the LMS.

## How it works

The draft and live courses are structural twins: same databases, same row counts, same
`Parent item`/`Sub-item` tree. Lessons are therefore matched **by position in that tree**, not by
title (titles diverge, e.g. `The Flowise Interface` → `The n8n Interface`).

Per lesson:

1. Back up the live page (`backup/*.json` verbatim blocks, `backup/*.md` readable).
2. Build the new content from the draft page, re-uploading every image into the live workspace
   (draft images are Notion-hosted behind URLs that expire within the hour, so they cannot be
   referenced — they are downloaded and uploaded as new files).
3. **Append** the new content, then **delete** the old blocks. In that order, so the page is never
   empty if the run is interrupted.
4. Rename the page if the draft title differs.
5. Re-read the page and compare it structurally against the draft; record any difference.

Nothing is created, deleted, moved or re-parented, so every page ID and URL survives.

### Internal cross-links

Advanced Agent Systems content contains 117 page mentions pointing at other lessons. Copied
verbatim these would send live students into the draft course, so each is remapped to the live
equivalent via `mention-remap.json` (built from the positional mapping). All 117 resolved.

### Known limitation

The Notion API cannot create a callout without an icon — it forces the default 💡. Three callouts
across both courses were icon-less in the draft and now show 💡. This is the only deviation found;
everything else verified byte-for-byte on the normalised block tree.

## Rollback

`backup/<module>-<lang>-<title>.json` holds the exact pre-migration blocks of each replaced page.
Notion's own page history also covers it. Re-running is safe: `run-state.json` records what was
already done per page.

## Files

- `tools/notionmig.py` — Notion client, block reader, structural normaliser, payload builder
- `tools/runner.py` — per-page orchestration with resumable state
- `<course>/mapping.json` — draft→live lesson mapping by tree position
- `<course>/plan.json` — per-lesson action (`rewrite` / `skip-identical` / `skip-empty-container`)
- `<course>/run-state.json`, `<course>/run.log` — what the run actually did
