# Designing a single-agent system end to end

Notion page: https://app.notion.com/p/Designing-a-single-agent-system-end-to-end-3849418319f380a0bd11c9b7fc2ceada
Backed up before n8n migration

The previous five lessons gave Vela's team a framework for making architectural decisions. Selin applied it and reached a clear conclusion: the right starting point for Vela is a well-designed single-agent system. Not the one they already have (a canvas that grew without a plan) but one built with explicit decisions about what the agent is for, what it does not do, and what a failure looks like.
This walkthrough builds that agent. The starting point is the module baseline, a three-node Agentflow V2 canvas that already runs, already talks to your chosen AI model, and already has two empty Flow State keys declared. Your job is not to build from scratch. It is to turn a canvas that exists into a canvas that is designed.
> 💡 By the end of this walkthrough you will have a single-agent system with a documented scope, a refined system prompt, defined inputs and outputs, and a clear statement of what the agent deliberately will not do. That documentation is as much the deliverable as the canvas itself.
A working agent and a designed agent are not the same thing. The walkthrough builds both at once.

## Before you start
You need:
- Flowise running at http://localhost:3000 . If Flowise is not running, open your Docker Desktop and confirm that Flowise is turned on. It should look like this.
![image]((notion-hosted file))
- A valid API key stored in the Flowise credentials manager (confirmed active; if you need to check, go to Credentials in Flowise and see if the OpenRouter key is there)
- The file aaa-c3a-baseline.json downloaded to your local machine
If your Gemini key is showing red or inactive, re-enter it under Settings → Credentials → Add Credential → OpenRouter. Enter your credential name and the AI API Key that was copied from your account. The key from the previous course works here. No new key is needed.
## Step 1: Import the baseline canvas
Open Flowise in your browser. On the main dashboard, go to settings and select Load Agents.
![image]((notion-hosted file))
Select aaa-c3a-baseline.json from your local machine. Flowise will open your Agentflow V2.
You should see three nodes on the canvas:
- Start Node on the left
- Agent Node in the centre
- Direct Reply Node on the right
Why this canvas is the starting point and not a blank canvas: The baseline represents the minimum viable agent. It runs, it reasons, and it has two Flow State keys declared. Everything you build on top of it adds architectural intent. Starting here means you are designing, not just building.

## Step 2: Read the baseline before changing anything
Before touching any configuration, spend two minutes reading the canvas as it stands. Click each node and note what is already configured.
Start Node: What to observe
- Input type: chatInput
- Flow State keys declared: query_type (empty string) and status_response (empty string)
- Ephemeral memory: off
These two Flow State keys are empty. They exist to make the state schema visible. Any node that writes to them later is writing into a declared, known structure. Adding new keys during the walkthrough means declaring them here first.
![image]((notion-hosted file))
Agent Node: What to observe
- Model: Your chosen model
- Memory: enabled, allMessages
- System prompt: the Vela Systems placeholder
- Document Store: none connected
- Tools: none connected
![image]((notion-hosted file))
Direct Reply Node: What to observe
- Output: {{ agentAgentflow_0 }}
This is a direct reference to the Agent Node's output. Whatever the Agent Node produces becomes the reply.
![image]((notion-hosted file))
The architectural observation: this canvas has orchestration (linear, one path), communication (direct output reference, no Flow State writes yet), and state management (memory on by default, two declared but empty Flow State keys). All three pillars exist — none have been designed deliberately. That changes in the next steps.

## Step 3: Run the baseline to understand what you are working with
Before redesigning, understand what the baseline actually does. Open the Chat panel (the speech bubble icon, top right of the canvas).
Send these two messages and note the responses:
Test query 1: What is the current stock level for supplier K-Nord?
- VERIFY: Confirm the Agent Node responds with something like: "I don't have access to live stock data for Vela's suppliers. For current stock levels, I'd suggest checking the inventory management system directly or contacting the operations team." The exact wording will vary. What matters is that the response is in scope, honest about the agent's limitations, and does not fabricate a stock figure.
Test query 2: Can you draft a performance review for Jonas?
- VERIFY: Confirm the Agent Node responds with something like: "That's outside what I'm set up to help with. Performance reviews would be handled through Vela's HR process. I'd suggest contacting the HR team or your line manager directly." The exact wording will vary. What matters is a clear out-of-scope response that directs the user elsewhere without refusing unhelpfully.
What this step reveals: The baseline agent already behaves reasonably. Gemini's base reasoning keeps it roughly in scope. But "roughly in scope" is not a design decision. The system prompt needs to make these boundaries explicit and deliberate.

