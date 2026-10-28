# Handling tool failure and infinite loops

Notion page: https://app.notion.com/p/Handling-tool-failure-and-infinite-loops-3689418319f380038bfafc2b9a1b9791
Backed up before n8n migration

> 💡 What you will work on in this lesson: Designing safeguards that stop repeated tool calls after failure and defining a client-safe fallback before additional tools are connected to the Contigo agent.

## Setting the scene
A tool-enabled agent can fail in a new way: the model may keep trying a tool because the requested task is still unresolved.
Imagine the loan-status service is unavailable. The agent calls it, receives an error, reasons that it still needs the status, and calls it again. Without a limit, the workflow can waste tokens and time while the client receives no useful answer.
A production design therefore needs two layers:
1. a deterministic iteration cap in the AI Agent;
1. a clear instruction for how to respond when a tool cannot provide a usable result.

## Layer 1: Max Iterations
The n8n AI Agent has a Max Iterations option. It limits how many reasoning/tool-use cycles the model may run for one request.
For this Contigo exercise, set:
Options → Max Iterations = 4
Four iterations leave enough room for the simple multi-tool scenarios in this sprint while preventing long retry loops. The exact production value is a design decision, but it should always be intentional rather than unlimited.
> ➡️ Important: Max Iterations is a circuit breaker, not a complete error-handling strategy. It stops the loop; the system message still needs to define what the client should hear when a tool is unavailable.

## Layer 2: Structured tool failure
When you control a tool workflow, prefer a structured failure result that the agent can interpret, for example:
```json
{
  "success": false,
  "error": "service_unavailable"
}
```
Do not ask the model to infer success from an empty or malformed response. A clear success flag makes the failure state observable and testable.
The loan-status sub-workflow you build in the next lesson will include a simulated failure case so you can verify the agent's behaviour safely.

## Your tasks
### Task A: Configure the circuit breaker
Open the AI Agent in your Contigo workflow and add Max Iterations = 4 under its options.
Write two sentences explaining why this value is reasonable for the current architecture. Your explanation should consider that most requests require zero or one tool call, while a small number may combine retrieval with one additional tool.

### Task B: Write the failure instruction
Add a short instruction to the system message that covers both an unavailable tool result and an exhausted reasoning loop.
A strong version should communicate all three requirements:
- No fabrication: Never invent a loan status or pretend the tool succeeded.
- No technical leakage: Do not expose internal errors, node names, stack traces, or implementation details.
- Clear next step: Tell the client what to do instead.
Example:
> "If a required tool is unavailable or does not return a usable result, do not guess or claim that the action succeeded. Tell the client: 'I’m unable to retrieve that information right now. Please try again later or contact your Contigo relationship manager for assistance.'"

### Task C: Define the observable failure contract
Before you build the loan-status tool, define its expected outputs:
[TABLE]
  | Condition | Expected result |
  | Status found | success = true plus application reference, status, detail, and next action |
  | Reference unknown | success = false, error = not_found |
  | Service unavailable | success = false, error = service_unavailable |
This contract makes the later tests deterministic.

## Check for Understanding
> 💡 A status tool keeps returning an unavailable result and the agent repeatedly calls it. Which safeguard should stop the reasoning loop even if the model keeps trying?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e820b00b-4cf0-4abe-8c70-96b6bf6aafc0

> 💡 Takeaway: Reliable tool use needs both model instructions and deterministic execution limits. Max Iterations bounds the loop; structured tool results and a precise failure instruction determine what happens next.