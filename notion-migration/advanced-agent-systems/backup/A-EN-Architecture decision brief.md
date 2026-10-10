# Architecture decision brief

Notion page: https://app.notion.com/p/Architecture-decision-brief-3849418319f380428248dab86f9f1dee
Backed up before n8n migration

Sprint 1 covered the framework for making architectural decisions: when to use a single agent versus multiple agents, which of the six patterns fits a given problem, how orchestration, communication, and state management each need deliberate design, and what the common mistakes look like before they reach a canvas.
This assessment asks you to apply that framework to a business you have not seen before. You are not being asked to build anything. You are being asked to think through a real operational problem, make a defensible architectural decision, and write it down clearly enough that a colleague could act on it.
The deliverable is a one-page architecture decision brief.

## The scenario: Karmen Freight
Karmen Freight is a logistics broker based in Vienna, Austria. It coordinates cross-border road shipments on behalf of manufacturer and retail clients across Austria, Hungary, and the Czech Republic. Karmen does not own trucks. It matches clients with vetted carriers, manages the documentation for customs clearance, and tracks shipments between origin and destination.
The operations team of twelve handles all client communication, carrier coordination, and compliance work. On an average day, the team receives around 80 internal queries mostly from account managers checking in on active shipments, from the compliance desk looking up customs procedure requirements, and from carrier coordinators confirming contact details or rate agreements. These queries are currently handled manually, which consumes roughly two hours of senior operations staff time per day.

The team's operations lead, Miriam, wants to build an internal agent to handle these queries. She has described the scope as follows:
- Shipment status queries: "Where is shipment KF-2847?" The most common query type, accounting for around 55% of daily volume. Answering requires a lookup against the shipment tracking API. If the API is unavailable, the agent should say so clearly and suggest the account manager contact the carrier directly.
- Customs procedure queries: "What documents does a pharmaceutical shipment require to cross from Austria into Hungary?" Around 30% of daily volume. Answers draw on documented customs procedure knowledge. These answers change infrequently but must be accurate.
- Carrier contact queries: "What is the contact email for TransCargo Kft?" Around 15% of daily volume. Answers come from the carrier directory. These answers are stable and factual.
Miriam has also stated two constraints:
1. The team is small. No one on the operations team has the capacity to maintain a complex multi-agent system. Whatever is built must be understandable and modifiable by someone without a technical background.
1. The agent must never fabricate a shipment status or a customs requirement. If it does not know, it must say so and direct the user to the appropriate source.

## Your task
> 🔥 Before you start, make a copy of this template. It mirrors the six sections of the brief: Decision, Pattern, Inputs and outputs, The three pillars, Rejected alternative, and Conditions for revisiting. Fill each section directly in the template.
Produce a one-page architecture decision brief for Karmen Freight's internal query agent.
The brief must cover all six sections below. Keep it to one page.
### Section 1 - Decision: Single-Agent or Multi-Agent
State your decision clearly. Then justify it using the four-question framework:
- Can one well-scoped agent handle the full range of inputs reliably?
- Do the different query types require tools or knowledge that conflict with each other?
- Does a failure in one query type need to be isolated from the others?
- Does the reliability gain of a multi-agent design justify the coordination cost?
Name which questions drove the decision and which were not decisive for this case.

### Section 2 - Pattern
Name the architecture pattern that fits best from the six: single agent, tool-using agent, workflow + agent, router, evaluator, supervisor-worker. If two are plausible, name both and state which you chose and why.

### Section 3 - Inputs and outputs
Define:
- What the agent will receive (input types, source, language if relevant)
- What the agent will produce (output format, what triggers a redirect vs. a direct answer)
- What the agent will explicitly not do (the deliberate exclusions)

### Section 4 - The three pillars
For each of the three architectural pillars, state the key design decision and the main risk if that decision is not made deliberately:
- Orchestration: What controls when each part of the flow runs?
- Communication: How does data move between the components you have designed?
- State management: What persists, what resets, and what must never be retained?

### Section 5 - Deliberate exclusions and the rejected alternative
Describe the architectural approach you considered but rejected, and explain why. If you chose single-agent, describe what a multi-agent design would have looked like and why it is not the right choice for Karmen Freight at this stage. If you chose multi-agent, describe the single-agent alternative and why it falls short.
This section is not optional. A decision is only defensible if the alternative has been considered.

