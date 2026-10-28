# Project submission instructions

Notion page: https://app.notion.com/p/Project-submission-instructions-3c79418319f381ecb219d76bb57e0067
Backed up before n8n migration

## 1. Intro
The redesign is done and the tests have been run. This page is the close of the module project: what to gather, how the presentation works, what the evaluator is listening for, and how to hand the work over.
Across four sprints you produced a set of deliverables that build on each other — the architecture decision brief that names the pattern, the multi-agent design diagram that shows how the agents relate, the memory and state specification that describes what the system knows and what it forgets, and the redesigned canvas with the test record that proves it behaves the way the specification says. The teaching canvas came away in Sprint 4. What you submit is your own architecture on your own domain.
The skills you've been practicing across the module:
- Reading a business case and translating it into an architecture decision that can be defended against the alternative you rejected
- Deciding when one agent is enough and when multiple agents earn their coordination cost
- Defining specialisations, boundaries, and routing strategies for a multi-agent design
- Drawing memory and state boundaries — what is shared, what is private, what must never persist
- Designing failure isolation and state recovery so one agent's failure does not corrupt shared state
- Implementing the design on an Agentflow V2 canvas and testing it against the failure modes you designed for
- Separating implementation from validation — a canvas that has been configured is not yet a canvas that has been verified
## 2. Tasks
The submission draws on one deliverable per sprint, plus the integration work.
1. Sprint 1: Architecture decision. The one-page architecture decision brief covering the six sections — decision, pattern, inputs and outputs, the three pillars, rejected alternative, and the conditions under which you would revisit the decision.
1. Sprint 2: Multi-agent design. The design diagram with every agent named, information flow shown, routing decision points marked, information boundaries called out, and at least one fallback path — plus the written design rationale covering diagnosis and justification, agent roles, the information boundary, and the fallback strategy.
1. Sprint 3: Memory and state architecture. The four-section specification: the memory boundary map with persistence scope, what must not persist and how each item is prevented, the state recovery design naming the failure scenario and the safe state, and the failure isolation assessment of which agents may write to which state keys.
1. Sprint 4: Integration and testing. The redesign in four stages — archetype staged on the canvas, memory boundaries enforced, state handoff and recovery wired, and the five safeguards confirmed. Then the nine tests in three groups: baseline function, boundary conditions, and architecture-specific validation. Refine until each safeguard holds under the test it was designed for, and export the canvas.
## 3. Project artifacts
Three layers: what you build, how well you can explain it, and a short written summary connecting the pieces together.
### Technical artifacts
By submission day you should have:
- The final canvas exported as JSON — the version produced after the testing work, loadable in a fresh Flowise instance without missing configuration. Keep the earlier exports; the final one is what you submit.
- The architecture decision brief from Sprint 1 — one page, six sections, tied to the business problem you chose.
- The multi-agent design diagram — updated to reflect the implemented architecture, not the Sprint 2 draft. If the canvas changed during the redesign, the diagram changes with it.
- The written design rationale from Sprint 2 — no more than 400 words, with the rejected alternative noted where applicable.
- The memory and state architecture specification from Sprint 3 — all four sections, updated if the redesign added or removed state keys.
- The test record — the nine tests across the three groups, with the expected behaviour written before the run and the actual behaviour logged after, plus what you changed as a result and any test you could not run and why.
### Analytical reasoning
For your presentation, you should be able to explain:
- Why you chose the archetype you chose. What property of your business problem made it fit? What was the rejected alternative, and why was it rejected?
- Why the design divides responsibilities where it does. What is the boundary statement between agents, and what happens at a query that straddles two of them?
- Why the memory boundaries sit where they sit. What is shared and why, what is private and why, what must never persist and why.
- What happens when a specialist fails — what detects it, what gets reset, and in what order control returns.
- What the tests revealed. Where did one confirm a design decision, and where did one expose a gap that forced a change to the canvas or the specification?
- What you would do with another week. Specific, not "make it better".
### Written summary
A short PDF, one to two pages, that ties the whole project together. Include:
- A one-paragraph problem framing: what your business problem is and why the design work matters for it.
- A one-paragraph solution overview: what your architecture does and what shape it has.
- Two or three bullet points naming the most interesting decisions you made across the four sprints, with the alternative you considered and rejected.
- A one-paragraph reflection on what your testing revealed and one limitation you could not fully resolve.
The summary is for someone who has not seen your presentation. It should read independently.
## 4. Presentation
The presentation is mandatory and is the main evaluation method for this project.
Format: Live, in front of the cohort, with Q&A. Target time: 5–7 minutes for the presentation itself, plus a few minutes of Q&A. Aim for the middle — a tight 6 minutes is better than a rambling 7.
The presentation has three components. All three are required. A presentation that covers only the canvas without the diagram, or the diagram without the design decisions, is incomplete.
### Component 1: The canvas, live
A live run of your redesigned canvas. The execution trace shows which nodes activated, in what order, and what was written to state — and that is what the room will be watching, not only the reply text.
Have two queries ready: one that takes the most common path through your architecture, and one that exercises a boundary condition — the scope edge or the recovery path. You may not get to both, but having both ready lets you answer if the instructor asks to see a specific path.
### Component 2: The system diagram
The diagram is the visual anchor for the defense. When you name a design decision out loud, the diagram should show it. It does not need a particular tool; it needs to be legible on a shared screen and accurate. If the diagram shows three specialists and the canvas has two, that discrepancy will be the first question.
### Component 3: The defense
A verbal account of the design decisions, covering the three areas that correspond to the sprint deliverables:
- Architecture: why this archetype, what the rejected alternative was, and under what conditions you would revisit the decision.
- Multi-agent design: how responsibilities divide, what coordination approach you used and why, and what happens when an agent fails.
- Memory and state: what is shared and what is private, what must never persist, and how the system recovers after an interruption.
The defense is an account of why those decisions were right for the specific domain and business problem you chose — not a statement of general principles about multi-agent systems.
### How the 5–7 minutes are structured
Use this as a guide.
- Minutes 0–1: Context and canvas. Your domain and business problem in one sentence, your archetype in one more. Then run the common-path query live and narrate the trace briefly as it plays — which agent is classifying, which specialist is answering, what is being written to state.
- Minutes 1–2: Architecture and design decisions. Walk the diagram, covering the three defense areas in order. Name the decision and the reason for it, one or two sentences each. Do not read the sprint deliverables aloud.
- Minutes 2–4: Test record. Two or three findings — one test that confirmed a design decision worked, one that revealed a gap and required a change. Name the test, what it revealed, what you changed. This is what distinguishes an implemented architecture from a described one.
- Minutes 4–5: Second query, if time allows. The boundary condition or recovery demonstration. For a technically engaged audience this is the most compelling part of the run.
- Minutes 5–7: Questions.
Focus on reasoning and communication. The presentation is not a code walkthrough. Do not click through every node. Do not read your system prompt out loud. Do not show JSON. Show the thinking behind the architecture — the choices you made, why you made them, what you would do differently.
## 5. Quality expectations / Evaluation
Your evaluation is based on the presentation, not on the artifacts in isolation. The artifacts are submitted so the reviewer can verify what you say and run your canvas if needed.
The evaluation covers four dimensions:
[TABLE]
  | Dimension | What the evaluator is listening for |
  | Architecture coherence | Do the four sprint decisions fit together as one design, or do they read as independent exercises that were never reconciled with each other? |
  | Decision justification | Is each major decision grounded in a specific property of the business problem and domain, or stated at the level of general principle ("multi-agent is more scalable")? |
  | Implementation evidence | Does the canvas match the design documents? Does the test record show the canvas was actually exercised rather than described? |
  | Failure handling | Can the learner say what the system does when something goes wrong — a specialist failing, a classifier producing malformed output, a state key holding a stale value? |
