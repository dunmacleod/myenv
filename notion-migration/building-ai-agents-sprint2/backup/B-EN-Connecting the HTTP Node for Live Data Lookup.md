# Connecting the HTTP Node for Live Data Lookup 

Notion page: https://app.notion.com/p/Connecting-the-HTTP-Node-for-Live-Data-Lookup-3669418319f3804692f4ea571717b406
Backed up before n8n migration

> 💡 What you will work on in this lesson: Replace the Path B placeholder Direct Reply Node with an HTTP Node connected to a mock API endpoint, completing the live data lookup path in the Meridian Agentflow v2.

## Setting the scene
Meridian's routing is now working correctly. The Condition Agent Node classifies consultant queries by intent and sends them down the right path. Knowledge queries go to the Agent Node with Document Store retrieval. Status requests go to Path B which currently returns a placeholder message telling the consultant to contact their engagement manager directly.
That placeholder was always temporary. Klaus Brandt has now confirmed that Meridian's operations team has a simple internal API that returns engagement status data for a given client name. The development team's next task is to connect Path B to that API using the HTTP Node, so that when a consultant requests live engagement status, the agent actually retrieves it.
For this lesson, a publicly available mock API is used in place of Meridian's real internal API. The configuration steps are identical to what would be used with a real endpoint. Only the URL and response format differ.

## What you are building
An updated Meridian Base Agent canvas where the Path B placeholder Direct Reply Node is replaced with:
- An HTTP Node that makes a GET request to a mock API
- An Agent Node (a second, lightweight instance) that formats the raw API response into a natural language reply
- A Direct Reply Node that returns the formatted response to the consultant
The Path A flow (Condition Agent Node → Agent Node → Direct Reply A) remains unchanged.

## The mock API
This lesson uses JSONPlaceholder, a free public mock API that returns realistic-looking JSON data. It requires no authentication and no account.
The endpoint used is:
```xml
https://jsonplaceholder.typicode.com/todos/1
```
This returns a JSON object representing a task item. In the lesson, this is treated as a mock engagement record. You map the response fields to Meridian engagement data for the purpose of building and testing the HTTP Node configuration.
> ➡️ Why a mock API: Meridian's internal API does not exist outside this business case. Using JSONPlaceholder allows the HTTP Node configuration to be built and tested against a real live endpoint with real responses, making the technical steps accurate and verifiable. We will later look at how to cover the response handling and failure logic which apply identically to real APIs.

## Your tasks
### Step 1: Open the Meridian Base Agent canvas
Open Flowise at http://localhost:3000. Click Agentflows and open your Meridian Base Agent canvas.
It should look like this.
![image]((notion-hosted file))
### Step 2: Remove the placeholder Direct Reply Node
Click Direct Reply B and delete it. Also delete the connecting line between the Condition Agent Node's status_request output to it.
The Condition Agent Node's status_request output anchor is now unconnected.

### Step 3: Add the HTTP Node
Click (+) on the canvas. Under the Agentflow category, select HTTP and add it to the canvas. Position it where Direct Reply B was.
Connect the Condition Agent Node status_request output to the HTTP Node input.

### Step 4: Configure the HTTP Node
Click the HTTP Node to open its settings. Configure as follows:
![image]((notion-hosted file))
What the response looks like: JSONPlaceholder returns the following JSON for this endpoint:
```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```
In the lesson context, treat this as a mock engagement record where title represents the engagement name, completed represents whether the engagement is closed, and id represents the engagement reference number.

### Step 5: Update Flow State for the HTTP response
Click the Start Node and scroll to Update Flow State. Add the following:
[TABLE]
  | Key | Initial Value |
  | status_response | `` |
All state keys that will be used throughout the workflow must be initialized with their default values using the Flow State parameter within the Start Node. Save the Start Node.

