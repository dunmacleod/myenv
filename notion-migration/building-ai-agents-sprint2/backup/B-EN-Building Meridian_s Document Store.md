# Building Meridian's Document Store

Notion page: https://app.notion.com/p/Building-Meridian-s-Document-Store-3669418319f380ee94bed826ffb28f7d
Backed up before n8n migration

> 💡 What you will work on in this lesson: Students follow a step-by-step process to create a Document Store, upload and configure Meridian's internal documents, and verify the knowledge base is working before connecting it to the agent.

## Setting the scene
Meridian Consulting's agent can now hold a conversation, stay in scope, and remember what was said earlier in a session. What it cannot do is answer questions about Meridian itself.

Ask it how a Severity 2 issue should be escalated, or what language to use for a deliverable in Poland, and it has nothing to draw on. The system prompt defines how the agent behaves. It does not contain Meridian's internal documentation. Without access to that documentation, the agent can only answer in generalities — useful for a chatbot, useless for a consulting firm.

The fix is to give the agent its own searchable copy of Meridian's internal documents. When a question comes in, the agent retrieves the most relevant passages and answers from those, instead of from training data alone. This pattern is called retrieval, and the place where the documents live is a Document Store.

## What you are testing for
A Document Store is only useful if retrieval actually returns the right passages for a given question. Two things have to work at the same time.
The documents are indexed at the right granularity. Chunks need to be small enough that a single chunk is about one thing, and large enough that the thing makes sense on its own. Chunks that are too big mix unrelated policies into one passage; chunks that are too small split a single policy across several passages. Either failure mode degrades retrieval.
The embedding and vector store agree on dimensions. The embedding model produces vectors of a fixed size. The vector store has to be configured to expect that exact size. A mismatch is not a slow failure — the upsert refuses to run.
Both conditions are checked at the end of this lesson with three retrieval test queries. If either is wrong, the queries will return nothing useful, and you will know before the Document Store is connected to the agent.

## What you are building
A Flowise Document Store called meridian-knowledge containing three synthetic Meridian internal documents. When complete, the store will be ready to connect to the Agent Node as a knowledge source.
## The synthetic documents
Download the three text files to your machine before starting. These represent Meridian's internal documentation.
- File 1: meridian_operations.txt
  https://drive.google.com/file/d/1nZKN-io5mgo02WHiynSua_ENvGDGJmr4/view?usp=drive_link
- File 2: meridian_engagement_standards.txt
  https://drive.google.com/file/d/1ChoCGGCj_dxbv3mZCsZTzRZJtOlsgbIB/view?usp=drive_link
- File 3: meridian_regional_playbook.txt
  https://drive.google.com/file/d/1LMePSCwEN7eo5BtSF5vVApecv-DtTqRs/view?usp=drive_link

## Your tasks
### Step 1: Start Flowise and Qdrant
Before opening Flowise, confirm both containers are running. Open a terminal and run:
```powershell
docker ps
```
You should see both containers listed as follows:
```powershell
flowise     running     0.0.0.0:3000->3000/tcp
qdrant      running     0.0.0.0:6333->6333/tcp
```
If either is missing, restart it as follows:
```powershell
docker start flowise
docker start qdrant
```
Then find your machine's Wi-Fi IPv4 address. You will need it to connect Flowise to Qdrant:
```powershell
ipconfig
```
Note the IPv4 Address under Wireless LAN adapter Wi-Fi. It will look like 192.168.x.x.

Confirm Qdrant is reachable by opening this URL in your browser:
```powershell
http://192.168.x.x:6333/dashboard
```
You may see a JSON response with the Qdrant version number or a dashboard. If you do, it is ready.

### Step 2: Open Document Stores in Flowise
Open your Flowise dashboard at http://localhost:3000. In the left-hand navigation panel, click Document Stores.
Click + Add Document Store. Name it meridian-knowledge and click Save.

### Step 3: Add the first document loader
Click into the meridian-knowledge store. Click + Add Document Loader.
From the loader options, select Text File. Upload meridian_operations.txt.
In the metadata field, add the following:
- Key: source
- Value: operations_handbook

### Step 4: Configure the Text Splitter
Select Recursive Character Text Splitter and configure:
[TABLE]
  | Setting | Value |
  | Chunk Size | 1000 |
  | Chunk Overlap | 100 |
Click Preview to confirm the document is being split into meaningful sections. Each policy section should appear as a distinct chunk. If a single section is being split across chunks, increase the chunk size. If two sections are being merged into one chunk, decrease it. Adjust in steps of 200 until the split looks clean, then click Save.

### Step 5: Add the remaining two documents
Repeat Steps 3 and 4 for the remaining two files using the same Text Splitter settings:
File 2:
- Upload meridian_engagement_standards.txt
- Metadata key: source, value: engagement_standards
File 3:
- Upload meridian_regional_playbook.txt
- Metadata key: source, value: regional_playbook
Save each document loader before continuing.

