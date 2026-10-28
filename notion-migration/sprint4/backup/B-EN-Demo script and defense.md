# Demo script and defense

Notion page: https://app.notion.com/p/Demo-script-and-defense-3669418319f380609932d22a0b538800
Backed up before n8n migration

> 💡 What this assessment covers: This assessment validates your ability to present a working agent to a non-technical stakeholder by demonstrating its core capabilities through a structured demo script and formally defend the platform decisions behind it against enterprise constraints. Both tasks are required.
## What this assessment covers
Meridian Consulting's agent has been built, refined, secured, end-to-end tested, and audited. The platform decision has been documented and defended on paper. The final step before deployment approval is the stakeholder presentation.
Meridian's CIO has allocated thirty minutes for the review. The first ten minutes are a live demonstration of the agent's capabilities. The remaining twenty are a formal architectural defense. The CIO wants to understand not just that the agent works, but why it was built the way it was and whether that architecture can be trusted handling confidential client operational data.
This is the moment where technical decisions become organisational commitments. A demo that shows a clean happy path without addressing failure handling does not build confidence. A defense that cannot explain the platform choice against specific enterprise constraints does not earn approval. Both must be precise, honest, and grounded in the agent's actual architecture.
### Task 1: Write the demo script
Write a structured five-turn conversation script that presents Meridian's Agentflow v2 to the CIO during the live demonstration. The script must demonstrate all five of the following capabilities in sequence within a single continuous session.
#### Turn 1 - Knowledge retrieval
The first turn must require the agent to retrieve content from the meridian-knowledge Document Store. The query must be specific enough that the agent cannot answer from Gemini's training data alone. It must retrieve from the ingested documents.
Format Turn 1 as:
- User: the consultant's query
- Agent Thought: the agent's internal reasoning about which path to take and why the knowledge base is the correct source
- Agent Output: the response delivered to the user including a brief indication of which document section was retrieved
#### Turn 2 - Cross-turn context retention
The second turn must demonstrate that the agent retains context from Turn 1 without re-querying the Document Store. The query must build on information established in Turn 1 in a way that requires session memory to answer correctly.
Format Turn 2 as:
- User: the consultant's follow-up query
- Agent Thought: the agent's reasoning confirming context is available from Turn 1 without a new retrieval call
- Agent Output: the response delivered to the user applying Turn 1 context to the new question
#### Turn 3 - Live data lookup with Human Input approval
The third turn must require the agent to invoke the HTTP Node for a live engagement status lookup. The query must contain a specific account reference. The agent must pause at the Human Input Node and present the retrieved data for approval before formatting and returning it.
Format Turn 3 as:
- User: the consultant's status query
- Agent Thought: the agent's reasoning identifying this as a live data request rather than a knowledge query
- Human Input Node pause: the message presented to the consultant with the raw data and the Proceed/Reject prompt
- Agent Output (after Proceed): the formatted engagement summary returned to the consultant
#### Turn 4 - Graceful failure handling
The fourth turn must demonstrate the agent's behaviour when the HTTP Node returns an error. Before writing this turn, temporarily change the HTTP Node URL to an invalid endpoint to simulate a failure, then restore it after.
Format Turn 4 as:
- User: a status query for a different account
- Agent Thought: the agent's reasoning identifying the HTTP error and applying the fallback instruction
- Agent Output: the fallback response by acknowledging the information is temporarily unavailable and offering a specific next step with no fabricated engagement details
> ⚠️ After writing and testing this turn, restore the HTTP Node URL to https://jsonplaceholder.typicode.com/todos/1 and save the canvas before proceeding.
#### Turn 5 - Scope boundary
The fifth turn must demonstrate the agent's behaviour at the edge of its authorised scope. Send a query that a consultant might reasonably ask but that falls outside the agent's defined capabilities.
Format Turn 5 as:
- User: the out-of-scope query
- Agent Thought: the agent's reasoning recognising the query is outside its authorised scope
- Agent Output: the fallback phrase with a constructive next step with no fabricated response, no attempt to answer outside the defined boundaries
### Task 2: Write the platform defense
Following the demo, the CIO raises the following concern:
> "This looks capable. But I need to understand the governance picture before I approve production deployment. We handle confidential client operational data across three EU jurisdictions. I need to know: can this run in a properly governed environment? And a colleague has suggested we rebuild this in Microsoft Copilot Studio because of its enterprise governance features. What is your recommendation?"
Write a formal platform defense that addresses the CIO's concern directly. The defense must cover the following three arguments in order.
Argument 1 - Why self-hosted Flowise is the correct production path
Explain what the current self-hosted Docker prototype provides and what it does not yet provide for production. Reference the four infrastructure dimensions (hosting, observability, security at scale, and governance). Explain why the migration from the current Docker prototype to a production-grade Flowise deployment is a well-defined path rather than a rebuild where the canvas logic, system prompt, Document Store configuration, and routing architecture all carry forward. Only the infrastructure layer changes.
Argument 2 - Why the current Gemini API setup needs a production upgrade
The current build uses the Gemini API free tier via Google AI Studio credentials. Explain the data handling implications of the free tier for a consulting firm processing confidential client operational data. Reference the specific concern: on the free tier, data sent to the API may be used by Google to improve its models. Explain what the upgrade path is (moving to a paid Gemini API tier or Gemini Enterprise Agent Platform) and what that provides in terms of data privacy, SLAs, and GDPR compliance.
Argument 3 - Why Microsoft Copilot Studio is the wrong choice for Meridian
Address the CIO's colleague's suggestion directly. Your argument must cover three points specifically:
- Copilot Studio's governance advantages are predicated on an existing Microsoft 365 ecosystem (Azure AD, SharePoint, Teams) that Meridian does not use. The inherited governance controls provide no value to an organisation without that infrastructure.
- Copilot Studio's connector ecosystem is optimised for Microsoft tools. Integrating with Meridian's custom internal APIs and the Gemini model already validated in the build requires custom connector development that negates the low-code governance benefit.
- Rebuilding in Copilot Studio means abandoning three sprints of validated canvas logic such as the Document Store configuration, the Condition Agent Node routing, the retry logic, and the Human Input approval checkpoint and then rebuilding it from scratch in an unfamiliar platform immediately before deployment. The risk profile of that decision is not justified by the governance benefit, which does not materialise without a Microsoft ecosystem.
> 💡 Takeaway: The demo script demonstrates that the agent works under realistic conditions including failure conditions. The platform defense demonstrates that the architectural decisions behind it were deliberate, evidence-based, and defensible against enterprise constraints. Together they represent the two capabilities that matter most when an AI agent moves from a project to a product: the ability to show it working and the ability to explain why it was built the way it was.
#### This is the final campus lesson of Course 2B. The live sessions that follow (Presentation Day and the Code Clinic) are where the agent is refined to its final state and presented to a stakeholder audience. Everything built across four sprints, from the minimal three-node baseline in Sprint 1 to the fully orchestrated, retrieval-augmented, human-supervised agent in Sprint 3, has been leading to this moment.