# Memory and state failure modes

Notion page: https://app.notion.com/p/Memory-and-state-failure-modes-3849418319f38099ab9cc79b80403dcd
Backed up before n8n migration

By this point, the Vela Systems canvas has a defined memory architecture: boundaries between shared and private state, write ownership per key, a recovery path after interruptions, and four log positions that produce a trace across the full execution chain. The architecture is sound on paper. What it has not been tested against is the specific ways memory and state tend to fail in production — not because the architecture was wrong in design, but because edge cases in real usage expose gaps that controlled testing does not surface.
The Vela team is preparing to hand the system to thirty users. Before that happens, they need to work through a set of scenarios that represent the realistic failure surface of a multi-agent system like theirs: cases where memory causes an agent to return irrelevant or stale output, cases where state causes incorrect routing or silent duplication, and cases where the combination of the two causes a failure that neither individually would produce. Your job in this lesson is to work through those scenarios on the Vela canvas and design a safeguard for each one.
> 💡 In this lesson, you will identify cases where memory or state causes irrelevant, stale, or unsafe agent behavior, and design a concrete safeguard for each.

## What this exercise builds
Identifying failure modes is a design skill, not a debugging skill. A debugger finds failures after they happen. A designer anticipates them before they do and builds the system so that when they occur, the damage is contained.
The failure modes in this lesson are not hypothetical edge cases invented for the exercise. They are the categories of memory and state failure that appear repeatedly in production multi-agent systems. The Vela canvas is the context you know well — use it to anchor your analysis. But the patterns you identify here apply to any multi-agent system, including your own project.
Three categories structure the exercise:
![image]((notion-hosted file))

## Working with documentation
Before starting the scenario analysis, review the Flowise Agentflow V2 documentation for the two mechanisms you will be working with: Flow State (the shared key-value store written and read across nodes) and the Update Flow State configuration on Agent Nodes. The distinction between what is written, when it is written, and who reads it is the source of all three failure categories above.
[TABLE]
  | Mechanism | What it does | Where to look |
  | Flow State | Shared key-value store available to all nodes in the canvas for the duration of a flow run | Flowise docs → Agentflow V2 → Flow State |
  | Update Flow State (Agent Node) | Configuration that writes key-value pairs from the agent's output into Flow State after the node completes | Flowise docs → Agentflow V2 → Agent Node → Update Flow State |
  | Context window | The conversation history visible to a single agent node within its own execution, not shared across nodes | Flowise docs → Agentflow V2 → Memory |
  | Session scope | The boundary within which Flow State keys persist — ends when the session ends | Flowise docs → Agentflow V2 → Sessions |
The reference above is not a checklist to copy. It is a pointer to the documentation you should have open while you work through each scenario. The analysis in each scenario requires you to reason about which mechanism is involved, not just what the symptom is.

## Your task
> 🔥 Before you start, make a copy of this template. It mirrors the structure of this lesson — one tab per scenario, with context, category, mechanism, guiding questions, and a safeguard field, plus a short checkpoint sheet.
Work through the five scenarios below. For each one:
1. Identify the failure category (stale memory, state contamination, or unsafe persistence).
1. Describe what the Vela user would experience, what the output looks like, and why it is wrong.
1. Identify the specific mechanism on the Vela canvas that allows the failure to occur.
1. Design a concrete safeguard, a specific change to the canvas configuration, to the memory architecture, or to the agent's write behavior — that prevents or contains the failure.
Write your safeguard as a concrete design decision: not "add a check" but "the Classifier node resets query_type to null before writing a new value, so a missed write always produces a detectable null rather than a stale classification."
The goal is a set of five safeguard decisions that you can carry directly into your integration work in the next lesson.

