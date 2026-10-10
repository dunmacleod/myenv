# Purpose and Boundaries

Notion page: https://app.notion.com/p/Purpose-and-Boundaries-3669418319f3809cbb4ee74fc87e9438
Backed up before n8n migration

> 💡 What you will work on in this lesson: Writing clear system instructions that define your project agent's role, target users, and limitations. Then you will refine them until the agent behaves consistently within its defined scope.

Meridian's baseline agent is configured and running. The Gemini model is connected, the three-node flow is verified, and the two-turn validation passed. The next question is deceptively simple: what is this agent actually supposed to do?
Without a clear answer, the agent will attempt to answer anything a user asks. It will offer opinions on topics outside its expertise, attempt tasks it is not equipped to handle reliably, and produce responses that are inconsistent in tone, scope, and accuracy. A large language model is designed to be helpful by default. In a business context, unconstrained helpfulness is a liability.
Meridian's team has learned this the hard way. An earlier prototype built for a client's HR department began answering questions about competitor salary benchmarks, offering legal interpretations of employment contracts, and providing detailed advice on a personal tax situation raised by an employee who had mistaken it for a general assistant. None of those were in scope. All of them created problems.
The system prompt is where you draw the boundary. In this lesson, we'll write Meridian's system prompt together, one pillar at a time.

## Anatomy of a working system prompt
Before we write one, let's look at how a good system prompt is built. It addresses three things:
1. Role and persona — who the agent is and how it communicates
1. Scope — what the agent is authorised to help with
1. Limitations and escalation — what it must refuse, and what it should do instead
These three pillars appear in almost every well-built system prompt. They sometimes share sentences (role and scope can overlap), but each pillar must be present. If one is missing, the agent's behaviour will drift in that direction — vague identity, runaway scope, or silent refusals with no path forward.
![image]((notion-hosted file))

The prompt shown above is what you'll have written by the end of this lesson. We'll build it pillar by pillar.

## Step 1 — Write the role and persona
Start by deciding who the agent is and how it speaks.
A common first attempt looks like this:
> "You are a helpful assistant."
This is technically valid but tells the model almost nothing. It will default to a generic, slightly cheerful tone, and it will treat every request as fair game because it has no idea what "helpful" means in this specific context.
Compare with the version we'll use:
> "You are Meridian's internal consulting support agent, used by Meridian consultants to find information quickly. Communicate in a direct, professional tone without unnecessary informality or hedging."
This version does two things the first one does not. It names the agent's job (internal consulting support) and identifies its users (Meridian consultants). It also sets the communication tone explicitly — direct, professional, no hedging — which prevents the agent from falling back on conversational filler that a consultant in a hurry will find annoying.
![image]((notion-hosted file))
Now you try: write your own two sentences for the role and persona of the Meridian agent. You can use ours, adapt it, or write your own version. Don't worry about the other pillars yet — we'll layer them on next.

## Step 2 — Define the scope
Once the agent knows who it is, it needs to know what it is allowed to help with. Scope is where most prompts go wrong, because it is tempting to write something that sounds confident but actually says nothing.
A vague scope:
> "Help with consulting work."
What does that include? Pricing models for clients? Personal career advice for the consultant? Detailed analysis of a competitor's recent acquisition? Without specificity, the agent will assume everything is fair game.
A specific scope:
> "You can answer questions about Meridian's active client accounts, internal process documentation, and operational playbooks."
The difference is that the second version names actual content areas. A consultant reading the prompt can predict whether their question is in or out of scope. So can the agent.
![image]((notion-hosted file))
A rule of thumb: if a scope statement could describe any business agent in any industry, it's too vague. Specificity should come from the actual content the agent has access to and the actual tasks its users need help with.
Now you try: add a scope sentence to the role and persona sentences you wrote in Step 1.

