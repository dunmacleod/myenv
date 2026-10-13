# How the Conversational Retrieval QA Chain Improves on Basic RAG

Notion page: https://app.notion.com/p/How-the-Conversational-Retrieval-QA-Chain-Improves-on-Basic-RAG-3669418319f3803c83e4e02a37a62745
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Why basic single-shot RAG fails in multi-turn conversations, how the Conversational Retrieval QA Chain addresses this by incorporating conversation history into query reformulation, and what you can and cannot control in your Chatflow build.

## When basic RAG is not enough
Contigo GmbH's development team has a working understanding of the RAG pipeline. Documents are ingested, chunked, embedded, and stored. At query time, the client's question is converted into a vector, the closest matching chunks are retrieved, and the language model generates a grounded response.
For a single isolated question, this works well. But Contigo's support agent is not handling isolated questions. It is handling conversations which are multi-turn exchanges where each question builds on what came before.
Consider this exchange:
Turn 1 Client:  
> "What are the eligibility criteria for the SME Standard loan?"
Turn 2 Client:
> "And what about the repayment conditions for that one?”
In a basic RAG system, Turn 2 is sent to the vector database exactly as written: "And what about the repayment conditions for that one?" The phrase "that one" has no meaning outside the context of Turn 1. The vector database has no knowledge of the previous exchange. It searches for chunks semantically similar to "repayment conditions for that one" and returns either nothing useful or a chunk from the wrong product section. The agent fails not because the information is missing from the knowledge base, but because the retrieval system had no way to know what "that one" referred to.

## What the Conversational Retrieval QA Chain does differently
The Conversational Retrieval QA Chain addresses this problem through a two-step process that happens before retrieval begins.

Step 1: Query reformulation - Before the query reaches the vector database, the chain passes it through the language model along with the recent conversation history from the Buffer Window Memory node. The language model rewrites the query into a standalone question that can be understood without the surrounding conversation.
Turn 2: "And what about the repayment conditions for that one?"  … becomes: "What are the repayment conditions for the Contigo SME Standard loan?"
This reformulated query is what gets sent to the vector database. It now contains the specific terminology that matches the correct chunk in the knowledge base.

Step 2: Retrieval and grounded generation - The reformulated query is embedded and used to retrieve the top matching chunks from the Document Store. Those chunks are passed to the language model along with the original query and the conversation history to generate a grounded, contextually accurate response.
![image]((notion-hosted file))

## What this means for your Chatflow build
The Conversational Retrieval QA Chain combines three components that you will connect in A8.1:
[TABLE]
  | Component | What it contributes |
  | Buffer Window Memory node | Provides the conversation history used for query reformulation |
  | Document Store | Provides the chunks retrieved after the query is reformulated |
  | ChatGoogleGenerativeAI node | Performs both the reformulation step and the final grounded generation |
This is why the Buffer Window Memory node you configured in Sprint 1 carries forward into Sprint 2. Without it, the chain has no conversation history to draw on and query reformulation cannot happen. The RAG pipeline and the memory configuration depend on each other.

## What you can control in your Chatflow
Within the Conversational Retrieval QA Chain, you have direct control over the following retrieval quality levers:
- Top K — The number of chunks retrieved per query. A higher value gives the language model more context but risks diluting the signal with loosely related chunks. A lower value keeps the context focused but risks missing relevant information. 
- System prompt grounding — The instruction that tells the language model how strictly to use the retrieved chunks. A weak instruction allows the model to supplement with its training data. A strong prohibition prevents it. 
- Chunk quality — Determined by the chunking and preparation decisions made. The Conversational Retrieval QA Chain retrieves whatever is in the Document Store. If the chunks are poorly prepared, query reformulation cannot compensate for them.
- Embedding model consistency — The same embedding model must be used during ingestion and at query time. A mismatch produces meaningless similarity scores regardless of how well the query is reformulated.

## What is beyond the scope of this Chatflow
The Conversational Retrieval QA Chain follows a fixed sequence. It reformulates the query, retrieves once, and generates. It does not evaluate whether the retrieved chunks are sufficient, re-query if they are not, or route queries to different knowledge bases based on their content.
These capabilities belong to a more advanced architecture called agentic RAG. Agentic RAG introduces an autonomous reasoning layer into the retrieval process itself, allowing the system to plan, evaluate, and iterate before generating a response. This is beyond the scope of your current Chatflow build but represents the direction the industry is moving for complex, multi-source retrieval tasks.
For Contigo's support agent as built in this course, the Conversational Retrieval QA Chain is the correct and sufficient architecture.

## Check for understanding
>  A Contigo client sends the following message in Turn 4 of a conversation: "Does it apply to the same product?" The agent returns an irrelevant chunk. A developer suggests increasing the Top K value to fix the problem. Why is this the wrong diagnosis, and what is the actual cause of the retrieval failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/0ea72e06-96db-45d4-a931-2a43f2148a71


> 💡 Takeaway: 
  The Conversational Retrieval QA Chain improves on basic RAG by reformulating ambiguous follow-up queries into standalone questions before retrieval begins. This makes multi-turn conversations reliable in a way that single-shot RAG cannot be. 
  The reformulation depends entirely on the conversation history provided by the Buffer Window Memory node which is why memory configuration and retrieval configuration are not two separate concerns in your Chatflow. They are one connected system.
