# Flowise and AI Agent Checkpoint

Notion page: https://app.notion.com/p/Flowise-and-AI-Agent-Checkpoint-3669418319f380468657c791cf3e8aab
Backed up before n8n migration

> 💡 What this assessment covers: This assessment validates your ability to configure a working Flowise and Gemini agent, define its purpose and boundaries clearly, and demonstrate that it behaves as intended under both standard and adversarial conditions. All three tasks are required.

> 🔥 Before you begin, make a copy of this Google Sheet template. Three tabs match Tasks 1 and 2: agent specification, canvas + conversation log, and behaviour evaluation. The Knowledge Quiz (Task 3) is completed on the platform, not in the template.

## Context
Throughout this sprint, Meridian Consulting's development team has moved from infrastructure setup through to a working, constrained agent. The environment has been verified, the stack has been understood, the baseline agent has been built, and the system prompt has been tested against boundary-breaking scenarios.
This checkpoint asks you to bring those elements together into a single coherent deliverable. The agent you create is the foundation that retrieval, memory, tools, and platform comparison work will be built on in the sprints ahead. Getting it right now matters.

## Task 1: System prompt and agent documentation
Before submitting your agent, document its intended design in writing. This documentation serves two purposes: it forces clarity about what the agent is supposed to do, and it provides a reference point for evaluating whether the agent's actual behaviour matches the intention. 
Write a short agent specification that covers the following three sections.
- Role and persona: Describe who the agent is, who it serves, and how it communicates. Be specific enough that someone unfamiliar with the project could read this section and understand the agent's identity and tone without needing to see the system prompt itself.
- Scope: List the specific tasks and topic areas the agent is authorised to handle. Name the categories of query the agent should engage with and, where relevant, the categories it should not.
- Limitations and escalation: Describe what the agent does when a query falls outside its defined scope. Specify the escalation behaviour. Does it redirect to a human colleague, explain the boundary and stop, or ask a clarifying question? Explain why you chose this behaviour for Meridian's context.

## Task 2: Flowise canvas submission and test report
#### Part A: Canvas screenshot
At this time, your canvas must show all of the following components connected correctly:
- A Start Node as the entry point of the flow
- An Agent Node authenticated with your API key, configured to use your AI model, and containing your custom system prompt in the System Prompt field
- A Direct Reply Node connected to the output of the Agent Node
- All three nodes connected by visible edges forming a continuous execution path: Start Node → Agent Node → Direct Reply Node
#### Part B: Test report
Run a multi-turn conversation in the Flowise chat interface that demonstrates the following three behaviours in a single continuous session of at least seven exchanges, with a minimum of two turns dedicated to each of the three behaviour tests:
- Context retention: Establish a specific piece of information early in the conversation such as a name or account and confirm the agent references it correctly in a later turn within the same session without being prompted again. This tests whether the Agent Node is maintaining session context correctly.
- Scope enforcement: Submit a request that falls clearly outside the agent's defined scope and confirm the agent handles it according to the escalation behaviour described in your specification.
- Boundary observation: Attempt a prompt injection by instructing the agent to ignore its system prompt or adopt a new identity. Document exactly what you sent and what the agent responded. Whether the agent resists or complies, write two to three sentences explaining why you think the outcome occurred.
Run the session as a single continuous conversation of at least seven exchanges, allowing enough room to establish context for the context retention test, submit and evaluate the out-of-scope request, and conduct the boundary observation with a follow-up turn.
Write a short evaluation covering all three behaviours. For each one, note whether the agent behaved as intended and identify any gap between the intended behaviour described in your specification and the actual behaviour observed. If the agent failed a test, describe the specific prompt revision you made in response and whether it resolved the failure.
A documented failure followed by a reasoned revision is a valid and instructionally valuable outcome at this stage. The evaluation is assessing your ability to diagnose and improve the agent's behaviour, not only whether the agent passed every test on the first attempt.

## Task 3: Knowledge Quiz
Complete all four questions below. Read each option carefully before selecting your answer.
### Question 1
>  Meridian's agent is running on the API free tier during a busy morning when multiple consultants are querying it simultaneously. The agent begins failing mid-conversation with no visible error in the Flowise canvas. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/89c0f8ed-4c70-4b6a-8802-0428574f5db9

### Question 2
>  A Meridian consultant attempts to override the agent's identity mid-conversation by instructing it to ignore its system prompt. The agent complies and begins behaving as a general-purpose assistant. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/650527fe-ae9d-46fd-8cb5-f2154ed3d2b6

### Question 3
>  In an Agentflow v2, a Meridian developer adds a Condition Node to the canvas to route queries to different paths but forgets to draw an edge from the Agent Node to the Condition Node. The flow is saved and tested. What happens at runtime?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/aa5fe3b7-7f5e-49b2-8bc6-4b916923c623

### Question 4
>  Which two practices together form the minimum security baseline for handling an API key when using Flowise?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f8df0c78-b566-4e64-9ea1-2ecdeafcda5e

> 💡 Takeaway: 
  The Agentflow v2 configured here (Start Node, Agent Node, Direct Reply Node) is the foundation that retrieval, conditional routing, tools, and orchestration logic will be built on in the sprints ahead.
