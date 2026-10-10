# Integration architecture brief

Notion page: https://app.notion.com/p/Integration-architecture-brief-3859418319f380559645c6e94b7ab4ea
Backed up before n8n migration

You are designing a Multi-Agent IT Support System for Halcyon Labs, a mid-sized research and technology firm whose engineers, analysts, and researchers submit a steady stream of technical requests through the internal helpdesk. The system should help users report technical issues, classify requests, retrieve relevant information, and route cases to the right specialist agent when needed.
A later phase of the project — which you build hands-on in Sprint 3 — will extend the system with a research-retrieval capability that connects to arXiv, the free open-access archive of nearly 2.4 million scholarly articles across physics, mathematics, computer science, and related fields. Your architecture brief needs to account for both phases: the initial IT-support workflow, and the eventual arXiv integration.
Your task is not to build the system. Your task is to produce an integration architecture brief that explains which communication and integration protocols the project should use.
## Project scenario
The Multi-Agent IT Support System includes several agent roles:
The Intake Agent receives the user's request and identifies the issue category.
The Knowledge Agent searches internal documentation, troubleshooting guides, and known issue records.
The Ticketing Agent creates or updates tickets in the organization's helpdesk system.
The Specialist Agents handle specific domains such as access problems, software issues, hardware requests, and billing-related IT services.
The Supervisor Agent reviews uncertain cases, escalations, and handoffs between agents.
The system may need to connect to internal tools such as a ticketing platform, knowledge base, asset inventory, employee directory, and communication tools.
## Assessment task
Write an integration architecture brief that answers this question:
Does the Multi-Agent IT Support System need MCP, A2A, or both?
Your brief should include the following sections.
### 1. Project integration needs
Describe what the system needs to connect to.
Include both tool/data needs and agent communication needs where relevant.
### 2. MCP decision
State whether MCP is needed.
Justify your decision by explaining whether the agents need access to tools, APIs, databases, files, or knowledge sources.
### 3. A2A decision
State whether A2A is needed.
Justify your decision by explaining whether independently deployed agents need to communicate across systems, teams, frameworks, or vendors.
### 4. Final architecture choice
Choose one:
MCP only
A2A only
Both MCP and A2A
Neither
Explain your final choice clearly.
### 5. Rejected option
Document why any rejected option was rejected.
If you choose both MCP and A2A, explain why "MCP only" and "A2A only" would be incomplete.
If you choose only one, explain why the other is not necessary for this project.
## Expected answer direction
A strong answer will usually conclude that this project needs MCP, and may also need A2A depending on deployment assumptions.
MCP is needed because the agents must access external tools and data sources such as the ticketing system, documentation, asset inventory, employee directory, and possibly communication platforms.
A2A is needed only if the specialist agents are separately deployed systems that must interoperate across teams, frameworks, or vendors. If all agents live inside one Flowise workflow or one orchestration environment, internal message passing may be enough, and A2A can be rejected for the current version.
A strong architecture choice could therefore be:
Use MCP now for tool and data integration. Do not use A2A in the first version unless agents are deployed independently across different systems. Keep A2A as a future architecture option if the support workflow grows into separately owned or separately deployed agents.
## Submission format
Submit a short architecture brief of 400–700 words.
Use clear section headings.
Do not write implementation steps.
Do not describe how to configure Flowise.
Focus on architecture reasoning and justification.
## Assessment checklist
- Your submission should clearly answer:
- What external tools or data sources does the system need?
- Why MCP is or is not required?
- Why A2A is or is not required?
- Which option is selected?
- Which option is rejected?
- Why the rejected option does not fit the current project?
## Close
This assessment checks whether you can make an architecture decision instead of just naming protocols. A good brief shows that you understand what the system must connect to, how agents need to communicate, and which integration layer is actually necessary for the current project.