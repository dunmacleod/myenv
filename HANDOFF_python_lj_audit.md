# Handoff — Python (DA) Learning Journey: audit + change plan

**For:** GPT (implementation agent) · **Prepared by:** Claude (audit) · **Date:** 2026-10-19
**Trigger:** student feedback from the current Python term (July GER cohort), three points about course content: project instructions (slides vs notebook), unrealistic LJ time estimates, project scope vs the new two-modules-per-term calendar.

---

## 0. What this document is

A complete, implementable change plan for the Python course content in Notion (+ the Drive notebooks it links to). Everything below is specified with page IDs and exact source text so it can be executed without re-deriving the audit. Where a decision needs a human (rubric ownership, campus CMS access), it is listed in §6 — do not invent those.

**Three workstreams, in the order they should be implemented:**

| # | Workstream | Feedback point | Pages touched | Blocker? |
|---|---|---|---|---|
| A | Project deliverable = notebook **+ slides**, said identically everywhere | 1 | 6 Notion pages (3 EN + 3 DE), 2 Drive notebooks, rubric | needs rubric owner (§6-Q1) |
| B | Recalibrated time estimates, per sublesson | 2 | 81 EN + 81 DE sublessons (metadata only) | needs campus CMS access (§6-Q2) |
| C | Reduced project scope (7+3 → 5+1 required, rest optional) | 3 | same pages as A + starter/solution notebooks | no |
| D | Content hygiene found during the audit (not requested, cheap, student-visible) | — | 14 sublesson pairs + 1 duplicate | no |

Sections below run **A → C → B → D**: A and C change the same project pages and should be executed as one pass, B is metadata only, D is cosmetic.

### Sources audited

- Lesson DB (the LJ link in the request): `33594183-19f3-805f-a91c-fcb96b315fc6` — 14 lessons, 81 EN sublessons, 81 DE sublessons (1:1 coverage, DE pages are children of the EN page they translate).
- Earlier-module DB on the same *Python* page: `33494183-19f3-81f4-acb0-df20c37022f5` (contains `Introduction to you Project`, which also describes the deliverable).
- Parent page *Python*: `33494183-19f3-80d3-9952-f5e75a5297c8`.
- Drive: `health_explorer_starter.ipynb` (`1C9S20YwmRN-nRNx24zVxqy9m0t3_TfPd`), `health_explorer_walkthrough.ipynb` (`1-s_r0qji0we2C6cUXvOZvToshhMZbrDq`), `health_explorer_solution.ipynb` (`19pqfkB8B7kRIrB22oX5IBaNcNdMdd4Fb`), `Health_Data_Explorer_Solution.ipynb` (`1wDdt0gmCEPGbMDsx_itfSTD76PEZp-lA`), dataset sheet `1RCJGLY1ZCm_oGjiCvjSwcHWPj-oac5b5PrrUAlLzij8`.
- All 81 EN sublesson bodies were read in full (word counts, code blocks, embedded campus exercises, quiz toggles) — that is the basis of workstream B.
- **Not found anywhere in Notion or Drive:** the grading rubric for this project, and any Python live-session (LS) deck. See §6-Q1/Q3.

### Notion page URL pattern

`https://www.notion.so/<page-id-without-dashes>` — e.g. the project brief: `https://www.notion.so/3619418319f380e0a689f859563e3eee`.

---

## 1. Audit findings (what is actually wrong today)

**F1 — The LJ explicitly forbids slides, in both languages.**
*Submitting Your Project and Presentation Day* (EN `36194183-19f3-80ce-9101-ca07e49e3eb2`) says verbatim:

> You don't need slides. Open your notebook on your shared screen and walk through it.

DE (`36194183-19f3-8080-84b2-fc8a490260e7`) mirrors it:

> Du brauchst keine Slides. Öffne dein Notebook auf deinem geteilten Bildschirm und führe hindurch.

So the students were right: they followed the instruction and were marked down against an expectation the LJ denies. **The LJ is the thing that changes** (plus the rubric, §6-Q1) — not the students.

**F2 — The deliverable is described in four places, and they will drift.**
1. `Introduction to you Project` (earlier module, EN `36194183-19f3-80a2-9f12-e05cacb95666`) — "What the final deliverable looks like → A single Jupyter notebook with: …"
2. `Health Data Explorer — Project Brief` (EN `36194183-19f3-80e0-a689-f859563e3eee`) — "You will deliver a single Jupyter notebook that answers seven guided questions, three questions of your own…"
3. `Submitting Your Project and Presentation Day` (EN `…80ce…`) — deliverable paragraph + checklist + presentation-day section.
4. `health_explorer_starter.ipynb` — the same brief, restated in Markdown cells.
Every change in A and C has to land in all four, in both languages (notebooks are EN-only in the shared folder; DE copies live in the `DE` folder `1VkcNK9UIaYMfg1rqnAyQ2huUsbhY2DZS`).

**F3 — Presentation guidance exists but is structure-free.** The 10-minute breakdown (1 min dataset / 3 min guided Q / 3 min own Q / 2 min summary / 1 min Q&A) is good and should survive — it becomes the slide structure, which is exactly the "minimum presentation structure" the feedback asks for.

**F4 — Time estimates are a flat default.** Every sublesson is 20 min; lesson totals are just 20 × number of sublessons. No duration field exists in the Notion DB, so the 20-min values come from the campus CMS. Content weight per sublesson varies by ~18× (5 min of reading vs 8 consecutive coding exercises), so the display is wrong in both directions: it understates practice lessons by 2–4.5× and overstates pure-theory pages by 2×.

**F5 — Project effort is invisible in the LJ.** The `Project` lesson shows 100 min, which is the reading time for five pages. The notebook itself (10 questions over 50,000 rows) is realistically 7–9 h of work under the current scope and appears nowhere in the LJ budget. That is a large part of why the term feels unsurvivable, independent of the estimates in F4.

**F6 — The submission step sits in the wrong module.** *Submitting Your Project* says "submit … through the course submission platform **in the next lesson**", but the Codio *Submission* item is at the end of M4 *Developer Tools & AI*, two lessons and one module later than the project lesson in M3.

