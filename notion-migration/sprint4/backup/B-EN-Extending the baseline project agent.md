# Extending the baseline project agent

Notion page: https://app.notion.com/p/Extending-the-baseline-project-agent-38c9418319f380c8a39ec348cea977a2
Backed up before n8n migration

The baseline project agent already uses an MCP-connected arXiv tool to search for research papers. In this practice, you will extend that flow so the system does not only retrieve papers, but also helps the user understand what to read first and why.
The new flow should look like this:

![image]((notion-hosted file))

Notice that the Summary Agent is only executed when the search has completed successfully.

## Your task
Modify the existing workflow by extending the To_User_Chat branch with a new Research Summary Agent.
The new agent should receive the successful search results and transform them into a structured response.

## Step 1: Locate the healthy execution path
Open your existing workflow.
Find the Evaluate Network State node.
Locate the branch labeled:
```plain text
To_User_Chat
```
At the moment, this branch ends by returning the search results to the user.
This is the part of the workflow you will extend.

## Step 2: Delegate the summarization task to a Research Summary Agent
After the workflow confirms that the arXiv search completed successfully, the Search Agent should delegate the retrieved papers to a specialized Research Summary Agent. Rather than searching again, this agent focuses entirely on organizing and summarizing the results before returning them to the Search Agent.
Connect a new Agent node after the To_User_Chat branch.
Name it:
```plain text
Research Summary Agent
```
This agent should not perform another search.
Its only responsibility is to organize the papers that were already retrieved by the arXiv Search Agent.

## Step 3: Configure the agent handoff
> ☝ Configure the workflow so the Search Agent passes the retrieved papers to the Research Summary Agent after the healthy branch of the workflow. The Summary Agent should receive the conversation history and paper results, complete its task, and return the structured response to the Search Agent.
Add a system prompt:
You are the Research Summary Agent.
The Search Agent has already completed a successful arXiv search and is delegating the summarization task to you.
Your responsibilities are to:
- analyze only the papers you receive
- recommend a logical reading order
- produce a concise research summary
Do not perform another search.
Do not answer the user directly.
Return your work to the Search Agent as valid JSON.
```json
{ "topic": "string", 
 "order_of_reading_papers": [ "paper title", "paper title", "paper title" ], 
 "summary": "One paragraph summarizing the research area 
						 and explaining why the papers are ordered this way." }
```
Rules: 
  - Do not perform another search.
    - Do not invent papers. 
  - Recommend a logical reading order, beginning with the most introductory paper. - Return only valid JSON.
> ☝ You can also add a JSON output directly to your agent. This will help ensure the flow is consistent.

## Step 4: Test the agent collaboration
Run the workflow with a query such as:
```plain text
Find papers about resilient multi-agent orchestration.
```
Verify that the workflow behaves correctly.
If the search fails, the retry loop should continue to operate exactly as before.
If the search succeeds, the workflow should continue to the Research Summary Agent, which should return output similar to:
```json
{ "topic": "Resilient Multi-Agent Orchestration", 
	"order_of_reading_papers": [ "...", "...", "..." ], 
	"summary": "..." }
```

## Check your work
Before finishing, confirm the following:
- The retry loop still works exactly as before.
- Failed searches never reach the Summary Agent.
- The Summary Agent only processes successful search results.
- The final response is valid JSON.
- The reading order is logical rather than random.

## Summary
You extended the healthy execution path of your orchestration without changing its resilience logic. The arXiv Search Agent remains responsible for retrieving papers, while the Research Summary Agent transforms successful search results into a structured research brief. This separation of responsibilities is a common orchestration pattern, where each agent performs one focused task while the workflow controls when each agent is allowed to execute.