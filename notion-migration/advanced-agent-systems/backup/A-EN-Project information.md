# Project information

Notion page: https://app.notion.com/p/Project-information-3849418319f3802a914fc679d1614aae
Backed up before n8n migration

## 1. Intro
The module project asks you to design and build a redesigned agent architecture for a business problem of your choice. Across four sprints you produced a set of deliverables that build on each other: the architecture decision brief that names the pattern, the multi-agent design diagram that shows how the agents relate, the memory and state specification that describes what the system knows and what it forgets, and the integration work on the Flowise canvas that turns those decisions into something that runs.
The skills you've been practicing across the module:
- Reading a business case (yours) and translating it into an architecture decision defensible against alternatives
- Deciding when one agent is enough and when multiple agents earn their coordination cost
- Defining specialisations, boundaries, and hybrid-query strategies for multi-agent designs
- Designing memory and state boundaries — what is shared, what is private, what must never persist
- Designing failure isolation and state recovery paths so one agent's failure does not corrupt shared state
- Implementing the design on a Flowise Agentflow V2 canvas and testing it against the failure modes you designed for
The Flowise canvas you started from was a baseline three-node Agentflow V2 template. Your final canvas reflects the full architecture you designed across the four sprints — not a rebuild from scratch, but a deliberate redesign of the baseline into something that matches your brief.

## 2. Tasks
This is what you will be doing over the coming weeks.
1. Sprint 1: Architecture decision. Read your chosen business case. Apply the four-question framework to decide single-agent or multi-agent. Name the pattern. Write a one-page architecture decision brief covering the six sections (Decision, Pattern, Inputs and outputs, The three pillars, Rejected alternative, Conditions for revisiting).
1. Sprint 2: Multi-agent design. Produce a design diagram of your agent architecture — every agent named, information flow shown, routing decision points marked, information boundaries called out, at least one fallback path. Write a design rationale covering diagnosis and justification, agent roles, information boundary, and fallback strategy. Note the rejected alternative if applicable.
1. Sprint 3: Memory and state architecture. Produce the four-section specification: memory boundary map (shared vs private vs conditional, with persistence scope), what must not persist (with the category and prevention strategy for each item), state recovery design (failure scenario, safe state, and specific recovery mechanism), and failure isolation (which agents may write to which state keys, and under what conditions).
1. Sprint 4: Integration and testing. Implement the design on the Flowise canvas: stage the archetype, enforce memory boundaries, wire up state handoff and recovery, and add the specific safeguards you designed for the failure modes. Run the test set (baseline, boundary, and architecture-specific tests). Refine until each safeguard holds under the tests it was designed for. Export the canvas.

## 3. Project artifacts
Three layers: what you build, how well you can explain it, and a short written summary connecting the pieces together.
### Technical artifacts
By submission day you should have:
- The Flowise canvas exported as JSON: Your final version after the integration and testing work in Sprint 4. Loadable in a fresh Flowise instance without missing configuration.
- Architecture decision brief from Sprint 1: One page, six sections, tied to your specific business problem.
- Multi-agent design diagram from Sprint 2: Legible on a shared screen, with agent roles, information flow, routing decision points, information boundaries, and at least one fallback path marked.
- Written design rationale from Sprint 2: No more than 400 words covering diagnosis and justification, agent roles and responsibilities, information boundary, and fallback strategy. Rejected alternative noted where applicable.
- Memory and state architecture specification from Sprint 3: The four sections: memory boundary map, what must not persist, state recovery design, failure isolation assessment.
- Test record from Sprint 4: The tests you ran against the canvas (baseline, boundary, and architecture-specific), expected behaviour written before running, actual behaviour logged after, and notes on what you changed as a result.
### Analytical reasoning
For your presentation, you should be able to explain:
- Why you chose the archetype you chose. What specific property of your business problem made the chosen archetype fit? What was the rejected alternative and why?
- Why the multi-agent design divides responsibilities where it does. What is the boundary statement between agents? What happens at hybrid queries?
- Why the memory boundaries are drawn where they are. What is shared and why? What is private and why? What must never persist and why?
- What tests revealed. Where did a test confirm a design decision worked as expected? Where did a test reveal a gap and require a change to the canvas or the specification?
- What you'd do with additional time.
### Written summary
A short PDF, one to two pages, that ties the whole project together. Include:
- A one-paragraph problem framing what your business problem is and why the design work matters for it.
- A one-paragraph solution overview of your agent architecture does and what shape it has.
- Two or three bullet points naming the most interesting decisions you made across the four sprints (decisions with the alternative you considered and rejected).
- A one-paragraph reflection on what your testing revealed and one limitation you couldn't fully resolve.
The summary is for someone who hasn't seen your presentation. It should read independently. Submit as a PDF; export from whatever tool you wrote it in.