**F7 — Starter notebook and brief disagree on the dataset.** The brief lists a `message` column (and Part 2 constraint 2 *requires* using it); the starter's "About the dataset" cell lists only height/weight/age/gender/activity/smoker + the four computed columns, and never mentions `message`.

**F8 — Duplicate sublesson title.** *Data Assessment* has two sublessons both called `DataFrame Assessment with Python` (EN `35594183-19f3-8026-b94e-ef7822c3ddab` = the code-along; EN `35594183-19f3-80a8-9fbc-d04cb3f2b123` = an exercise page with two campus exercises). In the campus list a student sees the same title twice.

**F9 — Student-visible typos in sublesson titles** — `Satistics`, `Mulrivariate` (×4), `Handing`, `Substracting`, `Two Question`, `Introduction to you Project`. Full list with IDs in §5.

---

## 2. Workstream A — project instructions: notebook **+ slides**, said identically everywhere

Implement A1–A5 as one batch, EN first, then the DE mirror, then the notebooks.

### A1 · `Submitting Your Project and Presentation Day` (EN `36194183-19f3-80ce-9101-ca07e49e3eb2`)

**Edit 1 — opening paragraph.** Replace:

> Your project deliverable is a single Jupyter notebook. Think of it as a small written report — someone who has never seen the data should be able to read it top to bottom and understand both what you did and what you found.

with:

> Your project has two deliverables: a **Jupyter notebook** and a **short slide deck (5–7 slides)** that you present on presentation day. The notebook is a small written report — someone who has never seen the data should be able to read it top to bottom and understand what you did and what you found. The deck is how you walk your evaluator through the two or three things in it that matter most. Both are graded; the deck is graded on structure and on whether you can explain your choices, not on design.

**Edit 2 — the "no slides" line.** Replace:

> You don't need slides. Open your notebook on your shared screen and walk through it.

with:

> Present from your slide deck, not from the notebook. Keep the notebook open in a second window — your evaluator will ask you to jump to the code or the chart behind something you claim, and being able to do that quickly is part of the evaluation.

**Edit 3 — new section, inserted immediately before "What your 10 minutes should cover".**

> ## Your slide deck
>
> Five to seven slides. Each one maps to a block of your 10 minutes, so the deck and the talk have the same shape.
>
> 1. **Title + dataset** — your name, the project, and the dataset in one line (what it is, 50,000 rows, which columns you used).
> 2. **Approach + what you noticed** — how you worked through the project and anything the initial inspection turned up (including the data quality quirk in `Activity_Level`).
> 3. **Your strongest guided question** — the question, one chart from your notebook, and the finding in one sentence. One or two slides.
> 4. **Your own question** — why you asked it, one chart, the finding. One or two slides.
> 5. **Three insights + what's next** — your three insights in your own words, and what you would investigate with more time.
>
> Rules:
> - Every chart on a slide is one you produced in your notebook. No screenshots of other people's charts, no charts you cannot reproduce on request.
> - Every chart keeps its title and axis labels.
> - No slide of raw code. Code lives in the notebook; if the evaluator wants to see it, switch windows.
> - Maximum six lines of text per slide. If a slide needs a paragraph, it belongs in the notebook.
> - Google Slides, PowerPoint, Keynote, or exported PDF — any of them is fine.

**Edit 4 — checklist.** Add three `to_do` items after "The notebook contains a Summary section…":

> - [ ] Your slide deck has the five sections listed under "Your slide deck" and is between 5 and 7 slides
> - [ ] Every chart in the deck comes from your notebook, with title and axis labels
> - [ ] You have run through the deck once, out loud, and it fits in 10 minutes

**Edit 5 — submission instructions.** In both Option 1 and Option 2, add a final step: "Add your slide deck to the same Drive folder (or paste a second share link), with the same *anyone with the link can view* permission."

### A2 · DE mirror (`36194183-19f3-8080-84b2-fc8a490260e7`)

Same five edits. Ready-to-paste German (informal *du*, English product terms kept, per the house translation standard):

**Edit 1:**
> Dein Projekt hat zwei Deliverables: ein **Jupyter Notebook** und ein **kurzes Slide-Deck (5–7 Slides)**, das du am Präsentationstag präsentierst. Das Notebook ist ein kleiner schriftlicher Bericht — jemand, der die Daten noch nie gesehen hat, sollte es von oben nach unten lesen und verstehen können, was du getan und was du herausgefunden hast. Das Deck ist der Weg, auf dem du deinen Evaluator durch die zwei bis drei wichtigsten Dinge darin führst. Beides wird bewertet; beim Deck zählen Struktur und ob du deine Entscheidungen erklären kannst — nicht das Design.

**Edit 2:**
> Präsentiere aus deinem Slide-Deck, nicht aus dem Notebook. Halte das Notebook in einem zweiten Fenster offen — dein Evaluator wird dich bitten, zum Code oder zum Chart hinter einer deiner Aussagen zu springen, und das schnell zu können, ist Teil der Evaluation.

**Edit 3 — neuer Abschnitt „Dein Slide-Deck"** (vor „Was deine 10 Minuten abdecken sollten"):
> ## Dein Slide-Deck
>
> Fünf bis sieben Slides. Jede entspricht einem Block deiner 10 Minuten, damit Deck und Vortrag dieselbe Struktur haben.
>
> 1. **Titel + Datensatz** — dein Name, das Projekt und der Datensatz in einer Zeile (was er enthält, 50.000 Zeilen, welche Spalten du verwendet hast).
> 2. **Ansatz + was dir aufgefallen ist** — wie du das Projekt angegangen bist und was die erste Inspektion ergeben hat (inklusive der Datenqualitäts-Auffälligkeit in `Activity_Level`).
> 3. **Deine stärkste geführte Frage** — die Frage, ein Chart aus deinem Notebook und das Ergebnis in einem Satz. Eine oder zwei Slides.
> 4. **Deine eigene Frage** — warum du sie gestellt hast, ein Chart, das Ergebnis. Eine oder zwei Slides.
> 5. **Drei Erkenntnisse + was als Nächstes** — deine drei Erkenntnisse in deinen eigenen Worten und was du mit mehr Zeit untersuchen würdest.
>
> Regeln:
> - Jedes Chart auf einer Slide stammt aus deinem Notebook. Keine Screenshots fremder Charts, keine Charts, die du auf Nachfrage nicht reproduzieren kannst.
> - Jedes Chart behält Titel und Achsenbeschriftungen.
> - Keine Slide mit rohem Code. Code lebt im Notebook; wenn der Evaluator ihn sehen will, wechselst du das Fenster.
> - Maximal sechs Textzeilen pro Slide. Wenn eine Slide einen Absatz braucht, gehört sie ins Notebook.
> - Google Slides, PowerPoint, Keynote oder exportiertes PDF — alles ist in Ordnung.

