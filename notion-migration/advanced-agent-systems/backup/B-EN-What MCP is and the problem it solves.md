# What MCP is and the problem it solves

Notion page: https://app.notion.com/p/What-MCP-is-and-the-problem-it-solves-37e9418319f3807dab30cea98d38d2b5
Backed up before n8n migration

Sofia's Intake Agent (from the previous lesson) does one job well: it classifies a customer message and writes structured context to Flow State. But that's only the first half of a real support workflow. To actually resolve a customer's issue, the Specialist Agent needs to look up the customer's order in Cascadia's order database, check the shipping status through the carrier's API, and pull warranty records from the compliance team's system.
Traditionally, every one of those integrations required custom code. Sofia's team would write one connector for the order database, another for the shipping API, another for the warranty records — each with its own format, its own error handling, its own authentication. Every new tool the agent needs is another maintenance burden.
This creates a familiar problem: agents become powerful, but connecting them to real systems becomes a bottleneck. As the number of tools grows, the integration work grows faster than the value the agent produces.
Model Context Protocol (MCP) was created to solve this problem.
## The integration problem
Imagine you are building an AI assistant for a company. The assistant needs to search internal documents, read files from Google Drive, query a PostgreSQL database, create Jira tickets, send Slack messages, and trigger automation workflows. Without a common integration standard, every system requires its own custom connection. Each tool may use different authentication methods, API designs, request formats, and response structures. As more tools are added, the amount of integration work grows quickly, making the system harder to develop, maintain, and scale. This is the challenge that Model Context Protocol (MCP) aims to solve.

![image]((notion-hosted file))
## What is MCP?
Model Context Protocol (MCP) is an open protocol that allows AI models and agents to communicate with external tools and data sources through a standardized interface.
Instead of building a custom connection for every system, developers implement the MCP standard once.
An MCP-compatible agent can then work with any MCP-compatible tool.
You can think of MCP as a universal power adapter when traveling. 
When you travel between countries, every country may have different wall sockets. Without a universal adapter, you need a different plug for every destination. The more countries you visit, the more adapters you need to carry.
MCP works in a similar way for AI agents. Instead of building a different connection for every tool, database, or application, the agent connects through one common standard. As long as a tool supports MCP, the agent can interact with it without needing a custom integration.
## MCP architecture
At a high level, MCP introduces two main components:
[TABLE]
  | Component | Purpose |
  | MCP Client | The agent or application requesting access |
  | MCP Server | The system exposing tools, resources, or actions |
The agent does not need to know implementation details.
Instead, it asks the MCP server:
- What tools are available?
- What parameters does this tool require?
- How should I call it?
The MCP server provides this information in a standard format.

![image]((notion-hosted file))
## What can MCP connect to?
An MCP server can expose many different kinds of resources to an AI agent. These resources may include files such as PDFs, spreadsheets, and documents; databases such as PostgreSQL, MySQL, or Snowflake; external APIs like weather services, CRM systems, or ERP platforms; knowledge bases such as Notion, Confluence, and SharePoint; communication tools including Slack, Microsoft Teams, and Gmail; automation platforms like n8n, Zapier, and Make; and developer tools such as GitHub, GitLab, and Jira.
The key advantage of MCP is that, from the agent's perspective, all of these resources appear as discoverable tools that can be accessed through a consistent interaction pattern. This allows the agent to work with many different systems without needing a custom integration for each one.
## Why MCP matters for agents
MCP is becoming important because agents rarely operate in isolation. Most useful agents need access to information, the ability to take actions, and connections to business systems while working across multiple tools and platforms. Traditionally, every new integration required custom engineering effort, meaning developers had to build and maintain separate connections for each system.
MCP addresses this challenge by providing a standardized way for agents to discover and interact with external resources. As a result, integrating new tools becomes simpler, extending an agent's capabilities no longer requires changes to its core logic, and organizations can benefit from a growing ecosystem of compatible tools built by different providers. This allows developers to focus on designing intelligent agent behavior rather than spending time on integration and infrastructure work.
## Check for Understanding
### Question 1
>  Your agent needs to access several systems:
  - A PostgreSQL database
  - A file storage system
  - A ticketing platform
  Which statement best describes the role of MCP?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/83293b5d-051f-4818-91c2-3a75451acf74

## Summary
Before MCP, every tool Sofia needs at Cascadia would require its own custom connector — one for the order database, another for the shipping API, another for the warranty system. MCP replaces that per-tool integration work with one standard protocol that any MCP-compatible tool can plug into.
In the next lesson, Sofia connects an actual MCP tool to a Flowise agent and watches the agent discover and call it.
