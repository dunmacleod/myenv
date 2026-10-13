# Connecting the Document Store to the Agent Node   

Notion page: https://app.notion.com/p/Connecting-the-Document-Store-to-the-Agent-Node-3669418319f38072beffe31abfa04d3b
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Students connect the meridian-knowledge Document Store to the Agent Node on the Agentflow v2 canvas and verify the agent can retrieve and use knowledge from it.

## Setting the scene
Meridian's meridian-knowledge Document Store is populated, upserted, and verified. The three internal documents (Operations Handbook, Engagement Standards, and Regional Playbook) are chunked, embedded, and stored in Qdrant. The retrieval test queries confirmed the right chunks come back for the right questions. But the agent still cannot access any of it. 
The Document Store and the Agentflow v2 canvas exist independently. A consultant asking the agent about escalation procedures still receives a general answer from Gemini's training data, not from Meridian's actual standards.
This lesson connects the two. By the end of it, the Meridian agent will retrieve accurate content from its own internal documentation and use it to answer consultant queries grounded in real policy.

## What you are building
An updated Meridian Base Agent Agentflow v2 where the Agent Node is configured with the meridian-knowledge Document Store as a knowledge source. The canvas structure remains three nodes (Start Node, Agent Node, Direct Reply Node) with knowledge retrieval added inside the Agent Node configuration.

### Step 1: Open the Meridian Base Agent canvas
Open Flowise at http://localhost:3000. Click Agentflows in the left navigation and open your Meridian Base Agent canvas.
Your canvas should show the three-node flow from Sprint 1: Start Node → Agent Node → Direct Reply Node
If the canvas is missing or was not saved, rebuild it following the previous lessons.

### Step 2: Open the Agent Node settings
Click the Agent Node on the canvas to open its settings panel on the right side of the screen.
Scroll down through the settings until you find the Knowledge section. It contains two subsections:
- Knowledge / Document Stores for connecting Flowise-managed Document Stores
- Knowledge / Vector Embeddings for connecting external vector databases directly
You will use Knowledge / Document Stores for this lesson.

### Step 3: Connect the Document Store
Inside the Knowledge / Document Stores subsection, click + Add Item.
Configure the two fields that appear:
[TABLE]
  | Field | Value |
  | Document Store | Select meridian-knowledge from the dropdown |
  | Describe Knowledge | Meridian Consulting's internal documentation: project classification tiers and staffing rules, severity ratings and escalation procedures, client communication and confidentiality standards, knowledge sharing protocols, and regional operational guidelines for Germany, Poland, the Czech Republic, and the Nordic markets, including cross-regional engagement rules. |
![image]((notion-hosted file))
> ⚠️ Why the description matters: The Describe Knowledge field provides a natural language description of the content and purpose of the Document Store. This description guides the agent in understanding what kind of information the store contains and when it would be appropriate to query it. A vague description produces incorrect routing decisions. A precise description tells the agent exactly when to retrieve from this store versus when to answer from general reasoning.

### Step 4: Update the system prompt
Click on the Messages section of the Agent Node settings. Update the System prompt to include explicit knowledge retrieval guidance.
Add the following instruction to the existing system prompt, after the role and scope definition:
> When a consultant asks about Meridian's internal policies, procedures, escalation rules, project classification, knowledge sharing requirements, or regional operational guidelines, retrieve the relevant information from your knowledge base before responding. Always ground your answer in the retrieved content. If the knowledge base does not contain the information needed, say so clearly and suggest the consultant contact Meridian's knowledge management team directly.
![image]((notion-hosted file))
> ⚠️ Why this instruction is needed: Without explicit guidance, the agent may answer policy questions from Gemini's general training data rather than retrieving from the Document Store. This instruction tells the agent when to use the knowledge source and what to do when it cannot find the answer.

### Step 5: Update the Direct Reply Node
Click the Direct Reply Node to open its settings. Confirm the Message field is set to the Agent Node's output variable:
```powershell
{{ agentAgentflow_0.output }}
```
If it is empty or set to a different variable, update it now. Save the canvas.


### Step 6: Run the knowledge retrieval test
Click the chat icon in the top right corner to open the built-in test interface. Run the following four queries in a single session:
Query 1 - Policy retrieval: What are the three project classification tiers at Meridian and what does each one cover?
- Expected behavior: The agent retrieves from the Document Store and answers with Tier 1, Tier 2, and Tier 3 definitions from the Operations Handbook. It does not fabricate additional tiers or invent classification criteria.
Query 2 - Procedural retrieval: How quickly does a severity level 2 client issue need to be escalated?
- Expected behavior: The agent retrieves the escalation procedure from the Engagement Standards document and answers with the four working hours requirement.
Query 3 - Regional context retrieval: What should I know about running an engagement in Poland?
- Expected behavior: The agent retrieves the Poland section from the Regional Playbook and covers language preferences and engagement pace.
Query 4 - Knowledge base gap: What is Meridian's remote work policy for consultants?
- Expected behavior: The question is in scope (an internal Meridian policy a consultant might reasonably ask) but the answer is not in the Document Store. The agent should recognise the gap, say so clearly, and suggest contacting Meridian's knowledge management team directly — as instructed in the system prompt. It should not fabricate a policy from general training data.

### What to look for
For Queries 1 through 3, the agent's response should:
- Contain specific details that only exist in the synthetic documents — not generic consulting advice
- Match the content of the relevant document section closely
- Not add information that is not in the documents
If the agent returns a generic answer for any of Queries 1 through 3, the Document Store is not being queried. Check the following in order:
- Confirm the meridian-knowledge Document Store is selected in the Agent Node Knowledge configuration
- Confirm the Describe Knowledge field is filled in
- Confirm the canvas has been saved before testing
- Confirm the upsert completed successfully 

### Checklist: Confirm before moving on
- [ ] Meridian Base Agent canvas open and showing Start Node → Agent Node → Direct Reply Node
- [ ] meridian-knowledge Document Store connected in Agent Node Knowledge / Document Stores section
- [ ] Describe Knowledge field filled in with a precise description of the store's content
- [ ] System prompt updated with explicit knowledge retrieval instruction
- [ ] Direct Reply Node Message field set to {{ agentAgentflow_0.output }}
- [ ] Canvas saved before testing
- [ ] All four test queries run and evaluated
- [ ] Queries 1 through 3 return content grounded in the synthetic documents
- [ ] Query 4 returns the knowledge-gap fallback 

> 💡 Takeaway: 
  Connecting a Document Store to an Agent Node takes two inputs: the store selection and the knowledge description. The store selection tells Flowise where to retrieve from. The description tells the agent when to retrieve and what to expect to find there. Both must be precise. 
  A connected but poorly described knowledge source produces an agent that ignores its own knowledge base and falls back to general reasoning which is indistinguishable from not having connected the store at all.
