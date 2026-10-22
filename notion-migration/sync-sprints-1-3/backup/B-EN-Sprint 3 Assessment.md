# Sprint 3 Assessment

Notion page: https://app.notion.com/p/Sprint-3-Assessment-3669418319f380f58548c32d9cd2eb7a
Backed up before n8n migration

> ⚠️ What this assessment covers: This assessment validates your ability to diagnose agent failures from execution traces, recommend the correct platform for a given business scenario, and demonstrate understanding of MCP and the broader platform landscape. All three tasks are required.
## Context
Throughout this sprint, Meridian Consulting's team has moved from debugging failing agent graphs to evaluating the platform landscape that surrounds the Flowise environment they have been building in. The sprint covered where visual agent builds fail and how to read those failures in execution traces, how open-source visual builders compare and where each fits, how enterprise platforms like Copilot Studio and the Gemini Enterprise Agent Platform provide governance that open-source tools require teams to build themselves, and how MCP reduces integration overhead by providing a universal connection standard across frameworks.
This assessment asks you to apply all of those concepts to two real-world tasks: A platform choice brief for a complex business scenario, and a knowledge quiz covering the sprint's core concepts.
## Task 1: Platform choice brief
You are an independent AI consultant. A new client has approached Meridian with the following requirements.
### Client profile: FinScope Analytics GmbH
FinScope Analytics is a Berlin-based financial data firm with 250 employees. They provide regulatory reporting tools to mid-sized banks across Germany, Poland, and the Czech Republic. Their engineering team consists of twelve senior Python data engineers who build and maintain complex data pipelines.
They want to build an internal AI agent that can answer analyst questions about their proprietary regulatory reporting datasets, summarise large structured data outputs, and route complex queries to specialist sub-agents: one focused on German regulatory frameworks, one on Polish requirements, and one on Czech requirements.
Their constraints are as follows. They self-host all infrastructure for data privacy reasons and cannot use any managed platform that processes their data externally. Their existing codebase is entirely Python. They require the ability to modify the underlying retrieval logic of their RAG pipeline beyond what any visual node exposes by default. Their budget is engineering time.
They also want to ensure that the specialist sub-agents they build can be consumed by their clients' own internal agent systems in the future, without requiring those clients to adopt FinScope's specific framework.
> 📥 Your deliverable: Write a platform choice brief of approximately 250 to 350 words. The brief must address the following four sections explicitly.
  1. Recommended platform: Name your recommended platform clearly. If your recommendation involves more than one tool, state both and explain the relationship between them.
  1. Justification: Defend your recommendation against FinScope's four specific constraints: self-hosting requirement, Python engineering team, need to modify underlying retrieval logic, and engineering-time budget structure. 
  1. Interoperability plan: FinScope wants their specialist sub-agents to be consumable by their clients' agent systems in the future. Explain which protocol or standard makes this possible and how it would be implemented in the recommended platform.
  1. Primary risk: Identify the single most significant risk of the recommended platform for FinScope's specific context.
## Task 2: Knowledge quiz
Complete all four questions below. Read each option carefully before selecting your answer.
### Question 1
>  A Flowise agent connected to fifteen tools with overlapping descriptions freezes when asked a straightforward order status query — producing a clarifying question rather than invoking the correct tool. What is the most accurate diagnosis of this failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7a9479c1-d85a-4345-ace8-08b5f778165b

### Question 2
>  A Meridian client is choosing between Flowise and Langflow for a new agent project. Their team has deep Python expertise and needs to modify the underlying ranking logic of their retrieval nodes beyond what the visual interface exposes. Which platform is most appropriate and why?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4b616869-46eb-4517-a4fa-f4ce2f86c94a

### Question 3
>  FinScope Analytics wants their specialist sub-agents — built in Langflow — to be consumable by their clients' agent systems built in different frameworks. Which standard most directly enables this cross-framework interoperability without requiring custom integration code for each client?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4256497c-593b-4d80-b988-a117454da30b

### Question 4
>  A Meridian client successfully builds and tests an agent in Google AI Studio using real employee records to validate retrieval accuracy. Before moving to production their CISO requires migration to the Gemini Enterprise Agent Platform. Which two reasons most directly justify this requirement? Select all that apply.
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/65728473-33e3-46ec-aa37-68f384afd03e

> 💡 Takeaway: 
  The platform landscape covered provides the foundation for the project integration and evaluation work. Understanding not just how to build agents but which environment to build them in, and how to diagnose them when they fail, is what separates a working prototype from a deployable system.