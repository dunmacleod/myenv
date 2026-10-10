# The Flowise Interface

Notion page: https://app.notion.com/p/The-Flowise-Interface-3669418319f3800ba25ad33db386851b
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: How to navigate the Flowise interface, how to read an Agentflow v2 node graph, and why Agentflow v2 is the correct build environment for this course.

## From infrastructure to workspace
Meridian Consulting's environment is verified. The local Flowise environment is running at a local browse, the Gemini API key is active, and the team is ready to begin building. Before anyone drags a single node onto the canvas, the team lead calls a ten-minute orientation. The reason is familiar: in previous projects, developers who skipped the orientation spent the first hour clicking through the interface trying to find components, misconnecting nodes, and building in the wrong flow type entirely.
Understanding the Flowise workspace by what the interface contains, how the canvas works, and what the different build modes are designed for takes less time than recovering from the confusion of skipping it. This lesson provides that orientation.

## The Flowise dashboard
When you open Flowise in your browser at http://localhost:3000, the dashboard is the first screen you see.
The navigation panel contains four primary sections. 
- Chatflows is where single-agent workflows and basic LLM chains are built and managed. 
- Agentflows v2 is where multi-agent systems and complex orchestration workflows are constructed. 
Marketplaces provides pre-built flow templates that can be imported and modified as starting points. Credentials is where API keys and authentication details are stored securely. This is where the Gemini key configured previously is held.

