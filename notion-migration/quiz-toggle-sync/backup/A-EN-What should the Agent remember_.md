# What should the Agent remember?

Notion page: https://app.notion.com/p/What-should-the-Agent-remember-3669418319f380bbb191cd95bb82999c
Backed up before n8n migration

> 💡 What you will work on in this lesson: Walking through a client conversation with us and classifying each piece of information the client shares — deciding what the agent should remember, what it should discard, and what it should ask for consent before storing.

## Setting the scene
Contigo GmbH's development team has moved past the question of whether their support agent needs memory. It does. The question now is harder: given everything a client might say during a conversation, what should the agent actually keep?
This matters in three ways. If the agent stores too much, its conversation history fills with noise and the agent struggles to find what's relevant. If it stores too little, it loses context the client expects it to keep. And in a regulated environment like EU financial services, storing the wrong thing — a financial identifier, a health disclosure — is a compliance risk.
The goal of this walkthrough is to make the call-by-call reasoning visible, so that when you face a new conversation, you already know how to decide.

## The three categories
You'll be sorting every relevant piece of conversational data into one of these three buckets:
- Remember. Safe to store and genuinely useful for future interactions. Storing it improves how the agent serves the client without raising privacy concerns.
- Discard. Temporary, irrelevant for future use, or sensitive enough that storing it in conversational memory creates an unacceptable risk. Some discarded items get routed to a secure system that's built to handle them — for example, a bank's account-update service. Others just get dropped after the current turn.
- Ask for consent. Useful enough to store but personal enough to require explicit permission first. The agent should ask the client before writing this to long-term memory.
![image]((notion-hosted file))

## The conversation
Read through this exchange between a Contigo client and the support agent. We'll come back to it five times.
> Agent: Welcome back to Contigo support. How can I help you today?
  Client: Hi. I need to update the IBAN on my account for direct debits. The new one is DE89 3704 0044 0532 0130 00.
  Agent: I can help with that. For verification, could you confirm your date of birth?
  Client: Sure, it is 14 March 1981. Also, I want to flag that I have been really frustrated with the mobile app lately. It keeps crashing when I try to view my statements.
  Agent: I am sorry to hear that. I will log the app issue. Is there anything else?
  Client: Yes. I recently went through a divorce so my surname has changed. I am now Katarina Brandt, not Katarina Fischer. Please update my profile. Also, I have a mild anxiety condition which sometimes makes long phone calls difficult, so I always prefer written communication if possible.

Five distinct pieces of data appear in this exchange:
1. The new IBAN: DE89 3704 0044 0532 0130 00
1. The date of birth: 14 March 1981
1. The frustration with the mobile app crashing
1. The legal name change to Katarina Brandt
1. The preference for written communication, tied to an anxiety condition
We'll walk through each one and decide what the agent does with it.
---

## Walking through the five data points
### 1. The IBAN
Ask first: is this useful for future interactions, and is it safe to keep in conversational memory?
An IBAN is a sensitive financial identifier. There is no version of "future helpfulness" that justifies leaving it sitting in a transcript log. If someone later gains access to the conversation history — through a leak, a misconfigured permission, an export — they have the account.
The call: Discard.
The IBAN does not get dropped in the sense of "forgotten and ignored." It gets handed straight to the system that actually handles account updates — a secure banking service — and is not retained in the conversational memory. The agent uses it, routes it, and lets go of it.

### 2. The date of birth
The date of birth showed up for one reason only: verification. The agent asked for it, the client provided it, and once the identity check passes the agent has no further use for it.
If the agent stored it anyway, you'd have a personally identifiable detail living in a conversation log with zero future utility. That's pure downside.
The call: Discard.
Used for verification, then dropped. Same pattern as the IBAN — touched once for a specific purpose, never written to memory.

