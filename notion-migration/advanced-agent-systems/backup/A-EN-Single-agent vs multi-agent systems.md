# Single-agent vs multi-agent systems

Notion page: https://app.notion.com/p/Single-agent-vs-multi-agent-systems-3849418319f380c9acc9cdb9f9c9a5b3
Backed up before n8n migration

After reviewing what went wrong with the first version of Vela's agent, Selin called a short planning session with Jonas and Petra. The conclusion from the previous lesson was clear: the agent failed not because it lacked capability, but because it had no architectural plan. Now the team needs to make their first real design decision before rebuilding anything on the canvas.
A colleague from another team has suggested the solution is simple: "Just add more agents." Selin isn't convinced. Adding agents means more nodes, more coordination logic, more places for things to go wrong, and more API calls per query. That has a cost — in latency, in tokens, and in debugging time. The question isn't whether multi-agent systems are more powerful. The question is whether Vela's problem actually requires one.
This lesson gives the team (and you) the framework to answer that question.

## What a single-agent system is
A single-agent system has one Agent Node doing all the reasoning. It receives the user's input, decides what to do, uses whatever tools or knowledge it has access to, and produces a response. The entire decision-making path runs through one node.
This is not a limitation. A well-designed single-agent system can handle routing logic, tool use, memory across turns, and diverse query types — all within one Agent Node, driven by a clear system prompt and connected to the right inputs.
Vela's current baseline is a single-agent system. One Start Node, one Agent Node, one Direct Reply Node. The Agent Node uses Gemini to reason about each query and respond. Nothing about that structure is wrong. The question is whether it is sufficient for what Vela needs.

## What a multi-agent system adds
A multi-agent system has more than one Agent Node, each with a defined role. One agent might handle information queries. Another handles action requests. A supervisor agent might decide which specialist to engage based on the incoming query. The agents coordinate — passing context, results, and control between them through the canvas.
Multi-agent systems solve a specific set of problems that single agents genuinely cannot:
- Specialisation at scale. When a single agent handles too many different types of tasks, its system prompt becomes long, its tool list grows, and its routing decisions become unreliable. Splitting the work across specialist agents (each with a narrow, well-defined scope) produces more consistent results.
- Parallel or sequential work. Some tasks require one step to complete before another can begin, or two steps to run at the same time. A single agent completes one thing at a time in a linear loop. Multi-agent architectures can structure the work differently.
- Failure isolation. When one agent in a multi-agent system fails, its failure does not necessarily corrupt the others. A single-agent failure is a total failure.
The cost of these benefits is real: more nodes, more coordination logic, higher latency per request, more tokens consumed per interaction, and harder debugging when something goes wrong between agents rather than inside one.

## The decision framework
The choice between single-agent and multi-agent should follow from the problem, not from a preference for complexity. Four questions make the decision clear.
![image]((notion-hosted file))

1. Can one well-scoped agent handle the full range of inputs reliably?
If the agent's scope is narrow enough that a clear system prompt governs all query types without becoming unwieldy, a single agent is appropriate. Vela's agent answers questions about inventory, fulfilment, and supplier communications; three related areas that share context. One well-scoped agent could cover all three.

2. Does the work require specialist knowledge or tools that conflict with each other?
If different query types need fundamentally different tools, access levels, or reasoning approaches (and combining them creates routing confusion) specialised agents produce better results. If the tools and knowledge work well together in one system prompt, they do not need to be split.

3. Does a failure in one part need to be isolated from the rest?
If one failure should not cascade into the whole agent stopping, multi-agent gives you isolation boundaries. If total failure on one query is acceptable and recoverable, single-agent is fine.

4. Is the complexity cost justified by the reliability gain?
Multi-agent systems are harder to build, test, and debug. If the reliability gain from splitting agents does not outweigh the coordination overhead introduced, the complexity is not earned. Default to the simpler system until the problem demands more.

[TABLE]
  | Signal | Points toward |
  | Scope is narrow and stable | Single agent |
  | System prompt is becoming long and unreliable | Multi-agent |
  | All tools belong together logically | Single agent |
  | Tools conflict or create routing confusion | Multi-agent |
  | A failure should stop the whole response | Single agent |
  | A failure in one part should not stop others | Multi-agent |
  | Coordination cost is low relative to reliability gain | Multi-agent |
  | Coordination cost exceeds the reliability benefit | Single agent |

## Applying the framework to Vela
Selin walks the four questions against Vela's actual problem.
The agent handles three related areas: inventory, fulfilment, and supplier communications. These share enough context that one system prompt can govern all three without becoming unmanageable. The tools Vela needs are logically compatible. A failure on one query type does not need to be isolated from the others. And the team is small; Jonas and Petra will maintain this agent, and adding coordination logic between multiple agents introduces work they cannot absorb right now.
The answer for Vela, at this stage, is a well-designed single-agent system. Not because multi-agent systems are more complicated, but because the problem does not yet justify the cost.
This conclusion is revisable. If Vela's agent scope expands significantly, or if the system prompt starts producing inconsistent routing, or if the team grows to support more complex infrastructure, then the decision changes. Architectural decisions are not permanent. They are appropriate to the problem at the time they are made.
In your live session, you will apply this same framework to your own project. The decision you make there will be the foundation of your Sprint 1 architecture brief.

## Summary
The distinction between a single-agent and a multi-agent system is not about sophistication — it is about fit. A single agent with a clear scope, a well-written system prompt, and the right tools can outperform a multi-agent system that is over-engineered for the problem in front of it.
The four-question framework (scope, specialisation, failure isolation, and coordination cost) is what turns this from a gut feeling into a defensible decision. Vela's answer is single-agent for now. The next lesson introduces the full range of architecture patterns available, so you can see where single-agent and multi-agent fit within a broader set of design choices.