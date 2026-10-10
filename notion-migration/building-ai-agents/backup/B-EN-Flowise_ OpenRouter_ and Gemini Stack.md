# Flowise, OpenRouter, and Gemini Stack

Notion page: https://app.notion.com/p/Flowise-OpenRouter-and-Gemini-Stack-3669418319f38016bf6eef4efd60b760
Backed up before n8n migration

> Using OpenRouter instead of Gemini
  Some AI course materials may show Gemini setup directly inside tools like n8n, Flowise, or Cursor. In this program, use your school-provisioned OpenRouter key instead. The workflow logic stays the same, but the model connection may change.
  Before starting, read the setup guide: How-To: Using OpenRouter instead of Gemini 
> 💡 What you will understand by the end of this lesson: How Flowise, Gemini, and knowledge storage fit together as a self-hosted stack, and why Agentflow v2 is the right build environment for creating a business-grade AI agent workflow.
## The starting point
Meridian Consulting is a Berlin-based operations consultancy that works with mid-sized businesses across Germany, Poland, and the Czech Republic. Their clients run lean teams and rely heavily on Meridian's advisors for process design, vendor selection, and operational troubleshooting.
The firm has decided to build an internal AI agent to help its consultants answer common client questions faster, surface relevant case history, and route complex queries to the right specialist. They have chosen to build on a self-hosted instance of Flowise, an open-source visual builder that runs locally without requiring the team to pay for managed cloud infrastructure.
The first decision the team faces is which tools to use. After evaluating several options, they have landed on a stack built around Flowise and Google's Gemini models. Before anyone writes a line of configuration, the team needs to understand how these components fit together and what role each one plays.

## Why a visual builder?
Building AI agent workflows from scratch in raw Python or JavaScript gives developers full control. It also means writing significant amounts of boilerplate code for every API integration, prompt chain, memory module, and tool connection — and then maintaining that code as the underlying models and APIs evolve.
Flowise is an open-source, low-code visual builder for LLM-powered applications. It provides a drag-and-drop canvas where components are represented as nodes that can be connected visually. The underlying logic is the same as a coded implementation, but the architecture is visible, debuggable, and modifiable without touching application code.
For Meridian's team, which includes consultants who are not software engineers, this is the decisive advantage. The agent can be built, tested, and refined by people who understand the business problem without requiring a dedicated engineering team for every change. 
Because Flowise is open-source, it can be run locally using Node.js and npm at no cost. This is the setup used throughout this course. Students run Flowise on their own machine. There is no subscription required.

## Why Agentflow v2?
Flowise provides two build environments: Chatflow and Agentflow v2.
Chatflow is designed for simpler, linear workflows such as a single agent following a fixed sequence of steps. It is useful for basic conversational agents but becomes limiting quickly when a workflow needs to branch, loop, retrieve knowledge dynamically, or coordinate multiple steps with shared context.
Agentflow v2 is the environment this course will use. It is Flowise's native orchestration environment for building stateful, multi-step AI workflows. In Agentflow v2, every step in the workflow is a discrete node on the canvas. The connections between nodes define the execution path explicitly. This architecture supports:
- Conditional branching based on rules or AI reasoning
- Loops and retry logic
- Knowledge retrieval from Document Stores
- Shared context across nodes via Flow State
- Human approval checkpoints
- Modular sub-flows
For Meridian's agent, Agentflow v2 is the correct environment from the start.

## The reasoning engine: OpenRouter API
Every agent stack needs a language model at its centre. This is the component that reads the prompt, reasons about it, and generates a response. For this stack, that role is filled by OpenRouter. 
OpenRouter is home to a series of AI models that you can use through a single API key. You will receive this API key in your e-mail. Make sure you never share the API key.
For the knowledge retrieval (RAG), you will need your Gemini API. For Meridian's production deployment handling real client data, upgrading to a paid tier would be a required step before going live.
> 🔥 Later models can also be used. That is fine: model names change over time, but the setup logic stays the same. If one model is unavailable, rate-limited, or deprecated, select the closest newer Flash-family model and continue.
For the current model strings, full capability details, and up-to-date pricing, refer to the official Gemini API documentation at ai.google.dev/gemini-api/docs/models and ai.google.dev/gemini-api/docs/pricing.
## The knowledge layer: Document Stores and the Retriever Node
Language models cannot natively search through large document sets. To give the agent access to Meridian's internal case library, vendor database, and operational playbooks, that content must first be loaded into a format the agent can search semantically.
In Agentflow v2, this is handled through Flowise Document Stores. A Document Store is a managed knowledge container built into Flowise. Documents are uploaded, chunked, embedded, and indexed inside the store. When an agent needs to retrieve information, it queries the store using the Retriever Node or accesses it directly through the Agent Node's Knowledge configuration.
This is the native Agentflow v2 approach to retrieval and the method this course uses. External vector databases such as Chroma can also be connected through the Agent Node's Vector Embeddings configuration, but Document Stores are the recommended starting point and require no additional infrastructure to set up.

## How the components connect
[TABLE]
  | Component | Technology | Role in the stack |
  | Orchestration environment | Flowise Agentflow v2 | Explicit workflow canvas where every step is a node; controls execution order, branching, and state |
  | Reasoning engine | Gemini (RAG) and OpenRouter | Drives the Agent Node's reasoning, tool selection, and response generation |
  | Knowledge layer | Flowise Document Stores | Stores and retrieves content semantically; queried by the Retriever Node or Agent Node |
  | Shared context | Flow State ($flow.state) | Runtime key-value store that passes data between nodes throughout a single execution |

## Check for Understanding
>  In Agentflow v2, what is the primary difference between a Document Store and the Flow State?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/77c31602-446c-474f-bc67-17d9fe211962

> 💡  Takeaway: 
  The Agentflow v2 stack separates its responsibilities cleanly. Flowise provides the orchestration environment, running locally via npm at no cost. Gemini reasons and generates. Document Stores hold and surface knowledge. Flow State connects it all at runtime. 
  Understanding what each component does is the foundation for building an agent that is reliable, maintainable, and easy to debug as it grows in complexity.
