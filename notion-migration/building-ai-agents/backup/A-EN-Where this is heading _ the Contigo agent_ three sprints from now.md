# Where this is heading — the Contigo agent, three sprints from now

Notion page: https://app.notion.com/p/Where-this-is-heading-the-Contigo-agent-three-sprints-from-now-3dd9418319f381c09a8ae9058ee38737
Backed up before n8n migration

You've already been introduced to Contigo's support agent and just finished the Sprint 1 memory-policy work. This page is the wider view: what the same agent needs to be able to do by the end of the module, and how the next three sprints get it there.
> 💭 Nothing is due today. This lesson is an early look at the module project so you know what you're heading toward. Sprints 2 and 3 add the pieces; Sprint 4 is when you finalise, present, and submit. If a section here reads as "I don't know how to do that yet," that's expected — you're not supposed to yet.
## What Contigo's agent needs to do by the end of the module
The agent you'll submit is the same Contigo GmbH support agent you're already building, extended step by step until it can hold its own with a real user. By Presentation Day it needs to:
- Hold multi-turn conversations with clean session isolation
- Answer from a verified knowledge base rather than the model's training data
- Invoke tools for live lookups and calculations
- Stay inside a refined system prompt that fixes role, scope, and grounding behaviour
- Refuse or de-escalate prompt injection attempts before they change the flow
- Ask for human confirmation before doing anything consequential
- Fail gracefully when a tool is unavailable
That's a production-relevant support agent — the kind Contigo's team would put in front of real clients.
## What you'll submit at the end of the module
Four artifacts, bundled together:
- A public chat URL — an active ngrok URL pointing at your locally hosted agent so a reviewer can talk to it.
- The Chatflow export — the .json that captures the canvas, node configuration, and tool definitions.
- The system prompt — the final refined version, as a single .txt or .md file.
- A one-page architecture brief — what the agent does, the decisions behind it, the failure modes you designed for, and the gap between your prototype and a production deployment.
## The arc, sprint by sprint
Sprint 1 — How Agents Remember. You just finished this one. You have a Chatflow with configured memory, a written memory policy, and a conversation-test log. This is the seed the project grows from.
Sprint 2 — Grounding Agents with Retrieval. You build a knowledge base, connect it to Contigo's agent, and learn what "evidence-aware" answers look like. The agent starts saying "I don't know" cleanly instead of guessing.
Sprint 3 — Tool Use and Agent Architectures. You add tools for live lookups, refine the system prompt, and handle tool failure and infinite loops. The agent moves from answering to doing.
Sprint 4 — Project Integration and Evaluation. You polish the Chatflow, test it end-to-end, add security guardrails and human-in-the-loop where it matters, then present and submit.
## Presentation Day and Code Clinic
The last week of the module has two live sessions, in this order.
Presentation Day is where your project is evaluated. You submit the four artifacts in advance, then give a live demo of the Chatflow to the class — including at least one conversation that stresses grounding, one that invokes a tool, and one that tries to push the agent outside scope. Your grade for the module project comes from what you submit and how you present it.
Code Clinic runs after Presentation Day. It doesn't count toward your grade — it's a technical support session for concrete questions about your own build. A retrieval that isn't ranking the way you'd expect, a system prompt that keeps drifting, a tool call that silently drops. Bring the Chatflow and specific problems, not general questions.
The exact format, agenda, and submission checklist come back in detail later in the module — you don't have to memorise anything today.
## Summary
The Contigo agent you built memory for in Sprint 1 is the same agent you'll submit at the end of the module — grounded, tool-using, guardrailed, and production-relevant. Sprint 2 adds retrieval, Sprint 3 adds tools and architecture, Sprint 4 integrates everything and ends with Presentation Day for grading and a Code Clinic afterwards for support.