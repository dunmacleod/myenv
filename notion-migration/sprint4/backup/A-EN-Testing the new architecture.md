# Testing the new architecture

Notion page: https://app.notion.com/p/Testing-the-new-architecture-3849418319f38076bd78ec162aaa9e53
Backed up before n8n migration

The canvas you exported at the end of the previous lesson represents your architecture decisions that were made. Implementation is not the same as validation. A canvas that is correctly configured on paper can still behave unexpectedly under real inputs, and the only way to find out is to run it.
This lesson is about structured testing and a planned set of scenarios designed to answer a specific question for each one. 
The question is always the same: 
> Does the canvas behave the way the architecture specifies, or does it not? If it does, you have evidence that the design holds. If it does not, you have a failure point to investigate and fix.
The test scenarios in this lesson are organised in three groups. 
- The first group tests whether the architecture functions correctly under normal inputs. 
- The second group tests the boundary conditions that expose the failure modes identified where edge cases reveal whether safeguards actually work, not just whether they are configured. 
- The third group tests your design decisions specifically (the choices you made in your Sprint 1 brief, your Sprint 2 diagram, and your Sprint 3 specification) to verify that the architecture does what you said it would do, not just what the baseline canvas was already doing.
By the end of this lesson, you will have a documented test record: which scenarios passed, which revealed failures, what you changed, and what remains to be addressed. That record is the backbone of your Presentation Day defense.
> 💡 In this lesson, you will validate that your redesigned architecture solves the limitations of the baseline through targeted test scenarios and document the results for your LS 15 defense.

## Before you start
Open the post-lesson-26.json canvas you exported at the end of the previous lesson. Confirm it loads correctly and that the node structure matches what you completed in the four redesign stages.
Use a document alongside Flowise. You will record the result of every test in that document. The test record is a deliverable, not optional notes. During the presentation, you will be asked which tests you ran, what they revealed, and what you did about any failures.

## Group 1: Baseline function tests
These three tests confirm that the canvas handles normal inputs correctly for each of the core paths in your architecture. They should pass without failures. If any of them fail, the implementation from the previous lesson is incomplete. Stop, fix the gap, and re-run the failing test before moving to Group 2.
### Test 1.1: Standard query, correct routing
Send a query that clearly maps to one of your specialist agents. For a Router, this means a query whose query_type is unambiguous. For a Coordinator, a task that the supervisor should delegate to a specific worker. For an Evaluator, a request that the generator should handle straightforwardly and the evaluator should approve.
- What to observe: Does the canvas route to the correct agent? Does that agent produce a reply that matches its system prompt scope? Does the session complete (a Position 4 log entry written) without error?
- Record: The input, which agent handled it, whether the reply was within scope, and whether the session completed cleanly.
### Test 1.2: Second query in the same session, different routing path
Without closing the session, send a second query that maps to a different specialist than the first. This tests whether the routing key resets correctly between queries within a session.
- What to observe: Does the canvas classify the second query correctly, independently of the first? Does the Condition Node route to a different specialist than it used for Test 1.1? Does the second session complete cleanly?
- Record: Both queries, both routing outcomes, and whether the second query's routing was determined by the second query's content or by a residual value from the first.
### Test 1.3: Query at the edge of one specialist's scope
Send a query that is close to the boundary between two specialist responsibilities. Make it ambiguous enough that the Classifier might classify it either way. For a Router with an Account specialist and a Support specialist, this might be: "The client mentioned their account is performing well but also raised a support question in passing." For a Coordinator, a task that partially overlaps two workers' defined responsibilities. For an Evaluator, a request that is borderline acceptable — one the evaluator might either approve or reject.
- What to observe: Which path does the canvas take? Is the routing or delegation decision consistent with what your Sprint 2 design specified for boundary cases? If the canvas behaves unexpectedly, is it because the system prompt boundary is unclear, or because the Classifier is not discriminating correctly?
- Record: The query, the routing outcome, whether the outcome matches your Sprint 2 specification, and, if it does not, whether the gap is in the system prompt or in the classification logic.

## Group 2: Boundary condition tests
These tests expose the edge cases that reveal whether safeguards work. They are designed to produce the failure conditions identified in the memory and state failure modes lesson and confirm that the safeguards you implemented actually prevent or contain them. Run each test and record the result honestly; a safeguard that does not hold under a boundary test is information, not a failure of the lesson.
### Test 2.1: Rapid consecutive queries, same session
Send three queries in rapid succession within the same session, without waiting for the previous reply to fully complete. This tests whether concurrent or near-concurrent writes to Flow State produce contamination between queries.
- What to observe: Does each query receive a reply based on its own content, or does any reply contain content that belongs to a different query in the sequence? Does the routing key hold the correct value for each query's path, or does a fast second write overwrite a first write that had not yet been read?
- Record: All three inputs, all three outputs, and whether any output appeared to contain content from a different query in the sequence.
### Test 2.2: Deliberate specialist failure simulation
This test requires you to temporarily break one specialist agent so that it cannot complete. The simplest method is to set an invalid model name or remove a required configuration field on one specialist node, run a query that would route to that specialist, then restore the configuration after observing the result.
- What to observe: When the specialist fails mid-execution, does the recovery path activate? Does the routing key reset before the recovery path returns control? Does the user receive a recovery message, or does the session hang? If a recovery message appears, does its text match the actual failure or does it describe the wrong agent or path?
- Record: Which specialist you broke, what the canvas did when the failure occurred, whether the recovery path activated and reset the routing key, and whether the session recovered to a usable state.
After the test, restore the specialist's correct configuration and confirm Test 1.1 still passes.
### Test 2.3: Input that targets persistent store boundary
If your canvas writes to a persistent store, send a query that would normally trigger a persistent store write, but frame the query as if it contains session-specific or identifying content: "My name is [test name] and I need to escalate this." Observe what, if anything, gets written to the persistent store.
- What to observe: Does the write configuration filter out session-specific or user-identifying content, or does the raw input get written as-is? If you open the persistent store and inspect the most recent write, what does it contain?
  - If your canvas does not write to a persistent store, substitute this test with a check of the last_account_summary pattern from the previous lesson: confirm that any intermediate summary key written by a specialist is reset at the start of a new query, not carried over from a previous one.
