# Connecting Tools to Your Chatflow

Notion page: https://app.notion.com/p/Connecting-Tools-to-Your-Chatflow-3689418319f380a5ad44c8e226b890d7
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Replace the Conversational Retrieval QA Chain with a Tool Agent node, connect a Retriever Tool for knowledge base queries and a Custom Tool simulating a loan status lookup, implement the system prompt instructions and safeguards you designed in the previous lessons and validate that memory, retrieval, and tools all work together as one connected system.

## Why this step comes now
Contigo GmbH's support agent can hold multi-turn conversations, retrieve accurately from the knowledge base, and enforce grounding behaviour. It cannot act. When a client asks for the status of their loan application, the agent retrieves a policy section about application timelines and generates a professionally worded explanation of the process. It cannot query the live system.
This walkthrough changes that. By the end, the agent will use tools to answer queries that require live data, while continuing to retrieve from the knowledge base for policy and product questions, all within the same Chatflow, the same memory configuration, and the same session isolation you built in Sprints 1 and 2.
The canvas changes in this lesson are the most significant since the initial Chatflow build. You are not adding to the existing chain. You are replacing it with a more capable node. The Conversational Retrieval QA Chain handled one job: retrieve and generate. The Tool Agent handles multiple jobs: reason about which tool to use, invoke it, observe the result, and generate a grounded response.

## What you are building
A Flowise Tool Agent Chatflow containing:
- OpenRouter node: The language model, carried over from Sprint 1
- Buffer Window Memory node: Session memory, carried over from Sprint 1
- Qdrant node: The vector store, carried over from Sprint 2
- Google Gemini Embedding node: Query-time embeddings, carried over from Sprint 2
- Retriever Tool node: Wraps the Qdrant retriever so the Tool Agent can invoke it as a tool
- Custom Tool node: Simulates a loan status lookup returning mock data
- Calculator node: A built-in tool requiring no API key, used to verify tool invocation
- Tool Agent node: The new orchestration node that replaces the Conversational Retrieval QA Chain

## Follow these steps
### Step 1: Open your existing Chatflow
Open your local Flowise instance at http://localhost:3000. Open the Chatflow you have been building. Before making any changes, export the current Chatflow as a JSON backup. Click the Settings icon in the top right corner and select Export Chatflow. Save the file as contigo_sprint2_backup.json. If anything goes wrong during this walkthrough you can reimport this file and start from the current working state.

### Step 2: Remove the Conversational Retrieval QA Chain node
Click on the Conversational Retrieval QA Chain node and delete it from the canvas.

### Step 3: Add the Tool Agent node
Click (+) to open the node panel. Under the LangChain tab, search for Tool Agent and drag it onto the canvas.
The Tool Agent node has the following inputs:
- Tool Calling Chat Model (mandatory) — connect your output
- Memory (mandatory) — connect your BufferWindowMemory output
- Tools (mandatory) — you will connect tools here in subsequent steps
- Input Moderation (optional) — leave blank for now
- Chat Prompt Template (optional) — leave blank for now

### Step 4: Add the Retriever Tool node
The Qdrant node on your canvas outputs a vector store retriever. To make this retriever available to the Tool Agent as an invokable tool, you need to wrap it in a Retriever Tool node. Click (+), under the LangChain tab search for Retriever Tool and drag it onto the canvas.
Configure the Retriever Tool node as follows:
- Name: contigo_knowledge_base
- Description: Enter the retrieval scope instruction you wrote (see the checklist in the previous lesson), the revised instruction specifying that this tool retrieves content from Contigo's static policy and product documentation stored in Qdrant, and should be invoked when the query asks for information in documented policies, product guides, or compliance materials.
- Vector Store Retriever: Connect the Qdrant Retriever output from the Qdrant node to this input
Connect the Retriever Tool node output to the Tools input on the Tool Agent node.
> ➡️ Why this matters: The Tool Agent cannot directly read from a vector store. It can only invoke tools. The Retriever Tool node is the bridge. It wraps the Qdrant retriever as a named, described tool that the Tool Agent can select and invoke through the ReAct loop when a query requires knowledge base retrieval.

### Step 5: Add the Calculator node
The Calculator is a built-in Flowise tool that requires no API key or external account. It gives the Tool Agent the ability to perform precise mathematical calculations. Click (+), under the LangChain tab search for Calculator and drag it onto the canvas. No configuration is required.
Connect the Calculator node output to the Tools input on the Tool Agent node.
> ➡️ Why the Calculator is included: It provides an immediate, zero-configuration way to verify that the Tool Agent is correctly invoking tools through the ReAct loop. If you send a calculation query and the agent invokes the Calculator rather than generating a number from its training data, the tool routing is working correctly. It also gives Contigo's agent a genuinely useful capability by calculating loan repayment figures or interest amounts on demand.
> ⚠️ Save your chatflow before going to Step 6.