## The canvas
Opening an Agentflow v2 presents the canvas where the workflow is built visually. Every step in the workflow is a discrete node. The connections between nodes define the execution path clearly and there is no hidden logic running between steps.
The canvas has three main elements, Nodes, Edges and Flow state.
Nodes are added by clicking the (+) button on the canvas, which opens a searchable component panel.
![image]((notion-hosted file))
In Agentflow v2, the available nodes are:
[TABLE]
  | Node | Role |
  | Start Node | The mandatory entry point of every Agentflow v2. Defines how the workflow is triggered and sets up the initial conditions. Accepts input from the chat interface or a customizable form. Also handles Flow State initialization and conversation memory settings. |
  | LLM Node | Provides direct access to a configured Large Language Model for executing AI tasks. Used for text generation, summarization, translation, analysis, and generating structured JSON output. Has access to memory and can read and write to Flow State. Use this when you need a direct model call without full agent reasoning. |
  | Agent Node | Represents an autonomous AI entity capable of reasoning, planning, and interacting with tools or knowledge sources to accomplish a given objective. Uses an LLM to dynamically decide a sequence of actions and can choose to use available Tools or query Document Stores. This is the primary reasoning node in Meridian's agent. |
  | Tool Node | Provides a mechanism for directly and deterministically executing a specific, pre-defined Flowise Tool within the workflow sequence. Unlike the Agent Node where the LLM dynamically chooses a tool based on reasoning, the Tool Node executes exactly the tool selected by the workflow designer during configuration. |
  | Retriever Node | Performs targeted information retrieval from configured Document Stores by querying them based on semantic similarity. A focused alternative to using an Agent Node when the only required action is retrieval and dynamic tool selection by an LLM is not necessary. |
  | HTTP Node | Facilitates direct communication with external web services and APIs via HTTP. Enables the workflow to send GET, POST, PUT, DELETE, and PATCH requests to external endpoints, supporting authentication, custom headers, query parameters, and different request body types. |
  | Condition Node | Implements deterministic branching logic within the workflow based on defined rules. Evaluates one or more conditions comparing strings, numbers, or booleans using logical operators such as equals, contains, greater than, or is empty, then directs execution down different paths based on the result. |
  | Condition Agent Node | Provides AI-driven dynamic branching based on natural language instructions and context. Uses an LLM to analyze input data against a set of user-defined scenarios and routes the workflow down the path corresponding to the scenario the LLM determines best matches the input. Use this when fixed rules are insufficient for routing decisions. |
  | Iteration Node | Executes a defined sub-flow for each item in an input array, implementing a for-each loop. Takes an array as input and for every individual element sequentially executes the sequence of nodes placed inside its boundaries on the canvas. |
  | Loop Node | Explicitly redirects the workflow execution back to a previously executed node, enabling the creation of cycles or iterative retries. Includes a configurable Max Loop Count to safeguard against infinite cycles, with a default value of 5.  |
  | Human Input Node | Pauses the workflow execution to request explicit input, approval, or feedback from a human user. Halts automated progression and presents information or a question via the chat interface, then resumes execution along the path corresponding to the user's chosen action. |
  | Direct Reply Node | Sends a final message to the user and terminates the current execution path. Takes a configured message — static text or dynamic content from a variable — and delivers it directly to the end-user through the chat interface. The Message field must be explicitly set to the output variable of the preceding node using {{ syntax. |
  | Custom Function Node | Provides a mechanism for executing custom server-side JavaScript code within the workflow. Allows writing and running arbitrary JavaScript snippets for complex data transformations, bespoke business logic, or interactions with resources not directly supported by other standard nodes. The function must return a string value. |
  | Execute Flow Node | Enables the invocation and execution of another complete Flowise Chatflow or Agentflow from within the current workflow. Functions as a sub-workflow caller, promoting modular design and reusability of logic by triggering a separate pre-existing workflow, passing input to it, and receiving its output back. |
Edges are the connection lines drawn between nodes. An edge defines the direction of execution — which node runs next. In Agentflow v2, edges are explicit and directional. A node that is on the canvas but not connected to the execution path by at least one edge does nothing at runtime.
Flow State is a shared key-value store that persists across nodes during a single execution. Nodes can read from and write to Flow State using $flow.state. This is how data is passed between steps without hardcoding values into individual nodes.
![image]((notion-hosted file))

## Reading an Agentflow v2 graph
An Agentflow v2 graph is read by following the edges from the Start Node to the Direct Reply Node, tracing the path a user's query takes through the workflow. In a basic Meridian agent graph, the path looks like this:
1. The Start Node receives the user's input and initialises the flow.
1. The Agent Node receives the input, applies the system prompt, calls Gemini, and decides what to do.
1. If the agent has enough information, it passes a response to the Direct Reply Node.
1. The Direct Reply Node returns the response to the user and ends execution.
Every node in the graph has a role in that path. A node that is not connected is inactive and has no effect on the flow and produces no error, which makes disconnected nodes a common source of silent bugs.  

## Chatflow versus Agentflow v2
Flowise provides two build environments. This course uses Agentflow v2 exclusively.
[TABLE]
  |  | Chatflow | Agentflow v2 |
  | Design | Linear chains with implicit execution | Explicit node graph with visible execution path |
  | Branching | Not supported | Condition Node and Condition Agent Node |
  | State | Implicit memory modules | Flow State shared across all nodes |
  | Loops | Not supported | Loop Node |
  | Human approval | Not supported | Human Input Node |
  | Sub-flows | Not supported | Execute Flow Node |
  | Best for | Simple conversational agents | Multi-step, stateful business workflows |
Chatflow is appropriate for basic conversational agents with linear execution. Agentflow v2 is the correct choice when the workflow needs to branch, loop, retrieve knowledge dynamically, or pass context between steps which describes every requirement in Meridian's agent project.
All canvas work in this course is done in Agentflows, not Chatflows. When creating a new flow, always select Add New Agentflow from the Agentflows section of the left navigation panel.

## Check for Understanding
>  A Meridian developer places a Condition Node on the Agentflow v2 canvas but does not connect it to the Start Node or any other node. What is the result at runtime?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/133f1b95-0463-45df-b1fc-dd3736f1a23e

> 💡 Takeaway: 
  The Agentflow v2 canvas is where agent architecture becomes visible and clear. Every step is a node, every decision is a connection, and every piece of shared context lives in Flow State. 
  Understanding how these three elements work together is what makes the difference between a flow that behaves as intended and one that fails silently.