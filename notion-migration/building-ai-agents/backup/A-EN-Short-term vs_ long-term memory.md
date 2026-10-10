# Short-term vs. long-term memory

Notion page: https://app.notion.com/p/Short-term-vs-long-term-memory-3669418319f380eaa97fcfbecf83d649
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson The difference between session memory and persistent memory, and where each one applies when designing a business agent.

## A different kind of forgetting
Contigo GmbH's support agent now has memory configured. Within a single conversation it performs well by remembering account numbers, tracks what has been discussed, and avoids repeating questions mid-session. The team considers it a success.

Then the complaints start coming from returning clients.
> Client 1: I already specified my preferred correspondence language three weeks ago and now I had to state it again.
> Client 2: A loan officer flagged a document discrepancy in a previous session and now, there is no trace of it in the new conversation.
> Client 3: A client with a long relationship with your business interacted with the agent dozens of times and treated like a stranger every time they return.
The agent is not stateless anymore. But it is amnesiac between sessions. This is a different problem and requires a different solution.

## Short-term memory: What happens inside a session?
Short-term memory, also called session context or working memory, tracks what is happening in the current active conversation. As the user and agent exchange messages, the dialogue is held in the model's context window (A total amount of text the model can process at once) and injected into each new prompt so the model can reason across turns.
This memory is ephemeral. It exists only for the duration of the active session. The moment the session ends, the working memory is wiped entirely. Nothing carries over to the next conversation.
Short-term memory is the right tool for tasks that only require continuity within a single conversation: tracking what has already been submitted, managing a multi-step process, or avoiding redundant questions mid-session. It is fast, requires no external infrastructure, and works out of the box in most agent frameworks.
![image]((notion-hosted file))

## Long-term memory: What survives across sessions?
Long-term memory stores information beyond the boundaries of a single session. Instead of relying on the context window, long-term memory writes important facts to an external database. This might be a relational database, a vector store, or a high-speed key-value store. When a user returns, the agent queries that database, retrieves relevant information, and injects it into the new session before the conversation begins.
This is what allows a Contigo agent to remember that a particular client prefers English correspondence, that their account was flagged for review in February, or that they have a loan application currently under assessment.
Long-term memory requires deliberate design decisions: what information is worth storing, how long it should be kept, who can access it, and how conflicts between old and new data are resolved. These involve privacy, compliance, and data governance. This matters in the EU financial services context that Contigo operates in. 
![image]((notion-hosted file))

## Where each applies?
[TABLE]
  |  | Short-term memory | Long-term memory |
  | Storage location | Context window (Inside the active prompt) | External database (Outside the model) |
  | Lifespan | Duration of the active session only | Persists across multiple sessions |
  | Best used for | Multi-step tasks, mid-session continuity | User preferences, history, ongoing cases |
  | Primary risk | Context window fills up, older content drops | Storing stale, incorrect, or sensitive data |

## Check for understanding
>  A returning Contigo client expects the agent to recall their preferred language from last month. Which memory type makes this possible?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/27261444-dcaa-451c-8832-a4861b30a8b0

> 💡 Takeaway: 
  Short-term memory makes a conversation coherent today. Long-term memory builds a reliable relationship over time. A well-designed business agent needs to know which one to use, when to use it, and what the risks of each are. Both types are part of the architecture.