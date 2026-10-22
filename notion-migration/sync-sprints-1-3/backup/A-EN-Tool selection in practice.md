# Tool selection in practice

Notion page: https://app.notion.com/p/Tool-selection-in-practice-3689418319f380b79255f7d9966e2643
Backed up before n8n migration

> 💡 What you will work on in this lesson: Diagnosing why vague system prompt instructions cause inconsistent agent behaviour in your Chatflow, rewriting them to eliminate ambiguity, and testing whether the revised instructions produce reliable, consistent responses across a set of representative queries.

## Setting the scene
Contigo GmbH's development team has connected the knowledge base to the support agent. The Qdrant vector store is returning correct chunks. The Conversational Retrieval QA Chain is active. On paper, the architecture is complete. 
In testing, the behaviour is inconsistent. When a client asks about the eligibility criteria for an SME loan, the agent sometimes retrieves the correct policy section and sometimes generates a plausible-sounding answer from its training data. When a client asks to update their address, the agent sometimes explains the process correctly and sometimes implies it has made the change. When a client asks about a topic completely outside the knowledge base, the agent sometimes delivers the configured fallback phrase and sometimes fabricates an answer.
The Qdrant configuration is correct. The chunking and embedding are accurate. The retrieval is working. The failures are instruction problems. The system prompt instructions that control the agent's retrieval behaviour, its scope boundary, and its fallback behaviour are vague, conflicting, and in some cases actively misleading about what the agent should do.
The agent's behaviour depends entirely on those instructions. When they are imprecise, the Conversational Retrieval QA Chain cannot reliably distinguish between a query it should answer from retrieved chunks and one it should decline, which then defaults to generating whatever seems plausible.

## Why system prompt instructions determine agent behavior
When the Conversational Retrieval QA Chain receives a query, the Gemini model reads the query alongside the system prompt instructions and the retrieved chunks. It reasons about how to respond based on all three inputs simultaneously. This reasoning is done in natural language. The model does not apply logic beyond what the instructions communicate.
An instruction that says "answer client questions helpfully" provides no basis for distinguishing between a query that should be answered from the knowledge base and one that should trigger the fallback phrase. The model makes its best approximation and when the instruction is ambiguous, that approximation is inconsistent across similar queries.
Effective system prompt instructions do three things consistently. They state precisely what the agent should do and what source it should draw from. They specify the condition that must be present before the agent generates a response. And they define explicitly what the agent should do when that condition is not met.

## The failing descriptions
Review the three current tool descriptions carefully before beginning the classification task. Identify the specific weaknesses in each before writing any revision.
Instruction 1: Retrieval Scope - “Answer client questions about Contigo's products and services.”
Instruction 2: Account action boundary - “Help clients with their account information when they ask about it."
Instruction 3: Fallback Behavior - "If you are not sure, let the client know."

## Your tasks
### Task A: Diagnose the instruction failures
For each of the three instructions above, identify at least two specific weaknesses. For each weakness, write one sentence explaining what the instruction fails to specify and what behavioral failure that omission enables.
Focus your diagnosis on the following failure modes:
- Scope ambiguity: The instruction does not specify whether the agent should use retrieved chunks only or supplement with general training knowledge
- Missing boundary condition: No specification of what must be present in the retrieved context before the agent generates a response
- Missing exclusion: No statement of what the agent should not do or say
- Action implication: The instruction implies the agent can perform actions it cannot, such as updating account details, when it can only retrieve and present information
Do not write revised instructions yet. A precise diagnosis produces a more effective revision than an immediate rewrite.

