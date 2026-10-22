# Adding resilience to the project orchestration

Notion page: https://app.notion.com/p/Adding-resilience-to-the-project-orchestration-3899418319f380f1b97dfcf6b3a1cea0
Backed up before n8n migration

You have now seen the four core resilience patterns — timeouts, retries, fallbacks, and circuit breakers — and how each addresses a different class of failure. In this lesson you apply what you learned to your own project agent. A project orchestration should not assume that every agent, tool, or MCP call will succeed on the first attempt; this lesson is where you decide what your workflow does when they don't.

## Your task
Open your project orchestration and extend it with:
1. At least one timeout rule
1. At least one retry rule
1. At least one fallback path
You do not need to make the workflow perfect. The goal is to make the main risk points visible and show how the orchestration should behave when something goes wrong.

## Step 1: Identify risky nodes
Look at your current project flow and mark the steps most likely to fail.
Good candidates are:
- agent nodes that call an LLM
- tool calls through MCP
- external API calls
- search or retrieval steps
- parsing or formatting steps
- routing decisions based on structured output
For each risky step, write down:
[TABLE]
  | Workflow step | What could go wrong? | User impact |
  |  Knowledge retrieval tool | Tool does not respond | User gets no answer |
  | Specialist agent | Invalid JSON output | Workflow cannot route correctly |
  |  Report generator | Takes too long | User waits without feedback |

## Step 2: Add timeout behavior
A timeout means the workflow stops waiting after a defined time limit.
Choose one risky step and define:
[TABLE]
  | Question | Your answer |
  | Which node gets a timeout? |  |
  | How long should the workflow wait? |  |
  | What happens after the timeout? |  |
  | Does the user see a message? |  |
Example:
> If the knowledge retrieval tool does not respond within 30 seconds, stop waiting and move to the fallback path.

## Step 3: Add retry behavior
A retry means the workflow tries the same step again after a failure.
Choose one step where retrying makes sense. Do not retry everything.
Define:
[TABLE]
  | Retry rule | Your design |
  | Trigger | Timeout, parsing error, empty response, tool error |
  | Maximum attempts | 2 or 3 |
  | What changes on retry? | Same request, simplified prompt, smaller query, different model |
  | Stop condition | Success or max attempts reached |
Example:
> If the specialist agent returns invalid JSON, retry up to 2 times with a stricter formatting instruction. If it still fails, move to fallback.

## Step 4: Add one fallback path
A fallback is the safe path used when the normal path cannot continue.
Choose one fallback type:
[TABLE]
  | Fallback type | When to use it |
  | Direct user message | The system cannot complete the task safely |
  | Simpler agent response | The advanced step failed, but a basic answer is possible |
  | Human escalation | The issue needs review |
  | Alternative tool | The first tool is unavailable |
  | Cached/static response | The system has a safe default answer |
Example fallback message:
> I could not complete the full automated check because the retrieval tool did not respond. I can still summarize what I know from the current conversation, or you can try again later.

## Step 5: Update your orchestration diagram
Add resilience elements directly to your diagram.
Your diagram should show:
- the normal successful path
- where the timeout is applied
- where retries happen
- when the workflow stops retrying
- where the fallback path goes
![image]((notion-hosted file))
## Checkpoint questions
Before submitting, check:
1. Did you add resilience to a real risk point, not just a random node?
1. Is the retry limit clear?
1. Does the fallback path protect the user from a broken or endless workflow?
1. Can someone else understand your design from the diagram?
1. Did you explain what happens when retries are exhausted?

## Summary
You moved your project from a “happy path” workflow to a more realistic orchestration design. The system now has a plan for slow responses, repeated failures, and unsafe continuation. That is an important step toward building agents that can fail gracefully instead of failing silently.