**Edit 4 — Checkliste:**
> - [ ] Dein Slide-Deck hat die fünf Abschnitte aus „Dein Slide-Deck" und umfasst 5 bis 7 Slides
> - [ ] Jedes Chart im Deck stammt aus deinem Notebook, mit Titel und Achsenbeschriftungen
> - [ ] Du hast das Deck einmal laut durchgesprochen und es passt in 10 Minuten

**Edit 5:** "Lege dein Slide-Deck in denselben Drive-Ordner (oder füge einen zweiten Freigabelink ein), mit derselben Berechtigung *Anyone with the link can view*."

### A3 · `Health Data Explorer — Project Brief` (EN `36194183-19f3-80e0-a689-f859563e3eee`, DE `36194183-19f3-8003-b667-ce0b3f481683`)

Replace the deliverable sentence (EN):

> You will deliver a single Jupyter notebook that answers seven guided questions, three questions of your own, and ends with a written summary of what you found.

with (this also carries the scope change from workstream C — keep the two edits together):

> You will deliver two things: a **Jupyter notebook** that answers five guided questions, one question of your own, and ends with a written summary of what you found; and a **5–7 slide deck** for presentation day. Two further guided questions and two further own questions are marked *optional* below — they are there if you want to go further, and they can only help your evaluation, never hurt it. The slide structure is specified in *Submitting Your Project and Presentation Day*; read it before you start, not the night before.

DE:
> Du lieferst zwei Dinge ab: ein **Jupyter Notebook**, das fünf geführte Fragen und eine eigene Frage beantwortet und mit einer schriftlichen Summary deiner Findings endet; und ein **Slide-Deck mit 5–7 Slides** für den Präsentationstag. Zwei weitere geführte Fragen und zwei weitere eigene Fragen sind unten als *optional* markiert — sie sind da, wenn du weitergehen willst, und können deine Evaluation nur verbessern, nie verschlechtern. Die Struktur des Decks steht in „Dein Projekt einreichen und Präsentationstag" — lies sie, bevor du anfängst, nicht am Abend davor.

Also add, right after the dataset section, a short **Deliverables and effort** box:

> **Deliverables:** `YourName_HealthDataExplorer.ipynb` + a 5–7 slide deck, both shared as *anyone with the link can view*.
> **Plan for about 5–6 hours** of work on the notebook, plus about 1 hour for the deck and a run-through. Spread over the project window, that is roughly 2 hours a week. If you are spending much more than that, stop and bring it to a live session or Code Clinic — that is what they are for.

### A4 · `Introduction to you Project` (earlier module; EN `36194183-19f3-80a2-9f12-e05cacb95666`, DE `36194183-19f3-8052-adff-eb5e23f60c9e`)

Under "What the final deliverable looks like", the bullet list currently ends with "A short written summary." Add one bullet and one line:

> - A short slide deck (5–7 slides) that you present on presentation day.
>
> The notebook is the evidence; the deck is how you present it. Both are specified in detail when you reach the project.

Also update that page's question list to match the new required/optional split (C) — it currently lists all seven guided questions as "the seven guided questions". Change the heading to "The guided questions" and mark questions 3 and 5 as *(optional)*.

### A5 · Rubric alignment — **needs an owner, see §6-Q1**

No rubric for this project exists in Notion or in the Drive folders the LJ links to. It presumably lives in the evaluator tool. Until it is found, the rubric below is the proposal; it is written so the LJ text above *is* the rubric, which is what the feedback asks for ("instructors and students work from the same criteria").

| # | Criterion | Weight | What earns it | What the LJ says about it |
|---|---|---:|---|---|
| 1 | Notebook completeness | 25 | All required questions answered (5 guided + 1 own + summary), each with Markdown-before, code, chart, interpretation-after | Brief Part 1–3, final checklist |
| 2 | Correctness of the analysis | 20 | Right pandas operations for the question; filters and groupings do what the question asks; numbers in the text match the output | Brief per-question instructions |
| 3 | Charts | 15 | Chart type fits the data shape; title and axis labels present; readable | "Every chart has a title and axis labels"; walkthrough §Step 3 |
| 4 | Interpretation and summary | 20 | Says what results *mean*, not what the chart looks like; summary names three specific insights, a surprise, and a next step | Walkthrough §Step 4; Brief Part 3 |
| 5 | Presentation | 20 | Deck has the five required sections, 5–7 slides, fits 10 minutes; charts come from the notebook; student can explain choices and answer one follow-up | "Your slide deck" + the 10-minute breakdown |

**Explicitly not graded** (state this in the rubric, so the mismatch cannot recur): slide design/aesthetics; whether optional questions were attempted (bonus only — they can raise a borderline grade, never lower one); presenting from the notebook instead of slides is a structure deduction under criterion 5 only, not a correctness one.

---

## 3. Workstream C — project scope for a 3-week window

(Implemented in the same pages as A; listed separately because it is a separate decision.)

### C1 · Required vs optional

Today: 7 guided + 3 own + summary. Proposed: **5 guided + 1 own + summary required**, 2 guided + 2 own optional. Nothing is deleted — optional questions stay in the brief and in the starter notebook, marked *(optional)*.

