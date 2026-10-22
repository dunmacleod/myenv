# Memory and state architecture for the project agent

Notion page: https://app.notion.com/p/Memory-and-state-architecture-for-the-project-agent-3849418319f380668e31dcae8df69ddf
Backed up before n8n migration

Nordvik Freight coordinates wholesale shipments across Norway, Sweden, and Finland. Their operations team handles hundreds of supplier queries each week. This includes questions about pricing windows, route availability, and customs compliance documentation. Until now, those queries have been handled manually by three specialist teams. Nordvik's product lead, Astrid, has been tasked with building the company's first internal multi-agent system to route and respond to those queries automatically.
Astrid's team has designed a Flowise Agentflow V2 canvas with the following structure:
- A Classifier Agent (LLM node) that reads each incoming supplier query and classifies it into one of three categories: pricing, logistics, or compliance. It writes the classification and the original query text to Flow State.
- A Condition node that reads the classification from Flow State and routes to the appropriate specialist agent.
- A Pricing Agent, a Logistics Agent, and a Compliance Agent. Each configured to read the supplier's query from Flow State as their User Message input.
- A Direct Reply node on each specialist path that returns the agent's response.
![image]((notion-hosted file))
The system is about to go into testing. Astrid has asked you to review the memory and state architecture before the first real queries are processed. Your job is to produce a complete architecture review by covering what is shared and what is private, what must not persist, and what recovery looks like when things go wrong.

## What you will work with
Nordvik's canvas has the following Flow State configuration, as declared on the Start Node:
[TABLE]
  | Key | Default value | Written by |
  | query_category | unclassified | Classifier Agent (via Update Flow State) |
  | supplier_query | (empty string) | Classifier Agent (via Update Flow State) |
  | urgency | normal | Classifier Agent (via Update Flow State) |
The Classifier's structured output schema:
[TABLE]
  | Key | Type | Values |
  | query_category | enum | pricing, logistics, compliance, unclassified |
  | supplier_query | string | The original query verbatim |
  | urgency | enum | high, normal |
Each specialist agent has allMessages memory enabled and reads {{$flow.state.supplier_query}} as its User Message input.
The Compliance Agent additionally writes a value to $flow.state via its own llmUpdateState configuration: it writes compliance_flag: "review_required" when it detects a query that may require manual regulatory review.
There is currently no fallback branch on the Condition node for unclassified.

## As you work, keep these questions in mind
Before completing the tasks below, read through the canvas description above carefully. Consider:
- Which Flow State keys are shared across agents; and which agents need each key?
- Which pieces of information are turn-scoped, session-scoped, or candidates for persistent storage?
- What happens to each key if the Classifier fails before writing to it?
- What does the Compliance Agent's compliance_flag write mean for the other agents in the same session?
- Is the absence of an unclassified fallback a design gap or an acceptable risk for this system?
You do not need to answer these questions directly. They are diagnostic prompts. Use them to guide your analysis across the four tasks.

## Quick diagnosis
> 🔥 Before you start, make a copy of this template. It mirrors the structure of this lesson — one tab with the canvas context, then one tab per task (A: boundary map, B: what must not persist, C: state recovery, D: failure isolation), plus a final check sheet.

### Question 1
>  The Logistics Agent is configured with allMessages memory enabled and reads {{$flow.state.supplier_query}} as its User Message. A supplier sends two queries in the same session; first about pricing, then about route availability. On the second query, what does the Logistics Agent receive as its User Message input?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/38babb19-92b3-42b1-8009-bdb33065c098

### Question 2
>  The Compliance Agent writes compliance_flag: "review_required" to Flow State when it detects a regulatory concern. In the next turn of the same session, the supplier sends a pricing query. The Classifier runs and routes to the Pricing Agent. What risk does the compliance_flag key create?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/9b0a483c-1200-4f52-acfb-60e0e0ee5e58

### Question 3
>  Nordvik's canvas has no fallback branch on the Condition node for unclassified. A supplier sends the message "Hello, is anyone there?". The Classifier returns query_category: "unclassified". What happens?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a76dda8a-9288-430b-8302-346b68a188ef

## Task A: Map the memory boundaries
For the Nordvik canvas, produce a memory boundary map covering every piece of information that moves between agents. Use the three-column format below.
[TABLE]
  | Information | Shared or private | Persistence scope |
  | query_category |  |  |
  | supplier_query |  |  |
  | urgency |  |  |
  | compliance_flag |  |  |
  | Each specialist agent's system prompt |  |  |
  | allMessages conversation history |  |  |
For each row:
- Shared or private: state whether the information is shared (readable by more than one node in the canvas), private (readable only by the agent that produced it), or shared with conditions (readable by multiple nodes, but with a constraint on which agents should act on it).
- Persistence scope: state whether the information is turn-scoped (valid only for the agent turn that produced it), session-scoped (valid for the current session), or should persist across sessions (and if so, why).
For any row where the current canvas design does not match your recommended design — for example, where a value is currently shared but should be private, or session-scoped but should be turn-scoped — note the gap in a one-sentence comment beneath the row.

## Task B: Identify what must not persist
Three pieces of information in the Nordvik canvas are candidates for the "must not persist" category. Identify them, state which of the four categories they fall into (ephemeral identifier, derived assumption, incidentally shared PII, or working context), and write one sentence on how you would prevent them from persisting beyond the appropriate scope.
You do not need to propose a canvas change for each. A system prompt instruction, a design note, or a documented constraint is sufficient.

## Task C: Define the state recovery design
The Nordvik canvas has two state recovery gaps identified in the canvas description: the absence of a fallback branch for unclassified, and the compliance_flag key that persists across turns without being reset.
For each gap, write:
1. The failure scenario: What happens to Flow State and to the supplier's experience when the gap is triggered?
1. The safe state: What each affected Flow State key should hold after recovery?
1. The recovery mechanism: One specific canvas change that addresses the gap. Be precise: name the node, the key, and the value.

## Task D: Assess failure isolation
The Compliance Agent writes to $flow.state specifically the compliance_flag key in addition to reading from it. No other specialist agent writes to Flow State.
Assess whether the Compliance Agent's write behaviour creates a failure isolation risk for the other agents in the canvas. Your assessment should address:
- Whether the compliance_flag write is a designated, documented decision or an implicit side effect.
- Whether the Pricing Agent or Logistics Agent could be affected by a stale compliance_flag value.
- What isolation boundary you would recommend — which agents should be permitted to write to $flow.state, and under what conditions.
Write your assessment in no more than three short paragraphs.

## Final check
Review your work against these questions:
- Does your memory boundary map cover every piece of information that moves between agents, including allMessages and the compliance_flag write?
- Have you identified at least three items in Task B, each assigned to one of the four persistence categories?
- Does each recovery mechanism in Task C name a specific node, key, and value or does it stay at the level of general principle?
- Does your failure isolation assessment in Task D take a position (recommending a specific boundary) rather than listing considerations without a conclusion?

## Summary
This assessment asked you to apply the memory and state architecture framework to a system you had not seen before (a different organisation, a different agent structure, and a different set of failure modes). The four tasks covered the same ground as the sprint's lessons, but on new material, where the right answers were not given in advance.
Producing a complete architecture review before a system goes into testing is exactly the kind of work this sprint was building toward. The decisions you documented here are the decisions that separate a system that works in testing from one that holds up in production.