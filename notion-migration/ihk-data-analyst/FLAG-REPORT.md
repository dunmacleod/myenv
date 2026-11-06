# IHK Data Analyst Certification — NOV → live

Source of truth: **IHK Data Analyst Certification (NOV)**. Destination: the live
**IHK Data Analyst Certification**. The live course now equals NOV: **18/18 pages match** on
title, Sprint, Language and content.

| | |
|---|---|
| Live rows before → after | 24 → 18 |
| Pages updated in place (URL kept) | 13 |
| Pages created | 5 |
| Pages removed | 11 |
| Attachments re-hosted | 8 |
| Verified equal to NOV | **18 / 18** |
| Errors | 0 |

## This one was a redesign, not a refresh

Unlike the earlier courses, the two pages were not twins. NOV restructures the curriculum into
chapters and consolidates tutor material into Tu1–Tu8, so only 13 of 18 lessons had an existing
counterpart. Automated title matching was not trustworthy here — it paired *Tu7 — Tutor-Tracker*
with *Tu1 — Tutor-Handbuch* at 0.59 similarity — so the mapping below was read by hand and
confirmed with you before anything was written.

### Updated in place (existing page kept, content and title replaced)

| NOV lesson | Live page it reused |
|---|---|
| Der IHK-Weg: Prüfung, Zeitplan und Freigabe | Die IHK-Prüfung im Überblick |
| Gruppenarbeit und individueller Beitragsnachweis | Gruppenarbeit aufteilen — individuelle Sichtbarkeit als IHK-Pflicht |
| Kapitel 1: Ausgangssituation und Ist-Zustand | Ist-Zustand mit Substanz |
| Kapitel 2: ML-Canvas nachvollziehbar begründen | Der Machine Learning Canvas |
| Kapitel 3: Projektplanung und SCRUM-Dokumentation | Projektplanung und SCRUM-Dokumentation |
| Kapitel 4: Workflow, Datenmodell und Ergebnisse | Workflow, Datenmodell und Ergebnisse |
| Den Bericht fertigstellen und abgeben | Den Bericht auf Deutsch schreiben — Stil, Form, Zitation |
| IHK-Präsentation und Live-Demo vorbereiten | Die Präsentation strukturieren — 30 Minuten Konzept, 15 Minuten Demo |
| Fachgespräch und Prüfungsreife | Das Fachgespräch — Vorbereitung auf das individuelle Gespräch |
| Tu1 — Tutor-Handbuch DA IHK | Tu1 — Tutor-Handbuch |
| Tu2 — Check-in-Rubrik | Tu2 — Check-in-Rubrik |
| Tu3 — Fachgespräch: Fragenkatalog | Tu3 — Mock Fachgespräch — Question Bank |
| Tu8 — DA-Bewertungsrubriken und Transparenz | IHK-Bewertungsrubriken — Transparenz-Dokument |

### Created (no live counterpart)

- [Sprint 1] **Überblick: Abgaben, Termine und Bewertung**
- [Internal] **Tu4 — Abgabeprüfung und individuelle Freigabe**
- [Internal] **Tu5 — Kalibrierungsleitfaden**
- [Internal] **Tu6 — Protokoll für den Prüfungstag**
- [Internal] **Tu7 — Tutor-Tracker**

### Removed (no NOV counterpart)

Per your decision to make live exactly equal to NOV. Every one is backed up under `backup/`
with a `DELETED-` prefix, and Notion's trash holds them for 30 days.

| Page | Blocks |
|---|---|
| Tu3 — Mock Fachgespräch — Question Bank (1) | 123 |
| Projekt-Briefing — Mitarbeiterfluktuation bei Sonnenfeld Industries GmbH | 96 |
| Projekt-Briefing — Energieverbrauchs-Anomalien bei StadtWerke Westhafen GmbH | 90 |
| Projekt-Briefing — Patienten-No-Shows beim Praxisverbund Rhein-Main eG | 83 |
| Projekt-Briefing — Kreditrisiko-Frühwarnung bei Schwarzwald Kreditkasse AG | 92 |
| Projekt-Briefing — Umsatzprognose bei GreenGarten Versandhandel GmbH | 94 |
| Projekt-Briefing — Lieferpünktlichkeit bei Adler Express GmbH | 93 |
| Datasets and Briefings | 0 |
| Sprint-Log Template — Datenbank-Schema | 20 |
| KI verantwortungsvoll einsetzen | 70 |
| ML-Grundlagen für den Canvas | 74 |

**Worth repeating, since it is the biggest consequence:** the six `Projekt-Briefing` pages and
their *Datasets and Briefings* parent are gone from the live course. Those were the project briefs
learners work from, and the NOV staging set contains no replacement for them. Nothing linked to
them internally, so no links broke, but if learners are meant to still receive those briefs they
need to come back — either restored from the backup or authored into NOV.

Also removed: `ML-Grundlagen für den Canvas` (NOV folds the canvas material into a single
*Kapitel 2*), `KI verantwortungsvoll einsetzen`, `Sprint-Log Template — Datenbank-Schema`, and a
duplicate `Tu3 — Mock Fachgespräch — Question Bank (1)`.

## One thing I had to choose

NOV's single *Kapitel 2: ML-Canvas nachvollziehbar begründen* could have reused either live page:
*Der Machine Learning Canvas* or *ML-Grundlagen für den Canvas*. I reused the first, so its URL
survives and the second's does not. The end state is the same either way; say the word if you
wanted the other URL kept.

## New capability this course needed

NOV pages carry **file attachments** — 7 learner worksheets (`IHK1–4_Arbeitsblatt_DE.md`,
`DA_Berichtsstruktur.md`, `DA_Abgabecheckliste.md`, `DA_Muendliche_Vorbereitung.md`) and a tutor
tracker (`candidate_readiness.csv`). Notion serves these from signed URLs that expire within the
hour, so each was downloaded and re-uploaded into the live workspace rather than referenced.
All 8 were checked afterwards and return HTTP 200.

## Left alone — your call

- **The NOV database has 7 columns the live one does not**: `Review status`, `Stage`, `Package`,
  `Lesson type`, `Order`, `Source key`, `English source`. These are staging/workflow fields, so I
  copied page content and the shared fields (Lesson, Sprint, Language) and left the schema alone.
  I can add the columns and populate them if you want full parity.
- **The live database has no name** (it shows as *New database*); NOV's is *DA IHK NOV — learner
  staging*, which would read wrong in production. Tell me what it should be called and I'll set it.
- **`Review status` on the NOV rows still reads "Ready for approval"**, not "Approved for
  production". You asked to migrate anyway; flagging it so the staging board can be updated to
  reflect that this content is now live.

## Checks

- All 13 reused pages kept their page IDs and URLs; none in trash
- All 11 removed pages confirmed in trash
- Live database holds exactly the 18 NOV lessons, no extra rows
- Language set to DE on all 18 (it was unset on every live row before)
- No images, mentions or internal Notion links anywhere in this course, so nothing to remap
- No campus quiz embeds, and no callout-icon deviation