Skill coverage, which is what the cut has to protect:

| Q | Skill it carries | Covered elsewhere? | Verdict |
|---|---|---|---|
| Q1 BMI category × gender | counts + percentages across a categorical, chart choice | no | **required** |
| Q2 mean BF% by activity level | single-key `groupby` + mean | no | **required** |
| Q3 % healthy BF%, smokers vs non | percentage of a precomputed boolean by one categorical | yes — same shape as Q2, same output as Q6 | *optional* |
| Q4 BMI distribution, age > 45 | numeric filter + `apply` on a column + distribution plot + subplots | no | **required** |
| Q5 gender × smoking | two-key `groupby` + `hue` barplot | partly — `hue` is drilled through all of Multivariate Analysis | *optional* |
| Q6 sedentary, healthy BF% by gender | row-wise `.apply(axis=1)` with a helper + countplot | no — only place row-wise apply appears | **required** |
| Q7 metrics across five age brackets | binning + multi-metric aggregation + summary DataFrame + lineplot | no — the capstone move | **required** |
| Own ×3 | question formulation under a constraint | — | **1 required** (must state its constraint *and* why the question matters), 2 optional |

The required five keep every distinct technique. The two that become optional are the two whose shape is already taught twice.

### C2 · Effort budget

| | Current scope | Proposed scope |
|---|---:|---:|
| Setup + inspection | 0.5 h | 0.5 h |
| Guided questions | 7 × ~35 min ≈ 4.0 h | 5 × ~35 min ≈ 2.9 h |
| Own questions | 3 × ~45 min ≈ 2.3 h | 1 × ~45 min ≈ 0.8 h |
| Summary | 0.5 h | 0.4 h |
| Polish, run-all, export, submit | 0.5 h | 0.4 h |
| Presentation prep | ~0.3 h (no slides) | ~1.3 h (deck + run-through) |
| **Total** | **~8.1 h** | **~6.3 h** |

Over a 3-week window that is ~2.1 h/week, on top of the recalibrated self-learn load in workstream B. Note that adding slides costs ~1 h, so the question cut has to be real for the net to come out lower — trimming only the own questions would not have been enough.

### C3 · Where C lands

- Brief (EN/DE): mark Q3 and Q5 *(optional — bonus)*, change Part 2 to "one question of your own (two more optional)", keep the three constraints but require only that the one question names its constraint and argues why it matters.
- Checklist item "All ten questions are answered — seven guided, three of your own" → "All six required questions are answered — five guided, one of your own (plus any optional ones you chose)". Same in DE ("Alle sechs Pflichtfragen sind beantwortet — fünf geführte, eine eigene (plus die optionalen, die du gewählt hast)").
- `health_explorer_starter.ipynb` (`1C9S20YwmRN-nRNx24zVxqy9m0t3_TfPd`): retitle the Q3/Q5 Markdown cells to "Question 3 *(optional)*" / "Question 5 *(optional)*", change "Seven questions to answer" to "Five required questions, two optional", change "Your Own Questions" intro to one required + two optional, and fix F7 by adding `message` to the About-the-dataset cell. Keep all placeholder cells.
- `health_explorer_solution.ipynb` / `Health_Data_Explorer_Solution.ipynb`: same required/optional labels so evaluators see the same thing.
- DE notebook copies in folder `1VkcNK9UIaYMfg1rqnAyQ2huUsbhY2DZS`.
- Rubric criterion 1 wording (§A5) already assumes 5+1.

### C4 · The "is the July GER cohort a special case?" question

Short answer: **do the scope reduction, but not because of that cohort.** The reason to do it is structural and applies to every future cohort — two modules per term put the project deadline on the Tuesday (Module A) or Thursday (Module B), which leaves ~3 weeks rather than 4, and the LJ load in those same weeks is the heaviest of the course (workstream B shows M2 at ~17 h and M3 at ~9 h of self-learn). A cohort-specific argument would be the wrong basis, and it is also unnecessary.

Two things keep this safe if the cohort *was* unusually weak: nothing is deleted (optional questions stay, and the rubric says they can only help), and the required five still cover every technique. If a later cohort sails through, the honest fix is to move questions back from optional to required, which is a one-line change in four places.

---

## 4. Workstream B — time estimates

### B1 · Method (so this can be re-run or argued with)

Every EN sublesson body was parsed. Per sublesson:

```
minutes = words / 110            # technical prose, first exposure
        + 1.5 × code_blocks      # read, type, run, read the output
        + 0.10 × code_lines      # long plotting scripts cost more than short snippets
        + 10 × campus_exercises  # embedded app.masterschool.com/campus/exercise: read, attempt, debug, check
        + 1.0 × quiz_toggles     # "Quick Questions" self-check items
        + 0.3 × screenshots
        + 3                      # open, orient, take notes
```

then rounded to the nearest 5 minutes. Setup/install lessons (Python + VS Code installs, Git, GitHub account, the AI hands-on build) and the five project pages are **not** model outputs — a model cannot see "PATH is wrong on Windows" or "spend 15 minutes on this question, don't look up the answer". Those are set by judgement and marked as such in the table.

Calibration check against the feedback ("40 min items taking 2–4 h"): the model puts the practice-heavy lessons at 2–4.5× their current value, which is the same ratio, and *lowers* the three pure-theory lessons (students were not complaining about those). Treat the numbers as a median for a first-timer; a student who is new to programming will still exceed them, which is an argument for the display policy in B3.

### B2 · Per-sublesson table

Current value is 20 min for every row. "Type" is how the page actually behaves: `concept` (read), `code-along` (read + run code), `practice` (embedded campus exercises), `setup/hands-on`, `project`.


### M1 Pandas Foundations

