# Designing a parallel workflow

Notion page: https://app.notion.com/p/Designing-a-parallel-workflow-3819418319f3803da27fc9ed9966bff1
Backed up before n8n migration

Not every request Cascadia's support system receives has a natural sequence. When a customer submits a message that touches multiple domains at once — a delayed shipment with a warranty question about the delayed product — Sofia does not want the workflow to check shipping first, then wait, then check warranty. Both checks can run at the same time, and their results can be combined into one response at the end. This is what parallel orchestration is for: independent agents working simultaneously on different angles of the same request, then merging their findings.

## Parallel orchestration in a nutshell
A parallel workflow sends the same request, or different parts of a request, to multiple agents at once and then combines their outputs into one final result.
In a sequential workflow, each step depends on the previous step. Agent B waits for Agent A. Agent C waits for Agent B. This is useful when the task has a clear chain of dependency.
In a parallel workflow, the agents do not wait for each other during their main work. Each agent receives its assignment, completes it independently, and returns a result. A final coordination step then compares, combines, or prioritizes those results.
For example, imagine a customer asks:
> “We are thinking about automating our reporting process. What should we consider?”
A parallel workflow could send this request to three agents at the same time. One agent checks business value, another checks data readiness, and another checks implementation risks. None of these agents needs to wait for the others before starting. After they respond, a final agent combines their perspectives into one balanced answer.
![image]((notion-hosted file))

## Why parallel workflows are useful
Parallel orchestration is useful when a task has several independent angles. Instead of asking one agent to think about everything, you assign different responsibilities to different agents.
This can improve speed, because several agents work at the same time. It can also improve quality, because each agent focuses on one type of reasoning. A risk agent can look for weak points, a business agent can focus on value, and a technical agent can focus on feasibility.
The key word is independent. Parallel orchestration works best when each agent can do meaningful work without needing another agent’s output first.

## A simple structure for parallel workflows
A parallel workflow usually has four parts.
First, there is an input. This is the original request, problem, or document that needs to be processed.
Second, there is a splitter. The splitter decides which agents should receive which part of the work. Sometimes every agent receives the same full input. Sometimes each agent receives a specific subtask.
Third, there are parallel agents. These agents work at the same time, each with a clearly defined role.
Fourth, there is a merge step. This step brings the outputs together. The merge step may summarize, compare, rank, resolve conflicts, or create a final answer.
The merge step is what makes parallel orchestration reliable. Without it, you only have several separate answers.

## Example: parallel workflow for a business automation request
Imagine the user asks:
> “Can we use an AI agent to reduce manual work in our monthly reporting process?”
A parallel workflow could be designed like this.
The Business Value Agent checks whether the automation solves a real problem. It looks for time savings, repeated manual effort, and possible business impact.
The Data Readiness Agent checks whether the required data is available, structured, and reliable enough for automation.
The Risk Agent checks what could go wrong. It considers hallucination risk, missing approvals, unclear ownership, and sensitive data.
The Final Response Agent receives all three outputs and creates one recommendation. It does not simply paste the answers together. It decides what matters most and produces a clear conclusion.

## What should run in parallel?
A good parallel task has three qualities.
The agents can work independently. One agent does not need another agent’s result before starting.
The outputs are complementary. Each agent adds a different perspective, rather than repeating the same work.
The results can be merged. There is a clear way to combine the outputs into a final decision, summary, or recommendation.
If these three qualities are missing, parallel orchestration may create more confusion than value.

## What should not run in parallel?
Do not use parallel orchestration when the task has strong dependencies.
For example, if one agent must first extract customer requirements and another agent must then build a solution based on those requirements, this is not a good parallel flow. The second agent needs the first agent’s output. That is sequential orchestration.
Parallel orchestration is also risky when agents are allowed to make overlapping decisions without a merge rule. If three agents each produce a different final recommendation and no agent is responsible for resolving the disagreement, the workflow becomes unreliable.

## The merge step
The merge step is the most important design choice in a parallel workflow.
A weak merge step says:
>  “Combine the outputs.”
A stronger merge step says:
>  “Compare the outputs from the business, data, and risk agents. Produce one recommendation. If the agents disagree, explain the disagreement and choose the safest recommendation.”
The merge step should define what to do with agreement, disagreement, missing information, and duplicated information. This is where the workflow becomes more than several agents running at the same time.

## Check for Understanding
### Question 1
>  A learner is designing a workflow for this request:
  > "Review this product idea and tell me whether it is worth building."
  Which design is the best fit for parallel orchestration?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/12a26e27-e752-4c53-aceb-79a0f4d52927

## Common design mistake
A common mistake is assuming that “more agents” means “better workflow.”
Parallel orchestration is not about adding agents for variety. It is about splitting work where the split creates value. If two agents are likely to produce the same answer, they probably should not both be in the workflow. If their outputs cannot be merged clearly, the workflow may become harder to debug.
A good parallel workflow feels like a well-organized team. Each person knows their role, works independently, and contributes to one shared result.

## Summary
Parallel orchestration is useful when a task can be divided into independent parts that benefit from different perspectives. The main design challenge is not only starting multiple agents at once, but also bringing their outputs back together in a reliable way.
You now have a practical mental model for designing parallel workflows: split only when the work is independent, give each agent a distinct role, and define the merge step before you run the workflow.