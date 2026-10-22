# Reading and debugging agent graphs

Notion page: https://app.notion.com/p/Reading-and-debugging-agent-graphs-3669418319f380f0a73ae561f909579a
Backed up before n8n migration

> 💡 What you will work on in this lesson: Students trace three failing execution logs from Meridian's deployed agent and propose targeted fixes for each failure mode.

## The scenario
Three failure reports have arrived from Meridian's consulting team two days after the agent went live. Each describes a different symptom. Your task is to read each execution trace, identify the specific failure point using the framework from the previous lesson and propose a targeted fix.
Reading a raw execution trace is more reliable than testing different chat messages in the UI. The trace shows exactly what the agent thought, what it tried to do, and what it received. This makes the origin of a failure locatable with precision.

## The three failure traces
### Trace Log A: The frozen agent
```json
{
  "user_input": "What is the status of my laptop replacement order?",
  "agent_config": {
    "tools_connected": 15
  },
  "trace": [
    {
      "thought": "I have many tools available. I should clarify 
       what order number they are referring to before proceeding.",
      "action": null
    },
    {
      "final_output": "Could you please provide more details 
       about your order so I can assist you better?"
    }
  ]
}
```

### Trace Log B: The cascading hallucination
```json
{
  "user_input": "Can I expense a new standing desk?",
  "trace": [
    {
      "thought": "I need to check the expense policy.",
      "action": "Document Store retrieval — query: standing desk expense",
      "observation": "0 documents found."
    },
    {
      "thought": "No policy found. I will apply the standard 
       €500 office equipment stipend based on industry norms.",
      "action": "Update Flow State — key: equipment_stipend, value: €500"
    },
    {
		  "user_followup": "Great — I will buy a €450 desk. 
		   Can you confirm the budget is available?",
		  "action": "HTTP Node — GET engagement budget check",
		  "observation": "Request sent with equipment_stipend: €500 
		  from Flow State. API returns malformed response no budget record found for assumed stipend value."
		}
  ]
}
```

### Trace Log C: The endless routing loop
```json
{
  "trace": [
    {"node": "Agent Node", 
     "thought": "IT issue. Need employee ID before routing.",
     "action": "Pass to Loop Node"},
    {"node": "Loop Node", 
     "action": "Return to Condition Node"},
    {"node": "Condition Node", 
     "check": "Employee ID present?", 
     "result": "False — return to Agent Node"},
    {"note": "Cycle repeats until token budget exhausted."}
  ]
}
```

## Your tasks
### Task A: Diagnose Trace Log A
The agent was given fifteen tools but invoked none. 
Answer the following:
- What architectural condition caused the Agent Node to ask for clarification instead of invoking the correct tool?
- What specific canvas change would resolve this?
> ➡️ Checkpoint: The Agent Node's thought began with "I have many tools available." When too many tools with overlapping descriptions are connected, the model cannot confidently select the correct one. Consider what an appropriate maximum number of well-scoped tools looks like for a single Agent Node.

### Task B: Diagnose Trace Log B
A hallucination was written to Flow State and then acted upon by the HTTP Node. This produces a real reimbursement ticket based on a fabricated policy figure. 
Answer the following:
- At which exact step did the failure become irreversible? Identify the action that converted a reasoning error into a structural one where the fabricated value left the agent's reasoning and entered the execution path as an input to a downstream node.
- Write a two-sentence addition to the Agent Node's system prompt that would prevent it from writing assumed or inferred information to Flow State when retrieval returns zero results.
> ➡️ Checkpoint: The hallucination had two stages: The agent assumed a figure, then wrote it to Flow State. Which of these was the point of no return? Once a fabricated value is written to Flow State, every downstream node that reads from that key treats it as verified fact.

### Task C: Diagnose Trace Log C
The loop cycled indefinitely because the exit condition was never met. 
Answer the following:
- The Loop Node in Agentflow v2 does not have a forward output anchor. Its only function is to redirect execution backward. This means the exit path cannot come from the Loop Node itself. Which node in Trace Log C is responsible for providing the exit path, and what is missing from its configuration?
- Propose two changes (one at the canvas level and one at the prompt level) that would prevent this loop from exhausting the token budget.
> ➡️ Checkpoint: The Condition Node is binary — it only has two outputs. The exit must be built around those two outputs, not by adding a third. The pattern is a retry counter that increments on each iteration and a Condition Node that compares the counter against a maximum. While the counter is below the maximum, the false branch routes back through the Loop Node for another attempt. Once the counter reaches the maximum, the same Condition Node fires its other branch into a Direct Reply Node with a fallback message. The counter is what makes a binary Condition Node sufficient to provide a controlled exit.

## Check for Understanding
>  In Trace Log B, the agent wrote an assumed policy figure to Flow State after retrieval returned zero results. Why does this specific action make the error significantly more dangerous than if the assumption had remained only in the agent's active reasoning?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/024e308c-563c-432a-9cd0-d841a8d2d1c3

> 💡 Takeaway: 
  Reading an execution trace is the most precise debugging tool available for a visual agent. It shows exactly what the agent thought, what it attempted, and what it received. The three failure modes in these traces are the most common production failures in visual agent builds. Recognising them in a trace log is the first step to preventing them in a canvas.