### 3. The frustration with the mobile app
This one feels different from the previous two — it isn't a sensitive identifier. It's an emotional reaction to a technical issue. So is it worth remembering?
Ask what the next conversation looks like if the agent remembers it. "Last time you mentioned the app was crashing — is it still happening?" sounds thoughtful in theory, but the app issue may already be resolved, or it may have been a one-off. The frustration was tied to a specific moment in time. Carrying it forward as a permanent attribute of this client — "this person is unhappy with the app" — is more likely to mislead the next interaction than help it.
The call: Discard.
Acknowledged in the current session, logged where app-issue reports actually live (a product feedback system, not the agent's memory), and dropped from conversational memory at the end of the session.

### 4. The legal name change
A name change is genuinely useful. The agent needs to know what to call the client going forward. So this seems like an obvious "Remember."
But pause. Where does a name change belong? It belongs in the client's official profile — the authoritative record the bank maintains for that client. If the agent writes "the client's name is now Katarina Brandt" only into its own conversational memory, you've created a shadow version of the truth that can drift from the official record. The next agent instance, or the next system that touches this client, won't see the update unless they happen to read the same conversation log.
The call: Discard from conversational memory. Route it to the system that holds the official client profile.
This is the subtle one. "Discard" doesn't mean "this information doesn't matter" — it means "this information doesn't belong in conversational memory specifically." Some things get discarded from memory precisely because they're important enough to belong somewhere more reliable.

### 5. The communication preference
The client said they prefer written communication, and they explained why: a mild anxiety condition.
If the agent remembers the preference, the next conversation can default to written channels without the client having to re-explain. That's a real improvement to service. So far this looks like the only true "Remember" candidate.
But there's a complication. The reason for the preference is a health disclosure. Under the EU General Data Protection Regulation (GDPR — the EU law that governs how personal data is handled), health information is treated as special category data. That means it can't simply be stored on the agent's discretion. The client needs to give explicit permission first.
The call: Ask for consent.
The agent should respond with something like:
> "Thanks for letting me know. Would you like me to note your preference for written communication so future interactions default to it? Because this involves a health-related detail, I'd like your permission before storing it."
If the client says yes, it goes into memory. If not, the agent respects the preference in the current session and lets it go.
---

## The pattern that emerges
Notice what happened across the five items:
[TABLE]
  | Data point | Category | Reason |
  | IBAN | Discard | Sensitive financial identifier — belongs in a secure banking system, not a transcript |
  | Date of birth | Discard | Used once for verification, no future utility |
  | App frustration | Discard | Transient emotional reaction tied to a moment, low future signal |
  | Legal name change | Discard | Belongs in the official client profile, not in memory |
  | Communication preference | Ask for consent | Genuinely useful, but involves health data under GDPR |

Nothing in this conversation qualified as an unconditional "Remember." That's not a quirk of this example — in regulated contexts, it's the norm. Most of what a client says either belongs somewhere more authoritative than the agent's memory, is too sensitive to keep there, or requires permission first.
The heuristic that does the work:
- If a system exists that's built to handle this kind of data (a banking service, a CRM, a verification service) — that's where it goes, not memory.
- If it's transient or tied to a single moment — discard after the current turn.
- If it's genuinely useful for future interactions and not sensitive — Remember.
- If it's useful but personal, especially special category data under GDPR — Ask for consent first.

## Check for Understanding
### Question 1
>  A Contigo agent is instructed to remember everything useful a client mentions. What is the most likely consequence over time?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a331a7cf-98de-4dd1-bf9a-5406671810af

### Question 2
>  A client tells the Contigo agent their legal name has changed. Where should this information be recorded and why?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4dfda95f-10ba-4b02-93d0-e723c69b0b75

> 💡 Takeaway: 
  Deciding what an agent remembers is a design decision, not a default. An agent's memory will hold whatever flows through the conversation unless you decide otherwise — it has no built-in judgment about what is sensitive or useful. That judgment comes from you.
Notice that in this scenario, almost nothing qualified for unconditional "Remember." That's not unusual. In regulated contexts, most conversational data is either routed elsewhere, dropped, or stored only with explicit consent. The default is not to remember.