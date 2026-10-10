# What A2A is and when it matters

Notion page: https://app.notion.com/p/What-A2A-is-and-when-it-matters-37e9418319f3802c989cea08cecef902
Backed up before n8n migration

Sofia's Order Lookup Agent can now reach Cascadia's tools via MCP. But when a customer's issue is a warranty claim, the answer isn't just a tool call — it needs judgement from a completely separate agent maintained by Cascadia's compliance team, on a different platform, with its own decision logic. That agent is not a tool; it is another agent.
When agents need to talk to other agents — not tools — MCP alone is not the right protocol. That is what Agent-to-Agent (A2A) is for. This lesson introduces A2A, distinguishes it from MCP, and explains when a system genuinely needs it.
## What is A2A?
Agent-to-Agent (A2A) is an emerging standard that allows independently deployed AI agents to communicate, coordinate, and delegate work to one another.
Instead of directly calling a tool or API, an agent can send a request to another agent that has its own capabilities, memory, goals, and decision-making process.
Think of A2A as a protocol for collaboration between agents.
For example:
- A customer support agent receives a request about a delayed shipment.
- The support agent contacts a logistics agent.
- The logistics agent retrieves shipment information and returns a response.
- The support agent combines that information and responds to the customer.
Each agent remains responsible for its own area of expertise, but they can work together to solve larger tasks.
![image]((notion-hosted file))
## MCP vs A2A
A common source of confusion is that both MCP and A2A involve communication beyond a single agent.
However, they solve different problems.
[COLUMN_LIST]
  [COLUMN]
    MCP
    - Connects an agent to tools, data, or services
    - Focuses on tool access
    - The receiving side is typically a tool
    - Useful for databases, APIs, files, and applications
    - One agent remains in control
  [COLUMN]
    A2A
    - Connects an agent to another agent
    - Focuses on collaboration
    - The receiving side is another reasoning system
    - Useful for teams of specialized agents
    - Control may move between multiple agents
> 💡 An organization can use both at the same time. An agent may use MCP to access tools and A2A to collaborate with other agents.
## When is MCP enough?
Many agent systems do not need A2A at all.
If a single agent can access all required tools through MCP, adding multiple agents may only increase complexity.
For example, an internal HR assistant might use MCP to access:
- employee records
- company policies
- calendar systems
- document repositories
In this case, one agent can solve the entire task. There is no need to introduce additional agents.
## Check for Understanding
### Question 1
>  Sofia's Order Lookup Agent accesses Cascadia's order database, shipping API, and returns system — all through MCP. Does this configuration require A2A?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/90896912-752b-4872-9d5f-6a13fa4e15df
## When does A2A become valuable?
A2A becomes useful when multiple independent agents need to cooperate. This is especially common in larger organizations where different teams build and maintain their own agents, where agents operate in separate environments, or where each agent specializes in a different business domain. In these situations, one agent may need to delegate part of a task to another agent that has expertise, permissions, or capabilities it does not have itself.
> Consider a travel company. A customer-facing agent receives a request from a traveler who wants to modify an existing booking. Rather than handling every aspect of the request on its own, it contacts a booking agent that manages reservations, a payment agent that verifies refunds or additional charges, and a support agent that handles customer communication. Each agent focuses on its own responsibility and returns the relevant information. The customer-facing agent then combines the results and provides a complete response to the traveler.
![image]((notion-hosted file))
Instead of building one large agent responsible for every possible task, A2A allows several specialized agents to collaborate while remaining independent. This makes systems easier to maintain, scale, and extend as new capabilities are added.

> 💡 Today, many multi-agent systems use custom integrations to communicate. Every organization often builds its own message formats, workflows, and handoff mechanisms.
## Summary
MCP and A2A solve different problems. MCP standardises the connection between an agent and a tool. A2A standardises the connection between two independent agents that need to reason and act on their own.
A useful rule of thumb:
- If an agent needs a tool, MCP is usually the right solution.
- If an agent needs another agent's expertise or capabilities, A2A becomes relevant.
In the next lesson, you produce the architecture brief for the Sprint 1 project — deciding which of these protocols an integration problem actually needs.
