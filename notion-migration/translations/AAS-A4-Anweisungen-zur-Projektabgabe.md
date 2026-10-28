# Translation log — `Anweisungen zur Projektabgabe`

Advanced Agent Systems · Module A · Sprint 4 · DE
Source: `Project submission instructions` (EN draft)
Date: 2026-10-28 · Standard: `ms-lesson-translate`

## Why this page was handled by hand

The sprint 4 sync copied the draft's German page verbatim, as instructed. That draft page
is **not a translation of its English counterpart** — it is a different, much shorter
document (755 words / 9 headings against the English 2243 / 19). The live page it replaced
*was* a faithful translation, mirroring the English heading for heading.

Rather than translate 2243 words from scratch, the previous German page was restored from
the migration backup and only the blocks whose **English** had changed were retranslated.
The English delta between the old live version and the current draft is exactly six blocks,
all of them Flowise/Agentflow → n8n rewrites. Everything else was already at par.

Result: 117 blocks, block-type identical to the English page, 2145 words against 2246.

## The six retranslated blocks

| # | Type | English (current draft) | German |
|---|---|---|---|
| 9 | bulleted_list_item | Implementing the design as n8n workflows and testing it against the failure modes you designed for | Das Design als n8n-Workflows implementieren und gegen die Fehlermodi testen, für die du es entworfen hast |
| 21 | bulleted_list_item | The final parent and specialist n8n workflow JSON exports … together with a dependency list (models, credentials, services, and sub-workflows) … | Die finalen JSON-Exporte des Parent- und der Spezialisten-Workflows in n8n … zusammen mit einer Abhängigkeitsliste (Modelle, Credentials, Services und Sub-Workflows) … |
| 47 | paragraph | A live run of the redesigned n8n workflow(s). Show which nodes executed, how classification and specialist handoff worked … | Ein Live-Lauf der neu entworfenen n8n-Workflows. Zeige, welche Nodes ausgeführt wurden, wie die Klassifizierung und der Handoff an die Spezialisten funktioniert haben … |
| 77 | to_do | Parent and specialist n8n workflow JSON exports checked for importability, with dependencies documented and credentials excluded | JSON-Exporte des Parent- und der Spezialisten-Workflows auf Importierbarkeit geprüft, mit dokumentierten Abhängigkeiten und ohne Credentials |
| 91 | numbered_list_item | Downloaded n8n JSON exports for all workflows involved, or a reviewer-accessible n8n instance link. A localhost URL is not externally accessible. | Heruntergeladene n8n-JSON-Exporte aller beteiligten Workflows, oder ein Link auf eine n8n-Instanz, die für den Reviewer zugänglich ist. Eine localhost-URL ist von außen nicht erreichbar. |
| 109 | bulleted_list_item | Does every field passed between workflows appear in your specification, with a defined writer and reader? | Erscheint jedes Feld, das zwischen Workflows übergeben wird, in deiner Spezifikation — mit festgelegtem Schreiber und Leser? |

## Terms kept English, with article (rule 12)

| Term | Form used | Why |
|---|---|---|
| Workflow | **der** Workflow, pl. die Workflows | Already in dictionary §2 |
| Sub-Workflow | **das** Sub-Workflow, pl. die Sub-Workflows | Matches the n8n node name `Execute Sub-workflow` used in the course |
| Credentials | **die** Credentials (pl.) | n8n UI label; the course's German pages already use it (`Qdrant- und Google-Gemini-Credentials`) |
| Execution / Execution-Daten | **die** Execution, pl. die Executions | Course corpus: `n8n-Agenten-Executions lesen und debuggen` |
| Handoff | **der** Handoff | Course corpus: `Nachrichtenweitergabe und Handoff-Verträge` |
| Reviewer | **der** Reviewer | Already used in the page's existing German |
| Node | **der** Node, pl. die Nodes | Course corpus throughout |
| Canvas | **die** Canvas | Retained only where the English deliberately contrasts it ("on one canvas") |
| `localhost` | verbatim | Rule 6 — technical literal |

New dictionary candidates from this page: `Sub-Workflow`, `Credentials`, `Execution`,
`Handoff`, `Node`, `Reviewer`, `Abhängigkeitsliste` (dependency list),
`Importierbarkeit` (importability).

## Self-check

- Rule 1 — German throughout; English retained only per the table above
- Rule 2 — no `KI`; 0 occurrences
- Rule 4 — 117 blocks, block types identical to the English page
- Rule 6 — `localhost` unchanged
- Rule 7 — numbering untouched
- Rule 11 — no false friends; no `Brief` (the page says `Briefing` where relevant)
- Rule 13 — headings in sentence case, unchanged from the approved translation
- Rule 14 — no calqued verbs; `entworfen` not `designt`
- Rule 15 — swept: Workflow/Arbeitsablauf, Credentials/Zugangsdaten, Reviewer/Prüfer,
  Schreiber/Writer, Execution/Ausführung — no term appears in two forms
- Rule 16 — German `„…"` retained
- Address form — **du**, per Bruno's ruling of 28 Oct 2026. 67 `du`-forms; the two
  capitalised `Sie` are the pronoun *sie* at sentence start, not formal address.

## Open items

- The **draft** German page still holds the short 755-word document. The next sync of
  sprint 4 would overwrite this page with it again unless the draft is updated first.
- `1. Intro` is left as `Intro` in the German heading, as in the approved translation.