## 4. Presentation
The presentation is mandatory and is the main evaluation method for this project.
Format: Live, in front of the cohort, with Q&A. Target time: 5–7 minutes for the presentation itself, plus a few minutes of Q&A. Aim for the middle — a tight 6 minutes is better than a rambling 7.
The presentation has three components. All three are required. A presentation that covers only the canvas without the diagram, or the diagram without the design decisions, is incomplete.
### Component 1: The canvas, live
A live demonstration of your redesigned Agentflow V2 canvas in Flowise. You will run at least one query during the presentation to make the architecture visible. The execution trace in Flowise shows which nodes activated, in what order, and what was written to Flow State. The instructor and your peers will be watching the trace, not just the output.
Prepare two queries before the session:
- One that takes the most common path through your architecture (the path most of your test record covers).
- One that exercises a boundary condition (a query that tests the scope boundary or the recovery path).
You may not use both in the time available, but having both ready lets you respond if the instructor asks to see a specific path.
### Component 2: The system diagram
A diagram showing your agent architecture: agent roles, responsibilities, coordination approach, the state keys that flow between agents, and the recovery path. This is the visual anchor for the defense. When you name a design decision verbally, the diagram should show it.
The diagram does not need to be produced in a specific tool. It should be legible on a shared screen and accurate. If the diagram shows three specialists but the canvas has two, that discrepancy will be the first question.
You produced a multi-agent design diagram in Sprint 2. The diagram you present should reflect the implemented architecture, not the Sprint 2 draft. Update it now if the canvas evolved during the integration work in Sprint 4.
### Component 3: The defense
A verbal account of the design decisions you made. The defense covers three areas, corresponding to the three sprint deliverables:
- Architecture (Sprint 1 brief): Why did you choose this archetype? What was the rejected alternative, and why was it rejected? Under what conditions would you revisit the decision?
- Multi-agent design (Sprint 2 diagram): How are responsibilities divided between agents? What coordination approach did you use, and why? What happens when an agent fails?
- Memory and state (Sprint 3 specification): What is shared and what is private? What must never persist, and why? How does the system recover after an interruption?
The defense is an account of why the decisions in those deliverables were made based on the specific domain and business problem you chose, not in general principles about multi-agent systems.

