# First AI-Powered Agentflow v2

Notion page: https://app.notion.com/p/First-AI-Powered-Agentflow-v2-3669418319f38082ae3ef82ece0ce65b
Backed up before n8n migration

> 💡 What you will do in this lesson: Build and test a minimal working Agentflow v2 in Flowise by connecting a Start Node, an Agent Node configured with Gemini, and a Direct Reply Node, then confirm it is working through a structured two-turn test.

## Why this is the starting point?
Meridian Consulting's team understands the stack, the interface, and the Agentflow v2 node graph. Now they need to build something that actually works. The goal at this stage is confirmation. A minimal Agentflow v2 that receives a user message, reasons with Gemini, and returns a coherent response is the foundation everything else is built on.
Before adding retrieval, branching, tools, or custom instructions, the team needs to know that the core loop (user input, agent reasoning, response output) is functioning correctly. A baseline that has not been verified is an assumption.
This walkthrough takes you through the construction of that baseline step-by-step.

### Step 1: Create a new Agentflow v2
Open your Flowise at http://localhost:3000 and navigate to Agentflows in the left-hand navigation panel. Click + Add New to open a blank canvas.
Give the flow a descriptive name by clicking the default name field at the top of the screen and typing Meridian Base Agent. Save immediately using the save icon in the top right corner.
> ➡️ Why this matters: Flowise does not autosave. Naming and saving before building prevents losing work if the browser tab is closed or the server process is interrupted.

### Step 2: Add a Start node
Whenever you start a new Agentflow, a Start node is usually there. If not, click the (+) button on the canvas. Under the Agentflow category, locate Start and add it to the canvas. Position it on the left side of the workspace.
The Start Node is the mandatory entry point of every Agentflow v2. It receives the user's input and passes it into the flow. Without it, the flow has no entry point and cannot execute.
In the Start Node settings panel, leave the default configuration in place for now. The input type is set to Chat by default, which is correct for this agent.

### Step 3: Add an Agent Node
Click (+) again. Under the Agentflow category, locate Agent and add it to the canvas. Position it to the right of the Start Node.
The Agent Node is the reasoning engine of the flow. It connects to a language model, holds the system prompt, and decides what action to take based on the input it receives.
Configure the Agent Node as follows:
- Connect Credential: Open the agent, select Model and fill in the details. Select the OpenRouter API key saved in your credentials manager. If it does not appear, navigate to Credentials in the left navigation panel and confirm the key was saved correctly.
- Model: Select your model from the model dropdown.
- Temperature: Leave at the default value for now.
- System Prompt: Leave blank for this baseline test. A system prompt will be added later.

### Step 4: Add a Direct Reply Node
Click (+) again. Under the Agentflow category, locate Direct Reply and add it to the canvas. Position it to the right of the Agent Node.
The Direct Reply Node sends the agent's response back to the user and ends that branch of execution. 
After adding the Direct Reply Node, click on it to open its settings. In the Message field, type {{ to open the variable selector and choose the Agent Node's output. It should be the following:
```powershell
{{ agentAgentflow_0 }}
```
This connects the agent's response to the reply sent to the user. Without this, the flow executes successfully but returns nothing to the chat interface.

### Step 5: Connect the Nodes
Draw the following connections in order:
1. Click and hold the output socket on the Start Node. Drag the edge to the input socket on the Agent Node and release.
1. Click and hold the output socket on the Agent Node. Drag the edge to the input socket on the Direct Reply Node and release.
Your canvas should now show a straight three-node chain: Start Node → Agent Node → Direct Reply Node
If an edge disappears after connecting, the socket types are incompatible. Confirm you are connecting output to input in the correct direction (left to right).
Save the canvas.
![image]((notion-hosted file))
### Step 6: Save and run the two-turn test
Save your Agentflow. Click the purple chat icon in the top right corner of the canvas to open the built-in test interface.
Run the following two-turn conversation:
> Turn 1: "My name is Lena and I am working on the Krauss Manufacturing account."
![image]((notion-hosted file))
> Turn 2: "Which client account am I working on?"
![image]((notion-hosted file))
What to look for:
- If the agent responds with Krauss Manufacturing or references Lena's name in Turn 2, the AI model connection is active and the Agent Node is correctly retaining conversation context within the session.
- If the agent asks which account in Turn 2, the Agent Node's built-in session memory is not active. Confirm the model is correctly configured and the canvas has been saved before testing.

## Checklist: Confirm before moving on
- [ ] New Agentflow v2 created, named Meridian Base Agent, and saved before building
- [ ] Start Node added to the canvas
- [ ] Agent Node added, AI credential connected and model selected
- [ ] Direct Reply Node added to the canvas
- [ ] Start Node connected to Agent Node by a visible edge
- [ ] Agent Node connected to Direct Reply Node by a visible edge
- [ ] Canvas saved before testing
- [ ] Two-turn test completed and agent recalled the account name in Turn 2 without being prompted

## Check for Understanding
>  A Meridian developer runs the two-turn test and the agent asks for the account name again in Turn 2. The canvas has been saved. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/3a22830f-d34d-415d-9612-c2de1a9c1627

> 💡 Takeaway: 
  A working minimal Agentflow v2 (Start Node, Agent Node, Direct Reply Node) is the verified starting condition for everything that follows. Every capability added from this point forward builds on this core loop. 
  Verifying it now through a structured two-turn test means that any problems encountered later can be attributed to what was added, not to what was already there.