# System Prompt Improvements

Notion page: https://app.notion.com/p/System-Prompt-Improvements-3689418319f380439d09fc992b5e6d75
Backed up before n8n migration

> 💡 What you will work on in this lesson: Using the results of your eight validation tests from the previous lesson to diagnose weaknesses in your system prompt, rewrite the instructions that produced unexpected behaviour, retest until all eight tests pass, and produce a finalised system prompt that is ready for the Sprint 3 assessment.

## Setting the scene
Contigo GmbH's support agent is running on the Tool Agent node with memory, retrieval, and tools all connected. The eight validation tests gave you the first real evidence of how your system prompt performs under realistic query conditions.
Some tests will have passed cleanly. Others may have revealed gaps such as a query that triggered the wrong tool, a fallback phrase that did not fire when it should have, an account action boundary instruction that was too vague to prevent the agent from implying it could perform a write operation.
This lesson is where you act on that evidence. A system prompt that passes a controlled test set once is a starting point. A system prompt that has been diagnosed, revised, and retested against known failure cases is a production-ready instruction set.
The work you do here directly feeds into the Sprint 3 assessment. The finalised system prompt you produce in this lesson is what the Sprint 3 assessment will evaluate.

## The system prompt review framework
Before diagnosing your test results, apply the following four-question framework to your current system prompt. Read each instruction against each question and flag any instruction that cannot answer all four clearly.
- Question 1: Is the scope explicit? Does the instruction specify exactly what the agent should and should not do in this situation? An instruction that says "answer helpfully" has no explicit scope. An instruction that says "answer using only the content retrieved from the Qdrant knowledge base and do not use general training knowledge" has an explicit scope.
- Question 2: Is the invocation condition specific? Does the instruction specify the exact condition that must be present before the agent takes the described action? For tool descriptions, this means the specific query characteristic that triggers invocation. For system prompt instructions, this means the specific situation the instruction governs.
- Question 3: Is the exclusion stated? Does the instruction say what the agent should not do as well as what it should do? Instructions that only describe desired behaviour leave the agent to infer what is prohibited. Explicit exclusions remove that inference.
- Question 4: Is the boundary between instructions clear? Read all your instructions together. Is there any query that could satisfy two instructions simultaneously? Any vocabulary that appears in more than one instruction's scope? Boundary ambiguity is the most common source of inconsistent behaviour in multi-instruction system prompts.

## Your tasks
## Task A: Apply the framework to your current system prompt
Review each of the three core instructions in your Tool Agent system prompt (retrieval scope instruction, the account action boundary instruction, and the fallback behaviour instruction) against the four framework questions above.
For each instruction, complete the following table:
[TABLE]
  |  | Retrieval scope | Account action boundary | Fallback behaviour |
  | Scope explicit? |  |  |  |
  | Invocation condition specific? |  |  |  |
  | Exclusion stated? |  |  |  |
  | Boundary clear? |  |  |  |
Mark each cell as 
- ✅ if the instruction satisfies the criterion or ❌ if it does not. 
- For every ❌, write one sentence describing what is missing and what failure mode that omission enables.

## Task B: Diagnose your test results
Return to the eight validation test results you recorded. For every test that did not produce the expected behaviour, complete the following diagnosis:
### Step 1: Identify the failure category
Classify each failure into one of the following four categories:
- Wrong tool invoked: The agent selected a tool other than the one the query should have triggered
- Tool not invoked: The agent generated a response from training data instead of invoking the appropriate tool
- Fallback did not fire: The agent generated a response for an out-of-domain query instead of delivering the fallback phrase
- Boundary failure: The agent implied it could perform an action it cannot, or retrieved information when it should have directed the client to another channel
### Step 2: Trace the failure to its instruction
For each failure, identify which specific instruction (or absence of instruction) caused it. Use the framework from Task A to guide your diagnosis. A wrong tool invocation usually traces to an invocation condition that is not specific enough. A fallback failure usually traces to a scope instruction that does not explicitly prohibit the use of general training knowledge.
### Step 3: Write a targeted revision
For each failure, write a revised version of the instruction that caused it. Your revision must directly address the specific weakness identified in Step 2. Do not rewrite the entire system prompt. Make targeted changes only. A revision that changes everything makes it impossible to know which change fixed which problem.

## Task C: Implement and retest
Enter your revised instructions into the System Message field of the Tool Agent node. Save the Chatflow.
Run only the tests that previously failed. Do not rerun all eight tests yet. For each previously failing test, record whether the revised instruction produced the expected behaviour.
If the test now passes, mark it resolved. If it still fails, return to Task B Step 2 and re-examine the instruction. A persistent failure after a targeted revision usually means the diagnosis was incomplete. The failure is caused by a different instruction than the one you revised, or by a boundary conflict between two instructions.
Once all previously failing tests pass, run all eight tests in sequence to confirm that your revisions did not introduce new failures. This full regression test is the final confirmation that your system prompt is stable.

