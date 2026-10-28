# Memory vs. Knowledge Base vs. Tool Base

Notion page: https://app.notion.com/p/Memory-vs-Knowledge-Base-vs-Tool-Base-3669418319f3805cb77fe305896bc012
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: The three core components of a business agent — memory, knowledge base, and tools — and why they serve different purposes. This sprint focuses on memory; you will configure knowledge bases in Sprint 2 and tools in Sprint 3.

## Three things that look similar but are not
As Contigo GmbH expands its agent capabilities, the development team runs into a recurring confusion. Developers are storing policy documents in the conversation memory. Others are using the knowledge base to track user preferences. One team is mixing live API calls with document retrieval in ways that make the system unpredictable and difficult to debug.
The root cause is the same in every case: the three core components of a business agent (memory, knowledge base, and tool state) are being treated as interchangeable but they are not.  Each serves a unique purpose that ensures that agents are reliable, maintained, and easier to trust.
This lesson draws those lines clearly.

## Memory (What the agent remembers about the conversation)
Memory tracks the history and context of an ongoing interaction. 
> ❓ 
  #### Memory answers the question: What has the user told me, and what have we already decided together?
In a Contigo support conversation, memory holds things like the account number the client provided at the start of the session, the steps already completed in a loan application process, or the fact that the client expressed a preference for being contacted by email rather than phone. Memory is about the user and the interaction. It can be short term (active session only) or long-term (across sessions).

## Knowledge base (What the agent retrieves from trusted sources)
A knowledge base is a collection of documents or records the agent can search when it needs factual information. Rather than relying on the language model's general training, the agent retrieves content from verified sources to ground its responses. You will build this in Sprint 2.
For Contigo, the knowledge base might contain the firm's loan eligibility criteria, regulatory compliance guidelines under EU financial law, or internal product documentation. This content is static or semi-static (It changes infrequently and applies to all users equally, not to any individual client specifically).
> ❓ 
  #### Knowledge base answers the question: What are the official facts or rules I need to provide an accurate, grounded answer?

## Tool state (What the agent executes in external systems)
Tools give an agent the ability to take actions beyond generating text such as querying a live system, submitting a form, triggering a workflow, or processing a transaction. You will build this in Sprint 3.
For Contigo, tool use might mean checking a client's current account balance via the core banking API, submitting a loan application to the processing system, or flagging a compliance issue in the case management platform. These are real-world actions that change the state of external systems, not just responses generated from stored or retrieved information.
> ❓ 
  #### Tool state answers the question: What external action must I take to complete what the user is asking for?

## Why the separation matters
[TABLE]
  |  | Memory | Knowledge base | Tool state |
  | What it holds | Conversation history and user context | Authoritative documents and policies | Live system connections and API integrations |
  | Changes how often | Every conversation turn | Infrequently | In real time |
  | Contigo example | Client's preferred language and open cases | EU loan eligibility regulations | Submitting a loan application via the banking API |
  | Risk if misused | Privacy violations, context bloat | Hallucination from outdated documents | Unintended real-world actions or data exposure |
Keeping these three components separate is a prerequisite for building agents that are safe, auditable, and maintainable. An agent that conflates memory with retrieval will struggle to find the right information. An agent that conflates retrieval with tool use may act on documents instead of querying live systems, or vice versa.
![image]((notion-hosted file))
## Check for Understanding
>  A Contigo agent needs to retrieve the firm's current loan eligibility criteria to answer a client question. Which component should it use?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a7b6cdca-3c51-4fa3-b341-7db59363c117

> 💡 Takeaway: 
  Memory, knowledge base, and tool state are three distinct components with three distinct jobs. Memory tracks the conversation. The knowledge base grounds the response in verified facts. Tools take action in the real world. A reliable business agent keeps these separate. This sprint covers memory. The other two components will be built in the sprints that follow.
