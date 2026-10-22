# Orchestration Checkpoint

Notion page: https://app.notion.com/p/Orchestration-Checkpoint-3789418319f3806c8a60ecb4a2e8338c
Backed up before n8n migration

> 💡 What will be covered: Validate that the Sprint 3 orchestration capabilities are working together correctly and that the canvas is in a verified state before Sprint 4 begins.

## Where we are
The Meridian Agentflow v2 now has full orchestration capability layered on top of the Sprint 2 intelligence foundation with the completion or knowledge of the following nodes:
- Loop Node: Retry logic for transient HTTP failures with a controlled exit path
- Iteration Node: Processing collections of engagement records in a single execution
- Human Input Node: Approval checkpoint before surfacing sensitive engagement data
- Execute Flow Node: Modular sub-flow invocation for reusable logic
- Custom Function Node: Custom JavaScript for transformations no standard node handles
- MCP: Universal standard for connecting agents to external tools across frameworks

## Canvas verification checklist
Work through every item before running the unified test. Do not skip items because the most common failures in Sprint 3 can come from basic errors such as misspelt keys or incorrect connections.
> ⚠️ Please note that while this list is extensive, you can also reference previous lessons to ensure that your agent is configured properly. 

Start Node
- [ ] Flow State contains all of these keys with correct initial values:
[TABLE]
  | Key | Initial Value |
  | query_type | knowledge |
  | routing_decision | `` |
  | status_response | `` |
  | retry_count | 0 |
  | engagement_list | [{"id":1,"title":"Krauss Manufacturing","completed":false},{"id":2,"title":"Bauer Logistics","completed":true},{"id":3,"title":"Novak Retail","completed":false}] |
  | briefing_output | `` |
  | approval_status | `` |
- [ ] Input Type: Chat Input
- [ ] Ephemeral Memory: Off
- [ ] Connected to Condition Node

Condition Agent Node (top-level routing)
- [ ] Input: {{ $flow.input }} — typed manually, not selected from dropdown
- [ ] Connected from Start Node
> ⚠️ If {{ $flow.input }} does not resolve correctly, temporarily set Value 1 to a static test phrase like generate the weekly engagement briefing to confirm the keyword check works. Then restore {{ $flow.input }}.

Condition Agent Node
- [ ] Model: API credential connected
- [ ] Memory: Off 
- [ ] Input: {{ $flow.input }} — typed manually, not selected from dropdown
- [ ] Scenario 0: status_request → Output 0 → HTTP Node
- [ ] Scenario 1: knowledge_query → Output 1 → Agent Node A
- [ ] Instructions contain explicit default to status_request when uncertain
> ⚠️ The scenario order is critical. status_request must be Scenario 0. If knowledge_query is Scenario 0, the Condition Agent Node defaults to the knowledge path for ambiguous queries.

HTTP Node (Path B)
- [ ] Method: GET
- [ ] URL: https://jsonplaceholder.typicode.com/todos/1 — confirm this is NOT the test failure URL
- [ ] Response Type: JSON
- [ ] Connected from Condition Agent Node output 0

Condition A
- [ ] Type: String
- [ ] Value 1: {{ httpAgentflow_0.data }}
- [ ] Operation: Is Empty
- [ ] Output 0 (true — empty — HTTP failed) → Custom Function Node
- [ ] Output 1 (false — not empty — HTTP succeeded) → Human Input Node
> ⚠️ These outputs may have to be switched depending on the scenario you are working on. Output 0 fires when the condition IS true meaning data IS empty which is the failure path. Output 1 fires when data exists as the success path.

Human Input Node
- [ ] Description Type: Fixed
- [ ] Description contains {{ httpAgentflow_0.data }}
- [ ] Feedback: On
- [ ] Proceed output → Agent Node B
- [ ] Reject output → Direct Reply with rejection message
- [ ] Connected from Condition A output 1

Custom Function Node
- [ ] Input Variable: retryCount = {{ $flow.state.retry_count }}
- [ ] JavaScript returns String(count + 1)
- [ ] Update Flow State: retry_count = {{ customFunctionAgentflow_0.output }}
- [ ] Connected from Condition A output 0

Condition B
- [ ] Type: Number
- [ ] Value 1: {{ $flow.state.retry_count }}
- [ ] Operation: larger
- [ ] Value 2: 2
- [ ] Output 0 (true — retries exceeded) → Direct Reply C
- [ ] Output 1 (false — retry available) → Loop Node

