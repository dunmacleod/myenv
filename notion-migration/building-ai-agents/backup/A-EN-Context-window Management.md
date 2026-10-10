# Context-window Management

Notion page: https://app.notion.com/p/Context-window-Management-3669418319f380c2b5a1c98b08a2d64e
Backed up before n8n migration

> 💡 What you will work on in this lesson: Evaluate two context management strategies for a business agent, design an approach based on your reasoning, and then implement it in your Chatflow by configuring a Buffer Window Memory node.

## What is Happening
Contigo GmbH's support agent is now retaining conversation history and isolating sessions correctly. But a new problem has emerged in testing.
During long troubleshooting conversations, the agent's performance degrades noticeably after fifteen or twenty exchanges. In some cases it begins contradicting instructions it was given earlier in the conversation. In others it fails entirely at a late turn, forcing the client to start over.
The cause is the context window. Every message added to the conversation history makes the prompt longer. At some point the prompt becomes too long for the model to process reliably and long before it hits the hard token limit, attention quality begins to degrade. The agent starts losing track of earlier content, prioritising recent messages at the expense of important context established at the start of the session.
Contigo's team needs a strategy to manage this before the agent goes into production. Your task is to reason through the options, make a design decision, and implement it in your Chatflow.

## The two main approaches
You have been given access to two context management strategies available in Flowise. Before deciding which to apply, you need to understand what each one does and what it costs.
1. Buffer Window Memory - Sliding window truncation: 
This node keeps only the most recent K messages in the active context and drops everything older. 
It is simple to configure, adds no additional overhead, and guarantees the prompt never exceeds a defined size. The trade-off is blunt: older content is dropped entirely, regardless of whether it was important. This is the node you will configure in this lesson.

1. Conversation Summary Memory - Compression via a Secondary Model Call: 
This node uses the language model to continuously summarise older portions of the conversation as new messages arrive. 
The summary replaces the raw dialogue, preserving general meaning without keeping the full verbose exchange. 
The trade-off is cost and latency: every summarisation step requires an additional model call, and the summary is an approximation — specific details can be lost in compression. This option is covered as a best practice consideration in the next lesson.
![image]((notion-hosted file))
## Your tasks 
### Part A: Evaluate the strategies
Read the following two scenarios and answer the questions for each. Write them down so you can analyse your answers later.

Scenario 1: Loan application review
- A Contigo loan officer is using the agent to work through a complex application. In the first three messages, the client provides their income figures, employment history, and the loan amount requested. The conversation then runs for twenty more exchanges covering eligibility criteria and document requirements.
- If a strict sliding window of the last six messages is applied, what critical information is at risk of being lost? What is the consequence for the agent's ability to complete the task?

Scenario 2: General account query
- A client contacts Contigo to update their contact details and ask a question about their current interest rate. The conversation is short and none of the early messages contain information that is needed later.
- For this type of conversation, is a sliding window sufficient? What window size would be reasonable, and why?
[toggle] Checkpoints: Use these to help guide you to the answer
  Checkpoint 1: The cost of truncation - Think about what the model can and cannot see after truncation happens. It has no way to flag that earlier context is missing. It simply reasons from what it has. Consider what happens in the loan application scenario if the income figures from Turn 1 are no longer in the active window by Turn 20.
  Checkpoint 2: Matching the window to the use case - A window that is too small drops important context too early. A window that is too large defeats the purpose of managing context at all. Think about the typical length of a Contigo support conversation and what a reasonable minimum number of recent messages would be to maintain coherent continuity.
  Checkpoint 3: What should never be dropped - Some information established early in a session is critical for the entire conversation. Case references, account identifiers, and stated preferences are examples. Consider whether a window-only approach can protect this information, or whether it needs to be handled differently.

### Part B: Implement Buffer Window Memory in your Chatflow
Based on your reasoning in Part A, you will now replace the Buffer Memory node in your Chatflow with a Buffer Window Memory node and configure it with a window size that reflects your design decision.

### Step 1: Open your existing Chatflow
From your Flowise Cloud dashboard, open the Chatflow you have been building. You should see the Conversation Chain, OpenRouter, and Buffer Memory nodes on the canvas.

### Step 2: Remove the Buffer Memory node
Click on the Buffer Memory node and delete it from the canvas. You will replace it with a Buffer Window Memory node in the next step.

### Step 3: Add a Buffer Window Memory node
Click (+) to open the node panel. Under the LangChain tab, search for Buffer Window Memory and drag it onto the canvas.

### Step 4: Connect the node
Connect the output of the Buffer Window Memory node to the Memory input socket on the Conversation Chain, exactly as you did with the Buffer Memory node previously.

### Step 5: Configure the node
Open the Buffer Window Memory node settings and configure the following:
- Size: Enter the window size you decided on in Part A. The default is 4 (last 4 messages). Adjust this based on your reasoning about Contigo's typical conversation length.
- Session ID: Enter the same Session ID you configured previously (client_001) to maintain consistency with your earlier test setup.
- Memory Key: Leave this as the default (chat_history).
![image]((notion-hosted file))
> ➡️ Why this matters: The Size parameter is the core of this node. It defines exactly how many recent message pairs the agent can see at any given turn. Everything older than that window is dropped from the active context. Setting this number deliberately rather than accepting the default is the difference between a memory configuration that works for your use case and one that fails under realistic conversation conditions.
![image]((notion-hosted file))
NEW IMAGE
### Step 6: Save and test
Save your Chatflow and open the built-in chat interface. Run the following test to verify the window is working as configured.
Send four or more messages that each introduce a new piece of information, for example:
- Turn 1: "My name is Markus and my case reference is CG-4821."
- Turn 2: "I am calling about a loan restructuring query."
- Turn 3: "My preferred contact language is English."
- Turn 4: "I have been a Contigo client for six years."
- Turn 5: "What is my case reference?"

### What to look for
If your window size is set to 4, Turn 1 should still be within the active window when Turn 5 is sent and the agent should recall CG-4821 correctly.
 If your window is set smaller, Turn 1 may already be outside the window and the agent will not be able to recall it. 
Observe the result and compare it against your design decision from Part A. Does your chosen window size produce the behaviour you intended?

## Check for Understanding
### Question 1
>  A client pastes a 3,000-word legal document into the Contigo agent chat for summarisation and policy cross-referencing. Which handling approach is most architecturally appropriate?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d452570f-8d0d-46d4-b71b-e65e1a0a35d4

### Question 2
>  In a Contigo financial services agent, which category of information should never be dropped from the active context window regardless of conversation length?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/014a6fcb-0cd1-4e49-9ea7-bf568e69fee7

> 💡 Takeaway: 
  Context management is a design decision you make. The window size you configure directly determines what the agent can and cannot remember at any point in a conversation. Getting this right for your specific use case, before the agent reaches production, is what separates a memory configuration that holds up under real conversation conditions from one that quietly fails when it matters most.