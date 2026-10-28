# Multi-agent design diagram

Notion page: https://app.notion.com/p/Multi-agent-design-diagram-3849418319f38061a952eeb4ded93135
Backed up before n8n migration

Trevi Health is a healthcare staffing agency based in Milan. They place nurses, physiotherapists, and specialist care workers in hospitals, private clinics, and home-care settings across northern Italy. Their operations team runs on a mix of email, spreadsheets, and a lightly customised CRM. They have no AI agents in production.
Their operations director, Marco, has been tasked with evaluating whether an AI agent could reduce the time their coordinators spend answering routine queries from two sources: candidate workers (asking about shift availability, pay rates, document requirements, and placement status) and client facilities (asking about candidate CVs, availability windows, compliance documentation, and invoicing). Both groups contact Trevi through the same shared inbox.
Marco has put together an initial brief: one agent, one inbox, handle everything. His team's feedback after a two-week prototype is that the agent does well on candidate queries and poorly on facility queries — and occasionally mixes up tone, occasionally shares candidate information with facility contacts.
Your job is to apply what you have learned in Sprint 2 to produce a multi-agent design diagram for Trevi Health's query-handling system, along with the written design rationale that would accompany it in a real architecture review.

## What you are working with
The Trevi Health scenario has the following confirmed properties:
Query sources:
- Candidate workers: nurses, physios, and specialists asking about shifts, pay, documents, and placement status. Tone expected: warm, reassuring, practical.
- Client facilities: hospitals and clinics asking about candidate credentials, compliance documentation, scheduling, and invoicing. Tone expected: professional, precise, efficient.
Confirmed failure modes in the single-agent prototype:
- Response quality for candidate queries: acceptable
- Response quality for facility queries: poor; the agent uses candidate-facing language and misses facility-specific details
- Information boundary failures: the agent occasionally references candidate personal data in responses directed at facilities
- Routing: all queries arrive in one shared inbox with no pre-classification
Volume and latency context:
- Approximately 60–80 queries per day total, split roughly 60% candidate, 40% facility
- Queries arrive throughout the working day via email integration; response time expectation is under 4 hours, not real-time
- The operations team reviews all agent responses before sending (human-in-the-loop approval is already in place)
Constraint:
- Trevi Health does not have a development team. The system must be buildable in n8n with standard nodes by a non-developer. Custom code is acceptable in Code nodes only when strictly necessary.
As you work, keep these questions in mind:
- Does the evidence point to overload, underspecification, or both? Your diagnosis determines whether a multi-agent design is justified.
- Where does the information boundary failure sit in the failure taxonomy? Is it a quality failure or a system failure, and what does that imply for the fallback design?
- Does the latency and volume context support the coordinator overhead? State your assumption explicitly.
- If you conclude that a single agent (better specified) would solve the problem, you still need to produce a multi-agent design diagram, as the rejected alternative, with documented reasoning for why it was rejected.

## Quick diagnosis
Answer these questions before producing your diagram. They test whether you are reading the Trevi Health scenario correctly; not whether you have memorised Sprint 2 terminology.
### Question 1
> 💡 Marco's initial single-agent prototype handles candidate queries well and facility queries poorly within the same session. Which diagnosis fits this evidence most precisely?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/547ce0b9-7074-42d4-838f-1f559bcb339b

### Question 2
> 💡 The information boundary failure (candidate personal data appearing in facility-directed responses) is best classified as which failure type?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/5ef87408-bc07-4a1e-a055-a1ec0cd7f640
### Question 3
> 💡 Trevi Health's human-in-the-loop approval step (all agent responses are reviewed before sending) is best described as which fallback strategy type from the lesson about handling failures?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e28c9dd2-51f9-4d11-87a6-4c663d550b78

### Question 4
> 💡 Marco wants to add a third query category to the system: internal HR queries from Trevi's own coordination team (questions about payroll, scheduling, and compliance policy). He proposes adding a third specialist agent. Before building, which check is most important?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f673d946-4bdf-4b13-b0d9-7eb6a4099b98