### Step 6: Configure the upsert settings
Inside the meridian-knowledge Document Store, click Upsert Configuration. You will see three cards: Embeddings, Vector Store, and Record Manager. Configure each one in order.

### Embeddings - Click the Embeddings card and select Google Gemini Embedding.
[TABLE]
  | Field | Value |
  | Connect Credential | Select your saved Gemini credential |
  | Model Name | gemini-embedding-001 |
  | Task Type | RETRIEVAL_DOCUMENT |
Click Save.
> ⚠️ Important: The Model Name may be different than what is here. That is ok. As long as it is the model you have been using already. 

### Vector Store - Qdrant
Click the Vector Store card and select Qdrant.
[TABLE]
  | Field | Value |
  | Qdrant Server URL | http://192.168.x.x:6333 — use your actual Wi-Fi IPv4 address |
  | Collection Name | meridian-knowledge |
  | Vector Dimension | 3072 |
  | Metric | Cosine |
  | Top K | 2 |
  | File Upload | Off |
  | Payload Indexes | Leave empty |
Click Save.

> ⚠️ Why your Wi-Fi IP and not localhost: Flowise and Qdrant are running as separate Docker containers. When Flowise tries to connect to localhost, it looks inside its own container where there is no Qdrant. Your machine's Wi-Fi IPv4 address is reachable from both containers via the port mappings configured when each container was started.
> ⚠️ Why 3072 dimensions: The gemini-embedding-001 model produces vectors of 3072 dimensions. The Vector Dimension in Qdrant must match the embedding model exactly. A mismatch causes a dimension error and the upsert will fail. Again, it is ok if the model is different.

### Record Manager - SQLite
Click the Record Manager card and select SQLite Record Manager.
[TABLE]
  | Field | Value |
  | Table Name | record_manager_cache |
  | Namespace | meridian-knowledge |
  | Cleanup | Incremental |
  | SourceId Key | source |
Click Save.
> ⚠️ Why SQLite: SQLite requires no external database or additional Docker container. It stores chunk hash records inside a file within the existing Flowise Docker container making it the simplest choice for a self-hosted development setup.
> ⚠️ Why Incremental cleanup: On re-upsert, only new or changed chunks are processed. Unchanged chunks are skipped. This prevents duplicate vectors accumulating in Qdrant every time you update a document and re-run the upsert.
![image]((notion-hosted file))
### Step 7: Upsert the documents
Once all three cards are saved, click Upsert. Flowise will process each document through the full pipeline automatically:
1. Split into chunks using the Text Splitter settings
1. Embed each chunk using Gemini gemini-embedding-001
1. Store vectors in Qdrant under the meridian-knowledge collection
1. Record each chunk's hash in the SQLite database
When complete, the Document Store status updates and shows the number of chunks stored.
> ⚠️ If you receive a dimension mismatch error: This means Qdrant created the collection with the wrong dimensions during a previous failed attempt. To fix it:

### Step 8: Verify the knowledge base
Click Retrieval Query and run the following three test queries one at a time:
[TABLE]
  | Query | Expected source |
  | What are the project classification tiers at Meridian? | meridian_operations.txt — Project Classification section |
  | How quickly must a severity level 2 issue be escalated? | meridian_engagement_standards.txt — Severity Ratings section |
  | What are Meridian's language guidelines for Poland? | meridian_regional_playbook.txt — Poland section |
For each query, confirm:
- At least one returned chunk contains content relevant to the question
- The metadata shows the correct source file
> ⚠️ Note on results: With short synthetic documents, each file produces approximately two to three chunks. Top K is set to 2 so each query returns the two most semantically similar chunks. If results seem off, check that the upsert completed without errors and that the correct embedding model is selected.

### Checklist: Confirm before moving on
- [ ] Both flowise and qdrant containers confirmed running with docker ps
- [ ] Wi-Fi IPv4 address confirmed with ipconfig
- [ ] Qdrant reachable at http://192.168.x.x:6333
- [ ] meridian-knowledge Document Store created in Flowise
- [ ] All three documents uploaded with correct metadata keys
- [ ] Recursive Character Text Splitter configured — chunk size 1000, overlap 100
- [ ] Embeddings configured — gemini-embedding-001, Task Type RETRIEVAL_DOCUMENT, Gemini credential connected
- [ ] Qdrant configured — Wi-Fi IP, collection meridian-knowledge, dimension 3072, Top K 2
- [ ] SQLite Record Manager configured — table record_manager_cache, namespace meridian-knowledge, cleanup Incremental
- [ ] Upsert completed successfully — chunk count displayed
- [ ] All three retrieval test queries return relevant chunks

> 💡 Takeaway: 
  A Document Store is only as useful as the care taken configuring it. Three decisions made during setup (chunk size, embedding model, and vector dimension) directly determine whether retrieval works correctly when the agent needs it. 
  Verifying the knowledge base with test queries before connecting it to the canvas is what confirms the pipeline is working end to end, not just technically connected.