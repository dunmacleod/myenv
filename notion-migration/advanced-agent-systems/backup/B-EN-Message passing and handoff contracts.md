# Message passing and handoff contracts

Notion page: https://app.notion.com/p/Message-passing-and-handoff-contracts-37e9418319f3804ca33eee2b38fe4879
Backed up before n8n migration

After the schema mismatch that broke the warranty handoff, Sofia is starting over with a proper contract. Before she rebuilds the full Cascadia support system, she wants to build the smallest possible handoff that could work: two agents in Flowise Agentflow V2, with a shared Flow State that carries the intent and reasoning from the first agent to the second.
In this walkthrough you build exactly that. An Intake Agent classifies a customer message and writes three keys to Flow State — the customer's intent, a one-line summary, and a reason for the handoff. A Specialist Agent reads those keys and answers based on them, without re-analysing the original message. This is the smallest concrete example of the communication contract the previous lesson described.
Every multi-agent handoff requires a shared memory layer so that Agent B knows what Agent A did. Agentflow V2 provides an implicit execution thread memory as well as a explicit global context called Flow State ($flow.state).  
• Start Node Initialization: At the absolute beginning of your canvas, the Start Node must explicitly declare and initialize the key-value pairs (the contract schema) that will be accessed or updated by agents down the line.  
• State Updates (Overwriting vs. Appending): When data passes through a node, you can configure how a variable is updated:
    ◦ Replace: Overwrites the variable (e.g., updating a ticket_status or current_summary).
    ◦ Append: Converts the variable into an array or appends to it (ideal for accumulating raw JSON logs or multi-step analysis across multiple agents).

A robust handoff contract guarantees that when Agent A hands execution over to Agent B, all critical information (e.g., intent, verified parameters, raw logs) is bundled cleanly into the graph flow.

## The workflow you will build
You will build the smallest version of Cascadia's support triage: an Intake Agent that classifies incoming messages, and a Specialist Agent that handles the billing branch.
The Intake Agent reads a customer's message and extracts the main issue. The Specialist Agent uses that extracted context to write a more focused response, without going back to the original message text.
The flow will look like this:
![image]((notion-hosted file))
This is a basic message-passing pattern. The first agent does not produce the final answer. Instead, it prepares the context for the next agent.
## Step 1: Create a new Agentflow V2 flow
Open Flowise and create a new Agentflow V2 workflow. 
![image]((notion-hosted file))
You can name it Customer Support Triage .
![image]((notion-hosted file))
The Start node represents the beginning of the conversation and is also where you define the shared state that later nodes can use.
In the Start Node, find the Flow State section and create these variables:
```json
{ "customer_intent": "", 
	"issue_summary": "", 
	"handoff_reason": "" }
```
![image]((notion-hosted file))
Click on Add Flow State to update variables:
![image]((notion-hosted file))
These variables are the handoff contract. They define what Agent A must prepare before Agent B can continue.
> ☝ Before moving on, confirm that the variables exist in the Start Node and are initialized as empty strings.
## Step 2: Add Agent A as the Intake Agent
Add an Agent Node after the Start Node. Since this agent does not need any tools, you can also opt for an LLM Node. Name it Intake Agent.
> ☝ For this task, it is best to use a Gemini or OpenAI LLM, since local models like Ollama may fail to produce structured output. There is a workaround, which is to add a custom function that returns the required structure, but to keep things simple, use Gemini models.
Connect the Start Node to the Intake Agent.
![image]((notion-hosted file))
Give the Intake Agent this role as a System  message by clicking on Add Message :
![image]((notion-hosted file))
> 💬 You are an Intake Agent for Cascadia Outfitters' customer support workflow. Your job is not to solve the customer's problem fully. Your job is to analyze the customer's request and prepare a clear handoff for the next agent. Identify:
  - the customer’s main intent with one word (billing, charged, payment, invoice, subscription, other)
  - a short summary of the issue
  - why this case should be handed off to a specialist
  - Return your answer in this structure
  {
  "customer_intent": "",
  "issue_summary": "",
  "handoff_reason": ""
  }