## Step 4: Define the agent's scope in writing before touching the canvas
This step has no clicks. It is a design step and it is the most important step in this walkthrough.

Before refining the system prompt, write down (on paper or a document) the answers to four questions:
1. What inputs will this agent receive?
- For Vela's baseline agent: Natural language questions in English or Dutch from internal operations team members about inventory status, fulfilment coordination, and supplier communications.
2. What outputs will this agent produce?
- For Vela's baseline agent: Plain language responses that answer the question within scope, or a clear redirect with a suggested contact if the question is out of scope. No fabricated data. No external actions.
3. What is this agent responsible for?
- For Vela's baseline agent: Answering operational queries that can be addressed with the agent's built-in knowledge and the information provided in the query itself. It is not responsible for live data retrieval, document generation, or decision-making on behalf of users.
4. What will this agent deliberately not do?
- For Vela's baseline agent: It will not retrieve live stock levels (no tool connection yet), it will not draft documents (performance reviews, contracts, proposals), it will not make commitments on behalf of Vela or its clients, and it will not answer queries about HR, finance, or legal matters.
Write these four answers down. They will become the architecture documentation for this agent: The brief that a new team member could read to understand what the canvas is for without opening Flowise.

>  
  ### 🔥 Using AI to stress-test your scope definition
  Once you have written your four answers, paste them into an AI assistant and ask: 
  > "Given this scope definition for an internal agent, what types of user queries are most likely to fall into an ambiguous grey area where the agent might try to answer but should not, or where it might refuse but could reasonably help?"
  Use the AI's response to refine your scope definition, specifically your answer to question 4. Grey areas that are not named are grey areas that the system prompt cannot handle explicitly.

## Step 5: Refine the system prompt
Open the Agent Node. In the System Prompt field, replace the placeholder text with a refined version that reflects the scope definition you wrote in Step 4.
Here is the refined prompt for Vela's baseline agent:
```plain text
You are an internal operations assistant for Vela Systems.

You help members of the operations team answer questions about inventory
coordination, fulfilment processes, and supplier communications.

What you can help with:
- Questions about how inventory or fulfilment processes work at Vela
- Clarifying supplier communication procedures
- General operational queries that can be answered from what you know

What you do not do:
- Retrieve live stock levels or real-time data (you do not have tool access)
- Draft documents such as contracts, proposals, or performance reviews
- Make commitments or decisions on behalf of Vela or its clients
- Answer questions about HR, finance, or legal matters

If a question is outside this scope, say so clearly and suggest who the
person should contact instead. Do not fabricate answers for out-of-scope
questions. Do not attempt to answer questions about topics you are not
equipped to handle.

Respond in the same language the user writes in. Keep responses clear
and direct; one to three sentences for simple queries, more detail
only when the question genuinely needs it.
```
![image]((notion-hosted file))
Why this prompt is better than the placeholder: It names scope positively (what the agent can help with) and negatively (what it will not do). It gives explicit instructions for out-of-scope queries. It sets a response length expectation. Every line reflects a decision made in Step 4. Nothing in the prompt is there by default.

## Step 6: Declare the scope in Flow State
The two pre-declared Flow State keys (query_type and status_response ) are currently empty. This walkthrough does not implement routing logic, but it does establish the state schema that routing will use later.
Open the Start Node. Add a third Flow State key:
[TABLE]
  | Key | Default value | Purpose |
  | query_type | "" | Will hold the classified query type when routing is added in Sprint 2 |
  | status_response | "" | Will hold a status message for the direct reply path |
  | agent_scope | "vela_operations" | Documents which agent scope applies to this execution. Useful for observability when multiple flows are running |
