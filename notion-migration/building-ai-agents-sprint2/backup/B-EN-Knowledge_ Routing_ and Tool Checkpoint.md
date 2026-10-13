# Knowledge, Routing, and Tool Checkpoint

Notion page: https://app.notion.com/p/Knowledge-Routing-and-Tool-Checkpoint-3669418319f38029b9d2d38d5810a090
Backed up before n8n migration

> 💡 What this assessment covers: Validate that the three Sprint 2 capabilities are working together correctly in a single continuous session, and establish a clear connection between what has been built and what the final project requires.

## Where we are
Meridian's Agentflow v2 has grown from a three-node baseline into a genuinely capable agent. Three new capabilities have been built, configured, and tested in isolation this sprint:
- Knowledge retrieval: The meridian-knowledge Document Store is connected to Agent Node A and returns grounded responses from Meridian's internal documentation
- Intent-based routing: The Condition Agent Node classifies consultant queries by intent and routes them to the correct path before any retrieval or API call is made
- Live data access: The HTTP Node retrieves external data and Agent Node B formats it into a professional natural language response
What has not yet been verified is whether all three work together correctly in a single continuous session. Each capability was tested in isolation. A unified session has not yet been run.
This checkpoint asks you to run that session now, before Sprint 3 begins.

## Why this matters for the final project
The final project is an Agentflow v2 that uses all of the relevant Flowise features introduced across the four sprints. By the end of Sprint 3, the agent will have loops, iteration, human approval checkpoints, and modular sub-flows added on top of what exists today.
If the Sprint 2 capabilities are not working together cleanly, problems introduced now become significantly harder to diagnose once Sprint 3 components are layered on top. A routing failure is straightforward to identify in a two-path canvas. The same failure buried inside a flow with loops and sub-flows is not.
Verifying the Sprint 2 build now is what keeps the final project debuggable.

## Overview
Before running the unified test, confirm each capability is in place by checking the following:
Canvas structure:
[TABLE]
  | Component | Expected state |
  | Start Node | Flow State initialised with query_type and status_response keys |
  | Condition Agent Node | Connected from Start Node, two scenarios defined, Instructions field populated |
  | Agent Node A | Connected from knowledge_query output, meridian-knowledge Document Store attached |
  | Direct Reply A | Connected from Agent Node A, Message field set to Agent Node A output variable |
  | HTTP Node | Connected from status_request output, GET method, JSONPlaceholder URL, JSON response type |
  | Agent Node B | Connected from HTTP Node, formatting and failure recovery instructions in System message, no Document Store |
  | Direct Reply B | Connected from Agent Node B, Message field set to Agent Node B output variable |
If any component is missing or misconfigured, return to the relevant lesson and correct it before running the unified test.

## Unified session test
Open the Flowise chat interface and run all six exchanges in a single session without resetting or closing the chat between turns.
Exchange 1 - Knowledge retrieval: What is Meridian's policy for submitting project close-out summaries after an engagement ends?
- Expected: Condition Agent Node routes to Agent Node A. Agent Node A retrieves the relevant chunk from the Document Store and answers from the retrieved content. The HTTP path is not triggered.
Exchange 2 - Context retention after retrieval: How many working days does that give me if my engagement closed last Friday?
- Expected: Agent Node A uses session context to apply the deadline from Exchange 1 to the consultant's specific situation without re-querying the Document Store.
Exchange 3 - HTTP Node live data lookup: Can you check the current engagement status for account reference 1?
- Expected: Condition Agent Node routes to the HTTP path. HTTP Node retrieves data from JSONPlaceholder. Agent Node B returns a professional natural language engagement summary.
Exchange 4 - Context retention after tool use: What was the name of the engagement you just retrieved?
- Expected: Agent Node B uses session context to recall the engagement title from Exchange 3 without re-invoking the HTTP Node.
Exchange 5 - HTTP failure handling: Before this exchange, temporarily change the HTTP Node Target URL to …
https://jsonplaceholder.typicode.com/invalid/endpoint/9999
Save the canvas, then send: Can you check the status for the Bauer account?
- Expected: Agent Node B acknowledges the failure honestly, communicates what happened in plain language, and offers a clear next step without fabricating a status.
After running this exchange, restore the HTTP Node URL to: https://jsonplaceholder.typicode.com/todos/1
Exchange 6 - Out of scope query: Can you give me a summary of Meridian's competitive positioning versus the major operations consultancies in Germany?
- Expected: Agent Node A recognises the query as outside its authorised scope and outputs the defined fallback phrase with a constructive next step.

### Evaluating your results
For each exchange, ask:
- Did the Condition Agent Node route correctly?
- Did the correct Agent Node respond?
- Was the response grounded in retrieved content or formatted API data — not fabricated from general training data?
- Was context retained correctly from the previous turn?
If any exchange fails, diagnose it before moving to Sprint 3. Use the following as your first diagnostic step:
[TABLE]
  | Symptom | Most likely cause |
  | Wrong path selected by Condition Agent Node | Instructions field does not clearly distinguish between the two scenarios |
  | Agent Node A returns generic answer instead of retrieved content | Document Store not connected or Describe Knowledge field is too vague |
  | Agent Node B receives raw JSON instead of formatted response | User message in Agent Node B not referencing the correct variable |
  | Context lost between exchanges | Memory not enabled on the relevant Agent Node |
  | Agent Node B fabricates status on failure | System prompt missing explicit prohibition on fabrication |

## Knowledge quiz
### Question 1
>  In the Meridian Agentflow v2, how does the Condition Agent Node decide which path to route a query down?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d2e397fd-7cd8-4a6b-b009-9a174bdcde58


### Question 2
>  After successfully retrieving engagement data in Exchange 3, Agent Node B re-invokes the HTTP Node in Exchange 4 instead of using session context. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/dcdf168b-d10d-466f-9844-75122e7371aa

### Question 3
>  Which two components together determine whether the Meridian agent routes a query to the Document Store path or the HTTP live data path?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bbf437e5-a345-4223-b038-6b5aad5eb70c

### Question 4
>  Agent Node B receives a network failure error from the HTTP Node and responds with a fabricated engagement status. Which two changes would most directly address this failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cae71420-03e0-4816-aba3-2615347b6a05

### Connecting Sprint 2 to Sprint 3
Sprint 2 added intelligence to the Agentflow v2 through the ability to know what a consultant needs, retrieve the right information, and return a grounded response. Sprint 3 adds orchestration whcih is the ability to handle complex multi-step logic, retry failures automatically, process data iteratively, pause for human approval, and invoke sub-flows as modular components.
Everything built in Sprint 3 sits on top of the Sprint 2 canvas. The node count will grow. The execution paths will become more complex. The Flow State will carry more keys across more steps.
  The agent that passes this checkpoint cleanly is ready for that. One that has unresolved routing failures, memory gaps, or fabrication problems is not — those issues compound as the canvas grows.
Resolve any failures from the unified session test before proceeding to Sprint 3.
