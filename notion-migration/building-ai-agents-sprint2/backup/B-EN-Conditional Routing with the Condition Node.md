# Conditional Routing with the Condition Node

Notion page: https://app.notion.com/p/Conditional-Routing-with-the-Condition-Node-3669418319f380b58de6c5c416629991
Backed up before n8n migration

> 💡 What you will work on in this lesson: Add deterministic branching to the Meridian Agentflow v2 using the Condition Node, routing queries down different execution paths based on defined rules.

## Setting the scene
Meridian's agent can now hold a conversation, retrieve grounded knowledge from internal documents, and respond within a clearly defined scope. The next challenge the development team has identified is routing.
During a pilot session, a consultant asked the agent to check the engagement status for a specific client project. The agent retrieved a chunk from the Operations Handbook about project classification tiers, technically related, but not what the consultant needed. The consultant needed live engagement data, not policy documentation.
The problem is that the agent is currently a single path where every query goes to the Agent Node, which then decides what to do. As the agent gains more capabilities, that single-path architecture becomes a bottleneck. Queries that need live data compete with queries that need document retrieval, and the agent has to reason its way to the right tool every time.
Conditional routing solves this by making some decisions explicit and deterministic. Instead of asking the agent to figure out whether a query needs live data or knowledge retrieval, the Condition Node evaluates a rule and routes the query before the agent even sees it.

## What you are building
An updated Meridian Base Agent canvas that routes incoming queries into two paths using a Condition Node:
- Path A - Knowledge queries: Queries about Meridian's internal policies, procedures, and regional context go to the Agent Node with Document Store knowledge retrieval
- Path B - Status queries: Queries that contain specific trigger phrases indicating a live data need are routed to a separate Direct Reply Node with a placeholder response
Path B will be connected to a live HTTP Node later. For now, the routing structure is built and verified with a placeholder.

## What the Condition Node does
The Condition Node routes the workflow based on a fixed rule. It compares input values using logical operators like equals, contains, greater than, or is empty. If the rule evaluates to true, execution continues down the true branch; if false, down the false branch.
The key word is deterministic. Unlike the Condition Agent Node, the Condition Node evaluates a fixed rule. The outcome is always the same for the same input. This makes it the right choice when the routing logic is clear and does not require interpretation.

### Step 1: Open the Meridian Base Agent canvas
Open Flowise at http://localhost:3000. Click Agentflows and open your Meridian Base Agent canvas.
Your canvas should currently show:
Start Node → Agent Node → Direct Reply Node
With the meridian-knowledge Document Store connected to the Agent Node's Knowledge configuration.

### Step 2: Initialize Flow State in the Start Node
All state keys that will be used throughout the workflow must be initialized with their default values using the Flow State parameter within the Start Node. This step effectively declares the schema or structure of your Flow State for that workflow. 
Click the Start Node to open its settings. Find the Flow State section and add the following key-value pair:
[TABLE]
  | Key | Initial Value |
  | query_type | knowledge |
This key will be used by the Condition Node to determine which path to take. It defaults to knowledge — meaning all queries are treated as knowledge queries unless the routing rule changes it.
Save the Start Node settings.

### Step 3: Add a Condition Node to the canvas
Click (+) on the canvas. Under the Agentflow category, select Condition and add it to the canvas.
Position it between the Start Node and the Agent Node. Your canvas layout should now read left to right:
Start Node → Condition Node → Agent Node → Direct Reply Node
![image]((notion-hosted file))

### Step 4: Rewire the canvas
The current edge runs directly from Start Node to Agent Node. This needs to change — the Condition Node now sits between them.
1. Delete the existing edge between Start Node and Agent Node
1. Draw a new edge from the Start Node output to the Condition Node input
1. Keep the existing edge from Agent Node to Direct Reply Node
The Condition Node will have two output anchors (one for true and one for false). You will connect these in Step 6.

### Step 5: Configure the Condition Node
Click the Condition Node to open its settings. Configure the condition as follows:
[TABLE]
  | Field | Value |
  | Type | String |
  | Value 1 | {{ question }} |
  | Operation | contains |
  | Value 2 | status |