### How the 5–7 minutes are structured
Use this structure as a guide.
- Minutes 0–1: Context and canvas. Name your domain and business problem in one sentence. Name your archetype in one sentence. Then run the first query live (the common path) and let the execution trace play. While it runs, narrate briefly: which agent is classifying, which specialist is routing to, what is being written to Flow State. The context and archetype sentences should take fifteen seconds; the rest is the live demonstration.
- Minutes 1–2: Architecture and design decisions. Walk through the system diagram. Cover the three defense areas in order; architecture choice, multi-agent design, memory and state. For each area, name the decision and the reason for it. One or two sentences per decision is enough. Do not read the sprint deliverables aloud; use them as preparation material, not as a script.
- Minutes 2–4: Test record. Name two or three findings from the test record: one that confirmed a design decision worked as expected, and one that revealed a gap and required a change. Be specific — name the test, what it revealed, what you changed. The test record is what distinguishes an implemented architecture from a described one.
- Minutes 4–5: Second query or recovery demonstration (if time permits). If time allows, run the boundary condition query — the one that exercises the recovery path or a scope boundary. This is the most compelling part of the demonstration for a technically engaged audience.
- Minutes 5–7: Questions. The instructor and peers will ask questions. 
Focus on reasoning and communication. The presentation is not a code walkthrough. Do not open Flowise and click through every node. Do not read your system prompt out loud. Do not show JSON schemas. Show the thinking behind the architecture (the choices you made, why you made them, what you'd do differently).
## 5. Quality expectations / Evaluation
Your evaluation is based on the presentation, not on the artifacts in isolation. The artifacts are submitted so the reviewer can verify what you say and run your canvas if needed.
The evaluation covers four dimensions:
[TABLE]
  | Dimension | What the evaluator is listening for |
  | Architecture coherence | Do the four sprint decisions fit together as a unified design, or do they look like independent exercises that were never reconciled with each other? |
  | Decision justification | Is each major decision grounded in a specific property of the business problem and domain, or are reasons stated at the level of general principle ("multi-agent is more scalable")? |
  | Implementation evidence | Does the canvas match the design documents? Does the test record show the canvas was actually exercised, not just described? |
  | Failure handling | Can the learner describe what the system does when something goes wrong — a specialist agent failing, a Classifier producing malformed output, a state key holding a stale value? |
There is no single right architecture. The evaluation is not checking whether you chose the Router over the Coordinator or the Evaluator. It is checking whether the architecture you chose is coherent, implemented, and defensible given the business problem you stated in Sprint 1.
## 6. Preparation checklist
Complete these before the live session. Do not leave any item for the session itself.
- [ ] Final canvas exported as JSON and confirmed loadable in a fresh Flowise instance
- [ ] System diagram updated to reflect the implemented architecture; roles, state flow, recovery path
- [ ] Two queries prepared: one for the common path, one for a boundary condition or recovery path
- [ ] All four sprint deliverables reviewed (architecture brief, multi-agent design diagram + rationale, memory and state specification, test record) so the key decisions are in mind, not just in documents
- [ ] Test record reviewed and at least one confirming result and one gap-revealing result ready to name
- [ ] Answer prepared for the most likely hard question: "Why this archetype rather than the alternative you rejected?"
- [ ] Written summary drafted (1–2 pages) and exported as PDF
- [ ] Presentation timing practised at least once (run through the 5–7 minute structure end to end before the session so the context sentence, demo, and defense fit the time)
## 7. Submission / Delivery instructions
Submission is for access and review. Evaluation happens during the presentation. These are two separate steps.
### What to submit
Bundle into a single submission package (a shared Google Drive folder):
1. Flowise canvas exported as JSON, or a link to the canvas in your Flowise instance (if shared, make sure the link is accessible).
1. A document (.md, .pdf, or other formats) showing the following:
  1. Architecture decision brief
  1. Multi-agent design diagram
  1. Memory and state architecture specification
  1. Test record
  1. A written summary
### Where and when
Submit your work as a link to a Google Drive folder. Add all the artifacts inside and share the link in the submission lesson.
> ⚠️ Important: Make sure to give permissions for the Google Drive folder so that anyone with the link can access your files. Test the link in an incognito window before submitting.
### What is not part of grading
- Code Clinic attendance. Not graded.
- The number of artifacts you produce beyond what's listed.
- The visual polish of your slides. Clear thinking matters more than beautiful slides.
## Final check
Before your presentation, read through your system diagram and ask these questions. They are the questions the instructor will be asking during your defense.
- Does the diagram show what happens when a specialist agent fails, not just when it succeeds?
- Can you trace a specific query from entry to reply on the diagram, naming the Flow State key that carries the routing decision and the key that carries the reply?
- If the business problem you described in Sprint 1 changed, which part of the architecture would need to change first? Can you name it from the diagram?
- Does the test record contain at least one result that you did not predict before running the test?
If any of these questions produce a moment of uncertainty, that is useful information. Use the time before the presentation to work through it.
## Summary
The module project moves from a set of design documents and a canvas into something you can stand behind and explain. The artefacts are already produced across four sprints. Focus your work on preparation, not creation: reviewing the decisions, practising the structure, and ensuring the diagram accurately reflects what was built.
The defense is not a test of whether the agent works. It is a test of whether you understand why it was designed the way it was and whether the design holds up when someone asks the questions a real architecture review would ask. The sprint deliverables are the evidence that it does.