# Memory at scale and observability

Notion page: https://app.notion.com/p/Memory-at-scale-and-observability-3849418319f38024ad21cc1bb917ef91
Backed up before n8n migration

Vela Systems has been running its multi-agent internal tooling for a few weeks. In a single-session test with one agent and one user, everything worked. The memory boundary decisions held. The state handoffs completed cleanly. State recovered correctly when the session was interrupted. But now the Vela team is planning to open the system to their full customer operations group, thirty users across two teams, running queries simultaneously across the three specialist agents. And the question on the table is not "does it work?" They've already established that. The question is: "does it still work at scale, and will we know when it doesn't?"
This lesson addresses both halves of that question. The first half is about how memory and state behave differently when the system is under load from multiple concurrent users. The second half is about observability, specifically, what to log so that when something goes wrong across a multi-agent system, you can trace the failure rather than guess at it.
> 💡 In this lesson, you will learn how memory and state behave under concurrent load, and what to log for observability across a multi-agent system.

## How scale changes the memory picture
When one user runs one query, memory boundaries feel clean and self-evident. The context window belongs to the session. Flow State keys update in a clear sequence. Nothing competes for write access.
When thirty users run queries concurrently, some hitting the Classifier, some mid-handoff to a specialist, some waiting on a second-agent reply, the picture gets more complicated in two specific ways.
[COLUMN_LIST]
  [COLUMN]
    Context windows scale cleanly. Flow State does not.
    Each user session gets its own context window. There is no sharing, no competition, no cross-contamination. The architecture already isolates sessions by design, so concurrency at the context-window level is not a problem.
    Flow State is different. If your agents write to a shared Flow State key (a key that is not scoped per session), then thirty concurrent sessions are writing to the same location. The last write wins. Earlier writes are silently overwritten. This is not a bug you will see in testing; it only surfaces when two sessions are mid-execution at the same moment.
    The fix is the same principle from Sprint 3: write ownership per key, scoped per session. Any key that carries per-user context must be namespaced by session identifier, not written globally. This is a production consequence of the memory boundary decisions you already made.
  [COLUMN]
    Persistent store reads accumulate.
    In a single-session system, a lookup to a persistent store (a Qdrant collection, an Airtable base, an external API) is one call per query. In a thirty-user concurrent system, those calls multiply. The total lookup volume is determined by how many agents perform reads and how many sessions are running simultaneously. 
    Systems that performed one persistent-store call per query in testing may perform thirty in production during peak load. This is a reason to be deliberate about which agent performs them, and whether a result can be carried forward in Flow State rather than re-fetched by each agent in the chain.

## What observability means for a multi-agent system
Observability is logging the right things in the right places so that when the system behaves unexpectedly (an agent returns stale output, a handoff completes but carries the wrong state, a session recovers to the wrong safe state) you can read the logs and identify where the failure happened without having to reproduce the session from scratch.
In a single-agent system, tracing a failure is relatively simple: the agent either completed or it did not, and the output is the evidence. In a multi-agent system, a failure can occur at any of several decision points: at the Classifier, in the handoff contract between agents, in a specialist's state write, or in the recovery logic after an interruption. Log nothing, and all you know is that the output was wrong. Log the right things, and you can read backward from the output to the specific agent and decision that produced it.

## The four positions to log
For a multi-agent Agentflow V2 system, observability coverage comes from logging at four positions. Each position corresponds to a decision the system makes that is invisible without a log entry.
- Position 1: Query received and classified
  - Log: the raw input, the query_type value written to Flow State, and the session identifier. This is the first decision the system makes. If the output of the whole chain is wrong, this log tells you whether the Classifier made the right call before anything else ran.
  - What to log: { session_id, timestamp, raw_query, query_type_written }
- Position 2: State written before handoff
  - Log: every Flow State key the Classifier or coordinator writes before control passes to a specialist. This is the handoff contract which is a set of values the receiving agent will read. If the specialist later returns stale or incorrect output, this log tells you whether the input it received was correct.
  - What to log: { session_id, timestamp, handoff_state_snapshot }
- Position 3: State read on specialist entry
  - Log: the Flow State values the specialist reads at the moment it begins execution. This is the receiving side of the handoff. Comparing Position 2 and Position 3 logs for the same session tells you whether the handoff contract was delivered intact.
  - What to log: { session_id, timestamp, agent_id, state_read_on_entry }
- Position 4: Reply written
  - Log: the output the agent writes along with the session identifier and a completion signal. If a session does not produce a Position 4 log, it did not complete, and you know exactly where to look.
  - What to log: { session_id, timestamp, agent_id, output_summary, status_written }
The four positions together form a trace from the classification decision, through the handoff contract, through the specialist's read, to the final output. Any gap in that trace tells you that the session started but did not finish, and the last log entry before the gap tells you where it stopped.
[TABLE]
  | Position | What it captures | What it tells you when something goes wrong |
  | 1 - Query classified | Raw input, query_type, session ID | Whether the Classifier made the right call |
  | 2 - State written before handoff | Full handoff state snapshot | Whether the specialist received the correct inputs |
  | 3 - State read on entry | State values the specialist actually read | Whether the handoff contract arrived intact |
  | 4 - Reply written | Output, status key, completion signal | Whether the session completed and with what output |

## What not to log
Logging has costs: storage, read time, and privacy exposure. Three categories of content should not appear in logs.
- User-identifiable content. The raw query text often contains names, account references, or internal details. The raw_query field at Position 1 is useful for debugging, but in a production system it should be stored only in a log channel with appropriate access controls, and never in a shared or public log stream.
- Credentials and tokens. Any value that provides access to an external system (API keys, bearer tokens, session cookies) must never appear in a log entry. If a log step writes these values, the log itself becomes a security vulnerability.
- Content that must never persist. The same rules that govern memory ownership (from Sprint 3) apply to logs. If a piece of information was identified as "must not persist" in the memory architecture, it should not appear in a log entry. Logs are persistence.

## Connecting this to your project
The memory and state architecture you defined in Sprint 3 specified what to store, where it lives, and who can access it. Observability is the production complement to that specification: it defines when to write a record of what happened, so that the architecture's behaviour is inspectable after the fact.
Before Sprint 4 integration work begins, the four log positions above should map to your project canvas. For each position, you should be able to answer: which node in my architecture is responsible for writing this log entry, and what specific keys does it log? If a position has no owning node, it is an unmonitored gap in the system.
In your project, the Classifier (or coordinator) owns Positions 1 and 2. Each specialist agent owns Position 3. The final reply node owns Position 4. The specifics depend on your chosen archetype (Router, Coordinator, or Evaluator) but the four positions apply in each case.

## Summary
A multi-agent system that works in testing can fail in production under concurrent load, and the failures are difficult to diagnose without the right log entries. Context windows scale cleanly because they are session-isolated by design. Flow State does not scale cleanly if any key is written globally rather than per session. This is a production consequence of the memory boundary decisions from Sprint 3, not a new problem.
Observability across a multi-agent system requires logging at four positions: query classification, state written before handoff, state read on specialist entry, and reply written. Together these four positions form a trace that spans the entire execution chain. Any gap in the trace identifies the specific agent and handoff where a failure occurred.
In the next lesson, you will identify the specific cases where memory or state causes failure, including how to recognise them in the logs you will now be producing, and design safeguards before integrating your redesigned agent in full.