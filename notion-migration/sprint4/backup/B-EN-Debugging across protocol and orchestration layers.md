# Debugging across protocol and orchestration layers

Notion page: https://app.notion.com/p/Debugging-across-protocol-and-orchestration-layers-38b9418319f380679131f98bca800d3a
Backed up before n8n migration

Download the starter project here:
Download project: [LINK]
This project should look very familiar. It is based on the workflow you built previously:
- an arXiv MCP Agent retrieves research papers,
- a parser checks the response,
- the workflow decides whether to retry or continue,
- successful responses are returned to the user.
However, this version contains one intentionally introduced bug.
The MCP integration itself is healthy. The retry logic also exists. Somewhere in the orchestration, a small mistake causes every successful request to be treated as a failure.
Your task is not to rebuild the workflow. Your task is to think like an engineer investigating a production issue.

# The debugging scenario
A user asks:
> Find recent papers about Retrieval-Augmented Generation.
Instead of returning the papers immediately, the workflow retries three times before stopping with the message:
> Loop completed after reaching maximum iteration count of 3.
The question is:
Why did the workflow retry when nothing appears to be wrong with the agent?

# Step 1: Reproduce the problem
Import the provided project into Flowise.
Run the workflow using any research-related prompt.
Observe the execution.
You should notice that:
- the arXiv MCP Agent completes successfully,
- the parser executes,
- the workflow enters the retry loop,
- after three iterations, execution stops.
At this point, do not start changing nodes. First, collect evidence.

# Step 2: Identify which layer is failing
Before looking at individual nodes, decide which part of the system is most likely responsible.
Ask yourself:
- Did the Arxiv MCP Agent fail?
- Did the MCP server return an error?
- Did the parser execute?
- Which node decided to enter the retry loop?
This simple reasoning helps narrow the investigation.
If the agent successfully returns research papers, the protocol layer is probably working correctly.
That means the problem is likely inside the orchestration.

# Step 3: Inspect the parser output
Open the Parse Status & Errors function.
Read through the function and determine what value it returns when no error is detected.
Then inspect the execution logs.
What value is actually produced?
Make a note of it before continuing.

# Step 4: Inspect the branching logic
Next, open the Evaluate Network State node.
This node decides whether the workflow should:
- continue to the user, or
- retry the request.
Compare the value expected by this node with the value produced by the parser.
Do they match exactly?
Remember that branching decisions often depend on exact string matching.
Even a small difference in spelling or formatting is enough to send execution down the wrong path.

# Step 5: Fix the workflow
Update the workflow so that the parser and the branching node use the same success value.
Run the workflow again.
A successful execution should now:
1. retrieve papers,
1. pass through the parser,
1. continue directly to the user,
1. avoid entering the retry loop.

## Checkpoint
After fixing the project, answer the following questions.
1. Did the Arxiv MCP integration fail?
2. Which node actually caused the incorrect behavior?
3. Why did the workflow enter the retry loop?
4. Was this primarily a protocol issue or an orchestration issue? Explain your reasoning.

## What happened?
This bug demonstrates an important principle of multi-agent systems.
A workflow can fail even when every individual component is working correctly.
In this project:
- the MCP integration successfully retrieved information,
- the parser successfully processed the response,
- but the orchestration interpreted the parser's output incorrectly.
As a result, the workflow repeatedly retried a request that had already succeeded.
This is a common class of orchestration bug. The individual nodes behave correctly, but the contract between them is inconsistent.

## Summary
In this lesson, you investigated a workflow that appeared to suffer from repeated agent failures. By following the execution step by step, you discovered that the protocol layer was functioning correctly and the real issue was in the orchestration logic that connected the parser to the branching node.
Being able to separate integration problems from orchestration problems is an essential debugging skill. As workflows become more complex, many failures occur not because an agent or tool is broken, but because information is passed or interpreted incorrectly between otherwise healthy components.
In the next lesson, you'll extend this project by adding another specialized agent to the workflow, increasing both its capabilities and its orchestration complexity.