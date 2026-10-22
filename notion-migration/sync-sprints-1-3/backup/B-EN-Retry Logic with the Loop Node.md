# Retry Logic with the Loop Node

Notion page: https://app.notion.com/p/Retry-Logic-with-the-Loop-Node-3669418319f38002b22bf1c6991c0305
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Students add a Loop Node to the Meridian Agentflow v2 to handle HTTP failures with automatic retry logic and a controlled exit path.

## Setting the Scene
Meridian's HTTP Node on Path B currently handles one response (success or failure). When the engagement status API is temporarily unavailable, Agent Node B returns a fallback message and the consultant has to try again manually. For a tool used frequently throughout the working day, that is friction the development team wants to eliminate.
The solution is retry logic by automatically re-attempting the HTTP call a defined number of times before falling back. The Loop Node enables the creation of cycles or iterative retries within a workflow. When execution reaches the Loop Node, it redirects back to a specified target node that has already been executed earlier in the current run, causing its re-execution along with any subsequent nodes in that part of the flow.

## What you are adding
An updated Path B that retries the HTTP Node up to two times when the API returns an error, before routing to a fallback Direct Reply Node. The success path bypasses the retry logic entirely and goes straight to Agent Node B for formatting.
> ⚠️ Before you begin, make sure you open your Docker Desktop. Under Actions, turn on Flowise and Qdrant. 

### Step 1: Update the Condition Agent node
Before adding the retry logic, the Condition Agent Node needs two updates to ensure reliable routing.
Scenario order:
- Scenario 0: status_request
- Scenario 1: knowledge_query
Rewire outputs:
- Output 0 → HTTP Node
- Output 1 → Agent Node A
Replace the Instructions field with this:
> 
  You are a query classifier for Meridian Consulting's internal agent.
  Classify the input as "status_request" FIRST if it contains any of these signals:
  - asks to "check", "look up", "retrieve", or "pull up"
  - mentions "account", "account number", or "account reference"
  - asks for current status of a specific project or client
  Classify as "knowledge_query" only if none of the above apply. Default to "status_request" when uncertain.
Confirm these settings:
- Input: {{ $flow.input }} typed manually, not selected from dropdown
- Memory: Off
Save the canvas.

### Step 2: Add a retry counter to Flow State
Click the Start Node and select + Add Flow State. Enter the following:
- Key: retry_count
- Initial value: 0

### Step 3: Add Condition node after the HTTP node
Add a Condition Node immediately after the HTTP Node on Path B. Connect the HTTP Node output to Condition input.
Configure Condition A:
[TABLE]
  | Field | Value |
  | Type | String |
  | Value 1 | {{ httpAgentflow_0.data }} |
  | Operation | Is Empty |
This checks whether the HTTP response contains data before deciding which path to take.
- Output 0 (true: data is empty, HTTP failed): Connect to the Custom Function node
- Output 1 (false: data exists, HTTP succeeded): Connect to the Agent 2 node

### Step 4: Add a Custom Function Node after Condition A
Click (+) and add a Custom Function Node on the failure branch of Condition A. Connect Condition A output 0 (the empty/failed branch you wired in Step 3) to the Custom Function Node input. The Custom Function Node only runs when the HTTP call has returned no data, which is the only situation in which the retry counter should be incremented.
![image]((notion-hosted file))
Configure it as follows:
Input Variables:
![image]((notion-hosted file))
JavaScript Function:
```javascript
const count = parseInt($retryCount) || 0;
return String(count + 1);
```
Update Flow State:
![image]((notion-hosted file))
This increments the retry counter each time the HTTP call is attempted.

### Step 5: Add a Condition Node to check retry count
Add a Condition node after the Custom Function node. 
Configure it:
![image]((notion-hosted file))
This evaluates whether the retry count has exceeded 2.
- Output 0 (true: retry count exceeds 2): Connect to Direct Reply C
- Output 1 (false: retry count is 2 or below): Connect to the Loop Node

### Step 6: Add Direct Reply C
Add a Direct Reply node connected to Condition B output 0.
In the message field, enter the following:
> 
  The engagement status service is currently unavailable. Please contact your engagement manager directly for current project status.

### Step 7: Add the Loop Node
Add a Loop Node connected to Condition B output 1. Configure it:
[TABLE]
  | Field | Value |
  | Loop Back To | Select the HTTP Node |
  | Max Loop Count | 2 |
The Loop Node does not have a standard forward-pointing output anchor. Its primary function is to redirect execution flow backward to the Loop Back To target node.

### Step 8: Connect Agent Node B and Direct Reply B
Connect Condition A output 1 to Agent 2 node. Confirm Agent 2 node is configured with your Gemini model, system message, and no document store is connected.
Connect Agent 2 node output to Direct Reply B node. In the Direct Reply B Message field, type {{ and select Agent Node B's output variable from the dropdown.

### Here is the complete diagram
![image]((notion-hosted file))
### Step 9: Test the retry logic
Test 1: Simulate API failure - Change the HTTP Node URL to an invalid endpoint: https://jsonplaceholder.typicode.com/invalid/9999
- Save and send: Can you check the engagement status for account 1?
- Expected: The flow retries twice, then routes to the fallback Direct Reply.
Test 2: Restore and confirm success path: - Restore the URL to: https://jsonplaceholder.typicode.com/todos/1
- Send the same query. 
- Expected: HTTP Node succeeds on the first attempt and Agent Node B returns a formatted status response.

> 💡 Takeaway: 
  The Loop Node adds resilience to Meridian's canvas by handling transient failures automatically. The key design principle is that the Loop Node provides the backward redirect, but the Condition Node provides the exit. Every loop needs both.