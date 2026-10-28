# Redesigning the baseline project agent

Notion page: https://app.notion.com/p/Redesigning-the-baseline-project-agent-3849418319f38008b808db05b9e4f487
Backed up before n8n migration

The Vela Systems canvas has been the teaching vehicle across the whole module. Every concept, every design decision, every failure mode was first worked through on that shared canvas so the architecture principles were visible before you had to apply them on your own. This lesson is where that scaffolding comes away.
What you are working with now is your own project canvas: the archetype you chose (Router, Coordinator, or Evaluator) built on a domain you defined, reflecting the architecture brief you wrote in Sprint 1, the multi-agent design you produced in Sprint 2, and the memory and state specification you completed in Sprint 3. Those three documents are the design you are now implementing. The job in this lesson is to apply them systematically: audit the current state of the canvas against what the design specifies, identify every gap, and close each one, then verify that the failure modes from the previous lesson do not exist in your implementation.
By the end of this lesson, your canvas should reflect the full architecture you designed across Sprints 1 through 3. What remains for your presentation is a demonstration and a defense, not further design work.
> 💡 In this lesson, you will apply the architecture and memory and state patterns from Sprints 1–3 to redesign your project agent by closing the gap between the design you specified and the canvas that currently exists.

## Before you open Flowise
Export your current canvas as a JSON backup before you change anything. In self-hosted Flowise, this is done through the canvas menu: Export → save the file as [your-canvas-name]__pre-lesson-26-backup.json. If anything in the redesign goes wrong, you can reimport this file and return to the current state.

## What you are implementing
The three sprint deliverables are your implementation specification. Pull them up before you audit the canvas.
- Sprint 1: Architecture decision brief. Single-agent or multi-agent decision, with justification. The brief names your chosen archetype and the domain.
- Sprint 2: Multi-agent design diagram. Agent roles, responsibilities, coordination approach, and the rejected alternative.
- Sprint 3: Memory and state architecture specification. What is shared, what is private, what must never persist, and how state recovers after failure.
If any of these documents is incomplete, that is the first thing to address. The implementation cannot be audited against a specification that does not fully exist. Fill in any missing sections before continuing.

## The redesign in four stages
Work through the four stages in order. Each stage has an audit question, a set of actions if the audit finds a gap, and a checkpoint to confirm the stage is complete before moving on.
### Stage 1: Architecture
Audit question: Does the current canvas reflect the archetype you chose in your Sprint 1 brief?
Open your canvas. Look at the node structure and compare it against the brief.
[COLUMN_LIST]
  [COLUMN]
    For The Router: 
    - The canvas should have a Classifier node (or an LLM Node / Condition Agent Node acting as a classifier), a Condition Node reading query_type from Flow State, and at least two specialist Agent Nodes with clearly distinct system prompts and non-overlapping responsibilities. A Direct Reply Node closes each routing path.
  [COLUMN]
    For The Coordinator: 
    - The canvas should have a supervisor LLM Node that delegates tasks explicitly, at least two specialist Agent Nodes operating as workers, and a loop structure (Loop Node and Condition Node) that returns incomplete work to the supervisor rather than passing it straight to reply.
  [COLUMN]
    For The Evaluator: 
    - The canvas should have a generator Agent Node, a separate evaluator Agent Node with a distinct evaluation prompt, a Human Input Node that gates approval, and a Loop Node that returns rejected output to the generator.
If the canvas does not match the archetype: add the missing nodes, configure their system prompts, and wire the connections before moving to Stage 2. Do not skip this even if the gap seems small.
Stage 1 checkpoint:
- [ ] Does the node structure on the canvas match the archetype named in your Sprint 1 brief?
- [ ] Does each agent node have a system prompt that defines its responsibilities clearly and without overlap with the other agents?
- [ ] Are all connections between nodes complete with no dangling outputs, no inputs left unwired?

