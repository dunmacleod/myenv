# Common architecture mistakes

Notion page: https://app.notion.com/p/Common-architecture-mistakes-3849418319f380c0a203c1da9d6781bf
Backed up before n8n migration

Selin reviews the first version of Vela's agent (the one that broke in production) with fresh eyes. The failure modes from the opening lesson of this sprint are now easier to name: inconsistent routing answers, degraded performance under load, a twenty-minute change that took a full day. At the time, the team diagnosed these as bugs. They patched them one at a time. The patches introduced new problems.
What Selin can see now is that each failure traced back to a specific architectural mistake made before a single node was added to the canvas. The mistakes did not look like mistakes when they were made. They looked like reasonable shortcuts — a quick way to get the canvas working faster, a configuration that seemed harmless, a design decision that felt flexible at the time.
> 💡 This lesson names the three mistakes that appear most often in real agent systems, explains why they are hard to spot before they cause damage, and shows how to recognise each one early enough to fix it at the design level rather than the patch level.

## Mistake 1: Over-engineering
- What it is: adding more nodes, more agents, more routing logic, and more coordination overhead than the problem actually requires.
- Why it happens: complexity feels like thoroughness. A canvas with a supervisor node, three specialist workers, a Loop Node, and four branches of Flow State handling looks more capable than a single Agent Node with a clear system prompt. It is more capable for a problem that needs that level of coordination. For a problem that does not, the extra nodes are a liability.
Over-engineering shows up in two forms. The first is premature multi-agent: splitting a single agent into two or more agents before there is evidence that one agent cannot do the job. The second is unnecessary branching: adding Condition Nodes and routing paths for scenarios that have not yet appeared, on the assumption that they eventually will.
Both forms share the same cost: more nodes means more places for execution to fail, more Flow State keys to manage, more tool descriptions to keep non-overlapping, and a harder debugging surface when something does go wrong.
- The Vela example: the first version of Vela's agent had implicit routing logic inside a single Agent Node that was asked to do too many things. The proposed fix from Jonas's colleague was to add multiple specialist agents. That would have been over-engineering — the problem was not that one agent was insufficient. The problem was that the one agent had not been designed deliberately. A well-scoped single agent with a clear system prompt handles Vela's three query types more reliably and with less overhead than three specialist agents with a supervisor routing between them.
- The signal to watch for: if the justification for adding another agent is "it might be useful later" or "it feels more robust," that is over-engineering. The justification for adding another agent should be a specific, observable failure in the existing agent that the new agent is designed to fix.

## Mistake 2: Hidden state
- What it is: Using Flow State in ways that are not declared, documented, or predictable — writing to a key that was never initialised, reading a key whose value depends on a path the current execution may not have taken, or letting state accumulate across a session in ways that affect later queries.
- Why it happens: Flow State is convenient. Any node can write to any key at any point in the execution. That flexibility makes it easy to pass data between non-adjacent nodes without adding explicit connections. It also makes it easy to introduce state that no one designed and no one fully understands.

Hidden state has three common forms:
1. Undeclared keys: A node writes to $flow.state.approval_result without that key being initialised in the Start Node. The key exists and the write succeeds, but there is no explicit record that the key is part of the architecture. When a different node later tries to read $flow.state.approval_result on a path where the writing node never ran, it receives an undefined value. The downstream node behaves unexpectedly, and the cause is not obvious from the execution trace.
1. Path-dependent values: A key is written on one branch of a Condition Node but not the other. A downstream node that reads the key on both branches behaves correctly on the branch where the write happened and incorrectly on the branch where it did not — but only under the specific input conditions that trigger the unwritten branch. This class of bug is easy to miss in testing and difficult to reproduce.
1. Session accumulation: Memory configured with allMessages and no window limit retains every turn of a long session. The Agent Node injects that full history into each new prompt. After twenty turns covering three different topics, the context window contains irrelevant earlier turns that bias the agent's interpretation of new queries. The agent is not broken — it is reasoning correctly from a context that is no longer appropriate.

- The Vela example: The baseline canvas has two Flow State keys pre-declared but empty: query_type and status_response. Those exist precisely to prevent hidden state: the keys are visible in the Start Node, their purpose is named, and any node that writes to them is doing so into a known, declared structure. Adding keys at the node level without declaring them in the Start Node is the mistake this design pattern prevents.
- The signal to watch for: if a Flow State key appears in a node's configuration but not in the Start Node's initialisation list, it is hidden state. Audit the Start Node against every $flow.state reference in the canvas before the architecture is considered complete.

