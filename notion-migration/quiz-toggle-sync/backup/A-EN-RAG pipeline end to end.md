# RAG pipeline end to end

Notion page: https://app.notion.com/p/RAG-pipeline-end-to-end-3669418319f38049a2bbf927ce4674fc
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: The full sequence of steps that transforms raw business documents into grounded agent responses from initial ingestion through to answer generation.

## From the Problem to the Process
Contigo GmbH’s development team now understands why RAG is necessary. The agent cannot rely only on frozen training data to answer questions about Contigo’s loan products, compliance requirements, or client-specific policies. To give useful answers, it needs access to Contigo’s actual documents.
The next question is how that access works in practice.
A document cannot simply be “given” to the agent as one large file every time a client asks a question. The system needs to prepare the document first, store it in a searchable format, and then retrieve only the most relevant parts when needed.
This is where the RAG pipeline comes in.
The pipeline has two main phases. The first phase happens in the background, before any user asks a question. Documents are loaded, split into smaller chunks, converted into embeddings, and stored. The second phase happens in real time, when a client submits a query. The system searches for the most relevant chunks and passes them to the LLM as context.
To understand this process clearly, the team first needs to understand where those chunks are stored and how they are searched.

### What is a vector database?
A vector database is a database designed to store and search embeddings.
A traditional database usually searches for exact matches: a keyword, an ID, a row value, or a filter condition. A vector database works differently. It searches by semantic similarity, which means it looks for pieces of text that are close in meaning, even if they do not use the exact same words.
For example, a traditional database might only find a document section if the word “refund” appears in it. A vector database can also retrieve sections that mention “money back,” “reimbursement,” or “cancelled payment,” because those meanings are represented by similar embeddings.
This makes vector databases especially useful for RAG. Users rarely ask questions using the exact wording of the source documents. The vector database bridges that gap by finding document chunks that are semantically related to the user’s question.

### What is Qdrant?
In Contigo’s stack, the vector database is Qdrant.
Qdrant is an open-source vector database commonly used in AI and RAG applications. In this pipeline, it stores the embedded document chunks together with the original chunk text and metadata such as the document name, page number, or section.
For Contigo, Qdrant acts as the retrieval layer of the RAG system. It does not write answers and it does not reason like an LLM. Its job is narrower and more mechanical: store the chunks, compare vectors, and return the most relevant pieces of text when a query arrives.
Once Qdrant returns those relevant chunks, the LLM can use them as context to generate a grounded answer.

## Phase 1: Preparing the knowledge base
The background phase converts raw documents into a format the system can search mathematically. It runs once when documents are first ingested, and again whenever the knowledge base is updated. In n8n, Phase 1 is implemented as a document-ingestion workflow. A document loader, text splitter, embedding model, and Qdrant Vector Store operation prepare and index the documents; simply uploading a file does not make it searchable. Understanding what the Document Store is doing under the hood is the reason this lesson comes before you build anything.
- Step 1: Ingestion - The pipeline begins by loading raw content from the source. For Contigo, this might mean importing PDFs of loan product specifications, Word documents containing compliance guidelines, or structured data from internal policy databases. The content is read and extracted into plain text that the system can process.
- Step 2: Chunking - Large documents are broken into smaller segments called chunks. This is necessary for two reasons. First, embedding models and language models have token limits. For example, a 200-page compliance manual cannot be fed into a model as a single input. Second, smaller chunks produce more precise retrieval. So when a client asks about a specific clause, the system should return that clause, not an entire document section surrounding it.
  Chunk size and the overlap between consecutive chunks are design decisions that affect retrieval quality significantly. These choices are covered in detail further on in this sprint.
- Step 3: Embedding - Each chunk is converted into a vector embedding which is a numerical array that captures the semantic meaning of the text. An embedding model performs this conversion. The resulting vectors represent the content mathematically, in a form the system can compare and search.
- Step 4: Storage — The vectors, together with the original text of each chunk and useful metadata such as the source document, page number, section title, or file name, are stored in a vector database. In Contigo’s stack, this database is Qdrant.
  At this point, each chunk has three important parts: the embedding vector, which represents the meaning of the chunk; the original text, which can later be sent back to the language model as context; and the metadata, which helps trace where the information came from. The database is now ready to receive queries.
  When a user asks a question, the question is also converted into a vector. Qdrant then compares this query vector with the stored chunk vectors and returns the chunks that are most semantically similar. These retrieved chunks become the context that the LLM uses to generate a grounded answer.

## Phase 2: Answering a query at runtime
The runtime phase happens every time a client sends a message to the agent. In n8n, this phase can be implemented with a vector-store retriever followed by a question-answering chain, or with a Qdrant retrieval tool connected to an AI Agent. Actual runtime depends on the model, data store, and hosting environment.
- Step 5: Query embedding - The client's question is passed through the same embedding model used during ingestion. This converts the query into a vector using identical mathematical representations, which is essential. If a different embedding model were used at query time, the similarity comparisons would produce meaningless results.
- Step 6: Retrieval - The query vector is compared against all stored document vectors in the database. The system calculates which stored vectors are closest to the query vector mathematically and returns the top matching chunks. This is semantic search where you can find content that means the same thing as the query, even if the exact words are different.
- Step 7: Generation - The retrieved chunks are appended to the client's original query to form an enriched prompt. The language model receives this combined input and generates a response grounded in the retrieved content. The system prompt instructs the model to answer only from the provided context and to acknowledge when the information is not available.

## The full pipeline at a glance
![image]((notion-hosted file))
[TABLE]
  | Stage | Step | What happens | Output |
  | Background | Ingestion | Documents are loaded and extracted | Raw text |
  | Background | Chunking | Text is split into segments | Text chunks |
  | Background | Embedding | Chunks are converted to vectors | Vector embeddings |
  | Background | Storage | Vectors are saved with metadata | Populated vector database |
  | Runtime | Query embedding | Client query is converted to a vector | Query vector |
  | Runtime | Retrieval | Database returns closest matching chunks | Relevant content |
  | Runtime | Generation | LLM responds using retrieved content | Grounded answer |

## Check for Understanding
> 💡 During the runtime phase of a RAG pipeline, why must the query be embedded using the same model that embedded the documents during ingestion?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/02fd45ad-6166-43a8-b050-0ed7e6b75fcd

> 💡 Takeaway: 
  The RAG pipeline is a data engineering system as much as it is an AI system. The quality of the agent's answers depends entirely on how well the pipeline prepares, stores, and retrieves the underlying content. A well-configured generation step cannot compensate for poor chunking, mismatched embedding models, or an incomplete knowledge base before the agent can perform reliably. 
  In n8n, keep document ingestion and runtime retrieval as separate workflow responsibilities. Use compatible embeddings and the same Qdrant collection for both, then inspect retrieved text and source metadata before trusting an answer.
