# Memory ownership and what must never persist

Notion page: https://app.notion.com/p/Memory-ownership-and-what-must-never-persist-3849418319f380f39b29edf931c224d2
Backed up before n8n migration

Petra had flagged it in the weekly ops review. A client from the Netherlands had asked the Vela agent about a delivery delay and in the process had mentioned the name of their logistics contact and a reference number from an internal procurement system. Standard support query. The agent had handled it correctly. But two sessions later, a different member of the same client's team had asked an unrelated question about supplier coordination and the agent had volunteered the logistics contact's name and the procurement reference in its response. It hadn't been asked. It had remembered.
The information hadn't been marked as sensitive. Nobody had decided it should persist. It had simply been written to allMessages during the first session and surfaced again in the second because the memory configuration allowed it.
This is the ownership problem. In the previous lesson, the question was which agents should be allowed to read shared memory. This lesson adds a second layer: who is responsible for what gets stored, and what categories of information should leave no trace beyond the turn that handled them.
> ➡️ allMessages is a memory type setting on the Agent Node in Flowise Agentflow V2. It tells the agent to pass the full conversation history into the model's context window on each execution.

## Memory ownership in a multi-agent system
In a single-agent system, ownership is obvious. One agent writes, one agent reads, and the same agent is responsible for both. In a multi-agent system, the lines blur. The LLM Classifier writes query_type to $flow.state. The Commercial Agent reads it. Who owns that key? Who is responsible for clearing it if it becomes stale? Who decides whether it should persist to the next session?
Ownership is not automatically assigned by the node that writes a value. It is a design decision. Without an explicit ownership decision, every piece of information in the system is effectively owned by nobody — which means nobody clears it, nobody audits it, and nobody notices when it causes a problem.
A useful working definition: the agent that writes a value to shared memory owns that value until another agent is explicitly designated as the consumer. 
The owning agent is responsible for three things:
- Writing the value in the correct format at the correct time
- Documenting what the value represents and what a downstream agent should do with it
- Not writing values that should remain private to its own context
That last point is what Petra's flag exposed. No agent had been designated as the owner of the logistics contact and procurement reference. They had been written to allMessages as a side effect of a normal conversation, not as a deliberate architectural decision.

## What must never persist
Some categories of information should not survive the agent turn that handled them. The test is not whether the information is technically sensitive. It is whether a future agent reading it could use it correctly, or whether the presence of that information creates a risk that outweighs the benefit of retaining it.
Four categories that routinely should not persist:
- Ephemeral identifiers. Temporary codes, one-time tokens, session reference numbers, and similar values that are only valid for a specific moment in time. If an agent retains a session token past its expiry and passes it to a downstream agent, the downstream agent may attempt to use an invalid credential or worse, succeed with one that should have been revoked.
- Derived assumptions. Values the agent computed or inferred rather than retrieved from a reliable source. The LLM Classifier's confidence score is a derived value. The Commercial Agent's internal tier assumption is a derived value. Derived values are correct in the context in which they were produced; they can become incorrect in a different context, a different session, or after the underlying state has changed. Storing them as if they were facts is the source of the "stale data" class of memory bugs.
- Personally identifying information volunteered incidentally. A client's name, internal contact's name, or reference to a third-party system that appeared in a support query but was not part of the structured data the agent was designed to handle. Vela's agent was not built to retain procurement references or logistics contacts, but allMessages retained them anyway, because nothing said not to.
- Conversation-internal working context. Intermediate summaries an agent produced to help it formulate a response, hypotheses it considered and rejected, or internal classifications it used to route a query. These are processing artefacts, not information the system needs to carry forward.
The common pattern across all four categories: the information was correct and useful in the moment it was produced, but its continued presence creates risk of misuse, misinterpretation, or misapplication in a future context.
![image]((notion-hosted file))

