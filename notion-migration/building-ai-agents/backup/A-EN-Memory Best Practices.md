# Memory Best Practices

Notion page: https://app.notion.com/p/Memory-Best-Practices-3669418319f380ceaf6cfc32055e0f26
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: The core rules for what to include in agent memory, what to exclude, and how to protect against the most common memory-related failures in a production business agent.

## Why best practices matter at this stage
Contigo GmbH's agent can now hold conversations using Buffer Memory, isolate sessions using Session IDs, and manage context length using Buffer Window Memory. The technical foundations are in place. But having a working memory configuration and having a well-designed one are not the same thing
In testing, Contigo's team has already encountered three recurring problems. The agent occasionally stores information it should not; including details that create privacy exposure. Its long-term memory database is growing faster than expected, with large amounts of content that is never retrieved and never useful. And in one instance, a piece of incorrect information stored early in a session persisted across turns, causing the agent to give a client inaccurate guidance for several exchanges before a human reviewer caught it.
None of these are configuration errors. They are design errors and they are the result of not having clear rules for how memory should behave. 

## Rule 1: Store the minimum necessary
The most common memory mistake is storing too much. Developers configure agents to capture everything a user says on the assumption that more context is always better. It is not.
Storing unnecessary content has three concrete costs. It increases the size of the context window on every subsequent turn, which raises token costs and degrades attention quality over long conversations. It fills the long-term memory database with noise that makes relevant retrieval harder. And it creates a larger surface area for privacy exposure if the database is ever accessed without authorisation.
The rule is simple: store only what the agent would genuinely use in a future interaction to serve the client better. If there is no clear answer to the question "how would remembering this improve the next conversation?", the information should not be stored.
> In your Chatflow: Your Buffer Window Memory node is already applying this principle by limiting the active context to the last K messages. The window size you configured is your first implementation of this rule.

Ask yourself: is every message inside that window something the agent would genuinely use to serve the client better in the current turn?

## Rule 2: Never store sensitive identifiers in memory logs
Financial credentials, government-issued identifiers, health disclosures, and similar sensitive data should never be written to conversational memory (short-term or long-term).
These items should follow one of two paths. If they are needed to complete an action (an IBAN required to update a direct debit), they should be passed directly to a secure tool via an API call and then discarded from the conversation context. If they are not needed for any immediate action, they should be dropped entirely.
This is not only a security practice. Under the EU General Data Protection Regulation, storing special category data without an explicit legal basis and appropriate safeguards is a regulatory violation. In Contigo's operating environment, this distinction is non-negotiable.
> In your Chatflow: Your current build has no tool connections yet. That will come later. For now, the correct behaviour is to ensure your system prompt instructs the agent to acknowledge sensitive data without repeating it back or storing it unnecessarily in the conversation history. This is the design constraint that your tool configuration will enforce properly.

## Rule 3: Apply time-based decay to long-term memory
Long-term memory databases grow without bound unless actively managed. Information that was relevant six months ago may be stale, inaccurate, or simply no longer applicable to the client's current situation.
Implement a time-based decay policy that automatically deprioritises or removes memory entries after a defined period. What that period is depends on the use case. This is a preference for written communication is likely to remain valid for years, while a note about a temporary account restriction may be irrelevant within weeks.
The key is making this decision deliberately rather than allowing the database to accumulate indefinitely.
> In your Chatflow: Buffer Window Memory handles this automatically by dropping messages outside the window. However, automatic truncation is not the same as a deliberate decay policy. Consider which information in your Contigo agent's conversation history would still be relevant in a long session versus what becomes irrelevant after a few turns.

## Rule 4: Validate stored facts and handle conflicts
Memory poisoning occurs when incorrect information is stored and then retrieved in future sessions as if it were true. This can happen when a client provides inaccurate details, when the language model hallucinates a fact that gets written to memory, or when new information contradicts something stored previously.
Define a conflict resolution rule before this becomes a problem. When new information contradicts an existing memory entry, the agent needs a clear instruction for how to proceed — whether to overwrite the old entry, flag the conflict for human review, or ask the client to confirm which version is correct.
> In your Chatflow: Your Buffer Window Memory node has no built-in conflict resolution. If a client corrects information they provided earlier, the agent will see both versions if they are within the active window. Your system prompt should include a clear instruction for how to handle this. A simple rule such as "always treat the most recently stated information as correct" is sufficient at this stage.
![image]((notion-hosted file))

## Check for Understanding
>  A Contigo agent stores every message from every client conversation in its long-term memory database without filtering. What is the most immediate operational risk?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7486b98a-16cc-4bf1-b8bb-de8327ae6ff8

> 💡 Takeaway: 
  Good memory design is as much about what the agent forgets as what it remembers. Storing the minimum necessary, protecting sensitive data, managing database growth, and handling conflicting information are the four practices that separate a memory configuration that works in a demo from one that holds up in production.