### Step 6: Create and add the Custom Tool as a loan status lookup
The loan status tool simulates a live application tracking query. It does not connect to a real banking API. It returns mock data based on the application reference provided. This is sufficient to test tool invocation, parameter passing, and the ReAct loop in a course environment.
Exit your chatflow and in your Flowise dashboard, search for Tools in the left-hand navigation panel. Click Create in the top right corner.
Configure the Custom Tool as follows:
Name: loan_status_lookup
Description: Enter the loan status tool description you wrote in the previous lesson — the revised instruction specifying that this tool queries the live loan application tracking system and should be invoked only when the client provides a specific application reference or asks for the current processing status of an active application.
Input Schema: Add one input parameter:
- Parameter name: application_reference
- Type: String
- Description: The client's loan application reference number, for example APP-7741. This must be explicitly provided in the client's query before the tool is invoked.
- Required: Yes
![image]((notion-hosted file))
JavaScript Function: Enter the following code:
```javascript
const ref = $application_reference;

const mockData = {
  "APP-7741": { status: "Under review", stage: "Credit assessment", estimatedCompletion: "5 business days" },
  "APP-8841": { status: "Approved", stage: "Documentation pending", estimatedCompletion: "2 business days" },
  "APP-9921": { status: "On hold", stage: "Additional information required", estimatedCompletion: "Pending client response" }
};

if (mockData[ref]) {
  const d = mockData[ref];
  return `Application ${ref}: Status — ${d.status}. Current stage — ${d.stage}. Estimated completion — ${d.estimatedCompletion}.`;
} else {
  return `Application reference ${ref} was not found in the tracking system. Please verify the reference number and try again.`;
}
```
Select ‘Add’ and it is now available. Return to your Chatflow canvas. Click (+) to open the node panel. Under the LangChain tab, search for Custom Tool and drag it onto the canvas. In the Custom Tool node settings, locate the Selected Tool dropdown. Click it and select loan_status_lookup from the list. If you do not see it, confirm that you saved the tool correctly and refresh the page.
Connect the Custom Tool node output to the Tools input on the Tool Agent node.

### Step 7: Configure the Tool Agent system prompt
Open the Additional Parameters of the Tool Agent node and locate the System Message field. Enter the following (based on the information you collected from the previous lessons):
> You are a support agent for Contigo GmbH, a financial services firm operating across Germany, Austria, and the Netherlands. Answer client questions using only the information retrieved from the Contigo knowledge base. Do not use outside knowledge or make assumptions beyond what the retrieved context states. You can explain account procedures and policies but you cannot make changes to any client account. If a client requests an account change, inform them clearly that you are unable to perform account modifications and direct them to contact their Contigo relationship manager or visit the client portal. If the answer is not contained in the retrieved context and no tool returns a relevant result, respond with: "I do not have that information in my current knowledge base. Please contact a Contigo advisor directly for further assistance." If a tool returns an error or fails to return a result after repeated attempts, respond with: "I was unable to retrieve that information at this time. Please contact your Contigo relationship manager directly for assistance with reference [state any reference number provided by the client]." Do not expose error codes, API references, or technical details in any client-facing response.

### Step 8: Set the Max Iterations parameter
Stay in the Additional Parameters and locate the Max Iterations field. Enter the value you decided in the previous lesson. If you have not yet decided, use 6 as the default.

### Step 9: Save and run the validation tests
Save the Chatflow and open the built-in chat interface. Run the following eight tests in order. Record each response before moving to the next test.
See below how it should look like.
NEW IMAGE
![image]((notion-hosted file))
Test 1: Memory continuity
Send: "Hi, my name is Markus Bauer and my open case reference is CG-4821." Then send: "What is my case reference and what did I tell you my name was?"
Expected: Agent recalls CG-4821 and Markus Bauer without asking the client to repeat either piece of information. This confirms Buffer Window Memory is correctly connected to the Tool Agent.
✅ Pass: Agent recalls both correctly.
❌ Fail: Check that the Buffer Window Memory node is connected to the Memory input on the Tool Agent and that the Session ID is configured.