## Task D: Produce the finalised system prompt
Write out your complete, finalised system prompt as a single document. This is the version you will carry into the Sprint 3 assessment and the Sprint 4 presentation.
Your finalised system prompt must include all of the following elements in this order:
1. Role and context statement: One to two sentences establishing who the agent is, what organisation it represents, and what its operating context is.
1. Retrieval scope instruction: The revised instruction specifying that the agent answers using only retrieved content from the Qdrant knowledge base and does not use general training knowledge.
1. Account action boundary instruction: The revised instruction specifying what the agent can explain versus what it cannot perform, and where to direct clients when an account change is requested.
1. Tool invocation guidance: One to two sentences in the system prompt reinforcing when the loan status tool should be invoked, particularly when it requires a clear application reference from the client before being called.
1. Fallback behaviour instruction: The revised instruction specifying the exact fallback phrase, the trigger condition, and the next step for the client.
1. Tool failure fallback: The instruction specifying what the agent says when a tool returns an error or the Max Iterations limit is reached by covering honest acknowledgement, no technical exposure, and a clear next step.

[toggle] Checkpoints
  - Checkpoint 1: Diagnosing a wrong tool invocation - When the agent invokes the wrong tool, the problem is almost always in the invocation condition (What the description says must be true before the tool is called). Read the invocation condition of the tool that was incorrectly selected. Then read the query that triggered it. Find the specific phrase in the query that matched the invocation condition semantically and revise the condition to exclude that match explicitly.
  - Checkpoint 2: Diagnosing a fallback failure - When the fallback does not fire for an out-of-domain query, the retrieval scope instruction is usually not prohibitive enough. The model found a plausible response from its training data and the instruction did not explicitly prevent it from using that knowledge. The fix is to make the retrieval scope instruction more restrictive.
  - Checkpoint 3: Diagnosing a boundary failure - When the agent implies it can perform an account action, the account action boundary instruction is missing an explicit exclusion. The instruction may describe what the agent should do but not what it must not do. Adding a sentence that explicitly states "you cannot make changes to any client account under any circumstances" is usually sufficient to close this gap.
  - Checkpoint 4: Regression testing logic - Running only the previously failing tests after a revision confirms the fix worked. Running all eight tests after all revisions confirms no new failures were introduced. Both steps are necessary — a targeted fix that resolves one failure while breaking another is not a net improvement.

[toggle] Answer Key: Finalised System Prompt Reference
  Note: The following is a reference example of a complete finalised system prompt. Your version should reflect your own diagnostic work and the specific revisions you made — it should not be identical to this example. Use it to check that your system prompt includes all required elements and that each instruction is explicit, specific, and non-overlapping.
  > You are a support agent for Contigo GmbH, a financial services firm operating across Germany, Austria, and the Netherlands. Your role is to assist clients with loan product queries, compliance questions, account procedure explanations, and application status checks.
    Answer all client questions using only the content retrieved from the Contigo knowledge base. Do not use your general training knowledge under any circumstances, even if you believe the answer is correct. If the retrieved context does not contain a relevant answer, deliver the fallback phrase below. Do not supplement with outside knowledge.
    You can explain account procedures and policies retrieved from the knowledge base. You cannot make changes to any client account under any circumstances. If a client requests an account modification of any kind, respond by explaining that you are unable to perform account changes and direct them to contact their Contigo relationship manager or visit the client portal at contigo.de/portal.
    Use the loan status lookup tool only when the client explicitly provides a specific application reference number such as APP-7741. Do not invoke this tool for general questions about loan application timelines or procedures. Those queries should be answered using the knowledge base.
    If the retrieved context does not contain information relevant to the client's query, respond with exactly: "I do not have that information in my current knowledge base. Please contact a Contigo advisor directly for further assistance." Do not add to or vary this phrase.
    If a tool returns an error or fails to produce a result, respond with: "I was unable to retrieve that information at this time. Please contact your Contigo relationship manager directly for assistance." Do not expose error codes, API references, or technical details in any client-facing response.

## Checklist: Confirm before moving on
- [ ] Four-question framework applied to all three core instructions
- [ ] All test failures from the diagnosis-task lesson diagnosed and traced to specific instructions
- [ ] Targeted revisions written for each failing instruction
- [ ] Previously failing tests retested and confirmed passing
- [ ] Full regression test of all eight tests completed with no new failures
- [ ] Finalised system prompt written with all six required elements
- [ ] Finalised system prompt saved in the Tool Agent System Message field
- [ ] Chatflow saved after final system prompt update

> 💡 Takeaway: 
  A system prompt is not complete when the instructions are written. It is complete when the agent's behaviour matches the instructions consistently across a full range of realistic queries. Diagnosis, revision, and regression testing are not extra steps. 
  They are the process. The finalised system prompt you produced in this lesson is the most important single artifact in your Chatflow build. It is what determines whether the agent behaves reliably when a real client asks an unexpected question.