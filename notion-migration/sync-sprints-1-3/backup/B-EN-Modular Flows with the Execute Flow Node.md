# Modular Flows with the Execute Flow Node

Notion page: https://app.notion.com/p/Modular-Flows-with-the-Execute-Flow-Node-37d9418319f38001b832e57f35275540
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Understand what the Execute Flow Node does, why modular flow design matters, and how to configure it correctly.

## Setting the Scene
Meridian's canvas has grown significantly over three sprints. The Meridian Base Agent now handles knowledge retrieval, intent routing, live data lookup, retry logic, iteration, and human approval checkpoints, all in a single canvas.
As agent workflows grow in complexity, a new problem emerges. Logic that is useful in one flow frequently needs to be available in another. The engagement briefing logic built is a good example. It is useful as a standalone weekly tool and also as a capability the base agent should be able to invoke on demand. Rebuilding the same logic in every flow that needs it is not maintainable. When the briefing logic changes, every copy needs updating. When a bug is found, it needs fixing in multiple places. This is the problem that modular flow design solves.

## What the Execute Flow Node does
The Execute Flow Node functions as a sub-workflow caller, promoting modular design and reusability of logic. It allows the current workflow to trigger a separate pre-existing workflow, pass an initial input to it, optionally override specific configurations of the target flow for that particular run, and receive its final output back into the calling workflow to continue processing.
![image]((notion-hosted file))
In practical terms: One flow invokes another, waits for it to complete, and uses its output as if it were produced locally. The calling flow does not need to know how the sub-flow works internally, only what input it expects and what output it returns.

## Why this matters for Meridian
Meridian's development team can use this pattern to:
- Invoke the Meridian Engagement Briefing flow from the base agent without rebuilding the iteration logic
- Build specialist sub-flows for Germany, Poland, and Czech Republic regional queries and invoke the correct one based on routing
- Centralise complex logic in one place and update it once when requirements change
When the sub-flow is updated, the calling flow benefits automatically without requiring any changes to the Execute Flow Node configuration. This is the core maintenance advantage of modular design.

## How to configure the Execute Flow Node
[TABLE]
  | Field | Purpose |
  | Select Flow | Choose the target Agentflow v2 or Chatflow from the dropdown list of all flows in your Flowise instance |
  | Input | The data passed to the sub-flow as its starting input — use plain text or a Flow State variable |
  | Base URL | The URL of the Flowise instance hosting the target flow — required when running in Docker, set to http://host.docker.internal:3000 |
  | Return Response As | Whether the sub-flow output is treated as a User Message or Assistant Message in the calling flow |
  | Update Flow State | Optionally store the sub-flow output in a Flow State key for downstream nodes to read |
> 💡 Docker users: The Execute Flow Node cannot use localhost to call another flow because both flows run inside the same Docker container. Always set the Base URL to http://host.docker.internal:3000 when running Flowise locally via Docker.

## How it fits into the Meridian canvas
The Execute Flow Node sits on a dedicated routing path. The Condition Node detects briefing requests by keyword and routes them to the Execute Flow Node, which invokes the Meridian Engagement Briefing sub-flow and returns the result to a Direct Reply Node.

The existing knowledge and status paths remain completely unchanged. The Execute Flow Node adds a third path without touching anything already built.

## Known platform limitation
In complex canvases with multiple HTTP paths, the Execute Flow Node's Input field may auto-populate with variable references from other paths and revert on save. This is a known Flowise behaviour in certain canvas configurations. If you encounter this on your canvas, the full implementation is demonstrated in the live session using a clean canvas where this conflict does not occur. The configuration steps above are correct. The issue is specific to canvases with conflicting node ID bindings, not to the Execute Flow Node itself.

## Check for Understanding
>  A developer updates the Meridian Engagement Briefing sub-flow to include five engagement records instead of three. What needs to change in the Meridian Base Agent canvas?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/605eb436-34c0-4f26-8904-1abd637cf0cf

> 💡 Takeaway: 
  The Execute Flow Node converts isolated Agentflow v2 builds into reusable components. Logic built once can be invoked from any other flow without rebuilding. When the sub-flow changes, every caller benefits automatically. As Meridian's canvas grows, modular sub-flows keep individual components focused, independently testable, and maintainable without cascading changes across the entire build.