| Lesson | Sublesson | Type | Now | Proposed | Basis |
|---|---|---|---|---:|---:|
| Pandas Foundations | DataFrame Indexing and slicing with .loc[] | practice | 20 | **90** | 296w, 1cb/1ln, 8ex, 0q |
|  | DataFrame Indexing and slicing with .iloc[] | practice | 20 | **35** | 276w, 0cb/0ln, 3ex, 0q |
|  | Adding, Substracting and Modifying Column | practice | 20 | **55** | 610w, 14cb/69ln, 2ex, 0q |
|  | Aggregating Values | practice | 20 | **65** | 283w, 3cb/27ln, 5ex, 0q |
|  | Sorting Data | practice | 20 | **40** | 324w, 7cb/27ln, 2ex, 0q |
| **Pandas Foundations — total** |  |  | **100** | **285** |  |
| Data Wrangling | What is Data Wrangling? | concept | 20 | **10** | 327w, 0cb/0ln, 0ex, 3q |
|  | CRISP-DM and Data Wrangling | concept | 20 | **15** | 554w, 0cb/0ln, 0ex, 5q |
| **Data Wrangling — total** |  |  | **40** | **25** |  |
| Data Integration | What is Data Integration? | concept | 20 | **5** | 98w, 0cb/0ln, 0ex, 0q |
|  | Concatenating DataFrames | code-along | 20 | **35** | 285w, 8cb/65ln, 1ex, 1q |
|  | Concatenating Practice | practice | 20 | **50** | 144w, 0cb/0ln, 4ex, 5q |
|  | Merging DataFrame | code-along | 20 | **55** | 866w, 17cb/84ln, 1ex, 1q |
|  | Merging Practice | practice | 20 | **80** | 414w, 0cb/0ln, 7ex, 3q |
| **Data Integration — total** |  |  | **100** | **225** |  |
| Data Assessment | What is Data Assessment? | concept | 20 | **10** | 206w, 1cb/8ln, 0ex, 1q |
|  | DataFrame Assessment with Python | code-along | 20 | **50** | 720w, 14cb/97ln, 1ex, 1q |
|  | DataFrame Assessment with Python (2nd page — see A-H4) | practice | 20 | **25** | 98w, 0cb/0ln, 2ex, 0q |
| **Data Assessment — total** |  |  | **60** | **85** |  |

**M1 Pandas Foundations self-learn total: 300 min (5.0 h) → 620 min (10.3 h)**

### M2 Cleaning & EDA Basics

| Lesson | Sublesson | Type | Now | Proposed | Basis |
|---|---|---|---|---:|---:|
| Data Cleaning | What is Data Cleaning? | concept | 20 | **5** | 93w, 0cb/0ln, 0ex, 0q |
|  | Handling Missing Values | code-along | 20 | **50** | 990w, 13cb/77ln, 1ex, 1q |
|  | Handing Missing Values, Practice | practice | 20 | **50** | 352w, 0cb/0ln, 4ex, 5q |
|  | Handing Duplicates | code-along | 20 | **30** | 346w, 7cb/42ln, 1ex, 1q |
|  | Handling Duplicates, Practice | practice | 20 | **30** | 177w, 0cb/0ln, 2ex, 3q |
|  | Data Type Conversion | code-along | 20 | **35** | 306w, 10cb/34ln, 1ex, 1q |
|  | Data Type Conversion, Practice | practice | 20 | **40** | 355w, 0cb/0ln, 3ex, 6q |
|  | Cleaning Strings | code-along | 20 | **55** | 844w, 15cb/81ln, 1ex, 2q |
|  | Cleaning Strings, Practice | practice | 20 | **55** | 392w, 0cb/0ln, 4ex, 9q |
| **Data Cleaning — total** |  |  | **180** | **350** |  |
| Aggregating information | Grouping Data with groupby() | code-along | 20 | **35** | 497w, 7cb/68ln, 1ex, 1q |
|  | Group Data with groupby(), Practice | practice | 20 | **70** | 274w, 0cb/0ln, 6ex, 6q |
|  | Grouping Data in Pivot Tables | code-along | 20 | **30** | 451w, 4cb/54ln, 1ex, 1q |
|  | Grouping Data in Pivot Tables, Practice | practice | 20 | **70** | 301w, 0cb/0ln, 6ex, 6q |
| **Aggregating information — total** |  |  | **80** | **205** |  |
| Intro to Exploratory Data Analysis (EDA) | Introduction to Exploratory Data Analysis (EDA) | concept | 20 | **10** | 439w, 0cb/0ln, 0ex, 2q |
|  | Random Variables within EDA | concept | 20 | **15** | 927w, 0cb/0ln, 0ex, 4q |
| **Intro to Exploratory Data Analysis (EDA) — total** |  |  | **40** | **25** |  |
| Univariate Analysis | Introduction to Univariate Analysis | concept | 20 | **15** | 722w, 0cb/0ln, 0ex, 3q |
|  | Satistics for Univariate Analysis | code-along | 20 | **55** | 1422w, 14cb/91ln, 0ex, 10q |
|  | Satistics for Univariate Analysis, Practice | practice | 20 | **50** | 660w, 0cb/0ln, 3ex, 9q |
|  | Histograms | code-along | 20 | **25** | 730w, 6cb/69ln, 0ex, 0q |
|  | Histograms, Practice | practice | 20 | **45** | 468w, 0cb/0ln, 3ex, 10q |
|  | Density Plot | concept | 20 | **15** | 643w, 1cb/52ln, 0ex, 0q |
|  | Density Plots, Practice | practice | 20 | **30** | 210w, 0cb/0ln, 2ex, 4q |
|  | Box Plots | code-along | 20 | **25** | 790w, 7cb/29ln, 0ex, 0q |
|  | Box Plots, Practice | practice | 20 | **40** | 234w, 0cb/0ln, 3ex, 5q |
|  | Violin Plots | code-along | 20 | **20** | 735w, 6cb/27ln, 0ex, 0q |
|  | Violin Plots, Practice | practice | 20 | **30** | 215w, 0cb/0ln, 2ex, 5q |
|  | Bar Plots | code-along | 20 | **20** | 401w, 6cb/25ln, 0ex, 0q |
|  | Bar Plots, Practice | practice | 20 | **25** | 96w, 0cb/0ln, 2ex, 1q |
|  | Line Plots | code-along | 20 | **20** | 447w, 6cb/30ln, 0ex, 0q |
|  | Line Plots, Practice | practice | 20 | **30** | 176w, 0cb/0ln, 2ex, 3q |
| **Univariate Analysis — total** |  |  | **300** | **445** |  |