### Section 6 - Conditions for revisiting the decision
Name two or three specific, observable changes to Karmen Freight's situation that would cause you to revisit the architecture decision. These should be concrete. For example, "if query volume exceeds 200 per day and latency becomes a reported problem" or "if customs requirements begin changing weekly and static knowledge is no longer sufficient."

## Before you write
Read the Karmen Freight scenario a second time. As you read, note:
- How similar or different the three query types are. Can one system prompt govern all three, or do they require meaningfully different handling?
- What the API dependency for shipment status queries means for the architecture. Specifically, whether its failure mode (API unavailable) is a communication problem, an orchestration problem, or a state management problem
- What Miriam's first constraint (small team, low maintenance overhead) rules out, and what it does not rule out
- Whether the constraint "must never fabricate" is an architectural requirement or a system prompt requirement and what that distinction means for the design
These are questions to hold in mind while making the decisions the brief requires.

## Hints
  Use these only if you are not sure how to proceed on a specific section.
  On the single vs. multi-agent decision: Start with Miriam's first constraint. A multi-agent system requires more maintenance than a single-agent system. The constraint does not rule it out, but it does raise the bar for justification. Ask whether the reliability gain is large enough to clear that bar.
  On the pattern: The three query types each have a different answer source (i.e. API, documented knowledge, carrier directory). That sounds like a router. But ask whether the routing decision actually needs to happen at the entry point, or whether a well-scoped single agent with a clear system prompt handles the classification internally without a dedicated routing node.
  On the API failure mode: An API that is sometimes unavailable is a communication design problem. Specifically, it is a brittle handoff waiting to happen. The brief should address what the agent does when the upstream data source is not available, not just what it does when it is.
  On the rejected alternative: The strongest brief does not dismiss the rejected alternative. It acknowledges its genuine strengths and then explains why this specific context makes the chosen approach the better fit. A brief that says "multi-agent would be more complex" is weaker than one that says "multi-agent would add isolation between query types, but the three types share enough context that routing overhead introduces more failure risk than isolation benefit."

## Checkpoints
Before submitting your brief, verify it against these questions:
- [ ] Does Section 1 name the specific questions that were decisive, not just state the conclusion?
- [ ] Does Section 2 name the pattern precisely, not just describe it in general terms?
- [ ] Does Section 3 include deliberate exclusions, not just what the agent does, but what it will not do?
- [ ] Does Section 4 address all three pillars, not just orchestration?
- [ ] Does Section 5 include a genuine description of the rejected alternative, not just a dismissal?
- [ ] Does Section 6 name specific, observable conditions, not vague scope statements?
- [ ] Is the brief one page? If it is longer, what can be cut without losing a decision?
If any checkpoint exposes a gap, revise that section before treating the brief as complete.

## In your project
The brief format you practiced in the walkthrough is the same format you will defend at the next live session. Before that session, compare what you have written for Karmen Freight with the architectural decisions you are facing on your own project canvas. The questions in Section 5 (the rejected alternative) and Section 6 (conditions for revisiting) are often the hardest to answer for your own agent, and are worth thinking through before the live session.

## Final check
Before you close the brief, read it once more with this question in mind: if Miriam handed this brief to a new team member and asked them to build the agent, would they know what to build, what to leave out, and when to come back and ask whether the architecture should change?
If the answer is yes, the brief is done.
Reflect briefly on these questions for clarity:
1. Which of the six sections was hardest to write, and what made it difficult?
1. Was there a moment where the scenario pushed you toward one architectural choice and the framework pushed you toward another? How did you resolve it?
1. Is there anything in the Karmen Freight scenario that the brief does not cover that you think it should?
These are the questions a good architect asks after making a decision.

## Summary
The Karmen Freight brief is the first time you have applied Sprint 1's full framework to a business you have not seen before. The scenario was chosen to be similar enough to Vela Systems to be recognisable (an operational team, internal queries, a constrained maintenance capacity), but different enough to require genuine reasoning rather than pattern-matching.
A one-page brief that covers all six sections, names the rejected alternative, and specifies observable conditions for revisiting the decision is the output of a deliberate architectural process, not a configuration exercise. That is what Sprint 1 has been building toward.
Sprint 2 takes the decision one step further from "should this be single-agent or multi-agent?" to "if it needs more than one agent, how do those agents work together?"