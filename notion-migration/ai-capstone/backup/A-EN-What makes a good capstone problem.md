# What makes a good capstone problem

Notion page: https://app.notion.com/p/What-makes-a-good-capstone-problem-3e59418319f380c9b37adfa96277b6a5
Backed up before n8n migration

> 💼 Welcome to the Capstone course. Your goal is to apply what you learned and complete a project that helps solve a business problem you either experienced before, thought about, or are currently exploring as part of a new career direction.
> 💼 If you do not have a business problem and require assistance, go to this list and select one of the options.
It's tempting to reach for the most ambitious idea you can think of, the one that would genuinely transform how a business operates. Resist that instinct for a moment. A capstone problem is judged on whether you can design it, build it, verify it, publish the evidence, and evaluate it (especially in the timeline of 4 weeks), and still have something to show at the end. There are many ideas and solutions that can fail the testing, implementation, and even while maintaining the solution. Plenty of modest ones pass it easily and end up more impressive in practice than the ambitious idea would have been half-finished.
Before you consolidate your business problem or explore the project options, let’s look at the three qualities a strong capstone problem should have, so you can test your own idea against them before you commit a sprint to it.
## The three qualities
A strong capstone problem is realistic, measurable, and achievable. Miss any one of the three and the project runs into trouble later, usually right when you have the least time left to fix it.
### Realistic
The problem should map to something an actual business would care about solving, not an exercise invented to showcase a technique. "Real" doesn't mean you need a genuine company on the other end of it, though that's a bonus if you have one. It means the problem, if solved, would save someone time, save someone money, reduce errors, or unblock some part of a workflow that currently depends on a person doing repetitive work.
> ⌛ A quick test: Could you explain, in one sentence, what value this creates through time saved, better service, reduced risk, improved compliance, public benefit, or another measurable operational outcome? "It classifies inbound emails so a support team stops triaging them by hand" passes. "It uses an AI agent to demonstrate multi-step reasoning" doesn't, because nothing about that sentence names a business cost the system removes.
### Measurable
You need to know, before you start building, what "working" looks like. Not "the agent responds intelligently" but something you could actually check against evidence: percentage of tickets routed correctly, minutes saved per task, accuracy on a defined test set. If you can't describe how you'd know the system succeeded, you won't be able to evaluate it in Sprint 3, and you won't be able to defend it in Sprint 4 when someone asks how you know it works.
This is worth getting concrete about early. "Success criteria" isn't a formality you write down and forget. It's the yardstick every design decision gets measured against for the rest of the module.
### Achievable
This is the one ambitious problems most often fail. Due to the time constraints, your build has to include problem scoping, a working core system, publication and optional deployment, safety and governance work, evaluation, and a rehearsed presentation. That's not four weeks of building; it's four weeks of building and everything around the building.
> A good gut check: strip your idea down to its smallest version, the one that solves the actual core of the problem with nothing extra. If that smallest version still feels like a stretch for four weeks, the full version definitely is. Scope down before you scope up. You can always add depth once the core works; you can't manufacture more time once you've spent Sprint 2 realizing the core doesn't fit.
## Where the three qualities interact
These three don't operate independently. A problem that's real but not measurable will feel productive to build and then fall apart the moment you try to evaluate it: you'll have a working system and no evidence it's good. A problem that's measurable but not achievable will have a clean success metric you simply never get the chance to hit. A problem that's achievable but not real will produce a technically impressive system nobody in the room cares about during your presentation.
The strongest capstone problems tend to be narrow, not broad. "An agent that triages inbound support tickets by intent and urgency" is narrower, and stronger, than "an agent that handles customer support." The narrow version has an obvious success metric (percentage triaged correctly), an obvious real-world value (time saved per ticket), and a scope you can actually finish. The broad version sounds more impressive and is much harder to finish, measure, or defend.
## If you don't have your own idea yet
That's fine. You don't need to arrive with a fully-formed business problem. Eight pre-defined fallback projects exist for exactly this situation, each one already built to pass all three tests above: real, measurable, and scoped for four weeks. Picking one isn't a consolation prize. It's a legitimate way to spend your four weeks on the build itself instead of on inventing a problem from nothing.
## Check for Understanding
Read the two problem statements below. For each, name which of the three qualities (real, measurable, achievable within four weeks) it's missing, and rewrite it in two or three sentences so it passes all three.
> Problem A: "Build an AI agent that helps our marketing team be more creative and produce better content."
> Problem B: "Build a system that ingests every document in the company's entire knowledge base across all departments, understands the full organizational structure, and can answer any question any employee might ever ask with perfect accuracy."
### Recommended Results
  Problem A is missing measurable. "More creative" and "better content" aren't things you can score against a test set or count as a percentage. A rewrite has to name a concrete output and a concrete metric:
  For example,
  > "Given a long-form input (webinar, podcast, or blog post), generate a LinkedIn post, an X thread, and a summary email in the brand voice, scored by editor edit-distance from the draft and time saved per piece of content produced."
  Problem B is missing achievable. "Every document," "all departments," and "any question... with perfect accuracy" describe a project with no scope boundary, the kind of system a real company would build over a year with a team, not four weeks solo. A rewrite has to narrow the scope hard:
  For example,
  > “A grounded chat agent over the company's HR policy documents specifically, citing sources on every answer and escalating to a human when it can't answer confidently, evaluated on a 20-question test set.”
  How you get there: 
  For each statement, check it against the three qualities one at a time. Realistic: can you name the person or organisation that benefits and the measurable operational value created? Measurable: is there a number or a pass/fail check you could compute? Achievable: does the smallest possible version of this still fit in four weeks? Whichever question you can't answer cleanly names the gap. Fixing "achievable" almost always means narrowing the scope of who the system serves or what it covers; fixing "measurable" almost always means replacing a vague adjective ("smarter," "better," "more helpful") with a number or a defined test.
## Summary
A strong capstone problem is real, measurable, and achievable, and the strongest ones tend to be narrower than your first instinct suggests. Before you commit to an idea, whether it's your own or one of the eight fallback projects, run it through these three questions: 
1. Who benefits, and what measurable value does solving it create?
1. How would you know it worked?
1. Does the smallest version of it actually fit in the time you have?
If you need a project idea, choose a fallback option before narrowing it into a precise scope and measurable success criteria.