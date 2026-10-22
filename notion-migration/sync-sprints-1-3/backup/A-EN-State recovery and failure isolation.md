# State recovery and failure isolation

Notion page: https://app.notion.com/p/State-recovery-and-failure-isolation-3849418319f3804d83cad67c0985a005
Backed up before n8n migration

The previous lesson added a fallback branch to the Vela canvas for when the Classifier returns unclassified. That is one form of state recovery: a clear path for a predictable failure. But recovery does not only mean handling bad classification results. It also means designing what happens when an agent fails mid-execution, when shared state is left in a partial or misleading condition, and when one agent's failure should not be allowed to affect what the next agent reads.
Jonas had raised the scenario in the team's last design review. What if the Commercial Agent fails after the Condition node has already routed to it after query_type has been written as commercial and the Classifier has completed successfully? The client gets no response, but Flow State now holds commercial as the current query type. If the session continues and the client sends a second message, the Classifier runs again and overwrites query_type correctly so the stale value clears. But what if the client doesn't send a second message? What if an external system reads query_type from Flow State to log the interaction, and it reads commercial even though the Commercial Agent never completed?
This is the failure isolation question: When one agent fails, does its failure corrupt the state that other parts of the system rely on?
This lesson is a design exercise. There is no canvas to modify. The task is to map the failure modes in the Vela system, apply the same analysis to your own project, and produce the state recovery and failure isolation section of your Sprint 3 project deliverable.

## Two distinct problems
State recovery and failure isolation are related but address different moments in a failure.
State recovery is about what happens after a failure. Can the system return to a known-good state, and what does "known-good" look like? For the Vela canvas, the unclassified fallback branch is a recovery mechanism: the system detects that the Classifier did not produce a usable result and routes to a safe path. The state after recovery is predictable. query_type holds unclassified, the fallback Direct Reply has fired, and the session can continue.
Failure isolation is about what happens to other agents and state keys when one agent fails. In the Vela canvas, if the Commercial Agent throws an error after query_type has been written to Flow State, the other state keys (confidence, client_query ) still hold values from the Classifier's run. If a future agent or external system reads those keys, it will see a state that looks like a completed commercial query when in fact the response was never delivered. The failure was isolated to the Commercial Agent's execution, but its effects leaked into the shared state surface.
The goal of failure isolation design is to ensure that one agent's failure leaves the shared state in a condition that is either clearly incomplete or reset to a safe default.

## Analysing the Vela canvas
> 🔥 Before you start, make a copy of this template. It mirrors the structure of this lesson — one tab for the three Vela scenarios with their four analysis questions, one tab for your project's per-state-key application, and a short deliverable summary.
Work through the three failure scenarios below. For each one, answer the four questions that follow.
### Scenario A: The Classifier fails to return a structured output.
- The LLM node runs but the model's response does not match the structured output schema. query_type stays at unclassified, confidence stays at high (its default), and client_query stays empty.
### Scenario B: The Condition node routes correctly, but the specialist agent fails mid-execution.
- The Classifier has written query_type: "commercial", confidence: "high", and client_query with the original message. The Condition node routes to the Commercial Agent. The Commercial Agent begins executing but fails before producing a response; the Direct Reply node never fires.
### Scenario C: The Hybrid Handler produces a response that partially overwrites Flow State.
- The Condition node routed to the Hybrid Handler. The Hybrid Handler runs and, due to a misconfiguration in its llmUpdateState settings, overwrites query_type with a value the Condition node did not expect. For example, "escalate". A second query arrives in the same session. The Classifier runs, but before it writes to query_type, the Condition node reads the stale "escalate" value from the previous turn.

For each scenario, answer:
1. Which state keys are affected? List every key in $flow.state that holds an incorrect, stale, or misleading value after the failure.
1. Is the failure detectable from Flow State alone? Could an external system or a downstream agent reading $flow.state tell that something went wrong or does the state look like a successful run?
1. What is the safe state after recovery? What should each affected key hold after the system recovers? Write the target value for each key.
1. What design change would prevent or contain the failure? Propose one specific change to the canvas (a new Flow State key, a different default value, a constraint on which nodes can write to a key, or an additional Condition branch) that would address the failure mode.
There is no single correct answer for every scenario. The right design depends on what the system needs to do. The exercise is in identifying the affected state, reasoning through detectability, and proposing a targeted intervention.