## Applying this to the Vela canvas
> 🔥 Before you start, make a copy of this template. It mirrors the structure of this lesson — one tab to work through the four "must not persist" categories on the Vela canvas, and one tab to add the persistence-decision column to your project's boundary map.
Return to the Sprint 2 canvas. For each of the four categories above, identify at least one concrete example of information in the current canvas that falls into that category.
Work through these questions for each example:
1. Where is the information currently stored ($flow.state, allMessages, or both)?
1. Which agent or node wrote it?
1. Is there a reason it needs to persist beyond the turn that created it? State the reason, or state that there is none.
1. If it should not persist, what is the correct handling? Options: do not write it to shared memory in the first place; write it to a Flow State key and document that the key should be treated as turn-scoped; or write it to allMessages with a system prompt instruction to the downstream agent not to reference it in responses.
There is no single correct answer for every canvas. The right handling depends on what the system is for. The exercise is in identifying the category and reasoning through the options.

## Applying this to your project
Extend the memory boundary map you produced in the previous lesson. Add a third column: Persistence decision.
For each piece of information in your boundary map, record one of three decisions:
- Persist across sessions: The information is valuable to future interactions and retaining it is intentional and appropriate.
- Session-scoped: The information is useful within this session but should not carry forward. Flow State is appropriate; a persistent store is not.
- Turn-scoped: The information is only valid for the agent turn that produced it and should not be written to any shared location. If it must be written (for example, because the routing logic requires it), document that it is turn-scoped and should not be referenced by downstream agents.
For each item marked turn-scoped, write one sentence describing how you would prevent it from persisting either by not writing it to shared memory, by using a system prompt instruction, or by a downstream clearing step.
This column completes the memory boundary section of your Sprint 3 project deliverable. You now have three dimensions documented for each piece of information in your system: whether it is shared or private, which agent owns it, and how long it should persist.

>  
  ### 🔥 Using AI when you get stuck
  Deciding what is turn-scoped is sometimes genuinely ambiguous. If you are unsure whether a specific piece of information should persist, describe it to AI precisely:
  - What the information is and where it comes from
  - Which agent produced it and which agent might read it next
  - What a future agent would do with it if it were still available
  For example: "In a Flowise multi-agent system, the first agent is a classifier that assigns a confidence score to each query. Should that confidence score persist to the next session? What could go wrong if it does?"
  Use the response to reason through the edge cases. Make the final decision yourself. The persistence decision for your project depends on context AI cannot fully see.

## Watch out for
- Assuming allMessages only retains what matters. allMessages retains everything said in the conversation including incidental mentions, classifier outputs, intermediate reasoning the model wrote out before giving its answer, and any information a client shared that the agent did not explicitly need. There is no automatic filtering. If it appeared in the conversation, it is in the history.
- Treating "nobody complained" as evidence that retention is safe. The Vela logistics contact issue did not produce a complaint. It produced an unwanted response. Most retention problems are silent until they surface in a user-facing output. The absence of a complaint is not a signal that persistence decisions are correct.
- Clearing shared state too aggressively. The opposite failure: marking everything as turn-scoped means agents cannot coordinate at all. A query_type that is cleared before the Condition node reads it breaks the routing logic. The question is not "should I clear everything?" but "what is the minimum that must persist, and for how long?"

## Summary
Memory ownership and persistence scope are two sides of the same design decision. Ownership determines which agent is responsible for a value; who writes it, what it represents, and who the designated consumer is. Persistence scope determines how long that value should survive: the current turn, the current session, or across sessions.
The Vela canvas surfaced a clear example of what happens when neither is decided explicitly: information that should have been turn-scoped persisted across sessions and appeared in an unrelated response. Preventing that requires deciding, for each piece of information in the system, who owns it and how long it lives.
The next lesson introduces state which is a related but distinct concept. Where memory tracks what an agent knows from past interactions, state tracks where the system is in its current execution. The distinction between the two shapes how you design the handoff from one agent to the next.