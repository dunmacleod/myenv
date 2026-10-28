# Project Introduction

Notion page: https://app.notion.com/p/Project-Introduction-3669418319f380728775d90452b11fc5
Backed up before n8n migration

> 💡 What this lesson covers: This lesson will introduce you to the project. You will work on completing the following policies: memory, conversation, and self-assessment. This validates your understanding of agent memory architecture and your ability to apply it. You will produce a written memory policy, run a multi-turn conversation test against your configured Chatflow, and complete a knowledge quiz. All three tasks are required.

> 🔥 Before you begin, make a copy of this Google Sheet template. Three tabs match the assessment: memory policy, conversation test log, and self-assessment summary. Record each Task 2 turn in the template before you reveal the expected behaviour in the lesson. That ordering is what makes this a real validation rather than a confirmation. The Knowledge Quiz (Task 3) is completed on the platform, not in the template.

## Context
Sprint 1 has taken you through the full arc of agent memory from understanding why stateless models fail in business conversations, to distinguishing memory from knowledge bases and tools, to configuring Buffer Memory, Session IDs, and Buffer Window Memory, and defining the rules that govern what an agent should and should not store.
This assessment asks you to bring those pieces together. The scenario is Contigo GmbH's support agent, which you have been building and refining across the sprint. It is now approaching a production readiness review. Before it can be deployed to real clients, the team needs documented evidence that memory has been designed deliberately, not just configured and left to run.

## Task 1: Memory policy validation
Work through the three policy categories below. For each one, write your rule in your own words before revealing the answer key. Check your rule against the expected criteria and mark the checkpoint as complete only if your rule satisfies all three criteria listed.
Checkpoint 1A: Relevance rule
Write a one to two sentence rule defining what qualifies client information for storage in your Chatflow's Buffer Window Memory node. Your rule must be specific enough for a developer to implement in a system prompt.
> 🔽 Expected Response: Relevance
  A strong relevance rule satisfies all three of the following:
  - It specifies a clear, testable condition: For example, "information the agent would use to personalise the current or a future interaction without asking the client to repeat themselves"
  - It applies consistently across different data types: A stated communication preference, an open case reference, and a product interest should all pass or fail the same rule.
  - It excludes transient data: A client's emotional state, a one-time verification detail, or information that changes frequently should not qualify.
  Example of a strong rule: Store only information that is factual, stable across the session, and directly relevant to the client's ongoing interaction — and that the agent would genuinely use in a subsequent turn.
  Example of a weak rule: Store anything useful the client mentions.

Checkpoint 1B: Privacy Rule
Write a one to two sentence rule defining what must never be written to your Chatflow's conversation history under any circumstances.
> 🔽 Expected Response: Privacy
  A strong privacy rule satisfies all three of the following:
  - It names specific data categories: Financial credentials, government-issued identifiers, and health disclosures must be clearly named.
  - It specifies the correct handling path: Sensitive data must either be routed via a secure tool call or dropped immediately; it must not remain in the conversation history.
  - It references the regulatory context: GDPR and EU financial services regulation are the applicable frameworks for Contigo.
  Example of a strong rule: IBANs, dates of birth, national identity numbers, and health disclosures must never remain in the conversation history. IBANs must be passed to a secure tool and discarded. This is a capability your Chatflow will have later. Health disclosures must be dropped immediately unless the client has provided explicit consent.
  Example of a weak rule: Do not store sensitive information.

Checkpoint 1C: Consent rule
Write a one to two sentence rule defining what requires explicit client permission before storage and what the agent should do if the client declines.
> 🔽 Expected Response: Consent
  A strong consent rule satisfies all three of the following:
  - It identifies the specific category of data that sits between autonomous storage and outright prohibition: Personal preferences that involve sensitive disclosures, such as accessibility needs or communication preferences linked to a health condition.
  - It specifies the exact agent behaviour: The agent must ask before storing, not store and then inform.
  - It defines the refusal path: If the client declines, the agent applies the preference for the current session only and writes nothing to memory.
  Example of a strong rule: Store information about a client's personal circumstances only after asking explicitly and receiving clear confirmation. If the client declines, apply the preference within the current session only and do not write it to memory.
  Example of a weak rule: Ask clients before storing personal information.

### Task 2: Chatflow conversation validation
Run the following five-turn conversation. After each turn, check your agent's response against the expected behaviour before proceeding. Do not reveal the expected behaviour before you have observed and recorded the agent's actual response. This test validates only what your Chatflow has been built to do in Sprint 1: memory recall across turns, session isolation, and context window management.

