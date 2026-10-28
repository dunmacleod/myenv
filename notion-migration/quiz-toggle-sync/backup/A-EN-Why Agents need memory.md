# Why Agents need memory

Notion page: https://app.notion.com/p/Why-Agents-need-memory-3669418319f38037b38cdb07ac299fae
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Why stateless AI models cannot handle real business conversations on their own, and what memory changes about that.

## The starting problem
Contigo GmbH is a Munich-based financial services firm that operates across Germany, Austria, and the Netherlands. They have just deployed an AI support agent to handle client queries about account management, loan applications, and document submissions.
The first week goes badly. Clients submit their account numbers, then get asked to repeat them two messages later. Loan officers receive incomplete summaries because the agent forgot earlier details. One client closes their account after being asked for the same document three times in a single conversation.
The problem is not the language model. The problem is not the prompts. The problem is that the agent has no memory. Without memory, no amount of intelligence makes a business agent reliable.

## Why language models are stateless by default
A large language model (LLM) processes the exact text it receives in a given request, generates a response, and immediately discards everything. It has no built-in record of previous messages. The next time a user sends a message, the model treats it as the very first interaction it has ever had with that person.
This is called being stateless. Stateless means no persistent record of what has happened before. Every request is isolated, processed independently, and forgotten the moment a response is generated. This is the default way of how large language models operate. The architecture is designed for single-turn interactions, not for ongoing business workflows.
The consequence for Contigo is straightforward. Every time a client sends a new message, the agent starts from scratch. It has no access to what was said five seconds ago, let alone five days ago. It cannot track progress, cannot avoid redundant questions, and cannot build on any earlier context.

## What stateless agents look like in practice
Let’s look at an example. A Contigo client wants to update their billing address. The conversation might unfold like this:
> Client: My account number is DE-4892. I need to update my billing address. 
> Agent: Of course, I can help with that. Could you please provide your account number?
The client has already provided it. The agent has already received it. But because the model processed each message in isolation, the account number from the first message is gone by the time the agent formulates its reply. The result is a support experience that feels broken ... because it is.
This pattern repeats across any multi-turn workflow such as loan applications, compliance document requests, and onboarding sequences. Any process that requires more than one exchange is compromised the moment memory is absent.

## What memory changes
Adding a memory component gives the agent access to what has already been said. The conversation history is stored outside the model and injected back into each new prompt, so the model can reason about the full context rather than just the latest message. This is what makes multi-turn business conversations possible.
[TABLE]
  | Turn | Without memory | With memory |
  | Turn 1 | Client provides account number. Agent responds. Data discarded. | Client provides account number. Memory stores it. Agent responds. |
  | Turn 2 | Client asks to update address. Agent asks for account number again. | Client asks to update address. Memory injects account number. Agent continues correctly. |

> 💡 Memory transforms a stateless text generator into an agent that can hold a real conversation, track a workflow, and serve a client without forcing them to repeat themselves.

## Check for understanding
>  A Contigo support agent asks a client for their account number twice in the same conversation. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/82fea941-d06e-44bc-ba25-0fa36dec7063

> 💡 Takeaway: 
  Memory is what separates a stateless text generator from an agent that can hold a real conversation. Without it, no multi-turn business workflow can function reliably. 
