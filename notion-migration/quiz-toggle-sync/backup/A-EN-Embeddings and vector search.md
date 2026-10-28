# Embeddings and vector search

Notion page: https://app.notion.com/p/Embeddings-and-vector-search-3669418319f380d79dc8ccf39464760e
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: How text is converted into a mathematical form that machines can search semantically and why this is the foundation that makes RAG retrieval work across varied query phrasings.

## The problem keyword search cannot solve
Contigo GmbH's compliance team is testing the retrieval pipeline with a set of representative client queries. Most return the correct chunks. But a pattern of failures emerges that the team cannot resolve by adjusting chunk size or overlap.
A client asks: 
> "What happens if I cannot make my loan repayment this month?" 
The retrieval system returns nothing relevant. The correct information exists in the knowledge base (a section titled "Payment Difficulties and Restructuring Options"). But the client's query shares no exact words with that section heading or its content. The system finds no match because it is looking for words, not meaning.
This is the fundamental limitation of keyword-based search. It matches text based on the presence of specific characters and words. It has no understanding of synonyms, paraphrasing, or the conceptual relationship between different phrasings of the same question. For a support agent serving clients who will phrase their questions in unpredictable ways, keyword search is not a viable foundation.
The solution is embeddings and vector search. These are mechanisms that allow the retrieval system to find content based on meaning rather than exact wording.

## What embeddings are
An embedding is a numerical representation of text. An embedding model converts a piece of text into a vector, which is an array of numbers. Each number in the array represents a dimension in a high-dimensional mathematical space.
For example, the phrase "cannot make my loan repayment" might be converted into a vector like [0.21, -0.87, 0.44, ...] which can be an array of hundreds of numbers. The phrase "payment difficulties" produces a different but mathematically nearby array. The phrase "office furniture catalogue" produces an array that is far away from both. The numbers themselves are not interpretable. What matters is the distance between them.
The key property of embeddings is that text with similar meaning produces vectors that are close together in that space. The phrase "payment difficulties" and the phrase "cannot make my loan repayment" will produce vectors that are mathematically near each other, because the embedding model has learned that these concepts are semantically related. The phrase "office furniture catalogue" will produce a vector that is far away from both.

## How chunking and embeddings relate
Chunking and embeddings work as a sequential pair. 
- Chunking splits a document into smaller pieces first. Each chunk is then passed to an embedding model, which converts it into a numerical vector that represents its semantic meaning. 
- The quality of the embedding depends directly on the quality of the chunk. A chunk that mixes unrelated topics produces a vector that represents nothing precisely, making it harder to retrieve accurately. 
- At query time, the user's question is embedded using the same model, and the resulting vector is compared against all stored chunk vectors to find the closest semantic matches.
![image]((notion-hosted file))
This is what makes semantic search possible. The system looks for vectors that are close to the query vector in the embedding space.
For Contigo's pipeline, the same embedding model is used at two points: 
1. During ingestion to convert document chunks into vectors for storage
1. Query time to convert the client's question into a vector for comparison
![image]((notion-hosted file))

## Where to configure embeddings in n8n
Use an Embeddings sub-node connected to the Qdrant Vector Store Insert Documents operation in the ingestion workflow. In the retrieval workflow, connect an Embeddings sub-node to the Qdrant retrieval operation, retriever, or agent tool. Configure the same embedding model and compatible settings in both places; credentials must be valid for both executions. Changing models may require creating a compatible Qdrant collection and re-indexing documents. Verify the actual vector dimensions rather than assuming every model returns the same size.

## How vector search works
When a client submits a query, the following sequence occurs inside the retrieval step.
1. The query is passed through the embedding model and converted into a vector. 
1. The vector database (Qdrant) calculates the mathematical distance between the query vector and every stored document vector.
1. The chunks whose vectors are closest to the query vector are returned as the retrieval results.
The distance calculation most commonly used is cosine similarity. Cosine similarity measures the angle between two vectors rather than the absolute distance between them. 
A cosine similarity of 1 means the vectors point in exactly the same direction. 
A cosine similarity of 0 means the vectors are orthogonal which means the content has no meaningful relationship to the query. A score of -1 means the vectors point in opposite directions.
This is why the client's question about missed repayments retrieves the payment difficulties section even though no words overlap. The embedding model places both phrasings close together in the vector space, the cosine similarity between their vectors is high, and the correct chunk is returned.
![image]((notion-hosted file))


## Why this matters for retrieval quality
The quality of semantic search depends on three factors that the development team controls.
- Embedding model choice: Different models produce different vector spaces. For Contigo's n8n pipeline, a supported embeddings node such as Google Gemini Embeddings may be used with a configured model and credentials. For a multilingual deployment covering Germany, Austria, and the Netherlands, gemini-embedding-001 is appropriate as it supports multilingual semantic similarity out of the box.
- Chunk quality: An embedding represents the meaning of the text it receives. A chunk that mixes multiple unrelated topics produces a vector that represents none of those topics precisely. The chunking decisions you made earlier directly determine how accurately your vectors represent the knowledge base content. Poor chunks produce imprecise vectors. Imprecise vectors produce poor retrieval. The two problems are the same problem.
- Query phrasing: A very short or ambiguous query produces a less precise vector because there is less semantic information for the embedding model to work with. This is why a conversational retrieval design may first rewrite context-dependent follow-up questions into standalone search queries before querying Qdrant. For queries that arrive already well-formed, no rewriting is needed. For queries that arrive vague or context-dependent, reformulation is what makes retrieval accurate.

## Keyword search versus vector search
[TABLE]
  |  | Keyword search | Vector search |
  | Match mechanism | Exact word or character matching | Mathematical proximity in embedding space |
  | Handles synonyms | Only if explicitly programmed | Automatically — similar meanings cluster together |
  | Handles paraphrasing | Fails unless exact terms are present | Succeeds — meaning is preserved across phrasings |
  | Appropriate for | Structured data with known terminology | Unstructured text with varied natural language |
  | Contigo use case | Unsuitable for client query handling | Foundation of the RAG retrieval pipeline |

## Check for Understanding
> 💡 A Contigo client asks "What are my options if I am struggling financially?" The correct chunk is titled "Payment Difficulties and Restructuring Options." No words overlap between the query and the chunk title. Why does vector search still retrieve the correct chunk?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/27a6b102-b45c-44f4-9a8e-c959426ffea4

> 💡 Takeaway: 
  Embeddings are the translation layer between human language and machine search. By converting text into vectors that cluster by meaning, the retrieval pipeline can find the right content even when the client phrases their question in a way that shares no words with the source document. 
  In n8n, that flexibility depends on configuring compatible embeddings in both the ingestion workflow and the runtime retrieval workflow. One mismatch between those two configuration points is enough to make the entire retrieval pipeline return meaningless results.