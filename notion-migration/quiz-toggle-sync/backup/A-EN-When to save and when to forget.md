# When to save and when to forget

Notion page: https://app.notion.com/p/When-to-save-and-when-to-forget-3669418319f380198c7fc6d8f903d2ab
Backed up before n8n migration

> 💡 What you will work on in this lesson: Writing a short memory retention policy as three rules an agent can apply consistently, and testing those rules against new conversational data from a different context — HR onboarding rather than financial-services support.

## Setting the scene
You've now seen how to classify individual pieces of conversational data into Remember, Discard, and Ask for consent. Classification alone is not enough though. What an agent needs is a policy — a small set of rules it can apply consistently to every new conversation, without re-deciding each case from scratch.
In this lesson, you'll write that policy yourself, then test it against new conversational data from a different business context. The shift in context matters: a good policy works across situations, not just the one it was designed around.

## What a memory retention policy covers
A memory retention policy defines three things:
- Relevance. What qualifies information to be stored at all? Not everything a client says is worth keeping. The policy needs a clear condition for distinguishing genuinely useful persistent information from conversational noise.
- Privacy. What data must never be written to memory under any circumstances? This includes sensitive personal identifiers, financial credentials, and health-related disclosures protected under GDPR (the EU law on personal data). Data in this category should either be dropped immediately or routed to a secure system built to handle it.
- Consent. What data is useful enough to store but personal enough to require the client's explicit permission first? The agent must ask before storing this. Storing it without permission is a breach of trust and potentially a legal violation.

## How to work on this lesson
You'll need somewhere to write your answers. Pick one:
>  
  - Recommended. Make a copy of this Google Sheet template — it's structured into three tabs matching Parts A, B, and C, with prompts in the right places and a dropdown for the category column.
- A blank document on your computer.
- A piece of paper.
Whichever you pick, work through Parts A → B → C in order. Don't peek at the answer key at the bottom until you've made your own calls.

## Part A — Draft the rules
Write a short rulebook. For each of the three categories above, write one or two sentences that define the rule clearly enough for someone to implement it.
Your rules should be specific and actionable. Avoid vague language like "store useful things" or "avoid sensitive data." A good rule tells the agent exactly what condition must be met before an action is taken.
Examples of the level of specificity you're aiming for:
- "Store information only if it describes a stable client attribute likely to remain accurate for more than six months and improves how future interactions are personalised."
- "Never store financial credentials, government identifiers, or any data classified as special category under GDPR."
Write one rule for each of: Relevance, Privacy, Consent.

## Part B — Apply your rules
Contigo's HR onboarding agent has extracted five data points from a conversation with a new hire during their first week. Apply your rules from Part A to each item. Classify it as Remember, Discard / Route, or Ask for consent, and write one sentence explaining how your rule justifies the choice.
1. "I prefer to receive all internal communications in English rather than German."
1. "My emergency contact is my partner, Stefan Krause, and his number is +49 151 2345 6789."
1. "I have a chronic back condition and will need an ergonomic workstation setup."
1. "My bank routing details for payroll are: IBAN DE44 2004 1155 0534 3400 00."
1. "I work best in the mornings and would prefer all training sessions before 12:00."

## Part C — Make each decision concrete
Classification alone doesn't tell the agent what to do next. For every item from Part B, do one specific thing based on the category you assigned:
- For Remember items. Write the sentence the agent could use in the next interaction with this person that shows it retained the information usefully. Example: "I have your preference for English communications on file — I'll continue using English going forward."
- For Discard / Route items. Name the kind of system that should hold this data instead (e.g. HR profile system, payroll system, secure verification service), and write one sentence explaining why that system is the right home for it — and the agent's conversational memory is not.
- For Ask for consent items. Write the exact one-or-two-sentence request the agent should make to the person before storing the information.
This is where classification turns into an operational decision. Not just "what category does this fall in?" but "what does the agent literally do or say next?"

## Checkpoints
Use these if you are uncertain or need guidance.
1. Testing your relevance rule. Think about whether the information would still be accurate and useful six months from now. If it's likely to change frequently or become irrelevant quickly, it probably doesn't belong in long-term memory. Ask yourself: would the agent genuinely use this in a future session, or would it just add noise?
1. Testing your privacy rule. Consider what would happen if the memory log were accessed without authorisation. Financial credentials and health data carry the highest risk. Under GDPR, health-related disclosures are special category data — they require an explicit legal basis before they can be stored anywhere, including conversational memory.
1. Testing your consent rule. Think about how a reasonable person would feel if they discovered this had been saved without their knowledge. If the answer is "uncomfortable" or "surprised," it likely belongs in the consent category rather than autonomous storage.
[toggle] Answer key — Part B classifications
  [TABLE]
    | Data point | Category | Justification |
    | Preference for English communications | Remember | Stable, factual, directly useful for personalising future interactions without raising privacy concerns. |
    | Emergency contact details | Discard / Route | A sensitive personal identifier that belongs in a structured HR system, not in conversational memory. |
    | Chronic back condition | Ask for consent | Health disclosures are GDPR special category data — the agent must ask before storing, even though the ergonomic preference it implies is useful. |
    | Payroll IBAN | Discard / Route | A financial credential that must never live in conversational memory. Route to the payroll system. |
    | Preference for morning training | Remember | Stable, useful for scheduling future sessions, and not sensitive enough to require consent. |
[toggle] Answer key — Part C example outputs
  Remember items
  - English communications: "Welcome back — I'll continue our conversations in English as you prefer."
  - Morning training: "I noted you work best in the mornings, so I'll prioritise training slots before 12:00 when we schedule next."
  Discard / Route items
  - Emergency contact → HR profile system. That system keeps emergency-contact data structured, secured, and auditable. Conversational memory has no access controls suited to that data.
  - Payroll IBAN → Payroll system. It's designed to handle financial credentials with proper encryption and access controls. A transcript log is not.
  Ask for consent items
  - Back condition: "Thanks for letting me know. Would you like me to note your need for an ergonomic workstation setup so future onboarding steps account for it? Because this involves a health-related detail, I'd like your permission before storing it."

## Check for Understanding
### Question 1
>  A Contigo client unexpectedly discloses a medical condition mid-conversation during a routine account query. Which response best describes how a well-designed memory retention rulebook should handle this?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/5ce3ea8c-5ee9-4d94-95cf-a07ad9ff35f2

### Question 2
>  Contigo must demonstrate to EU regulators that its agent handles client consent lawfully. Which approach most effectively creates an auditable record of consent decisions?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f2d382d6-5530-4519-8d5f-e08b5bbf5f4a

> 💡 Takeaway: 
  A memory retention policy is a design decision, not a default. It determines what an agent knows, what it is allowed to know, and what it must never touch. Without one, an agent stores whatever flows through the conversation — useful and sensitive alike. In regulated contexts that isn't just sloppy; it's a liability.
Notice that the rules you wrote are deliberately short. That's a feature: a policy that can't fit in a few sentences is unlikely to be applied consistently across thousands of conversations.