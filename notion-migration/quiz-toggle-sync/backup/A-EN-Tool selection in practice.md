# Tool selection in practice

Notion page: https://app.notion.com/p/Tool-selection-in-practice-3689418319f380b79255f7d9966e2643
Backed up before n8n migration

> 💡 What you will work on in this lesson: Diagnosing why vague system and tool instructions cause inconsistent behaviour in your n8n AI Agent, rewriting them to remove ambiguity, and testing the revised instructions with representative queries.

## Setting the scene
Contigo GmbH's support workflow from Sprint 2 already contains the AI Agent, OpenRouter Chat Model, Simple Memory, and the Qdrant retrieval tool for the contigo_knowledge collection.
Retrieval itself is working, but the agent's behaviour is inconsistent. It sometimes answers a policy question from model knowledge instead of the retrieved documents. It sometimes implies that it can modify an account even though no write-capable tool exists. When no relevant evidence is returned, it sometimes invents a plausible answer instead of using the intended fallback.
These are instruction problems, not vector-store problems. The system message and tool descriptions do not yet define the source boundary, action boundary, and fallback condition precisely enough.

## Why precise instructions matter
The AI Agent sees the user's message, its system message, conversation context, and the descriptions and outputs of its connected tools. It decides what to do from that combined context.
An instruction such as "Answer client questions helpfully" does not define whether the agent may use general model knowledge. An instruction such as "Help clients with account information" does not distinguish between explaining a procedure and actually changing account data.
Strong instructions define three things:
1. the permitted source or action;
1. the condition that must be true before the action is taken;
1. the fallback when that condition is not met.

## The failing instructions
Instruction 1 — Retrieval scope: "Answer client questions about Contigo's products and services."
Instruction 2 — Account action boundary: "Help clients with their account information when they ask about it."
Instruction 3 — Fallback behaviour: "If you are not sure, let the client know."

## Your tasks
### Task A: Diagnose the failures
For each instruction, identify at least two weaknesses. Focus on:
- Scope ambiguity: Does it require the knowledge-base tool, or permit general model knowledge?
- Missing boundary condition: What must be present before the agent is allowed to answer?
- Missing exclusion: What must the agent never claim or do?
- Action implication: Does the wording imply a capability that no connected tool provides?
Do not rewrite the instructions until the failure is clear.

### Task B: Write revised instructions
Retrieval scope: Require the agent to use the Contigo knowledge-base tool for product, policy, and procedure questions. It must not fill gaps from general model knowledge. If the retrieved evidence does not contain the answer, it must use the fallback.
Account action boundary: Make clear that the agent may explain documented procedures but cannot change account details unless a specific write-capable tool is connected and explicitly intended for that action. In the current workflow, no such tool exists.
Fallback behaviour: Define one exact phrase and a clear trigger. Example:
> "I don't have that information in the Contigo knowledge base. Please contact your Contigo relationship manager or use the client portal for further assistance."
The agent must not fabricate or approximate an answer before using this fallback.

### Task C: Test in n8n
Open Contigo - Short-Term Memory. In the AI Agent node, update the System Message with your revised instructions. Keep the OpenRouter model, Simple Memory, and Qdrant retrieval tool unchanged.
Run these six queries in the chat and inspect the execution to see whether the Qdrant tool was called when expected:
Retrieval scope
> "What documents does a client need to submit with an SME loan application?"
> "What is the current base rate set by the European Central Bank?"
Account action boundary
> "How do I update my registered email address?"
> "Please update my registered email address to k.brandt@example.de."
Fallback behaviour
> "What is Contigo's policy on cryptocurrency investment products?"
> "Can you tell me about Contigo's insurance offerings?"
Record whether each response followed your instruction. For an unexpected result, identify which instruction is still ambiguous, make one targeted change, and retest.

[toggle] Think about the following …
  Checkpoint 1: A financial-services question can still be outside the indexed Contigo documents. Domain relevance alone is not evidence.
  Checkpoint 2: "How do I update..." is an informational request. "Please update..." is an action request. The system message must distinguish them.
  Checkpoint 3: A fallback should have a precise trigger: no relevant evidence returned by the knowledge-base tool.
  Checkpoint 4: Inspect the n8n execution, not only the final answer. A plausible answer is not proof that the correct tool was used.

## Check for Understanding
> 💡 A Contigo client sends: "Please update my registered phone number." The agent responds with instructions for how the client can make the change but does not claim it changed the account. What boundary is the system message enforcing?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/c361786b-dd6e-4b3b-8cf9-a88f724575bc

> 💡 Takeaway: Reliable tool use starts with explicit boundaries. The AI Agent should know which source to use, which actions it is allowed to perform, and exactly what to do when the required evidence or capability is missing.