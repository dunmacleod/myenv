# Orchestration vs choreography

Notion page: https://app.notion.com/p/Orchestration-vs-choreography-37e9418319f3808e98b2c397997b2367
Backed up before n8n migration

Cascadia's support flow now has multiple agents — an Intake Agent that classifies incoming messages, a Warranty Agent, and a Returns Agent — and Sofia needs to decide how they talk to each other. She has two very different design choices in front of her. In one, a coordinator sits above the specialists and decides who does what. In the other, the specialists talk to each other directly, without a coordinator in the middle.
There are two common answers. One approach uses a central coordinator that decides how work moves through the system. The other lets agents interact directly and adjust on the fly. These two styles are called orchestration and choreography, and the choice between them shapes how the whole workflow behaves.

## Orchestration: one agent coordinates the work
In an orchestrated system, a central agent acts as a coordinator. It receives the request, decides which agent should perform each task, collects the results, and determines the next step.
Think of an orchestra. The musicians play different instruments, but the conductor decides when each section should start, stop, or change tempo. The musicians focus on their own work while the conductor manages the overall performance.
In a multi-agent system, the orchestrator plays the same role. Individual agents remain specialized, but a central coordinator controls the workflow.

### Typical orchestration flow
1. A user sends a request.
1. The orchestrator receives it.
1. The orchestrator assigns work to one or more agents.
1. Agents return their results.
1. The orchestrator combines the outputs and delivers the final response.
![image]((notion-hosted file))

## Choreography: agents coordinate directly
In a choreographed multi-agent system, there is no central coordinator responsible for managing the workflow. Instead, each agent understands its own role and communicates directly with other agents when additional information or capabilities are needed. When a request enters the system, one agent begins processing it and decides which other agents should be involved. Those agents exchange information with one another, contribute their specialized expertise, and continue collaborating until the task is completed. The final result emerges from the collective work of the agents rather than being assembled by a central controller.
This approach can be highly flexible because agents can interact dynamically based on the needs of the task. It also avoids creating a single coordination bottleneck, which can improve scalability in larger systems. However, because decisions and communication are distributed across multiple agents, choreographed systems can be more difficult to monitor, debug, and understand than orchestrated systems.

### Typical choreography flow
1. A user request enters the system.
1. An agent begins processing it.
1. That agent contacts other agents when needed.
1. Agents exchange information directly.
1. The final result emerges from their collaboration.
![image]((notion-hosted file))
## Comparing the two approaches
[COLUMN_LIST]
  [COLUMN]
    ### Orchestration
    - One central coordinator
    - Workflow is explicitly controlled
    - Easier to monitor and debug
    - Simpler for predictable processes
    - Single point of control
    
  [COLUMN]
    ### Choreography
    - No central coordinator
    - Workflow emerges from interactions
    - More flexible and decentralized
    - Better for dynamic environments
    - No single point of failure
## Check for Understanding
### Question 1
>  A Cascadia workflow has three agents:
  - A Research Agent gathers information.
  - A Compliance Agent checks regulations.
  - A Report Agent creates the final document.
  A fourth agent receives every request, decides which of the three should work on it, collects the outputs, and returns the final answer. Which coordination style is this?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4a8701e1-fd76-4356-b7a3-5734f538567e

## Summary
Orchestration and choreography solve the same coordination problem in different ways. Orchestration puts a coordinator in the middle — predictable, easier to reason about, easier to debug — at the cost of a central point of complexity. Choreography lets agents interact directly — more flexible and resilient — at the cost of visibility into how the system behaves. For Cascadia's support flow, Sofia will start with orchestration in the next lessons; it is the pattern that fits when the specialists are known ahead of time and a coordinator can be trusted to route them.
