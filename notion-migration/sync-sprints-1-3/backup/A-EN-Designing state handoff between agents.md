# Designing state handoff between agents

Notion page: https://app.notion.com/p/Designing-state-handoff-between-agents-3849418319f3804eb53fd5a64f52cb43
Backed up before n8n migration

The Vela canvas classifies every incoming query into one of three categories: commercial, technical, or hybrid. When the Classifier runs cleanly and the model returns a valid enum value, the Condition node routes correctly and the right specialist agent responds. But the Classifier does not always run cleanly.
If the model returns a response that does not match the structured output schema — because the query was ambiguous, too short to classify, or phrased in a way the model could not interpret confidently — the query_type key stays at its default value of unclassified. The Condition node then has no matching branch. Without a fallback, the canvas has no safe path. The client query is either silently dropped or routed incorrectly using whatever value the state key happened to hold.
This is the stale routing failure mode from the previous lesson applied to a real canvas. The fix is not complex. It is going to be the fourth branch on the Condition node, but the decision about what that branch does is an architectural one: the system needs to respond safely to the client without pretending a classification happened.
Start from your copy of the Sprint 2 canvas (the multi-agent classifier + Commercial / Technical / Hybrid Handler canvas you built in the previous sprint).

## What state recovery means here
State recovery in this context is not about restarting a failed run or restoring a previous canvas state. It is about designing a path the system can take when the state it depends on (query_type ) did not arrive in a usable form.
The Condition node is the consumer of query_type. It has three branches: commercial, technical, and hybrid. Each branch assumes the Classifier wrote a valid value. When that assumption is violated (when query_type is unclassified ), the three branches have nothing to match and the canvas stalls.
The recovery pattern is an explicit fourth branch that catches unclassified and routes to a safe response. Safe means: the client receives a reply, the reply is honest about the system's uncertainty, and no specialist agent is invoked on an unclassified query.

## Step 1: Open the canvas and locate the Condition node
Open your Sprint 2 canvas in Flowise. Click the Condition node. Review the existing branches. There are currently three conditions, each checking {{ $flow.state.query_type }}:
[TABLE]
  | Branch | Type | Value 1 | Operation | Value 2 |
  | 0 | String | {{$flow.state.query_type}} | Equal | commercial |
  | 1 | String | {{$flow.state.query_type}} | Equal | technical |
  | 2 | String | {{$flow.state.query_type}} | Equal | hybrid |
These branches cover the Classifier's expected outputs. There is no branch for unclassified which is the Start Node's default value for query_type and the value that remains if the Classifier does not write a valid enum result.

## Step 2: Add the fallback branch
In the Condition node, add a fourth branch with the following configuration:
[TABLE]
  | Field | Value |
  | Type | string |
  | Value 1 | {{ $flow.state.query_type }} |
  | Operation | equal |
  | Value 2 | unclassified |
![image]((notion-hosted file))
This branch catches any run where the Classifier returned an unusable result including the Start Node's own default value, which means it also catches the case where the Classifier did not run at all.

## Step 3: Add a fallback Direct Reply node
Add a new Direct Reply node to the canvas and connect it to the fourth (unclassified) output of the Condition node.
![image]((notion-hosted file))
Set the Direct Reply node's message to:
```plain text
I wasn't able to determine the type of your query. Could you rephrase or give me a bit more detail so I can connect you with the right team?
```
This response does three things: it acknowledges the client, it is honest about the system's uncertainty, and it gives the client a clear next action. It does not route to a specialist agent, and it does not pretend a classification happened.
![image]((notion-hosted file))

## Step 4: Test with an ambiguous query
Save your canvas, open the chat, and send a test message through the canvas.
Test message: Hi
A one-word greeting gives the Classifier very little signal to classify. 
Expected behaviour:
1. The LLM Classifier runs. The model cannot confidently assign commercial, technical, or hybrid . It returns unclassified as the query_type structured output value.
1. The Update Flow State entries write query_type: "unclassified" to $flow.state.
1. The Condition node evaluates all four branches. The fourth branch matches.
1. The fallback Direct Reply fires with the clarification message.
After the run, check the Flow State values to confirm query_type holds unclassified.
![image]((notion-hosted file))

## Step 5: Test with a second ambiguous query, then verify existing routing
Send a second ambiguous message.
Test message: Can you help me?
Same expectation; fallback Direct Reply fires, Flow State shows query_type: "unclassified".
![image]((notion-hosted file))
Then send one clear commercial query to confirm the three original branches are still working correctly.
Test message: I'd like to upgrade our plan to premium.
Expected behaviour: Classifier returns query_type: "commercial", Condition node routes to the Commercial Agent, fallback Direct Reply does not fire.
![image]((notion-hosted file))
Expected output: Flow State shows query_type: "commercial" after the third test message. The Commercial Agent's response appears in the chat panel.

## What you've built
The canvas now has an explicit recovery path for the most common classification failure, a query the model cannot confidently categorise. The Classifier's unclassified default no longer leaves the Condition node with an unmatched state value and no safe exit. The fallback branch catches it, the Direct Reply handles the client honestly, and the three original specialist paths are unchanged.
The pattern has a broader application: any state key that has a default value and a downstream consumer that depends on it being overwritten needs an explicit recovery branch for the case where the overwrite does not happen. query_type is the clearest example in this canvas, but the same logic applies to any key the Condition node reads.

## Watch out for
The Classifier returning a valid enum value for very short queries. If the model is configured with a prompt that instructs it to always pick one of the three categories as its best guess, it may return commercial, technical, or hybrid even for "Hi" meaning the fallback branch is never reached. If the test queries route to a specialist agent instead of the fallback, check the Classifier's system prompt for language like "always classify" or "pick the closest category." The fallback branch is only reachable if the model is allowed to return unclassified.
The fallback Direct Reply connected to the wrong Condition output. If the fourth branch was added but wired to one of the existing specialist agents by mistake, the canvas will appear to work, but ambiguous queries will be handled by the wrong agent rather than the fallback. Verify the canvas wiring after Step 3 by checking which node the fourth Condition output connects to.
Forgetting to test that existing branches still work. Adding a fourth branch does not automatically break the first three, but the Step 5 verification test is worth running. A configuration error in the Condition node (for example, accidentally changing an existing branch's value) can silently break routing for valid queries while the fallback appears to work correctly.

## Quick reference
[TABLE]
  | Element | Role in this walkthrough | Key setting |
  | Condition node: Branch | Catches unclassified queries | {{ $flow.state.query_type }} equal unclassified |
  | Fallback Direct Reply | Returns a safe response to the client | Clarification message; no specialist agent invoked |
  | Start Node: query_type default | unclassified — the value branch 4 catches | Default set on the Start Node's Flow State panel |
  | LLM Classifier: structured output | Returns unclassified when no confident category | query_type enum: commercial, technical, hybrid, unclassified |

## Summary
The Condition node now has four branches instead of three. The fourth catches unclassified , the value query_type holds when the Classifier cannot confidently categorise a query, and routes to a Direct Reply that responds to the client honestly without invoking a specialist agent.
This is state recovery at the design level: identifying the state value that signals a failure, and building an explicit path the system can take when that value appears, rather than leaving the canvas with no safe exit.
The next lesson extends this thinking to your own project. The task is to design the recovery and failure isolation patterns for your project agent's state architecture. You will identify which state keys have failure modes, what the safe response is in each case, and how one agent's failure should be prevented from affecting what the next agent reads.