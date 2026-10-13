# What is a Document Store?

Notion page: https://app.notion.com/p/What-is-a-Document-Store-3669418319f3804497d0d4e89886eea3
Backed up before n8n migration

> 💡 What you will work on in this lesson: Build understanding of what a Document Store is, why it exists, and how it fits into the Agentflow v2 architecture before any configuration begins.

## Where we are
Meridian Consulting's Agentflow v2 can hold a conversation, respond to instructions, and stay within its defined scope. But it only knows what Gemini was trained on. Ask it about Meridian's internal project classification tiers, escalation procedures, or knowledge-sharing protocols and it will either guess or fall back.
The next capability to add is knowledge retrieval by giving the agent access to Meridian's actual internal documents so it can surface accurate, specific information rather than relying on general reasoning.
Before connecting anything to the canvas, it is worth understanding exactly what a Document Store is and why it exists.

## The problem with giving documents directly to a language model
A language model has a context window which is a maximum amount of text it can process in a single request. Sending a full document library into every prompt is not feasible. It is expensive, slow, and hits limits quickly.
The solution is to store documents in a format that can be searched semantically by finding the relevant sections for a specific query rather than loading everything at once. This is what a Document Store does.

## What a Document Store is?
Flowise's Document Stores offer a versatile approach to data management, enabling you to upload, split, and prepare your dataset and upsert it in a single location. This centralised approach simplifies data handling and allows for efficient management of various data formats, making it easier to organise and access your data within the Flowise app.
In practical terms, a Document Store is a self-contained knowledge container inside Flowise. Everything needed to make a document searchable (uploading, chunking, embedding, and indexing) happens inside the store through a single interface. There is no external vector database to configure or manage separately.

## What happens inside a Document Store
When a document is added to a Document Store, it goes through four stages before it becomes searchable:
[TABLE]
  | Stage | What happens | Why it matters |
  | Upload | The raw document file is loaded into Flowise | Makes the content available for processing |
  | Chunking | The document is split into smaller segments | Enables precise retrieval of relevant sections rather than whole documents |
  | Embedding | Each chunk is converted into a numerical vector by an embedding model | Allows semantic similarity search; finding meaning, not just keywords |
  | Upserting | The vectors and their source text are stored in the vector store | Makes the chunks retrievable at query time |
![image]((notion-hosted file))

Chunking explained simply: Imagine Meridian's Operations Handbook as one long document. A consultant asking about escalation procedures does not need the entire handbook, just the relevant section. Chunking divides the document into focused segments so the retrieval system can return precisely what is relevant without loading everything.

## How it connects to Agentflow v2
With an Agent Node, you can add the Document Store directly through the Knowledge configuration in the Agent Node settings. Once connected, the agent can query the store whenever a user's input requires information from those documents.
The Agent Node decides when to query the store based on its reasoning and the description you provide for the knowledge source. A well-written description tells the agent what kind of information the store contains and when it is appropriate to retrieve from it.

## What Meridian's Document Store will contain
For this sprint, three synthetic internal Meridian documents will be loaded into a single Document Store:
[TABLE]
  | Document | Content |
  | Operations Handbook | Project classification policy, knowledge-sharing protocol, escalation procedure |
  | Engagement Standards | Severity rating definitions, client communication guidelines |
  | Regional Playbook | Operational context for Germany, Poland, and Czech Republic engagements |
These documents give the agent enough grounded content to answer real consulting queries without fabricating policy details.

## Check for Understanding
>  A Meridian developer adds a Document Store and uploads three files but does not click Upsert. A consultant then asks the agent about escalation procedures. What does the agent return?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/afaface6-ae58-4f14-bca7-e0d01cc13ad8


> 💡 Takeaway: 
  A Document Store is not a file library. It is a processed, searchable knowledge base. The four stages (upload, chunk, embed, and upsert) transform raw documents into something the agent can query meaningfully. Understanding these stages before configuring them is what makes the difference between a knowledge base that surfaces accurate content and one that returns irrelevant chunks or nothing at all.
