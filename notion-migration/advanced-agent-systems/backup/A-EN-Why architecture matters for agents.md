# Why architecture matters for agents

Notion page: https://app.notion.com/p/Why-architecture-matters-for-agents-3849418319f38087a2f4d4627ba46a40
Backed up before n8n migration

Vela Systems has a working agent. Selin, the product manager leading the AI practice, built it with Jonas and Petra over two weeks, a single Agentflow V2 canvas with a Start Node, an Agent Node, and a Direct Reply Node. It can hold a conversation, answer questions about inventory and fulfilment, and stay within its defined scope. During internal testing, it handled every query the team threw at it.
Then they opened it to the broader operations team.
Within three days, the agent started giving inconsistent answers to the same question depending on how it was phrased. During a busy period, response times slowed and eventually it stopped responding to some queries entirely. When Jonas tried to add a supplier communication feature, he found that the change he needed to make touched the same part of the canvas as the memory configuration and adjusting one broke the other.
Nothing crashed. There was no error message. The agent just became unreliable in ways that were hard to trace, hard to fix, and hard to explain to the rest of the team. The problem was not the agent's capability. It was the architecture.

> 💡 In this lesson, you will learn why the decisions made when designing an agent determines whether it stays reliable as it grows.

## What architecture actually means
Architecture is not the same as configuration. Configuration is the settings you apply to individual nodes: which model to use, what the system prompt says, how many messages to keep in memory. Architecture is the decisions that determine how those nodes relate to each other: how data flows between them, who owns what information, and what happens when something goes wrong.
When an agent is small (one node doing one thing) architecture barely matters. The canvas is the architecture, and it is simple enough that you can hold it in your head. But as an agent grows, architectural decisions made early become load-bearing. Change one thing and something unexpected shifts elsewhere.
Vela's agent grew without an architectural plan. The memory configuration was entangled with the routing logic. The system prompt carried responsibilities that belonged in separate nodes. There was no defined path for failure. The agent worked until it was used at real scale, by real people, in real conditions and then the gaps showed.

## The three things architecture determines
Every agent architecture makes decisions across three dimensions. Each one produced a specific failure at Vela.
Reliability is whether the agent does what it is supposed to do, consistently, across all the inputs it will actually receive. Vela's agent gave inconsistent answers to rephrased queries because the routing logic was implicit inside a single overloaded Agent Node. There was no explicit path for different query types. The model inferred the routing from context and inferred it differently depending on phrasing.
Scalability is whether the agent holds up as volume, complexity, or scope increases. When Vela's operations team started using the agent simultaneously, response times degraded and some queries stopped being answered. The architecture had no way to separate high-priority queries from routine ones. Everything went into the same node, in the same way, at the same pace.
Maintainability is whether the agent can be changed (i.e. adding a feature, fixing a behaviour, updating a prompt) without unintended consequences elsewhere. Jonas found that the canvas had grown into a single point of coupling: the memory configuration and the routing logic shared the same node, so modifying either required understanding both. A change that should have taken twenty minutes took most of a day and introduced a new problem.
![image]((notion-hosted file))

## Why this matters before you build
Most agent problems that appear at the usage stage were decided at the design stage. By the time an agent is in the hands of real users, the architectural decisions are baked in. Changing them requires reworking the canvas.
This is the difference between fixing a reliability problem and re-architecting an agent. Fixing a reliability problem means adjusting a prompt or a retrieval setting. Re-architecting means changing how nodes relate to each other, how state flows between them, and where responsibility sits. It is a much larger piece of work, and it is almost always done under pressure, because by the time it becomes necessary, the agent is already in use.
The goal of this module is not to teach you to build agents differently. It is to teach you to design them first to make the decisions that determine reliability, scalability, and maintainability before they get baked into a canvas that is harder to change.
Vela's three-node agent is not a bad agent. It is an undesigned one. The next lessons introduce the tools for designing it properly.

## Summary
Vela's agent worked in testing and broke in production because no one had made explicit decisions about how the architecture should handle real usage. The three failures the team experienced each traced back to a different dimension: inconsistent answers came from a reliability gap, slow responses from a scalability gap, and a day lost to a twenty-minute change from a maintainability gap.
Architecture is what determines which of those gaps exist before the agent reaches its first real user. The rest of this sprint introduces the frameworks for identifying the right architectural decisions for a given problem and for explaining those decisions clearly enough to defend them.