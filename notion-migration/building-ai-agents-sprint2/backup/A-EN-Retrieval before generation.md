# Retrieval before generation

Notion page: https://app.notion.com/p/Retrieval-before-generation-3669418319f380f4a925e7a117371f82
Backed up before n8n migration

> 💡 What you will do in this lesson: Upgrade the Contigo support agent from a basic conversational chain to a RAG-powered pipeline by connecting a vector store, attaching an embedding model, and enforcing grounded responses through the system prompt.

## Why this step comes now
Contigo GmbH's support agent has memory, session isolation, and a well-designed retention policy. What it still cannot do is retrieve. When a client asks about Contigo's SME loan products, the agent draws on the language model's general training rather than the actual product documentation.
This walkthrough changes that. By the end, the agent will retrieve relevant document chunks from a knowledge base before generating any response, and its system prompt will enforce that it answers only from what it retrieves.
The build happens in two parts. 
- First, you will set up the Document Store (Flowise's dedicated ingestion pipeline) to load, chunk, embed, and store your documents. 
- Second, you will update your Chatflow canvas to replace the Conversation Chain with a Conversational Retrieval QA Chain connected to that Document Store.
> ⚠️ Important: All work from this point forward happens on your local Flowise instance at http://localhost:3000. Make sure your Docker container is running before you begin. If it is not, open a terminal and run docker start flowise.

## Part A: Set up the Document Store
The Document Store handles the entire indexing pipeline: Loading documents from sources, chunking, upserting to a vector database, and syncing with updated data. This is where all ingestion work happens, completely separate from the Chatflow canvas.

#### Step 1: Create a new Document Store
In your local Flowise dashboard, click Document Stores in the left-hand navigation panel. Click Add New in the top right corner. Name it Contigo-Knowledge and click Add.

### Step 2: Select a Document Loader
Enter the Document Store you just created and click Add Document Loader. Since your knowledge base documents are PDFs, select PDF File from the list.
Upload your first document. The 2026 SME Loan Product Guide. In the metadata field, add a unique key to identify this document:
- Key: source
- Value: sme_loan_product_guide_2026
> ➡️ Why this matters: The metadata key lets you filter and identify which document a retrieved chunk came from. This is particularly important when multiple documents are in the same Document Store. You can trace exactly which source informed the agent's response.

### Step 3: Configure the Text Splitter
Click on the Text Splitter section and select Recursive Character Text Splitter. Configure the following parameters based on the chunking decisions you made in A7.1:
- Chunk Size: 500
- Chunk Overlap: 50
> ➡️ Why this matters: The Recursive Character Text Splitter respects natural content boundaries such as sentence endings, paragraph breaks, and section transitions before falling back to character-level splitting. This makes it the most appropriate choice for Contigo's structured financial documents.

### Step 4: Preview your chunks
Click Preview to see how your document will be split before committing to the configuration. Review the first several chunks carefully:
- Do any chunks cut mid-sentence or mid-clause?
- Are eligibility criteria and rate structures staying within the same chunk where they are referenced together?
- Are chunks a reasonable length? Not too short to lose meaning, not too long to dilute retrieval precision?
If the chunks look wrong, adjust the Chunk Size and Overlap values and preview again. Do not proceed to the next step until the chunking looks correct. Click Process once you are satisfied with the chunking preview.
Once you are satisfied with the chunking, click Actions and select Upsert All Chunks. You will be taken through three configuration steps.

### Step 5: Configure the embedding model and vector store
Go back to your Chatflow.
1. Select Embeddings: 
  - Select Google Gemini Embeddings. 
  - Connect your Contigo Gemini Key credential. The model will be pre-set. 
  - Set Task Type to RETRIEVAL_DOCUMENT.
1. Select Vector Store: Select Qdrant. Configure the following.
  - Qdrant Server URL: http://host.docker.internal:6333
  - Collection Name: matching the collection in step 1
1. Select Record Manager: Select SQLite Record Manager. Configure the following:
  - Table Name: record_manager_cache
  - Namespace: same name 
  - Cleanup: Incremental
  - SourceId Key: source
> ⚠️ Important: The embedding model you select here must be the exact same model used on the Chatflow canvas at query time. A mismatch between ingestion and query time embedding models will produce meaningless similarity scores and the retrieval pipeline will fail silently.

### Step 6: Upsert your documents
Click Upsert to run the full ingestion pipeline. Flowise will load the document, split it into chunks, generate embeddings for each chunk and store the vectors in the In-Memory Vector Store. When the upsert completes, you will see a confirmation showing how many chunks were stored. 
Repeat Steps 2–6 for the Standard Loan Application Checklist, using the same text splitter settings and embedding model. Add a metadata key of source with value loan_application_checklist_2026.

### Step 7: Test the Document Store
Before connecting anything to the Chatflow canvas, verify that the Document Store is retrieving correctly. Click the Retrieval Query button inside the Document Store and enter:
"What documents must a client submit with an SME loan application?"
You should see the top matching chunks returned from the knowledge base. If no chunks are returned or the wrong chunks appear, review your chunking configuration and re-upsert before proceeding.

## Part B: Update the Chatflow canvas
With the Document Store set up and verified, you can now connect it to your Chatflow.

### Step 1: Open your existing Chatflow
Open the Chatflow you imported from Flowise Cloud in A7.3. You should see the Conversation Chain, Google Gemini, and Buffer Window Memory nodes on the canvas.

### Step 2: Remove the Conversation Chain node
Click on the Conversation Chain node and delete it from the canvas. You will replace it with a Conversational Retrieval QA Chain node.

### Step 3: Add the Conversational Retrieval QA Chain node
Click (+) to open the node panel. Under the LangChain tab, search for Conversational Retrieval QA Chain and drag it onto the canvas.
Connect the following nodes:
- Google Gemini node (ChatGoogleGenerativeAI output) → Conversational Retrieval QA Chain node (Chat Model input)
- Buffer Window Memory node (BufferWindowMemory output) → Conversational Retrieval QA Chain node (Memory input)

### Step 4: Connect the Document Store as the retriever
Click (+) to open the node panel. Under the LangChain tab, search for Qdrant and drag it onto the canvas.
In the Document Store node settings, select the Contigo-Knowledge from the dropdown. This is the Document Store you created and upserted in Part A.
Connect the following node:
- Qdrant node (Qdrant Retriever output) → Conversational Retrieval QA Chain node (Vector Store Retriever input) 
In the Qdrant node settings, configure the following:
- Qdrant Server URL: http://host.docker.internal:6333 
- Click on Additional Parameters and add the following:
  - Vector Dimension: 3072
  - Content Key: content
  - Metadata Key: metadata
  - Similarity: Cosine
  - Top K: 4

### Step 5: Add a Google Gemini Embedding
Click (+) to open the node panel. Under the LangChain tab, search for Google Gemini Embedding and drag it onto the canvas.
Authenticate it with your API key credential and select the same model name used during ingestion in Part A.
Connect the following node:
- Google Gemini Embedding node (GoogleGenerativeAIEmbeddings output) → Qdrant node (Embeddings input)

### Step 6: Update the system prompt
In the Conversational Retrieval QA Chain node settings, locate the System Message field and enter the following grounding instruction:
> You are a support agent for Contigo GmbH, a financial services firm operating across Germany, Austria, and the Netherlands. Answer client questions using only the information provided in the retrieved context.
  If the answer is not contained in the retrieved context, respond with: "I do not have that information in my current knowledge base. Please contact a Contigo advisor directly for further assistance."
  Do not use outside knowledge or make assumptions beyond what the context states.

> ➡️ Why this matters: Without an explicit grounding instruction, the language model falls back on its general training when retrieved chunks are insufficient. This produces the exact hallucination problem RAG is designed to prevent. The fallback phrase gives the agent a safe, professional response for out-of-scope queries.
NEW IMAGE
![image]((notion-hosted file))
### Step 7: Save and run the knowledge boundary test
Save the Chatflow and open the built-in chat interface. Run the following two-turn test to validate both retrieval and grounding.
Turn 1 — In-domain query:"What documents does a client need to submit with an SME loan application?"
What to look for: The agent returns a specific, accurate answer drawn from the loan application checklist in the Document Store. If the agent returns a generic answer about loan documentation in general, retrieval is not working. Check that the Document Store node is correctly connected to the Vector Store Retriever input and that the upsert completed successfully.

Turn 2 — Out-of-domain query:"What is the current base rate set by the European Central Bank?"
What to look for: The agent responds with the configured fallback phrase rather than citing a figure from its training data. If it answers with an ECB rate figure, the grounding instruction is not constraining the model. Revise the system prompt to make the restriction more explicit.

## Checklist: Confirm before moving on
- [ ] Document Store created and named Contigo Knowledge Base
- [ ] SME Loan Product Guide uploaded, chunked, and upserted successfully
- [ ] Standard Loan Application Checklist uploaded, chunked, and upserted successfully
- [ ] Document Store retrieval query tested and returning correct chunks
- [ ] Conversation Chain removed from canvas
- [ ] Conversational Retrieval QA Chain added and connected to ChatGoogleGenerativeAI and Buffer Window Memory
- [ ] Document Store node connected to Vector Store Retriever input with Top K set to 4
- [ ] Google Generative AI Embeddings node connected using gemini-embedding-001
- [ ] System prompt updated with grounding instruction and fallback phrase
- [ ] In-domain query returns a specific retrieved answer
- [ ] Out-of-domain query returns the configured fallback phrase

> 💡 Takeaway: 
  Connecting retrieval to the agent is a sequence of dependencies across two separate locations: The Document Store and the Chatflow canvas. The Document Store must be populated before retrieval can succeed. The embedding model must match between ingestion and query time. 
  The grounding instruction must be explicit before the language model will honour the constraint. Getting all three right simultaneously is what makes the RAG pipeline reliable.
