# Chunking strategies

Notion page: https://app.notion.com/p/Chunking-strategies-3669418319f380089184d2958c5822b4
Backed up before n8n migration

> 💡 What you will work on in this lesson: Choosing between fixed-size and semantic chunking strategies for two structurally different document types and justifying each decision based on the document's structure and the queries it will need to support.

## The Scenario
Contigo GmbH's development team has finalised the document selection and prepared the files for ingestion. Before any document enters Qdrant, the team must make one more foundational decision: how to chunk each document.
The team's data engineer raises the question in a review session. Two documents are ready for ingestion: The 2026 SME Loan Product Guide and the EU Consumer Credit Directive Summary. Both are PDFs. Both contain financial and regulatory content. But their internal structures are completely different, and applying the same chunking strategy to both would be the same mistake as applying generic processing.
The team needs to define a chunking approach for each document that reflects its actual structure, the types of queries it will need to support, and the trade-offs between chunk size, overlap, and retrieval precision.

## What is chunking?
Chunking is the process of splitting large documents into smaller, manageable pieces before storing them in a knowledge base. Because language models have a limited context window, they cannot process an entire document at once. Chunking breaks content into segments small enough to be embedded as individual vectors and retrieved selectively based on relevance to a query. 
The size and boundaries of each chunk directly will affect retrieval quality
- Chunks that are too large will dilute the semantic signal
- Chunks that are too small will lose the context needed to answer questions accurately
Good chunking respects the natural structure of the document.

## The two chunking strategies
Before beginning the task, review the two primary approaches available.
- Fixed-size chunking: Naive splitting - Text is divided into segments of a defined token or character count, with a defined overlap between consecutive chunks. The splits occur at the defined boundary regardless of whether they fall mid-sentence, mid-clause, or at a natural content boundary. This approach is fast to configure and consistent in output size, but it risks breaking context at arbitrary points.

Fixed-size chunking works well when the source content is already granular — short, self-contained entries that are unlikely to be split in a damaging way regardless of where the boundary falls.
- Semantic chunking: Structure-aware splitting - Text is divided at meaningful content boundaries such as section headings, paragraph breaks, topic transitions, or logical clause endings. The splits respect the document's inherent structure rather than imposing an external size constraint. This approach requires more configuration and produces variable chunk sizes, but it preserves the integrity of complex, interconnected content.

Semantic chunking is necessary when the source content contains multi-part arguments, cross-referenced clauses, or structured sections where splitting mid-content would destroy the meaning of the retrieved chunk.

## The two documents
Document 1: 2026 SME Loan Product Guide - A 5-page document organised into clearly marked sections, one per loan product, each containing subsections for eligibility criteria, interest rate structures, application requirements, and repayment conditions. Content within each section is densely interconnected. The eligibility criteria for a product reference the rate structure in the same section. The repayment conditions reference the application requirements. Splitting across subsection boundaries would produce chunks that are syntactically complete but semantically incomplete.
Expected query types: 
- Product-specific questions
- Eligibility checks
- Rate comparisons
- Application requirement lookups

Document 2: EU Consumer Credit Directive Summary - A two-page internal summary prepared by Contigo's legal team. The document is organised as a numbered list of thirteen obligations, each stated in one to three sentences. Each obligation is self-contained, does not reference the others, and does not require surrounding context to be understood. The document has no cross-references, no nested clauses, and no interconnected sections.
Expected query types: 
- Specific obligation lookups
- Compliance requirement checks
- Regulatory threshold queries

## Your Tasks

> 🔥 Template: Contigo Chunking Strategy worksheet — make a copy (File → Make a copy) and use it to record your strategy choice for each document, configure the parameters, and work through the transcript case.

#### Task A: Assign and justify the chunking strategy
For each of the two documents, determine which chunking strategy is most appropriate (fixed-size or semantic, and write two to three sentences justifying your choice. Your justification should reference the document's structure and the types of queries it will need to support, not just the general properties of the strategy.

#### Task B: Configure the parameters
For the document where you have chosen fixed-size chunking, propose a specific chunk size in tokens and an overlap value. Justify both numbers. Consider the average length of an individual entry in the document, the risk of splitting a meaningful unit across two chunks, and the cost of storing redundant content through overlap.
For the document where you have chosen semantic chunking, identify the structural feature you would use as the chunking boundary and explain why that boundary preserves the content's meaning for the expected query types.

#### Task C: Evaluate a borderline case
A third document has been added to the ingestion queue: A transcript of a recorded client Q&A session held by Contigo's product team. The transcript is 1,000 words long, has no headings or structural markers, and contains a mixture of product questions, off-topic tangents, and partial sentences where the audio was unclear.
Identify two specific challenges this document presents for both chunking strategies. Propose one pre-processing step the team should apply before chunking that would improve the quality of whatever chunks are produced.

[toggle] Think about the following … 
  🔽 Checkpoint 1: Thinking about the product guide structure - Section-level chunking puts eligibility criteria, rate structure, and repayment conditions into one chunk. Consider whether that serves specific product queries. Subsection-level boundaries produce smaller chunks but more precise retrieval when clients ask about one aspect of a product.
  🔽 Checkpoint 2: Thinking about overlap for fixed-size chunks - Each obligation is self-contained and averages 60 tokens. At a 150-token chunk size, two obligations fit comfortably with room to spare. Since nothing depends on adjacent obligations, a small overlap or none at all is likely sufficient here.
  🔽 Checkpoint 3: Thinking about the Q&A transcript - Chunking a transcript with off-topic tangents and partial sentences embeds noise alongside meaningful content. The retrieval system cannot distinguish between them. Before chunking, consider what transformation removes the irrelevant material without discarding the genuine questions and answers.
  🔽 Checkpoint 4: Thinking about variable chunk sizes - Semantic chunking respects content boundaries but produces variable sizes. A dense section may exceed the embedding model's token limit. Before reverting to fixed-size splitting, check whether the section contains natural internal boundaries such as sub-clauses, numbered points, or paragraph breaks.

## Check your Understanding
### Question 1
>  Contigo's knowledge base contains documents in German, English, and Dutch. A consultant submits a query in German that requires retrieving a relevant chunk from the Dutch regulatory summary. Which factor most directly determines whether the correct chunk is retrieved?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d629cc3b-8cd5-45e0-b7ee-cb1d31c224ac

### Question 2
>  The SME Loan Product Guide is updated next quarter with revised interest rate figures. When should Contigo's team reconsider the chunking strategy rather than applying the existing configuration to the new version?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/2d9d6a98-ffcd-42fa-84c0-5deb9f2b1c0c


> 💡 Takeaway: 
  Chunking strategy is a design decision that must be made for each document based on its structure and the queries it will need to support. A strategy that works well for a numbered list of self-contained obligations will produce broken, incomplete chunks when applied to a densely cross-referenced product guide. 
  Getting this decision right before ingestion determines how accurately the retrieval pipeline performs for the lifetime of that knowledge base.