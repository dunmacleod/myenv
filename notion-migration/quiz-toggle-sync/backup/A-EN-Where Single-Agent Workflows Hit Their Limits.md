# Where Single-Agent Workflows Hit Their Limits

Notion page: https://app.notion.com/p/Where-Single-Agent-Workflows-Hit-Their-Limits-3689418319f380a09d7adb2e47c3849e
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: What happens when a single-agent workflow reaches the boundaries of what it can handle reliably, why those boundaries exist, and what the industry has built to address them without requiring you to build anything beyond your current workflow.

## What you have built
Contigo GmbH's support agent now holds multi-turn conversations, retrieves accurately from a knowledge base, invokes tools through a ReAct loop, and enforces grounding behaviour through a carefully designed system prompt. For the majority of Contigo's client support queries (product questions, compliance lookups, loan status checks, and account procedure explanations), this architecture is the correct and sufficient choice.
But the executive team has a more ambitious question. Could the same architecture handle a full corporate loan application assessment by simultaneously analysing the client's financial position, evaluating regulatory compliance under current EU law, assessing credit risk against Contigo's internal models, and drafting the client communication summarising all three outcomes?
The development team tries it. They connect four additional tools and expand the system prompt. The first tests reveal the problem immediately.

## Context dilution
A single agent processes every task through one context window. As the task grows in complexity, that context window fills with an increasing volume of tool outputs, retrieved chunks, intermediate reasoning steps, and conversation history. When the context becomes crowded, the model's ability to attend to earlier information degrades.
This is called context dilution which is the degradation of reasoning quality as the volume of information in the context window increases beyond the model's effective attention capacity.
For Contigo's complex application assessment, the agent begins confusing outputs from different analytical steps. It retrieves regulatory content when it should be running credit calculations. It generates the client summary before completing the compliance check. On complex multi-step applications, its error rate climbs significantly compared to simpler queries.
The context window has not reached its hard token limit. But the model's attention has been stretched across too many competing inputs simultaneously  and reasoning quality has degraded as a result.

## Tool bloat
The second failure mode is related. When a single agent is connected to many tools to handle diverse tasks, the tool descriptions themselves consume context window space. More critically, the model's routing accuracy decreases as the number of tools increases.
This is tool bloat: The degradation of tool selection accuracy as the number of connected tools grows beyond the model's reliable discrimination capacity.
You experienced a version of this in the previous lesson when three vague tool descriptions caused routing failures. Imagine the same problem across twelve tools with overlapping descriptions. The model's routing becomes unreliable not because the descriptions are poorly written but because there are simply too many similar options to discriminate between consistently.

## What multi-agent systems do differently
A multi-agent system distributes the cognitive load that overwhelms a single agent across multiple specialised models. Instead of one agent attempting to be a financial analyst, a regulatory expert, a risk assessor, and a communication writer simultaneously, the system assigns each role to a dedicated agent with its own focused system prompt, its own constrained toolset, and its own isolated context window.
Each specialised agent operates within a context window that contains only the information relevant to its specific role. The credit risk agent sees credit data and risk models. It does not see the regulatory compliance analysis or the draft client communication. Its context is smaller, more focused, and its reasoning is correspondingly more reliable.
Independent tasks can also be assigned to multiple agents simultaneously rather than sequentially. This reduces the total processing time for complex multi-step assessments. 
> ➡️ Multi-agent systems are not a single architecture. They are a family of patterns, each appropriate for a different class of problem. You do not need to understand how to build these; only that they exist and what problem each one solves.

## Where your workflow fits
The workflow you have built is not a stepping stone to something better. It is the correct architecture for Contigo's support use case. The conditions that justify multi-agent complexity (simultaneous deep expertise across multiple unrelated domains, parallel execution of independent analytical tasks, a tool registry too large for accurate single-agent routing) do not apply to a support agent handling loan product queries, compliance lookups, and account status checks within a single domain.
Understanding where the limits are is what makes you a more deliberate architect. The decision to stay with a single-agent workflow is a justified architectural choice.
![image]((notion-hosted file))

## Check for Understanding
> 💡 Contigo's development team adds eight additional tools to the support agent to extend its capabilities. Performance on complex multi-step queries degrades significantly. What is the most accurate explanation?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4e24ac71-3589-4c8d-9177-933f97aff0e1


> 💡 Takeaway: 
  Context dilution and tool bloat are the specific failure modes that mark the boundary of what a single-agent workflow can handle reliably. Understanding them is a reason to design it carefully. 
  The system prompt refinement you will do in the next lesson is the practical response to everything introduced here: keeping the context focused, the tool descriptions precise, and the agent's behaviour predictable within the scope it was designed for.
