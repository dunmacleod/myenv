# Final Flowise and AI Agent Refinement

Notion page: https://app.notion.com/p/Final-Flowise-and-AI-Agent-Refinement-3689418319f380b795cfcdc8121fc01a
Backed up before n8n migration

> 💡 What you will work on in this lesson: You will diagnose three production-blocking failures from execution evidence and apply targeted fixes to the model configuration, tool descriptions, and system prompt.

## Setting the scene
Meridian Consulting's internal agent has passed its security review and is entering its final refinement phase before the stakeholder presentation. The canvas is configured, the four-layer security stack is understood, and the agent behaves correctly under ideal conditions.
A pre-launch stress test simulating a full day of usage across Meridian's consulting team has surfaced three failures. All three have clear causes visible in the execution traces. All three have targeted fixes that do not require rebuilding the canvas. Your task is to identify each cause and apply the correct fix independently.

## The three test failures
### Failure 1: Latency and cost 
During the stress test, average response latency was 18 seconds per query. Token cost per session was approximately €0.94, projecting to €940 per month at Meridian's expected volume of 1,000 monthly sessions.
Inspection of the Agent Node reveals what the model is set to for every interaction including simple greetings, status acknowledgements, and one-sentence follow-up responses that require no complex reasoning.

### Failure 2: Tool invocation paralysis
Eleven queries requesting engagement status lookups were routed incorrectly during the stress test. The agent returned a generic knowledge base response rather than triggering the HTTP Node for a live lookup. Review of the Agent Node configuration reveals the Describe Knowledge field currently reads:
> "Use this to answer questions about Meridian's internal processes and engagements."
The HTTP Node's tool description reads:
> "Use this tool to help with engagement-related queries."
Both descriptions use the word "engagement." The agent cannot distinguish between them on semantic grounds and defaults to the knowledge source.

### Failure 3: Hallucination on tool failure
During three test sessions, the HTTP Node returned a 504 timeout error. In all three cases, the agent ignored the error and generated a fabricated engagement status including specific phase names and milestone dates that were not present in any returned data. Review of the Agent Node's system prompt reveals no instruction governing what the agent should do when the HTTP Node returns an error code. The agent defaulted to general helpfulness and filled the information gap with plausible-sounding fabrication.

## Your tasks
### Task A: Resolve Failure 1 - Model optimisation
Reconfigure the Agent Node model to address the latency and cost problem. Document your solution covering:
- Which AI model you will switch to and why it is appropriate for Meridian's standard consulting query types
- What the projected monthly cost impact would be at 1,000 monthly sessions using the relative token cost difference between gemini-3.1-flash-lite and your chosen model
- Write two to three sentences documenting your configuration change and its expected operational impact
> ➡️ Checkpoint: Meridian's queries require fast retrieval and clean presentation of grounded results. Ask yourself could a competent person answer this query correctly after reading the retrieved content once? If yes, a frontier reasoning model is not needed. Review the Gemini model comparison before deciding.

### Task B: Resolve Failure 2 - Describe knowledge base and tool description refinement
Rewrite both the Describe Knowledge field in the Agent Node's Knowledge configuration and the HTTP Node's tool description to eliminate the routing ambiguity that caused eleven invocation failures. Each revised description must satisfy these requirements:
- Describe Knowledge field: State precisely what documented content the knowledge base contains. Specify that it covers static internal policies, procedures, and guidelines. Be between two and three sentences.
- HTTP Node tool description: State precisely what live data the tool returns. Specify the exact condition that must be present before the tool should be invoked. For example, a specific account reference or an explicit request for current live status. Distinguish it clearly from the knowledge base. Be between two and three sentences.
> ➡️ Checkpoint: The routing failures happened because both descriptions used language that could apply to the same query. Look at what a live API call requires structurally that a document retrieval does not. A query containing "account 1" or "account reference" is structurally different from a general policy question. Build the invocation condition around that signal.

### Task C: Resolve Failure 3: Error handling instruction
Write a two to three sentence addition to the Agent Node's system prompt that governs its behaviour when the HTTP Node returns an error code.
Your instruction must address all three requirements:
- No fabrication: The agent must not generate a plausible status when the HTTP Node has not returned one
- Honest acknowledgement: The consultant must understand the information is temporarily unavailable
- Actionable next step: The agent must offer a specific alternative path, not leave the consultant without a resolution
> ➡️ Checkpoint: A vague instruction like "do not guess" tells the agent what not to do but leaves the next action undefined. A probabilistic model defaults to helpfulness meaning it generates a plausible continuation regardless. Writing the exact fallback phrase inside the instruction gives the agent a concrete output to produce. Include three elements: acknowledge the information is unavailable, avoid implying the agent found a result, and direct the consultant to a specific next step.

### Task D: Validate all three fixes
Test each failure scenario independently. Do not combine them in a single session. You will not be able to isolate which fix is incomplete.
Fix 1 validation - Send a simple greeting: Hello, I am preparing for a client meeting this afternoon
- Compare response time against the pre-fix 18-second baseline. 
- Confirm the model shown in the Agent Node settings has changed.
Fix 2 validation - Send a query containing a specific account reference: Can you check the current engagement status for account 1?
- Confirm the flow routes to the HTTP Node rather than returning knowledge base content.
Fix 3 validation - Temporarily change the HTTP Node URL to an invalid endpoint: https://jsonplaceholder.typicode.com/invalid/9999
- Send: Can you check the engagement status for the Krauss account?
- Confirm the agent returns your configured fallback phrase with no fabricated engagement details. 
- Restore the correct URL after testing: https://jsonplaceholder.typicode.com/todos/1

## Check for Understanding
>  Meridian's agent receives a 504 timeout from the engagement status tool and responds: "The ENG-1041 engagement is currently in active delivery with a Q3 milestone review scheduled." No such status was returned by the tool. Which system prompt instruction would most reliably have prevented this specific response?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a165dd15-e308-484d-b13c-909a03b6f678


> 💡 Takeaway: 
  Production refinement is about removing failure modes. The three fixes in this lesson (model optimisation, description precision, and error handling instructions) each address a specific, evidence-based failure identified in execution traces. Targeted fixes grounded in trace evidence are significantly more reliable than iterative prompt tweaking guided by intuition.
