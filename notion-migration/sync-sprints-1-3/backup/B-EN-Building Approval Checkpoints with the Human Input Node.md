# Building Approval Checkpoints with the Human Input Node

Notion page: https://app.notion.com/p/Building-Approval-Checkpoints-with-the-Human-Input-Node-37d9418319f3809eb3a6e834163c1507
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: You will add a Human Input Node to the Meridian Agentflow v2 to create an approval checkpoint before the agent returns a sensitive response.

## Setting the Scene
Meridian's senior partner Klaus Brandt has raised a governance concern. When a consultant requests engagement status data, the agent retrieves it and returns it immediately. But there was no review and no confirmation. For routine queries this is fine. For queries involving sensitive client accounts flagged for escalation, the agent should pause and ask for confirmation before proceeding.
The Human Input Node halts the automated progression of the workflow and presents information or a question to a human user via the chat interface. Once the user makes a selection and submits their response, the workflow resumes execution along the specific output path corresponding to their chosen action.
This is the Human-in-the-Loop pattern. The agent pauses at a defined checkpoint, presents what it is about to do, and waits for explicit approval before continuing.

## What you are building
An updated Path B that inserts a Human Input Node between Condition A and Agent Node B. When the HTTP Node returns data successfully, the agent presents the raw engagement record to the consultant and asks for confirmation before formatting and returning the final response.

### Step 1: Open the Meridian Base Agent canvas
Open Flowise at http://localhost:3000 and open your Meridian Base Agent canvas.

### Step 2: Disconnect and Reconnect Condition A outputs 0 and 1
- Delete the edge between Condition A output 0 and Agent 2 node. Place output 0 to Custom Function node.
- Delete the edge between Condition A output 1 and Custom Function node. 
> ➡️ Why are we doing this? The Human Input Node is a review checkpoint. It only adds value when there is something to review. If you remember the previous lessons, Pausing on a failed HTTP call and asking "do you want to proceed?" when there is no data to proceed with would confuse the consultant and serve no purpose. Thus, if the condition failed, then no human is needed. But if it is a success, then you need to review.

### Step 3: Add a Human Input Node
Click (+) and add a Human Input Node to the canvas. Position it between Condition A and Agent 2 node. Connect Condition A output 1 to the Human Input Node input.

### Step 4: Configure the Human Input Node
Click the Human Input Node to open its settings.
- Description Type: Select Fixed
- Description: The following engagement data has been retrieved. Do you want to proceed with generating the summary? {{ httpAgentflow_0.data }}
- Feedback: Toggle On
> ➡️ Why enable Feedback: If Feedback is enabled, the user will be prompted with a feedback window to leave their feedback, and this feedback will be appended to the node's output. Enabling this allows the consultant to add a note. For example flagging that the data looks incorrect before the agent formats the response.
The Human Input Node provides two output anchors corresponding to distinct user actions (proceed and reject).

### Step 5: Connect the Human Input Node outputs
- Proceed output: Connect to Agent Node B
- Reject output: Add a new Direct Reply Node with the message: Understood. The engagement summary has not been generated. Please contact your engagement manager directly if you need further information about this account.

### Step 6: Update the Start Node Flow State
Click the Start Node and forward-declare one new key for use in a later lesson. No node in this lesson writes to or reads from it; it is reserved as a slot so the Flow State stays consistent with the keys introduced later in the sprint.
[TABLE]
  | Key | Initial Value |
  | approval_status | `` |
Save the Start Node.
![image]((notion-hosted file))
### Step 7: Save and test
Save the canvas. Open the chat interface and send: Can you check the engagement status for account 1?
Expected flow:
1. Condition Agent Node routes to HTTP path
1. HTTP Node retrieves data
1. Condition A confirms data exists
1. Human Input Node pauses and displays the raw engagement data with Proceed and Reject buttons
1. Click Proceed. Agent Node B formats the response and Direct Reply B returns it.
1. Open a new session, run the same query, and click Reject. Direct Reply returns the rejection message.

### Checklist: Confirm before moving on
- [ ] Human Input Node added between Condition A output 1 and Agent Node B
- [ ] Description Type set to Fixed with the confirmation message and HTTP data variable
- [ ] Feedback enabled
- [ ] Proceed output connected to Agent Node B
- [ ] Reject output connected to a new Direct Reply Node with rejection message
- [ ] approval_status key added to Start Node Flow State
- [ ] Proceed path returns formatted engagement summary
- [ ] Reject path returns rejection message

> 💡 Takeaway: 
  The Human Input Node converts a fully automated path into a supervised one. The agent does the retrieval work and the consultant makes the final decision about whether to proceed. This pattern is essential for any action that is difficult to reverse or involves data that requires human verification before being surfaced. The checkpoint adds one interaction but eliminates an entire category of automated errors.
