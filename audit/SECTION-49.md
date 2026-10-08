# §49 — INDEPENDENT THIRD AUDIT: live publication verification

**Written by:** Independent third auditor, 2026-10-08.
**Pen passes to:** GPT for F-3 and F-7; content lead for the items in §49.9.
**Status:** **AUDIT COMPLETE. CLOSEOUT PENDING F-3 AND F-7.**

---

## §49.0 Auditor identity, independence and evidence base

**Role.** A third agent in the loop, distinct from both parties in §0:

| Agent | Role |
|---|---|
| **GPT** | Holds the pen on repairs and publication (§§14–48). |
| **Claude (auditor)** | Produced §§0–44. |
| **This auditor** | Independent third party. Re-verified the live published state against the handoff's own claims. No part in building, repairing or publishing any of it. |

Not to be confused with `Course6_Capstone_Third_Audit.md` — that is the third *audit of Tom's
Capstone*, 2026-10-05. This is a third *auditor*, auditing the publication recorded in §§45–48.

**Why the independence is real, and where it is limited.** This auditor runs in a separate session
with no access to the build machine, to the publication utilities under
`C:\Users\Mac\.codex\...\audit_artifacts\`, or to their run logs. Every count below was
re-derived from a live API response. Where a verification artefact was used instead, the entry
says so explicitly.

**Evidence base**

| Source | How reached |
|---|---|
| The three live Notion databases | Notion public API, read calls only: `GET /v1/databases/{id}`, `POST /v1/databases/{id}/query` (paginated to exhaustion), `GET /v1/blocks/{id}/children`, `GET /v1/pages/{id}` |
| The live Google Drive tutor-deck folder | Drive connector; folder listing paged to exhaustion, each deck's content read |
| `HANDOFF_Course6_Capstone_Repair.md` | Supplied as a file, 5,020 lines, §§0–48 |
| `AI_6.zip`, `AI_IHK_dev.zip` | Supplied as files |

**Not reachable from this environment** — stated so no reader assumes these were checked:

- The build machine and its local tree.
- `app.notion.com` and `learn.microsoft.com` — both denied by this environment's egress policy
  (`CONNECT tunnel failed, response 403`).
- The German-cohorts page `3e694183-19f3-80b2-8286-e670d7d210d3` — the API returns
  `404 object_not_found`. **Verified unreachable, not verified absent**: the integration does not
  have that page shared with it. §49.9 carries the consequence.

## §49.1 Units and conventions

- **"Active rows"** = non-archived pages returned by a paginated query of the database, counted
  from the response, not from a view.
- **"Verified absent"** = queried the full row set and the item is not in it. **"Not found"** =
  searched and did not locate it. Both appear below and are not used interchangeably.
- Deck slide counts are `ppt/slides/slideN.xml` parts for a `.pptx`, and rendered slide blocks for
  a native Google Slides file.

---

## §49.2 Verified against live Notion

| Database | ID | Active rows | Against |
|---|---|---:|---|
| `AI IHK Certification` | `53094183-19f3-833d-944d-814d01343ee8` | **19** | §46.4 ✅ — **not** §45.7's 23 (F-1) |
| `Lessons` (tutor sessions) | `1cd94183-19f3-82cd-b5d7-01344958cc23` | **4** | §46.3 ✅ |
| `Module B — Microsoft Applied Skill (Optional)` | `3f294183-19f3-80ea-9460-db9a1df29b07` | **32** | §47.2 ✅ |

**AI IHK — 11 learner rows (`Order 1–11`) + 8 retained internal tutor resources.** All 19 rows
carry `Language = DE` and `Translation review = Listo`; all 8 tutor rows carry `Sprint = Internal`
(**§45.7 #3 ✅**). `Tu2–Tu5` are **verified absent** from the row set, confirming the §46.4
relocation. Zero page icons. `Order` ascending, no duplicates.

**Attachments — each present exactly once (§45.7 #4 ✅)**, by walking page children and counting
`file` / `image` blocks:

| Page | Attachment |
|---|---|
| `Tu12 — Tutor-Tracker` | `AI_IHK_Tutor_Tracker.xlsx` |
| L10 `IHK-Präsentation und Systemdemo vorbereiten` | `AI_IHK_Praesentationsvorlage.pptx` |
| L09 `Den Bericht fertigstellen und in Codio abgeben` | `AI_IHK_KI_Einsatzplanung_Vorlage.docx` |
| L02 `Gruppenarbeit und individueller Beitragsnachweis` | `AI_IHK_Beitragslog.xlsx` |

Ten file/image blocks across the database in total: those four documents plus six images — the six
German visuals of §45.3. No duplicates.

**Tutor sessions — four rows, `Order 1–4`, Weeks 1–4**, each linking exactly its matching deck,
file IDs identical to §46.2. Week-4 framing is live on the page, quoted from the block content:

> *"Tutor-Unterlage für die gemeinsame deutsche Presentation Prep LS. Dies ist keine zusätzliche
> IHK-only Live Session."* — **§46.6 ✅**

**Module B — 8 English roots + 12 English lessons + 12 German translations = 32 (§47.6 ✅).**
Every DE row nests under its matching EN lesson via the `Parent item` relation. Zero page icons,
zero database icon. `Order` ascending, no duplicates. All 24 `Microsoft Learn` URL property values
resolve to host `learn.microsoft.com` — no third-party or shortened hosts.

**Module B is outside the IHK databases (§45.7 #1 ✅)** — a separate database with no relation
property pointing at either IHK database.

## §49.3 Verified against live Google Drive

Folder `1N6CMJ0naIubLpCgRt7JO1aITCRwS1Wxe` contains **exactly four files**, listing paged to
exhaustion, all native Google Slides, no extras. IDs and titles match §46.2 exactly, each **8
slides**:

`1HRti5k-…nyLUg` W1 · `11C9nz1g…ieRqo` W2 · `1nskiEaX…ZHqAk` W3 · `1n4lG5MR…gKyYo` W4

**The §42/§43 soft hyphen survived the Google Slides import.** W3 slide 3 reads
`Einsatz\u00adbereiche` in the live Drive copy. §43 verified the PowerPoint render only; §30.7
warned that import re-renders. **This is the first check of the imported copy.** Intact.

**§40.2 deck German re-read in the live copies**, not inferred from source:
`Fragen, die jede Person beantworten kann` (relative-clause comma present), the
`On-Track` / `At-Risk` / `Off-Track` triple, `Kontrolltermin`, `Bereitschaftscheck`,
`IHK-Status prüfen`. No regressions.

## §49.4 Verified against the local artefacts

- **Decks.** W1–W4 are 8 slides each; `AI_IHK_Praesentationsvorlage.pptx` is 9. Zero
  `ppt/diagrams/` parts in all five — no SmartArt, so the §27/§30.1 two-layer divergence risk does
  not apply here.
- **The soft hyphen is surgical, as §43 claimed.** Exactly **one** `U+00AD` in the whole package,
  in `W3_Submission_Review.pptx`. `W1` and the presentation template still carry plain
  `Einsatzbereiche` (1 and 2 occurrences) — consistent with §42's finding that those render on one
  line at their box widths.

---

## §49.5 CHECKED AND FOUND CLEAN — so this is not re-litigated

**Codio is the only learner submission route (§45.7 #6 ✅).** `L09` carries 10 occurrences of
`Codio`, `L01` two. The single Google-Drive string anywhere in the learner campus is an explicit
negative, quoted from `campus/L09_bericht_und_codio_abgabe.md:39`:

> *"Die Einreichung erfolgt in Codio über die für die IHK-Abgabe eingerichtete Aktivität. **Es gibt
> keinen Google-Drive-Abgabelink.**"*

**`open_items_tracker.md` was not published (§45.7 #5 ✅).** **Verified absent** from the 19-row set
and from every published title in the publication artefacts. It exists only under
`tutor_materials/`.

**No coverage over-claim for IHK Modules 5/6.** This was checked because the 20-hour gap is the
package's largest external exposure, and the danger is content that *promises* coverage it lacks.
It does not:

- **Zero claims** about the eight IHK modules or the 80 Lehrgangsstunden in any of the 11 learner
  lessons. The only `80` in the entire campus is the `80 %` attendance rule in `L01` — unrelated.
- **Zero mentions** of Modules 5/6 or creative tools anywhere learner-facing or tutor-facing. The
  one occurrence in the whole package is a single row in `tutor_materials/open_items_tracker.md`,
  which is **verified absent** from the published set.
- That row reads: *"O7 | Nachweis für kreative Tools Module 5/6 | **Bridge nicht bauen oder
  versprechen**, bis Tiefe bestätigt ist | IHK/Data School"*. The build honours **both** halves.

§37.7's decision to omit the Module Coverage Map carries more weight than it appeared to: that
lesson was the one artefact that would have *had* to assert a coverage position. Omitting it
avoided manufacturing the over-claim rather than merely skipping a nice-to-have.

**Consequence:** the Modules 5/6 gap is external exposure — a question for IHK about evidence
requirements — and **not** a content defect. If IHK requires separate evidence for Modules 5/6,
that is an addition; nothing in the learner material needs unpicking.

---

## §49.6 FINDINGS

### F-1 · §45.7 #2 and #4 are stale and will produce two false failures
§45.7 asks for "23 active rows in exact `Order 1–23`" and for `Tu2–Tu5` to hold session decks. The
live database has **19 rows** and `Tu2–Tu5` are verified absent, because §46.4 archived them
deliberately. §48 already applies this kind of chronology correction to Module B; §45.7 has no
equivalent. **Recommended text to append to §45.7:**

> **[SUPERSEDED 2026-10-07]** Checks #2 and #4 describe the pre-relocation state. §46.4 archived
> `Tu2–Tu5` from this database, leaving **19 active rows** (11 learner + 8 internal tutor
> resources). Audit the row count against §46.4, not against this list. The session decks now live
> in database `1cd94183-19f3-82cd-b5d7-01344958cc23`, verified in §46.6 and §49.2.

### F-2 · `Order` gap at 13–16, with no renumber recorded
Live sequence: `1–11` learner, `12` (Tu1), **`17–23`** (Tu6–Tu12). The archived `Tu2–Tu5` held
13–16. Sorting is still ascending and unique, so this is **not** a functional defect.

**Recommendation: document the gap, do not renumber.** `Order` is an internal sort key; gaps in
sort keys are normal and harmless. Renumbering is eight writes that invalidate any externally
recorded `Order` value for no functional gain. What is actually wrong is the *claim* "exact
`Order 1–23`", and the F-1 note corrects it.

### F-3 · The Week-4 reframing exists only in the published page, not in its source
§46.1 establishes Week 4 as support for the **shared** German Presentation Prep LS; §46.3 states
the live page says so, and §49.2 confirms it does, quoted above.

The source does not. `tutor_materials/sessions/W4_exam_readiness_plan.md` is headed *"Woche 4
Präsentation und Prüfungsreife"* and contains no shared-Presentation-Prep wording — searched for
`presentation prep`, `präsentationsprobe`, `gemeinsam`, `shared`, `zusätzlich`; zero hits. The deck
does not carry it either.

**This is the §38/§39 failure mode inverted.** There, fixes went into the Markdown and the decks
were regenerated from source strings that were never corrected. Here the published page was
corrected and the source was not. Any regeneration from source silently drops a correction §46.1
made authoritative.

**Recommended repair:** add to `W4_exam_readiness_plan.md` under `## Ziel`, mirroring the live
wording — *"Tutor-Unterlage für die gemeinsame deutsche Presentation Prep LS. Dies ist keine
zusätzliche IHK-only Live Session."* See also the method note in §49.10.

