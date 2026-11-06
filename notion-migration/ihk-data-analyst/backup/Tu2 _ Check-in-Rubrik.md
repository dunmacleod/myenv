# Tu2 — Check-in-Rubrik

https://app.notion.com/p/Tu2-Check-in-Rubrik-38b9418319f380bf974ace94dff73948

Internal document. To be used during every group check-in to assess progress against expected deliverables. Notes go into the group's check-in log (Google Sheet from the check-in-notes template — see Tu1 §9).
---
### How to Use This Rubric
One 30-minute group check-in per sprint. Use the Current progress rows to assess where the group is now and the Sprint-end targets rows to agree the remaining priorities for the week. In each check-in:
1. Open this rubric alongside the group's sprint log.
1. Work through the four chapters in order. Don't try to cover everything in 30 minutes — focus on the chapters most at risk.
1. For each criterion, assign one of the six IHK ratings: +++, ++, +, −, −−, −−− (consistent with T5).
1. For each amber/red point, write a one-sentence feedback formulation — send it to the group directly in the chat after the call.
1. Close every check-in with: "What is the single most important thing to get done in the next three days?"
---
### Universal Signals (apply in every check-in)
[TABLE]
  | Signal | Green (+++/++) | Amber (+/−) | Red (−−/−−−) |
  | Sprint log is current | Updated daily; tasks individually owned; decisions documented with reasoning | Updated weekly; some tasks without an owner | Empty or last updated more than 4 days ago |
  | Every member can explain their section | Each person walks confidently through their own work | One person dominates, others are passive | One person cannot describe what their section is about |
  | Decisions vs. improvisation | Decisions are documented with reasoning | Decisions were made but not written down | Choices were made; nobody can say why |
  | Responsible AI use | AI used for writing / polishing / structuring; content is explainable | Group cannot explain a paragraph or a feature choice | Entire sections clearly AI-generated; nobody can defend them |
---
### Sprint 1 — Check-in 1
Sprint focus: Problem definition, dataset exploration, Chapter 1 draft, ML Canvas started (fields 1–2), sprint log running.
#### Current progress
[TABLE]
  | Point | What to look for | Red flag |
  | Project brief read together | All three members can summarise the business problem in one sentence | Group only skimmed the brief; nobody knows the company name |
  | Dataset downloaded and opened | Group has loaded the CSV in their chosen tool; reports first headline figures | "Not opened yet" |
  | First data quality check | Group has spotted at least 2–3 quality issues (missing values, formats, duplicates) | "Looks fine" — group hasn't really looked |
  | Task split agreed | Each member has a clear area of ownership | Roles still open — flag immediately |
  | Sprint log active | Template imported; first tasks entered | Template not yet imported |
Sample feedback formulations (copy & paste into chat):
- "Please add a one-sentence description of the business problem to the sprint log notes by tomorrow morning."
- "Watch the CSV encoding — utf-8-sig matters here."
#### Sprint-end targets
[TABLE]
  | Point | What to look for | Red flag |
  | Chapter 1 draft (current situation) | 1–2 pages, grounded in the company, existing analytics processes named | Generic text with no company-specific content |
  | Data quality inventory complete | Group can name 5+ engineered issues | Only the obvious problems spotted — typos and mixed formats missed |
  | ML Canvas: fields 1 and 2 | Both filled in, framed in business language | Fields filled with technical jargon instead of business language |
  | 3–5 user stories | Format: "As a <role> I want <goal> so that <benefit>." | Tasks disguised as user stories |
  | Sprint 1 retrospective done | Group can name 1 "keep" and 1 "change" | "It went fine" — no real retro |
---
### Sprint 2 — Check-in 2
Sprint focus: Data cleaning, full ML Canvas (all 10 fields), EDA, workflow documentation started, ethics discussion happened.
#### Current progress
[TABLE]
  | Point | What to look for | Red flag |
  | Cleaning pipeline documented | One documented decision per engineered issue (drop / impute / cap / flag) with reasoning | Cleaning happened but decisions aren't written down |
  | Date formats parsed | All date columns are a true date type | Dates still stored as text — group hasn't noticed |
  | Categorical normalisation | Typo mappings are explicit; canonical values visible | Group called lower() and considers it done |
  | Outlier treatment defensible | Every outlier is kept / capped / dropped / flagged with reasoning | Outliers silently removed |
  | Workflow documentation draft | Source → import → cleaning are written up | Workflow documentation empty |