**M2 Cleaning & EDA Basics self-learn total: 600 min (10.0 h) → 1025 min (17.1 h)**

### M3 Advanced EDA & Project

| Lesson | Sublesson | Type | Now | Proposed | Basis |
|---|---|---|---|---:|---:|
| Bivariate Analysis | Introduction to Bivariate Analysis | concept | 20 | **10** | 455w, 0cb/0ln, 0ex, 4q |
|  | Correlation | code-along | 20 | **30** | 995w, 4cb/94ln, 0ex, 0q |
|  | Correlation, Practice | practice | 20 | **55** | 299w, 0cb/0ln, 4ex, 7q |
|  | Chi-Square Test | code-along | 20 | **15** | 171w, 3cb/33ln, 0ex, 0q |
|  | Chi-Square Test, Practice | practice | 20 | **35** | 309w, 0cb/0ln, 2ex, 10q |
|  | ANOVA | code-along | 20 | **30** | 1371w, 6cb/51ln, 0ex, 0q |
|  | ANOVA, Practice | concept | 20 | **20** | 211w, 1cb/4ln, 1ex, 3q |
| **Bivariate Analysis — total** |  |  | **140** | **195** |  |
| Multivariate Analysis | Multivariate Scatter Plot | concept | 20 | **20** | 289w, 2cb/111ln, 0ex, 0q |
|  | Multivariate Scatter Plot, Practice | practice | 20 | **35** | 212w, 0cb/0ln, 3ex, 0q |
|  | Multivariate Line Plot | concept | 20 | **15** | 89w, 1cb/70ln, 0ex, 0q |
|  | Multivariate Line Plot, Practice | practice | 20 | **25** | 98w, 0cb/0ln, 2ex, 0q |
|  | Mulrivariate Box Plot | concept | 20 | **10** | 140w, 1cb/53ln, 0ex, 0q |
|  | Mulrivariate Box Plot, Practice | practice | 20 | **45** | 199w, 0cb/0ln, 4ex, 0q |
|  | Mulrivariate Bar Plot | concept | 20 | **10** | 149w, 1cb/48ln, 0ex, 0q |
|  | Mulrivariate Bar Plot, Practice | practice | 20 | **25** | 86w, 0cb/0ln, 2ex, 0q |
| **Multivariate Analysis — total** |  |  | **160** | **185** |  |
| Project | From Functions to Findings — What EDA Is and Why It Matters | project | 20 | **15** | judgement (install/hands-on/project) |
|  | Health Data Explorer — Project Brief | project | 20 | **20** | judgement (install/hands-on/project) |
|  | Walking Through a Full EDA Question | project | 20 | **45** | judgement (install/hands-on/project) |
|  | Practicing the EDA Loop on Two Question | project | 20 | **60** | judgement (install/hands-on/project) |
|  | Submitting Your Project and Presentation Day | project | 20 | **20** | judgement (install/hands-on/project) |
| **Project — total** |  |  | **100** | **160** |  |

**M3 Advanced EDA & Project self-learn total: 400 min (6.7 h) → 540 min (9.0 h)**

### M4 Developer Tools & AI

| Lesson | Sublesson | Type | Now | Proposed | Basis |
|---|---|---|---|---:|---:|
| IDE: Visual Studio Code | Introduction to IDEs and Visual Studio Code | setup/hands-on | 20 | **10** | judgement (install/hands-on/project) |
|  | Python Installation | setup/hands-on | 20 | **25** | judgement (install/hands-on/project) |
|  | Visual Studio Code Installation | setup/hands-on | 20 | **15** | judgement (install/hands-on/project) |
|  | Setting Up VS Code for Python | setup/hands-on | 20 | **25** | judgement (install/hands-on/project) |
|  | Run Python Code | setup/hands-on | 20 | **15** | judgement (install/hands-on/project) |
|  | Debugger | setup/hands-on | 20 | **20** | judgement (install/hands-on/project) |
|  | Packages | setup/hands-on | 20 | **15** | judgement (install/hands-on/project) |
| **IDE: Visual Studio Code — total** |  |  | **140** | **125** |  |
| Git & GitHub | Overview | setup/hands-on | 20 | **15** | judgement (install/hands-on/project) |
|  | Git Commands | setup/hands-on | 20 | **35** | judgement (install/hands-on/project) |
|  | Branches | setup/hands-on | 20 | **30** | judgement (install/hands-on/project) |
|  | GitHub: Taking Your Code Online | setup/hands-on | 20 | **15** | judgement (install/hands-on/project) |
|  | Creating a GitHub Account | setup/hands-on | 20 | **15** | judgement (install/hands-on/project) |
|  | GitHub in VS Code | setup/hands-on | 20 | **30** | judgement (install/hands-on/project) |
| **Git & GitHub — total** |  |  | **120** | **140** |  |
| AI Enhancement: AI in Visual Studio Code | What are AI Agents | concept | 20 | **15** | judgement (install/hands-on/project) |
|  | Using AI Agents in Visual Studio Code | code-along | 20 | **25** | judgement (install/hands-on/project) |
|  | Hands On Exercise | code-along | 20 | **45** | judgement (install/hands-on/project) |
| **AI Enhancement: AI in Visual Studio Code — total** |  |  | **60** | **85** |  |

**M4 Developer Tools & AI self-learn total: 320 min (5.3 h) → 350 min (5.8 h)**

**All four modules: 1620 min (27.0 h) → 2535 min (42.2 h), +56%**

### B3 · How to apply these numbers

