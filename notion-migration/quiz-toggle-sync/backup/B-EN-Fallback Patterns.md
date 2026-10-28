# Fallback Patterns

Notion page: https://app.notion.com/p/Fallback-Patterns-3889418319f3808caad4ec60e4ed53ce
Backed up before n8n migration

Timeouts stop the workflow from waiting forever. Retries give it a second chance. But some failures aren't temporary and won't recover on retry — the warranty database is down for maintenance, or a customer's query genuinely cannot be answered by any single specialist. What should the workflow do then? Just fail? Sofia knows that means a customer waits, an agent looks broken, and Lena has to intervene manually. This lesson is about the third resilience pattern: the fallback — an alternative path the workflow takes when the preferred path cannot complete.

## What is a fallback?
A fallback is an alternative path used when the preferred path cannot complete the task reliably.
In an agent workflow, the main path is usually the best option: the most capable model, the most accurate tool, or the most complete process. But if that path fails, the workflow should not always collapse. A fallback gives the system another safe option.
For example, Cascadia's Order Lookup Agent may first try to query the live order database through a connected tool. If that tool is rate-limited or unavailable, the workflow could switch to a fallback path, such as returning the last cached order status with a note that the data may be a few minutes stale.
The fallback does not pretend that nothing failed. It gives the best safe response available under the current conditions.

## Timeout, retry, and fallback
These three patterns are related, but they solve different problems.
[TABLE]
  | Pattern | Main question | What it does |
  | Timeout | “How long should we wait?” | Stops a step that takes too long. |
  | Retry | “Should we try the same path again?” | Repeats the same action when the failure may be temporary. |
  | Fallback | “What should we do instead?” | Switches to an alternative path when the main path is not reliable. |
A timeout protects the workflow from waiting forever. A retry gives the same path another chance. A fallback changes the strategy.

## Why fallback matters
Without fallback logic, a workflow often has only two outcomes: success or failure. That is too fragile for real systems.
A fallback pattern creates a middle option. The system may not complete the ideal path, but it can still respond usefully, safely, and transparently.
For example:
> 💡 Cascadia's Warranty Agent tries to reach the warranty records service. The request fails because the service is unavailable. The workflow retries twice. The service still fails. Instead of looping forever or returning a confusing error, the workflow moves to a fallback path — sending an acknowledgement to the customer that a specialist will follow up manually within one business day.
This makes the experience better for the user and safer for the system.
![image]((notion-hosted file))
## Common fallback options
A fallback can take different forms depending on the task.
One option is a simpler model path. If the main agent uses a tool and the tool fails, the workflow may route to a model-only answer with a clear limitation.
Another option is a different tool. If one search tool is unavailable, the workflow may try another source.
A third option is a user-facing recovery message. If the system cannot continue safely, it should explain what happened and what the user can do next.
The key is that the fallback should be intentional. It should not hide the failure or invent results.
![image]((notion-hosted file))

## Combining retries and fallbacks in n8n
In n8n, retries and fallbacks can work together without a separate loop node.
For an HTTP Request, open Settings → Retry On Fail, choose a limited number of attempts and set a wait between attempts. Set On Error → Continue (using error output) so an execution error that remains after the retries can follow a separate error branch. Connect that branch to an Edit Fields node containing an honest fallback response.
![image]((notion-hosted file))
For example, if Cascadia's warranty records service remains unavailable after three total attempts, return an acknowledgement rather than inventing warranty information. Retry settings handle node execution failures; valid but incomplete data needs a separate validation check.
This lets temporary failures recover without endless retries, while persistent failures receive a controlled response.

## Quick decision rule
Use a timeout when the system is waiting too long.
Use a retry when the same path might work if attempted again.
Use a fallback when the same path has failed enough times or is not safe to trust.
A resilient workflow often uses all three together: timeout to limit waiting, retry to handle temporary issues, and fallback to recover when the main path cannot complete the job.

## Quiz
### Question 1
> 💡 An agent calls a tool, but the tool takes too long to respond. Which pattern directly handles this situation?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/89f28fc9-f312-41c4-af58-3b508e2625e8

### Question 2
> 💡 An archive search tool returns a rate-limit error. The workflow sends the same request again after a short wait. Which pattern is being used?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d0145db7-852d-4e5e-81cd-dfb10509aa6d

### Question 3
> 💡 A workflow retries a failed tool call three times. After the third failure, it switches to a simpler response that explains the limitation to the user. Which pattern is this final switch?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/0e422a4e-62e5-4f51-a2ce-8e72f400166e


### Question 4
> 💡 Why should a fallback response be transparent?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/ce6c95bb-7fde-4981-ab53-c4d888f49df8

### Question 5
> 💡 Which workflow design is the most resilient?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4d2ceb4c-fa09-41fb-adf1-db0e4d9b7ec4

## Summary
Fallback patterns help agent workflows recover when the preferred path cannot complete the task. A timeout controls waiting, a retry gives the same path another chance, and a fallback changes the path when continuing the same way is no longer useful. Together, these patterns make orchestrated systems more reliable, safer, and easier for users to trust.