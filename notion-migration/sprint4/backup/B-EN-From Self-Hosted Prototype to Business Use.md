# From Self-Hosted Prototype to Business Use

Notion page: https://app.notion.com/p/From-Self-Hosted-Prototype-to-Business-Use-3669418319f380f0a769ed717428a0cb
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Understand the four infrastructure dimensions that separate a locally running Flowise prototype from a production-ready deployment and why crossing that boundary requires more than moving a canvas to a server.

## Setting the scene
Meridian's agent is running. The canvas is clean, the security stack is understood, the end-to-end test has passed, and the presentation is being prepared. On a developer's laptop at localhost:3000, the agent handles queries reliably, retrieves accurately from Qdrant, and degrades gracefully when the HTTP Node fails.
Tomorrow, Meridian's CTO wants to make it available to the full consulting team (43 people across offices in Berlin, Warsaw, and Prague), querying the agent simultaneously throughout the working day. Within hours of that deployment, the current architecture will fail. Not because the agent logic is wrong, but because the infrastructure beneath it was never designed to handle concurrent users, persistent state across server restarts, or the observability requirements of a system that must be diagnosed when something goes wrong at 09:00 on a Monday morning.
This is the localhost problem. It is where the majority of AI agent projects fail to make the transition from prototype to production.

## Dimension 1: Hosting and scalable infrastructure
The current Flowise installation runs as a single Docker container on one machine. It uses a SQLite database for session storage and a local Qdrant Docker container for vector storage. Both work correctly for a single developer testing in isolation. Neither survives the demands of a multi-user production deployment.
- Database migration: SQLite cannot handle concurrent write operations from multiple simultaneous sessions reliably. Moving to PostgreSQL provides concurrent access, connection pooling, and transaction integrity that multi-user deployments require.
- Vector store persistence: The local Qdrant container stores vectors on a single machine. Moving to a managed Qdrant Cloud instance ensures the knowledge base is consistently available regardless of which server instance handles a given request and persists across Docker restarts.
- Container deployment: Running Flowise behind a load balancer allows the deployment to scale horizontally by adding server instances as concurrent user volume grows without changing any application or canvas logic.

## Dimension 2: Observability and monitoring
A production agent that fails at 09:00 on a Monday morning needs to be diagnosed before 09:30. On a local development instance, a developer opens the Flowise execution trace and reads it manually. At scale, across 43 concurrent users generating hundreds of traces per day, manual inspection is not viable.
- Structured telemetry: Every agent invocation must generate a structured log entry (trace ID, prompt, retrieved chunks, tool calls, response, and latency) exportable to an observability platform. Flowise supports integration with LangSmith, Langfuse, and OpenTelemetry-compatible platforms for this purpose.
- Metric dashboards: Production monitoring requires automated dashboards tracking response latency, token cost per session, HTTP Node failure rates, and retrieval quality scores. When any metric drifts outside defined bounds, an alert fires before the problem reaches users.
- Continuous evaluation: An automated evaluation pipeline runs against a standardised benchmark suite whenever the system prompt, tool descriptions, or Document Store is updated. This catches performance regressions before they affect production queries.

## Dimension 3: Security at production scale
The defence-in-depth stack (input validation, least-privilege execution, output filtering, and audit logging) was designed for a single-instance deployment. At production scale, each layer requires infrastructure-level implementation.
- Secret management: The Gemini API key currently stored via Flowise's credentials manager must be migrated to a dedicated secrets manager where it is encrypted at rest, access-controlled by role, and rotated automatically.
- Network isolation: Production agents handling confidential client data should run within a Virtual Private Cloud. This is a network perimeter that prevents external access to internal services and restricts which systems the agent can reach.
- Identity and access management: The current single-credential setup must be replaced with a proper IAM system where each consultant's identity is verified, permissions are enforced at the tool level, and all actions are attributable in the audit log.

## Dimension 4: Governance and compliance
Meridian's agent handles confidential client operational data across three EU jurisdictions. This creates regulatory obligations the prototype architecture does not address.
- Data residency: All data processed by the agent must remain within the EU. Managed infrastructure in Frankfurt or Amsterdam, rather than a developer's laptop, is required to satisfy this obligation.
- Audit trails: Every tool invocation, Flow State change, and routing decision must produce a tamper-evident log entry that can be retrieved and presented to a regulatory body if required. The Flowise execution trace is a debugging tool.
- Incident response: A production deployment requires a documented process for what happens when the agent produces an incorrect or harmful output. Include who is notified, how the incident is logged, and what the rollback procedure is.

## The prototype-to-production gap
[TABLE]
  | Dimension | Current state | Production requirement |
  | Database | SQLite: single instance | PostgreSQL: concurrent, connection-pooled |
  | Vector store | Local Qdrant Docker container | Managed Qdrant Cloud instance |
  | Hosting | Single Docker container | Load-balanced, horizontally scalable |
  | Observability | Manual execution trace inspection | Structured telemetry + automated alerting |
  | Secret management | Flowise credentials manager | Dedicated secrets manager with rotation |
  | Identity | Single API key | IAM with per-user authentication |
  | Audit trail | Flowise execution trace | Tamper-evident structured log |
  | Data residency | Developer's laptop | EU-hosted managed infrastructure |
![image]((notion-hosted file))

## Check for Understanding
>  Meridian deploys the Flowise agent to a cloud server without changing the SQLite database configuration. Within two hours of the full consulting team accessing it simultaneously, session data becomes corrupted and several consultants receive responses containing fragments of other consultants' conversation history. What is the most accurate explanation?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/6793a920-9d85-4892-ae0f-7f65261f469e


> 💡 Takeaway: 
  Building the agent is twenty percent of the work. The surrounding infrastructure is the other eighty percent. A prototype running at localhost:3000 has demonstrated that the agent logic is sound. It has not demonstrated that the system can be trusted with real client data, real concurrent users, and real regulatory obligations. 
  That demonstration requires the four infrastructure dimensions this lesson maps out and understanding them is what separates a developer who can build an agent from one who can deploy it.
