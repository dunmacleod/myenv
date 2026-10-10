# Agent Memory Node and Thread IDs in Flowise

Notion page: https://app.notion.com/p/Agent-Memory-Node-and-Thread-IDs-in-Flowise-3669418319f380938f8adaa621eaff6f
Backed up before n8n migration

> 💡 What you will do in this lesson: Configure the Session ID on your Buffer Memory node to isolate conversation history between users, and verify that session data is being stored and separated correctly.

## Why this step comes now
The Buffer Memory node you configured in the previous lesson gives Contigo's agent short-term conversational context within a single session. But it has a limitation: by default, if a Session ID is not specified, Flowise generates a random ID for each interaction. This is fine for single-user testing, but in a client-facing deployment where multiple users interact with the same Chatflow simultaneously, their conversation histories could bleed into each other.
In a client-facing financial services context like Contigo's, that is a serious problem. This walkthrough shows you how to configure the Session ID parameter on the Buffer Memory node. This is Flowise's mechanism for keeping each client's conversation history completely isolated from every other user's.

## What you are building
You are extending the Chatflow you built in the previous lesson. The Buffer Memory node is already connected and working. You have confirmed that the agent can recall information within a single session. The next step is to make that memory safe for a multi-user environment by configuring a Session ID on the Buffer Memory node.

### Step 1: Open your existing Chatflow
From your Flowise dashboard, navigate to Chatflows and open the Chatflow you built in the previous lesson. You should see your existing canvas and nodes already connected.
You do not need to add any new nodes for this lesson. The changes happen inside the Buffer Memory node configuration.
CHANGED IMAGE
![image]((notion-hosted file))
### Step 2: Open the Buffer Memory node settings.
Select ‘Additional Parameters.’ You will see two parameters:
- Session ID
- Memory Key
The Session ID field is empty by default (but we did add client_001) which means Flowise generates a random ID for each interaction. This is fine for single-user testing but is not suitable for production, where multiple users may be active at the same time.

### Step 3: Configure the Session ID
In the Session ID field, enter a value that represents a unique identifier for the current user or session. For testing purposes, we will keep the fixed value: client_001.
![image]((notion-hosted file))
> ➡️ Why this matters: The Session ID groups all conversation history under one identifier. When a Session ID is set, Flowise stores and retrieves memory only for that specific ID. Each client gets their own isolated memory space: One client's account details, case references, and preferences cannot appear in another client's conversation.

### Step 4: Save and test session isolation
Save your Chatflow and open the built-in chat interface. Run the following isolation test using two separate browser sessions, each with a different Session ID configured in the Buffer Memory node.
Session 1 Session ID: client_001
Send: "My preferred contact language is English and my open case is CG-9921."
Then send: "What is my open case reference?"
The agent should respond with CG-9921, confirming memory is working correctly for this session.
![image]((notion-hosted file))

Session 2 Session ID: client_002
Open a second browser session, update the Session ID in the Buffer Memory node to client_002, save, and send:
"What language does this client prefer, and do they have any open cases?"
What to look for:
- Session 2 should have no knowledge of the information provided in Session 1. If it does, the Session IDs are not being applied correctly and the sessions are sharing the same memory space.
- Session 1 should recall its own data correctly across turns, confirming that messages are being stored and retrieved under the correct Session ID.

### Step 5: Verify message storage
In your Flowise dashboard, navigate to the chat history for your Chatflow. You can access this from the settings icon within the Chatflow canvas, under View Messages. You should see two separate conversation threads, each stored under its own Session ID. Each thread contains only the messages from that session, with no overlap between them. 
This is your confirmation that session isolation is working correctly. In a regulated environment like Contigo's, being able to demonstrate that client conversation data is correctly isolated is a compliance requirement, not just a technical detail.
![image]((notion-hosted file))

## Checklist: Confirm before moving on
- [ ] Buffer Memory node opened and Session ID field located
- [ ] Session ID configured with a unique value for testing (e.g. client_001)
- [ ] Chatflow saved after Session ID is set
- [ ] Memory test completed: agent recalled case reference across turns in Session 1
- [ ] Isolation test completed: Session 2 had no access to Session 1 data
- [ ] Chat history verified in Flowise dashboard showing separate threads per Session ID

> 💡 Takeaway: 
  The Session ID is what makes Buffer Memory safe for a multi-user environment. Without it, conversation histories have no guaranteed isolation between users. Configuring it correctly before adding more complexity is what makes the rest of your Chatflow build reliable.
