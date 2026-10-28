# Observability and system monitoring

Notion page: https://app.notion.com/p/Observability-and-system-monitoring-3689418319f38081b3d7ef6aecb87e05
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Why traditional software monitoring is insufficient for AI agents, what must be logged to make an agent debuggable, and which telemetry signals indicate a problem that requires human intervention.

## The black box problem
Contigo GmbH's agent is approaching presentation readiness. The canvas is configured, the tools are connected, the guardrails are in place, and the system prompt has been refined against real test evidence. But once the agent is made publicly accessible and handling real client interactions, a new operational question emerges: how does the team know when something is going wrong?
In traditional software, a failure produces a stack trace; a precise, deterministic record of exactly which function failed, on which line, with which input. The fix is locatable and reproducible. An AI agent fails differently. A pipeline can complete without throwing a single error and still produce a completely wrong response; one that hallucinated a regulatory figure, invoked the wrong tool, or ignored the grounding instruction entirely. No exception is raised. No alert fires. The client receives incorrect information and the monitoring dashboard shows a successful execution.
This is the black box problem. And the solution is observability; deep, structured visibility into why the agent made each decision, not just whether the pipeline ran.

## What Flowise gives you built-in
Before introducing production observability requirements, it is worth understanding what your local Flowise instance already provides.
- Chat history: Every conversation turn is logged and accessible from the Chatflow settings panel under View Messages. You can review the exact exchange between the client and the agent for any session, filtered by Session ID.
- Execution traces: When Return Source Documents is enabled on the Tool Agent node, Flowise displays which chunks were retrieved and which tools were invoked for each turn. This gives you basic visibility into the agent's tool selection and retrieval behaviour during testing.
- Analytic integrations: Flowise supports integrations with observability platforms including Arize, Phoenix, LangWatch, Langfuse, Lunary, and Opik for deeper telemetry capture. These go beyond what the built-in interface shows and are the starting point for production-grade observability.
These built-in capabilities are sufficient for the course build and the Sprint 4 presentation. They are not sufficient for a production deployment handling hundreds of concurrent client sessions.

## What must be logged
Every agent invocation in a production deployment should generate a structured trace tied to a unique trace ID. Four categories of telemetry are essential.
- Full prompt and response logging: The exact text sent to the language model and the raw response returned must be logged. This establishes the baseline of what the model was asked versus what it produced. Without this, diagnosing whether a failure was a prompt problem or a model reasoning problem is impossible. A wrong answer could originate from a poorly written system prompt, an ambiguous query, or a model reasoning failure. These are three different root causes requiring three different fixes.
- Retrieved chunk logging: When the agent queries the knowledge base, the exact document chunks returned must be logged alongside the query that triggered retrieval. A wrong answer can originate from a retrieval failure rather than a generation failure. Without logging the retrieved content, the two failure modes are indistinguishable from the output alone. If the agent cites an incorrect loan limit, the chunk log reveals whether the knowledge base contained outdated content, whether retrieval returned the wrong chunks, or whether the model ignored the retrieved content and generated from training data.
- Tool call and result logging: Every tool invocation must be logged which includes the tool name, the exact parameters passed, the response or error code returned, and the execution latency. High tool failure rates and malformed parameter patterns are both diagnosable from this data. A loan status tool that fails silently on 15% of queries is invisible without this log. With it, the failure pattern becomes identified.
- Reasoning trace logging: The agent's internal chain of thought (the Thought, Action, Observation sequence from the ReAct loop) must be captured. This allows engineers to follow the agent's logic step by step and identify exactly where its reasoning diverged from the intended behaviour. A tool routing failure that appears random in the output log often reveals a clear pattern in the reasoning trace. This is a specific phrasing in the query that consistently triggers the wrong invocation condition.

## Signals that require intervention
Continuous analysis of logged traces surfaces patterns that indicate systemic problems requiring human attention. The following signals should trigger review before they reach clients at scale.
[TABLE]
  | Signal | What it indicates | Likely root cause |
  | Retrieval returning consistently low similarity scores | Knowledge base content does not match query patterns | Chunking strategy mismatch or outdated documents |
  | Tool failure rate above 5% | Tool endpoint instability or parameter extraction errors | API reliability issue or invocation condition too broad |
  | Fallback phrase triggering on in-scope queries | Grounding instruction too restrictive or retrieval missing relevant content | System prompt over-restriction or knowledge base gap |
  | Session token cost increasing over time | Context window accumulation; sliding window not constraining effectively | Window size too large or retrieval injecting too many chunks |
  | Reasoning trace showing repeated tool re-invocations | Tool output not satisfying the model's reasoning loop | Tool description mismatch or Max Iterations too high |
  | Grounding instruction ignored in late turns | Context drift; system prompt attention diluting as history accumulates | Window size too large relative to session length |

## What observability reveals that testing cannot
The end-to-end test script will validate the agent under controlled conditions with known queries. Production observability reveals what happens under uncontrolled conditions with real client queries (the long tail of query patterns, edge cases, and failure modes) that a test script cannot anticipate.
Three categories of production failure are only detectable through observability:
- Silent degradation: The agent's response quality decreases gradually over time as the knowledge base becomes stale or query patterns shift. No single response is obviously wrong. The degradation is only visible in aggregate quality metrics tracked over weeks.
- Intermittent failures: A tool fails on 3% of invocations under specific load conditions. In testing, the tool always works. In production, the pattern is invisible without failure rate logging across thousands of sessions.
- Prompt injection variants: Novel injection phrasings that pass the moderation node's deny list appear in the reasoning trace before the system prompt catches them. Without trace logging, these near-misses are invisible and the first sign of a problem is a successful compromise rather than a detected attempt.

## Check for Understanding
>  Contigo's monitoring dashboard shows the agent pipeline completing successfully with normal latency for every session. However client feedback indicates the agent is citing incorrect loan limits in approximately one in eight interactions. What type of monitoring capability would most directly identify the source of this failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8bc261ae-db3c-4c44-b9fd-3ddd0f610db5

> 💡 Takeaway: 
  You cannot fix an AI failure you cannot see. Standard infrastructure monitoring confirms the pipeline ran. Observability confirms it ran correctly. 
  Logging full prompts, retrieved chunks, tool calls, and reasoning traces transforms an opaque agent into a debuggable system where every wrong answer has a traceable cause.
