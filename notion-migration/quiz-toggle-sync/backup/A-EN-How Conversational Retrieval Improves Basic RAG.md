# How Conversational Retrieval Improves Basic RAG

Notion page: https://app.notion.com/p/How-Conversational-Retrieval-Improves-Basic-RAG-3669418319f3803c83e4e02a37a62745
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: Why basic single-shot RAG fails in multi-turn conversations, how explicit query reformulation using conversation history improves retrieval in n8n, and which components you can configure.

## When basic RAG is not enough
Contigo GmbH's development team has a working understanding of the RAG pipeline. Documents are ingested, chunked, embedded, and stored. At query time, the client's question is converted into a vector, the closest matching chunks are retrieved, and the language model generates a grounded response.
For a single isolated question, this works well. But Contigo's support agent is not handling isolated questions. It is handling conversations which are multi-turn exchanges where each question builds on what came before.
Consider this exchange:
Turn 1 Client:  
> "What are the eligibility criteria for the SME Standard loan?"
Turn 2 Client:
> "And what about the repayment conditions for that one?”
In a basic RAG system, Turn 2 is sent to the vector database exactly as written: "And what about the repayment conditions for that one?" The phrase "that one" has no meaning outside the context of Turn 1. The vector database has no knowledge of the previous exchange. It searches for chunks semantically similar to "repayment conditions for that one" and returns either nothing useful or a chunk from the wrong product section. The agent fails not because the information is missing from the knowledge base, but because the retrieval system had no way to know what "that one" referred to.

## How to improve conversational retrieval in n8n
In n8n, build an explicit two-step process: an LLM rewrites the context-dependent query using recent chat history, then the retriever searches Qdrant with the standalone question. This reformulation is not automatic in the vector-store node.

Step 1: Query reformulation - Before the query reaches the vector database, a Basic LLM Chain uses the current question and relevant history from your n8n memory setup. The language model rewrites the query into a standalone question that can be understood without the surrounding conversation.
Turn 2: "And what about the repayment conditions for that one?"  … becomes: "What are the repayment conditions for the Contigo SME Standard loan?"
This reformulated query is what gets sent to the vector database. It now contains the specific terminology that matches the correct chunk in the knowledge base.

Step 2: Retrieval and grounded generation - The reformulated query is embedded and used to retrieve the top matching chunks from Qdrant. Those chunks are passed to the language model along with the original query and the conversation history to generate a grounded, contextually accurate response.
![image]((notion-hosted file))

## What this means for your n8n workflow
Implement query rewriting and retrieval with these n8n components:
[TABLE]
  | Component | What it contributes |
  | n8n chat-memory sub-node | Provides the conversation history used for query reformulation |
  | Qdrant Vector Store | Provides the chunks retrieved after the query is reformulated |
  | Basic LLM Chain and connected Chat Model | Performs both the reformulation step and the final grounded generation |
This is why the n8n chat-memory sub-node you configured in Sprint 1 carries forward into Sprint 2. Without relevant previous messages in the rewriting prompt, the model cannot reliably resolve expressions such as “that one”. The RAG pipeline and the memory configuration depend on each other.

## What you can control in your n8n workflow
Configure these retrieval quality factors through the n8n workflow's nodes:
- Top K — The number of chunks retrieved per query. A higher value gives the language model more context but risks diluting the signal with loosely related chunks. A lower value keeps the context focused but risks missing relevant information. 
- System prompt grounding — The instruction that tells the language model how strictly to use the retrieved chunks. A weak instruction allows the model to supplement with its training data. A strong prohibition prevents it. 
- Chunk quality — Determined by the chunking and preparation decisions made. The Qdrant retriever returns the chunks indexed into the selected collection. If the chunks are poorly prepared, query reformulation cannot compensate for them.
- Embedding model consistency — The same embedding model must be used during ingestion and at query time. A mismatch produces meaningless similarity scores regardless of how well the query is reformulated.

## What is beyond the scope of this workflow
The proposed n8n workflow follows a fixed sequence: rewrite the query, retrieve relevant chunks once, and generate an answer. It does not evaluate whether the retrieved chunks are sufficient, re-query if they are not, or route queries to different knowledge bases based on their content.
These capabilities belong to a more advanced architecture called agentic RAG. Agentic RAG introduces an autonomous reasoning layer into the retrieval process itself, allowing the system to plan, evaluate, and iterate before generating a response. This is beyond the scope of the current n8n exercise but represents the direction the industry is moving for complex, multi-source retrieval tasks.
For this sprint, explicit query reformulation followed by Qdrant retrieval is a sufficient baseline.

## Check for understanding
> 💡 A Contigo client sends the following message in Turn 4 of a conversation: "Does it apply to the same product?" The agent returns an irrelevant chunk. A developer suggests increasing the Top K value to fix the problem. Why is this the wrong diagnosis, and what is the actual cause of the retrieval failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/0ea72e06-96db-45d4-a931-2a43f2148a71


> 💡 Takeaway: 
  Query reformulation improves on basic RAG by reformulating ambiguous follow-up queries into standalone questions before retrieval begins. This makes multi-turn conversations reliable in a way that single-shot RAG cannot be. 
  The reformulation depends entirely on the conversation history provided by the n8n chat-memory sub-node which is why memory configuration and retrieval configuration are not two separate concerns in your n8n workflow. They are one connected system.
