# §49 — CLAUDE: FINAL PUBLICATION AUDIT (PARTIAL — NOT A CLOSEOUT)

**By:** Claude, 2026-10-08. Working from the uploaded `HANDOFF_Course6_Capstone_Repair.md`
(5,020 lines, §§0–48), `AI_6.zip`, `AI_IHK_dev.zip`, and the live Google Drive folder.

**This entry does not close the handoff.** §45.7, §46.6 and §47.6 all require independent
re-reading of **live Notion pages**. This session has no Notion access: `app.notion.com` is
denied by the environment's egress policy (403 on CONNECT), and no device/browser bridge is
attached. Every Notion-dependent check is listed as BLOCKED below, unverified. The checks
that could be made first-hand were made first-hand.

---

## §49.1 Verified first-hand — Google Drive (§46.2, §46.6)

Read directly through the Drive connector, not from any verification artefact.

Folder `1N6CMJ0naIubLpCgRt7JO1aITCRwS1Wxe` contains **exactly four files**, all native
Google Slides (`application/vnd.google-apps.presentation`), no extras — confirmed by paging
the listing to exhaustion. File IDs and titles match §46.2 exactly:

| # | Title | File ID | Slides |
|---|---|---|---|
| 1 | IHK Tutor – Woche 1: Einführung und Gruppenbildung | `1HRti5k-zr3unxTDPbnm92tfgIkLkltbPfLl6E-nyLUg` | **8** |
| 2 | IHK Tutor – Woche 2: On-Track-/At-Risk-Check | `11C9nz1gTGBg3WR0Mk3cQHp2repWHjwzWgYaqO-ieRqo` | **8** |
| 3 | IHK Tutor – Woche 3: Submission Review | `1nskiEaXhNbmRPa7cfWPPBfSO4NxRyNS4JJJmFNZHqAk` | **8** |
| 4 | IHK Tutor – Woche 4: Präsentationsprobe und Prüfungsreife | `1n4lG5MRVpOTTr_cZvFylRmkMKpk8nFaMo3Kno7gKyYo` | **8** |

**The §42/§43 soft hyphen survived the Google Slides import.** W3 slide 3 reads
`Einsatz­bereiche` in the live Drive copy. §43 verified the PowerPoint render; this is the
first check of the imported Slides copy, which is where §30.7 warned that import re-renders.
Confirmed intact.

**§40.2 deck German is live in the Drive copies**, re-read rather than inferred:
`Fragen, die jede Person beantworten kann` (D-? relative-clause comma — present),
the `On-Track` / `At-Risk` / `Off-Track` triple, `Kontrolltermin`, `Bereitschaftscheck`,
`IHK-Status prüfen`. No regressions.

## §49.2 Verified first-hand — local artefacts

- **Deck integrity.** W1–W4 are 8 slides each; the learner presentation template is 9.
  Zero `ppt/diagrams/` parts in all five — no SmartArt, so no two-layer divergence risk.
- **The soft hyphen is surgical, as §43 claimed.** Exactly **one** `U+00AD` in the whole
  package, in W3. W1 and the presentation template still carry plain `Einsatzbereiche`
  (1 and 2 instances) — consistent with §42's finding that those render on one line.
