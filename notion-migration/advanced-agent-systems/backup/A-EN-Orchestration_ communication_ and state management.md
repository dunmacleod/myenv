# Orchestration, communication, and state management

Notion page: https://app.notion.com/p/Orchestration-communication-and-state-management-3849418319f38017a0d5ea2b8732b4fa
Backed up before n8n migration

Selin has confirmed the pattern: a well-designed single-agent system. Vela does not need multiple agents at this stage. But when Jonas starts sketching the new canvas, he realises that "single-agent" still leaves a lot of decisions open. Which node controls when the Agent Node runs? How does the agent's output get to the right place? What happens to context that needs to carry forward from one step to the next?
These are not configuration questions. They are design questions and they come up in every agent system, regardless of whether it has one agent or ten. Three concerns sit beneath every architectural pattern: orchestration, communication, and state management. Getting all three right is what makes the difference between an agent that works in a demo and one that holds up in production.
> 💡 In this lesson, you will learn what orchestration, communication, and state management each mean and why conflating them is one of the most common sources of agent failures.

## Orchestration
Orchestration is the mechanism that controls when each part of the workflow runs and in what order.
In Agentflow V2, orchestration is explicit: the visual connections between nodes on the canvas define the execution path. The Start Node triggers the Agent Node, which produces an output, which flows to the Direct Reply Node. Nothing runs unless a connected node before it has completed. Nothing is assumed.
This matters because orchestration is where sequence, branching, and looping decisions live. A Condition Node that routes to one of three downstream Agent Nodes is an orchestration decision. A Loop Node that sends a worker's output back to the supervisor is an orchestration decision. An Iteration Node that processes each item in a list before moving on is an orchestration decision.
The failure mode when orchestration is not designed deliberately: nodes run in an order that produces unexpected results, or loops fire without a defined exit condition, or a branch that should handle failures has no path. These are not bugs in a node — they are gaps in the orchestration.
Vela's current baseline has the simplest possible orchestration: Start → Agent → Direct Reply. One path, no branches, no loops. That is appropriate for a single-agent system handling uniform queries. The orchestration becomes more complex the moment the canvas needs to handle different query types or coordinate multiple steps.

## Communication
Communication is how data moves between nodes, what one node passes to the next, and in what form.
In Agentflow V2, communication happens two ways. The first is direct output reference: a downstream node reads the output of a specific preceding node using {{ nodeName.output }}. This is point-to-point. The connection is explicit and the data flows through it automatically.
The second is Flow State: a runtime key-value store shared across all nodes within a single execution that any node can read from or write to using {{ $flow.state.keyName }}. Flow State is not a message passed between two nodes; it is a shared context that any node in the flow can access, regardless of whether it is directly connected to the node that wrote it.
The distinction matters because the two mechanisms solve different problems:
[TABLE]
  |  | Direct output reference | Flow State |
  | Use when | One node's output is the direct input to the next | Data needs to be available to non-adjacent nodes, or across branches |
  | Example | Agent Node output → Direct Reply message | Supervisor writes next to $flow.state; Condition Node reads it on the other side of a branch |
  | Scope | Between two connected nodes | Across the entire execution |
  | Persistence | Not stored — passes through the connection | Stored in memory for the duration of the execution; reset between runs |
The failure mode when communication is not designed deliberately: a node cannot access data it needs because it was passed through a route it is not connected to, or Flow State keys are written without being declared in the Start Node, or a downstream node reads a key that was never updated.
Vela's baseline uses only direct output reference. The Agent Node's output flows directly to the Direct Reply Node. Flow State exists, but nothing writes to them yet. That is by design: the baseline is minimal. Communication becomes a more significant design concern as the canvas grows.

## State management
State management is the discipline of deciding what information persists, where it lives, who can access it, and what happens when a step fails.
State and communication are related but different. Communication is about moving data from one node to another. State management is about the lifetime and ownership of that data — whether it persists across turns, which agents are allowed to read it, and what a safe recovery looks like if something goes wrong mid-execution.

In Agentflow V2, state exists at two levels:
1. Conversation memory: What the agent remembers across turns in a session. Configured on the Agent Node or LLM Node with memory type, window size, and token limit settings. This is the memory that lets a user say "what about the second option?" and have the agent understand what they mean. It persists across turns but is scoped to one conversation thread.
1. Flow State ($flow.state): What nodes share within a single execution. Initialised in the Start Node. Reset at the start of every new execution. Not visible across separate conversations. This is runtime state which is the scratchpad for one run of the flow.
The failure mode when state management is not designed deliberately: an agent carries context from one topic into another (context bleed), a node writes to a Flow State key that was never declared, a failed step leaves a stale value in $flow.state that corrupts a downstream node's reasoning, or memory grows across a long session and degrades routing decisions.

Vela's baseline has memory enabled with allMessages as the memory type. This means every turn in the session is retained and injected into every subsequent prompt. For a short session with a focused topic, that is appropriate. For a longer session covering multiple unrelated queries, it becomes a reliability risk. This is exactly the kind of context bleed that appeared in the first version of Vela's agent.
State management is the concern that scales fastest as agent complexity grows. A single-agent system with one memory configuration and two empty Flow State keys has relatively little to manage. A multi-agent system with multiple agents sharing some state but not others, and with handoffs between agents that carry structured context, has a great deal to manage. Sprint 3 of this module is dedicated entirely to it.

## Why all three must be designed together
Orchestration, communication, and state management are not independent. A change to one affects the others.
![image]((notion-hosted file))
If the orchestration adds a new branch, the communication design must ensure that the data needed on that branch is available, either through a direct connection or through Flow State. If communication relies on Flow State, the state management design must ensure those keys are declared, initialised correctly, and handled gracefully if a node fails to write to them. If state management introduces a new memory boundary between agents, the orchestration must define which path each agent takes so the boundary is respected.
This is why agents that are built node by node, without a design that considers all three, tend to develop gaps that only appear at scale or under real usage conditions. Vela's first agent had implicit orchestration (one path, no branches, no defined failure handling), implicit communication (no Flow State design, just a direct output reference), and implicit state management (memory on by default, no rules about what to retain or clear). It worked until it didn't.
The architecture brief you produce at the end of this sprint (and the project brief you develop in your live sessions) will document all three for the agent you are designing. Not as an academic exercise, but because a brief that names the orchestration pattern, the communication mechanism, and the state boundaries is a canvas that can be built, tested, and handed to someone else without explanation.

## Summary
Every agent architecture makes decisions across three concerns: orchestration controls when things run, communication controls how data moves, and state management controls what persists and for how long. The three are interdependent. A gap in any one tends to surface as a failure in one of the others.
Vela's baseline has all three, but in their simplest forms: linear orchestration, direct-output communication, and default memory state. What the next lessons build toward is making those decisions deliberately rather than by default and knowing how to justify each one. The decision framework in the next lesson is the tool for doing that.