### F-4 · One session carries four names, with no shared identifier
| Surface | Name |
|---|---|
| Deck title slide (local `.pptx` and the Drive copy) | `Woche 4 Präsentation und Prüfungsreife` |
| Drive file title | `IHK Tutor – Woche 4: Präsentationsprobe und Prüfungsreife` |
| Notion session row (§46.3) | `Woche 4 — Presentation Prep: Präsentationsprobe und Prüfungsreife` |
| Archived `Tu5` row (§45.4) | `Tu5 — Woche 4: Präsentation und Prüfungsreife` |

**The concrete failure:** a tutor opens the Week 4 session page, clicks through to the deck, and
the deck's first slide shows a different title from the page they came from. No week code or ID
ties them, so "is this the right deck?" is answerable only by position in the list. With four decks
that is obvious; it stops being obvious the moment one is added, reordered or duplicated.

**Recommendation:** make the Notion row's name canonical, since §46.1 made the Presentation Prep
framing authoritative, then align the deck's title slide and the Drive filename to it.

### F-5 · `Hohe Nichtbestehenswahrscheinlichkeit` is live
W3 slide 5, confirmed in the live Drive copy. Not a defect — §42.3 left it as a content-lead
readability call. See §49.9.

### F-6 · §47.2's `Translation review` claim did not reproduce
§47.2 states: *"Every active row has `Translation review = Listo`."* At audit time it did not. The
12 DE rows were `Listo`; **all 20 EN rows read `Sin empezar`** — the same Spanish stray the Third
Audit logged as **M-07** (*"Translation review: Sin empezar on all 47 Campus pages"*), now present
in the newly built Module B database.

