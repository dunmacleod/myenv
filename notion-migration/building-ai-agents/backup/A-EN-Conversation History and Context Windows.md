# Conversation History and Context Windows

Notion page: https://app.notion.com/p/Conversation-History-and-Context-Windows-3669418319f38059ac3df3c183809bca
Backed up before n8n migration

> 💡 What you will do in this lesson: Configure a Flowise agent to retain conversation history across turns using a memory node, and validate that it is working correctly.

## Why this step comes now
Contigo GmbH's team has defined what the agent should remember and drafted a memory retention policy. The next step is implementation. Before building anything more complex the agent needs a working foundation: the ability to hold a conversation across multiple turns without losing context.
That is what this walkthrough covers. You will add a memory node to a Flowise agent, connect it correctly, and run a simple test to confirm the configuration is working before moving further.

## What you are building
A Flowise chatflow with a Buffer Memory node connected to a Conversational Chain. The memory node captures the ongoing dialogue and injects it back into each new prompt, giving the language model access to what has already been said in the current session.
This is short-term memory only. It exists for the duration of the active session and is cleared when the session ends. Persistent cross-session memory is addressed further on in this sprint.
> ✅ Important: Before you work on the steps below, make sure you have your Gemini API environment set up. Go to this link for instructions.

### Step 1: Open your Flowise canvas
Open your Flowise dashboard and navigate to Chatflows. Either open your existing project canvas or create a new Chatflow by clicking + Add New.
If you are starting from a blank canvas, you will see an empty workspace. Components are accessed by clicking the (+) button on the canvas.
![image]((notion-hosted file))

### Step 2: Add a Conversational Chain node
Go to (+) and under LangChain, in the search bar, search for Conversation Chain. Drag it onto the canvas.
The Conversation Chain acts as the central orchestrator for this flow. It manages the back-and-forth between the user and the language model, and it has dedicated input sockets for both a chat model and a memory component.
![image]((notion-hosted file))

### Step 3: Add and connect a chat model
Go to (+) and under LangChain, in the search bar, search for your preferred chat model node (OpenRouter) and drag it onto the canvas. 
Connect the ChatOpenRouter output from the node to the Chat Model input socket on the Conversation Chain. A socket is the typed connection point on a node that accepts a compatible input or output from another node. This connection tells the Conversation Chain which chat model to use when generating responses.
Go to the OpenRouter node, select Connect Credential, and add the credential name and your API Key. Make sure you finish this before proceeding.
NEW IMAGE
![image]((notion-hosted file))
### Step 4: Add a Buffer Memory node
Go to (+) and under LangChain, in the search bar, look for Buffer Memory under the Memory category and drag it onto the canvas.
Connect the output of the Buffer Memory node to the Memory input socket on the Conversation Chain.
NEW IMAGE
![image]((notion-hosted file))
> ➡️ Why this matters: The Buffer Memory node captures the recent dialogue and injects it into the background context of every new prompt. Without this connection, the chain has no access to previous messages and will treat every user input as the start of a new conversation.

### Step 5: Configure a Session ID
In the Buffer Memory node, select Additional Parameters and locate the Session ID field. For now, enter a fixed test value such as client_001.
![image]((notion-hosted file))
> ➡️ Why this matters: The Session ID groups all conversation history under one identifier. In a deployed application this would be set dynamically per user, but for testing purposes a fixed value is sufficient. You will configure proper session isolation in the next lesson.

### Step 6: Save and test
Save your Chatflow and open the built-in chat window by clicking the chat icon in the top right corner of the interface. Run the following two-turn test to verify memory is working:
![image]((notion-hosted file))
> Turn 1: My name is Markus and my case reference is CG-7741.
> Turn 2: What is my case reference?

## What to look for:
- If the agent responds with CG-7741, the memory node is correctly capturing and injecting the session context.
- If the agent asks for the reference again, check that the Buffer Memory node output is securely connected to the Memory input socket on the Conversation Chain, and that the canvas has been saved before testing.

## Checklist: Confirm before moving on
- [ ] Buffer Memory node added to the canvas
- [ ] Memory node output connected to the Conversation Chain memory input
- [ ] Chat model node connected to the Language Model input
- [ ] Session ID configured on the Buffer Memory node
- [ ] Two-turn test completed and memory recall confirmed

> 💡 Takeaway: 
  A memory node is the simplest and most foundational addition to a Flowise agent. Without it, every conversation starts from zero. With it, the agent can hold context across turns which is the prerequisite for every more complex memory behaviour covered further on in this sprint.