Test 2: Knowledge base retrieval via Retriever Tool
Send: "What documents does a client need to submit with an SME loan application?"
Expected: Tool Agent invokes the contigo_knowledge_base Retriever Tool and returns a specific answer drawn from the knowledge base. Review the agent's intermediate steps in the chat panel to confirm the Retriever Tool was invoked.
✅ Pass: Agent invokes the Retriever Tool and returns a specific knowledge base answer.
❌ Fail: Check that the Retriever Tool node is correctly connected to the Tools input and that the Qdrant Retriever output is connected to the Retriever Tool's Vector Store Retriever input.

Test 3: Calculator tool invocation
Send: "If a client's monthly loan repayment is €847 and the loan term is 36 months, what is the total amount repaid?"
Expected: Tool Agent invokes the Calculator tool and returns €30,492. This confirms the tool routing is working and the agent is not generating mathematical results from its training data.
✅ Pass: Agent invokes the Calculator and returns the correct result.
❌ Fail: Check that the Calculator node is connected to the Tools input on the Tool Agent.

Test 4: Loan status tool invocation with valid reference
Send: "Can you check the status of my application, reference APP-8841?"
Expected: Tool Agent invokes the loan_status_lookup tool with APP-8841 as the parameter and returns the mock status — Approved, Documentation pending, estimated 2 business days.
✅ Pass: Agent invokes the tool and returns the correct mock status.
❌ Fail: Check that the Custom Tool node is connected to the Tools input and that the tool description specifies the invocation condition clearly enough to distinguish it from the knowledge base tool.

Test 5: Loan status tool with invalid reference
Send: "What is the status of application APP-0000?"
Expected: Tool Agent invokes the loan_status_lookup tool, receives the not-found response from the JavaScript function, and informs the client that the reference was not found and asks them to verify it.
✅ Pass: Agent invokes the tool, receives the not-found response, and communicates it professionally.
❌ Fail: If the agent fabricates a status rather than invoking the tool, the tool description invocation condition needs to be more specific.

Test 6: Account action boundary
Send: "Please update my registered email address to k.brandt@example.de"
Expected: Agent does not imply it has made the change. It explains the procedure for updating contact details using the knowledge base and directs the client to the appropriate channel. It does not invoke the loan status tool or the Calculator.
✅ Pass: Agent explains the procedure and directs the client to the relationship manager or client portal.
❌ Fail: Revise the account action boundary instruction in the System Message to make the distinction between information and action more explicit.

Test 7: Out-of-domain query
Send: "What is the current base rate set by the European Central Bank?"
Expected: No tool is invoked. The agent delivers the configured fallback phrase — it does not cite an ECB rate figure from its training data.
✅ Pass: Agent delivers the fallback phrase.
❌ Fail: Strengthen the retrieval scope instruction in the System Message to explicitly prohibit the use of general training knowledge.

Test 8: Memory and tools working together
Send: "Based on what I told you earlier, can you check the status of case CG-4821 and tell me what documents Markus would need to submit?"
Expected: Agent recalls Markus Bauer and CG-4821 from the Buffer Window Memory node, invokes the loan_status_lookup tool for the case status, and invokes the contigo_knowledge_base Retriever Tool for document requirements combining all three in one response.
✅ Pass: Agent combines memory context, tool output, and knowledge base retrieval in a single response.
❌ Fail: Diagnose which component is failing by running Tests 1, 2, and 4 independently and checking the results.

## Checklist: Confirm before moving on
- [ ] Conversational Retrieval QA Chain removed from canvas
- [ ] Tool Agent node added and connected to ChatGoogleGenerativeAI and Buffer Window Memory
- [ ] Retriever Tool node added, configured with knowledge base description, and connected to Qdrant Retriever output and Tool Agent Tools input
- [ ] Calculator node added and connected to Tool Agent Tools input
- [ ] Custom Tool loan_status_lookup created with correct JavaScript function and description
- [ ] Custom Tool node added to canvas and connected to Tool Agent Tools input
- [ ] System Message configured with all revised instructions from A12.1 and fallback behaviour from A12.2
- [ ] Max Iterations parameter set in Additional Parameters
- [ ] All eight validation tests completed and results recorded
- [ ] All eight tests passed before proceeding

> 💡 Takeaway: 
  The Tool Agent node is the architectural upgrade that transforms your Chatflow from a retrieval system into an action-capable agent. The ReAct loop runs automatically for every query. The quality of your tool descriptions and system prompt instructions is what makes that loop reliable. 
  The memory configuration from Sprint 1 and the knowledge base from Sprint 2 are both fully active. The Tool Agent orchestrates them alongside the new tools you have just connected.