### Stage 2: Memory boundaries
Audit question: Does the canvas enforce the memory boundaries specified in your Sprint 3 document?
Open your Sprint 3 memory and state architecture specification. Find the section that defines what is shared and what is private.
Work through each item in that section and locate it on the canvas. For each shared key, identify which node writes it and which nodes read it. Confirm this matches the write ownership you specified. For each private item, confirm it exists only in the context window of the agent that owns it and is not written to Flow State where other agents could read it.
If a key that should be private is written to Flow State: remove it from the Update Flow State configuration on that node. If a key that should be shared is not written to Flow State at all: add it to the Update Flow State configuration of the owning agent.
Three checks to run after adjusting boundaries:
- Open the Update Flow State configuration on each agent node. List every key it writes. Compare that list against your Sprint 3 specification. Any key not in the specification is either a gap in the specification (update it) or an undocumented write that should not be there (remove it).
- Confirm that no agent reads a Flow State key it does not own, except keys explicitly designated as shared.
- Confirm that query_type or whatever key your Classifier or coordinator writes to signal routing decisions is reset to null before a new query value is written. If it is not reset, a failed write in the Classifier leaves a stale value that the Condition Node reads as valid.
Stage 2 checkpoint:
- [ ] Does every Flow State key on the canvas appear in your Sprint 3 specification? Are there any undocumented keys?
- [ ] Is write ownership enforced or is it one designated node per key?
- [ ] Is query_type (or your equivalent routing key) reset before each new write?

### Stage 3: State handoff and recovery
Audit question: Does the canvas implement the state handoff and recovery design from your Sprint 3 specification?
Open your Sprint 3 specification. Find the state handoff section and the recovery section.
[COLUMN_LIST]
  [COLUMN]
    State handoff: For each handoff between agents, confirm the canvas passes the required context through Flow State. The receiving agent should be able to run correctly from the Flow State values available to it at the moment it starts, without re-querying information the previous agent already retrieved. If the handoff contract is incomplete, add that key to the Update Flow State configuration of the sending agent.
  [COLUMN]
    Recovery: Your Sprint 3 specification defined a safe state. The specific Flow State values the canvas returns to when a specialist agent fails. Confirm the canvas implements this. In Agentflow V2, recovery after failure is designed through the flow's error handling configuration and the Condition Node's fallback path. If a failure in Specialist A leaves query_type: "support" in Flow State without a completion signal, a recovery path should detect the missing completion signal, reset query_type to null, and route back to the Classifier.
If no recovery path exists on the canvas, design and implement one now. The minimum recovery path is a Condition Node fallback that fires when a completion signal key is absent, resets the routing key, and returns control to the Classifier or coordinator.
Stage 3 checkpoint:
- [ ] Does each agent-to-agent handoff pass the required Flow State keys as specified in Sprint 3?
- [ ] Does the canvas have an explicit recovery path for at least one specialist agent failure?
- [ ] Does the recovery path reset the routing key before returning control, not after?

### Stage 4: Failure mode safeguards
Audit question: Does the canvas implement safeguards for the failure modes identified in the previous lesson?
Review the five safeguard decisions you produced in the previous lesson. For each one, confirm whether it applies to your canvas, not every Vela failure mode will apply to every archetype, but most will have a structural equivalent.
Work through each applicable safeguard and confirm it is implemented:
- Reset timing for routing keys. Is query_type (or your equivalent) reset before every new write? (Stage 2 addressed this, confirm it is still the case after all other edits.)
- Cross-query key contamination. Are any Flow State keys used to carry intermediate results across queries within a session? If yes, does each one reset at the start of a new query, not at the end of the previous one?
- Persistent store write rules. If your canvas writes to a persistent store (Qdrant or equivalent), does the write configuration exclude session-specific content?
- Session-namespaced keys. If your canvas is expected to run with multiple concurrent users (relevant if you chose the Router or Coordinator archetype), are routing and intermediate keys namespaced by session ID rather than written as global keys?
- Diagnostic message accuracy. If your recovery path produces a user-facing message, does that message derive its content from the actual Flow State value at runtime, not from hardcoded text that could describe the wrong agent?
If a safeguard applies and is not implemented: implement it now. If a safeguard does not apply to your archetype, note why in one sentence. This will be part of your defense during the presentation.
Stage 4 checkpoint:
- [ ] Have you confirmed or implemented each applicable safeguard from the previous lesson?
- [ ] For safeguards that do not apply to your canvas, have you noted the reason?
- [ ] Does the canvas still match the Stage 1 and Stage 2 state after the Stage 4 edits? (Safeguard implementations sometimes introduce new connections or key writes. Re-check that Stage 2 boundaries are still correct.)

