# n8n, OpenRouter, and the AI Stack

Notion page: https://app.notion.com/p/n8n-OpenRouter-and-the-AI-Stack-3669418319f38016bf6eef4efd60b760
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: what n8n does, how it fits together with OpenRouter, and which responsibility belongs to the workflow platform, the model, credentials, and later knowledge or tool integrations.
## The starting point
Meridian Consulting wants an internal AI assistant that can answer common operational questions, use business tools when needed, and eventually retrieve information from company knowledge sources.
A useful agent is not only a language model. It needs an environment that can receive input, connect services, run logic, call models and tools, and show us what happened when something fails.
In this course, that environment is n8n.
## What n8n is
n8n is a workflow automation platform. You build workflows from connected nodes. A node can receive a chat message, call an API, transform data, query a model, use a tool, or send a result to another system.
For this course, n8n is the orchestration layer around the agent. It makes the architecture visible and testable rather than hiding everything inside one large script.
> 📸 SCREENSHOT SUGGESTION: n8n Overview page with the Create Workflow action visible. Crop out personal workspace names if necessary.
## The stack used in Sprint 1
- n8n — workflow orchestration and execution.
- OpenRouter Chat Model — model access through the school-provisioned OpenRouter API key.
- Credentials in n8n — secure storage for API keys; keys should not be pasted directly into prompts or workflow text.
- AI Agent node — the agent component that receives instructions and can use a model and tools.
- Tools — capabilities the agent can call. We will add a simple tool in the first workflow and expand this later.
- Knowledge and persistent memory — introduced in later sprints.
n8n has a dedicated OpenRouter Chat Model node. The available models are loaded dynamically from OpenRouter, so model names can change while the workflow pattern stays the same.
Official references:
- n8n OpenRouter Chat Model
- n8n OpenRouter credentials
## Why use a workflow builder?
You could build the same system in Python or JavaScript. In n8n the main integration steps are explicit on the canvas.
That gives Meridian three advantages:
1. Visibility: the team can see how input moves from one step to the next.
1. Debugging: each node exposes its input, output, and execution result.
1. Iteration: a model, prompt, tool, or branch can be changed without rebuilding the entire application.
The visual canvas does not remove the need to understand architecture. It makes architecture easier to inspect.
## How the pieces connect
A simple AI workflow will soon look like this:
Chat Trigger → AI Agent
The AI Agent then has supporting connections:
- OpenRouter Chat Model for generation and reasoning.
- A tool that the agent may call when the task requires it.
Later we will add memory, retrieval, databases, and external services.
![image]((notion-hosted file))
## Keep responsibilities separate
When something goes wrong, ask which layer is responsible:
- The workflow did not start → trigger or workflow configuration.
- Authentication failed → credential or provider issue.
- The model returned an unexpected answer → instructions, model choice, or input.
- The agent could not perform an action → missing or incorrectly configured tool.
- A later retrieval step returns irrelevant information → knowledge or retrieval configuration.
## Check your understanding
Before moving on, make sure you can explain:
- Why n8n is not itself a language model.
- Why an API key belongs in credentials rather than in a prompt.
- What the AI Agent node is responsible for.
- Why a visual workflow still needs deliberate architecture.
> 💡 Takeaway: n8n is the orchestration layer. OpenRouter provides model access. Credentials authenticate safely. The AI Agent combines instructions, a chat model, and tools inside an executable workflow.