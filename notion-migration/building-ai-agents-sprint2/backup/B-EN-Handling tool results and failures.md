# Handling tool results and failures

Notion page: https://app.notion.com/p/Handling-tool-results-and-failures-3669418319f380088c77c79df2e64d5b
Backed up before n8n migration

> 💡 What you will work on in this lesson: Design professional result integration and graceful failure handling for both the successful HTTP response and failure states in Meridian's Agentflow v2.

## Setting the scene
Meridian's Agentflow v2 is now routing queries by intent and retrieving live engagement data through the HTTP Node. When a consultant asks about an engagement status, the flow executes correctly. The Condition Agent Node classifies the query, the HTTP Node fetches the data, Agent Node B formats it, and Direct Reply B returns the response.
The happy path is working. But two failure patterns have emerged in extended testing that the current configuration does not handle adequately.
The first is a presentation problem. When the HTTP Node returns a successful response, Agent Node B sometimes reproduces the raw JSON structure directly rather than transforming it into natural language. A consultant asking about an engagement status receives something like:
```json
{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}
```
This is technically correct but reads like a database dump rather than a professional consulting tool response.
The second is a failure handling problem. During testing, a developer deliberately pointed the HTTP Node at an invalid URL to simulate an API outage. Instead of acknowledging the failure and directing the consultant to their engagement manager, Agent Node B generated a fabricated status which consisted of hallucinating that an engagement was active and in the implementation phase when the HTTP Node had returned an error.
Both problems are system prompt failures. The HTTP Node and Agent Node B are working as configured. The agent is failing to handle outputs appropriately because it has not been given explicit instructions for how to do so.

## The two output states
Your task involves designing Agent Node B's behaviour for two distinct output states. Review both before beginning.
#### Output state 1: Successful HTTP response
```xml
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```
Treat this as Meridian's mock engagement record where:
- id = engagement reference number
- title = engagement name
- completed = whether the engagement is closed (false = active, true = closed)
Agent Node B must transform this into a natural, professional response that presents the key information clearly without reproducing the raw JSON structure or field names.

#### Output state 2: HTTP Node failure
When an HTTP Node request fails, Flowise returns an error response to the downstream node. The error typically appears as a string containing the HTTP status code and error message rather than the expected JSON body.
Agent Node B must acknowledge the failure clearly, communicate what happened in plain language appropriate for a consulting professional, and provide a clear next step without fabricating a status or presenting the error as a partial success.

## Your mission
#### Task A: Design the successful result response
Assume Agent Node B has received the JSONPlaceholder response shown in Output State 1. Write the exact natural language response Agent Node B should produce for the following consultant query:
> "Can you check the current engagement status for account reference 1?"
Your response must satisfy the following requirements:
- Present the key information from the JSON output in natural, professionally phrased language appropriate for Meridian's consulting environment
- Do not reproduce the raw JSON structure or field names in the response
- Include the most operationally relevant fields such as engagement reference, name, and active or closed status
- End with a brief offer to provide further detail or assistance if needed
This task tests your ability to write the kind of response a well-designed agent would produce before writing the instruction that produces it.

#### Task B: Write the result-handling instructions
Draft a system prompt instruction for Agent Node B that tells it exactly how to behave when the HTTP Node returns an error state. 
Draft system prompt instructions for Agent Node B that cover both output states. Your prompt must specify:
1. How to format a successful HTTP response into the kind of natural-language reply you designed in Task A — including which fields to surface and which to suppress.
1. How to behave when the HTTP Node returns an error state (the three requirements below).
The two sections together replace the existing Agent Node B system message. Indicate clearly to the model which behaviour applies when.

Your instruction must address the following three requirements:
Draft system prompt instructions for Agent Node B that cover both output states. Your prompt must specify:
- Acknowledge the failure honestly: Agent Node B must not present the error as a success or generate a fabricated status. The consultant must understand that the lookup did not return a result.
- Communicate the relevant detail: Agent Node B should explain what happened in plain language without exposing raw HTTP status codes, technical error strings, or JSON error objects that are not meaningful to a consulting professional.
- Provide a clear next step: The instruction must specify what Agent Node B should offer after communicating the failure — for example, suggesting the consultant contact their engagement manager directly, or offering to search Meridian's knowledge base for related information instead.

#### Task C: Update Agent Node B and test both output states
Open Agent Node B's settings and replace the existing system message with the instructions you wrote in Task B. The previous formatter prompt is superseded by your new version, which now handles both successful and failed lookups.
Enter your failure recovery instruction from Task B into the System message of Agent Node B on your canvas. Then run the following two tests in separate chat sessions and record the agent's responses.
Test 1 Successful lookup: "Can you check the current engagement status for account reference 1?" 
Evaluate the response against the requirements in Task A. Does Agent Node B present the information professionally? Does it avoid reproducing raw JSON field names? Does it identify the most operationally relevant information?
Test 2 Simulated HTTP Failure: "Can you pull up the status for engagement ENG-9999?" 
To simulate a failure, temporarily change the HTTP Node's Target URL to an invalid endpoint:
```json
https://jsonplaceholder.typicode.com/invalid/endpoint/9999
```
This returns a 404 response. Save the canvas and send: “Can you check the engagement status for the Bauer account?”
Evaluate the response against Task B requirements. Does Agent Node B acknowledge the failure without fabricating a status? Does it communicate what happened in plain language? Does it offer a clear next step?
After testing, restore the HTTP Node URL to:
```json
https://jsonplaceholder.typicode.com/todos/1
```
If either test produces an inadequate response, identify which part of the system prompt instruction failed to produce the expected behavior and revise it. Re-run the test after each revision and document what changed.

#### Task D: Simulate a complete API outage
Change the HTTP Node's Target URL to a domain that does not exist: https://api.meridian-internal-nonexistent.com/engagements/status
Save the canvas and send: Can you check the engagement status for the Krauss account?
Observe and record Agent Node B's response. Evaluate whether the current system prompt instruction handles a complete connection failure differently from a 404 not-found response.
> What to think about: A 404 response returns a structured HTTP error with a status code. A complete connection failure returns no response at all — Flowise receives a network error and passes it downstream as a generic error string. These are two different failure modes that may produce different agent behaviours even with the same system prompt instruction.
After testing, restore the HTTP Node URL to: https://jsonplaceholder.typicode.com/todos/1

> 💡 Takeaway: 
  A tool that executes correctly is not the same as an agent that handles tool results well. The gap between the HTTP Node returning an error and Agent Node B responding to that error professionally is entirely governed by the system prompt. 
  Clear instructions for both successful result integration and failure recovery are the difference between an agent that behaves reliably under real conditions and one that fabricates confidence when it should be acknowledging uncertainty.
