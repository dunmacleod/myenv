# Building the baseline agent: retries and fallbacks

Notion page: https://app.notion.com/p/Building-the-baseline-agent-retries-and-fallbacks-3889418319f380f2ac25f540b6579a22
Backed up before n8n migration

> 🎯 What you build here is the baseline for the Sprint 4 project. By the end of this walkthrough, your Flowise workspace contains the arXiv agent that Sprint 4 extends, evaluates, and debugs. Save the workflow.

Halcyon Labs now wants to extend the IT support system you designed in Sprint 1 with a research-retrieval capability: an agent that queries arXiv and returns papers to internal researchers. This lesson is where you build that capability. From this point onwards, you shift from watching Sofia build Cascadia's support automation as a teaching example to building your own project deliverable — the arXiv agent Halcyon Labs needs. The arXiv MCP server is real and public, its API sometimes rate-limits or times out, and the retrieve-then-summarise pattern is small enough to build in a walkthrough and real enough to fail interestingly — exactly the conditions the resilience patterns in this sprint were designed for.
External tools do not always respond successfully. An MCP server may be rate-limited, unavailable, or slow. In an agent workflow, we do not want every temporary failure to immediately become a failed user experience. A retry pattern gives the system a second chance, while still keeping control over how many times it tries.

## What we are building
In this walkthrough, we will build an arXiv research agent that tries to search academic papers through an arXiv MCP tool.
The workflow will:
1. Receive a user request.
1. Ask the arXiv agent to search for papers.
1. Parse the agent output for temporary failure signals.
1. If the search worked, return the result to the user.
1. If the search hit a temporary failure, retry the same step.
1. Stop retrying after the maximum loop count is reached.
1. Add a fallback response.

# Workflow structure
```plain text
Start
  ↓
Arxiv MCP Engine
  ↓
Parse Status & Errors
  ↓
Evaluate Network State
  ├── To_User_Chat → Direct Reply
  └── Trigger_Loop → Retry Counter Loop
                          │
                          ├── Retry Available → Arxiv MCP Engine
                          │
                          └── Max Retries Reached → Fallback Reply
```
> ☝ The important idea is that the workflow does not retry every failure blindly. It retries only when the parsed output suggests a temporary problem, such as a rate limit or service unavailability.

## Step 1: Create the arXiv agent
In the Agentflows tab create a new worksheet and call it Arxiv Agent.
Create an agent node called Arxiv MCP Engine .
Use the Gemini Flash Lite model and connect the arXiv MCP tool.
The agent’s job is simple: search arXiv and return useful paper information to the user.
Add a system prompt:
```plain text
You are an expert Research Assistant Agent specializing in fetching, analyzing, and synthesizing scientific papers from arXiv using the provided Model Context Protocol (MCP) tools.

Your primary objective is to answer user queries with accurate, up-to-date academic context.

OPERATIONAL INSTRUCTIONS:


Always translate the user's research query into precise, well-formatted keywords before calling the search_papers or get_details tools.

If a query returns multiple papers, select the most relevant ones and synthesize their findings. Do not just list them blindly.

CRITICAL: TRANSIENT ERROR & RATE LIMIT HANDLING:

The arXiv API enforces strict rate limits. If you receive an error message from a tool execution containing "429", "Rate Limit", "Too Many Requests", or "503 Service Unavailable", you must immediately stop trying alternative tools and output the exact phrase: "Error: 429 Rate limit exceeded by arXiv." 

Do not attempt to guess or hallucinate data if a tool fails. Outputting this exact error string allows the orchestration system to safely trigger a workflow retry loop on your behalf.

FINAL ANSWER FORMATTING rules:

When presenting the final answer to the user, DO NOT output raw JSON, tool parameters, or programming code.
Write your response in clear, concise, professional academic markdown.
Structure your answer with clear headings, bullet points for key findings, and include the paper titles alongside their authors and publication years.


```
![image]((notion-hosted file))