**Resolved by the content lead, 2026-10-08.** §47.2's written claim should still be corrected to
describe the agreed state, so no later reader re-verifies a claim that did not hold when written.

### F-7 · Five Module B `Order` values carry floating-point artefacts
Live values, with their intended values. All five are the **German translation page** under a
`How to Prepare` module section, plus the final assessment page:

| Section | Lesson (EN) | Page (DE) | Stored | Intended |
|---|---|---|---|---|
| How to Prepare — Module 1 | Get started with Microsoft Copilot Studio | Erste Schritte mit Microsoft Copilot Studio | `4.109999999999999` | `4.11` |
| How to Prepare — Module 2 | Design agent conversations using topics | Agent-Unterhaltungen mit Themen gestalten | `5.109999999999999` | `5.11` |
| How to Prepare — Module 3 | Build intelligent agents in Microsoft Copilot Studio | Intelligente Agents in Microsoft Copilot Studio erstellen | `6.109999999999999` | `6.11` |
| How to Prepare — Module 4 | Add structured automation to agents in Microsoft Copilot Studio | Strukturierte Automatisierung zu Agents in Microsoft Copilot Studio hinzufügen | `7.109999999999999` | `7.11` |
| How to Take the Applied Skill Assessment | After passing: share the credential | Nach dem Bestehen: Leistungsnachweis teilen | `8.209999999999999` | `8.21` |

