# Memory failure modes

Notion page: https://app.notion.com/p/Memory-failure-modes-3689418319f38038a198f71f24e73b97
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: The four ways ungoverned memory causes agent behaviour to become irrelevant, stale, or unsafe; and how the memory configuration decisions you made in Sprint 1 directly address each failure mode.

## Memory as a liability
Contigo GmbH's agent retains conversation context across turns, isolates sessions by Session ID, and enforces a window size that prevents the context window from filling with irrelevant history. These were deliberate Sprint 1 decisions. But it is worth understanding what happens when those decisions are not made because memory that is not actively governed becomes a liability rather than an asset.
The same mechanism that makes the agent feel coherent to a client also makes it vulnerable to acting on outdated, incorrect, or maliciously injected information. In production, where sessions accumulate across days and weeks, memory failures compound in ways that are difficult to detect and expensive to fix.
There are four distinct failure modes. Each one maps directly to a decision you made in Sprint 1.

## The four failure modes

#### Failure Mode 1: Context degradation and relevance decay
As an agent accumulates conversation history, injecting all of it into the context window on every turn degrades reasoning performance. Research consistently shows that model attention quality decreases as input length increases, often breaking down long before the model reaches its advertised context limit.
The result is an agent that becomes distracted by older, irrelevant detail. A client who asked about personal loans three weeks ago should not have that exchange influencing the agent's reasoning about their current SME application. Injecting everything produces an agent that is less focused with every passing session.
> ➡️ How your Sprint 1 configuration addresses this: The Buffer Window Memory node you configured limits the active context to the last K message pairs. Only the most recent turns are injected into the prompt. Older exchanges are dropped automatically. The window size you set up during the first sprint was your direct response to this failure mode. A window that is too large reintroduces context degradation. A window that is too small drops important context too early. The value you chose was a deliberate trade-off between those two risks.

#### Failure Mode 2: State drift and stale information
In long-running systems, memory state becomes outdated. An agent that successfully resolved a compliance query last week may retrieve that cached context when the same client returns and the regulatory guidance may have changed in the interim. When the agent cannot distinguish between historical memory and current reality, it produces responses grounded in information that is no longer accurate.
For Contigo, this is particularly acute. EU financial regulation evolves. Product terms are updated quarterly. A memory store that is never refreshed becomes a record of how things were.
> ➡️ How your Sprint 1 configuration addresses this: The Buffer Window Memory node stores only the current session's recent turns. It does not persist information across sessions unless configured to do so. When a new session begins with the same client, it starts with a fresh context window. Historical exchanges from previous sessions do not carry over and influence the current session's responses. The Session ID you configured in ensures each session is isolated, which also means each session starts without the accumulated state drift of prior interactions.

#### Failure Mode 3: Memory poisoning and compounding errors
Agents treat their memory stores as ground truth. If a tool fails and the agent hallucinates a fact. For example, an incorrect loan application status and that hallucination is written to the conversation history, every subsequent reasoning step in that session builds on corrupted state. A single error compounds non-linearly across the execution loop.
This failure mode is insidious because the agent behaves consistently. It is consistently wrong in a way that traces back to one poisoned entry that was never validated or corrected.
> ➡️ How your Sprint 1 and Sprint 3 configuration addresses this: The tool failure fallback instruction you wrote and implemented directly addresses this. When the loan status tool fails, the agent is instructed to acknowledge the failure honestly rather than fabricate a status. A fabricated status written to the conversation history would poison every subsequent turn in that session. The fallback instruction prevents the fabrication which prevents the poisoning.

#### Failure Mode 4: Persistent security compromise
Unlike a stateless chatbot that resets when the window closes, a memory-enabled agent carries state across sessions when configured to do so. If a malicious user succeeds in injecting a harmful instruction. For example, instructing the agent to always approve refund requests above a certain threshold and that instruction is written to long-term persistent memory, it persists across restarts and affects future sessions with other clients. This transforms a prompt injection attack from a single-session incident into a persistent system compromise.

> ➡️ How your Sprint 4 configuration addresses this: The Simple Prompt Moderation node you added intercepts injection attempts before they reach the Tool Agent. The anti-injection instruction in the system prompt governs model behaviour for attempts that pass the filter. Together they reduce the probability that a malicious instruction reaches the conversation history and gets treated as ground truth in subsequent turns.

## The underlying principle
All four failure modes share one root cause: memory that is passively accumulated without active governance. The mitigation for each is the same design principle. Memory must be actively managed.
Practical governance mechanisms include:
- Time-based decay: Automatically deprioritising or removing entries after a defined period
- Importance-based retention: Discarding information that has not proven relevant to subsequent queries
- Periodic validation: Checking stored facts against current system state before using them in responses
- Session isolation: Ensuring one client's history cannot influence another client's session
![image]((notion-hosted file))

## Check for Understanding
>  A Contigo agent retrieves a cached compliance interpretation from three months ago and presents it to a client as current guidance. The underlying regulation was updated six weeks ago. Which memory failure mode does this describe?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8aa70d13-eda3-4353-9080-314102a78ce5

> 💡 Takeaway: 
  The four memory failure modes (context degradation, state drift, memory poisoning, and persistent security compromise) are not edge cases. They are predictable consequences of memory that accumulates without governance. 
  The Buffer Window Memory configuration, Session ID isolation, tool failure fallback instruction, and input moderation you built across Sprints 1 through 4 each address one or more of these failure modes directly. Understanding the failure modes gives you the vocabulary to explain and defend those design decisions during your presentation.