# What is MCP and Connecting MCP Tools in Agentflow v2

Notion page: https://app.notion.com/p/What-is-MCP-and-Connecting-MCP-Tools-in-Agentflow-v2-3669418319f380d39e71ffede85a6202
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Understand what MCP is, why it exists, and how MCP tools connect to Agentflow v2 nodes.

## Setting the scene
Meridian's agent is connected to three capabilities: a Document Store, an HTTP Node for live data, and an iteration flow for briefings. Each connection required custom configuration: credentials, URL endpoints, response handling, and error logic written specifically for each integration.
If Meridian were to rebuild the same agent in a different framework tomorrow, every integration would need to be reconfigured from scratch. If a client wanted to access Meridian's knowledge base from their own agent built on a different platform, the entire integration layer would need to be rebuilt again.
This is the integration problem that MCP solves.

## What MCP is
The Model Context Protocol is an open standard that defines a universal interface for how AI agents connect to external tools and data sources. It was introduced by Anthropic in late 2024 and has since been adopted across agent frameworks, development environments, and enterprise platforms.
The analogy that captures it most clearly is USB-C. Before standardised ports, connecting a peripheral required knowing which specific connector each device used. USB-C provides a universal connection standard and any compatible peripheral connects to any compatible device through the same port. MCP does the same for AI agents and external tools.
An MCP server exposes three categories of capability:
[TABLE]
  | Category | What it provides |
  | Tools | Functions the agent can invoke to take actions or retrieve data |
  | Resources | Data sources the agent can read from |
  | Prompts | Reusable prompt templates stored on the server |
When a new tool or resource is added to an MCP server, connected agents discover it automatically without requiring updates to the agent configuration.

### How MCP works in Agentflow v2
Agentflow v2 allows MCP tools to be connected as part of the workflow, rather than functioning solely as agent tools. Custom MCPs can also be created independently, without depending on platform-provided integrations. MCP is widely considered an industry standard and is typically supported and maintained by the official providers.
In Agentflow v2, MCP tools connect through the Agent Node's Tools configuration. Once an MCP server is configured in Flowise, its tools appear in the Agent Node's tool selector alongside native Flowise tools. The agent can then invoke them dynamically based on reasoning exactly like any other tool.
![image]((notion-hosted file))
This means Meridian's Agent Node A could connect to a Jira MCP server and create tickets, query a GitHub MCP server for repository context, or retrieve live data from a Brave Search MCP server, all without writing custom API integration code for each one.

### Why MCP matters for the Meridian project
Three specific benefits apply directly to what has been built:
- Cross-framework interoperability: An MCP server built to expose Meridian's Document Store can be consumed by a Flowise agent, a Langflow agent, and a Claude environment simultaneously without rebuilding the integration for each platform.
- Reduced integration overhead: Instead of writing custom connectors for every tool in every framework, a team builds one MCP server per tool. Any MCP-compatible agent can then access it through the same standardised interface.
- Ecosystem composability: MCP transforms isolated agent frameworks into an interconnected ecosystem. A tool built for one platform becomes available to all platforms that support the standard.

### MCP versus the HTTP Node
Students who have worked through Sprint 2 will notice a similarity between MCP tools and the HTTP Node. Both connect the agent to external systems. The difference is scope and standardisation:
[TABLE]
  |  | HTTP Node | MCP Tool |
  | Setup | Configure per endpoint | Configure once per server |
  | Discovery | Manual: You define each call | Automatic: Agent discovers available tools |
  | Portability | Specific to this canvas | Available to any MCP-compatible agent |
  | Best for | One-off API calls | Reusable, multi-tool integrations |
The HTTP Node is the right choice for a single specific API call. MCP is the right choice when a tool needs to be reusable, discoverable, and available across multiple agent frameworks.

## Check for Understanding
>  Meridian builds a single MCP server that exposes its Document Store as a resource. A client organisation wants to access the same knowledge base from their own Flowise agent. What does the client need to do?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/0acaa5be-684a-45ac-9654-7df3e7f8ecfa


> 💡 Takeaway: 
  MCP does for AI agent integrations what USB-C did for hardware connectivity — it replaces a fragmented landscape of custom connectors with a single universal standard. One MCP server per tool. Any compatible agent can use it. When a new capability is added to the server, all connected agents discover it automatically. For Meridian's agent and its clients, this means integrations built once become available everywhere.