The other seven DE rows (`1.11`, `1.21`, `1.31`, `2.11`, `2.21`, `3.11`, `8.11`) are clean, so the
database is internally inconsistent. Sorting is unaffected; the raw value renders in the Notion UI
wherever the `Order` column is visible. A generation-script rounding artefact — five `PATCH` calls.

**Method note, recorded because it nearly produced a false negative:** a first pass using a
tolerance of `1e-9` reported zero affected rows. The error is of order `1e-15`. Detection requires
comparing the value's shortest representation against a clean two-decimal rendering, not a
numeric tolerance.

### F-8 · Icons were inconsistent across the three databases — NOW RESOLVED
At audit time: Module B 0 icons (§47.1 removed them), AI IHK 0 icons, tutor sessions **4 of 4**
carrying `🎓`. No stated rule covered the session database. See §49.8 — applied.

The tutor-session database also lacks the `Language` and `Translation review` properties the other
tutor surface uses. Recorded as an observation, not a defect against spec.

---

## §49.7 Not verifiable from this environment

Stated rather than assumed, per the §0 evidence standard.

- **View sort configuration.** The Notion public API does not expose a view's sort rules. Verified
  instead that the underlying `Order` values are ascending and unique in all three databases, which
  is the property the sort depends on. The view configuration itself remains **verified by GPT,
  not by this auditor**.
