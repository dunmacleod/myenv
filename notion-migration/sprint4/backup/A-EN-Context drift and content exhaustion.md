# Context drift and content exhaustion

Notion page: https://app.notion.com/p/Context-drift-and-content-exhaustion-3689418319f3802086c3db115a057add
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: How long-running agent sessions degrade in quality as the context window fills, why a large context window does not solve this problem, and how the Buffer Window Memory configuration you made in Sprint 1 fits into the broader landscape of context management strategies used in production deployments.

## The myth of infinite context
Contigo GmbH's agent handles multi-turn client conversations that can run to twenty or thirty exchanges in complex loan assessment or compliance sessions. Each turn adds to the context window, conversation history from the Buffer Window Memory node, retrieved document chunks from the Qdrant knowledge base, tool outputs from the loan status lookup and Calculator. Over the course of a long session, this accumulation grows significant.
A common assumption is that using a model with a large context window solves this problem entirely. It does not. Research consistently shows that reasoning performance degrades as input length increases, often breaking down long before the advertised context limit is reached. A model processing a 200,000-token prompt does not reason as well as the same model processing a 10,000-token prompt, even if both are within the technical limit.
This degradation has a name: context drift. And its operational consequence is one of the most common and costly failure modes in production agent deployments.

## How context drift manifests
As the context window fills, the model's attention becomes distributed across an increasingly large input. Three specific failure patterns emerge.
- Degraded reasoning: The agent begins ignoring its system prompt or the client's immediate instruction in favour of older content that dominates the context by volume. A client who pivots from discussing personal loans to asking about SME products may find the agent continues reasoning about personal loan parameters because that content fills more of the context than the new query.
- Tool selection errors: An agent that was routing correctly at Turn 5 may begin invoking the wrong tool at Turn 25 because the tool descriptions are being outweighed by the volume of accumulated history. The model's attention to the routing instructions dilutes as the context grows. This connects directly to the context dilution and tool bloat failure modes introduced in an earlier lesson.
- Cost and latency spikes: Every reasoning step processes the entire context window. A session that grows from 8,000 tokens to 80,000 tokens over thirty turns increases the token cost of each individual step by a factor of ten and increases latency proportionally. For Contigo's deployment across hundreds of concurrent client sessions, this cost multiplication is operationally significant.
![image]((notion-hosted file))

## How your Sprint 1 configuration addresses this
The Buffer Window Memory node configured uses a sliding window approach. It retains only the most recent K message pairs in the active context and drops everything older. This directly limits the volume of conversation history injected into each prompt turn.
The window size you chose was a deliberate trade-off. A window that is too small drops important context too early. A client's case reference from Turn 1 may be outside the active window by Turn 7. A window that is too large reintroduces context pressure by retaining more history than is genuinely needed for the current turn.
For Contigo's typical support conversation (product questions, eligibility queries, and status checks), the window size you configured is the correct and sufficient mechanism. It keeps the active context focused without losing the conversational continuity that makes the agent useful.

## Four strategies to manage context
Your sliding window configuration is one of four strategies used to manage context in production deployments. Understanding the others positions your current build in the broader landscape and prepares you for more complex deployments.

#### Strategy 1: Sliding window (your current implementation)
- Only the most recent N turns are retained in full. Older turns are dropped. The system prompt and current task instructions are always present regardless of how many turns have passed. Simple to configure and directly implemented by your Buffer Window Memory node.
- Limitation: Important information from early in a long session (a case reference and a stated preference) can fall outside the window and be lost entirely.

#### Strategy 2: Compression and summarisation
- Rather than retaining raw tool outputs and full exchange transcripts, the system compresses older content. A series of five exchanges about loan eligibility is summarised into two sentences that preserve the conclusion without the verbose back-and-forth. The summary replaces the raw history, keeping the context window lean while preserving the essential meaning.
- Limitation: Summarisation requires an additional model call, adding latency and cost. The summary is an approximation and specific details can be lost in compression.

#### Strategy 3: Token budgeting
- Fixed token allocations are reserved for the system prompt, tool schemas, and generation headroom. History and retrieved content fill only what remains. When the budget is approached, the lowest-priority content is dropped first. This is typically older conversation turns rather than retrieved chunks or system instructions.
- Limitation: Requires careful calibration. A budget that is too restrictive drops important context. A budget that is too generous reintroduces context pressure.

#### Strategy 4: Tiered memory
- Recent turns are held in fast working memory equivalent to your Buffer Window Memory node. Older turns are archived to a vector store and retrieved only when semantically relevant to the current query. The active context window stays small. The full history remains accessible without occupying prompt space permanently.
- Limitation: Significantly more complex to implement. Requires a persistent vector store configured for long-term memory retrieval. This would be a different use of Qdrant than the knowledge base configuration built in Sprint 2.
For Contigo's support use case (short-to-medium focused conversations where session continuity matters but long-term cross-session history is not required), the sliding window is the correct and sufficient strategy.

## Check for Understanding
>  A Contigo agent handles a 25-turn compliance session correctly through Turn 15 but begins ignoring its grounding instruction and fabricating regulatory figures in Turns 16 through 25. No configuration changes were made during the session. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f7cfc817-3fd5-46d1-a0c9-38470991ad6d


> 💡 Takeaway: 
  Context is a budget, not a warehouse. Every token injected into the prompt competes for the model's attention. The Buffer Window Memory configuration you built in Sprint 1 is your primary mechanism for managing that budget by keeping the active context focused on what the current turn actually needs. 
  Understanding the three additional strategies used in production deployments positions your current build accurately: it is the correct and sufficient architecture for Contigo's support use case, and the starting point for more sophisticated context management when the deployment scale demands it.