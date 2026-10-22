# Selecting the right pattern for a use case

Notion page: https://app.notion.com/p/Selecting-the-right-pattern-for-a-use-case-3849418319f38024b1e0ea3b87ec9620
Backed up before n8n migration

By this point, Vela's team has a working design framework: a four-question test for single-agent vs. multi-agent, six named patterns to choose from, and three pillars that determine whether any pattern holds up in production. Selin used the framework to confirm that Vela's current problem calls for a well-designed single agent.
Now it is your turn to use the same framework.
> 💡 This lesson presents four business scenarios. Each one describes a real operational problem that a team wants to solve with an agent. Your job is to work through the decision framework for each scenario, name the appropriate architecture pattern, and write a short justification that a colleague could read and act on.
There is no canvas to build in this lesson. The output is your reasoning documented clearly enough that it could become the foundation of an architecture decision brief.

## What you are deciding
For each scenario, answer three questions in order:
1. Single agent or multi-agent? Apply the four-question framework from the previous lesson. Name which questions drove the decision and why.
2. Which pattern? From the six patterns (single agent, tool-using agent, workflow + agent, router, evaluator, supervisor-worker), name the one that fits best. If two are plausible, name both and explain which you would choose and why.
3. Which pillars need the most attention? From the three pillars (orchestration, communication, state management), identify which one will require the most deliberate design for this specific use case and explain what the risk is if it is not handled well.

## The four scenarios
> 🔥 Before you start, make a copy of this template. It mirrors the structure of this lesson — one tab with the four scenarios (Norda, Helio, Daven, Arco), each with three-question answer fields, plus a short checkpoint sheet.
### Scenario A: Norda Retail
Norda Retail is a mid-sized clothing retailer with stores across Scandinavia. Their customer service team receives around 400 queries per day through an internal chat tool. Roughly 60% are order status questions ("where is my order?"), 30% are return and exchange requests, and 10% are complaints that need to be escalated to a human agent. The team wants to build an agent that handles all three types. Order status queries require a live lookup against the order management system. Return and exchange requests follow a fixed policy that is documented internally. Escalations need to be flagged immediately and handed off with a summary.
Work through the three questions for Norda Retail. Write your answers before reading the hints.

### Scenario B: Helio Engineering
Helio Engineering provides technical consulting to renewable energy projects. A consultant submits a project scoping request, typically two to three paragraphs describing the client, the problem, and the constraints. The agent's job is to produce a structured project brief: a summary of the problem, a suggested approach, a list of relevant case studies from Helio's internal knowledge base, and a risk section. The brief needs to be reviewed by a senior consultant before it is sent to the client. If the senior consultant rejects it, the agent should revise and resubmit. The revision loop should stop after three attempts.
Work through the three questions for Helio Engineering.

### Scenario C: Daven Logistics
Daven Logistics coordinates freight movements between suppliers and distribution centres across central Europe. They want an agent that monitors a daily list of twenty shipments, checks the current status of each one against their tracking API, flags any shipment that is delayed by more than 24 hours, and produces a daily summary report. The list of shipments is provided as structured data at the start of each run. The tracking API returns a status and an estimated arrival time for each shipment ID.
Work through the three questions for Daven Logistics.

### Scenario D: Arco Insurance
Arco Insurance processes commercial property claims. When a new claim is submitted, it needs to go through three stages before a human adjuster reviews it: an initial completeness check (are all required documents present?), a fraud-signal scan (does the claim match known fraud patterns?), and a coverage verification (does the policy cover what is being claimed?). Each stage produces a structured output that the next stage depends on. If the completeness check fails, the claim should not proceed to the fraud scan. If the fraud scan raises a flag, the claim should be escalated to a specialist team rather than continuing to coverage verification.
Work through the three questions for Arco Insurance.
## Hints
  Use these only after you have written your own answers.
  Scenario A: Classify the input into a small set of allowed labels, then route with Switch. A branch can be an API lookup, a grounded policy answer, or a human escalation. Three routes do not automatically require three agents. Define the fallback for unknown labels.
  Scenario B: A draft needs human approval, not just another model's opinion. Consider a supported send-and-wait approval operation or Wait resumed by a review event. Track attempt count explicitly; permit at most three draft/review attempts, then escalate. The design must handle rejection and no response.
  Scenario C: n8n can process a list as items. Use Loop Over Items when you need explicit batching or per-item control; it is not required for every list. Use deterministic logic for the 24-hour threshold, handle each API error, and summarise verified results. An agent is optional for writing the report, not required for every lookup.
  Scenario D: The order and exit conditions are fixed. A workflow with If/Switch can enforce them. Use model reasoning only where interpretation is needed. A supervisor-worker pattern is justified only if choosing the next task is itself a reasoning problem.

