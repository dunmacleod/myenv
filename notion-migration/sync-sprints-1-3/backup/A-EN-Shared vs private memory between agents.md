# Shared vs private memory between agents

Notion page: https://app.notion.com/p/Shared-vs-private-memory-between-agents-3849418319f3803ab688fc4a7a1b0292
Backed up before n8n migration

Jonas had sent a screenshot. Two messages, same session. The Commercial Agent had responded to a client's pricing question with the correct tier details. Ten seconds later, the Technical Agent had told the same client that their account was on the free tier. Both agents were using allMessages memory. Both were reading the same conversation history. The problem was that the Commercial Agent had written a working assumption about the account to the shared context (something it used internally to calibrate its answer) and the Technical Agent had read that assumption as fact.
The agents weren't broken. They were sharing memory they shouldn't have been sharing.
This is the practical version of the design question from the previous lesson: not where memory lives, but which agents should be allowed to read it. In a single-agent system, that question doesn't arise, there's only one reader. In a multi-agent system like the Vela canvas, every piece of information in shared memory is available to every agent, whether or not that was intended.
> 💡 This lesson is a design exercise. There is no canvas to build. The task is to map the memory boundaries of the Vela system and then apply the same thinking to your own project agent.

## What shared and private mean in practice
Shared memory is any information that one agent writes and another agent can read. In the Vela canvas, $flow.state keys are shared by design. Any node in the canvas can read them. allMessages memory on each Agent Node also shares the conversation history by default, which means an agent that reads allMessages sees everything that has been said in the session, including what other agents have contributed.
Private memory is information that belongs to one agent's execution context and is not accessible to others. A local variable inside a Custom Function node is private — it disappears when the node finishes. A system prompt is private. It instructs one agent and is not forwarded to the next. Structured output fields that are written to a Flow State key become shared the moment they're written; until they're written, they're private.
The line between shared and private is not always obvious from looking at the canvas. allMessages looks like a per-agent setting, but it reads from the conversation history that includes turns from other agents. Flow State looks like a technical detail, but it is the clearest shared surface in the canvas.

## The three design questions
Before deciding what is shared and what is private, answer three questions for each piece of information in the system.
1. Does the receiving agent need this information to do its job? If the Technical Agent doesn't need the Commercial Agent's pricing tier assumption to answer a technical query correctly, that assumption shouldn't be in shared memory. Need is the test. Convenience is not.
1. Could the receiving agent misread this information? A working assumption is not a fact. An intermediate classification label is not a client attribute. Anything that was correct in one agent's context but could be misleading in another agent's context should not be shared or should be clearly labelled as an agent-internal value if it must be written to Flow State.
1. What is the cost if this information is wrong or stale? Some information is low-stakes to share. The client's original query text, the routing decision. Other information is high-stakes — an account status the agent derived rather than looked up, a permission level it inferred from context. High-stakes derived information should either be sourced directly rather than passed between agents, or validated before the next agent uses it.

## The Vela canvas: Mapping what is shared
Open the Sprint 2 canvas (the multi-agent classifier + Commercial / Technical / Hybrid Handler canvas you built in the previous sprint). Identify every piece of information the canvas writes to a location that multiple agents can read. Work through the Flow State keys and the conversation history that allMessages exposes.
The canvas currently writes three keys to $flow.state:
- query_type set by the LLM Classifier node. Value: commercial, technical, or hybrid.
- confidence set by the LLM Classifier node. Value: high or low.
- client_query set by the LLM Classifier node. Value: the original client message.
Each specialist agent (Commercial Agent, Technical Agent, Hybrid Handler) also reads allMessages memory which means each agent sees the full conversation history, including the classifier's output and any prior agent responses.
For each piece of information, complete the table below. Use the three design questions to fill in the Justification column.
[TABLE]
  | Information | Current location | Should it be shared? | Justification |
  | query_type | $flow.state |  |  |
  | confidence | $flow.state |  |  |
  | client_query | $flow.state |  |  |
  | Classifier's reasoning trace (implicit in allMessages) | allMessages history |  |  |
  | Commercial Agent's response (visible in allMessages to subsequent agents) | allMessages history |  |  |
Fill in the "Should it be shared?" column with Yes, No, or Yes with conditions, and write a one-sentence justification for each decision. There is no single correct answer for every row. The right answer depends on how the system is intended to work.

