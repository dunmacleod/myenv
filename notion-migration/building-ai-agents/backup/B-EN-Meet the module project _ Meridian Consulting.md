# Meet the module project — Meridian Consulting

Notion page: https://app.notion.com/p/Meet-the-module-project-Meridian-Consulting-3dd9418319f381cb9acbf9fe98cf6f35
Backed up before n8n migration

Sprint 1 was you and Flowise. Installing it locally, setting up the Gemini and OpenRouter credentials, building your first Agentflow v2 canvas, learning what a Start Node → Agent Node → Direct Reply Node actually does when you send it a message.
By the end of this module, the same platform is running an internal agent for a real consulting firm. This lesson is the first look at who they are and what the agent needs to do.
> 💭 Nothing is due today. This lesson is an early look at the module project so you know what you're heading toward. Sprints 2 and 3 add the pieces; Sprint 4 is when you refine, present, and submit. If a section here reads as "I don't know how to do that yet," that's expected — you're not supposed to yet.
## The company you'll be building for
Meridian Consulting is a mid-sized professional services firm. Consultants spend a chunk of every week digging through internal handbooks, policy documents, and live engagement data to answer their own procedural questions — "what's our sub-contracting policy for public-sector work?", "what stage is the Kessler engagement at?", "who signs off on scope changes over €50k?".
The firm wants an internal support agent that answers from Meridian's own material rather than the model's training data, looks up live engagement status when asked, pauses for human approval before it does anything consequential, and stays inside the scope Meridian set for it. You'll build that agent on a single canvas — the Meridian Base Agent — and grow it capability by capability across the sprints.
## What you'll submit at the end of the module
The canvas you refine and submit is the same one you're already building. What's being assessed is whether it behaves the way you say it behaves, and whether you can explain the design. The final submission includes:
- The refined Meridian Base Agent canvas — exported from Flowise
- The final system prompt — role, scope, hard boundaries, escalation behaviour, capability routing
- The Meridian Document Store — populated with the source material, retrieval verified
- Test evidence — end-to-end runs across separate sessions covering grounding, tool use, prompt injection attempts, and graceful failure
- A short written brief — why this canvas over the alternatives, on the criteria a business would actually care about
## The arc, sprint by sprint
Sprint 1 — Setting up Flowise and the Gemini stack. You just finished this one. Flowise runs locally, the API keys work, and you have a first agentflow that speaks.
Sprint 2 — Memory, retrieval, and tools in Flowise. You build the Document Store, connect it to the agent, add conditional routing between capabilities, and connect an HTTP Node for live data lookups.
Sprint 3 — Debugging agents and the platform landscape. You add human approval checkpoints, iteration and retry logic, custom logic nodes, and sub-flows. You learn to read and debug an agent graph. You get a sense of when Flowise is the right tool and when it isn't.
Sprint 4 — Project finalisation and comparison. You harden the canvas end-to-end, refine the system prompt one last time, run comparison evidence against alternatives, then present and submit.
## Presentation Day and Code Clinic
The last week of the module has two live sessions, in this order.
Presentation Day is where your project is evaluated. You submit the canvas package in advance, then run a live demo — including at least one conversation that stresses grounding, one that invokes a tool, one that trips the approval gate, and one that tries to push the agent outside scope. You defend the platform choice against a named alternative. Your grade for the module project comes from what you submit and how you present it.
Code Clinic runs after Presentation Day. It doesn't count toward your grade — it's a technical support session for concrete questions about your own build. A retrieval that isn't ranking the way you'd expect, a Condition Agent Node that keeps routing wrong, a Human Input Node that isn't pausing where you want it to. Bring the canvas and specific problems, not general questions.
The exact format, agenda, and submission checklist come back in detail later in the module — you don't have to memorise anything today.
## Summary
The Meridian Base Agent you started in Sprint 1 is the same canvas you'll present at the end of the module — grounded in a Document Store, routing between specialist capabilities, gated by human approval, and defensible against alternatives. Sprint 2 adds knowledge and tools, Sprint 3 adds oversight and debug muscle, Sprint 4 is when you present it on Presentation Day, with a Code Clinic afterwards for any deeper technical support.