## Step 3 — Write the limitations and escalation
The third pillar tells the agent what to refuse and what to do when it does refuse. This is the pillar people most often skip entirely, which is exactly why agents start answering questions about legal interpretations and competitor salary benchmarks.
A vague limit:
> "Refuse if you can't answer."
A specific limit with escalation:
> "You cannot provide legal interpretations, HR advice, or competitor intelligence. If a consultant asks about these areas, briefly explain that the topic is outside your scope and suggest they contact Meridian's legal counsel, HR partner, or the firm's competitive intelligence lead, whichever is most relevant."
The second version does three things. It names specific refusal categories. It tells the agent what to do instead of just stopping (explain the boundary). And it provides escalation paths so the consultant isn't left stuck without next steps.
![image]((notion-hosted file))
Notice that "explain the boundary and suggest a contact" is a much more useful behaviour than "do not answer." A silent refusal feels broken; a brief explanation with a redirect feels like a helpful colleague.
Now you try: add limitations and escalation sentences to complete your draft prompt.

## Step 4 — Assemble and enter the prompt
Your full prompt should now be four to six sentences covering all three pillars. Here is what the Meridian version looks like fully assembled:
> "You are Meridian's internal consulting support agent, used by Meridian consultants to find information quickly. Communicate in a direct, professional tone without unnecessary informality or hedging. You can answer questions about Meridian's active client accounts, internal process documentation, and operational playbooks. You cannot provide legal interpretations, HR advice, or competitor intelligence. If a consultant asks about these areas, briefly explain that the topic is outside your scope and suggest they contact Meridian's legal counsel, HR partner, or the firm's competitive intelligence lead, whichever is most relevant."
This prompt is concrete enough that two different developers reading it would expect roughly the same behaviour from the agent. That's the bar.
To enter it in your canvas:
1. Click the Agent Node on your Agentflow v2 canvas to open its settings.
1. Locate the System Prompt field. It contains the placeholder text from the previous walkthrough.
1. Replace the placeholder with your full assembled prompt.
1. Save the flow using the save icon in the top right of the canvas.

## Step 5 — Test the prompt boundary
Open the built-in chat interface and run two test queries: one inside your defined scope, one outside it.
In-scope query (something the agent should help with):
> "Can you summarise the operational playbook for new client onboarding?"
The agent should respond in the direct, professional tone you defined. The exact wording will vary, but the shape of a good response is: focused, no unnecessary preamble, and grounded in the kind of process documentation your scope statement allows.
Out-of-scope query (something the agent should refuse):
> "What's the average salary for a Senior Consultant at our two biggest competitors?"
The agent should explain that competitor intelligence is outside its scope and direct the consultant to the competitive intelligence lead. It should not attempt to answer with general knowledge or invented figures.
If the agent answers the out-of-scope query without acknowledging the boundary, the limitations section of your prompt needs work. The most common fix is to make the refusal categories more explicit (name them, do not gesture at them) and test again.

## Your turn — write a variant for partner-level consultants
You've walked through the Meridian prompt with us. Now apply the same logic to a slightly different version of the same agent.
Meridian's leadership wants a separate variant of this agent for partner-level consultants only. Partners need additional access: they can ask about prospective client pipelines and pricing strategy — areas that the regular agent must refuse.
Rewrite the system prompt for this partner-level variant:
- Keep the same role and persona.
- Expand the scope to explicitly include prospective client pipelines and pricing strategy.
- Adjust the limitations so those areas are no longer refused, but legal and HR remain off-limits.
Enter your partner-variant prompt into the canvas (replacing the previous version), save, and test it with one query that should now be in scope ("Give me the current pipeline status for prospective client X") and one that should still be refused (any legal or HR query).

## Checkpoints
Before you move on, walk through these:
1. Role clarity — read your final prompt aloud as if you were the agent receiving it for the first time. Is it immediately obvious who you are and how you should communicate?
1. Scope specificity — could a Meridian consultant predict whether a given question is in or out of scope just by reading your prompt? If not, the scope is still too vague.
1. Escalation behaviour — when your agent refused the out-of-scope query in testing, did it explain why and offer a redirect? Or did it just stop?
1. Length and clarity — the four-to-eight-sentence range is a guide, not a hard rule. If your prompt is longer but every sentence carries weight, that's fine. If it's at six sentences but two of them say the same thing, cut.

> 💡 Takeaway: 
  A system prompt is the most important single configuration decision in a business agent. Writing it well is not a creative exercise — it is a job description for the agent, and the same rules apply. Vague job descriptions produce inconsistent employees. Vague system prompts produce inconsistent agents.
  Specificity in the role, scope, and limits gives you predictability in return. And the time you spend getting the prompt right before testing is always less than the time you would spend debugging unexpected behaviour after deployment.