### LLM Node JSON Structured Output
[COLUMN_LIST]
  [COLUMN]
    ![image]((notion-hosted file))
  [COLUMN]
    ![image]((notion-hosted file))
  [COLUMN]
    ![image]((notion-hosted file))

### LLM Node Update Flow State
![image]((notion-hosted file))

## Identifying what should be private
Three categories of information are candidates for private treatment in most multi-agent systems.
- Agent-internal working values. Intermediate results the agent produces on the way to an answer, not the answer itself. The classifier's confidence score is borderline. It might be useful for the Condition node but probably shouldn't inform the specialist agents' responses. The Commercial Agent's internal account tier assumption is clearly internal.
- System prompt contents. Each agent's instructions are private by design. They're not written to Flow State or to allMessages. This is correct behaviour and should stay that way. Be aware that a poorly written system prompt might instruct an agent to echo its instructions back in its response, which would then appear in allMessages and leak to the next agent.
- Sensitive or ephemeral input. If a client shares authentication credentials, a temporary code, or personal information during the session, that information should not persist beyond the handling agent's turn. Storing it in Flow State or relying on allMessages to carry it forward creates a retention problem.
For the Vela canvas, identify one piece of information from each category above that is (or could become) a privacy or reliability concern. Write a one-sentence note on how you would address each.

## Applying the framework to your project
> 🔥 Before you start, make a copy of this template. It mirrors the structure of this lesson — one tab for the Vela shared-or-private mapping, one for the three private-candidate categories, and one for the four-step application to your project.
The Vela exercise is practice. The deliverable is a memory boundary map for your own project agent. Your project agent started as a single-agent system. By this sprint, you have a multi-agent design from Sprint 2, either implemented or documented as a rejected alternative. Either way, you have at least two agent roles defined. Apply the three design questions to your own system.
Work through these steps:
1. Step 1: List every agent in your design. If your Sprint 2 diagram defines a coordinator and two specialists, list all three. If you decided to stay single-agent, list that agent and treat the "other agent" as a hypothetical future addition — the discipline of thinking through boundaries is useful even for single-agent systems.
1. Step 2: List every piece of information that could move between agents. Include Flow State keys, anything written via llmUpdateState, and anything that allMessages would expose to a downstream agent.
1. Step 3: Apply the three questions to each item. Does the receiving agent need it? Could it misread it? What is the cost if it is wrong?
1. Step 4: Write your boundary decisions. For each item, state: shared (and why), private (and why), or shared with conditions (and what the condition is).
> ➡️ This document is the memory boundary section of your Sprint 3 project deliverable. Keep it because during the Sprint 3 Project Deliverable lesson, you will be asked to integrate it with the rest of the architecture specification.

>  
  ### 🔥 Using AI when you get stuck
  If you're finding it hard to decide whether a specific piece of information should be shared or private, try describing the situation to AI clearly:
  - Name the two agents involved.
  - Describe the information in question; what it is, where it comes from, and what a downstream agent would do with it?
  - Ask whether sharing it could cause a reliability or interpretation problem.
  For example: "In a Flowise multi-agent system, the first agent classifies a client query and writes a confidence score to $flow.state. The second agent is a specialist that responds to the query. Should the specialist read the confidence score? What could go wrong if it does?"
  Use the response to pressure-test your decision, not to replace it.

## Watch out for
Treating allMessages as safe by default. Because allMessages is a node-level toggle that feels like a per-agent setting, it's easy to assume each agent has its own isolated memory. It doesn't. Every agent node with allMessages enabled reads from the same session conversation history. If one agent wrote something misleading into that history, the next agent inherits the problem.
Confusing "this agent wrote it" with "this agent owns it." Writing a value to $flow.state does not mean only that agent will use it. Any downstream node can read it. Treat Flow State writes as publishing, not storing.
Leaving the boundary decision implicit. The most common source of memory bugs in multi-agent systems is no decision. If the boundary wasn't explicitly chosen, it defaulted to "shared everything," which is rarely what was intended.

## Summary
Shared memory in a multi-agent system is not just a convenience. It is a design surface that determines what each agent knows, what it might misread, and what happens when information from one agent's context leaks into another's. The three questions in this lesson (need, misreading risk, and cost of being wrong) give you a framework for making those decisions explicitly rather than accepting the defaults.
The boundary map you produced in the "Applying the framework" section is the first concrete output of your Sprint 3 project deliverable. The next lesson adds the second layer: not just what is shared and what is private, but what must never be stored at all. This is information that should leave no trace beyond the agent turn that handled it.