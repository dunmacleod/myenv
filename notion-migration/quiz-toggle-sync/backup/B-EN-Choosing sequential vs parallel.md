# Choosing sequential vs parallel

Notion page: https://app.notion.com/p/Choosing-sequential-vs-parallel-3819418319f3802d8271eacd5942c34f
Backed up before n8n migration

Sofia now knows both patterns — sequential when each step depends on the one before, parallel when independent agents can work at the same time. But real Cascadia requests do not label themselves. A support message about a delayed shipment might work better sequentially (verify order → check shipping → generate reply) or in parallel (check shipping AND check warranty AND check account status, all at once, then merge). Which pattern to choose is one of the highest-leverage decisions in a multi-agent design, and getting it wrong costs latency or coordination overhead that never had to exist.
The key question is simple:
> Can the next task start before the previous task finishes?
If the answer is no, use sequential orchestration.
If the answer is yes, parallel orchestration may be a better choice.

## Two different ways of organizing work
### Sequential orchestration
In a sequential workflow, each agent depends on the output of the previous one. Work moves step by step through the system.
![image]((notion-hosted file))
The recommendation agent cannot start until the risk assessment is complete. Every step builds on the previous step.

### Parallel orchestration
In a parallel workflow, multiple agents receive the same input and work independently at the same time.
Example:
![image]((notion-hosted file))
Each specialist agent works simultaneously. The results are merged once all agents finish.

## How to decide
A useful rule is to look for dependencies.
[COLUMN_LIST]
  [COLUMN]
    Use sequential orchestration when:
    - One agent needs information produced by another agent.
    - The workflow follows a clear decision path.
    - Later steps depend on earlier validation.
    - Accuracy is more important than speed.
  [COLUMN]
    Use parallel orchestration when:
    - Agents can work independently.
    - Multiple perspectives are needed.
    - Speed is important.
    - Results can be combined later.
    
## Comparing the trade-offs
[TABLE]
  | Factor | Sequential | Parallel |
  | Speed | Slower | Faster |
  | Coordination complexity | Lower | Higher |
  | Dependency handling | Excellent | Limited |
  | Resource usage | Lower | Higher |
  | Best for | Dependent tasks | Independent tasks |
>  Notice that parallel orchestration is not automatically better because it is faster. If agents depend on each other's outputs, parallel execution may produce incomplete or incorrect results.

## Check for Understanding
### Question 1
>  A Cascadia customer submits a ticket saying:
  > "My payment was charged twice and my order never arrived."
  Which orchestration pattern would you choose to investigate?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cb8c1b5d-5c7c-47a6-b543-00abc92def71

## Real-world example
Consider an e-commerce company handling product returns.
A sequential design might work like this:
![image]((notion-hosted file))
Each step depends on the previous result.
A parallel design might work like this:
![image]((notion-hosted file))
## Summary
Choosing between sequential and parallel orchestration is less about technology and more about dependencies. Sequential orchestration works best when each step requires information from the previous step. Parallel orchestration works best when multiple agents can investigate different aspects of a problem independently.
The most effective multi-agent systems often combine both approaches: parallel branches handle independent work, while sequential stages coordinate decisions and assemble the final result. This ability to match the orchestration pattern to the business problem is a key part of designing reliable agent systems.