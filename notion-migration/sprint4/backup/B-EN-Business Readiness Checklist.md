# Business Readiness Checklist

Notion page: https://app.notion.com/p/Business-Readiness-Checklist-37d9418319f3802685fbdf88a52be4dd
Backed up before n8n migration

> 💡 What you will complete by the end of this lesson: You will validate the ability to audit a prototype agent against production constraints, identify architectural failures, and propose targeted fixes. This applies the full course framework to an agent they did not build.

## What this assessment covers
Meridian Consulting's agent has been refined, secured, end-to-end tested, and the platform decision documented. The team is preparing for the final stakeholder review.
Before that review, one more capability needs to be demonstrated. In a consultancy context, Meridian's team will regularly be asked to evaluate AI systems they did not design. The ability to audit an agent you did not build by reading its architecture against known failure modes and proposing targeted fixes, is as important as the ability to build one.
This assessment applies the full course framework to a separate prototype: an e-commerce customer success agent built by a different team with different constraints.

## The agent prototype
Review the following architecture document for a newly prototyped e-commerce customer success agent intended for deployment on a company's main client-facing website serving customers across Germany and the Netherlands.

### Agent profile: E-commerce Customer Success Agent
[TABLE]
  | Component | Current configuration |
  | Purpose | Resolve customer issues regarding orders, returns, and product recommendations |
  | Memory strategy | Passes the entire unfiltered conversation history into the language model prompt on every turn |
  | Retrieval strategy | Standard semantic search against product catalogue and return policy PDFs — no metadata filtering, no source date validation, no conflict resolution logic |
  | Tool configuration | Twenty API tools including check_inventory, issue_refund, send_email, update_shipping_address, apply_discount, cancel_order all loaded simultaneously in the Agent Node's Tools configuration on every query |
  | Security configuration | System prompt includes: "Never share customer personal data with other customers." No input validation layer, output filter, or least-privilege tool credential configuration in place |
  | Testing protocol | Development team manually tested twenty queries over two hours before declaring the agent production-ready |

### Task 1: Write the business readiness audit
Draft a structured audit report of approximately 250-300 words covering all five dimensions below. Each dimension must include a specific architectural fix.
- Memory constraints: Identify why passing the entire unfiltered conversation history on every turn will cause performance degradation at scale. Specify what memory management strategy should replace it and what configuration change in the Agent Node's memory settings would implement that strategy.
- Retrieval constraints: Identify why simple semantic search without metadata filtering or conflict resolution is insufficient for an agent serving customers across two EU jurisdictions with potentially conflicting policy versions. Specify which retrieval enhancement (source date validation, metadata filtering, or conflict resolution instruction) would address the most critical gap.
- Tool constraints: Identify what specific failure mode emerges from loading twenty tools simultaneously in the Agent Node's Tools configuration. Reference the precise reasoning degradation that occurs when the model must select from a large registry of overlapping tool descriptions. Specify how the tool registry should be restructured.
- Security constraints: Identify why a single system prompt instruction is insufficient as the only data privacy control for a client-facing agent handling customer personal data under GDPR. Specify two architectural controls (one at the input layer and one at the output layer) that must be added to make the security posture production-appropriate.
- Testing constraints: Identify why twenty developer-written queries over two hours is inadequate validation for an agent intended to handle thousands of daily customer interactions. Specify what continuous evaluation mechanism must be implemented such as what it tests and how frequently it runs.

### Task 2: Knowledge quiz
### Question 1
>  An e-commerce agent passes its entire unfiltered conversation history into the language model prompt on every turn. After fifteen exchanges, response quality degrades significantly and the agent begins ignoring its system prompt instructions. What is the most accurate explanation?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e6d2648c-f9ae-42cb-9f82-ab2f9a761a9a

### Question 2
>  An agent equipped with twenty API tools frequently invokes the wrong tool for straightforward queries by triggering send_email when the user asked to check their order status. What architectural change most directly resolves this routing failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f22f6255-0a2a-4ba9-aeab-9ea302152cc4

### Question 3
>  A customer support agent serving users across Germany and the Netherlands retrieves two conflicting return policy chunks. One citing a 14-day return window from a 2023 document and one citing a 30-day window from a 2025 update. The agent adds both figures and tells the customer they have 44 days to return their order. Which two changes would most directly prevent this failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bce9c482-6bdb-4fdb-9b47-1fa79b85b2f3
### Question 4
>  A development team declares their agent production-ready after two hours of manual testing across twenty developer-written queries. The agent is deployed and within 48 hours begins failing on customer queries the team never tested. Which testing gap most directly explains this outcome?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e9eaea9b-a5d5-4e4c-b832-589846ad3f38


> 💡 Takeaway: 
  The audit skill developed here (reading an agent's architecture against known failure modes and proposing targeted fixes) is directly applicable to Meridian's consultancy work evaluating AI systems built by their clients. A team that can audit an agent they did not build is significantly more valuable than one that can only build agents they designed themselves. Every failure mode in this prototype appeared in some form during the Meridian build. Recognising them in an unfamiliar architecture is the evidence that the course framework has been internalised.