# Router and evaluator patterns

Notion page: https://app.notion.com/p/Router-and-evaluator-patterns-3849418319f380738159dea3826e59e8
Backed up before n8n migration

At the end of the previous lesson, Petra made an observation that stuck with Selin: the confidence signal they added to the coordinator was doing something different from the routing decision. The routing decision said where to send the query. The confidence signal said how much to trust the routing decision before acting on it. Those are two different jobs and in the multi-agent design literature, they have two different names: router and evaluator.
The Vela coordinator is already doing both jobs inside one node. That is fine for their current system. The flow is small, the stakes are modest, and having one node that routes and self-evaluates is not causing problems. But understanding why those jobs are distinct, and what happens when they are handled by separate nodes, is what makes the difference between a multi-agent system that holds up in production and one that requires constant instruction tuning.
> 💡 A router decides where work goes. An evaluator decides whether the work is good enough before it moves on. They look similar from the outside (both sit between agents), but they answer different questions.

## The router pattern
A router is a node (typically a coordinator agent or a condition node) whose sole job is to classify an input and direct it to the right handler. The router does not answer the user's query. It does not assess quality. It reads the input, applies a decision rule, and passes the input to the appropriate downstream node.
The Vela coordinator is a router. It reads a client query, classifies it as commercial, technical, or hybrid, and passes it on. It has no opinion on whether the query is well-formed, whether the specialist will be able to answer it, or whether the answer the specialist gives is good. Routing and answering are separated.

#### What a router needs to work well:
A router is only as good as its classification logic. Three things determine whether a router is reliable:
Clear, mutually exclusive categories. If the categories overlap (if a query could plausibly belong to more than one), the router will route inconsistently, and the inconsistency will be hard to detect because no error is thrown. The specialisation design work from earlier in this sprint was essentially preparation for having a reliable router: narrow, non-overlapping responsibility statements make routing categories that a model can apply consistently.
A defined default for the ambiguous case. Every router will eventually receive a query that does not fit any of its named categories. The Vela coordinator's hybrid category is partly a genuine third category and partly a default for queries that don't clearly belong to either specialist. Naming the default (and deciding what happens to it) is part of router design.
No side effects. A router that modifies the query, adds context, or makes assumptions about what the downstream agent needs is no longer just a router. It has started doing the evaluator's job or the specialist's job. The Vela coordinator's Custom Function node exists partly for this reason: the shaping of context (adding the context_note, stripping routing metadata) was moved out of the coordinator and into a dedicated node so the coordinator stays clean.

#### When a router is the right pattern:
- The input space is divisible into clearly distinct categories
- Different categories require genuinely different handling (different specialists, different tools, different response posture)
- The routing decision itself is low-stakes — a misroute sends the query to the wrong specialist, but the specialist's boundary behaviour catches it and the query can be re-routed

#### When a router alone is not enough:
- The categories are fuzzy and classification confidence varies significantly by input
- A misroute has a high cost — the specialist produces a confident, authoritative-sounding but wrong answer that the client acts on
- The input space includes queries that no defined category covers, and the default path produces poor results
In those cases, the router needs a companion: an evaluator.
![image]((notion-hosted file))

## The evaluator pattern
An evaluator is a node whose job is to assess the quality of another node's output before deciding what to do with it. It does not answer the user's query. It does not route the input. It reads an output that has already been produced and makes a judgment: is this good enough to pass on, or does it need to be revised, re-routed, or flagged?
The confidence signal added to the Vela coordinator in the previous lesson is a primitive evaluator because the coordinator is assessing its own classification confidence before committing to a routing decision. But a proper evaluator is a separate node, downstream from the agent it is evaluating, with its own instructions and its own decision logic.
> ➡️ An example: after the Vela Commercial Agent produces a response, an evaluator node reads the response and checks two things: does the response stay within the Commercial Agent's defined responsibility (pricing, contracts, billing, renewal), and does it contain anything that should not appear in a client-facing response (internal account flags, system error codes, routing metadata)? If both checks pass, the evaluator sends the response to the End node. If either check fails, the evaluator can re-route to the Hybrid Handler, request a revised response, or trigger a graceful degradation response.

#### What an evaluator needs to work well:
- A specific, testable criterion. An evaluator that checks "is this a good response?" will fail; "good" is not testable. An evaluator that checks "does this response contain any of the following patterns: [list] yes or no" can be tested and will produce consistent results.
- A clear action for each verdict. The evaluator's job is not complete when it produces a verdict. It needs to do something with the verdict: pass the output forward, send it back for revision, route to a fallback, or flag for human review. An evaluator without a defined action for its failure case is not a fallback strategy. It is a quality check with no consequence.
- Its own failure mode considered. An evaluator is an LLM node, which means it can give wrong verdicts, time out, or return malformed output. A multi-agent system with an evaluator that itself fails silently is more complex and no more reliable than one without an evaluator. The evaluator needs its own fallback; typically a conservative one: if the evaluator cannot produce a verdict, treat the output as failed and route to the fallback path.

