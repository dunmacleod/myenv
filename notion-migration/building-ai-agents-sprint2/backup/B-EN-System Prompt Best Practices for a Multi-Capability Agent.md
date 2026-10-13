# System Prompt Best Practices for a Multi-Capability Agent

Notion page: https://app.notion.com/p/System-Prompt-Best-Practices-for-a-Multi-Capability-Agent-3669418319f38017aac3cc562b931472
Backed up before n8n migration

> 💡 What you will do in this lesson: Understand the four elements of a well-governed system prompt and why precise instructions become more critical as the agent gains new capabilities.

## Where we are
Meridian's Agentflow v2 now has three capabilities working together. The Agent Node reasons with Gemini. The meridian-knowledge Document Store provides grounded knowledge from internal documentation. The canvas is verified and returning accurate retrieval results.
Now we are going to add conditional routing which is the ability for the agent to send different queries down different paths based on rules or AI reasoning. After that, an HTTP Node will be connected for live data lookups.
Before any of that is added, there is a foundational question worth addressing clearly: what, precisely, is this agent supposed to do, and how should it behave when it encounters the edges of that definition?
This question needs a precise answer encoded in the system prompt. The reason is structural. Once the agent has multiple capabilities, its behaviour is shaped by all of them simultaneously. Debugging unexpected behaviour across several connected components is significantly harder than getting the instructions right while the build is still manageable.

## Why system instructions are governance
Every production-ready business agent requires three things operating together:
[TABLE]
  | Component | What it provides |
  | Reasoning engine | Intelligence: Gemini reads, reasons, and generates |
  | Capabilities | Power: The Document Store, routing nodes, and tools give the agent things it can do |
  | System instructions | Governance: The rules that determine how intelligence and capability are applied |
Without governance, intelligence and capability operate without constraint. For Meridian's agent, ungoverned behaviour is not a theoretical risk. Earlier boundary tests already showed what happens when the agent lacks clear instructions: it fabricates plausible-sounding answers, complies with override attempts, and loses its defined identity under pressure.
A well-written system prompt is what prevents those failures from appearing in production.

## The four elements of a governed system prompt
### Element 1: Role and persona
The role definition tells the model who it is, who it serves, and how it communicates. It should be specific enough to produce consistent behaviour across varied interactions.
A weak role definition:
> You are a helpful assistant.
This tells the model nothing specific. Any behaviour is consistent with being a helpful assistant.
A strong role definition for Meridian:
> You are an internal knowledge and operations support agent for Meridian Consulting, serving the firm's consulting team across their client engagements in Germany, Poland, the Czech Republic, and the Nordic markets. You communicate in a direct, precise, and professional tone appropriate for a consulting environment.
This defines who the agent works for, who it serves, the operational context, and the expected communication style. All of these shape behaviour consistently.

### Element 2: Scope and hard boundaries
Scope defines what the agent is authorised to do. Boundaries define what it must not do under any circumstances. Scope should be defined at the task level, not the topic level.
A topic-level scope:
> Answer questions about consulting work.
This is too broad. Almost any question could be framed as relevant to consulting work.
A task-level scope:
> Surface relevant content from Meridian's internal knowledge base, answer questions about internal process documentation and operational playbooks, and route complex queries to the appropriate specialist within the firm.
This defines specific authorised actions that produce predictable, auditable behaviour.
Hard boundaries must be stated as prohibitions, not preferences.
A preference:
> Try to avoid discussing competitor firms.
This leaves room for the model to decide when an exception is warranted.
A prohibition:
> Do not discuss competitor firms, client confidentiality terms, or ongoing commercial negotiations under any circumstances.
This closes that room entirely.

### Element 3: Capability routing instructions
As the agent gains capabilities, it needs clear instructions for when to use each one and how to handle the outputs.
Without routing instructions, the agent makes capability decisions based on semantic similarity alone. This works when capabilities are clearly distinct but produces routing failures when a query could plausibly be addressed by more than one. For example, a consultant asking about the status of a specific engagement might trigger either a knowledge base retrieval or a live data lookup. Without clear routing guidance, the agent guesses.
Routing instructions should specify:
- The condition under which each capability is invoked
- What information the agent must have before invoking it
- How the agent should handle the output
For Meridian's current build, the routing instruction for the knowledge base is already in the system prompt. As new capabilities are added in the coming lessons, a routing instruction for each one should be added at the same time.

### Element 4: Fallback behaviour
The fallback instruction governs what the agent does when none of its capabilities can resolve the query. Without a defined fallback, the agent produces one of two failure modes: it generates a plausible-sounding answer from Gemini's training data, or it produces a vague unhelpful response that leaves the consultant without a next step. Both are worse than an honest, specific fallback.
A weak fallback:
> I don't know.
This is an abdication. It tells the consultant nothing useful.
A strong fallback for Meridian:
> I do not have the information you are looking for in my current knowledge base. For this query, I would recommend contacting Meridian's knowledge management team directly.
This acknowledges the limitation clearly, names it honestly, and provides a path forward.
![image]((notion-hosted file))

## What a complete Meridian system prompt looks like now
The four elements together produce a system prompt that is specific enough to govern behaviour consistently across all of the agent's current and upcoming capabilities:
> 
  You are an internal knowledge and operations support agent for Meridian Consulting, serving the firm's consulting team across their client engagements in Germany, Poland, and the Czech Republic. You communicate in a direct, precise, and professional tone appropriate for a consulting environment.
  You are authorised to surface relevant content from Meridian's internal knowledge base, answer questions about internal process documentation and operational playbooks, and route complex queries to the appropriate specialist within the firm.
  Do not discuss competitor firms, client confidentiality terms, or ongoing commercial negotiations under any circumstances. Do not answer questions about Meridian's commercial performance, share price, or ownership structure under any circumstances.
  When a consultant asks about Meridian's internal policies, procedures, escalation rules, project classification, knowledge sharing requirements, or regional operational guidelines, retrieve the relevant information from your knowledge base before responding. Always ground your answer in the retrieved content.
  If none of your capabilities can resolve the query, respond with: I do not have the information you are looking for in my current knowledge base. For this query, I would recommend contacting Meridian's knowledge management team directly.
This prompt will be extended as conditional routing and a live data tool are added. Each new capability gets its own routing instruction added to the existing prompt while the role, scope, boundaries, and fallback remain unchanged.

## Check for Understanding
>  Meridian's agent is connected to both the meridian-knowledge Document Store and an HTTP Node for live engagement data. A consultant asks: "Can you check the current status of my engagement?" The agent retrieves a chunk from the knowledge base about project classification tiers and responds with that instead of querying the live data tool. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/770198c8-b1ff-4916-be27-508068162599


> 💡 Takeaway: 
  A system prompt is governance. The four elements are the mechanism that makes the agent's behaviour predictable, auditable, and safe across every query it will ever receive. 
  As Meridian's agent gains new capabilities in the lessons ahead, each one gets a routing instruction added to this framework. The framework itself stays stable.