### Scenario 1: The Classifier does not reset query_type between queries in the same session
A Vela user sends two queries in the same session. The first is an account inquiry, which the Classifier correctly classifies as account. The Classifier writes query_type: "account" to Flow State and routes to Specialist B. The specialist returns a correct reply.
The same user immediately sends a second query: "Any open support tickets for that client?" This is a support query. The correct classification is support, which should route to Specialist A.
But the Classifier's LLM, processing a short follow-up query in a fast session, produces a malformed output. The Update Flow State step does not execute correctly for the second query. query_type in Flow State still holds "account" from the first query.
The Condition Node reads query_type: "account" and routes to Specialist B again. Specialist B handles account queries. It returns account information for the same client, not the support ticket history the user asked for.
Questions to guide your analysis:
- Which Flow State key is at the centre of this failure?
- At what point in the execution sequence should the key be reset?
- What value should it be reset to, and which node is responsible for that reset?
- How does the log at Position 1 (from the previous lesson) help you detect this failure after it occurs?

### Scenario 2: A specialist agent writes a summary into Flow State that is read by the next query
The Vela canvas is configured so that Specialist B writes a brief account summary into a Flow State key called last_account_summary after every query it handles. This was added as a convenience. The idea was that the summary could be referenced by the final reply node to avoid re-summarising the same content.
A user sends a query about Client A. Specialist B runs and writes last_account_summary: "Client A — renewal due Q3, no open tickets" to Flow State.
The same user, later in the same session, sends a query about Client B. Client B is a different account entirely. The Classifier correctly classifies this as an account query and routes to Specialist B. Specialist B runs and generates a reply about Client B. But the final reply node reads last_account_summary from Flow State — and that key still holds the Client A summary from earlier in the session.
The reply to the Client B query contains an embedded reference to Client A's renewal date.
Questions to guide your analysis:
- Is this a stale memory failure, a state contamination failure, or both?
- What is the write ownership problem in the original design?
- How should last_account_summary be scoped to prevent cross-query contamination within a session?
- If you decided to keep the key, what reset rule would make it safe?

### Scenario 3: A persistent memory store is written with session-specific content
The Vela team added a Qdrant collection to the canvas to store customer account notes. A persistent memory that agents can query across sessions. During a support query, a Vela user types the following: "The client mentioned in our last call that they are considering cancellation. Route this to the account team."
The support specialist agent, following its system prompt, writes the user's full input to the Qdrant collection as a note associated with the client account. The note persists across sessions.
Three days later, a different Vela user handles the same client account. They run an account query. Specialist B retrieves the stored notes from Qdrant. The retrieved note contains the first user's verbatim input (including the phrase "considering cancellation") which was accurate three days ago but has since been resolved. The second user's reply to the client is informed by a stale and now-incorrect status.
Questions to guide your analysis:
- Which category does this failure belong to, and what makes it more serious than a within-session contamination?
- What property of persistent memory makes this failure possible even when the session architecture is correct?
- What should the write rule for the Qdrant collection specify about the content of notes — specifically what must not be written?
- What expiry or invalidation mechanism would reduce the risk of stale persistent notes?

### Scenario 4: Two concurrent sessions write to the same Flow State key
Two Vela users are running queries simultaneously. User A sends an account query. The Classifier writes query_type: "account" to Flow State. At almost the same moment, User B sends a support query. The Classifier for User B's session writes query_type: "support" to Flow State.
Both sessions are writing to a Flow State key that is not namespaced by session ID. There is only one query_type key on the canvas, shared across all sessions.
User A's Condition Node reads query_type and receives "support" the value written by User B's session. User A is routed to Specialist A instead of Specialist B. Specialist A handles a support query on behalf of User A's account context. The reply is incorrect for User A's original question.
Questions to guide your analysis:
- What is the specific mechanism that allows User B's write to overwrite User A's value?
- How does session-namespacing a Flow State key prevent this failure?
- Write out the namespaced key name pattern you would use for query_type on the Vela canvas, and identify which node is responsible for writing it and which node reads it.
- Can this failure be detected from the log at Position 1? What would you look for?

