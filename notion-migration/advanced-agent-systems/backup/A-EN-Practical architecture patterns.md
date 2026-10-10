# Practical architecture patterns

Notion page: https://app.notion.com/p/Practical-architecture-patterns-3849418319f3807997f0fbe3b024f6bd
Backed up before n8n migration

Selin now knows that Vela needs a single-agent system for the moment. The scope is manageable, the tools are logically compatible, and the coordination overhead of splitting agents is not yet justified. But "single agent" is not a complete design. It describes the number of agents, not what the agent does, how it makes decisions, or what happens when it fails.
Before Jonas opens the canvas, the team needs to agree on which architectural pattern fits the problem. In Agentflow V2, different patterns use different combinations of nodes. Choosing the wrong pattern means rebuilding later, which is the situation Vela is already trying to avoid.
This lesson introduces the six patterns that appear most often in real agent systems. Some of them you have seen on a canvas before. Two of them are new.

## The six patterns at a glance
Each pattern solves a different design problem. The name describes the structure, not the capability. An agent built on any of these patterns can be powerful or weak. The pattern determines how decisions are made and how work flows, not whether the underlying model is good.
![image]((notion-hosted file))

## Single agent
- The structure: one Agent Node receiving input and producing output. Everything (reasoning, tool selection, and response generation) happens inside one node.
- When it fits: the scope is narrow and stable. The system prompt can govern all query types clearly. Tool use is simple or absent. The volume of requests does not require separation.
Vela's baseline is this pattern. The Sprint 1 walkthrough builds a deliberately designed version of it as a single-agent system with explicitly defined inputs, outputs, and responsibilities.

## Tool-using agent
- The structure: an Agent Node connected to one or more tools (a HTTP Node, a Custom Function Node, or an external API call). The agent decides at runtime which tool to invoke and when.
- When it fits: the agent needs to reach outside its own reasoning to retrieve live data, perform a calculation, or trigger an action. The tools have distinct, non-overlapping purposes so the agent can select the right one reliably.
- The key authoring decision: tool descriptions. The Agent Node selects tools based on how their purpose is described in the configuration. A vague description, "use this to get data," produces inconsistent selection. A precise description "use this to retrieve the current stock level for a specific product SKU when the user asks about inventory" tells the model exactly when to invoke it.

## Workflow + agent
- The structure: a sequence of nodes where some steps are deterministic (a Condition Node checking a value, a Custom Function Node transforming data, an HTTP Node fetching a record) and one or more Agent Nodes handle the parts that require reasoning.
- When it fits: some steps in the process are predictable enough to be handled with fixed logic, while others require interpretation. Mixing deterministic steps with agentic reasoning keeps costs down and behaviour consistent for the predictable parts.
- The distinction from a pure agent: in a workflow + agent pattern, the canvas controls the flow. The Agent Node reasons about its specific task within that flow, but the overall execution path is defined by the node connections, not by the agent's runtime decisions.

## Router
- The structure: a Condition Agent Node that classifies the input and directs it to one of several downstream paths. Each path handles a specific type of query.
- When it fits: the agent receives meaningfully different types of input that benefit from different handling — a query about policy versus a request to check a live status versus an escalation request. Routing separates these at the entry point rather than asking one overloaded Agent Node to handle everything.
You have seen this pattern before. In an earlier course, the Condition Agent Node was used to classify queries as status_request, knowledge_query, or briefing_request. That was a router. The pattern itself is the same here; the design decisions around it (how many routes, how precisely each scenario is described, what happens on each branch) are what change per use case.

## Evaluator
- The structure: one Agent Node (or LLM Node) produces an output. A second node (typically another LLM Node or Condition Agent Node) evaluates whether that output meets a defined quality bar before it proceeds.
- When it fits: the first agent's output needs to be checked before it reaches the user or triggers a downstream action. The evaluation can be rule-based (does the response contain a required field?) or model-based (is this response accurate and within scope?).
- The distinction from a router: a router decides where to send the input. An evaluator decides whether the output is good enough to proceed. They look similar on the canvas, both involve a decision node, but they operate at different points in the flow and answer different questions.
A Human Input Node can serve as a manual evaluator when the stakes are high enough that a human needs to approve before the output is delivered.

## Supervisor-worker
The structure: an LLM Node acts as the supervisor. It analyses the task, decides which specialist worker should act next, and writes that decision to Flow State — the runtime key-value store that passes data between nodes within a single execution. A Condition Node reads the Flow State and routes to the corresponding Agent Node (worker). Each worker returns its result to the supervisor via a Loop Node. The supervisor reviews the result and either assigns the next worker or concludes with a Final Answer Agent Node.
When it fits: the task is complex enough that it benefits from being broken into sub-tasks handled by specialists. The supervisor coordinates; the workers execute. This is the most powerful pattern in this module — and the most expensive, because the supervisor and each worker each make their own model call.
This pattern is new. You have not built it before. Sprint 2 introduces it step by step.
[TABLE]
  | Element | Role in the pattern |
  | LLM Node | Supervisor — decides which worker acts next; uses JSON Structured Output to write next and instruction to $flow.state |
  | Condition Node | Reads $flow.state.next and routes to the matching Agent Node |
  | Agent Node (×2 or more) | Workers — each has a specific role and system prompt; reads $flow.state.instruction as its task |
  | Loop Node | Returns the worker's output to the supervisor for review |
  | Agent Node (final) | Compiles the collaborative output into a single coherent response |
## Choosing between them
No pattern is universally better than another. The choice follows from the problem:
[TABLE]
  | If the problem is… | Pattern to consider |
  | A narrow, well-scoped set of queries with no complex routing | Single agent |
  | Queries that need live data or external actions | Tool-using agent |
  | A process with predictable steps mixed with reasoning steps | Workflow + agent |
  | Input that arrives in meaningfully different types | Router |
  | Output that needs checking before it reaches the user | Evaluator |
  | A complex task that benefits from specialist sub-tasks | Supervisor-worker |
For Vela's current problem (internal queries across three related areas, single agent confirmed), the right pattern is a well-designed single agent, possibly with one or two tools attached if live stock or supplier data becomes necessary. That is the pattern the Sprint 1 walkthrough builds.

## Check for Understanding
>  Selin reviews a new requirement from Vela's operations team. When a consultant submits a request to the agent, the agent drafts a response. But before it is delivered, it must be checked to confirm it does not reference outdated supplier terms. Which pattern handles this requirement?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d9030af1-3cc8-4129-92dd-3e8fed6b8aa4


## Summary
Six patterns cover the vast majority of real agent architectures: single agent, tool-using agent, workflow + agent, router, evaluator, and supervisor-worker. Each solves a different design problem. The router and the evaluator are easy to confuse because both involve a decision node. The distinction is whether the decision is about the incoming input or the outgoing output.
For now, Vela's answer is a well-designed single agent. The next lesson adds the second layer: once a pattern is chosen, three design pillars (orchestration, communication, and state management) determine whether the canvas built on that pattern actually holds up in production.