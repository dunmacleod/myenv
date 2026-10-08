# §49 — CLAUDE: FINAL PUBLICATION AUDIT

**By:** Claude, 2026-10-08. Live Notion read directly through the Notion API
(`api.notion.com`, read-only calls: `GET /databases`, `POST /databases/{id}/query`,
`GET /blocks/{id}/children`). Google Drive read through the Drive connector. Local
artefacts from `AI_6.zip` and `AI_IHK_dev.zip`. Every count below was re-derived from the
live API response, not read from a verification file.

**Verdict: all structural checks in §45.7, §46.6 and §47.6 reproduce. Three items need
disposition before this closes (F-3, F-6, F-7); two could not be verified from this
environment and are recorded as such.**

---

## §49.1 Live database state, independently derived

| Database | ID | Active rows | Matches |
|---|---|---:|---|
| `AI IHK Certification` (learner + retained tutor) | `53094183…343ee8` | **19** | §46.4 ✅ (not §45.7's 23 — see F-1) |
| `Lessons` (tutor sessions, §46 destination) | `1cd94183…58cc23` | **4** | §46.3 ✅ |
| `Module B — Microsoft Applied Skill (Optional)` | `3f294183…f29b07` | **32** | §47.2 ✅ |

**AI IHK database — 11 learner (`Order 1–11`) + 8 retained internal tutor resources.**
Every one of the 19 rows carries `Language = DE` and `Translation review = Listo`;
all 8 tutor rows carry `Sprint = Internal` (§45.7 #3 ✅). `Tu2–Tu5` are absent, confirming
the §46.4 relocation. No page icons. `Order` ascending, no duplicates.

**Attachments (§45.7 #4) — each present exactly once**, confirmed by walking page blocks:

| Page | Attachment |
|---|---|
| `Tu12 — Tutor-Tracker` | `AI_IHK_Tutor_Tracker.xlsx` |
| L10 `IHK-Präsentation und Systemdemo vorbereiten` | `AI_IHK_Praesentationsvorlage.pptx` |
| L09 `Den Bericht fertigstellen und in Codio abgeben` | `AI_IHK_KI_Einsatzplanung_Vorlage.docx` |
| L02 `Gruppenarbeit und individueller Beitragsnachweis` | `AI_IHK_Beitragslog.xlsx` |

Ten file/image blocks across the database: those four documents plus six images — the six
German visuals of §45.3. No duplicates.

**`open_items_tracker.md` is not published (§45.7 #5 ✅)** — absent from all 19 rows.

**Tutor sessions — four rows, `Order 1–4`, Weeks 1–4**, each linking exactly its matching
deck, file IDs identical to §46.2:

| Row | Linked deck |
|---|---|
| Woche 1 — IHK-Einführung und Gruppenbildung | `1HRti5k-…nyLUg` |
| Woche 2 — IHK Progress: On-Track-/At-Risk-Check | `11C9nz1g…ieRqo` |
| Woche 3 — IHK Submission Review | `1nskiEaX…ZHqAk` |
| Woche 4 — Presentation Prep: Präsentationsprobe und Prüfungsreife | `1n4lG5MR…gKyYo` |

**Week-4 framing is live on the page (§46.6 ✅):** *"Tutor-Unterlage für die gemeinsame
deutsche Presentation Prep LS. Dies ist keine zusätzliche IHK-only Live Session."*

**Module B — 8 English roots + 12 English lessons + 12 German translations = 32 (§47.6 ✅).**
Every DE row nests under its matching EN lesson via `Parent item`. No icons on any row.
`Order` ascending with no duplicates. All 24 `Microsoft Learn` URL values route to
`learn.microsoft.com` — no third-party or shortened hosts.

**Module B is outside the IHK database (§45.7 #1 ✅)** — a separate database under the
general Course 6 root, with no relation to either IHK database.

## §49.2 Carried forward from the partial audit (unchanged)

Verified first-hand earlier and not revisited: the Drive folder holds exactly four native
8-slide Google Slides decks with IDs matching §46.2; the §42/§43 soft hyphen survived the
Slides import (`Einsatz­bereiche`, W3 slide 3); exactly one `U+00AD` in the package;
zero SmartArt in all five decks; Codio is the only submission route, with L09 stating
*"Es gibt keinen Google-Drive-Abgabelink"* (§45.7 #6 ✅).

---

## §49.3 FINDINGS

### F-1 · §45.7 #2 and #4 are stale — CONFIRMED LIVE
§45.7 asks for "23 active rows in exact `Order 1–23`" and for `Tu2–Tu5` to hold session
decks. The live database has **19 rows** and no `Tu2–Tu5`, because §46.4 archived them on
purpose. Auditing §45.7 literally yields two false failures. §48 already applies this kind
of chronology correction to Module B; **§45.7 #2 and #4 need the same annotation.**

### F-2 · `Order` gap at 13–16 — CONFIRMED LIVE
Live sequence: `1–11` learner, `12` (Tu1), **`17–23`** (Tu6–Tu12). The archived `Tu2–Tu5`
held 13–16 and nothing renumbered. Sort order is still correct and unique, so this is not
a functional defect — but "exact `Order 1–23`" no longer describes the database. Renumber
to `1–19`, or record the gap as intentional so the next auditor doesn't read it as loss.

### F-3 · Week-4 reframing is live but missing from its source — CONFIRMED BOTH SIDES
The framing is on the published page (quoted above). It is **not** in
`tutor_materials/sessions/W4_exam_readiness_plan.md`, which is still headed *"Woche 4
Präsentation und Prüfungsreife"* with no shared-Presentation-Prep wording at all, and not
in the deck. This is the §38/§39 failure inverted — there, fixes went to Markdown and decks
regenerated from stale strings; here the page was fixed and the source was not. **Any
regeneration from source silently drops a correction §46.1 made authoritative.** Fix at source.

### F-4 · One session carries four names
Deck title slide `Woche 4 Präsentation und Prüfungsreife` · Drive file `IHK Tutor – Woche 4:
Präsentationsprobe und Prüfungsreife` · Notion row `Woche 4 — Presentation Prep:
Präsentationsprobe und Prüfungsreife` · archived `Tu5 — Woche 4: Präsentation und
Prüfungsreife`. Cosmetic, but a tutor matches deck to session by position. Pick one.

### F-5 · `Hohe Nichtbestehenswahrscheinlichkeit` is live
W3 slide 5. Not a defect — §42.3 left it as a content-lead readability call. Recorded so it
is decided rather than forgotten.

### F-6 · §47.2's `Translation review` claim does not reproduce — NEW
§47.2 states: *"Every active row has `Translation review = Listo`."* **It does not.**
Live: the **12 DE rows are `Listo`; all 20 EN rows are `Sin empezar`.**

`Sin empezar` is Spanish for "not started" — the same stray the Third Audit logged as
**M-07** (*"Translation review: Sin empezar on all 47 Campus pages"*). It has now
propagated into the newly built Module B database. Either the claim is wrong or the data
is, and the Spanish value is a known production defect either way. Decide whether EN source
rows should read `Listo`, a proper English value, or empty — then apply it consistently.

### F-7 · Five Module B `Order` values carry floating-point artefacts — NEW
Live values `4.109999999999999`, `5.109999999999999`, `6.109999999999999`,
`7.109999999999999`, `8.209999999999999` where `4.11 … 8.21` was intended. The other seven
DE rows (`1.11`, `1.21`, `1.31`, `2.11`, `2.21`, `3.11`, `8.11`) are clean, so the database
is internally inconsistent. Sorting is unaffected — but the raw value renders in the Notion
UI wherever the `Order` column is visible. A generation-script rounding bug; cheap to fix.

### F-8 · Icons are inconsistent across the three databases — NEW
Module B: 0 icons (§47.1 removed them). AI IHK: 0 icons. **Tutor sessions: all 4 rows carry
icons.** The tutor-session database also lacks the `Language` and `Translation review`
properties the other tutor surface uses. No stated rule covers the session database, so
this is a consistency observation, not a defect against spec.

---

## §49.4 Not verifiable from this environment

Stated rather than assumed:

- **View sort configuration.** The public Notion API does not expose a view's sort rules.
  I verified instead that the underlying `Order` values are ascending and unique in all
  three databases, which is the property the sort depends on. The view configuration itself
  remains verified-by-GPT.
- **Microsoft link health (§47.4).** `learn.microsoft.com` is denied by this environment's
  egress policy, so the 24 URLs could not be fetched. Their **routing** is verified — all
  24 resolve to the official host. GPT's successful fetch of 21 distinct URLs stands
  unchallenged but unreproduced.

---

## §49.5 Status

Structural publication state is sound and matches the handoff as corrected by §46 and §48.
Nothing in the published content contradicts a locked decision.

**Before closing, three items need action, none of them a rebuild:**

1. **F-6** — decide the `Translation review` value for EN rows and apply it; §47.2's claim
   must be corrected either way.
2. **F-7** — round the five float `Order` values.
3. **F-3** — patch `W4_exam_readiness_plan.md` at source so the Week-4 reframing survives
   regeneration.

**F-1** should be annotated into §45.7 so the stale checks don't mislead a later reader.
**F-2**, **F-4**, **F-5** and **F-8** are content-lead calls, not blockers.

**Status: AUDIT COMPLETE. CLOSEOUT PENDING F-3, F-6, F-7.**
