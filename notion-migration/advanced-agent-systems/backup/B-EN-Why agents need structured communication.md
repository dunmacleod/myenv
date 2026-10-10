# Why agents need structured communication

Notion page: https://app.notion.com/p/Why-agents-need-structured-communication-37e9418319f3805bb423fcdd5799e88f
Backed up before n8n migration

> Using OpenRouter instead of Gemini
  Some AI course materials may show Gemini setup directly inside tools like n8n, Flowise, or Cursor. In this program, use your school-provisioned OpenRouter key instead. The workflow logic stays the same, but the model connection may change.
  Before starting, read the setup guide: How-To: Using OpenRouter instead of Gemini 

Sofia is running the first end-to-end test of Cascadia Outfitters' new support automation. A customer message comes in: "My order arrived damaged, I have a two-year warranty — can you replace it?" Sofia's customer-service agent classifies it as a warranty case and hands it off to the Warranty Agent maintained by Cascadia's compliance team. The Warranty Agent fails, silently. Nothing is broken in either agent — they both work fine in isolation. What broke was the message between them: Sofia's agent sent order_id; the Warranty Agent expected orderNumber. Same information, different label. The Warranty Agent looked at what arrived, could not find the fields it needed, and returned an empty response.
This is the first thing Sofia has to solve before Cascadia can put any multi-agent workflow into production: not making the agents smarter, but making them speak to each other reliably. This lesson is about why that reliability requires a communication contract, what a contract is, and what breaks when there isn't one.
## An example: an AI-assisted request
Consider a request Lena forwards to the system: "Analyze this month's returns data and send me a summary." A human immediately understands the steps:
1. Access the returns data.
1. Analyze it.
1. Create a summary.
1. Send the result.
An AI system may also complete these steps, but only if every component knows what information it should receive, what information it should return, and what format should be used. Without clear communication rules, the system becomes unreliable very quickly.
## A simple communication problem
Two agents inside Cascadia's support system:
- The Order Lookup Agent — retrieves details for a given order.
- The Warranty Agent — decides whether a warranty claim is covered and drafts a response.
![image]((notion-hosted file))
The Warranty Agent expects this:
```json
{
  "month": "May",
  "revenue": 125000
}
```
But the Order Lookup Agent sends:
```json
{
  "sales_month": "May",
  "total_sales": 125000
}
```
Both messages contain the same information. Yet the Warranty Agent may fail because it cannot find the fields it expects. The problem is not intelligence. The problem is communication.
![image]((notion-hosted file))
## What is a communication contract
A communication contract is an agreement between components. The contract defines:
[TABLE]
  | Element | Example |
  | Input format | JSON |
  | Required fields | month, revenue |
  | Data types | text, number |
  | Expected behavior | return summary |
  | Error handling | return error message |
> 💡 The contract does not describe how the component works internally.
  It only describes:
  > "If you send me this, I will return that."
  This allows different components to work together without knowing each other's internal implementation.
## Why contracts matter
Imagine a team at Cascadia builds a new version of the Order Lookup Agent. The developers decide to rename the field revenue to total_revenue because they think it is clearer. The change seems small and harmless. However, the Warranty Agent still expects a field called revenue. As soon as the updated agent is deployed, the workflow breaks.
This kind of problem becomes increasingly common as systems grow. Different teams may develop different components, agents may evolve over time, and new tools may be added to existing workflows. Without a shared communication standard, every change introduces the risk that one component will no longer understand another.
Communication contracts reduce this risk by creating a clear agreement between components. As long as an agent follows the contract, its internal implementation can change without affecting the rest of the system. One team can improve an agent, replace a database, or introduce a new tool without requiring every other component to be rewritten.
Contracts also make failures easier to diagnose. When something goes wrong, engineers can quickly check whether the message being sent matches the agreed format. Instead of investigating the entire system, they can focus on the specific point where the contract was violated.
This is the same principle used by APIs. An API does not require you to understand how a service works internally. You only need to know what information to send and what response to expect. Agent communication works in much the same way.
## Check for Understanding
### Question 1
>  What is the primary purpose of a communication contract?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4c73dd47-d335-4c6f-9ff7-2e9172e6608f
### Question 2
>  Sofia's Order Lookup Agent runs successfully and sends its output to the Warranty Agent. The Warranty Agent runs successfully too, but returns an empty response. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4f6c7631-92f2-4a58-a52c-26fa71f75b1d
### Question 3
>  A communication contract between two agents typically defines:
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d89b4fa7-1ad5-41b9-9852-d581c1532823
## Summary
Cascadia's support automation does not fall over because any single agent is wrong. It falls over when two agents disagree about the shape of the message they exchange. Structured communication — a contract between components — is what makes multi-agent systems reliable enough to ship.
In the next lesson, we look at how these contracts show up in practice when Sofia designs the actual handoff between the customer-service agent and the specialist agents downstream.
To specify how components exchange information.