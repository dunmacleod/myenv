# When one agent is enough

Notion page: https://app.notion.com/p/When-one-agent-is-enough-3689418319f38068a804d683ad7ad2e7
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Why a single, well-equipped agent is often the optimal architectural choice and what specific business conditions make adding more agents a liability rather than an advantage.

## The temptation to scale too early
Contigo GmbH's development team has built something genuinely capable. The support agent holds multi-turn conversations, retrieves accurately from the knowledge base, enforces grounding, and handles tool failures gracefully. It is a working, production-ready system.
The team's next planning session produces an immediate proposal: Split the agent into specialised sub-agents. One for loan products. One for compliance queries. One for client account management. One to orchestrate the others.
The compliance lead asks a question that stops the room: 
> What problem, specifically, does adding more agents solve that the current agent cannot handle?
Nobody has a clear answer. The proposal is shelved because the case for building one has not been made. Before introducing coordination complexity, the team needs to understand precisely when a single agent stops being sufficient. That understanding starts here.

## Defining a single-agent architecture
In a single-agent pattern, one language model acts as the central reasoning engine for all tasks. It handles every query through the same model, the same memory, and the same toolset. Every request enters the same reasoning loop and exits through the same response generation step.
- Debugging: When the agent produces an unexpected response, there is one chain of reasoning to inspect. The prompt, the retrieved chunks, the tool output, and the generated response are all part of a single, traceable sequence. In a multi-agent system, the same failure might involve three or four agents passing state between each other, any one of which could be the source of the problem.
- Cost predictability: A single agent makes a bounded number of language model calls per query. The token consumption per interaction is predictable and manageable. Multi-agent systems can consume ten to fifteen times more tokens for the same underlying task because coordination, delegation, and synthesis all require additional model calls.
- Latency: A single agent processes a query in one sequential pass. Every agent added to a system adds at least one additional model call to the critical path of every response.

## When a single agent is the right answer
A single agent handles the majority of business use cases that organisations actually deploy at scale. The conditions that favour a single-agent architecture are consistent across industries.
The task is well-scoped: It has a clear input, a defined goal, and a bounded set of tools needed to achieve it. Contigo's support agent handles loan queries, compliance lookups, and account status checks. These are distinct tasks but they operate within a single domain and draw on a consistent set of capabilities.
The task is repetitive: The same types of queries arrive regularly and the agent's response pattern is stable across them. Contigo's clients ask about loan eligibility, application requirements, and payment options. The agent does not need to invent new reasoning strategies for each interaction.
The task does not require deep cross-domain expertise simultaneously: A query that requires financial analysis, legal interpretation, and software engineering in the same reasoning loop is a genuinely different challenge from one that requires only financial services knowledge. Contigo's queries are firmly in the financial services domain.

## Single agent versus multi-agent at a glance
[TABLE]
  |  | Single-agent architecture | Multi-agent architecture |
  | Complexity | Low — one reasoning chain to build and maintain | High — requires orchestration, routing, and state management |
  | Token cost | Predictable and bounded per query | Variable — can be ten to fifteen times higher |
  | Latency | One sequential pass per query | Each additional agent adds a model call to the critical path |
  | Debugging | One chain of reasoning to inspect | Failures can originate anywhere in the agent network |
  | Best suited for | Focused, domain-specific, repetitive tasks | Complex cross-domain problems requiring specialised parallel execution |
  | Where you build it in this course | n8n workflow canvas | Multiple AI Agent/workflow components; covered in advanced agent-system material |
> ➡️ Why this matters: Everything you have built across Sprints 1, 2, and 3 is a single-agent n8n workflow. Understanding why single-agent architecture is sufficient for Contigo's use case is not just a theoretical exercise. It is the justification for the architectural choices you have already made.

![image]((notion-hosted file))

## Check for Understanding
> 💡 Contigo's development team is considering replacing the current single agent with a four-agent system for the same support use case. What is the most important question to answer before proceeding?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/9cd44e12-0b84-4758-84fb-20cac8a94be3


> 💡 Takeaway: 
  The correct starting point for any agent architecture is the simplest system that can solve the problem reliably. A single agent with well-configured memory, retrieval, and tools handles the majority of business use cases at lower cost, lower latency, and higher debuggability than a multi-agent alternative. For Contigo's support agent as built in this course, no such gap exists. The single-agent n8n workflow with memory, retrieval, and tools is the correct and sufficient architecture.
