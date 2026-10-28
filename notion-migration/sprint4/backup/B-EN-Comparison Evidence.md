# Comparison Evidence

Notion page: https://app.notion.com/p/Comparison-Evidence-3669418319f3803f949be190547da288
Backed up before n8n migration

> 💡 What this assessment covers: You will produce a structured platform comparison and written justification that a technical stakeholder could use to evaluate the Flowise decision against realistic alternatives.

## Setting the scene
Meridian Consulting's CTO has reviewed the internal agent project and raised a pointed question before approving the final deployment:
> "We built this in Flowise. Why Flowise specifically? Could we have achieved the same result in Langflow, Copilot Studio, or Google AI Studio? Would any of those have been a better fit for our team and our clients?”
This is a good question. Platform decisions made at the start of a project have long-term consequences for maintenance, team capability, ecosystem compatibility, and governance overhead. A team that cannot articulate why they chose their platform is a team that has not evaluated the decision rigorously.
Your task is to produce the evidence that answers the CTO's question, not a generic platform comparison, but a specific analysis of how the Meridian consulting agent would have been built, maintained, and governed differently on each of the four platforms, and why Flowise was the appropriate choice given Meridian's actual constraints.

## Meridian's constraints: The evaluation criteria
Before comparing platforms, establish the criteria the comparison must address. These are Meridian's actual constraints from the project.
[TABLE]
  | Constraint | Detail |
  | Engineering ecosystem | Meridian's development team works primarily in JavaScript and TypeScript. There are no Python data engineers on the team. |
  | Customisation depth | The agent required custom JavaScript logic for the HTTP Node engagement status lookup and the Custom Function Node retry counter. Standard node configurations were insufficient for both. |
  | Self-hosting requirement | Meridian handles confidential client operational data. All infrastructure must be self-hosted. No external managed platform may process real client data without explicit contractual data processing agreements. |
  | Governance overhead | Meridian does not currently operate within a Microsoft 365 ecosystem. SharePoint, Teams, and Azure AD are not part of the firm's technology stack. |
  | Prototyping versus production | The agent required rapid iteration during the build phase followed by a stable, governed production deployment path. |

## Before you begin: Platform reference reading
Before completing the comparison matrix, review the following official documentation for each platform. You do not need to read everything. Focus on the architecture overview, deployment options, and integration capabilities for each one.
Langflow
- Overview and core concepts: docs.langflow.org
- Self-hosting options: docs.langflow.org/deployment-overview
Microsoft Copilot Studio
- Overview: learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
- Governance and security: learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance
- Deployment options: learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
Google AI Studio
- Overview: ai.google.dev/gemini-api/docs/ai-studio-quickstart
- Data privacy and terms: ai.google.dev/gemini-api/terms
- Difference between AI Studio and Gemini Enterprise Agent Platform: cloud.google.com/vertex-ai/generative-ai/docs/migrate/migrate-google-ai
Flowise (for reference)
- Self-hosting options: docs.flowiseai.com/configuration/deployment
> ➡️ Reading guidance: For each platform, focus on three questions:
  These three questions map directly to Meridian's evaluation criteria and are enough to complete the matrix accurately.

## Your tasks
### Task A: Complete the platform comparison matrix
Using Meridian's five evaluation criteria as your column headers, complete the matrix below by filling in how each platform performs against each criterion. Write one to two sentences per cell. Be specific enough to reflect the platform's actual architecture. 
[TABLE]
  | Platform | Engineering ecosystem | Customisation depth | Self-hosting | Governance overhead | Prototyping vs production |
  | Flowise |  |  |  |  |  |
  | Langflow |  |  |  |  |  |
  | Copilot Studio |  |  |  |  |  |
  | Google AI Studio |  |  |  |  |  |
> ➡️ Checkpoint 1 - Langflow and engineering ecosystem: Langflow is built on Python and exposes the underlying Python code of every component. Meridian's team works in JavaScript and TypeScript. Consider the practical consequence of this mismatch when custom tool logic needs to be written or modified and how this compares to writing custom JavaScript in Flowise's Custom Function Node.
> ➡️ Checkpoint 2 - Copilot Studio and governance overhead: Copilot Studio's governance advantage is that it inherits Azure Active Directory, role-based access controls, and Data Loss Prevention policies automatically. This advantage only materialises if the organisation already operates within the Microsoft ecosystem. Meridian does not use SharePoint, Teams, or Azure AD, so what does the governance value proposition actually deliver for this deployment?
> ➡️ Checkpoint 3 - Google AI Studio and prototyping versus production: Google AI Studio is designed for rapid prototyping and prompt experimentation. It does not provide VPC isolation, contractual SLAs, or the audit trail infrastructure that a consulting firm handling confidential client data requires. Consider what the migration path from AI Studio to production actually involves and compare that to the path from a self-hosted Flowise prototype to a production Flowise deployment.
> ➡️ Checkpoint 4 - Flowise limitation for Task B paragraph 3: Flowise is built on Node.js and currently runs as a single Docker container. As Meridian's consulting team grows and concurrent session volume increases, consider what the infrastructure limitations of the default single-instance deployment are and what the upgrade path looks like.

### Task B: Write the platform justification brief
Using your completed matrix as evidence, write a three-paragraph justification brief addressed to Meridian's CTO explaining why Flowise was the correct platform choice for this specific project.
#### Paragraph 1: Why Flowise fit Meridian's constraints
- Reference at least three of the five evaluation criteria. Ground every argument in Meridian's specific situation, not generic platform strengths.
- For example: "Meridian's development team works in JavaScript and TypeScript, making Flowise's Custom Function Node the natural extension mechanism for the custom retry logic and engagement status lookup the agent required, no language context switch needed."
#### Paragraph 2: Why the alternatives were less appropriate
- Address each of the three alternative platforms in turn. For each one, identify the single most significant reason it would have been a worse fit for Meridian specifically.
- For example, the Copilot Studio argument is not that it is a bad platform. It is that its governance advantages are predicated on an existing Microsoft 365 infrastructure that Meridian does not use, making its licensing cost produce no corresponding governance value for this deployment.
#### Paragraph 3: One acknowledged limitation
- A strong architectural defense acknowledges what the chosen platform does not do well. Identify one genuine limitation of Flowise for Meridian's specific use case. It is a constraint that became apparent during the build or that will become relevant as the agent scales. Explain how you would address it if the project continues beyond this sprint.

> 💡 Takeaway: 
  A platform justification that cannot be defended against alternatives is a preference. The comparison matrix forces the kind of honest, criteria-based evaluation that distinguishes an architectural decision from a default choice. Documenting why the alternatives were less appropriate is as important as documenting why the chosen platform was a good fit because it is the alternatives analysis that makes the argument credible to a technical stakeholder who could have made a different choice.