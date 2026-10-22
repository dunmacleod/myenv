# From implementation to architecture

Notion page: https://app.notion.com/p/From-implementation-to-architecture-3849418319f380d487d7ed3b08bbe930
Backed up before n8n migration

Selin had been staring at the same slide for twenty minutes. Vela Systems' internal demo of the two-agent Flowise canvas (the one the team built in Sprint 2) had gone well. The Commercial Agent and Technical Agent both answered their respective queries correctly. The Condition node routed cleanly. Jonas had been pleased. But then a client asked what would happen when the agents needed to share information mid-conversation, and Selin didn't have an answer. She'd looked at the canvas and realised she didn't know where information lived between steps, who owned it, or what happened to it after the conversation ended.
The agents worked. That wasn't the same as understanding how they remembered.
In Sprint 2, you configured memory on each Agent Node. You turned allMessages on, set a memory type, and moved forward. That was the right move at the time. But memory in a multi-agent system is not just a node setting. It is an architectural decision that determines what each agent can know, what gets passed between agents, what persists across sessions, and what happens when things go wrong. Those decisions were implicit in the Sprint 2 build. Sprint 3 makes things clearer.
> 💡 In this lesson, you will learn to treat memory as an architectural concern by asking not just how to configure it, but what to store, where it lives, and who can access it.

## From configuration to decision
When you configure memory at the node level, you are answering a narrow question: does this agent have memory enabled, and of what type? That is a valid question. It is not the only question.
Architectural thinking asks three further questions that node configuration cannot answer:
1. What should be stored? Not everything that passes through a conversation is worth remembering. The client's query about a supplier coordination issue is worth storing, because it shapes the next agent's context. The intermediate classification label the LLM assigned is worth storing if downstream agents need it, not if the Direct Reply node is the only consumer. The raw input text from an earlier turn is worth storing if the agent needs to reference it, problematic if it contains sensitive data that shouldn't persist.
1. Where does it live? Memory can live in a single agent's context window, in Flow State shared across the canvas, or in a persistent store that survives beyond the session. Each location has a different scope, lifespan, and accessibility. Treating all three as interchangeable is how memory bugs appear — an agent reads stale information because the wrong store was used, or two agents overwrite each other's context because they share state they shouldn't.
1. Who can access it? In a multi-agent system, different agents often need different views of the conversation. The Commercial Agent at Vela might need the client's account history. The Technical Agent might need the error log from the previous interaction. Neither needs, and both probably shouldn't have, access to information meant for the other. Access is a design choice, not a default.

## The three memory locations
Before decisions can be made, the locations need to be distinct.
[TABLE]
  | Location | What it is | Lifespan | Who can read it |
  | Agent context window | The message history passed directly to the model in this agent's execution | One turn | This agent only |
  | Flow State | Key-value pairs written to $flow.state during execution | This session | Any node in the same canvas |
  | Persistent store | External storage (a database, Document Store, or vector store) written to and read back across sessions | Across sessions | Any agent with access credentials and a retrieval step |

These three are not interchangeable. The context window disappears when the agent's turn ends. Flow State is cleared when the session closes. A persistent store survives until something explicitly deletes the record. Using Flow State when you need persistence, or a persistent store when you only need to pass a value to the next node, creates a system that is harder to understand and harder to fix.
In the Sprint 2 canvas, $flow.state.query_type lived in Flow State. That was the right choice. It only needed to survive long enough for the Condition node to read it and route the query. It did not need to persist beyond the session. But if Vela later wanted the Commercial Agent to remember what a client had asked about last week, Flow State would be the wrong location. That information needs a persistent store.
![image]((notion-hosted file))

## Why the distinction matters in practice
Two problems appear frequently in multi-agent systems when these three locations are confused.
- State bleed. An agent writes to a location that the wrong node reads. In the Vela canvas, if the Commercial Agent wrote a detailed client summary to $flow.state.client_summary and the Technical Agent read that value without checking whether it was relevant to the current query — the Technical Agent might incorporate stale or irrelevant information into its response. The problem isn't memory itself; it's that the wrong agent accessed information it wasn't supposed to read.
- Persistence mismatch. An agent writes to Flow State information it expects to be available next session such as a client preference, a previous resolution, a user's name. The session ends. Flow State clears. The next session starts fresh, and the agent behaves as if it has never spoken to this client before. The fix isn't to change the memory type at the node level; it's to move that information into a persistent store from the beginning.
Both problems are easier to prevent than to diagnose after the fact. That is why memory is an architectural concern. The decision about location is made at design time, not during debugging.

## The design questions to ask before configuring
For the Vela system, three questions sharpen every memory decision.
1. Does this information need to survive the session? If a client asks about supplier coordination today and comes back tomorrow, should the agent remember the earlier conversation? If yes, Flow State is insufficient. A persistent store is needed. If the information is only relevant for this session's routing, Flow State is correct.
1. Which agents need access? If only one agent needs a piece of information, it belongs in that agent's context window or in a Flow State key that only that agent reads. If multiple agents need it, Flow State is appropriate, but the key should be written once and read carefully, not written by multiple agents and overwritten mid-session.
1. What must not be stored? Some information should never persist. A client's raw emotional state during a complaint. A temporary authorisation code. Information that is only valid for this interaction and would mislead any future agent that reads it. Deciding what must not persist is as important as deciding what should.
These questions don't have universal answers. They depend on the system's purpose. But asking them before configuring memory, rather than after the system starts behaving unexpectedly is the habit this sprint builds.

## How this connects to the project
The Sprint 3 project deliverable asks you to define the memory and state architecture for your own project agent: what is shared, what is private, what must never persist, and how state is recovered after failure. This lesson is the foundation for that specification.
By the end of this sprint, that specification will be a real design document, not a description of node settings, but a set of architectural decisions you can justify. The next two lessons refine the vocabulary: shared versus private memory between agents and memory ownership and what must never persist. When you start the State Architecture lessons, you will be introduced to a state as a parallel concern, distinct from memory but closely related. 
This lesson gives you the foundation.

## Check for Understanding
### Question 1
>  Vela's ops team wants the Technical Agent to remember a client's recurring error pattern so it can reference it next time the client connects, even weeks later. Which memory location is appropriate?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/78874726-b1b3-4849-9d34-05cb2f477ad8

## Summary
Memory in a multi-agent system is not a node toggle. It is a set of decisions about what to store, where to store it, and who is allowed to read it. The three storage locations (agent context window, Flow State, persistent store) differ in lifespan, scope, and accessibility, and treating them as interchangeable produces bugs that are hard to diagnose after the fact.
The shift this lesson introduces is from configuration to design: asking memory questions at the architecture stage, before anything is built, so that the decisions are intentional rather than accidental. The next lessons sharpen two specific design concerns and what happens when multiple agents share access to memory, and what information should never be stored at all.