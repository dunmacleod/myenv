# Processing Data Sets with the Iteration Node

Notion page: https://app.notion.com/p/Processing-Data-Sets-with-the-Iteration-Node-3669418319f38057b5d9c0928ee0be54
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: You will add an Iteration Node to a new Agentflow v2 to process a list of engagement records and generate a summary for each one.

## Setting the Scene
Meridian's operations manager has requested a new capability, a weekly engagement briefing that loops through a list of active client accounts and produces a one-line status summary for each one. Rather than a consultant querying each account manually one at a time, the agent should process the entire list in a single execution and return all summaries together.
This is a fundamentally different pattern from what has been built so far. The existing canvas handles one query at a time. Processing a collection of items requires a different node. This is known as the Iteration Node.

## What the Iteration Node does
The Iteration Node executes a defined sub-flow (a sequence of nodes nested within it) for each item in an input array, implementing a for-each loop. For every individual element within that array, the Iteration Node sequentially executes the sequence of nodes visually placed inside its boundaries on the canvas.
This makes it the correct tool for any task where the same operation needs to run repeatedly across a collection of inputs by processing multiple documents, summarising multiple records, or validating a list of values.

## What you are building
A new standalone Agentflow v2 called Meridian Engagement Briefing that takes a hardcoded list of engagement records, iterates over each one using an LLM Node inside the Iteration Node, and returns a combined briefing summary.
This is built as a separate flow to keep the two use cases clean and independent.

### Step 1: Create a new Agentflow v2
Click Agentflows in the left navigation and click + Add New. Name it Meridian Engagement Briefing and save immediately.

### Step 2: Go to Start Node and initialise Flow State
[COLUMN_LIST]
  [COLUMN]
    Add a Start Node. In the Flow State section, add:
    [TABLE]
      | Key | Initial Value |
      | engagement_list | [{"id":1,"title":"Krauss Manufacturing","completed":false},{"id":2,"title":"Bauer Logistics","completed":true},{"id":3,"title":"Novak Retail","completed":false}] |
      | briefing_output | `` |
    
  [COLUMN]
    > ➡️ The engagement_list key holds a JSON array of three mock engagement records. The briefing_output key will accumulate summaries as the iteration runs.
    Save your Start node.
    
### Step 3: Add a Custom Function Node to parse the list
Add a Custom Function Node after the Start Node.
Input Variables:
[TABLE]
  | Variable Name | Variable Value |
  | engagementList | {{ $flow.state.engagement_list }} |
JavaScript Function:
```javascript
const list = JSON.parse($engagementList);
return JSON.stringify(list);
```
Update Flow State:
[TABLE]
  | Key | Value |
  | engagement_list | {{ customFunctionAgentflow_0.output }} |
This confirms the list is valid JSON before passing it to the Iteration Node.

### Step 4: Add an Iteration Node
Add an Iteration Node after the Custom Function Node.
Configure it:
[TABLE]
  | Field | Value |
  | Array Input | {{ $flow.state.engagement_list }} |
The Array Input specifies the input array the node will iterate over, provided by referencing a variable that holds an array from a previous node's output or from Flow State.

### Step 5: Add an LLM Node inside the Iteration Node
Place an LLM Node inside the Iteration Node boundaries on the canvas. 
Configure it:
- Model: Select your model and API credential.
- Messages - System role: You are a briefing assistant for Meridian Consulting. Generate a single sentence engagement status summary from the data provided. Be concise and professional.
- Messages - User role: Engagement data: {{ $iteration.item }}. Generate a one-sentence status summary.
> ➡️ Note: {{ $iteration.item }} is the variable that holds the current item being processed inside the Iteration Node. Each time the loop runs, this variable contains one engagement record from the array.

### Step 6: Add a Direct Reply Node
The Iteration Node provides a single output anchor that becomes active only after the nested sub-flow has completed execution for all items in the input array. Add a Direct Reply Node after the Iteration Node output. In the Message field, type {{ and select the Iteration Node's output variable. 
It should be {{iterationAgentflow_0}}. 
Save the canvas. It should look like this when you are done.
![image]((notion-hosted file))
### Step 7: Test
Open the chat interface and send: Generate the weekly engagement briefing
- Expected: The Iteration Node processes all three engagement records, the LLM Node generates a one-sentence summary for each, and the Direct Reply Node returns all three summaries together.

> 💡 Takeaway: 
  The Iteration Node handles collection processing that would otherwise require multiple manual queries or a custom scripted loop. The key design principle is that nodes inside the Iteration Node boundary execute per item while nodes outside execute once after all items are processed. Understanding this boundary is what makes the difference between a flow that processes a list correctly and one that processes only the first item or collapses all items into a single pass.
