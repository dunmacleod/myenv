# Why orchestration patterns matter

Notion page: https://app.notion.com/p/Why-orchestration-patterns-matter-37f9418319f380439617d250939a99e6
Backed up before n8n migration

The orchestration pattern determines how work moves through the system, how decisions are made, and where failure points appear. Choosing the right pattern is one of the highest-leverage design decisions a system will encounter: it shapes latency, cost, debuggability, and the shape of every future extension.
Agent orchestration tools — including n8n and code-based frameworks such as LangGraph, CrewAI, and AutoGen — can implement variations of these patterns, though their node models and capabilities differ. This lesson covers six common patterns, when each fits, and where each starts to strain.
![image]((notion-hosted file))

## Chaining (Sequential)
Chaining is the simplest orchestration pattern. Work moves through a fixed sequence of agents or steps, with each step using the output of the previous one.
Example:
> In the given workflow, the requirements analysis step identifies the goals and constraints, the research step gathers relevant information, the draft generation step creates the initial content, and the review step checks for accuracy, quality, and alignment with the original requirements before final delivery.
![image]((notion-hosted file))
Each stage has a clear responsibility and passes its result to the next stage.
This pattern works well when tasks have a natural sequence and each step depends on the previous one.
[COLUMN_LIST]
  [COLUMN]
    ### Advantages
    >  
      - Easy to understand
      - Predictable execution path
      - Simple to debug
    
  [COLUMN]
    ### Limitations
    >  
      - Slow for large workflows
      - Every step must wait for the previous step to finish
      - A failure can stop the entire chain
    

## Parallel
In a parallel pattern, multiple agents work simultaneously on different parts of the problem.
Example:
> A travel-planning assistant may search for flights, hotels, and activities at the same time. Once all results are available, they are combined into a single itinerary.
![image]((notion-hosted file))
Because independent tasks run simultaneously, parallel workflows are often significantly faster than sequential workflows.
[COLUMN_LIST]
  [COLUMN]
    ### Advantages
    >  
      - Faster execution
      - Efficient use of specialized agents
      - Good for independent subtasks
  [COLUMN]
    ### Limitations
    >  
      - Requires a way to combine results
      - More complex than chaining
      - Higher resource usage

## Routing
Routing introduces a decision point into the workflow. A router examines the incoming request and chooses the most appropriate agent to handle it.
Example:
> A customer submits the question, "Why was I charged twice this month?" The router analyzes the request and determines that it is a billing-related issue, so the request is sent to the Billing Agent. If the question were about a product malfunction, it would be routed to the Technical Agent. General inquiries would be sent to the General Support Agent.
![image]((notion-hosted file))
The router evaluates the input and selects the most appropriate path. 
>  Unlike parallel execution, only one branch is chosen and executed.
Many customer-support systems, help desks, and AI assistants use routing to ensure requests are handled by the right expert.
[COLUMN_LIST]
  [COLUMN]
    ### Advantages
    >  
      - Efficient use of specialist agents
      - Easy to add new expertise areas
      - Reduces unnecessary work
  [COLUMN]
    ### Limitations
    >  
      - Routing mistakes affect the entire workflow
      - Router logic must be maintained carefully

## Iteration
Iteration allows an agent to improve its own work multiple times before producing a final result.
Instead of immediately generating an answer, the system evaluates its progress and performs another pass if improvements are needed.
Example:
> A research agent creates an initial plan for investigating a topic. It gathers information from available sources and then passes the findings to an evaluation agent. The evaluation agent checks whether the information is accurate, complete, and relevant. If gaps or quality issues are found, the workflow loops back to the research agent to collect additional information. This cycle continues until the evaluation criteria are met, after which a final report is produced.
![image]((notion-hosted file))
[COLUMN_LIST]
  [COLUMN]
    ### Advantages
    >  
      - Higher-quality outputs
      - Supports self-correction
      - Encourages deeper analysis
  [COLUMN]
    ### Limitations
    >  
      - Increased cost
      - Longer execution time
      - Requires evaluation criteria

## Looping
Looping is similar to iteration but focuses on repeatedly executing a workflow until a condition is satisfied.
Example:
> Suppose a research agent is trying to answer a question about a company's recent financial performance. It first generates a search query, retrieves relevant information, and evaluates whether the results provide enough evidence to answer the question. If the information is incomplete or unclear, the agent generates a refined query and repeats the process until it has gathered sufficient information.
![image]((notion-hosted file))
This pattern is frequently used in Retrieval-Augmented Generation (RAG) systems where information retrieval may need several attempts.
>  Unlike iteration, which typically repeats a process to progressively refine or improve an output, looping focuses on repeating a sequence of steps until a specific condition is met. In other words, iteration is often used for enhancement through multiple passes, while looping is driven by a stopping criterion such as finding sufficient information, achieving a target confidence level, or satisfying a validation check.
[COLUMN_LIST]
  [COLUMN]
    ### Advantages
    >  
      - Handles uncertainty well
      - Improves retrieval quality
      - Can recover from weak intermediate results
  [COLUMN]
    ### Limitations
    >  
      - Risk of excessive repetitions
      - Requires clear stopping conditions

## Hierarchy
Hierarchy introduces a supervisor that coordinates multiple worker agents.
Instead of all agents communicating directly, the supervisor decides who should work next, reviews outputs, and combines results.
Example:
> A customer support workflow receives a user question. First, an intent-classification agent determines whether the request is about billing, technical support, or account management. The output is then passed to a specialized agent for that category, which generates a response. Each step depends on the output of the previous step, forming a chain.
![image]((notion-hosted file))
The supervisor manages the workflow and ensures that the workers remain aligned with the overall goal.
This pattern is common in advanced multi-agent systems because it enables specialization while maintaining central coordination.
[COLUMN_LIST]
  [COLUMN]
    ### Advantages
    >  
      - Handles complex projects
      - Clear separation of responsibilities
      - Easier coordination of many agents
  [COLUMN]
    ### Limitations
    >  
      - More complex design
      - Additional communication overhead
      - Supervisor becomes a critical component

## Comparing the patterns
Different patterns solve different coordination problems.
[TABLE]
  | Pattern | Best for |
  | Chaining | Sequential tasks with clear dependencies |
  | Parallel | Independent tasks that can run simultaneously |
  | Routing | Directing requests to specialists |
  | Iteration | Improving quality through multiple passes |
  | Looping | Repeated retrieval or validation cycles |
  | Hierarchy | Large multi-agent systems with specialized roles |
There is no universally best pattern. The right choice depends on the task, the number of agents involved, and the level of coordination required.

## Check for Understanding
### Question 1
>  Cascadia is building a customer-support assistant. Billing questions should go to a billing specialist, technical questions should go to a technical specialist, and general questions should go to a general-support agent. Which orchestration pattern is the best fit?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f00be6ba-b870-455c-ba5a-79932aa14d9e

## Summary
Not all agent systems coordinate work the same way. Chaining, parallel, routing, iteration, looping, and hierarchy each solve different coordination problems. The pattern you choose shapes latency, cost, and debuggability long before model quality becomes the limiting factor.
In the next lessons, Sofia zooms into the three patterns most relevant to Cascadia's support workflow — sequential, parallel, and hierarchical — and works through when each earns its complexity.