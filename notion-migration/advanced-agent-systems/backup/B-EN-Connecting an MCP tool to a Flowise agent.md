# Connecting an MCP tool to a Flowise agent

Notion page: https://app.notion.com/p/Connecting-an-MCP-tool-to-a-Flowise-agent-37e9418319f3807e8dccf27b8f23c646
Backed up before n8n migration

Sofia's Intake Agent can now hand off structured context, but it still can't reach any external system on its own. To actually resolve customer issues at Cascadia, the agent will need tools — starting with something simple. In this walkthrough, you connect a single MCP server to a Flowise agent and check whether the agent can discover and use it correctly.
## Scenario
Sofia wants to see the MCP integration pattern working before she wires up Cascadia's business systems. She sets up the smallest possible test: one Flowise agent, one MCP server, one query that requires the tool. If the agent discovers the tool, calls it, and uses the response, she knows the pattern will hold when she plugs in real Cascadia tools later.
For this walkthrough, use a simple MCP server such as Sequential Thinking MCP server that is already available in your Flowise setup. 
## Instructor walkthrough
### Step 1: Create a new Agentflow
Open Flowise and create a new Agentflow V2 workflow. Add a Start node and a Chat Input field if your canvas does not already include one.
![image]((notion-hosted file))
### Step 2: Add an Agent node
Add an Agent node and connect it to the Start node.
![image]((notion-hosted file))
You can rename your agent to something like Agent with Sequential MCP. Select the LLM of your choice (Gemini or Ollama) and in the system prompt (Add Message button), use:
> 💬 You are an IT support assistant.
  Your job is to answer the user’s request.
  When an MCP tool is useful, call the tool before answering.
  When no tool is needed, answer directly.
![image]((notion-hosted file))
Keep the prompt simple. The goal is not to build the final support agent yet. The goal is to prove that the agent can use an MCP tool.

### Step 3: Connect the MCP tool
In the Agent node configuration, open the tools section and add the available MCP tool/server for sequential thinking:
![image]((notion-hosted file))
In the Available actions section, select SEQUENTIAL THINKING.
![image]((notion-hosted file))
### Step 4: Test tool discovery
Save and run the flow with a prompt that clearly requires the MCP tool. For Sequential Thinking MCP, use something like:
> 💬 Break this problem into steps: I need to diagnose why a user cannot access their company email.
The agent should not only answer from memory. It should call the MCP tool or show evidence that it used the connected capability.
### Step 5: Observe the result
![image]((notion-hosted file))
Open the run details or node execution output. Look for:
- whether the agent selected the MCP tool,
- what input it passed to the tool,
- what result came back,
- how the final answer used the result.
This is the key learning moment: MCP is successful only if the agent can actually call the tool during the workflow.
## Common failure points
[TABLE]
  | Problem | What learners see | How to recover |
  | MCP tool does not appear | No available MCP actions in Flowise | Check that the MCP server is installed, running, and connected to Flowise |
  | Agent ignores the tool | The answer appears, but no tool call is visible | Make the prompt more explicit and ask for a task that requires the tool |
  | Authentication fails | Tool call returns an auth error | Check access token, environment variables, or provider login |
  | Local server unavailable | Connection or timeout error | Restart the MCP server and Flowise container |
  | Wrong node type | Tool cannot be attached | Use an Agent node that supports tools, not a plain LLM node |
## Solved reference behavior
A successful run should show this pattern:
![image]((notion-hosted file))
The exact output depends on the MCP server, but the run log should clearly show that the MCP tool was called.
## Debrief lens
The important distinction is between having a tool configured and having an agent use the tool correctly. A tool listed in Flowise is only potential capability. The real test is whether the agent calls it at the right moment and uses the result in the final response.
## Summary
You connected one MCP tool to a Flowise agent and watched it discover, call, and use the result. This is the basic integration pattern behind more advanced agent systems. In the next lesson, we look at what happens when Sofia's agents need to talk to another team's agent — a different problem that MCP alone does not solve.