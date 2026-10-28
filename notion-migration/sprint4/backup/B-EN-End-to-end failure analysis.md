# End-to-end failure analysis

Notion page: https://app.notion.com/p/End-to-end-failure-analysis-38b9418319f380b0a53cd100ab6dc356
Backed up before n8n migration

## Looking beyond individual failures
When an orchestrated system fails, the root cause is not always the component that appears to have stopped working.
Take your arXiv research assistant as an example:
1. A user submits a support request.
1. The Intake Agent classifies the request.
1. The Orchestrator sends it to the correct specialist.
1. The specialist queries a knowledge base through MCP.
1. The response is returned to the user.
If the user receives an incorrect answer, the specialist agent may not actually be at fault. The real issue could have happened much earlier:
- the Intake Agent classified the request incorrectly,
- the orchestrator routed it to the wrong specialist,
- the MCP server returned incomplete information,
- the knowledge base was outdated,
- or an earlier retry produced stale state that propagated through the workflow.
End-to-end failure analysis means examining the entire chain of execution to determine where the failure actually originated.
![image]((notion-hosted file))

## Where failures commonly occur
Instead of thinking about individual nodes, it helps to think about the different layers of the system.
[TABLE]
  | Layer | Example failure | Possible mitigation |
  | User input | Ambiguous or incomplete request | Clarification step before routing |
  | Agent reasoning | Incorrect classification or planning | Validation agent or confidence checks |
  | Orchestration | Wrong routing or skipped step | Routing rules and state validation |
  | Tool integration | MCP server unavailable or API timeout | Retries, fallbacks, circuit breakers |
  | External data | Missing or outdated information | Alternative data source or cached results |
  | Final response | Hallucinated or incomplete answer | Response validation before returning |
Notice that not every problem should be solved with retries. If an Intake Agent misunderstands the user's request, retrying the same classification several times is unlikely to improve the result. A clarification question is usually a better mitigation.

## Think in cause and effect
When debugging an orchestration, work backwards from the visible problem.
Suppose a customer receives pricing information instead of troubleshooting steps.
Rather than immediately changing the specialist agent, investigate questions like:
- Was the original request classified correctly?
- Was the correct specialist selected?
- Did the specialist receive the expected context?
- Did the MCP tool return the expected information?
- Did a fallback activate unexpectedly?
Following the execution path helps identify the first incorrect decision, which is usually the true source of the failure.

## Quiz
>  A workflow produces the following result:
  > The user asks how to reset their password, but receives billing instructions.
  Which component would you investigate first?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4f6e2a84-6afc-4ccf-a0f7-e284056c58b8

## Failure analysis checklist
When analysing an end-to-end workflow, ask yourself:
- Where did the first incorrect decision occur?
- Did every agent receive the expected inputs?
- Did every tool return valid outputs?
- Were retries or fallbacks triggered?
- Did any incorrect state propagate to later steps?
- Could the workflow recover automatically, or did it require manual intervention?
Following these questions systematically is much more effective than debugging individual nodes in isolation.

## Summary
A reliable multi-agent system depends on more than well-designed agents. Integration, orchestration, external tools, and recovery mechanisms all influence the final result. End-to-end failure analysis helps you trace a problem back to its original source so you can apply the right mitigation strategy instead of fixing the symptom. As your projects become larger, this systems-level view becomes one of the most valuable debugging skills you can develop.