> 💡 
  ### 🔥 Using AI when you get stuck
  If you are unsure which pattern fits a scenario, a useful approach is to describe the problem structure to an AI assistant and ask it to identify which of the six patterns matches, then challenge the answer by asking what the failure mode would be if that pattern were wrong.
  A good prompt:
  > "I am designing an agent for [describe the scenario in two sentences]. The agent needs to [describe the core behaviour]. Given these six patterns (single agent, tool-using agent, workflow + agent, router, evaluator, supervisor-worker), which fits best, and what is the main risk if I choose the wrong one? I am using n8n."
  Use the AI's answer as a starting point, not a final answer. Then check it against the three questions in this lesson.
## Checkpoints
After completing all four scenarios, check your answers against these questions:
- For each scenario where you chose multi-agent: Did you name a specific coordination mechanism, which node or tool delegates work, and which task and result fields cross the handoff?
- For each scenario where you chose single agent: Did you identify a concrete constraint that would change the decision to multi-agent if it appeared?
- For Scenario B: Did you distinguish between the human approval gate and a model-based evaluator and decide which role applies here?
- For Scenario C: Did you identify the failure mode when one list item returns an API error, and name whether the pattern handles it or requires an explicit fallback?
- For Scenario D: Did you justify why the canvas controls the sequence rather than a supervisor agent and identify what would have to change about the scenario to make supervisor-worker the better choice?
If any checkpoint exposes a gap, revise that scenario before the next lesson. The architecture decision brief you produce later in this sprint will require the same reasoning, applied to your own agent.

## In your project
The decision framework you practiced here is the same one you will apply to your own agent at the next live session. Before that session, think about which of the four questions (scope and reliability, tool conflicts, failure isolation, or coordination cost) is the hardest to answer for your own use case. That is the question worth preparing for.

## Summary
Four scenarios, four decisions, four sets of justifications. The framework is the same each time: single vs. multi-agent first, then which pattern, then which pillar needs the most deliberate attention. The scenarios in this lesson were chosen to exercise different parts of the framework — a router, an evaluator with a human gate, an iteration pattern, and a sequential workflow. Together they cover most of what you will encounter in real agent design.
The next lesson examines the mistakes that architects make when they apply this framework under pressure (over-engineering, hidden state, and brittle handoffs) and how to recognise them before they reach the canvas.
## 📸 Screenshot suggestions
- Norda: show classifier output and Switch with a fallback.
- Helio: show a conceptual n8n draft, human gate, and bounded revision flow; highlight attempt_count.
- Daven: show example shipment-status items including a marked API error. Arco: show If branches with fixed exits.
## Check for understanding
### 1. What does Helio's approval requirement need?
- A. Only a second model call — Incorrect. The scenario requires human approval.
- B. A human gate with bounded attempts and escalation — Correct. Approval, rejection, and the limit are part of the design.
- C. A larger memory store — Incorrect. Memory cannot replace approval.
### 2. Do twenty shipment lookups need twenty agents?
- A. No, deterministic item processing may be sufficient — Correct. Multiple records are not separate reasoning roles.
- B. Yes, each record needs a specialist — Incorrect. API lookups do not automatically require agents.
- C. Yes, because HTTP Request is a model decision — Incorrect. A main-path request can run deterministically.
### 3. What fits Arco's fixed stages and exits?
- A. An If/Switch-controlled workflow — Correct. The sequence is already specified.
- B. A supervisor that freely changes the order — Incorrect. That would conflict with the requirements.
- C. Skip the checks and generate an answer — Incorrect. The required checks must occur.