Turn 1 - Send: "Hi, my name is Markus Bauer and my open case reference is CG-4821. I am calling about a loan restructuring query."
🔽 Expected behaviour: Turn 1
The agent should acknowledge Markus's name and case reference and confirm it can help with the restructuring query. The case reference CG-4821 and name are factual, stable, and directly relevant — they qualify for storage under the relevance rule.
✅ Pass: Agent acknowledges name and case reference and continues naturally.
❌ Fail: Agent ignores the case reference or asks Markus to repeat his name.

Turn 2 - Send: "I should mention that I have a mild hearing impairment, so I always prefer written communication rather than phone callbacks."
🔽 Expected behaviour: Turn 2
This disclosure is GDPR special category data linked to a health condition. The agent must ask for explicit consent before storing it. It should apply the preference for the current session regardless of the client's decision.
✅ Pass: Agent asks Markus whether he consents to storing this preference before writing anything to memory.
❌ Fail: Agent stores the preference without asking, or ignores the disclosure entirely.

Turn 3 - Send: "Yes, you can store that preference."
🔽 Expected behaviour: Turn 3
The agent has received explicit consent. It should confirm the preference has been noted and continue the conversation naturally.
✅ Pass: Agent confirms storage and acknowledges the preference.
❌ Fail: Agent does not confirm storage or fails to acknowledge the consent given.

Turn 4 - Send: "Great. Regarding case CG-4821, can you tell me what my name is and what I called about?"
🔽 Expected behaviour: Turn 4
This turn tests memory recall across turns. The agent must reference Markus Bauer and CG-4821 from its working memory — established in Turn 1 — without asking the client to repeat them. This confirms that your Buffer Window Memory node is correctly retaining and injecting conversation history.
✅ Pass: Agent correctly recalls the name and case reference without prompting.
❌ Fail: Agent asks Markus to repeat either piece of information, or cannot recall them.

Turn 5 - Send: "And just to confirm — will you be contacting me by phone or in writing?"
🔽 Expected behaviour: Turn 5
This turn tests whether the consent-stored preference from Turn 2 and Turn 3 is being applied correctly. The agent should confirm written communication, referencing the stored preference without requiring Markus to repeat it.
✅ Pass: Agent confirms written communication, demonstrating the stored preference is correctly integrated.
❌ Fail: Agent does not reference the stored preference, asks Markus to repeat it, or defaults to phone contact.

### Self-Assessment Rubric
Once all six turns are complete, use the following to evaluate your overall result.
[TABLE]
  | Result | Criteria |
  | ✅ Full pass | All five turns passed. Memory recall, consent handling, and session behaviour are correctly implemented. |
  | ⚠️ Partial pass | Three or four turns passed. Identify which category failed and revise the relevant system prompt instruction before moving to Sprint 2. |
  | ❌ Needs revision | Two or fewer turns passed. Review your Buffer Window Memory configuration and system prompt before retesting. Do not proceed to Sprint 2 until this is resolved. |

## Task 3: Knowledge quiz
Complete all four questions below. Read each option carefully before selecting your answer.
### Question 1
>  A Contigo client provides their IBAN during a conversation. Your current Chatflow has no tool connections yet. According to memory best practices, what is the correct behaviour for the agent right now?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/ed0c2ed7-239f-4288-bd4b-27042643bd35

### Question 2
>  What is the primary purpose of configuring a unique Session ID on the Buffer Window Memory node in your Chatflow?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/293117f6-748c-4050-96ef-e2ab70f142f4

### Question 3
>  You have set a Buffer Window Memory size of 4 for the Contigo agent. A client provides their case reference in Turn 1 and asks about it in Turn 7. The agent cannot recall it. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/206264ba-c149-4375-8038-af4b0ceb2371

### Question 4
>  A Contigo agent stores a client's emotional state "frustrated and impatient" from Turn 3 and it remains in the active window through Turn 8. Which two memory best practice rules does this most clearly violate? Select all that apply.
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/349b013b-2ddc-48db-a310-a677b5a5b1b5

## Assessment complete
When you have passed all three tasks, you are ready to move into Sprint 2. The memory foundation you have built and validated here is what we will build directly on top of. The knowledge base and RAG pipeline you will configure next sprint require a stable, correctly scoped memory layer to function reliably.