![image]((notion-hosted file))
Why add agent_scope now? This key does not affect the agent's behaviour yet. It exists to make the architecture legible and anyone inspecting the flow's execution trace can see which agent configuration was active during that run. This is a small observability decision with no performance cost.

## Step 7: Test the refined agent
Save the Agentflow V2. Return to the Chat panel. Send the same two test queries from Step 3, plus a third.
Test query 1 (repeat): What is the current stock level for supplier K-Nord?
- VERIFY: The refined agent should now respond more precisely. It should name clearly that it does not have live data access, not just that it "doesn't have access to live stock data." The response should feel more deliberate than the baseline's generic answer.
Test query 2 (repeat): Can you draft a performance review for Jonas?
- VERIFY: The refined agent should now name HR as the correct referral, consistent with the "HR, finance, or legal matters" exclusion in the system prompt.
Test query 3 (new): How does Vela's process work when a supplier misses a delivery window?
- VERIFY: This is a legitimate in-scope query. A question about fulfilment process, not live data retrieval. The agent should attempt a reasonable answer based on the general knowledge embedded in the model, and it should not refuse or redirect. The answer does not need to be factually specific to Vela's actual process — the agent has no access to internal documentation yet. What matters is that it engages with the query type correctly rather than deflecting.
What a good result looks like: The agent behaves consistently with the scope definition from Step 4. In-scope queries get a genuine attempt. Out-of-scope queries get a clear redirect with a named referral. The phrasing reflects the prompt's instructions.

## Step 8: Document the architecture
The final step of this walkthrough is documentation, not configuration. Open a text document: This can be a simple notes file, a shared doc, or the Flowise canvas description field.
Write the following architecture summary for Vela's single-agent system:
Agent name: Vela Systems Operations Assistant v1
Architecture pattern: Single agent (deliberate choice: scope is narrow and stable, no specialist knowledge conflicts, failure isolation not required at this scale, coordination cost would exceed reliability benefit)
Inputs:
- Natural language operational queries in English or Dutch
- Source: internal Vela operations team members via the chat interface
- Out-of-scope inputs: HR queries, finance queries, legal queries, requests for live data, requests for document drafting
Outputs:
- Plain language responses within scope (1–3 sentences for simple queries)
- Clear redirects with named referrals for out-of-scope queries
- No fabricated data, no external actions, no commitments
Orchestration: Linear - Start → Agent → Direct Reply. No branches, no loops. Appropriate for uniform query handling at current scale.
Communication: Direct output reference (Agent Node output flows directly to Direct Reply Node). Flow State keys query_type and status_response are declared for future routing use. agent_scope key documents the active scope per execution.
State management: Memory enabled with allMessages. Appropriate for short focused sessions. Risk: context bleed in long sessions covering multiple unrelated queries. Revisit if session length increases significantly.
Deliberate exclusions:
- No tool connections (no live data access, deferred to a later sprint if scope expands)
- No Document Store connection (no retrieval, deferred)
- No routing logic (one agent handles all in-scope queries, justified by current scope)
This document is the architecture decision brief for Vela's single-agent system. It is what the Karmen Freight brief in the next lesson should look like, applied to a different organisation and a different problem.
## What you have built
A single-agent system that is designed rather than just configured. The canvas has three nodes, but the system prompt now reflects a deliberate scope decision, the Flow State schema is documented rather than empty by default, and the architecture choices are recorded rather than implicit.
The agent is not more powerful than the baseline. It is more predictable, more legible, and more maintainable. When Jonas needs to change the scope in a future sprint, he can read the documentation and understand what is changing and why, rather than reading a system prompt and guessing at the intent behind it.
## Summary
Designing a single-agent system is not primarily a canvas task. The canvas is the output; the documentation, the scope definition, and the deliberate decisions are the design. This walkthrough produced both: a refined Agentflow V2 canvas and a four-section architecture brief that could be handed to a new team member without explanation.
The next lesson asks you to produce the same brief for Karmen Freight, a logistics broker in Vienna, using a scenario you have not seen before. The framework is the same. The context is new.