### Scenario 5: A recovery path restores state to the wrong safe state
The Vela canvas has a recovery path: if a specialist agent fails after the Classifier has already written query_type to Flow State, the system recovers by resetting query_type to null and routing back to the Classifier.
During a session, Specialist C fails mid-execution. The recovery path activates. It resets query_type to null correct so far. But it also reads last_routed_agent from Flow State (a key that records which specialist last ran) and writes that value into the reply as a diagnostic message: "Routing to support agent was interrupted. Please re-send your query."
The problem: last_routed_agent holds the value "specialist_c" from the current session correct. But the diagnostic message says "support agent," which is Specialist A, not Specialist C (which handles escalation queries). The label was hardcoded in the reply template and does not match the actual value in last_routed_agent.
A second problem: last_routed_agent is not reset after the recovery path runs. A subsequent query in the same session reads last_routed_agent: "specialist_c" even though the new query has not yet been classified and routed. If anything in the canvas reads last_routed_agent as an input to a decision, it will read a stale value.
Questions to guide your analysis:
- This scenario involves two separate safeguard failures. Name each one clearly.
- For the first failure: what is the correct design rule for user-facing diagnostic messages that reference Flow State values?
- For the second failure: at what point in the recovery sequence should last_routed_agent be reset, and to what value?
- How does a completion signal (a status key) interact with last_routed_agent to make this failure more detectable?

## Hints
[toggle] Use these if you need them.
  - If a Flow State key is read by more than one node and written by only one, the failure is likely a timing or reset problem; ask when the write happens relative to the read.
  - If a key carries information from a previous query into a new query, the fix is almost always a reset at session start or query start; not a change to who reads it.
  - If a key is written to a persistent store, ask whether the content is session-specific or account-level; only account-level, time-stable content belongs in a persistent store.
  - If two sessions share a key name, the fix is namespacing by session ID; the key name becomes query_type:{session_id} rather than a single global query_type.
  - If a recovery message references a Flow State value, the message text must be derived from the actual key value at runtime, not hardcoded in the template.

>  
  ### 🔥 Using AI when you get stuck
  If you are working through a scenario and cannot identify the specific mechanism causing the failure, a useful workflow is:
  1. Name the symptom first in plain language: "The user received the wrong specialist's reply."
  1. Trace backward one step: "What did the Condition Node read to make that routing decision?"
  1. Ask where that value was written and when.
  1. Then ask AI to confirm your diagnosis: "In Flowise Agentflow V2, if a Flow State key is written by the Classifier and then read by a Condition Node, what happens to that key value if the Classifier's Update Flow State step fails to execute? Does the Condition Node read the previous value or null?"
  Use AI to clarify the mechanism, not to do the diagnosis for you. The safeguard you design must be grounded in your own reasoning about the canvas. An AI-generated safeguard that you do not understand will not hold up in your project defense.

## Checkpoints
As you complete each scenario, check your safeguard against these questions:
- [ ] Is the safeguard a concrete design decision (naming a specific node, key, value, or configuration) or is it still a general principle? A general principle is not a safeguard.
- [ ] Does the safeguard prevent the failure, contain the damage, or make the failure detectable? Name which one it does. A single safeguard does not have to do all three.
- [ ] Does the safeguard introduce a new risk, for example, a reset that fires too early and wipes a key that another node still needs?
- [ ] Can the failure be detected from the four log positions designed in the previous lesson? If yes, which position would surface it, and what would you look for in the log?
If a safeguard introduces a new risk you cannot resolve, note it explicitly. A documented tradeoff is better than a safeguard that creates a hidden problem.

## Summary
Anticipating failure modes before integration is the difference between a system that works in a controlled test and one that holds up under real usage. The five scenarios in this lesson represent the categories of memory and state failure that appear in production multi-agent systems: stale memory caused by reset timing, state contamination within a session, unsafe persistence to a shared store, concurrent-session key collision, and recovery paths that restore to an incorrect or stale state.
Each safeguard you designed is a concrete design decision for your Vela analysis and a direct input into your own project's integration work in the next lesson. In the next lesson, you will apply the architecture decisions from Sprints 1 through 3 to your own canvas, with the failure modes from this lesson as the lens for validating that the integration is sound.