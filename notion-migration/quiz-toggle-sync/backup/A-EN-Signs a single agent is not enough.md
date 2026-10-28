# Signs a single agent is not enough

Notion page: https://app.notion.com/p/Signs-a-single-agent-is-not-enough-3849418319f380e6a72eeddffd5b3d27
Backed up before n8n migration

Selin opened the sprint retrospective with a question nobody on the Vela team had expected to ask so soon: "Should we split this into two agents?" The internal operations agent they had built was holding up well. It handled inventory status queries, flagged supplier delays, and summarised fulfilment backlogs without breaking a sweat. So when the client support team asked whether the same architecture could be extended to handle inbound client queries, the answer had seemed obvious: just give it more instructions.
Six weeks later, the extended agent was struggling. It mixed up commercial queries with technical ones, gave billing answers to integration questions, and occasionally surfaced supplier data in responses to clients asking about API rate limits. The agent was not broken. It was overloaded. Vela's team had hit one of the most common and least-obvious ceilings in agent design: the point where a single agent's responsibilities become too broad for it to stay coherent.
This lesson names that ceiling clearly. By the end, you will be able to look at an agent, identify whether its problems are symptoms of overload and whether the right fix is a redesign or a split.
> 💡 In this lesson, you will learn to identify the scenarios where a single agent creates bottlenecks, and to distinguish between problems that need a better single agent and problems that need more than one.

## What a single agent is actually doing
Before diagnosing overload, it helps to be precise about what a single agent is managing at runtime.
Every time a user sends a message, the agent's LLM (the model behind the node) reads three things together: the system prompt (its instructions and persona), the conversation history (what has been said so far), and the user's current message. From those three inputs it decides what to do: call a tool, ask a clarifying question, or generate a response directly.
This means a single agent's coherence depends entirely on its ability to hold a clear, consistent mental model of its purpose across every possible input it might receive. When the range of inputs is narrow and well-defined, that works well. When the range becomes wide, the agent's instructions grow longer, its context window fills faster, and its responses become less consistent at the edges.
The Vela client support agent was asked to handle everything from "What does our enterprise plan include?" to "Why is our webhook returning a 502?" Those two queries require different knowledge, different tone, different tools, and different fallback behaviour. Crammed into one agent with one system prompt, neither gets handled as well as it could be.

## Three signals that a single agent is at its limit
Not every underperforming agent needs to be split. Some agents underperform because their instructions are vague, their tools are misconfigured, or their memory is not set up correctly. Those are fixable without adding a second agent. The signals below point specifically to the kind of overload that a second agent resolves.
Signal 1: The system prompt is trying to be two different experts at once
- When you open an agent's system prompt and find yourself reading two distinct sets of instructions that would never appear in the same job description, the agent is being asked to be two different people. Vela's extended agent had instructions for how to speak to clients about commercial terms and instructions for how to debug API integration issues. These are different roles. The model cannot consistently switch between them based on the input, especially when a single message touches both. For example, a client asks “Is our plan rate-limited? we're getting 429s" is simultaneously a billing question and a technical question.
Signal 2: Response quality varies significantly by query type
- If you run a test set across an agent and notice that it handles one category of query reliably but another category poorly, the issue is usually not the instructions. It is that the agent is being asked to apply different levels of specialisation simultaneously, and the LLM context that makes it good at one category competes with the context that would make it good at the other. Vela's team found their agent scored well on fulfilment queries and poorly on commercial queries in the same session. The fix was separation.
Signal 3: A query arriving at the wrong agent produces a plausible-but-wrong response
- This is the most dangerous signal because it is the hardest to catch in testing. When a single agent handles everything, there is no routing failure. Every query lands with the same agent, so there are no visible handoff errors. But the agent may answer a technical query with commercial language, or vice versa, in a way that sounds confident and coherent but is subtly wrong. This is the failure mode that only shows up when a subject-matter expert reviews the output.
![image]((notion-hosted file))

## The distinction that matters: Overload vs Under-specification
The three signals above all describe overload (an agent that has too many responsibilities to handle any of them at the level of quality the use case requires). This is different from under-specification, where an agent handles a narrow task but handles it poorly because its instructions, tools, or memory are not set up correctly.
[TABLE]
  | Problem type | What it looks like | Fix |
  | Under-specification | Agent handles one query type but gives vague, inconsistent, or off-target responses | Better instructions, clearer tool descriptions, improved system prompt |
  | Overload | Agent handles multiple query types but quality degrades as breadth increases; different query types compete for coherence | Split into specialised agents with non-overlapping responsibilities |
  | Both | Agent handles multiple query types poorly across the board | Underspecification first — confirm the use case is viable as a single agent before splitting |
The order matters. Adding a second agent to fix under-specification is one of the most common over-engineering mistakes in agent design. The right question before splitting is always: if this agent only had to handle one type of query, would it handle it well? If the answer is no, the problem is underspecification and more agents will not help.

## What overload is not
Two situations that look like overload but are not:
- High query volume is not overload. An agent that handles ten queries a day and one that handles ten thousand are architecturally identical. Volume is an infrastructure concern, not an agent design concern. Splitting an agent to handle volume is a common but wrong instinct.
- Long conversations are not inherently overload. An agent that holds a twenty-message conversation about a single complex topic is where the context window is being used as intended. Overload is about the breadth of responsibilities, not the length of interactions.

## Applying this to Vela
The Vela client support agent shows all three signals clearly:
- Its system prompt contained distinct instruction blocks for commercial queries and technical queries — two different experts in one node.
- Test results showed consistent quality on one query type and poor quality on the other within the same session.
- Clients occasionally received technically accurate but contextually wrong responses — a billing answer phrased in the language of a technical support ticket.
The diagnosis is overload, not under-specification. The agent handling fulfilment queries works well with a single agent because its responsibilities are narrow and consistent. The client support use case, by contrast, spans two distinct domains with different knowledge bases, different tones, and different downstream actions. That is the kind of breadth that earns a multi-agent design.
The next step is not just deciding to split, but deciding how to split: what each specialist agent is responsible for, where the boundaries sit, and what the coordination between them looks like.

## Summary
The Vela team's instinct to extend their internal operations agent to cover client support was reasonable. What they discovered is that the breadth of the client support use case (commercial queries, technical queries, and hybrid queries that touch both) made a single agent inconsistent in ways that better instructions could not fix. That is overload, and it is the specific condition that a multi-agent design resolves.
The three signals (a system prompt trying to be two experts, quality that varies by query type, and plausible-but-wrong responses at the boundaries) give you a diagnostic framework you can apply to any agent before deciding whether to split it. The key discipline is checking for underspecification first. A poorly specified agent will still be poorly specified after you add a second one.
The next lessons take this diagnosis forward: how to define specialised agents with clear, non-overlapping responsibilities, and when the additional complexity of a multi-agent system is actually worth its cost.

## Quiz
### Question 1
>  Vela's client support agent is handling both commercial queries (pricing, contracts, renewals) and technical queries (API errors, integration issues, platform bugs). Response quality is consistently strong for commercial queries but degrades noticeably for technical ones within the same session. Which diagnosis fits?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4ee32edd-f701-4e93-bfc9-52f467e92e49
### Question 2
>  Jonas suggests splitting the Vela client support agent into two specialist agents before doing anything else. Selin pushes back, arguing they should check something first. What is the most important thing to check before deciding to split?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/664e574f-16fe-4a2f-b086-b76fae5c9a64