1. **Campus CMS is the only place the student-facing number lives.** The Notion DB has no duration property, so GPT cannot change what students see by editing Notion. Someone with campus CMS access enters the values (§6-Q2).
2. **Make Notion the source of truth anyway:** add a number property `Duration (min)` to DB `33594183-19f3-805f-a91c-fcb96b315fc6` and fill it from the table for all 81 EN sublessons, and the same value on each DE child page (DE pages are children of the EN page they translate, so the mapping is unambiguous). Lesson-level rows get the sum of their children. This makes the next recalibration a diff instead of another full audit.
3. **DE values are identical to EN** — same content, same exercises. No separate calibration.
4. **Order of entry:** M2 first (largest error, 600 → 1025), then M1 (300 → 620), then M3, then M4.

### B4 · Load balancing — the finding behind the finding

Recalibrated, the four modules are badly unbalanced:

| Module | Self-learn now | Recalibrated | + live sessions | Verdict |
|---|---:|---:|---:|---|
| M1 Pandas Foundations | 5.0 h | 10.3 h | +4 h | heavy but workable |
| M2 Cleaning & EDA Basics | 10.0 h | 17.1 h | +4 h | **overloaded** |
| M3 Advanced EDA & Project | 6.7 h | 9.0 h | +4 h (+ ~6.3 h project) | overloaded *with* the project |
| M4 Developer Tools & AI | 5.5 h | 5.8 h | +4 h | light |

Two cheap rebalancing moves, both worth proposing to the curriculum owner before the next cohort (they are **not** part of the implementation batch — they change the syllabus, not the text):

- **M2 is the problem, and `Univariate Analysis` is the reason** (445 min alone). It teaches six chart types as theory+practice pairs: histogram, density, box, violin, bar, line. Box and violin answer the same question, and bar and line reappear in full in Multivariate Analysis. Marking the **violin** pair and the **bar** pair as optional/extension removes ~75 min from M2 without losing a technique.
- **`Aggregating information` (205 min) sits in M2 but belongs with `Pandas Foundations`** (groupby/pivot is pandas mechanics, not EDA). Moving it to M1 makes M2 ≈ 13.7 h and M1 ≈ 13.7 h — still heavy, but even, and it puts groupby before the lessons that assume it.

Either move needs the campus module structure changed, so it is a syllabus decision, not an edit.

### B5 · Display policy (recommendation)

The numbers above are medians. For a cohort seeing Python for the first time, the P75 is roughly 1.4× on `practice` rows. Rather than inflating every estimate, state the convention once in each module intro: *"Time estimates assume you are seeing the topic for the first time and include the exercises. If a lesson takes you up to half again as long, you are not behind."* That is honest, and it stops the estimate from reading as a deadline.

---

## 5. Workstream D — content hygiene (found during the audit)

Small, student-visible, cheap. Not requested in the feedback — include or drop as a batch.

**D1 · Typos in sublesson titles.** Titles appear in the campus lesson list, so students see them. DE titles are listed for the same pass; most are already correct, but check for trailing spaces (`Histogramme   `, `Mulrivariate Box Plot `, `Boxplots `).

| Lesson | Current title | Proposed title | EN page id | DE page id | DE title (check too) |
|---|---|---|---|---|---|
| Project | `Practicing the EDA Loop on Two Question` | `Practicing the EDA Loop on Two Questions` | `36194183-19f3-80d2-9dd0-e810dd93887f` | `36194183-19f3-80c1-843e-eee7b2109c7b` | Den EDA-Loop an zwei Fragen üben |
| Multivariate Analysis | `Mulrivariate Box Plot` | `Multivariate Box Plot` | `35594183-19f3-802e-bdb3-c7dda5d1aac4` | `35594183-19f3-80a7-b3bf-d23223fecdc9` | Multivariater Box Plot |
| Multivariate Analysis | `Mulrivariate Box Plot, Practice` | `Multivariate Box Plot, Practice` | `35594183-19f3-80e0-beee-cf0fdf987a40` | `35594183-19f3-8046-a72d-e1cfaa85eb91` | Multivariater Box Plot, Übung |
| Multivariate Analysis | `Mulrivariate Bar Plot` | `Multivariate Bar Plot` | `35594183-19f3-8082-9b97-ceff7fe49596` | `35594183-19f3-807d-88c6-efe291e5b5fb` | Multivariates Balkendiagramm |
| Multivariate Analysis | `Mulrivariate Bar Plot, Practice` | `Multivariate Bar Plot, Practice` | `35594183-19f3-804b-a657-ea077c39e340` | `35594183-19f3-80e5-a222-f8f1e1beef52` | Multivariates Balkendiagramm, Übung |
| Univariate Analysis | `Satistics for Univariate Analysis` | `Statistics for Univariate Analysis` | `35594183-19f3-8003-bc9d-d73efbe7bd77` | `35594183-19f3-8050-a94c-e31f615b81e0` | Statistik für univariate Analysen |
| Univariate Analysis | `Satistics for Univariate Analysis, Practice` | `Statistics for Univariate Analysis, Practice` | `35594183-19f3-8053-854a-e0f7bb8c2eb1` | `35594183-19f3-802a-8887-d558ed4d84ef` | Statistik für univariate Analysen, Übung |
| Aggregating information | `Group Data with groupby(), Practice` | `Grouping Data with groupby(), Practice` | `35594183-19f3-8055-b114-c64e7fdfb10c` | `35594183-19f3-8084-ac21-ca51d5215899` | Gruppieren von Daten mit groupby(), Übung |
| Data Cleaning | `Handing Missing Values, Practice` | `Handling Missing Values, Practice` | `35594183-19f3-8063-95ac-c0f0190c616d` | `35594183-19f3-80e7-83ae-d334c67de453` | Umgang mit fehlenden Werten, Übung |
| Data Cleaning | `Handing Duplicates` | `Handling Duplicates` | `35594183-19f3-80a7-b280-e71b0a5cfe7e` | `35594183-19f3-8031-a275-f03b69f50245` | Umgang mit Duplikaten |
| Data Integration | `Concatenating Practice` | `Concatenating DataFrames, Practice` | `35594183-19f3-8037-a8c7-fb1525c6e1db` | `35594183-19f3-8043-88af-c76a58c50684` | Verkettung von Datenframes, Übung |
| Data Integration | `Merging DataFrame` | `Merging DataFrames` | `35594183-19f3-80e7-aa86-e187041157d1` | `35594183-19f3-80e7-98d4-d7e2e8835a15` | Zusammenführen von Dataframes |
| Data Integration | `Merging Practice` | `Merging DataFrames, Practice` | `35594183-19f3-8008-888d-cc60466bd21b` | `35594183-19f3-8095-afae-eef73a8557a2` | Zusammenführung von DataFrames, Übung |
| Pandas Foundations | `Adding, Substracting and Modifying Column` | `Adding, Subtracting and Modifying Columns` | `35594183-19f3-80f4-bed9-d5de2fb040a2` | `35594183-19f3-8072-9b25-ff92e71de5e9` | Hinzufügen, Subtrahieren und Ändern von Spalten |


