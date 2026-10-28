# Preparing documents for retrieval

Notion page: https://app.notion.com/p/Preparing-documents-for-retrieval-3669418319f380348ac9ee553d6abe49
Backed up before n8n migration

> 💡 What you will work on in this lesson: Designing a document preparation strategy for two structurally different file types by identifying why generic processing fails for each and proposing approaches that preserve the content's meaning and usability for retrieval.

## The Scenario
Contigo GmbH's knowledge base curation is complete. The team has selected the documents that belong in the retrieval pipeline and excluded those that do not. The next step is preparing those documents for ingestion and this is where a common and costly mistake gets made.
A junior developer on the team proposes a simple solution:
- Run every selected document through the same text splitter, cut everything into 500-word blocks, embed the blocks, and load them into Qdrant. It is fast, consistent, and requires no document-specific configuration.
The compliance lead pushes back immediately. She has seen this approach fail before. The last time a team applied generic chunking to a legal compliance document, the retrieval system split a critical clause across two chunks
- Chunk 1 - The condition appeared in one chunk
- Chunk 2 - The consequence
The agent retrieved only the first chunk, gave clients an incomplete interpretation of the policy, and the error went undetected for three weeks. The team needs a preparation strategy that accounts for the structure of each document type, not just its file format.

## The two Documents
Contigo's team is preparing two of the selected files for ingestion.
1. Document 1: The 2026 SME Loan Product Guide (PDF) - A 5-page document structured with clear section headings, subsections for each product, and detailed eligibility criteria, interest rate tables, and application requirements. The content is dense and interconnected; eligibility criteria in one section reference rate structures in another, and the application requirements vary depending on the loan type described earlier in the document.
1. Document 2: The Standard Loan Application Checklist (PDF) - A single-page document listing twelve items clients must submit with a loan application. Each item is a short, standalone entry; a bullet point with a label and a one-sentence description. There are no cross-references, no nested clauses, and no dependency between items.
![image]((notion-hosted file))
## Your Tasks

> 🔥 Template: Contigo Document Preparation worksheet — make a copy (File → Make a copy) and use it to capture your diagnosis of Document 1, your approach for Document 2, and your handling of the comparison table.

#### Task A: Diagnose the generic chunking failure for Document 1
The junior developer's proposed approach applies a fixed 500-word text splitter to the SME Loan Product Guide without regard for its section structure. Identify two specific ways this approach would damage the document's usefulness for retrieval. Consider what happens when a chunk boundary falls mid-clause, and what happens when a retrieved chunk references content from a section the chunk does not include.
Then propose a better preparation approach for this document. Your proposal should specify what structural feature of the document you would use as the chunking boundary, and explain why that boundary preserves the content's meaning better than a fixed word count.

#### Task B: Determine the correct approach for Document 2
The loan application checklist has a fundamentally different structure from the product guide. Applying the same chunking logic to both documents is not appropriate, but the reason is not immediately obvious.
Describe how you would prepare the checklist for ingestion. Consider whether each checklist item should be its own chunk, whether the items should be grouped, and what metadata you would attach to each chunk to support accurate retrieval. Explain how a client query like "What do I need to submit with my loan application?" should ideally interact with the chunks you have created.

#### Task C: Identify the structural problem with tabular data
Contigo's team is also considering whether to include a structured product comparison table — a section of the product guide that presents loan limits, rates, and eligibility thresholds for five different products in a side-by-side table format.
When a standard text splitter processes a table, it typically reads across rows and concatenates the text sequentially, losing the column relationships that give the data its meaning. Explain what the agent would retrieve if this table were processed with a generic text splitter, and propose an alternative approach for handling tabular content in a RAG pipeline.

[toggle] Think about the following … 
  - Checkpoint 1: Thinking about cross-references - The SME Loan Product Guide references the same eligibility threshold in three different sections. If a fixed text splitter cuts across those sections without overlap, each chunk contains only one piece of the picture. When a client asks a question that requires all three in context, the agent retrieves whichever chunk scored highest in similarity. The client receives a partial answer that appears complete.
  - Checkpoint 2: Thinking about chunk overlap - Overlap adds a defined number of tokens shared between consecutive chunks, reducing the risk of splitting a meaningful unit at the boundary. For a dense legal or financial document, a small overlap may still cut mid-clause, while a large overlap stores significant amounts of redundant content across many chunks. The right overlap value is the smallest number that keeps critical clause boundaries intact.
  - Checkpoint 3: Thinking about tabular data - A text splitter reads a table sequentially and loses the column relationships that give the data its meaning. A chunk produced from a five-column rate table might read "SME Standard 5.2% SME Plus 4.8% SME Flex 5.5%" with no headers to indicate what those figures represent. When a client asks about the SME Plus interest rate, the agent retrieves that chunk and has no reliable way to isolate the correct figure from the string of concatenated values.
  - Checkpoint 4: Thinking about metadata - Every chunk stored in the vector database carries metadata alongside its vector. Semantic similarity search finds chunks that are mathematically close to the query, but two chunks from different sections of the product guide might score similarly for the same query. A "section" metadata field gives the retrieval system an additional filter: if the query is about eligibility criteria, chunks tagged with the eligibility section can be prioritised over chunks from the rate structure section that happened to score similarly.

## Check your Understanding
### Question 1
>  Contigo publishes the 2026 Q2 SME Loan Product Guide. The Q1 version remains in Qdrant alongside the new one. What is the most significant risk of this versioning failure?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cedf2385-9985-4398-85e7-06afacf208dd

### Question 2
>  Contigo's development team is deciding whether to re-ingest the SME Loan Product Guide with a revised chunking strategy. Which criterion most strongly justifies undertaking a full re-ingestion?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/9ce851d5-1101-4f01-91a3-931bce7edfee

> 💡 Takeaway: 
  Document preparation is a design decision that determines how much of the document's meaning survives the ingestion process. A chunk boundary in the wrong place destroys context. A table processed as sequential text loses its structure entirely. The investment in preparing documents correctly before ingestion pays back every time the agent retrieves accurately.