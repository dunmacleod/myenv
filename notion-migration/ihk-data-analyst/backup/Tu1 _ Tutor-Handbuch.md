# Tu1 — Tutor-Handbuch

https://app.notion.com/p/Tu1-Tutor-Handbuch-38b9418319f38036aa93f4b335c8c408

Internal document. Reference for tutors accompanying a cohort of the IHK Certificate Programme Data Analyst (IHK).
---
## 1. Your Role in One Paragraph
You accompany some groups of three students through a four-week IHK data project. During the three active sprints, you run one 30-minute group check-in per week; in the finalisation week, there is no additional individual tutor session, and you attend the exam day (60 minutes per group). You are not a tutor in the SQL/Python/BI sense — the group brings those competencies from the program. Your job is to keep the project structurally on track, surface risks early, challenge the group's thinking, and issue a readiness verdict per person before the real exam.
---
## 2. The 3+1 Rhythm
[TABLE]
  | Week | What students do | What you do |
  | Sprint 1 | Problem definition + dataset exploration + Chapter 1 draft + ML Canvas fields 1–2 + sprint log running | 1 group check-in (30 min) — focus: scope, data quality awareness, Chapter 1 grounded in the actual company |
  | Sprint 2 | Data cleaning + ML Canvas complete + EDA + workflow documentation started | 1 group check-in (30 min) — focus: cleaning decisions are defensible, Canvas is coherent, ethics discussion happened |
  | Sprint 3 | Modelling + dashboard + report draft and submission | 1 group check-in (30 min) — focus: model choice, metric suitability, report is ready to submit |
  | Finalisation | Polishing, presentation rehearsal, individual Fachgespräch preparation | No separate tutor session + exam day (60 min/group) |
---
## 3. What Check-ins Are and What They Are Not
Check-ins are:
- a 30-minute progress review against the expected sprint deliverables,
- a space where the group surfaces blockers and decisions,
- a coaching moment — challenge the group's thinking, don't give them the answers,
- an early warning system — you spot drift before the report is submitted.
Check-ins are not:
- SQL / Python / Tableau tutoring (the group brings that competency),
- code review,
- a debugging session,
- a space for you to dictate decisions — students must be able to defend the project themselves.
If a group asks "How do I write this SQL query?" or "Why is my Pandas merge failing?" — redirect: that is program-level competency. If they ask "Should we remove these rows or impute them, and how do we defend that choice in the exam?" — that is your job.
---
## 4. Materials You Work With
[TABLE]
  | Artefact | Where it lives | Purpose |
  | Dataset bundles | datasets/0X_* |  |
  | https://drive.google.com/drive/folders/1mQ0ULunRxKNkPz0T4LL8K5IM_ihY-5Na | Each group works on one of the six datasets. Read the corresponding instructor_key.md before the first check-in. |  |
  | Templates | Campus - Shared with students | Sprint log (T1), report (T2), ML Canvas (T3), presentation (T4), IHK rubrics (T5). |
  | Check-in rubric | Tu2 — Check-in-Rubrik | Per sprint: expected deliverables + green/amber/red signals + feedback formulations. |
  | Fachgespräch question bank | Tu3 — Fachgespräch — Question Bank | ~25 sample questions for Fachgespräch preparation, organised by chapter. |
  | Live session plans | ‣ | LS-A Kick-off (maintenance notes for the existing slide deck) and LS-B SCRUM (full session plan). |
---
## 5. The Two Live Sessions in Week 1
Both take place in Week 1, in this order:
- LS-A — Project Kick-off (1 hour). Exam format, group formation, dataset assignment, AI use. The slide deck lives in the Cohort Workspace; before each cohort, check it against the maintenance table in ‣ .
- LS-B — SCRUM Session (1 hour). Practical, not theoretical. Each group leaves the session with a filled-in sprint log and a planned Sprint 1. Full plan in ‣ .
---
## 6. AI Policy — What to Communicate to Students
The exam board does not test whether students used AI. It tests whether students can explain and defend everything in the report themselves. The boundary:
- Acceptable: drafting text, polishing German style, structuring sections, generating example sentences, summarising sources, learning a function from the documentation.
- Not acceptable: AI-generated analysis that the student cannot reproduce or explain in their own words.
If a student cannot explain a number, a feature choice, a cleaning decision, or a Canvas field when challenged during a group check-in — that person is not ready. AI-generated content is the most common cause.
Make this explicit in your first check-in.
---
## 7. The Readiness Verdict
Before exam day, you give each person a "Ready" or "Not ready" verdict. Anyone who is "Not ready" does not sit the real exam in this cohort — they apply for the next one. This protects the student (prevents a fail result on their certificate) and protects Masterschool's quality relationship with the IHK.
A person is ready when all of the following apply:
- Can explain every section of the group project without notes.
- Can defend every Canvas field in one sentence.
- Can justify the cleaning decisions and the chosen evaluation metric.
- Can answer "What would you do differently today?" with a real answer.
- Says professionally "I don't know" when something was genuinely out of scope.
A person is not ready if any of these signals appear:
- They recite the report verbatim but cannot paraphrase or defend it in their own words.
- They cannot explain a number or a chart from their own dashboard.
- They refer to "the model" without being able to name the model type or the evaluation metric.
- They become evasive under pressure — or conversely, start making things up.
When in doubt: ask the person to walk through the workflow live. Anyone who gets stuck at a cleaning step they signed off on is not ready.
---
## 8. Escalation Paths
[TABLE]
  | Situation | What to do |
  | Group is behind in Sprint 1 | Adjust scope early. Drop stretch goals; protect the four chapters. |
  | Conflict within the group | Acknowledge it, repeat the IHK rule on individual visibility, make the task split more explicit. If unresolved by mid-Sprint 2 — escalate to MSIT staff. |
  | Plagiarism / clearly AI-generated content | Show the student the passage and ask them to explain it. If they can't — not ready. Document in your notes. |
  | Technical incident (data loss, tool outage) | Group should document the workaround in the sprint log. Workflow documentation should mention the contingency. |
  | Health or personal emergency | Escalate to MSIT staff. Do not make eligibility decisions on your own. |
---
## 9. Documentation You Maintain
For each group, maintain a single tutor-only Google Sheet (copy of the check-in-notes template — https://drive.google.com/drive/folders/1QA1nEZpqbjcRdMjN9LChU-eIWcHC0-zj?usp=drive_link ) named checkin_notes_cohort<XY>_group<N>.xlsx and saved in the tutor Drive folder (https://drive.google.com/drive/folders/1QA1nEZpqbjcRdMjN9LChU-eIWcHC0-zj?usp=drive_link), with:
- members and dataset assignment,
- date of each check-in + 3-point summary,
- flagged risks,
- readiness verdict per person with a one-paragraph justification.
This is your reference for the readiness decision and for any post-exam debrief with MSIT staff.
---
## 10. Quick Reference
[TABLE]
  | Question | Answer |
  | Tutor time per group per week | Weeks 1–3: 1 × 30 min group check-in. Week 4: no individual tutor session. Exam day: 60 min/group. |
  | Sprint length | 1 week; 3 active sprints + 1 finalisation week |
  | Pass threshold | ≥ 50% in both parts (70-pt report and 30-pt oral), independently |
  | Report submission | set per cohort by MSIT — typically end of Sprint 3 / start of finalisation week |
  | Exam day | A single day; 60 minutes per group. IHK representative + MSIT tutor jointly decide pass/fail. |
---