**D2 · Duplicate title (F8).** `Data Assessment` has two sublessons titled `DataFrame Assessment with Python`:
- `35594183-19f3-8026-b94e-ef7822c3ddab` — the code-along (head/shape/dtypes/isnull/duplicated/unique + coding challenge). Keep the title.
- `35594183-19f3-80a8-9fbc-d04cb3f2b123` — two campus exercises on the Iris and Diabetes datasets. Rename to `DataFrame Assessment with Python, Practice` (DE: `DataFrame-Assessment mit Python, Übung`), matching the naming convention every other lesson uses.

**D3 · Submission step in the wrong place (F6).** *Submitting Your Project* says the submission platform is "in the next lesson", but the Codio *Submission* item is at the end of M4. Either move the Codio item to directly follow the project lesson in M3 (campus structure change — needs the same owner as B1), or, as a text-only fix GPT can make now, replace "in the next lesson" with "in the *Submission* item at the end of the *Developer Tools & AI* module" in EN and DE.

**D4 · Starter notebook misses the `message` column (F7).** Fixed as part of C3.

**D5 · Fragile walkthrough link.** In *Walking Through a Full EDA Question*, the Drive link to `health_explorer_walkthrough.ipynb` is the text of a `heading_2` block. It works, but it reads as a heading and breaks if the file moves. Make it a normal paragraph with a labelled link ("Download the walkthrough notebook"), EN and DE.

---

## 6. Open questions — do not guess these

**Q1 — Who owns the grading rubric, and where does it live?** It is not in Notion and not in the Drive folders the LJ links to; the LJ only refers to "your evaluator". The rubric in §A5 is a proposal. Implementation of A is incomplete until the real rubric is updated with the same five criteria and the same "not graded" list — otherwise this exact mismatch recurs next term. *Blocking for the "same criteria" half of feedback point 1.*

**Q2 — Who can edit time estimates in the campus CMS?** Workstream B's table is useless until someone enters it. Notion-side (`Duration (min)` property) GPT can do immediately.

**Q3 — Do Python live-session decks exist, and where?** The feedback asks that "the LJ instructions, LS and the grading rubric say the same thing". No Python LS deck was found in Notion or Drive (the LS databases that surfaced belong to other courses). If the decks exist, the presentation-day deck and the instructor notes need the same five-section structure pasted in; if they do not, presentation day is run from the LJ text alone, which makes A1's new section the single source.

**Q4 — Should the optional questions be removed from the evaluator's view entirely?** The §A5 proposal says optional work can raise a borderline grade but never lower it. If the evaluator tool cannot express that, the safer configuration is to hide optional questions from the rubric completely.

**Q5 — Are the module boundaries (B4) in scope this cycle?** The rebalancing proposals are the most effective single change for feedback point 2, but they move lessons between modules and so touch the campus syllabus, not just content.

---

## 7. Implementation order and acceptance

Suggested batching for GPT:

1. **Batch 1 — Notion text, EN** (A1, A3, A4 + the C3 wording inside them, D3, D5).
2. **Batch 2 — Notion text, DE** (A2 + DE mirrors of A3/A4/C3/D3/D5). Each DE page is the child of its EN page; translate with the house standard (informal *du*, EN product terms kept, no new content invented).
3. **Batch 3 — titles** (D1, D2), EN and DE.
4. **Batch 4 — notebooks** (C3): download from Drive, edit the Markdown cells, re-upload the same file IDs so the links in the LJ keep working. Do not touch code cells or placeholder cells.
5. **Batch 5 — Notion `Duration (min)` property** (B3 step 2) for 81 EN + 81 DE pages.
6. **Hand back** to the humans: rubric (Q1), campus time entry (Q2), LS decks (Q3), module rebalancing (Q5).

Acceptance checklist:

- [ ] No page in either language contains "You don't need slides" / "Du brauchst keine Slides" or any other statement that slides are unnecessary.
- [ ] The deliverable is described as *notebook + 5–7 slide deck* in all four places (Intro to your Project, Brief, Submitting, starter notebook) and in both languages.
- [ ] The slide structure appears exactly once as the authoritative version (Submitting), and every other page links to it rather than restating it.
- [ ] Required scope reads *5 guided + 1 own + summary* everywhere, with Q3/Q5 and own-questions 2–3 labelled optional; no question text was deleted.
- [ ] The final checklist no longer says "all ten questions".
- [ ] Starter notebook: required/optional labels match the brief; `message` is in the dataset description; all placeholder cells intact; file opens in Colab.
- [ ] `Duration (min)` is set on all 162 sublesson pages and the 14 lesson rows carry the sum of their children.
- [ ] DE pages differ from EN only in language — no DE page carries an instruction the EN page does not.

---

## 8. Appendix — raw audit data

Per-sublesson content metrics (words, code blocks, code lines, campus exercises, quiz toggles) and the computed estimates are in the table in §B2; the basis column carries the raw counts, so any single row can be recomputed with the formula in §B1 without re-reading the page.

Totals: 81 EN sublessons, 42,840 words of prose, 226 code blocks (1,592 lines), 102 embedded campus exercises, 1,630 min currently displayed across the four modules (including the 10-min Codio submission item), 2,535 min proposed for the 81 lessons.
