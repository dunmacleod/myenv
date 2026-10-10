# Meet the module project — your extended, connected agent system

Notion page: https://app.notion.com/p/Meet-the-module-project-your-extended-connected-agent-system-3dd9418319f381f8852de27c334dfb14
Backed up before n8n migration

Sprint 1 introduced how agents talk — to each other and to tools. Structured messaging, handoff contracts, MCP as agent-to-tool integration, and A2A awareness for cross-agent interoperability.
By the end of this module, you've taken a baseline project agent and extended it into a connected, resilient, orchestrated system that handles failures without falling over. This lesson is the first look at what "extended" actually means and how the pieces fit.
> 💭 Nothing is due today. This lesson is an early look at the module project so you know what you're heading toward. Sprints 2 and 3 add the pieces; Sprint 4 is when you integrate, present, and submit. If a section here reads as "I don't know how to do that yet," that's expected — you're not supposed to yet.
## The project you'll be extending
You start from a baseline project agent — a single-agent workflow that uses an MCP-connected tool to do one thing well. That's the seed. Across the module you extend it into a multi-agent system where specialist agents own their part of the request, hand off cleanly, call external tools through MCP, and recover from timeouts and tool failures without corrupting shared state.
The business domain the extended system serves is one you pick — a support agent for a real firm, a research assistant, a triage system, a specialist advisor. Same principle as its first module: a narrow, real brief produces a defensible system; a vague one doesn't.
## What you'll submit at the end of the module
Four deliverables that build on each other, plus the extended canvas that turns them into something that runs:
- Sprint 1 deliverable — the structured communication and handoff design for your project (message passing contracts, MCP integration for one tool, awareness of the A2A layer)
- Sprint 2 deliverable — the orchestration design for your project agent (sequential or parallel patterns, routing decisions, when the orchestrator hands off vs decides itself)
- Sprint 3 deliverable — the resilience layer applied to your project (timeouts, retries, fallback orchestration, circuit-breaker-style handling at the design level)
- Sprint 4 deliverable — the connected, extended canvas end-to-end: intake agent, specialist agents, orchestration, MCP tools, retry and fallback logic, evaluated against the failure modes you designed for
## The arc, sprint by sprint
Sprint 1 — Communication and integration protocols. You just finished this one. You know how structured messages travel between agents, how MCP connects agents to tools, and where A2A fits. Your first deliverable comes out of this sprint's work.
Sprint 2 — Orchestration patterns. You learn when orchestration earns its complexity, the difference between orchestration and choreography, and how sequential vs parallel patterns change what breaks and how. Your second deliverable takes shape here.
Sprint 3 — Resilience and failure handling. You add timeouts, retries, fallback orchestration, and circuit breakers at the design level. You learn to diagnose why orchestrations fail without waiting for them to fail in production. Your third deliverable takes shape here.
Sprint 4 — Project integration. You connect all the agents in your project, run end-to-end failure analysis, debug across the protocol and orchestration layers, evaluate the extended agent, then present and submit.
## Presentation Day and Code Clinic
The last week of the module has two live sessions, in this order.
Presentation Day is where your project is evaluated. You submit the four deliverables in advance, then present live — the architecture, the orchestration pattern, the resilience choices, the canvas running end-to-end on realistic user requests. You defend the pattern against the alternative you rejected. Your grade for the module project comes from what you submit and how you present it.
Code Clinic runs after Presentation Day. It doesn't count toward your grade — it's a technical support session for concrete questions about your own build. An orchestration path that isn't routing where you expected, a retry loop that never gives up, a handoff contract that keeps dropping context. Bring the canvas and specific problems, not general questions.
The exact format, agenda, and submission checklist come back in detail later in the module — you don't have to memorise anything today.
## Summary
The baseline single-agent workflow becomes an extended, connected, orchestrated system you present at the end of the module. Sprint 2 gives you the orchestration design, Sprint 3 gives you the resilience layer, Sprint 4 integrates everything and ends with Presentation Day for grading and a Code Clinic afterwards for support.