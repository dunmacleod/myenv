# The problem RAG solves

Notion page: https://app.notion.com/p/The-problem-RAG-solves-3669418319f380989a75d90eec3aca5c
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Why standard language models produce unreliable answers without external data, and how Retrieval-Augmented Generation solves that problem for business agents.

## A new kind of failure
Contigo GmbH's support agent has memory, session isolation, and a well-designed retention policy. In multi-turn conversations about things the agent already knows from its training, it performs reliably. But when clients ask about Contigo's specific loan products, current interest rates, or internal compliance procedures, something goes wrong.
The agent answers confidently. The answers are fluent, professionally phrased, and completely wrong.
A client asks about the maximum loan amount available under Contigo's SME financing programme. The agent cites a figure from a general financial services context it encountered during training. The actual Contigo limit is different. The client proceeds on the basis of incorrect information. The compliance team flags the interaction as a serious incident.
This is a knowledge problem and memory alone cannot fix it.

## Why language models hallucinate
A large language model is trained on a vast body of text up to a fixed point in time. After training, its internal knowledge is frozen. It cannot access information that postdates its training cutoff, it has no visibility into private or proprietary business data, and it has no mechanism for knowing what it does not know.
When a question falls outside what the model genuinely knows, it does not stop and say so. It generates the most plausible-sounding continuation of the prompt it can produce. The result is a confident, fluent, and potentially fabricated answer; known as hallucination.
For a consumer chatbot, hallucination is an embarrassment. For a financial services agent operating under EU regulatory oversight, it is a liability. Contigo cannot deploy an agent that invents loan terms, fabricates compliance thresholds, or misquotes product conditions to clients.

## What RAG does
Retrieval-Augmented Generation (RAG) is an architectural pattern that addresses this problem directly. Instead of relying on the model's frozen internal knowledge, RAG gives the agent access to an external, up-to-date knowledge base at query time.
The process works in three steps. When a client submits a query, the system searches an external database to retrieve document chunks that are relevant to that query. Those chunks are appended to the prompt as context. The language model then generates its response based on that retrieved context rather than relying on its general training.
The result is an agent that answers from evidence rather than from approximation. When a Contigo client asks about the SME loan limit, the agent retrieves the current product documentation, reads the actual figure, and responds accurately. When the information is not in the knowledge base, the agent can be instructed to say so explicitly rather than fabricating an answer.
![image]((notion-hosted file))

## What RAG changes for Contigo
The practical implications for Contigo's agent are significant across three dimensions.
- Accuracy: Responses are grounded in the actual content of Contigo's documents rather than in what the language model's training data happened to contain about financial services in general.
- Currency: The knowledge base can be updated as products change, rates are revised, or compliance requirements evolve. The model itself does not need to be retrained.
- Auditability: Because responses are tied to specific retrieved documents, it becomes possible to trace which source material informed a given answer. In a regulated environment, this traceability is a compliance asset.

[TABLE]
  |  | Without RAG | With RAG |
  | Knowledge source | Frozen training data | External, updatable knowledge base |
  | Response to unknown queries | Hallucinated plausible answer | Retrieves evidence or states information is missing |
  | Domain specificity | General financial services context | Contigo's actual products and policies |
  | Auditability | Cannot cite sources | Can reference specific documents retrieved |

## Check for Understanding
>  A Contigo client asks the support agent about the current SME loan limit. The agent responds confidently with an incorrect figure not found in any Contigo document. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b944a2d7-4cec-49ae-80b0-91feca042d98

> 💡 Takeaway:
  Memory gives an agent continuity. RAG gives it accuracy. A business agent that can hold a coherent conversation but cannot access the organisation's actual knowledge is still unreliable at the moment it matters most when a client asks a specific question that only the business can answer correctly.