- Record: What was written to the persistent store (or what the intermediate key contained after a second query), and whether the write content matches the rule you specified in Sprint 3.

## Group 3: Architecture-specific validation tests
These tests are specific to your design decisions. The choices that distinguish your implementation from the baseline canvas. Each test in this group maps to a commitment you made in one of your three sprint deliverables. The test verifies that the implementation actually honours the commitment.
### Test 3.1: Archetype structural test
This test is different for each archetype.
[COLUMN_LIST]
  [COLUMN]
    If you chose The Router: 
    Send a query that the Classifier should route to each of your three specialist paths, one at a time. 
    Confirm that all three paths are reachable and that each specialist's system prompt scope is distinct, a query intended for Specialist A should not produce output that draws on Specialist B's domain.
    
  [COLUMN]
    If you chose The Coordinator: 
    Send a task that requires both workers to contribute to the final answer. 
    Confirm that the supervisor delegates to both workers in the sequence your Sprint 2 design specified, that the Loop Node returns incomplete work to the supervisor rather than passing it directly to reply, and that the final reply synthesises both workers' outputs.
    
  [COLUMN]
    If you chose The Evaluator: 
    Send a request that the generator handles and the evaluator should reject; a request that is close to acceptable but not quite. 
    Confirm that the evaluator node returns a rejection, that the Loop Node routes the rejected output back to the generator with the evaluator's feedback visible in the context, and that the generator's second attempt incorporates the feedback.
    Confirm that the Human Input gate receives the revised output and prompts correctly for approval.
- Record: the inputs used, the sequence of agent activations observed in the Flowise execution trace, and whether the sequence matches the Sprint 2 multi-agent design diagram.
### Test 3.2: Memory specification compliance
Return to your Sprint 3 memory and state architecture specification. Find the three items you designated as highest-priority in the shared/private boundary: the key that must be shared across agents, the key that must remain private to one agent, and the item that must never persist. Design one query that exercises each of these three items. Run the query. Inspect the Flow State after the session completes.
- What to observe: Is the shared key readable by all agents that should access it? Is the private key absent from Flow State visible only in the context window of the owning agent? Is the must-never-persist item absent from any Flow State key and absent from the persistent store?
- Record: Which three items you tested, what you observed in Flow State and the persistent store for each, and whether the observation matches the specification.
### Test 3.3: Justification test
Your Sprint 1 brief justified the chosen architecture against the rejected alternative. The justification named at least one concrete advantage that your chosen design has over the alternative you did not choose.
Design a query that directly exercises that advantage. If you argued the Router is faster than the Coordinator for your use case because routing is stateless and delegation requires a loop, send a query and time the response. If you argued the Evaluator produces higher-quality output than a single-agent alternative, send a request and compare the final output quality against what a single-agent version of the canvas would produce.
- What to observe: Does the canvas produce behaviour that supports the justification you wrote in Sprint 1? This is not a pass/fail test, it is evidence-gathering for your defense. A justification that holds up under a live test is a stronger defense than one stated from the design document alone.
- Record: The query used, what the canvas produced, and whether the result supports or complicates the justification from Sprint 1.

## Checkpoints
After completing all nine tests, work through these questions before closing the lesson:
- [ ] How many tests passed without any failure? List them.
- [ ] How many tests revealed a failure or unexpected behaviour? For each one, did you identify the cause? Did you implement a fix? Does the fix change anything in Stages 1–4 from the previous lesson?
- [ ] Is there any test you could not run because the canvas configuration required a tool or service you do not have access to? Note it — and note how you would run the test if the resource were available.
- [ ] Do the Group 3 test results give you evidence you can use for your presentation? If a test produced output that directly supports a design decision, make a note of what to demonstrate during Presentation Day.
Export the final canvas as [your-canvas-name]__post-lesson-27.json. This is the version you bring to the live session before Presentation Day.

## Check for Understanding
### Question 1
>  During Test 2.1, a learner runs three rapid queries in the same session and finds that the third reply contains the routing outcome from the second query rather than the third. The learner's canvas uses a single global query_type key, not namespaced by session. What is the most likely cause of the contamination?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/22197d44-c088-4541-88eb-66027537237c

## Summary
Structured testing is the final check between a designed architecture and a defensible one. The nine scenarios in this lesson cover three layers: baseline function (does it work under normal conditions?), boundary conditions (do the safeguards hold when conditions are not normal?), and architecture-specific validation (does the implementation honour the design commitments from Sprints 1 through 3?).
The test record you produced in this lesson is the evidence base for your presentation. Presentation Day is a defense of the decisions that produced it. The tests you ran today are what make that defense concrete.
In the next lesson, you will present the redesigned agent, walk through the system diagram, and defend the architecture, memory, and state decisions to peers and instructor.