## Watch out for
- Editing the backup file instead of the live canvas. Open the correct file in Flowise before making any changes. If you are unsure which is which, look at the canvas description field. The live canvas should have the architecture summary you wrote in Sprint 1.
- Adding nodes that are not in your Sprint 3 specification without updating the specification. Every new Flow State key or agent node added during Stage 4 should be reflected in the specification before your presentation. A canvas that has diverged from its specification cannot be defended coherently.
- Skipping the reset check at Stage 2 because "the Classifier always runs before the Condition Node." The Classifier always runs before the Condition Node in a working session. In a failed session, it may not. The reset protects the failed case, not the working one.
- Treating the recovery path as optional for architectures with only one specialist. A Router with three specialists has three failure surfaces. An Evaluator with a generator and an evaluator agent has two. Even a minimal multi-agent canvas needs at least one recovery path.
- Closing the canvas after Stage 2 and before Stage 3 without exporting. Export after each stage. A mid-session Flowise crash without a stage checkpoint means repeating work.

## Checkpoints
As you work through the four stages, use these questions to verify your state before moving on from each one:
- [ ] After Stage 1: Can you draw the node structure of your canvas from memory and match it to your Sprint 1 archetype choice? If the answer is uncertain, the architecture is not fully implemented.
- [ ] After Stage 2: If you removed all node labels from the canvas and looked only at the Update Flow State configurations, could you reconstruct which agent owns which key? Write ownership should be readable from the configuration, not implied by node position.
- [ ] After Stage 3: If Specialist A (or whichever specialist is most central to your design) failed completely after the Classifier had already written the routing key, what would happen? Walk through the sequence. The answer should not be "the session hangs" or "the user receives an unhandled error."
- [ ] After Stage 4: Export the canvas as [your-canvas-name]__post-lesson-26.json. This is your implementation checkpoint. Keep both the pre-lesson backup and this export. You will need the post-lesson export as the starting state for the next lesson.

>  
  ### 🔥 Using AI when you get stuck
  If you are at a stage where you know what the canvas should do but cannot work out the Flowise configuration to make it happen, use AI as a configuration helper, not as a design substitute:
  1. Describe the specific behaviour you need: "When the Update Flow State step on the Classifier node fails to execute, I need the Condition Node to detect this and route to a fallback path rather than routing based on a stale value."
  1. Specify the tool: "I am using self-hosted Flowise Agentflow V2."
  1. Ask for the configuration approach: "What is the correct way to configure this in Agentflow V2, which node handles the detection, and where does the fallback path connect?"
  Do not ask AI to describe what your canvas should contain that is the Sprint 3 specification you already wrote. Use AI to close the gap between the specification and the Flowise configuration that implements it.

## Summary
The four stages of this lesson close the gap between the design you specified across Sprints 1 through 3 and the canvas that implements it. 
1. Architecture stage: The node structure must match the archetype.
1. Memory boundaries: Write ownership and scope must match the Sprint 3 specification. 
1. State handoff and recovery: The canvas must pass context correctly between agents and handle failure without hanging. 
1. Failure mode safeguards: The specific protections you designed in the previous lesson must be present in the implementation.
The canvas you export at the end of this lesson is the implementation checkpoint. In the next lesson, you will validate that the implementation actually solves the limitations of the baseline, not by reading the specification, but by running the canvas against targeted test scenarios and checking whether it behaves the way the design predicted.