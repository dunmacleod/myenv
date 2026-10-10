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
  Scenario A: Three distinct input types that each require different handling — a routing decision at the entry point is the natural fit. Think about what happens to the Condition Agent Node's scenario descriptions if all three are crammed into one system prompt instead.
  Scenario B: The revision loop and the human approval gate are the structural signals. Which Agentflow V2 node handles the approval (Human Input Node), and which handles sending the output back for revision (Loop Node)? Think about where the evaluator role sits — is it the human, the model, or both?
  Scenario C: Twenty shipments processed one at a time using structured input data — this is a pattern you have seen before. Think about which Agentflow V2 node was designed specifically for iterating over a list. The orchestration question here is: what happens when one item in the list returns an error from the tracking API?
  Scenario D: Three sequential stages where each depends on the previous one, with conditional exits at stages one and two. Think carefully about the distinction between a workflow + agent pattern and a supervisor-worker pattern. The stages here have a defined order and fixed exit conditions — does that call for an agent deciding what to do next, or for the canvas to control the sequence?

>  
  ### 🔥 Using AI when you get stuck
  If you are unsure which pattern fits a scenario, a useful approach is to describe the problem structure to an AI assistant and ask it to identify which of the six patterns matches, then challenge the answer by asking what the failure mode would be if that pattern were wrong.
  A good prompt:
  > "I am designing an agent for [describe the scenario in two sentences]. The agent needs to [describe the core behaviour]. Given these six patterns (single agent, tool-using agent, workflow + agent, router, evaluator, supervisor-worker), which fits best, and what is the main risk if I choose the wrong one? I am using Flowise Agentflow V2."
  Use the AI's answer as a starting point, not a final answer. Then check it against the three questions in this lesson.
## Checkpoints
After completing all four scenarios, check your answers against these questions:
- For each scenario where you chose multi-agent: Did you name a specific coordination mechanism, which node routes between agents, and what data travels through Flow State?
- For each scenario where you chose single agent: Did you identify a concrete constraint that would change the decision to multi-agent if it appeared?
- For Scenario B: Did you distinguish between the human evaluator (Human Input Node) and the model-based evaluator (Condition Agent or LLM Node) and decide which role applies here?
- For Scenario C: Did you identify the failure mode when one list item returns an API error, and name whether the pattern handles it or requires an explicit fallback?
- For Scenario D: Did you justify why the canvas controls the sequence rather than a supervisor agent and identify what would have to change about the scenario to make supervisor-worker the better choice?
If any checkpoint exposes a gap, revise that scenario before the next lesson. The architecture decision brief you produce later in this sprint will require the same reasoning, applied to your own agent.

## In your project
The decision framework you practiced here is the same one you will apply to your own agent at the next live session. Before that session, think about which of the three questions (scope and reliability, tool conflicts, failure isolation, or coordination cost) is the hardest to answer for your own use case. That is the question worth preparing for.

## Summary
Four scenarios, four decisions, four sets of justifications. The framework is the same each time: single vs. multi-agent first, then which pattern, then which pillar needs the most deliberate attention. The scenarios in this lesson were chosen to exercise different parts of the framework — a router, an evaluator with a human gate, an iteration pattern, and a sequential workflow. Together they cover most of what you will encounter in real agent design.
The next lesson examines the mistakes that architects make when they apply this framework under pressure (over-engineering, hidden state, and brittle handoffs) and how to recognise them before they reach the canvas.