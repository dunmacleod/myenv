# Timeout Patterns

Notion page: https://app.notion.com/p/Timeout-Patterns-3889418319f380548779f668dd242f1e
Backed up before n8n migration

A week into Cascadia's soft launch, Emil brings Sofia a specific complaint from Lena: some customer messages just hang. No error message, no failure notification — the workflow starts, an agent goes off to look something up, and nothing ever comes back. Sofia opens the logs and sees the same pattern each time: one component was waiting for another that never responded, and the whole workflow got stuck on that wait. Timeouts are how orchestrated systems refuse to wait forever. This lesson explains why waits happen, why leaving them uncapped is dangerous, and how timeouts protect the whole workflow when one component slows down.

## What a timeout means
A timeout is the maximum amount of time one system component is willing to wait for another component to respond.
For example, imagine a Flowise agent deployed behind a cloud proxy. The user sends a request, the proxy forwards it to Flowise, and Flowise starts generating a response. If the proxy has a 30-second timeout, it will stop waiting after 30 seconds.
That does not always mean Flowise crashed. It may mean the response simply took too long.
The failure happens because the proxy, the backend service, the agent, and the user-facing interface do not all share the same expectation about response time.

## Why timeouts matter in agent workflows
Agent workflows can take longer than normal web requests because they may involve several steps.
An agent might need to classify the request, call a tool, wait for an external system, retrieve context, generate a response, or pass work to another agent. Each step adds time.
In a simple app, 30 seconds may be enough. In an agent workflow, 30 seconds can be too short, especially when the workflow includes long model responses, tool calls, retrieval, or multi-agent handoffs.
This creates a common resilience problem:
The workflow is still doing useful work, but the infrastructure gives up too early.

## Common causes of timeouts
Timeouts often happen because:
- An agent is processing a large task.
- A tool or API responds slowly.
- A service is temporarily unavailable.
- A message is lost and never reaches its destination.
The timeout itself is not the root cause. It is a signal that something took longer than expected.

### What happens after a timeout?
Different systems handle timeouts differently.
A workflow might:
- Retry the task.
- Send the task to another agent.
- Use a fallback response.
- Escalate to a human.
- Stop the workflow and report an error.
The right choice depends on the business situation. A customer support chatbot might retry.
A fraud detection workflow might escalate immediately.

### Example
An orchestrator sends a task to an agent.
Expected behavior
![image]((notion-hosted file))
Timeout behavior
![image]((notion-hosted file))
> ☝ The important point is that the agent may not have failed. The orchestrator simply reached the maximum waiting time.

## Summary
Timeouts are one of the most common failure points in orchestrated systems. They happen when one part of the system stops waiting before another part finishes working.
Good timeout handling is not only about increasing a number. It is about understanding how long the workflow should reasonably take, where the timeout is enforced, and what should happen when work takes longer than expected.