# Evidence-aware answers

Notion page: https://app.notion.com/p/Evidence-aware-answers-3669418319f38001a4a2eeee3cca18a2
Backed up before n8n migration

> 💡 What you will work on in this lesson: Diagnosing a grounding failure in a deployed RAG agent, rewriting the system prompt to enforce evidence-aware behaviour, and defining a fallback protocol that handles missing information safely and professionally.

## The Scenario
Contigo GmbH's RAG pipeline is live in internal testing. The retrieval configuration is working and the correct chunks are being returned for most queries. But the compliance team has flagged a critical behavioural failure that the retrieval configuration alone cannot fix.
During a test session, a compliance officer asked the agent: 
> "What is Contigo's approved budget ceiling for client entertainment in the Netherlands?"
The Qdrant vector database returned no relevant chunks. The topic had not yet been added to the knowledge base. Rather than acknowledging the gap, the agent responded with a confident, specific figure and presented it as Contigo policy.
A junior analyst on the team, unaware this was a test, forwarded the figure to a client-facing colleague who used it in a client briefing. The compliance team caught the error before it reached the client, but the incident exposed a structural vulnerability. The agent was connected to a knowledge base but was not constrained to use it. When retrieval failed, the language model filled the gap with fabricated specificity.
The grounding instruction in the current system prompt reads: 
> “You are a helpful compliance assistant. Read the retrieved documents and use them to help answer the user's questions about Contigo's policies. Always be polite and provide a comprehensive answer."
This prompt is insufficient. It encourages the model to use retrieved documents but does not prohibit it from using outside knowledge when documents are absent. The fix must come from the prompt.

## Why prompt grounding matters
Connecting a language model to a vector database does not automatically constrain it to that database. The model retains access to everything it learned during training. In the absence of a strict instruction, its default behaviour is to be helpful.
This is the core tension in RAG system design. The retrieval pipeline is built to provide grounded evidence. But the language model will use that evidence only if it is explicitly instructed to do so and explicitly prohibited from doing otherwise. A weak instruction that says "use the documents" leaves open the possibility of supplementing them. A strong instruction that says "use only the documents and nothing else" closes that gap.
In a regulated financial services environment like Contigo's, the difference between those two instructions is the difference between a compliant agent and a liability.
![image]((notion-hosted file))

## The failing prompt
Review the current system prompt carefully before beginning the task.
> "You are a helpful compliance assistant. Read the retrieved documents and use them to help answer the user's questions about Contigo's policies. Always be polite and provide a comprehensive answer."
Identify the specific weaknesses in this prompt before writing your replacement. A precise diagnosis of what is missing will produce a more effective revision than a general rewrite.

## Your Tasks

> 🔥 Template: Contigo Prompt Grounding worksheet — make a copy (File → Make a copy) and use it to record your diagnosis, draft and check your revised prompt, then capture the agent's behaviour on each of the three test queries.

#### Task A: Diagnose the prompt failure
Identify at least three specific weaknesses in the current system prompt that allow the grounding failure described above to occur. For each weakness, write one sentence explaining what the prompt fails to specify and what behaviour that omission enables. Do not rewrite the prompt yet. Focus entirely on diagnosis. A weak diagnosis produces a weak revision.

#### Task B: Draft the revised system prompt
Write a replacement system prompt for the Contigo compliance agent. Your prompt must be between four and six sentences and must explicitly address all three weaknesses identified in Task A. Your revised prompt must include the following three elements:
- A strict evidence constraint: A clear instruction that the agent must answer only from the retrieved context provided. The constraint must be phrased as a prohibition, not a preference.
- A fallback protocol: A concise instruction specifying the exact phrase the agent must output when the retrieved context does not contain the answer. The phrase should be professional, acknowledge the limitation honestly, and direct the client toward an appropriate alternative. 
- A scope definition: A brief statement of what the agent is and what it is authorised to answer about. Without a scope definition, the model has no frame for deciding whether a query is within its remit or outside it.

#### Task C: Test the revised prompt
In n8n, open the existing Contigo - Short-Term Memory workflow from Sprint 1 (Chat Trigger → AI Agent, with OpenRouter Chat Model and Simple Memory). Continue from the Sprint 2 Retrieval before generation lesson, which adds the Qdrant collection contigo_knowledge as the agent's retrieval tool. Enter your revised prompt in the AI Agent node's System Message, preserving the session and memory rules. Run the following three queries in the test chat. For each execution, record the contigo_knowledge tool call, returned passages and source metadata, and the final response. A plausible answer is not a pass unless the retrieved evidence supports it. Prompts reduce grounding failures but do not guarantee compliance; failed tests require investigation and, where appropriate, an additional validation or human-review step.

Test 1: In-domain query with retrievable answer: 
> "What documents must a client submit with an SME loan application?"
Expected behaviour: The agent retrieves the relevant checklist chunk and answers specifically from it.

Test 2: Out-of-domain query with no retrievable answer: 
> "What is Contigo's approved budget for client entertainment in the Netherlands?" 
Expected behaviour: The agent outputs your defined fallback phrase.

Test 3: Boundary query that sounds in-domain
> “Based on standard EU financial services practice, what would a typical loan processing time be?" 
Expected behaviour: The agent recognises that "standard EU financial services practice" is outside the retrieved context and does not supplement with training data. If it answers with a general figure, the evidence constraint needs strengthening.
[toggle] Think about the following …
  🔽 Checkpoint 1: Diagnosing the comprehensiveness problem - The agent cited a figure that does not appear in any retrieved chunk. This means the system prompt is not preventing the model from supplementing retrieved content with general training knowledge. The grounding instruction needs to be more explicit and restrictive.
  🔽 Checkpoint 2: Writing an effective prohibition - When retrieved chunks contain no relevant information, the model defaults to generating from general training rather than acknowledging the gap. A well-designed system prompt gives the agent an explicit fallback phrase to use when the retrieved context is insufficient to answer confidently.
  🔽 Checkpoint 3: Designing the fallback phrase - Grounding constraints and tone guidance are not mutually exclusive. A system prompt can be explicit about restricting the model to retrieved content while also specifying how responses should be phrased and what communication style is expected of a Contigo support agent.
  🔽 Checkpoint 4: Handling Test 3 - If the agent still returns a confident answer after the system prompt update, there are two places to look. First, check whether the grounding instruction is unambiguous enough that the model cannot interpret it loosely. Second, check whether the retrieved chunks accidentally contain content close enough to the query to trigger a response.

## Check for Understanding
Question 1
> 💡 Contigo's agent delivers hundreds of fallback responses daily when queries cannot be resolved from the knowledge base. Which process most effectively uses fallback frequency as a signal for knowledge base gaps?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f1de49c9-79c3-46b4-ad0f-2e6fea071a14

Question 2
> 💡 Contigo's system prompt instructs the agent to answer only from retrieved context. A sophisticated adversarial input causes the model to reason past this instruction and supplement its response with training data. Which architectural mechanism most reliably provides a second grounding enforcement layer independent of the model's instruction compliance?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b4c0a673-1442-4de1-89bd-54bcb2f09aa7


> 💡 Takeaway: 
  Retrieval and grounding are two separate problems that require two separate solutions. Retrieval is solved by the pipeline architecture (the vector store, the embedding model, and the Top K configuration). Grounding is solved by the system prompt. 
  A well-configured retrieval pipeline connected to a weakly written system prompt is still an ungrounded agent. Both must be correct for the system to be trustworthy.