![image]((notion-hosted file))
This rule evaluates whether the user's input contains the word status. If true, the query is a status request and should be routed to a live data lookup. If false, it is a knowledge query and should go to the Agent Node.
> Why contains and not equals: Consultants phrase queries naturally "What is the status of the Krauss account?" or "Can you check the engagement status for Bauer?" The word status will appear in different positions and sentence structures. The contains operator catches all of these without requiring an exact phrase match.


### Step 6: Connect the Condition Node outputs
The Condition Node has two output anchors:
True output (contains "status"):
- Add a new Direct Reply Node to the canvas for Path B
- Connect the true output of the Condition Node to this new Direct Reply Node
- In the new Direct Reply Node's Message field, enter:
Live engagement status lookup is not yet configured. Please contact your engagement manager directly for current project status.
This is the placeholder response for Path B. It will be replaced with the HTTP Node output in the lesson on live data lookups.
False output (does not contain "status"):
- Connect the false output of the Condition Node to the existing Agent Node
Your canvas should now show:
![image]((notion-hosted file))
### Step 7: Confirm the existing Direct Reply Node
Click the original Direct Reply Node (Path A connected to the Agent Node) and confirm the Message field is still set to:
{{ agentAgentflow_0.output }}
If it has been cleared, re-enter it using the {{ variable selector.

### Step 8: Save and run the routing test
Save the canvas. Click the chat icon and run the following four queries in separate sessions. Open a new chat session between each test to avoid cross-session context:
Test 1 - Knowledge query (should route to Agent Node): What are the project classification tiers at Meridian?
- Expected: Agent Node retrieves from Document Store and returns policy content.
Test 2 - Status query (should route to placeholder Direct Reply): Can you check the engagement status for the Krauss account?
- Expected: Placeholder response about live status not yet configured.
Test 3 - Knowledge query with the word "status" in a different context: What is the escalation status procedure for severity level 2 issues?
- Expected: This query contains the word "status" and will route to Path B. Note this result because it reveals a limitation of the contains rule that will be addressed using the Condition Agent Node.
Test 4 - Regional query (should route to Agent Node): What should I know about running an engagement in Poland?
- Expected: Agent Node retrieves the Poland section from the Regional Playbook.

### What Test 3 reveals
Test 3 is deliberately designed to expose the limitation of deterministic routing. The query is genuinely about knowledge. It asks about an escalation procedure, but the word "status" triggers the wrong path. This is the core trade-off of the Condition Node:
[TABLE]
  |  | Condition Node | Condition Agent Node |
  | Routing method | Fixed rule: keyword match | AI reasoning: intent interpretation |
  | Speed | Fast: no model call | Slower: requires a model call |
  | Accuracy on clear queries | High | High |
  | Accuracy on ambiguous queries | Low: keywords can mislead | High: intent is understood |
  | Best for | Clear, unambiguous triggers | Nuanced, intent-based routing |
### Checklist: Confirm before moving on
- [ ] Flow State initialised in Start Node with key query_type set to knowledge
- [ ] Condition Node added to canvas between Start Node and Agent Node
- [ ] Start Node connected to Condition Node by a visible edge
- [ ] Condition Node configured - Type: String, Value 1: {{ $flow.input }}, Operation: contains, Value 2: status
- [ ] True output connected to Path B Direct Reply Node with placeholder message
- [ ] False output connected to Agent Node
- [ ] Agent Node connected to Path A Direct Reply Node
- [ ] Path A Direct Reply Node Message field set to {{ agentAgentflow_0.output }}
- [ ] Canvas saved before testing
- [ ] All four test queries run and results evaluated
- [ ] Test 3 result noted as a known limitation of deterministic routing

> 💡 Takeaway: 
  The Condition Node is a precise, fast, and reliable routing mechanism when the routing logic is unambiguous. Keyword-based rules work well when trigger phrases are distinct and do not appear in other contexts. When the same word or phrase can mean different things depending on context, deterministic routing produces incorrect results that are silent and hard to detect. 
  The next lesson introduces a routing approach that interprets intent rather than matching strings, the Condition Agent Node.