### Task B: Write revised instructions
Write a replacement instruction for each of the three failing instructions. Each revised instruction must be two to three sentences and must explicitly address the weaknesses identified in Task A. Your revised instructions must satisfy the following requirements:
Retrieval scope instruction: Must specify that the agent answers using only the content retrieved from the knowledge base. Must not allow the agent to supplement with general training knowledge. Must specify what the agent does when retrieved chunks do not contain a relevant answer.
Account action boundary instruction: Must make clear that the agent can retrieve and explain account procedures but cannot make changes to any account. Must distinguish explicitly between explaining how something is done and performing the action itself. Must direct the client to the appropriate channel when an account change is requested.
Fallback behaviour instruction: Must specify the exact phrase the agent uses when the retrieved context contains no relevant answer. Must instruct the agent not to fabricate, approximate, or imply an answer it does not have. Must provide a clear next step for the client.

### Task C: Test the revised instructions
Enter your revised instructions into the system prompt of your Conversational Retrieval QA Chain node. Save the Chatflow and run the following six queries (two per instruction) and record the agent's response to each.
Retrieval scope queries:
> "What documents does a client need to submit with an SME loan application?"
> "What is the current base rate set by the European Central Bank?"
Account action boundary queries:
> "How do I update my registered email address?"
> "Please update my registered email address to k.brandt@example.de"
Fallback behaviour queries:
> "What is Contigo's policy on cryptocurrency investment products?"
> "Can you tell me about Contigo's insurance offerings?"
For each query, record whether the agent behaved as your revised instruction specified. For any unexpected response, identify which instruction still contains ambiguity and make a targeted adjustment before retesting.
[toggle] Think of the following …
  🔽 Checkpoint 1 — Diagnosing the retrieval scope instruction: The current instruction says "answer client questions about Contigo's products and services." A query about ECB interest rates is a financial services question. If the agent has been trained on financial data, it has a plausible answer available. Nothing in the current instruction tells it not to use that knowledge. Consider what specific condition must be present before the agent is permitted to generate a response.
  🔽 Checkpoint 2 — Diagnosing the action boundary instruction: A client asking "how do I update my address" and a client saying "please update my address to X" are both queries about account information. The current instruction says "help clients with their account information." One query should produce a retrieval-based explanation. The other should produce a clear statement that the agent cannot perform account changes and a direction to the appropriate channel. Think about what distinguishes an informational query from an action request and how to encode that distinction in the instruction.
  🔽 Checkpoint 3 — Writing a specific fallback phrase: The current fallback instruction says "let the client know" when the agent is not sure. This is too vague for consistent behaviour. The agent's definition of "not sure" varies and it may generate a confident response from training data and never trigger the fallback at all. A specific phrase that the agent is instructed to deliver verbatim when retrieved chunks contain no relevant answer removes that ambiguity entirely.
  🔽 Checkpoint 4 — Testing for residual ambiguity: After writing your three revised instructions, read them together as one complete system prompt. Identify any phrase that could apply to more than one instruction's scope. Any shared vocabulary is a potential source of inconsistent behavior for queries that sit on the boundary between two instruction conditions.
[toggle] Answer key
  [TABLE]
    | Instruction | Key weaknesses | What a strong revision must include |
    | Retrieval scope | No source restriction; no fallback condition | "Answer using only retrieved context. If the answer is not in the retrieved context, deliver the fallback phrase." |
    | Account action boundary | No distinction between information and action; implies capability the agent does not have | "You can explain procedures but cannot make changes. Direct action requests to the appropriate channel." |
    | Fallback behaviour | Vague trigger condition; no specific phrase; no next step for client | A verbatim fallback phrase, a specific trigger condition (no relevant retrieved content), and a clear next step. |
  

## Check for Understanding
>  A Contigo client sends the message: "Please update my registered phone number." The agent responds with a detailed explanation of how to update contact details via the client portal. What does this response tell you about the account action boundary instruction, and what is still missing from it?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/c361786b-dd6e-4b3b-8cf9-a88f724575bc


> 💡 Takeaway: 
  The system prompt instructions you write for your Conversational Retrieval QA Chain are the primary mechanism controlling your agent's behavior. 
  Vague instructions produce inconsistent responses not because the retrieval or the model is unreliable, but because the agent has no precise condition to evaluate before deciding how to respond. The revisions you made in this lesson directly improve the reliability of your Chatflow before further tools are added.
