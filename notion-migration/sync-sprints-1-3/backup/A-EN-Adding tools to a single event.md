# Adding tools to a single event

Notion page: https://app.notion.com/p/Adding-tools-to-a-single-event-3689418319f380789e9fc6d36b278ee8
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: How tools transform a language model from a text generator into an active system capable of interacting with live data and external services. 

## The boundary of read-only RAG
Contigo GmbH's support agent retrieves accurately from the knowledge base and answers client questions about loan products, eligibility criteria, and compliance requirements. For informational queries, it performs reliably.
But a category of client requests has emerged that the current system cannot handle. A client contacts the agent and asks not for information, but for action.
> "Please cancel my pending loan application and confirm the cancellation by email."
The agent retrieves the relevant policy section about application withdrawals. It generates a professionally worded explanation of the cancellation process. It cannot cancel the application. It cannot send the email. It can only describe what would happen if a human performed those actions.
This is the structural boundary of a retrieval-only agent. RAG gives the agent access to knowledge. It does not give the agent the ability to act on that knowledge in the world. For Contigo to move from an agent that answers questions to one that resolves requests, the agent needs tools.

## What tools are
Tools are external capabilities that a language model can invoke programmatically during its reasoning process. They extend the agent's reach beyond text generation into live systems, databases, and services.
Tools fall into three functional categories that together cover the majority of enterprise automation requirements.
Data and information tools: These give the agent access to live, structured data that is not in the knowledge base and cannot be embedded as static documents. 
For Contigo, this includes querying the client database for account status, checking the current application processing queue, or retrieving a client's payment history from the core banking system. Data tools query live systems in real time.
Action and execution tools: These allow the agent to change the state of external systems on the user's behalf. Cancelling a loan application, updating a client's contact details in the CRM, triggering a document generation workflow, or sending a confirmation email are all execution actions. These are the capabilities that transform the agent from an information provider into a resolution system.
Computational tools: Language models are unreliable at precise mathematics and structured logic execution. A computational tool offloads these tasks to a deterministic system and returns the result to the agent for incorporation into its response. 
For Contigo, this might mean calculating a client's remaining loan term based on their payment history, or running a structured query against the eligibility criteria database.

## The ReAct loop
The mechanism that governs how an agent decides when and how to use a tool is the ReAct framework - Reasoning and Acting. ReAct is the execution pattern that most agentic frameworks, including those built on Flowise and Gemini, implement under the hood when an agent is connected to tools.
The loop operates in three repeating steps.
Thought: The agent reasons about the current state of the task. It reads the user's request, reviews what it already knows from the conversation history and any prior tool outputs, and determines what it needs to do next. 
Action: The agent selects a tool and invokes it with the parameters determined in the Thought step. It does not generate a user-facing response at this stage. It calls the tool and waits for the result.
Observation: The agent receives the tool's output and incorporates it into its reasoning context. The loop then returns to the Thought step. This continues until the agent determines it has sufficient information to generate a final response.
For Contigo's cancellation request, the ReAct loop might proceed as follows. 
1. The agent thinks: the client wants to cancel application APP-7741 and receive a confirmation email. 
1. It acts: it calls the cancellation tool with the application ID. It observes: the tool returns a success confirmation and a reference number. 
1. It thinks again: the cancellation is confirmed; now call the email tool with the reference number and the client's address. 
1. It acts again: It observes the email confirmation. It generates the final response to the client.
![image]((notion-hosted file))

> ➡️ How this works in your Chatflow: In Flowise, the ReAct loop is implemented through the Tool Agent node. This is the node you will use to replace your Conversational Retrieval QA Chain when you add tools to your Chatflow. The Tool Agent node connects to your language model, your memory node, your vector store retriever, and your tools. It also executes the ReAct loop automatically for every incoming query. Understanding the loop before configuring the node is what makes the configuration decisions meaningful rather than mechanical.

## Why this matters for agent design
Understanding the ReAct loop has direct implications for how tools are configured and described. The agent's Thought step relies entirely on the natural language descriptions provided for each tool to determine which tool to invoke and what parameters to pass. A tool description that is vague or overlapping with another tool's description produces routing failures.
The quality of the tool description is the primary lever controlling the reliability of the ReAct loop. This is covered in practice further on in this sprint.
RAG versus tool-enabled agents
[TABLE]
  |  | RAG agent | Tool-enabled agent |
  | Primary capability | Retrieving and presenting information from documents | Taking action in external systems and live databases |
  | Data access | Static or periodically updated embedded documents | Live APIs, databases, and real-time services |
  | System impact | Read-only — cannot modify external state | Read and write — can create, update, and trigger |
  | Example — Contigo | "What documents are required for a loan application?" | "Cancel application APP-7741 and send a confirmation email" |
  | Flowise node | Conversational Retrieval QA Chain | Tool Agent |

## Check for Understanding
>  A Contigo client asks the support agent to update their registered email address. The agent retrieves the policy for updating contact details correctly but does not make any change to the client's account. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bf6c2b9e-4f18-47cb-911d-654ec5cfd2df


> 💡 Takeaway: 
  RAG gives an agent knowledge. Tools give it the ability to act on that knowledge. The ReAct loop is the mechanism that connects reasoning to action until the task is resolved. For Contigo's agent to move from answering questions to resolving requests, tools are the architectural requirement that makes the difference between a sophisticated information retrieval system and a genuine automation platform. 
  In your Chatflow, this transition happens when you replace the Conversational Retrieval QA Chain with a Tool Agent node and connect Contigo's first action tool to the canvas.