![image]((notion-hosted file))
Run a quick test with this user message:
> 💬 I was charged twice for my subscription this month. Can someone help me fix it?
Expected result: the Intake Agent should identify a subscription-related issue and summarize it clearly.
![image]((notion-hosted file))
## Step 3: Save the output in JSON format
To update the Flow State and map variables correctly, first create a structured output from the agent. Click on JSON Structured Output and add variables:
![image]((notion-hosted file))
This is the agent’s output. It is not connected to Flow State yet, but you will map it in the next step. Each field should be a string, and you can add a brief description for each one.
## Step 4: Save the Intake Agent output into Flow State
Now configure the Intake Agent so its output updates the Flow State.
Map the agent’s result into the variables you created earlier:
```json
customer_intent → billing 
issue_summary → user says they were charged twice for the subscription 
handoff_reason → billing specialist needed
```
Reopen your agent configuration and update the Flow State:
![image]((notion-hosted file))
Map the output from the Agent to update the state:
![image]((notion-hosted file))
Here, output is the Agent’s output.
## Step 5: Add Agent B as the Specialist Agent
Add a second Agent Node after the Intake Agent. Name it Specialist Agent. As in the previous case, this can also be an LLM node.
Connect the Intake Agent to the Specialist Agent.
![image]((notion-hosted file))
The Specialist Agent should not start from zero. It should use the handoff contract created by Agent A.
Use this prompt as a system message:
> 💬 A previous intake agent has already analyzed the user request. Do not repeat the intake process and do not ask for information that is already available. Use this handoff context: Customer intent: {{$flow.state.customer_intent}} Issue summary: {{$flow.state.issue_summary}} Handoff reason: {{$flow.state.handoff_reason}} Now write a helpful, focused response to the customer.
Run the same test message again.
> 💬 I was charged twice for my subscription this month. Can someone help me fix it?
Expected result: the Specialist Agent should answer as if the case has already been triaged.

![image]((notion-hosted file))
## Step 6: Add a simple routing decision
Now make the handoff more realistic.
Add a Condition Node between the Intake Agent and the Specialist Agent. You can give it a relevant title.
![image]((notion-hosted file))
The Condition Node should check whether the issue is billing-related.  We check the flow state value in customer_intent .

![image]((notion-hosted file))
You can add the second branch that is connected to Direct Reply node.
You can add the following output there
> 💬 Thank you for reaching out. Based on the information provided, your request does not appear to be related to billing.
  To ensure your inquiry is handled by the most appropriate team, we have forwarded it to the relevant specialist. They will review your case and get back to you as soon as they become available.
  Thank you for your patience and understanding.
![image]((notion-hosted file))
And your final Agent Flow should look like this:
![image]((notion-hosted file))
Modify prompt in you Specialist Agent, since now it has to be responsible for the billing issues only:
> 💬 You are a Billing Specialist Agent.
  You ONLY handle billing-related issues such as:
  - double charges
  - payment failures
  - invoices
  - subscription billing
  - refunds
  - account charges
  A previous Intake Agent has already analyzed the request and prepared a handoff for you.
  Use the following handoff information:
  Customer Intent:
  {{ $flow.state.customer_intent }}
  Issue Summary:
  {{ $flow.state.issue_summary }}
  Handoff Reason:
  {{ $flow.state.handoff_reason }}
  Instructions:
  - Assume the intake analysis is correct.
  - Do not repeat the intake process.
  - Do not ask for information that is already available in the handoff.
  - Focus only on resolving the billing issue.
  - If additional information is needed, ask concise follow-up questions.
  - Provide a clear explanation and next steps.
  - If the issue is not billing-related, politely state that it falls outside your scope.
  Response structure:
  Issue Assessment:
  [brief explanation of the billing issue]
  Recommended Action:
  [specific next step]
  Additional Information Needed:
  [question(s) if required, otherwise "None"]
## Step 7: Test the handoff contract
Use this test prompt:
```plain text
My invoice says I paid for the Pro plan, but my account still shows the Basic plan.
```
Check three things:
First, the Intake Agent should identify the intent correctly.
Second, Flow State should contain the extracted handoff context.
Third, the Specialist Agent should use that context instead of re-analyzing everything from scratch.
## Summary
You built a basic two-agent handoff in Flowise Agentflow V2. The first agent analyzed the user request, saved useful context into Flow State, and passed control to the next agent through the graph. The second agent used that context to produce a more focused response.
This is the foundation of predictable multi-agent coordination: agents do not simply continue a conversation blindly. They pass structured context through an explicit handoff contract.
