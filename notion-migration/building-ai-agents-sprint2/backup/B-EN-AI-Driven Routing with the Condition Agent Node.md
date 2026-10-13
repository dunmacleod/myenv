# AI-Driven Routing with the Condition Agent Node

Notion page: https://app.notion.com/p/AI-Driven-Routing-with-the-Condition-Agent-Node-3669418319f380d9afd6c0052779156d
Backed up before n8n migration

> 💡 What you will work on in this lesson: Students replace the Condition Node with a Condition Agent Node to handle intent-based routing that keyword matching cannot resolve reliably.

## Setting the scene
In the previous lesson, Meridian's development team added deterministic routing using the Condition Node. The routing worked well for clear status requests but Test 3 exposed a real problem: the query "What is the escalation status procedure for severity level 2 issues?" routed to the live data path because the word "status" appeared in the sentence even though the query was genuinely asking about a policy procedure, not live engagement data.
Klaus Brandt reviewed the test results and flagged the issue immediately. If a consultant asks about an escalation procedure and gets a placeholder response about live data lookup, the agent has failed. Not because of a technical error, but because keyword matching cannot understand intent.
The development team's conclusion: the routing decision for Meridian's agent is not a rules problem. It is a classification problem. The agent needs to understand what the consultant is trying to do, not just match words in the query.
This is what the Condition Agent Node is built for.

## What the Condition Agent Node does differently
The Condition Agent Node provides AI-driven dynamic branching based on natural language instructions and context. It uses a Large Language Model to route the workflow. It analyzes provided input data against a set of user-defined scenarios guided by high-level natural language instructions that define the decision-making task. 
The LLM then determines which scenario best fits the current input context. This node is particularly useful for tasks like user intent recognition, complex conditional routing, or nuanced situational decision-making where simple predefined rules are insufficient.

The difference in practice:
[TABLE]
  |  | Condition Node | Condition Agent Node |
  | How it decides | Evaluates a fixed rule | Asks an LLM to classify the intent |
  | Input | A value to compare | A text description of the decision task |
  | Routing basis | Keyword presence or value match | Semantic understanding of meaning |
  | Speed | Instant: no model call | Slower: requires a Gemini API call |
  | Handles ambiguity | No | Yes |
  | Best for | Clear unambiguous triggers | Intent-based or nuanced routing |
For Meridian's routing problem, the Condition Agent Node is the correct tool.

## What you are building
An updated Meridian Base Agent canvas where the Condition Node is replaced with a Condition Agent Node. The two output paths remain the same:
- Path A: Knowledge and policy queries → Agent Node with Document Store
- Path B: Live engagement status requests → Placeholder Direct Reply Node
The routing decision is now made by Gemini interpreting the consultant's intent rather than by a keyword rule.

### Step 1: Open the Meridian Base Agent canvas
Open Flowise at http://localhost:3000. Click Agentflows and open your Meridian Base Agent canvas.
Your canvas should look like this:
![image]((notion-hosted file))
### Step 2: Remove the Condition Node
Click the Condition Node to select it. Delete it from the canvas.
Also delete the lines that were connected to it:
- The line from Start Node to Condition Node
- The line from Condition Node true output to Direct Reply B
- The line from Condition Node false output to Agent Node
The Start Node, Agent Node, Direct Reply A, and Direct Reply B should all remain on the canvas.

### Step 3: Add a Condition Agent Node
Click (+) on the canvas. Under the Agentflow category, select Condition Agent and add it to the canvas. Position it in the same location where the Condition Node was: between the Start Node and the Agent Node.

### Step 4: Configure the Condition Agent Node
Click the Condition Agent Node to open its settings. Configure as follows:
Model: Select Google Gemini and connect your saved Gemini credential. Set the model to gemini-3.1-flash-lite.
Instructions: 
> 
  You are a query classifier for Meridian Consulting's internal agent. Your task is to determine whether the consultant's query is requesting live engagement status data for a specific client project, or whether it is asking about Meridian's internal policies, procedures, documentation, or general knowledge. Classify the query as "status_request" only when the consultant is explicitly asking for the current live status, progress update, or real-time information about a specific named client engagement or project. Classify the query as "knowledge_query" for everything else including questions about Meridian's internal policies, procedures, escalation rules, regional guidelines, project classification, or any other knowledge base content, even if the word "status" appears in the query in a different context.
Input:
```powershell
{{ $flow.input }}
```
Scenarios: Add two scenarios in order.
[TABLE]
  | Scenario | Label |
  | Scenario 0 | knowledge_query |
  | Scenario 1 | status_request |

### Step 5: Connect the Condition Agent Node
Connect everything so it should look like this.
![image]((notion-hosted file))
### Step 6: Update the Start Node Flow State
Click the Start Node and update the Flow State to add a second key that will track the routing decision for use by downstream nodes in later sprints:
[TABLE]
  | Key | Initial Value |
  | query_type | knowledge |
  | routing_decision | `` |
The routing_decision key starts empty and can be updated by the Condition Agent Node output in future extensions of this flow. For now, initialising it here ensures it is available when needed. Save the Start Node settings.

### Step 7: Save and run the routing test
Save the canvas. Open the chat icon and run the following five queries. Open a new chat session between each test.
Test 1 - Clear knowledge query: What are the project classification tiers at Meridian?
- Expected: Routes to Agent Node. Returns policy content from Document Store.
Test 2 - Clear status request: Can you check the engagement status for the Krauss account?
- Expected: Routes to Direct Reply B. Returns placeholder response.
Test 3 - Ambiguous query with "status" in a policy context: What is the escalation status procedure for severity level 2 issues?
- Expected: Routes to Agent Node. The Condition Agent Node interprets this as a knowledge query because it is asking about a procedure, not requesting live project data. This is the query that failed before.
Test 4 - Regional knowledge query: What should I know about running an engagement in Poland?
- Expected: Routes to Agent Node. Returns Regional Playbook content.
Test 5 - Explicit live data request: What is the current progress on the Bauer Manufacturing engagement?
- Expected: Routes to Direct Reply B. The Condition Agent Node identifies this as a request for live project data.

### Checklist: Confirm before moving on
- [ ] Condition Node and its edges removed from the canvas
- [ ] Condition Agent Node added and positioned between Start Node and Agent Node
- [ ] Model configured to gemini-3.1-flash-lite with saved credential
- [ ] Instructions field populated with the full classification prompt
- [ ] Input field set to {{ $flow.input }}
- [ ] Two scenarios configured knowledge_query and status_request in correct order
- [ ] Start Node connected to Condition Agent Node
- [ ] knowledge_query output connected to Agent Node
- [ ] status_request output connected to Direct Reply B
- [ ] routing_decision key added to Flow State in Start Node
- [ ] Canvas saved before testing
- [ ] All five test queries run
- [ ] Test 3 correctly routes to Agent Node confirming intent-based routing works

> 💡 Takeaway: 
  The Condition Agent Node makes routing decisions the way a human would by understanding what the consultant is trying to accomplish, not by matching words in the query. 
  This comes at a cost: every routing decision requires a Gemini API call, which adds latency compared to the Condition Node's instant rule evaluation. The right choice between the two depends on the nature of the routing problem. When triggers are clear and unambiguous, use the Condition Node. When intent matters more than keywords, use the Condition Agent Node.
