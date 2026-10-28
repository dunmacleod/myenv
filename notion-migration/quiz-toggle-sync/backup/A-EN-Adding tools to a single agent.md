# Adding tools to a single agent

Notion page: https://app.notion.com/p/Adding-tools-to-a-single-agent-3689418319f380789e9fc6d36b278ee8
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: How tools extend an n8n AI Agent beyond retrieval and text generation, and how the agent decides when a tool is needed.

## The boundary of read-only RAG
Contigo GmbH's support agent can already answer questions from the knowledge base you connected in Sprint 2. It can explain loan products, eligibility criteria, and application requirements using retrieved evidence.
But some client requests require more than information:
> "Can you check the current status of application APP-7741?"
The knowledge base can explain the application process, but it cannot know the current status of one specific application. That information belongs to a live system. To answer reliably, the agent needs a tool that can query that system.
This is the difference between retrieval and tool use. RAG gives the agent access to documented knowledge. Tools give it access to capabilities such as live lookups, calculations, APIs, databases, and deterministic workflows.

## What tools are
A tool is a capability the AI Agent can invoke while processing a request.
Three common categories are useful for Contigo:
- Information tools: Query live or structured data, for example an application-status service.
- Action tools: Trigger a controlled operation in another system or workflow.
- Computational tools: Perform deterministic calculations rather than asking the language model to calculate approximately.
In n8n, tool-capable nodes connect to the Tool input of the AI Agent. In this sprint you will keep the Qdrant retrieval tool from Sprint 2 and add a Calculator plus a workflow tool for a mock loan-status lookup.

## The agent tool loop
A tool-enabled agent follows a repeated decision loop:
1. Reason: Determine what information or action is needed.
1. Act: Select an appropriate tool and provide its required inputs.
1. Observe: Read the tool result.
1. Continue or answer: Call another tool if necessary, or produce the final response.
For example:
1. The client asks for the status of APP-7741.
1. The AI Agent recognises that this requires live application data.
1. It calls the loan-status tool with APP-7741.
1. The tool returns a structured status.
1. The agent explains that result to the client.
The model should not call every connected tool. It should call only the tool whose description and input requirements match the request.

> ➡️ How this maps to your n8n build: You do not replace the AI Agent you built in Sprints 1 and 2. The same Chat Trigger → AI Agent workflow remains the core. The OpenRouter Chat Model, Simple Memory, and Qdrant retrieval tool stay connected; Sprint 3 expands the AI Agent's Tool connections.

## Why tool descriptions matter
The AI Agent chooses tools from their names, descriptions, input schemas, the system message, and the current conversation. If two tools have vague or overlapping descriptions, the model may call the wrong one or call a tool when no tool is needed.
A strong tool description therefore states:
- what the tool can do;
- when it should be used;
- what input is required;
- what it must not be used for.
You will practise this explicitly in the next lessons.

## RAG and tool-enabled agents
[TABLE]
  |  | Retrieval capability | Additional tool capability |
  | Primary purpose | Answer from indexed documents | Use live data, deterministic logic, or external operations |
  | Contigo example | "What documents are required for an SME loan?" | "What is the status of application APP-7741?" |
  | n8n implementation | AI Agent + Qdrant retrieval tool | The same AI Agent + additional Tool connections |

## Check for Understanding
> 💡 A Contigo client asks the support agent for the current status of a specific application. The agent retrieves a policy page explaining normal processing times but cannot provide the actual status. What capability is missing?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bf6c2b9e-4f18-47cb-911d-654ec5cfd2df

> 💡 Takeaway: RAG gives the agent documented knowledge. Tools extend the same n8n AI Agent with capabilities that are not contained in static documents. Good architecture starts by giving one agent a small, clearly described toolset before adding more agents or orchestration complexity.