### Question 5
> 💡 Trevi Health's 4-hour response time window and human review step before sending make the multi-agent coordinator overhead more or less acceptable compared to a real-time chat system. Why?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/66d17c27-6d50-40a4-9129-cca871adbcec

## Making improvements
> 🔥 Before you start, make a copy of this template. It holds your written design rationale (Task B) and rejected alternative (Task C). Task A (the diagram itself) is drawn separately in the tool of your choice.
You have diagnosed the Trevi Health scenario and confirmed the multi-agent design is justified. Now produce the deliverable.
### Task A: Multi-agent design diagram
Produce a diagram of the proposed Trevi Health multi-agent system. 
Your diagram must show:
- Every agent or node in the system and its name
- The input source (the shared inbox) and the output destination (the operations team review queue)
- The direction of information flow between nodes — use arrows
- The routing decision point and what it routes on
- The information boundary between the candidate specialist and the facility specialist — mark it explicitly on the diagram
- At least one fallback path
Format: You may produce this diagram in any tool — n8n editor canvas, a drawing tool, a document diagram, or hand-drawn and photographed. What matters is that all required elements are present and legible. Label every node and every connector.

### Task B: Written design rationale
Alongside the diagram, write a short design rationale (no more than 400 words) that covers the following four points. This is the document Marco would bring to a design review.
B1: Diagnosis and justification. State in two to three sentences why the single-agent prototype's failures justify a multi-agent design rather than a better single-agent specification. Reference the specific failure modes you identified in the Quick Diagnosis section.
B2: Agent roles and responsibilities. State the responsibility of each specialist agent in one sentence each. Apply the design standard from the lesson about coordinating two specialist agents: no "and" in the responsibility statement, and the boundary must be stated explicitly.
B3: Information boundary. Explain in two to three sentences how the multi-agent design enforces the information boundary between candidate and facility data that prevents candidate personal data from appearing in facility responses.
B4: Fallback strategy. Identify the highest-consequence failure mode in the Trevi design (not necessarily the most likely) and describe the fallback strategy for it in two to three sentences. You may use any of the four strategy types from handling failures. State which type you are using and what tradeoff you accepted.

### Task C: Rejected alternative (if applicable)
If you concluded during Quick Diagnosis that a better-specified single agent could solve the problem, produce a one-paragraph explanation of why the multi-agent design is the rejected alternative. Your explanation must address the information boundary failure specifically: why a single-agent architecture cannot enforce the boundary reliably even with improved instructions.
If you concluded that the multi-agent design is the correct choice (which the evidence supports), skip Task C and note that the single-agent alternative was considered and rejected with one sentence giving the reason.

## Final check
Before submitting your diagram and rationale, verify the following:
- [ ] Does your diagram include every required element from Task A? Check the list item by item — missing the information boundary marker or a fallback path are the two most common omissions.
- [ ] Is your responsibility statement for each specialist free of "and"? Read each statement aloud. If it requires "and" to be complete, the scope is too broad.
- [ ] Does your information boundary explanation address the mechanism, not just the intent? "The agents are kept separate" is intent. "The candidate specialist's context does not include facility account data, and the coordinator's handoff passes only the client query, not any candidate record" is mechanism.
- [ ] Is your fallback specific enough to build? For example, an n8n Set (Edit Fields) node assigns a safe route_key when the classifier category is missing, then the Switch fallback sends a clarification response. Do not claim that a live escalation was sent without an authorized integration.
- [ ] Does your rationale stay within 400 words? Concision is part of the skill being assessed; a design rationale that requires 800 words to make its case has not been written clearly enough.

## Summary
You have applied the full Sprint 2 toolkit to a scenario you have not seen before. The diagnosis framework, the specialisation design standard, the failure taxonomy, and the router/evaluator vocabulary all appear in this assessment as tools applied to a specific problem with a specific set of evidence.
Trevi Health's scenario is realistic in a way the Vela walkthrough could not fully be: the information boundary failure is a compliance and trust problem. Getting candidate personal data into a facility response is the kind of failure that ends a client relationship. The multi-agent design addresses it structurally, not just instructionally. That is the argument the diagram and the rationale need to make together.