# Step 2: Add a parser function
Add a custom function node after the arXiv agent.
Name it Parse Status & Errors
// Grab the textual response from the agent trying to query arXiv
const assistantResponse = $input.text || "";
// Detect if arXiv rate-limited the agent or dropped the connection
if (assistantResponse.includes("429") ||
assistantResponse.includes("Rate limit") ||
assistantResponse.includes("503 Service Unavailable")) {
```plain text
return "Trigger_Loop"; // Matches the path leading to the Loop Node
```
} else {
return "To_User_Chat"; // Matches the path completing the workflow
}
![image]((notion-hosted file))
Use this function:
```javascript
// Grab the textual response from the agent trying to query arXiv
const assistantResponse = $input.text || "";

// Detect if arXiv rate-limited the agent or dropped the connection
if (assistantResponse.includes("429") || 
    assistantResponse.includes("Rate limit") || 
    assistantResponse.includes("503 Service Unavailable")) {
    
    return "Trigger_Loop"; // Matches the path leading to the Loop Node
} else {
    return "To_User_Chat"; // Matches the path completing the workflow
}
```
This function converts a messy agent response into a clean routing decision. In this example, we are checking for temporary service failures that often recover on their own. Specifically, we look for 429 (Too Many Requests), which indicates a rate limit has been reached, "Rate limit" messages returned by the tool or model, and 503 Service Unavailable, which indicates the service is temporarily unable to process requests. These errors are good candidates for retries because a second or third attempt may succeed once the temporary condition has passed.
The function does not solve the problem itself. It only answers:
> Should we retry, or should we return the result to the user? 
So it provides two outputs: Trigger_Loop in case something was broken or To_User_Chat if the execution of the Agent was healthy.

# Step 3: Add the condition node
Add a condition node called Evaluate Network State .
![image]((notion-hosted file))
This node checks the output of the parser. 
Create two branches: 
- To_User_Chat
- Trigger_Loop
If the parser returns To_User_Chat, the workflow goes to the direct reply node.
If the parser returns Trigger_Loop, the workflow goes to the retry loop.
Open the node and place:
![image]((notion-hosted file))
We add a branch for Trigger_Loop  which will result in Agent retries. Alternative healthy branch is going to be added automatically, so you do not have to add second condition.

# Step 4: Add the retry loop
Add a loop node called Retry Counter Loop . Connect the first branch of conditional node to it.
![image]((notion-hosted file))
Set the maximum loop count to 3. This is important. A retry pattern must always have a limit. Without a maximum count, the workflow could keep calling the same failing tool again and again.  Connect the loop back to Arxiv MCP Engine.
![image]((notion-hosted file))
Now the workflow can try the arXiv search again when the error looks temporary.

# Step 5: Add the direct reply
Add a direct reply node for the successful path.
This node returns the agent’s final output to the user.
You can keep the default name.
![image]((notion-hosted file))
This path is used when the parser does not detect a retryable error. The message of the direct reply node should contain the output from the agent:
![image]((notion-hosted file))

# Checkpoint
Test the workflow with a normal query:
> Find recent papers on transformers
![image]((notion-hosted file))

### Step 6: Add a fallback response
So far, the workflow retries the arXiv search up to three times. But what should happen if all three attempts fail?
A resilient workflow should not simply stop or return an error trace to the user. Instead, it should provide a controlled response that explains what happened and suggests a next step.
> ☝ In Flowise, the Loop node routes the workflow back to the selected retry step. It does not need a separate “max retries reached” branch. Instead, we add a fallback message directly in the loop settings, so when the maximum loop count is reached, the workflow returns a controlled user-facing response instead of continuing to retry.
Add a fallback message to your node:
> 
  I’m currently unable to retrieve results from arXiv because the service may be temporarily unavailable or rate-limited.
  Please try again in a few minutes, or simplify your search query and run it again.
![image]((notion-hosted file))

# Watch out for
The most common mistake is retrying every error. Not every error should be retried. A missing input, invalid query, or broken prompt will probably fail again. Retries are best for temporary problems: rate limits, service unavailable errors, dropped connections, or short network issues.
Another common mistake is forgetting the retry limit. Always set a maximum loop count.

# Summary
You built a controlled retry pattern for an arXiv MCP agent. The workflow now checks whether a tool failure looks temporary, sends retryable failures back through a loop, and stops after a limited number of attempts.
That is the core of a resilient orchestration pattern: the workflow does not panic after one failed call, but it also does not keep trying forever.