### Step 6: Add a second Agent Node for response formatting
The HTTP Node returns raw JSON. A consultant asking about engagement status should receive a natural language response, not a JSON object. A lightweight Agent Node sits after the HTTP Node to convert the raw response into readable output. Click (+) and add a second Agent Node to the canvas. Position it to the right of the HTTP Node. Connect the HTTP Node output to this new Agent Node input.
Configure the second Agent Node as follows:
Model: OpenRouter API (Gemini).
Messages - System role:
> 
  You are a response formatter for Meridian Consulting's internal agent. You receive raw engagement data retrieved from Meridian's operations API and convert it into a clear, professional natural language summary for the consulting team. Format the engagement information clearly. Include the engagement reference, name, and current status. Keep the response concise, two to three sentences maximum. Do not add information that is not present in the data.
Messages - User role:
> 
  Here is the engagement data retrieved from the API: {{httpAgentflow_0}}. Please format this as a professional engagement status summary for the consultant.
Do not connect the meridian-knowledge Document Store to this Agent Node. This node has a single formatting task. It does not need knowledge retrieval.

### Step 7: Add Direct Reply B
Click (+) and add a Direct Reply Node to the canvas. Position it to the right of the second Agent Node. Connect the second Agent Node output to this Direct Reply Node input.
In the Message field, type {{ and select the second Agent Node's output from the variable selector.
The variable name will be {{agentAgentflow_1}}; confirm the exact name from the selector.
### Step 8: Confirm the full canvas structure
Your canvas should now show:
![image]((notion-hosted file))
With meridian-knowledge Document Store connected to Agent Node A only. Save the canvas.
### Step 9: Run the end-to-end test
Open the chat icon and run the following tests in separate sessions.
Test 1 - Knowledge path still works: What are the project classification tiers at Meridian?
- Expected: Routes to Agent Node A. Returns policy content from Document Store. Confirms Path A is unaffected by the Path B changes.
Test 2 - Status path with HTTP Node: Can you check the engagement status for the Krauss account?
- Expected: Routes through Condition Agent Node to HTTP Node. HTTP Node fetches from JSONPlaceholder. Agent Node B formats the response. Direct Reply B returns a natural language engagement summary.
Test 3 - Ambiguous query still routes correctly: What is the escalation status procedure for severity level 2 issues?
- Expected: Condition Agent Node correctly routes to Agent Node A. Returns procedure content from Document Store.

### What a successful Test 2 looks like
The consultant should receive a response similar to:
> "The engagement record shows reference number 1, titled 'delectus aut autem', with a current status of open (not yet completed). Please confirm with your engagement manager if this record matches the Krauss account details."
The exact wording depends on how Gemini formats the mock data. What matters is that the response is natural language and draws from the actual API response.
> ⚠️ Known limitation: The Flowise GitHub issues note that passing HTTP Node output directly into downstream nodes via {{ variable }} syntax can sometimes be evaluated as a literal string rather than a resolved value in certain Flowise versions. If the second Agent Node receives {{ httpAgentflow_0.data }} as plain text rather than the actual JSON data, use the Update Flow State approach confirmed in Step 5 reading from {{ $flow.state.status_response }} in the User message instead, which is the more reliable method for passing HTTP Node output downstream.

### Checklist: Confirm before moving on
- [ ] Placeholder Direct Reply B removed from canvas
- [ ] HTTP Node added and connected to Condition Agent Node status_request output
- [ ] HTTP Node configured: GET method, JSONPlaceholder URL, JSON response type
- [ ] status_response key added to Start Node Flow State
- [ ] HTTP Node Update Flow State configured to write response to status_response
- [ ] Second Agent Node added and connected to HTTP Node output
- [ ] Second Agent Node configured with formatting system prompt and User message referencing {{ $flow.state.status_response }}
- [ ] No Document Store connected to second Agent Node
- [ ] Direct Reply B added and connected to second Agent Node output
- [ ] Canvas saved before testing
- [ ] Test 1 confirms Path A is unaffected
- [ ] Test 2 returns a formatted natural language engagement summary
- [ ] Test 3 confirms ambiguous routing still works correctly

> 💡 Takeaway: 
  A tool is only as useful as the description that governs when the model invokes it. The mock code, the input schema, and the Flowise canvas configuration are all necessary, but the tool description is what determines whether your AI model reaches for the tool at the right moment. 
  A description that is too vague produces routing failures. A description that overlaps with the knowledge base produces confusion. The precision required to distinguish two overlapping capabilities in natural language is the practical skill this lesson develops.