### When an evaluator is the right pattern:
- The quality of a specialist's output is variable and unpredictable
- A wrong output reaching the client has a high cost (reputation, trust, compliance)
- The checks that define quality are specific enough to be encoded in an evaluator prompt
- The added LLM call cost and latency are acceptable given the stakes

### When an evaluator adds complexity without benefit:
- The specialist's output quality is already high and consistent
- The quality criteria are too vague to encode reliably
- The evaluator introduces more failure modes than it prevents
- The added latency is unacceptable for the use case
[TABLE]
  |  | Router | Evaluator |
  | Question it answers | Where should this input go? | Is this output good enough to pass on? |
  | Reads | The input (the user's query) | The output (a specialist's response) |
  | Position in flow | Before the specialist | After the specialist |
  | Failure mode | Misroute; input goes to wrong handler | False pass; bad output cleared; false fail; good output rejected |
  | Cost | One additional LLM call at the start | One additional LLM call at the end |
  | When to add | Categories are distinct; routing error is recoverable | Output quality is variable; quality failure is costly |
![image]((notion-hosted file))

## Router and evaluator together
The two patterns are not mutually exclusive. A mature multi-agent system often has both: a router at the front that directs inputs to the right specialist, and an evaluator at the back that checks the specialist's output before it reaches the client.
The Vela system as built in the previous lesson has a router (the coordinator and condition node) but no evaluator. That is the right starting point — adding an evaluator before the router is working reliably introduces complexity without the data to calibrate it. The typical progression is:
1. Build the router. Test it against a representative sample of inputs. Measure misroute rate.
1. If misroute rate is acceptable, ship without an evaluator — the boundary behaviour in each specialist handles edge cases.
1. If output quality is variable after correct routing, add an evaluator downstream of the specialist with the highest quality variance.
1. If routing confidence is consistently low for a query type, add a confidence evaluator upstream (before the specialist) — which is what the confidence signal introduced in the previous lesson was approximating.

#### The combined pattern in practice:
For the Vela system, if the team decides to add an evaluator, the most valuable placement would be after the Commercial Agent (not the Technical Agent, and not the Hybrid Handler). Here is why: the Commercial Agent's domain (pricing, contracts, billing) contains information that can do real business harm if stated incorrectly to a client. A wrong technical answer about API behaviour is recoverable. The client can test it and find out it was wrong. A wrong pricing answer or a misquoted contract term may be acted on by the client before it is corrected. High consequence of quality failure = evaluator earns its cost.

## Choosing between the patterns
The most common mistake in multi-agent design is adding both patterns reflexively; treating router and evaluator as a standard architecture that all multi-agent systems need. They are not. Each adds an LLM call, latency, and a new failure surface. The question is always whether the benefit in reliability or quality justifies those costs in the specific system.
Use this as a rough decision guide:
- Add a router when the input space has clearly distinct categories that require different handling, and a single agent handling all of them would be overloaded.
- Add an evaluator when output quality is variable after routing, and the cost of a quality failure reaching the client is high enough to justify an additional LLM call and latency.
- Add both when the input space is diverse and routing errors are common and output quality from correctly-routed specialists is still variable. This is the most complex configuration and should only be built once the simpler configurations have been tested and found insufficient.
- Add neither when a single, well-specified agent handles the full input space with acceptable quality. Adding routing and evaluation to a system that doesn't need them produces complexity without benefit. The precise mistake the Vela team avoided by evaluating multi-agent complexity before building.

## Summary
Two patterns, two questions, two positions in the flow. A router sits before the work and answers: where does this input belong? An evaluator sits after the work and answers: is this output good enough to deliver? Both add LLM calls and latency; neither should be added without a specific, testable reason.
The Vela system has a router. The team now has the vocabulary, the decision framework to decide whether it needs an evaluator and where to place one if it does. That decision belongs with the Sprint 2 assessment: designing the full multi-agent architecture for the project agent, with agent roles, responsibilities, coordination approach, and the patterns that hold the system together when inputs are ambiguous or outputs fall short.

## Quiz
### Question 1
>  The Vela team adds a new node after the Technical Agent that reads the Technical Agent's response and checks whether it contains any internal system error codes that should not appear in a client-facing message. If it finds one, it removes the error code and replaces it with a plain-language explanation before passing the response to the End node. What pattern does this node implement?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/ef412d00-227e-4ac7-a23e-de4a5248b89c

### Question 2
>  After two weeks in production, the Vela team reviews their data. The coordinator is misrouting about 4% of queries — mostly edge cases that mention both pricing and technical symptoms in the same message. The Commercial Agent and Technical Agent are both handling their correctly-routed queries well, with high client satisfaction scores. Which addition to the system is most justified by this data?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/db36c3ca-1935-450f-a4d8-72d1d15ad892