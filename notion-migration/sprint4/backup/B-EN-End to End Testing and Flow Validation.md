# End to End Testing and Flow Validation

Notion page: https://app.notion.com/p/End-to-End-Testing-and-Flow-Validation-3669418319f380e680dae5869d85841e
Backed up before n8n migration

> 💡 What you will work on in this lesson: You will run a complete end-to-end test of the Meridian Agentflow v2 across all capabilities in a single verified session and confirm the canvas is in a production-ready state before presentation preparation begins.

## Setting the scene
Meridian's agent has been refined, secured, and had its three production-blocking failures resolved. The fixes have been validated individually. The model optimisation tested with a greeting, routing tested with an account reference, error handling tested with a forced timeout.
Individual validation is not the same as end-to-end validation. Testing each fix in isolation confirms that the specific failure mode is resolved. It does not confirm that the fixes work correctly together, that one fix has not introduced a regression in another capability, or that the full execution path from consultant query to formatted response is intact across every path in the canvas.
This lesson runs that complete validation. By the end of it, every path in the Meridian Agentflow v2 will have been exercised in a single session and the canvas will be in a confirmed production-ready state.

## Before you start
Confirm the following before opening the chat interface:
Docker:
```powershell
docker ps
```
Both flowise and qdrant containers must show as running. If either is stopped:
```powershell
docker start flowise
docker start qdrant
```
HTTP Node URL:
Confirm the HTTP Node is set to the correct URL, not the test failure URL: https://jsonplaceholder.typicode.com/todos/1
Canvas saved: 
Open the Meridian Base Agent canvas at http://localhost:3000 and confirm the save icon shows no unsaved changes.

## The end-to-end test protocol
Run all seven exchanges across three separate sessions as specified. Do not skip exchanges or combine sessions. The session boundaries are part of the test design.

### Session 1: Knowledge and context retention
Open a new chat session.
Exchange 1 - Knowledge retrieval: What is Meridian's escalation procedure for a severity level 2 client issue?
- Expected: Condition Node passes to Condition Agent → routes to knowledge_query → Agent Node A retrieves from Document Store → returns escalation procedure with the 4 working hours requirement.
- Pass criteria: Response contains content from meridian_engagement_standards.txt. Response does not fabricate policy details not present in the document.
Exchange 2 - Cross-turn context retention: How many working hours would I have left if the issue was first reported at 2pm today?
- Expected: Agent Node A uses session memory to apply the 4-hour escalation window from Exchange 1 to the consultant's specific situation without re-querying the Document Store.
- Pass criteria: Response correctly calculates from the retrieved policy without a new retrieval call. Response references the same policy content established in Exchange 1.
Exchange 3 - Regional knowledge retrieval: What language should client materials be prepared in for a Poland engagement?
- Expected: Condition Agent routes to knowledge_query → Agent Node A retrieves from the Regional Playbook section of the Document Store.
- Pass criteria: Response references Polish language preference from meridian_regional_playbook.txt. Response does not fabricate regional guidance.

### Session 2: Status path and Human Input
Open a new chat session.
Exchange 4 - Status request with Human Input approval: Can you check the current engagement status for account 1?
- Expected: Condition Agent routes to status_request → HTTP Node retrieves data → Condition A confirms data exists → Human Input Node pauses with Proceed and Reject buttons.
- Click Proceed.
- Pass criteria: Agent Node B returns a formatted natural language engagement summary. Response does not contain raw JSON. Direct Reply B delivers the response.
Exchange 5 - Reject the approval
- Open a new session. Send the same status query. When the Human Input Node pauses, click Reject.
- Pass criteria: Rejection message is returned. Agent Node B does not execute. No engagement data is surfaced.

### Session 3: Retry logic and fallback
Open a new chat session.
Exchange 6 - Retry logic
- Temporarily change the HTTP Node URL to: https://jsonplaceholder.typicode.com/invalid/9999
- Save the canvas. Send: Can you check the engagement status for the Krauss account?
- Expected: HTTP Node fails → Condition A output 0 → Custom Function increments counter → Condition B → after 2 retries → Direct Reply C with fallback message.
- Pass criteria: Fallback message returned after retry attempts. No fabricated engagement status in the response. Direct Reply C fires — not Direct Reply B.
- Restore the HTTP Node URL to: https://jsonplaceholder.typicode.com/todos/1
- Save the canvas.
Exchange 7 - Out of scope query
- Open a new session. Send: Can you give me a summary of Meridian's revenue for this financial year?
- Expected: Condition Agent routes to knowledge_query → Agent Node A recognises query as outside its authorised scope → returns fallback phrase with a constructive next step.
- Pass criteria: Agent does not fabricate financial data. Response contains the defined fallback phrase. Response offers a specific next step.

## Results recording
For each exchange record:
[TABLE]
  | Exchange | Path taken | Pass or Fail | Notes |
  | 1 - Knowledge retrieval |  |  |  |
  | 2 - Context retention |  |  |  |
  | 3 - Regional knowledge |  |  |  |
  | 4 - Status with approval |  |  |  |
  | 5 - Reject approval |  |  |  |
  | 6 - Retry logic |  |  |  |
  | 7 - Out of scope |  |  |  |
Any exchange that fails should be diagnosed using the Sprint 3 Orchestration Checkpoint diagnostic table.

## Pass threshold
All seven exchanges must pass before the canvas is considered production-ready for the presentation. A canvas with unresolved failures is not ready for demonstration to a stakeholder. Failures surfaced live during a presentation are significantly more damaging than failures caught and resolved during validation.

## Final canvas checklist
Before closing this lesson confirm:
- [ ] All seven exchanges passed
- [ ] HTTP Node URL restored to https://jsonplaceholder.typicode.com/todos/1
- [ ] Canvas saved
- [ ] Docker logs show no errors. Confirm with docker logs flowise --tail 20
- [ ] No 429 rate limit errors in the logs. If present, note the time and wait before the presentation

> 💡 Takeaway: 
  End-to-end testing is the difference between a canvas that has been configured and a canvas that has been verified. Individual node tests confirm that each component works in isolation. An end-to-end test confirms that they work together. For example, routing decisions are correct, context transfers between nodes as expected, that failure paths exit cleanly, and that the agent's boundaries hold under realistic query conditions. This is the validation that gives a stakeholder confidence that the demonstration they are about to see reflects a system that actually works.