There is no single right architecture. The evaluation is not checking which archetype you picked. It is checking whether the architecture you chose is coherent, implemented, and defensible given the business problem you named in Sprint 1.
## 6. Preparation checklist
Complete these before the live session. Do not leave any item for the session itself.
- [ ] Final canvas exported as JSON and confirmed loadable in a fresh Flowise instance
- [ ] System diagram updated to match the implemented architecture — roles, state flow, recovery path
- [ ] Two queries prepared: one common path, one boundary condition or recovery path
- [ ] All four sprint deliverables reviewed so the key decisions are in mind, not just in documents
- [ ] Test record reviewed, with at least one confirming result and one gap-revealing result ready to name
- [ ] Answer prepared for the most likely hard question: why this archetype rather than the alternative you rejected
- [ ] Any safeguard that does not apply to your architecture has its one-sentence written reason ready
- [ ] Written summary drafted, one to two pages, and exported as PDF
- [ ] Presentation timed once end to end against the 5–7 minute structure
- [ ] No credentials, API keys, or private tokens in the export or the documents
## 7. Submission / Delivery instructions
Submission is for access and review. Evaluation happens during the presentation. These are two separate steps.
### What to submit
Bundle into a single submission package (a shared Google Drive folder):
1. The final canvas exported as JSON, or a link to the canvas in your Flowise instance if the link is accessible to the reviewer.
1. One document (.md or .pdf) containing the following, in this order:
  1. The architecture decision brief
  1. The multi-agent design diagram
  1. The written design rationale
  1. The memory and state architecture specification
  1. The test record
1. The written summary as a PDF.
### Where and when
Submit your work as a link to a Google Drive folder. Put all the artifacts inside it and share the link in the submission lesson.
> ⚠️ Important: Make sure the folder permissions allow anyone with the link to open every file inside it. Test the link in an incognito window before submitting. Do not include credentials, API keys, or private tokens in the export or the documents.
### What is not part of grading
- Code Clinic attendance. Not graded.
- The number of artifacts you produce beyond what is listed.
- The visual polish of your slides. Clear thinking matters more than beautiful slides — which does not mean they should be thrown together.
## Final check
Before your presentation, read through your system diagram and ask these questions. They are the questions the instructor will be asking during your defense.
- Can you name every agent on the diagram and say what it is responsible for, without looking at the canvas?
- Does every state key on the canvas appear in your specification, and does each one have exactly one designated writer?
- Can you say what resets before control returns after a failure, and why the order matters?
- Does the diagram match the canvas as it stands now, not as it stood in Sprint 2?
- Can you name one test that changed your design, and say what it changed?
If any of these questions produce hesitation, that is useful information. Use the time before the session on the one that hesitated most.
## Summary
The module project moves from a set of design documents and a canvas into something you can stand behind and explain. The architecture brief named a pattern, the diagram showed the relationships, the specification drew the boundaries, and the testing work turned all of it from a claim into evidence.
What matters now is coherence: the canvas, the diagram, the specification, and the account you give of them all describing the same system. Gather the artifacts, run the timing once, and be ready to say what you would change.