- **Codio is the only submission route (§45.7 #6).** `L09` carries 10 Codio references,
  `L01` two, and the single Google-Drive string in the learner campus is an explicit
  negative: *"Die Einreichung erfolgt in Codio über die für die IHK-Abgabe eingerichtete
  Aktivität. Es gibt keinen Google-Drive-Abgabelink."* No Drive submission route exists.
- **`open_items_tracker.md` was not published (§45.7 #5).** Absent from the 23 ordered
  titles in `tutor-layer-verification.json` and from every publication artefact. It exists
  only under `tutor_materials/`.
- **11 learner lessons** present locally and in `notion-publication-20261007/verification.json`,
  sprint-tagged 1/1/1/1/2/2/3/3/3/4/4.
- **Module B** — `microsoft-module-b-20261007/verification.json` self-reports
  32 active / 8 EN roots / 12 EN leaves / 12 DE, with DE nested by decimal `Order`
  (`1.1` EN → `1.11` DE → `1.2` EN). That ordering sorts correctly ascending.

---

## §49.3 FINDINGS

### F-1 · §45.7's auditor checklist is stale and will produce two false failures

§45.7 asks the auditor to verify "the AI IHK database has **23 active rows** in exact
`Order 1–23`" (#2) and "**`Tu2–Tu5`** each contain one correct session deck" (#4).

§46.4 deliberately superseded both: `Tu2–Tu5` were archived after relocation, leaving
**19 active rows** (11 learner + 8 retained internal tutor resources). An auditor working
§45.7 literally would report two failures against a state that was corrected on purpose.

§48 anticipates exactly this hazard for Module B and fixes it with a chronology pointer.
The same pointer is missing for §45.7. **Recommend: annotate §45.7 #2 and #4 as superseded
by §46.4**, the way §48 annotates §47.

### F-2 · The `Order` sequence now has a gap at 13–16, and nothing records a renumber

Per `tutor-layer-verification.json` the tutor rows were `Tu1=12 … Tu12=23`. §46.4 archived
`Tu2–Tu5`, which held `Order` 13, 14, 15, 16. The 19 surviving rows therefore run
`1–11` (learner), `12` (Tu1), `17–23` (Tu6–Tu12).

Not a functional defect — the single view sorts ascending and the sequence is still
monotonic. But "exact `Order 1–23`" no longer describes the database, and §46 records no
renumber. Either renumber to `1–19` or state the gap as intended, so the next auditor does
not read it as data loss.

### F-3 · The Week-4 reframing exists only in the published page, not in the local source

§46.1 establishes that Week 4 is tutor support for the **shared German Presentation Prep
LS**, not an additional IHK-only session, and §46.3 states the live Notion page says so
explicitly.

The local source does not. `tutor_materials/sessions/W4_exam_readiness_plan.md` is still
headed *"Woche 4 Präsentation und Prüfungsreife"* and contains no shared-Presentation-Prep
wording at all (searched for `presentation prep`, `präsentationsprobe`, `gemeinsam`,
`shared`, `zusätzlich` — zero hits). The W4 deck does not carry it either.

**This is the §38/§39 failure mode inverted.** There, fixes went into the Markdown and the
decks were regenerated from uncorrected source strings. Here the published page was
corrected and the source was not — so anyone regenerating from source silently drops the
reframing that §46.1 just established as authoritative. Fix at source.

### F-4 · One session now carries three different names

| Surface | Name |
|---|---|
| Deck title slide (local + Drive content) | `Woche 4 Präsentation und Prüfungsreife` |
| Drive file title (§46.2) | `IHK Tutor – Woche 4: Präsentationsprobe und Prüfungsreife` |
| Notion session row (§46.3) | `Woche 4 — Presentation Prep: Präsentationsprobe und Prüfungsreife` |
| Archived Tu5 row (§45.4) | `Tu5 — Woche 4: Präsentation und Prüfungsreife` |

Cosmetic, but a tutor matching a deck to a session page has to do it by position. Pick one.

### F-5 · `Hohe Nichtbestehenswahrscheinlichkeit` is live

W3 slide 5 in the Drive copy. Not a defect — it fits and breaks nowhere, and §42.3 left it
as a content-lead readability call. Recorded only so it is decided rather than forgotten.

---

## §49.4 BLOCKED — requires live Notion, not verified

None of the following is asserted either way in this entry.

| Source | Check |
|---|---|
| §45.7 #1 | Module B remains optional/async and outside the IHK database |
| §45.7 #2 | Active row count and `Order` sequence **on the live database** (see F-1, F-2) |
| §45.7 #3 | All tutor pages carry `Internal` / `DE` / `Listo` |
| §45.7 #4 | Deck and template attachments present exactly once (see F-1) |
| §45.7 #7 | §45.1 decisions reflected as closed/external |
| §46.6 | Four ordered session rows; each links its matching deck; Week-4 framing on the page; `Tu2–Tu5` absent; eight internal resources retained |
| §47.6 / §48 | 8/12/12 hierarchy, no icons, EN→DE nesting, ascending `Order`, link routing, optional/async boundary |
| §47.4 | The 21 Microsoft URLs — `learn.microsoft.com` is also unreachable from this container (`http=000`), so link health could not be re-tested either |

Everything above is reachable from a session with the Notion connector attached, or from a
browser pane on the content lead's machine. The Drive half of §46.6 is already done (§49.1).

**Status: PARTIAL. The handoff is NOT closed.**