#### Sprint-end targets
[TABLE]
  | Point | What to look for | Red flag |
  | All 10 Canvas fields filled | Each field 1–3 sentences; fields are coherent (Prediction fits Evaluation fits Decision) | Two or more fields empty; or Evaluation = "Accuracy" on imbalanced classification |
  | EDA produces ≥ 4 insights | Quantified (e.g. "Churn rate is 36% for satisfaction ≤ 2 vs. 10% for ≥ 4") | Vague claims ("there is a relationship") |
  | Ethics discussion happened | Group can explain which features they kept, which they excluded, and why | No discussion; or "we don't care, the data is synthetic" |
  | Sprint 2 retrospective done | Real learnings documented | Skipped |
---
### Sprint 3 — Check-in 3
Sprint focus: Modelling, dashboard, complete report draft, submission.
#### Current progress
[TABLE]
  | Point | What to look for | Red flag |
  | Model trained | At least one model on the cleaned dataset with plausible metrics | No model yet |
  | Train/test split defensible | Time-based for time series (datasets 03 and 06); stratified random split otherwise. Reasoning documented. | Random split on a time-series dataset |
  | Metric fits the task | Recall / ROC-AUC for classification; RMSE / MAE / R² for regression; Precision@K or residual threshold for anomaly | "Accuracy is 83%" on imbalanced classification, with no further explanation |
  | Feature importance interpretable | Group can name the top 3 features and discuss their business plausibility | "The model says X" with no sanity check |
  | Dashboard exists | At least one chart carrying the final story | No visualisation yet |
#### Sprint-end targets
[TABLE]
  | Point | What to look for | Red flag |
  | All 4 chapters drafted | Report has current situation + Canvas + project planning + workflow at near-final quality | One chapter less than 50% drafted |
  | Sprint log feeds Chapter 3 | Chapter 3 is built from sprint log entries, not reconstructed | Sprint log was empty mid-sprint and Chapter 3 is retrofitted |
  | Workflow documentation complete | Source → import → cleaning → transformation → analysis → visualisation → export all written up | One or more steps missing |
  | Report formatting compliant | 1.5 line spacing, 2.5 cm margins, Arial/Times 12pt, 10–15 pages | Wrong margins, wrong font, length out of range |
  | Every member can explain their section | Cold-call per member: "explain section X in 90 seconds" | Member cannot explain |
---
### Finalisation Week — No Individual Tutor Session
There is no separate tutor session in Week 4. Use the readiness criteria below as an internal reference based on evidence from the three group check-ins and the submitted work.
[TABLE]
  | Readiness criterion | What to look for | Red flag |
  | Walks through their own section without notes | Confident 2–3 minute walkthrough | Reads from slides; freezes when asked to summarise |
  | Defends every Canvas field for the group | One sentence per field, without hesitation | "I don't remember what we wrote for Decision" |
  | Explains a cleaning decision | "We chose median imputation because…" | "I think we used median… or maybe drop…" |
  | Defends the chosen metric | Articulates why accuracy is (un)suitable | "We used whatever was in the example" |
  | Handles a challenge confidently | "A fair point — in our dataset this was the case because…" | Defensive, makes things up, or freezes |
  | Says "I don't know" cleanly | "We didn't analyse that. If I had to do it now, I would…" | Pretends to know |
Readiness verdict before exam day:
- Ready — person passes all green/amber points, no reds.
- Not ready — person has one or more red points. Document the reasoning in the group's check-in log (Google Sheet · Bereitschaft tab). Communicate to Masterschool staff and to the student — friendly but clear.
---
### Common Feedback Formulations (copy & paste)
- "Please add one line per cleaning decision to the sprint log, with reasoning."
- "Your evaluation metric doesn't fit the class distribution — Recall or ROC-AUC would be more robust here."
- "Can you defend this feature choice in the Fachgespräch? If not, either justify it better or leave it out."
- "Your model is looking good. Please rehearse the workflow demo three times with a stopwatch — you need 15 minutes, not 25."
- "In the Fachgespräch you will be asked why you chose this split. Write your answer down now."