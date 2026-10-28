# Project submission information

Notion page: https://app.notion.com/p/Project-submission-information-3c79418319f3817fa7eefb84971911db
Backed up before n8n migration

## 1. Intro
The module project is Meridian Consulting's internal support agent: an Agentflow v2 running on a self-hosted Flowise instance that answers consultants' questions from the firm's own material, looks up live engagement status, pauses for human approval before it acts on anything consequential, and stays inside the scope Meridian set for it. Across four sprints you built it one capability at a time on a single canvas, Meridian Base Agent, and then spent Sprint 4 making it survive contact with a stakeholder.
The skills you've been practicing across the module:
- Writing a system prompt that fixes role, scope, hard boundaries, and escalation behaviour, then testing it against prompts designed to push past those boundaries
- Grounding an agent's answers in a Document Store so replies come from Meridian's own material rather than from the model's training data
- Routing a query to the right capability with a Condition Agent Node, and giving each path its own specialist Agent Node with a non-overlapping prompt
- Connecting a live data source through an HTTP Node, and designing what the agent does when that source fails
- Adding a Human Input Node approval gate, retry logic, and sub-flow invocation so the flow degrades gracefully instead of guessing
- Validating a canvas end to end across separate sessions, rather than confirming that individual nodes are configured
- Defending a platform choice against named alternatives on the criteria the business actually cares about
The canvas you submit is the refined version of the one you have been building all along, not a rebuild. What is being assessed is whether it behaves the way you say it behaves, and whether you can explain why it is built the way it is.
## 2. Tasks
This is the work the submission draws on, sprint by sprint.
1. Sprint 1: Foundation and behaviour. Stand up the Flowise and Qdrant containers, connect the Gemini and OpenRouter credentials, and build Meridian Base Agent as Start Node → Agent Node → Direct Reply Node. Write the three-pillar system prompt covering role and persona, scope, and limitations and escalation. Test it in a single continuous session across context retention, scope enforcement, and boundary observation.
1. Sprint 2: Knowledge, routing, and tools. Build the meridian-knowledge Document Store from the three Meridian source files and verify retrieval against it. Rewrite the system prompt to four elements, adding capability routing instructions and the defined fallback phrase. Add intent-based routing with a Condition Agent Node and wire the live path: HTTP Node → Agent Node B → Direct Reply B. Run the six-exchange unified session test, including a deliberate HTTP failure.
1. Sprint 3: Orchestration. Add the Human Input Node approval gate, the Custom Function Node retry counter, Loop Node retry, and the Meridian Engagement Briefing iteration sub-flow. Seed Flow State. Work through the canvas verification checklist, then run the five-exchange session test covering approval, rejection, and forced failure.
1. Sprint 4: Refinement, validation, and comparison. Fix the three documented failures: the model configuration behind the latency and cost problem, the mis-routing caused by weak tool and knowledge descriptions, and the fabricated status on a failed lookup. Validate each fix independently. Run the seven-exchange end-to-end test across three separate sessions until all seven pass. Then produce the platform comparison matrix and the justification brief, the business readiness audit, the five-turn demo script, and the written platform defense.
## 3. Project artifacts
Three layers: what you built, the evidence that it works, and how well you can explain the decisions behind it.
### Technical artifacts
By submission day you should have:
- The canvas exported as JSON — the version that passed all seven end-to-end exchanges, loadable in a fresh Flowise instance without missing configuration.
- The system prompt as it stands after the Sprint 4 refinement — the four elements plus the addition covering honest failure acknowledgement.
- The Document Store configuration record — the three source files with their source metadata values, and the embeddings, vector store, and Record Manager settings used at upsert.
- The end-to-end test results table from Sprint 4 — seven rows, with path taken, pass or fail, and notes for each exchange.
- The three refinement notes from Sprint 4 — the model configuration change with its projected monthly cost impact, the rewritten Describe Knowledge and HTTP Node tool descriptions, and the system prompt addition.
- The platform comparison matrix — four platforms against Meridian's five evaluation criteria — and the three-paragraph platform justification brief addressed to Meridian's CTO.
- The business readiness audit report — 250 to 300 words across the five dimensions, each naming a specific architectural fix.
- The five-turn demo script and the written platform defense.
### Analytical reasoning
For your presentation, you should be able to explain:
- Why the routing decision sits in a Condition Agent Node rather than in keyword matching. What changed in the agent's behaviour when you moved it there?
- What the agent does when the live lookup fails, and why that behaviour was designed rather than left to the model to improvise.
- Why the approval gate sits where it sits. What would go wrong if the flow acted first and reported afterwards?
- What the seven end-to-end exchanges proved, and what they did not cover.
- Why Flowise was the right platform for Meridian, which of the three alternatives came closest, and on which criterion it lost.
- What would have to change before this canvas served 43 consultants across three jurisdictions rather than one learner on http://localhost:3000.
### Written summary
A short PDF, one to two pages, that ties the whole project together. Include:
- A one-paragraph problem framing: what Meridian's consultants were doing before the agent existed, and why the firm wanted one.
- A one-paragraph solution overview: the paths a query can take through the canvas, and where it can stop.
- Two or three bullet points naming the most consequential decisions you made across the four sprints, with the alternative you considered and rejected.
- A one-paragraph reflection on what the end-to-end test revealed and one limitation you could not resolve.
The summary is for someone who has not seen your presentation. It should read independently.
## 4. Presentation context
The presentation is mandatory and is the main evaluation method for this project.
Format: Live, in front of the cohort, with Q&A. Your instructor will confirm the exact length of your slot.
The presentation has three components. All three are required. A demonstration without the platform defense, or a defense without the live canvas behind it, is incomplete.
### Component 1: The canvas, live
Run the demo script against the live canvas. The five turns cover knowledge retrieval, cross-turn context retention, live lookup with the approval gate, graceful failure, and a scope boundary — in one continuous session. The Flowise execution trace shows which nodes activated and in what order, and that is what the room will be reading alongside the reply text.
Confirm before you present: both containers running, the HTTP Node pointing at the working endpoint after the failure tests, and the canvas saved with no unsaved changes.
### Component 2: The platform defense
The three arguments, in order: why self-hosted Flowise is the correct production path, why the free model tier needs a production upgrade before real client data moves through it, and why Copilot Studio is the wrong fit for Meridian specifically. Ground each one in Meridian's constraints — a JavaScript and TypeScript team with no Python data engineers, no Microsoft 365 estate, a self-hosting requirement, and clients in three EU jurisdictions.
### Component 3: The readiness account
What the end-to-end test proved, and what the business readiness audit taught you about reading an agent you did not build. Name the prototype-to-production gap honestly: the canvas logic, system prompt, Document Store configuration, and routing architecture carry forward. The infrastructure layer does not.
### Suggested spine
- Open with Meridian's problem in one sentence, and the shape of the canvas in one more.
- Run the demo script live, narrating the trace as it plays — which node is classifying, which specialist is answering, where the flow pauses for approval.
- Name two or three findings from the end-to-end test: one that confirmed a design decision, one that revealed a gap and forced a change.
- Give the platform defense, three arguments in order.
- Close on what is missing before real use, then take questions.
Focus on reasoning and communication. The presentation is not a node-by-node tour. Do not open every node's configuration panel. Do not read the system prompt aloud. Show the thinking behind the architecture — the choices you made, why you made them, and what you would do differently.
## 5. Quality expectations / Evaluation
Your evaluation is based on the presentation, supported by the submitted artifacts. The artifacts let the reviewer verify what you say and run your canvas if needed.
The evaluation covers five dimensions:
[TABLE]
  | Dimension | What the evaluator is listening for |
  | Capability coverage | Does the canvas actually exercise retrieval, intent routing, live lookup, the approval gate, retry, and the scope boundary — or are some of those configured but never demonstrated? |
  | Failure behaviour | When the live source fails, does the agent acknowledge the failure and offer a constructive next step, or does it fabricate a status? Was that behaviour designed, or is it luck? |
  | Evidence quality | Are the seven exchanges recorded with the expected path written before the run and the actual behaviour logged after? Does the record show the canvas was exercised rather than described? |
  | Decision justification | Is each decision grounded in something specific about Meridian — the team's stack, the jurisdictions, the absence of a Microsoft estate — or stated at the level of general principle? |
  | Production judgement | Can the learner name what is missing before 43 consultants use this, and separate what carries forward from what has to be rebuilt? |