## Mistake 3: Brittle handoffs
- What it is: designing a connection between two nodes, or two agents, where one node's output is assumed to arrive in a specific format, and there is no handling for what happens when it does not.
- Why it happens: when building a canvas, it is natural to test the happy path first. Agent A produces a well-structured response. Agent B reads it and uses it correctly. The connection works. The problem is that Agent A's output format is not guaranteed. It is the result of a model inference, and model inference is not deterministic. Under slightly different input conditions, the same Agent Node may produce a response with a missing field, a different key name, or a format that a downstream node cannot parse.
Brittle handoffs manifest in three specific ways:
1. Format dependency: A Condition Node expects $flow.state.next to contain one of three specific string values ("worker_a", "worker_b", "done"). The supervisor LLM Node is prompted to write one of those three values. Under most inputs, it does. Under some inputs such as ambiguous requests, very short inputs, inputs in an unexpected language; it writes "Worker A" or "complete" or nothing. The Condition Node has no matching branch and the execution fails silently.
1. Missing fallback: An Agent Node is connected to a Direct Reply Node on the success path. There is no path defined for what happens if the Agent Node produces an empty response or an error. The execution reaches a dead end with no Direct Reply fires, the conversation stops, and the user receives nothing.
1. Tight coupling: Agent A's output is used directly as Agent B's system prompt context, with no transformation step between them. When Agent A's output changes in length, structure, or tone, Agent B's behaviour shifts unpredictably because its context has shifted. The two agents are coupled without a defined interface between them.

- The Vela example: An earlier Vela canvas used a Loop Node with a Max Loop Count of 2 and a fallback Direct Reply on the "retries exhausted" branch. That was a deliberate handoff design. The loop had a defined exit condition, and the exit path had a defined response. That is the right approach. A canvas where the Loop Node has no Max Loop Count, or where the retry-exhausted branch leads nowhere, is a brittle handoff waiting to fail.
- The signal to watch for: For every node connection on the canvas, ask: what happens if the upstream node produces an unexpected output? If the answer is "the canvas has no path for that," the handoff is brittle.
![image]((notion-hosted file))

## How the three mistakes relate to the three pillars
Each mistake is a failure in one of the three architectural pillars from the previous lesson:
[TABLE]
  | Mistake | Root pillar | Observable symptom |
  | Over-engineering | Orchestration | Canvas is harder to debug than the problem justifies; coordination nodes add latency without adding reliability |
  | Hidden state | State management | Unexpected agent behaviour that varies by execution path; context bleed across topics; undeclared keys producing undefined reads |
  | Brittle handoffs | Communication | Execution stops silently; downstream node behaves unexpectedly on specific inputs; no fallback path fires |
This mapping matters because the fix for each mistake lives in the same pillar as the mistake. Over-engineering is corrected by simplifying the orchestration — removing nodes that are not earning their place. Hidden state is corrected by auditing the state management — ensuring every key is declared, and every write happens on every execution path that downstream nodes later read from. Brittle handoffs are corrected by designing the communication deliberately — adding explicit format constraints, fallback paths, and transformation steps between tightly coupled nodes.
Knowing which pillar a mistake belongs to points directly to where the fix should be made.

## Check for Understanding
>  Jonas reviews the redesigned Vela canvas before the Sprint 1 walkthrough. He notices that the supervisor LLM Node writes $flow.state.next to indicate which worker should act next, but the key is not listed in the Start Node's Flow State initialisation. The Condition Node downstream reads $flow.state.next to route to the correct worker. Which mistake does this represent?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/5397f76c-6169-4249-9124-ac63df8268d5

## Summary
Three mistakes, three root pillars, three early warning signals. Over-engineering adds coordination overhead that the problem does not justify. The signal is a canvas that is harder to debug than the problem requires. Hidden state creates keys and memory that are not part of the declared architecture. The signal is a Flow State key that appears in a node but not in the Start Node. Brittle handoffs assume output formats that are not guaranteed, the signal is a node connection with no path for unexpected input.
The Sprint 1 walkthrough in the next lesson builds a single-agent system for Vela with all three mistakes deliberately avoided: the orchestration is no more complex than the problem requires, every Flow State key is declared in the Start Node, and every connection has a defined path for the case where the upstream node produces an unexpected output. That is what a deliberately designed agent looks like before it is tested.