## Applying this to your project
Extend the memory and state architecture document you have been building in the earlier lessons of this sprint. Add a final section: State recovery and failure isolation.
For each state key in your project agent's Flow State, work through these steps:
1. Step 1: Identify the failure mode. What happens to this key if the agent that writes it fails before completing? Does it stay at its default? Does it hold a partial value? Does it hold a value from a previous turn?
1. Step 2: Assess detectability. If a downstream agent or external system reads this key after the failure, will it be able to tell that the failure occurred? A key holding its default value is ambiguous — it could mean the run hasn't started yet, or it could mean the writing agent failed. A key holding an unexpected value is detectable. A key holding a plausible but wrong value is the most dangerous — it looks correct but isn't.
1. Step 3: Define the safe state. For each key, write the target value it should hold after a failed run that the system has recovered from. This is your recovery specification. The state the system should reach before it is safe to process the next input.
1. Step 4: Propose an isolation boundary. Identify which agents are allowed to write to each key. An agent that should only read a key but accidentally writes to it (overwriting a value set by a different agent) is a failure isolation violation. For each key, state the designated writer and what, if anything, should happen if a non-designated agent attempts to write to it.
The output of these four steps completes the state recovery and failure isolation section of the Sprint 3 project deliverable.

>  
  ### 🔥 Using AI when you get stuck
  If you are unsure whether a specific failure scenario is detectable from Flow State alone, describe the scenario precisely to AI:
  - Name the agent that failed and at what point in its execution it failed.
  - List the Flow State keys and the values they hold after the failure.
  - Ask whether a downstream agent reading those values would be able to distinguish the failed state from a successful one.
  For example: "In a Flowise multi-agent system, the Classifier runs and writes query_type: 'commercial' to Flow State. The Commercial Agent then fails before producing a response. A second query arrives in the same session. Is the state left by the failed run detectable from Flow State alone?"
  Use the response to pressure-test your detectability assessment. The final isolation boundary decisions depend on your project's specific canvas. Make them yourself.

## Watch out for
- Treating default values as safe recovery states. 

A key that returns to its default value after a failure looks clean, but the default is also the value the key holds at the start of every session, before any agent has run. An external system or a downstream agent reading the default cannot tell whether the run failed or simply hasn't started yet. If detectability matters for your system, the recovery state needs to be different from the initial state. For example, a dedicated "failed" or "recovery_needed" value rather than the original default.

- Assuming one agent's failure is always isolated. 

In a canvas where multiple agents share the same Flow State keys, a failure in one agent that leaves a stale value in a shared key is not isolated. It affects every agent that reads that key in the same session. Isolation requires either that the failing agent resets the key to a safe value before failing, or that downstream agents check the key's validity before using it.

- Conflating recovery with retry. 

Retrying a failed agent run is not the same as recovering state. If the Classifier fails and the system retries the Classifier, the retry may succeed and overwrite the stale values, but between the failure and the successful retry, the state was in a misleading condition. Recovery design addresses that window, not just the eventual successful outcome.

## Summary
State recovery and failure isolation are the final layer of the memory and state architecture for any multi-agent system. Recovery defines what the system should look like after a failure, which keys hold what values, and whether the state is safely ready for the next input. Isolation defines which agents can corrupt shared state when they fail, and how to contain that corruption so it does not propagate.
The Vela canvas has one explicit recovery mechanism (the unclassified fallback branch) and several failure modes that are currently unaddressed. Your project agent has its own version of both. The section you produced in this lesson (failure modes, detectability, safe states, and isolation boundaries) is the final piece of the Sprint 3 project deliverable. The last lesson of the sprint assembles all four sections into the complete memory and state architecture specification.