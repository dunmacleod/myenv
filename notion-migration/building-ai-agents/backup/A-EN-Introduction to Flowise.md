# Introduction to Flowise

Notion page: https://app.notion.com/p/Introduction-to-Flowise-36c9418319f3801cb4eadc8b4518971f
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: What Flowise is, why it exists, how it works as a visual builder for AI agents, and how it will be used throughout this course to build the Contigo GmbH support agent.

## The problem Flowise solves
Building an AI agent from scratch in code means writing connection logic for every component. This includes the language model, the memory module, the vector database, the tools, the prompt chain. Each integration requires its own API calls, error handling, and configuration. Before a single agent behaviour is tested, a developer has written hundreds of lines of boilerplate that has nothing to do with the actual problem they are trying to solve.
For a team like Contigo GmbH's, which needs to move from business requirement to working prototype quickly, this overhead is a barrier. The time spent on infrastructure is time not spent on the agent's actual design such as the memory strategy, the retrieval pipeline, the tool descriptions, the failure handling.
Flowise removes that barrier. It provides a visual, drag-and-drop environment where AI agent components are represented as nodes on a canvas. Connecting a language model to a memory module is a drag-and-drop gesture. Adding a vector database to the retrieval pipeline is a configuration panel. The infrastructure is handled. The design work is what remains.

## What Flowise is
Flowise is an open-source, low-code visual builder for large language model applications and AI agents. It was developed to make the construction of LLM-powered systems accessible to developers who understand the problem they are solving without needing to write framework-level integration code from scratch. Flowise is available in two main ways: as a self-hosted application or as Flowise Cloud. In this course, you will use the self-hosted version of Flowise. 

Go to this page to set up your local environment. You will mainly work with the visual builder, where you create agents and workflows by adding components and connecting them. You can check the official interface documentation here: Flowise documentation

The Flowise interface is accessible through your local browser. Once the application is running, every component of an agent architecture is available as a draggable node in the component palette. The agent's architecture is built by connecting those nodes and configuring their parameters.
## How Flowise works
Flowise organises agent builds into multiple environments, each designed for a different level of architectural complexity. However, we will focus on Chatflow for this course.
Chatflow is the primary environment for single-agent systems. It supports the main building blocks you'll learn to use throughout this course: chaining conversation steps together (conversational chains), letting an agent answer from your own documents (a pattern called RAG), the kind of memory you just learned about, and connecting agents to external tools. You'll get a dedicated lesson on each — no need to recognise the names yet.
The execution path through a Chatflow is relatively linear. A user query flows through the connected components in a defined sequence and returns a response. This is the environment used for the majority of the Contigo agent build throughout this course.
Each node has connection points called inputs and outputs. Outputs from one node can be connected to compatible inputs on another node. Flowise helps prevent some setup mistakes by only allowing certain connection types to fit together. A node placed on the canvas only affects the agent if it is connected to the active flow path used at runtime.
![image]((notion-hosted file))

## Why Flowise exists
Three shifts in the AI development landscape created the conditions that made Flowise necessary.
1. The first reason was the growing number of moving parts in AI systems. Teams had to connect language models that write responses, embedding models that turn text into searchable numerical meaning, vector databases that store and search that meaning, memory components that keep useful context, and external tools such as APIs or databases. As these pieces multiplied, building everything in raw code became harder to manage.
A visual abstraction layer that handled the connections reduced that surface to a manageable configuration problem.
1. The second was the emergence of agentic patterns. Agents are reasoning loops that call tools, observe results, and decide what to do next. Representing those loops in code requires architectural discipline that is error-prone and hard to debug. A canvas that makes the loop visible makes it significantly easier to reason about and correct.
1. The third was the need for rapid iteration. Agent behaviour emerges from the interaction of prompt, memory, retrieval, and tools. Changing one parameter and immediately observing the effect in the built-in test interface is a faster feedback loop than editing code, redeploying, and retesting manually.

## How Flowise will be used in this course
Flowise is the primary tool for implementing the Contigo GmbH support agent. Each sprint introduces a new capability and the corresponding Flowise configuration that implements it. By the end of the course, the Flowise canvas will contain a complete, production-informed agentic architecture; all built incrementally, one sprint at a time, using Contigo's financial services context as the business case throughout.

## Check for Understanding
>  Contigo's development team is reviewing the Flowise builder before starting the build. A junior developer suggests that because the agent will eventually need memory, retrieval, and tool connections, it must be too complex for Chatflow. How would you respond?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7f4de909-ab10-4b9d-8782-8b736cdc9179

> 💡 Takeaway: 
  Flowise turns agent architecture into something you can see, configure, and debug visually. It changes how quickly and clearly you can build one. Understanding why each component exists before connecting it on the canvas is what makes the difference between following instructions and building with intention.