There is no single right canvas. The evaluation is not checking whether your routing keywords match someone else's. It is checking whether the agent you built behaves as specified, fails honestly, and can be defended against the alternatives you rejected.
## 6. Preparation checklist
Complete these before submission and the live session. Do not leave any item for Presentation Day itself.
- [ ] All seven end-to-end exchanges passing, with the results table filled in
- [ ] HTTP Node URL restored to the working endpoint after the failure tests
- [ ] Canvas saved, and docker ps showing both the flowise and qdrant containers running
- [ ] docker logs flowise --tail 20 checked — no errors, and no 429 rate-limit messages close to your slot
- [ ] Canvas exported as JSON and confirmed loadable in a fresh Flowise instance
- [ ] Demo script rehearsed once against the live canvas, not read off the page
- [ ] Platform defense reviewed so all three arguments can be given without notes
- [ ] Written summary drafted, one to two pages, and exported as PDF
- [ ] No API keys or credential values anywhere in the export or the documents
## 7. Submission / Delivery instructions
Submission is for access and review. Evaluation happens during the presentation. These are two separate steps.
### What to submit
Bundle into a single submission package (a shared Google Drive folder):
1. The canvas exported as JSON.
1. One document (.md or .pdf) containing the following, in this order:
  1. The system prompt after refinement
  1. The Document Store configuration record
  1. The end-to-end test results table
  1. The three Sprint 4 refinement notes
  1. The platform comparison matrix and the justification brief
  1. The business readiness audit report
  1. The five-turn demo script
  1. The written platform defense
