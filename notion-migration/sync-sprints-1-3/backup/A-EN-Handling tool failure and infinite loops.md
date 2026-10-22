# Handling tool failure and infinite loops

Notion page: https://app.notion.com/p/Handling-tool-failure-and-infinite-loops-3689418319f380038bfafc2b9a1b9791
Backed up before n8n migration

> 💡 What you will work on in this lesson: Designing deterministic safeguards that prevent a Contigo agent from entering an infinite execution loop when a tool fails and writing a fallback protocol that degrades gracefully without fabricating an answer.
> ➡️ The tool failure scenario in this lesson describes behaviour you will configure in the next lesson when tools are connected to your Chatflow. The design decisions you make here (the Max Iterations value and the fallback instruction) will be implemented directly on the Tool Agent node in the next lesson. Complete the tasks now so your safeguards are ready before the tools go live.

## Setting the scene
Contigo GmbH's loan status tool has been running in internal testing for two weeks without incident. Then, during a scheduled maintenance window, the core banking API goes offline. The tool begins returning a generic 503 error on every call. The agent receives the error, reasons that it has not yet fulfilled the client's request, and calls the tool again. The tool returns another 503. The agent tries again. And again. Within four minutes, the agent has made sixty-three consecutive tool calls against a downed API, consumed a significant portion of the sprint's token budget, and produced no response to the client.
The problem is the agent has no instruction for what to do when those tools fail. Its system prompt tells it to retrieve the loan status before responding. The tool keeps failing. The agent keeps trying. Nothing in the architecture tells it to stop.
This failure mode is one of the most operationally dangerous risks in production agent deployment. It is also entirely preventable with two targeted interventions: a deterministic iteration cap and an explicit fallback protocol.

## Why language model instructions alone are insufficient
The instinctive response to this failure is to add a system prompt instruction: "if the tool fails, stop trying and apologise to the client." This is necessary but not sufficient.
Language models are probabilistic. An instruction to stop after a failure will reduce the frequency of looping. Under certain conditions, with certain query phrasings, or after a specific sequence of tool outputs, the model may reason its way past the instruction and retry the tool anyway. Probabilistic compliance is not an acceptable safety standard for a production system handling client-facing financial workflows.
The only reliable way to cap execution is at the infrastructure level — a hard, deterministic limit enforced by the framework itself, independent of the model's reasoning. In Flowise, this is the Max Iterations parameter on the agent node. When this limit is reached, the framework terminates the execution cycle regardless of what the model would do next. It is a circuit breaker that the model cannot override.
> ➡️ Where this is configured in your Chatflow: In Flowise, the Max Iterations parameter is located in the Additional Parameters of the Tool Agent node. It is a single integer field. Setting it before connecting any tools is the correct order of operations and the safeguard should be in place before the first live tool call is made.
The system prompt fallback is still required. It governs what the agent says to the client after the circuit breaker fires. But the instruction alone, without the infrastructure constraint, is not a safe architecture.
![image]((notion-hosted file))

## Your tasks
### Task A: Configure the circuit breaker
The Tool Agent node you will add has a Max Iterations parameter in its Additional Parameters. Before you get there, decide what value you will set and document your justification. Consider the following. This parameter caps the total number of reasoning and tool-calling cycles the agent can execute before the framework terminates the loop.
Set a value and write two to three sentences justifying your choice. Consider the following:
- The typical number of tool calls a legitimate multi-step Contigo query requires. For example, a query that checks a loan status and then triggers a follow-up document retrieval might require two to three cycles
- The point at which repeated calls to the same failing tool signal a loop rather than legitimate multi-step reasoning
- The cost of setting the limit too high versus too low. This is a limit that is too generous allows significant resource drain before terminating; one that is too tight terminates legitimate multi-step queries prematurely

### Task B: Write the fallback system prompt instruction
Draft a two to three sentence addition to the Contigo agent's system prompt that governs its behaviour when the Max Iterations limit is reached or when a tool returns a persistent error across consecutive calls. When you add the Tool Agent node in the next lesson, this instruction goes in its System Message field as a new paragraph after your existing grounding instruction. Draft it now so it is ready to copy in directly.
Your instruction must address the following three requirements:
Honest acknowledgement: The agent must not fabricate a loan status, generate a plausible-sounding response from its training data, or imply the tool succeeded when it did not. The client must understand that the system encountered a problem.
No technical exposure: The instruction must tell the agent to communicate the failure in professional, client-appropriate language. Error codes, API terminology, and infrastructure references must not appear in the client-facing response.
Clear next step: The agent must offer the client a specific alternative such as directing them to contact their assigned relationship manager or providing Contigo's direct support line.
#### Task C: Evaluate the human-in-the-loop threshold
Not every tool failure warrants an automated fallback. For high-stakes operations, the appropriate response to a failure may not be an automated fallback but a mandatory pause for human review.
Answer the following two questions:
- For Contigo's loan status tool, is an automated fallback sufficient, or does a tool failure require human intervention? Justify your answer.
- For a hypothetical loan disbursement tool that transfers funds directly to a client's account, is the same automated fallback appropriate, or should the architecture enforce a human-in-the-loop step before any retry or alternative action? 

[toggle] Think about the following …
  🔽 Checkpoint 1: Setting the Max Iterations value - A legitimate multi-step query needs enough iterations to complete its work. A looping failure needs to be caught before it drains the token budget. The gap between those two numbers is where your Max Iterations value should sit.
  🔽 Checkpoint 2: The probabilistic compliance problem - A system prompt instruction reduces the frequency of looping. A Max Iterations cap stops it regardless of what the model reasons. One is probabilistic compliance. The other is a hard stop. For a client-facing financial services agent, consider which risk profile is acceptable.
  🔽 Checkpoint 3: Designing the human-in-the-loop threshold - Not every failure carries the same consequence. A status lookup that fails inconveniences the client. A fund transfer that fails carries financial and regulatory consequences. The stakes of the operation determine whether human review is proportionate. 

## Check for Understanding
>  A Contigo agent hits its Max Iterations limit after five consecutive 503 errors from the loan status tool. The system prompt does not include a fallback instruction. What is the most likely agent behaviour?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e820b00b-4cf0-4abe-8c70-96b6bf6aafc0


> 💡 Takeaway: 
  Deterministic safeguards and probabilistic instructions serve different purposes. The Max Iterations cap guarantees the loop stops. The fallback instruction governs what happens after it stops. 
  Together they ensure the client receives a professional, honest response rather than a fabricated answer or a raw error string. Both are required for a production-ready agent in a regulated financial services environment and both need to be designed before the first tool is connected, not after a failure reveals they are missing.

## Checklist for the next lesson
Make sure you have the following done before moving to the next lesson.
From the previous lesson:
- [ ] Three revised system prompt instructions written and documented: retrieval scope, account action boundary, and fallback behaviour
- [ ] Six validation queries prepared (two per instruction) with the expected agent behaviour noted for each
- [ ] Any residual overlap between instructions identified and resolved
From this lesson:
- [ ] Max Iterations value decided and justified in writing
- [ ] Fallback system prompt instruction drafted covering honest acknowledgement, no technical exposure, and a clear next step for the client
- [ ] Human-in-the-loop threshold evaluated for the loan status tool and your conclusion documented