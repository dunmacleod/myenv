# Meet the module project — your architectural redesign

Notion page: https://app.notion.com/p/Meet-the-module-project-your-architectural-redesign-3dd9418319f3818b83d7cf5442e44803
Backed up before n8n migration

Sprint 1 introduced the pieces: agent architectures, single-agent versus multi-agent tradeoffs, the four-question framework for choosing between them, and a baseline three-node Agentflow V2 canvas as the neutral starting point.
By the end of this module, that baseline is gone. You've redesigned it into something that matches a business problem you chose — with an architecture you can defend, memory boundaries you drew deliberately, and a canvas that runs. This lesson is the first look at what the whole redesign looks like when it's assembled.
> 💭 Nothing is due today. This lesson is an early look at the module project so you know what you're heading toward. Sprints 2 and 3 add the pieces; Sprint 4 is when you integrate, present, and submit. If a section here reads as "I don't know how to do that yet," that's expected — you're not supposed to yet.
## The project you'll be shaping
Unlike a fixed running case, this module's project is built on a business problem you choose yourself. It might be an internal support agent for a firm you've worked at, a research assistant for a domain you know, an ops-side triage system, a specialist advisor — the shape doesn't matter as much as the specificity. A vague brief produces a vague redesign; a narrow, real brief produces a defensible one.
Your job across the module is to take the baseline Agentflow V2 canvas and turn it into an architecture that fits that brief. Not a rebuild from scratch — a deliberate redesign, defensible against the alternatives you rejected.
## What you'll submit at the end of the module
Four deliverables that build on each other, plus the integration on the canvas that turns them into something that runs:
- Architecture decision brief — one page: the decision, the pattern, inputs and outputs, the three pillars, the rejected alternative, and the conditions under which you'd revisit the decision
- Multi-agent design diagram — every agent named, information flow shown, routing decision points marked, information boundaries called out, at least one fallback path
- Memory and state architecture specification — memory boundary map (shared/private/conditional with persistence scope), what must not persist, state recovery design, failure isolation assessment
- The redesigned Flowise canvas — implementing the design, with a test record showing it behaves the way the specification says it should
## The arc, sprint by sprint
Sprint 1 — Agent architecture foundations. You just finished this one. You know the patterns, the tradeoffs, and how to make an architecture decision defensibly. Your first deliverable — the decision brief — comes out of this sprint's work.
Sprint 2 — Multi-agent system design. You learn when multi-agent earns its complexity, how to define specialisations and boundaries, and how to draw a design diagram that a reader can actually understand. Your second deliverable takes shape here.
Sprint 3 — Memory and state architecture. You draw memory and state boundaries deliberately — what's shared, what's private, what must never persist — and design failure isolation so one agent's failure doesn't corrupt shared state. Your third deliverable takes shape here.
Sprint 4 — Project integration. You implement the design on your Flowise canvas, test it against the failure modes you designed for, then present and submit.
## Presentation Day and Code Clinic
The last week of the module has two live sessions, in this order.
Presentation Day is where your project is evaluated. You submit the four deliverables in advance, then present the redesign live — the decision, the diagram, the memory boundaries, the canvas running end-to-end. You defend the pattern against the alternative you rejected. Your grade for the module project comes from what you submit and how you present it.
Code Clinic runs after Presentation Day. It doesn't count toward your grade — it's a technical support session for concrete questions about your own build. A routing decision that isn't landing where you expected, a memory boundary that leaks in a way you didn't design for, a failure isolation path that doesn't recover cleanly. Bring the canvas and specific problems, not general questions.
The exact format, agenda, and submission checklist come back in detail later in the module — you don't have to memorise anything today.
## Summary
The baseline canvas from Sprint 1 becomes the redesigned architecture you present at the end of the module — chosen deliberately, drawn diagrammatically, bounded in memory, and running. Sprint 2 gets you the design, Sprint 3 gets you the memory and state boundaries, Sprint 4 is when you present it on Presentation Day, with a Code Clinic afterwards for any deeper technical support.