Loop Node
- [ ] Loop Back To: HTTP Node
- [ ] Max Loop Count: 2
- [ ] Connected from Condition B output 1

Direct Reply C
- [ ] Message: fallback text about service unavailable
- [ ] Connected from Condition B output 0

Agent Node A
- [ ] Model: Using saved credential
- [ ] System message: full four-element system prompt
- [ ] meridian-knowledge Document Store connected
- [ ] Connected from Condition Agent Node output 1

Direct Reply A
- [ ] Message: {{ agentAgentflow_0.output }} — confirm .output suffix is present
- [ ] Connected from Agent Node A

Agent Node B
- [ ] Model: Using saved credential
- [ ] System message: formatting and failure recovery instructions
- [ ] No Document Store connected
- [ ] Connected from Human Input Node Proceed output

Direct Reply B
- [ ] Message: Agent Node B output variable with .output suffix
- [ ] Connected from Agent Node B

Docker configuration
- [ ] Both containers running; confirm with docker ps
- [ ] Flowise started with HTTP_SECURITY_CHECK=false if Execute Flow Node was used
- [ ] Qdrant running at http://192.168.x.x:6333
## Session test
Run all five exchanges in a single session without resetting between turns.
#### Exchange 1 - Knowledge retrieval
- What is Meridian's escalation procedure for a severity level 2 issue?
- Expected: Condition Node → Condition Agent → Agent Node A → Direct Reply A with policy content.
#### Exchange 2 - Status request with Human Input
- Can you check the engagement status for account 1?
- Expected: Condition Agent → HTTP Node → Condition A → Human Input Node pauses and displays data. Click Proceed. Agent Node B formats response → Direct Reply B.
#### Exchange 3 - Reject the approval
- Open a new session. Send the same status query. This time click Reject on the Human Input Node.
- Expected: Direct Reply returns the rejection message without Agent Node B executing.
#### Exchange 4 - Retry logic
- Temporarily change the HTTP Node URL to: https://jsonplaceholder.typicode.com/invalid/9999
- Send: Can you check the engagement status for the Krauss account?
- Expected: HTTP Node fails → Custom Function increments counter → after 2 retries → Direct Reply C with fallback message.
- Restore the URL to: https://jsonplaceholder.typicode.com/todos/1
#### Exchange 5 - Engagement briefing
- Open a new session and send: Can you generate the weekly engagement briefing?
- Expected: Condition Node detects "briefing" → routes to Execute Flow Node or briefing path → returns engagement summaries.

## Diagnostic table
If any exchange fails, use this to identify the cause quickly:
[TABLE]
  | Symptom | Most likely cause |
  | All queries go to Agent Node A | Condition Node not connected to Start Node |
  | Status request goes to Agent Node A | Condition Agent Node Memory is on; turn it off |
  | Human Input Node not appearing | Edge from Condition A output 1 missing |
  | Retry loop never exits | Condition B exit path not wired to Direct Reply C |
  | Briefing goes to Agent Node A | Condition Node Value 2 field has a typo or extra space |

## Knowledge quiz
### Question 1
>  The Loop Node in Meridian's canvas has Max Loop Count set to 2 and loops back to the HTTP Node. The HTTP Node fails on every attempt. What happens after the second retry?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/db64256a-841b-4414-be38-fb0fdeebeceb

### Question 2 
>  The Human Input Node is placed between Condition A output 1 and Agent Node B. A consultant clicks Proceed. What happens next?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d382fe32-e13b-467d-bda3-83b4b81b138f

### Question 3
>  A Custom Function Node returns JSON.stringify(dataArray) where dataArray contains three engagement records. What does the downstream Condition Node receive?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/ae5728dd-ee2c-4844-91ab-2ed1d4f66d34

### Question 4
>  Meridian builds an MCP server exposing its Document Store. A client organisation using Langflow wants to query the same knowledge base. What do they need to do?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/283cf756-b1d1-4bb9-bce0-56dc45018b7f

### Connecting Sprint 3 to Sprint 4
Sprint 3 added orchestration depth to the Agentflow v2 such as loops for resilience, iteration for scale, human checkpoints for governance, and modular sub-flows for maintainability. The canvas is now a genuinely capable system.
Sprint 4 is about making what exists production-ready with end-to-end testing, system prompt refinement, documentation, and presentation preparation. The agent that passes this checkpoint cleanly is ready for that final phase.