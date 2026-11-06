# Tu3 — Mock Fachgespräch — Question Bank (1)

https://app.notion.com/p/Tu3-Mock-Fachgespr-ch-Question-Bank-1-3aa9418319f3807dabb1e7991b532f1f


Internal document for tutors. Use to prepare students for the individual Fachgespräch and to calibrate readiness. Questions are in German because the Fachgespräch is conducted in German.
---
## How to Use
Use these questions selectively during the regular group check-ins or for independent exam preparation. Cover all four chapters over the preparation period, but go deeper on one or two. Use the strong/weak answer notes to calibrate your verdict.
Format of each question:
- Frage — exact question to ask, in German.
- What to look for — what a strong answer covers.
- Weak answer pattern — typical weak / not-ready response.
- Follow-up — optional probe if the first answer is shallow.
---
## Chapter 1 — Current Situation and Relevance
### Question 1.1
"Bitte beschreiben Sie in zwei Sätzen, vor welchem Problem die Organisation in Ihrem Projekt steht."
- What to look for: Name of the organisation, concrete industry, the observed business problem (e.g. "turnover rate of 17%") — not generic.
- Weak answer pattern: "The company has a data problem." (too vague, interchangeable)
- Follow-up: "Why now? What has changed?"
### Question 1.2
"Welche Analytics-Prozesse nutzt die Organisation bereits heute — und welche Lücke schließt Ihr Projekt?"
- What to look for: Specific existing tools or reports (e.g. "quarterly Excel reports") plus a clear description of the gap.
- Weak answer pattern: "They don't have anything." — rarely realistic.
- Follow-up: "Who manages those existing processes today, and how would our model complement rather than replace them?"
### Question 1.3
"Was wäre der konkrete Nutzen für die Organisation, wenn Ihr Modell morgen produktiv gehen würde?"
- What to look for: Quantified (EUR, customers, incidents avoided) — not "better business outcomes".
- Weak answer pattern: Generic statements without numbers.
- Follow-up: "What assumption are you using to arrive at that figure?"
---
## Chapter 2 — Machine Learning Canvas
### Question 2.1
"Bitte erklären Sie Ihren Canvas in drei Sätzen — das Geschäftsproblem, die Vorhersage, die Entscheidung."
- What to look for: Three coherent sentences. Prediction and decision fit together logically.
- Weak answer pattern: Reads out fields one by one; cannot connect the thread.
### Question 2.2
"Warum diese Vorhersage-Art — Klassifikation, Regression oder Anomalie-Erkennung?"
- What to look for: Reasoning grounded in the data and the business question (e.g. "because the target variable is binary and we need actionable thresholds").
- Weak answer pattern: "Because that's what we learned." / "Because it was in the example."
### Question 2.3
"Welche Evaluation-Metrik passt zu Ihrer Aufgabe — und welche passt nicht?"
- What to look for: Conscious choice with reference to class imbalance / time series context. Explains why accuracy is (un)suitable here.
- Weak answer pattern: "Accuracy is 83%, that's good." (on imbalanced classification)
- Follow-up: "What would the accuracy be if you always predicted the majority class?"
### Question 2.4
"Welches Feld in Ihrem Canvas war am schwersten zu füllen, und warum?"
- What to look for: An honest answer — often Impact or Decision. Shows reflection.
- Weak answer pattern: "They were all easy." (never true)
### Question 2.5
"Würden Sie ein Feld in Ihrem Canvas heute anders schreiben? Welches und warum?"
- What to look for: One specific field, one concrete improvement.
- Weak answer pattern: "No, it's perfect." — usually a red flag.
---
## Chapter 3 — Project Planning and SCRUM
### Question 3.1
"Wie haben Sie die drei Sprints geplant — und was war Ihre größte Anpassung zwischen Sprint 1 und Sprint 3?"
- What to look for: A concrete adjustment (scope reduced, tool switched, task reassigned), with reasoning.
- Weak answer pattern: "We did everything as planned." (rarely true; usually a sign of retrospective documentation)
### Question 3.2
"Welche Aufgabe haben Sie persönlich verantwortet, und wie würden Sie das Ergebnis dieser Aufgabe heute verteidigen?"
- What to look for: A clear individual section, concrete defence.
- Weak answer pattern: "We did it together." (individual visibility missing — violates IHK requirement)
### Question 3.3
"Zeigen Sie mir eine User Story aus Ihrem Sprint-Log und erklären Sie den Bezug zum Endergebnis."
- What to look for: A real user story in the format "As X I want Y so that Z"; link to a report section or model decision.
- Weak answer pattern: A task dressed up as a user story.
### Question 3.4
"Was war Ihr persönliches größtes Learning aus diesem Projekt?"
- What to look for: Specific and methodological or technical — not "teamwork is important".
- Weak answer pattern: Generic statements.
---
## Chapter 4 — Workflow, Data Model, Results
### Question 4.1
"Bitte führen Sie mich in 90 Sekunden durch Ihren Workflow — von der Rohdatei bis zum Modell-Output."
- What to look for: Clear sequence, all 7 steps covered (source → import → cleaning → transformation → analysis → visualisation → export).
- Weak answer pattern: "We loaded the data and trained the model." (skips 5 steps)
### Question 4.2
"Welche Datenqualitäts-Probleme haben Sie gefunden, und wie haben Sie sie behandelt?"
- What to look for: At least 4–5 problems named with a concrete action (drop / impute / cap / flag) and reasoning.
- Weak answer pattern: "We cleaned the data."
- Follow-up: "On the imputation — why median rather than mean?"
### Question 4.3
"Warum diese Train/Test-Aufteilung?"
- What to look for: For time series (datasets 03 + 06): time-based split justified. For others: stratified + why.
- Weak answer pattern: "test_size=0.25 is standard."
- Follow-up (for time series): "What would happen if you split randomly?"
### Question 4.4
"Welches Merkmal trägt im Modell den größten Beitrag — und ist das geschäftlich plausibel?"
- What to look for: Specific feature named, reflection on plausibility, caveats where relevant (e.g. "salary ranks highly but as a proxy for seniority — the real driver is seniority").
- Weak answer pattern: "The model says so."
### Question 4.5
"Hätten Sie mehr Zeit gehabt — welche eine Verbesserung am Modell hätte den größten Effekt?"
- What to look for: Concrete and prioritised (feature engineering / more data / different model / hyperparameter tuning).
- Weak answer pattern: "More features." (too vague)
### Question 4.6
"Welche Entscheidung in der Bereinigung würden Sie heute anders treffen?"
- What to look for: A specific decision, honest reflection.
- Weak answer pattern: "We did everything correctly."
---
## Ethics and Responsibility
### Question E.1
"Welche Merkmale haben Sie bewusst NICHT in das Modell aufgenommen — und warum?"
- What to look for: At least one feature with reasoning (e.g. gender, insurance_type, driver_id).
- Weak answer pattern: "We used all the columns."
### Question E.2
"Wenn Ihr Modell falsch liegt — welche Konsequenz hat das im Geschäft, und wer ist davon betroffen?"
- What to look for: False positives and false negatives distinguished; stakeholders named.
- Weak answer pattern: "The model is good, it doesn't get things wrong."
### Question E.3
"Wie nutzen Sie KI in Ihrer Projektarbeit — was war akzeptabel, was haben Sie bewusst nicht delegiert?"
- What to look for: Thoughtful use: AI as a language aid / structuring tool, own analysis as core responsibility.
- Weak answer pattern: "We didn't use AI." (often untrue and unreflective) or "AI did everything for us." (instant red flag)
---
## Instant Red-Flag Answers
If a student gives any of the following responses, it is a clear "not ready" signal:
- "The team did that, I can't say much about it."
- "That's just how it is in the code."
- "We took it from the example, I don't know why."
- "ChatGPT wrote that — I'll explain it if you show me the code."
An honest "We didn't analyse that — if I had to do it now, I would…" is not a red flag. That is good, professional gap communication.
---
## Language, Presence, and Structure Observations
Note during the conversation:
[TABLE]
  | Criterion | Points (max) | Notes |
  | Content accuracy and structure | 16 |  |
  | Language (clarity, sentence structure, use of pauses) | 8 |  |
  | Presence (eye contact, free speaking, delivery) | 6 |  |
  | Total | 30 |  |
