# Presentation Preparation Guide and Submission

Notion page: https://app.notion.com/p/Presentation-Preparation-Guide-and-Submission-3689418319f380e39163da6eed6b9170
Backed up before n8n migration

> 💡 What you will do in this lesson: Structure your Sprint 4 presentation, prepare your deliverables for submission, understand what you will be evaluated on, and rehearse the key talking points and demonstration sequence for presenting your Contigo Chatflow to the class.

## What the presentation is
The Sprint 4 presentation is the main evaluation moment for Course 2A. It is not a walkthrough of your canvas nodes or a line-by-line explanation of your system prompt. It is a demonstration and defense of a working system — showing that you built something functional, explaining why you made the decisions you made, and communicating what the agent does and why it matters in a business context.

## What you are presenting
You built a Contigo GmbH support agent over four sprints. Here is what that agent does:
- Holds multi-turn conversations with session isolation
- Retrieves accurately from a verified knowledge base
- Invokes tools to perform live lookups and calculations
- Enforces grounding behaviour through a refined system prompt
- Intercepts prompt injection attempts before they reach the model
- Asks for human confirmation before sensitive tool invocations
- Fails gracefully when tools are unavailable
That is a production-relevant system. Present it as one.

## What you will submit
Before presentation day, submit the following through the course submission platform.
[TABLE]
  | Deliverable | What to include |
  | Public chat URL | Your active ngrok URL pointing to your local Flowise Chatflow. Must be reachable when the instructor opens it. |
  | Chatflow export | The .json export of your Chatflow, downloaded from the Flowise dashboard. Captures the canvas structure, node configuration, and tool definitions. |
  | System prompt | The final, refined version of your Tool Agent system prompt as a single .txt or .md file. |
  | Architecture brief | A one-page summary of your agent's architecture and the key decisions behind it. |
The architecture brief should answer four questions in one page or less:
- What does the agent do, and for whom?
- What architectural decisions did you make, and why?
- What failure modes did you build for?
- What is the gap between your prototype and a production deployment?

## Submission instructions
1. Save each file using the naming convention YourName_2A_FinalProject_[type] — for example, YourName_2A_FinalProject_Chatflow.json, YourName_2A_FinalProject_SystemPrompt.md, YourName_2A_FinalProject_Brief.pdf.
1. Upload all files to a single Google Drive folder.
1. Set the folder sharing to Anyone with the link can view.
1. Paste the Google Drive folder link into the submission platform.
1. Include your active ngrok URL as a separate field on the submission form.
> ⚠️ 
  ### Important: Confirm the Google Drive folder is set to Anyone with the link can view before submitting. Locked folders cannot be assessed and will be returned to you.

## Presentation structure
Part 1: Problem and Context (1–2 minutes). Open with the business problem. Cover who Contigo GmbH is and what it does, what problem the support agent is solving, and what the agent needs to be able to do to be useful in that context.
Part 2: Live Demonstration (2–3 minutes). Show the agent working through your public chat URL. Run a conversation sequence that exercises memory, knowledge base retrieval, tool use, fallback behaviour, and security.
Part 3: Chatflow Design (1–2 minutes). Briefly explain the architecture that makes it work. Cover the key components you exercised during the live demonstration.
Part 4: Gaps and Reflection (1 minute). Close with one honest observation about the gap between your prototype and a production deployment.

## What to avoid
- Do not walk through the canvas node by node. Narrate the conversation and explain the architecture, not the interface.
- Do not read from notes. Know your talking points well enough to speak naturally.
- Keep the demonstration moving. Pace matters.
- Do not skip the production gap. It is the clearest signal of architectural maturity.

## What evaluators are looking for
Your presentation is assessed on reasoning and demonstration, not on slide polish or canvas aesthetics. A working agent demonstrated clearly with rough talking points will score higher than a beautiful deck with a broken demo.
Evaluators will assess:
- Does the agent work end-to-end against the prepared scenarios?
- Can you explain why you chose each architectural component without reading from notes?
- Can you defend the trade-offs — why a Tool Agent over a Conversational Retrieval QA Chain, why these tool descriptions, why this memory configuration?
- Can you describe failure modes the agent handles gracefully, and name at least one it does not?
- Can you field architectural questions and respond with reasoning rather than guesswork?

## Preparation checklist
Complete all of these before the presentation day.
Build verification:
- [ ] All twelve turns from the Sprint 3 live validation conversation pass
- [ ] Public chat URL tested and working via ngrok
- [ ] ngrok inspection dashboard confirmed at http://localhost:4040
- [ ] Make Public toggle enabled in Chatflow Configuration → Security tab
- [ ] Chatflow .json exported and saved with the submission naming convention
- [ ] System prompt exported as a .md or .txt file
- [ ] One-page architecture brief drafted and saved as PDF
Content preparation:
- [ ] Opening problem framing rehearsed — can explain Contigo's context in under 90 seconds without notes
- [ ] Twelve demonstration turns rehearsed — know what each one demonstrates before sending it
- [ ] Four architecture points prepared — memory, retrieval, tools, safety
- [ ] Production gap selected and prepared — one honest, specific observation
- [ ] Submission deliverables uploaded to Google Drive folder with link sharing confirmed
On the day:
- [ ] Docker Desktop open and all three containers running before the session starts
- [ ] ngrok tunnel active and public URL confirmed working
- [ ] Public chat URL shared with instructor or class in advance if required
- [ ] Presentation time slot confirmed

## Code Clinic
You have access to a Code Clinic session before presentation day. Use it. Bring your Chatflow, a list of any failures from your Sprint 3 validation, and any architectural questions you have not been able to resolve on your own. The Code Clinic is a support session — the right place to debug a broken tool description, work through a memory edge case, or pressure-test your architecture defense before the live presentation.

> 💡 Takeaway:
The presentation is not a tour of your Flowise canvas. It is a demonstration that you built something that works, and a defense of why you built it the way you did.
  Every architectural decision you made across four sprints was a deliberate choice in response to a specific requirement. Knowing why you made each decision is what separates a confident presentation from a hesitant one.

