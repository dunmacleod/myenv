# Failure points in visual builds

Notion page: https://app.notion.com/p/Failure-points-in-visual-builds-3669418319f3801f9c87f2dbf7041ddb
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Students understand where and why Agentflow v2 architectures fail and how failures in one node cascade through the rest of the graph.

## Setting the Scene
Meridian's agent did not fail during two weeks of internal testing. It began failing two days after being made available to the full consulting team. The canvas looked identical both times. The difference was the variety and volume of real queries hitting every corner of the configuration simultaneously. Visual builders hide complexity. When everything works, that is a productivity gain. When something breaks, the failure often originates not inside a node but between them in the connections that look trivial on the canvas. Understanding where Agentflow v2 architectures are structurally fragile is essential before Sprint 3 adds loops, iteration, and approval checkpoints to Meridian's canvas.

## The Four Failure Points
### Failure point 1: Prompt failures
The system prompt governs the agent's behaviour. When it is ambiguous or incomplete, the agent fills the gap with Gemini's general training data. The response sounds authoritative. It is wrong. No error is raised. The agent simply produces a confident incorrect answer that looks identical to a correct one.

### Failure point 2: Retrieval failures
The Document Store returns semantically adjacent chunks that are close to the query topic but not containing the information needed to answer correctly. The Agent Node treats them as sufficient and generates a response grounded in the wrong material. No node crashed. The failure is semantic, visible only when the response is compared against the actual document content.
Here is a related failure: If the Qdrant vector store is not re-upserted after Meridian's playbooks are updated, the agent retrieves outdated content with full confidence with no indication in the canvas that anything is wrong.

### Failure point 3: Tool and HTTP failures
When the HTTP Node returns an error instead of data, Agent Node B without explicit failure handling either fabricates a status or writes an incorrect value to Flow State. Flow State is a runtime key-value store shared among nodes in a single execution. A fabricated value written to $flow.state.status_response is immediately available to every downstream node that reads from that key and the contamination is structural and immediate.
In Sprint 3, the Loop Node will handle retry logic for failed HTTP calls. The Loop Node's Max Loop Count parameter defines the maximum number of times the loop can execute within a single workflow run, safeguarding against infinite cycles. The default value is 5. Without a configured exit path when the limit is reached, the loop terminates without returning a meaningful response.

### Failure point 4: Memory failures
Context bleed occurs when detail from an earlier account discussion carries into a later one by misattributing action items or applying a constraint from one engagement to another. As conversation length grows, the probability increases and routing decisions degrade.

## How failures cascade
Failures rarely stay contained within the node where they originate. A retrieval failure produces incorrect content that Agent Node A reasons from. That response enters session memory. The next turn injects it as established fact. Each step compounds the error. This is why production failures are more severe than isolated testing reveals. Individual nodes tested against clean inputs do not surface the failure modes that emerge from their interaction.
![image]((notion-hosted file))

## Check for Understanding
>  Meridian's agent retrieves an outdated policy chunk and generates a response from it. The Agent Node stores this in session memory. What happens in the next turn?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/830a1d35-bf13-4019-8248-1fae4817685b


> 💡 Takeaway: 
  Agentflow v2 builds fail at the connections between nodes. A prompt failure produces confident wrong answers. A retrieval failure poisons the context window. A tool failure triggers loops or Flow State contamination. 
  A memory failure compounds all of the above across turns. Recognising these four failure categories is the diagnostic framework for Sprint 3 where loops, iteration, and approval checkpoints add new ways for each one to occur.