- **Microsoft link health (§47.4).** `learn.microsoft.com` is denied by this environment's egress
  policy, so the URLs could not be fetched. Their **routing** is verified — all 24 property values
  resolve to the official host. GPT's successful fetch of 21 distinct URLs stands unchallenged but
  unreproduced.
- **Pedagogical quality of the 11 learner lessons.** This audit was structural. First-hand, the 11
  lessons are structurally consistent: 6–7 sections each, every one closing with a Summary; the six
  `KI-Einsatz-Planung` chapters map one lesson each (L03–L08), with L01/L02 as scaffolding and
  L09–L11 exam-facing; each chapter lesson runs concept → concept → *Beispiel Falkenwerk* →
  *Arbeitsauftrag* → *Finaler Check*; 5,899 words across the eleven. **The quality verdicts in
  §§34, 37, 40 and 44 are relayed, not re-made by this auditor.**

## §49.8 Action applied by this auditor

**F-8 — the four `🎓` page icons removed**, on the content lead's explicit instruction,
2026-10-08. Method: `PATCH /v1/pages/{id}` with `{"icon": null}` against the four tutor-session
pages `3f294183-19f3-8101-b13a-dd4a276e2982`, `…-81a6-b192-e623d616b730`,
`…-8194-bc2e-db23cfac3d4d`, `…-812a-a3bc-d6285cdf962b`. Verified `icon = null` on all four
afterwards. All three databases now carry zero page icons and zero database icons.

This is the only write this auditor made. Everything else in §49 is a read.

## §49.9 Content-lead decisions recorded

- **Falkenwerk — RETAINED.** The running case is `Falkenwerk Service GmbH`, a customer-service
  organisation building a support-triage agent in `n8n`. The real FALKENWERK in Koblenz is a media
  agency — a different sector, as §40.1 judged. Decision: keep the name. **Closes the open item
  §40.1 left with the content lead.**
- **The four house-voice calls accepted as they stand** — masculine `der Tutor`, `Finaler Check`,
  the absent `Lernergebnisse` / `Check zum Verständnis` blocks, and
  `Hohe Nichtbestehenswahrscheinlichkeit` (F-5). No change required; do not re-litigate.
- **F-6 resolved** — see F-6.
- **F-8 applied** — see §49.8.
- **Deborah's two stale lines remain unverified and unactioned.** §36.3 recorded *"6 pre-defined
  project options"* (should be 8) and briefs including *"data"* (superseded — learners generate
  their own) as live on the German-cohorts page. This auditor could not reach that page
  (§49.0). It is Deborah's page; neither agent edits it. **Still needs a human to check and
  correct it before the German tutor reads it.**

## §49.10 Method note — for the collection in §44.3

**A correction is not done until it exists in the source that regenerates the artefact, not only in
the artefact.** This project has now been bitten in both directions: §38/§39 corrected the Markdown
and regenerated decks from source strings that were never fixed; §46 corrected the published page
and left the source stale (F-3). The existing §44.3 notes cover stored-string-versus-render and
grep-hit provenance; this is the third of the same family and belongs beside them.

## §49.11 Status

Structural publication state is sound and matches the handoff as corrected by §46 and §48. Nothing
in the published content contradicts a locked decision. No redesign is implied by anything in this
entry.

**Remaining before closeout:**

1. **F-3** — patch `W4_exam_readiness_plan.md` at source.
2. **F-7** — round the five `Order` values.

**Recommended but not blocking:** annotate §45.7 per F-1; correct §47.2's claim per F-6; document
the `Order` gap per F-2; settle the naming per F-4.

**Status: AUDIT COMPLETE. CLOSEOUT PENDING F-3 AND F-7.**