1. The written summary as a PDF.
### Where and when
Submit your work as a link to a Google Drive folder. Put all the artifacts inside it and share the link in the submission lesson.
> ⚠️ Important: Make sure the folder permissions allow anyone with the link to open every file inside it. Test the link in an incognito window before submitting. Do not include your API keys or any credential values in the export or the documents.
### What is not part of grading
- Code Clinic attendance. Not graded.
- The number of artifacts you produce beyond what is listed.
- The visual polish of your slides. Clear thinking matters more than beautiful slides — which does not mean they should be thrown together.
## Final check
Before your presentation, read through your demo script and the platform defense and ask these questions. They are close to the questions the instructor will ask.
- Can you name the path a query takes through the canvas without opening Flowise?
- Does the demo script show the agent acknowledging a failed lookup rather than inventing a status?
- Can you say which of the five comparison criteria mattered most to Meridian, and why?
- Does the readiness audit name a specific architectural fix for each of the five dimensions, not just the problem?
- Can you name one thing the seven-exchange test did not cover?
If any of these produce hesitation, that is useful information. A limitation you can describe precisely is stronger than a claim that everything is solved.
## Summary
The module project moves from a three-node canvas that answers a question to an agent that retrieves from the firm's own material, routes by intent, checks live data, waits for a human before acting, and refuses the questions that are not its job. Sprint 4 was where it stopped being a build and started being something you can put in front of a stakeholder.
What matters now is not adding another node. It is being able to run the canvas cleanly, name what each design decision was for, and say honestly what would have to change before Meridian's consultants could rely on it.