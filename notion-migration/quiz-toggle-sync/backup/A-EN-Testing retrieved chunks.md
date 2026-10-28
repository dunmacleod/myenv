# Testing retrieved chunks

Notion page: https://app.notion.com/p/Testing-retrieved-chunks-3669418319f380208891e0070711733d
Backed up before n8n migration

> 💡 What you will work on in this lesson: Inspecting simulated retrieval results across varied query phrasings, diagnosing where semantic search fails to return the correct chunks, and proposing targeted improvements to the retrieval configuration.

## The Scenario
Contigo GmbH's RAG pipeline is configured and the grounding instruction is in place. The compliance team has signed off on the system prompt. The development team is now in the final quality assurance phase before the agent goes into broader internal testing.
The QA engineer assigned to the retrieval evaluation raises a concern that the team has not yet addressed systematically. The retrieval pipeline has been tested with clean, precise queries. But Contigo's clients do not write queries like developers. They describe their situations in natural language, use informal phrasing, reference personal circumstances rather than policy categories, and sometimes ask questions that are semantically adjacent to the correct content without using any of its terminology.
The question the QA engineer is asking is not whether the pipeline works for ideal queries. It is whether the pipeline works for the queries real clients will actually send and what happens when it does not.
This evaluation exercise uses simulated retrieval logs to answer that question. The logs show what Qdrant actually returned for a set of test queries against Contigo's knowledge base. The task is to inspect those results, identify where retrieval succeeded and where it failed, and diagnose why.


## What retrieval evaluation measures
Evaluating a RAG pipeline requires separating two distinct quality dimensions that are easy to conflate.
Retrieval quality: Measures whether the chunks returned by the vector database are relevant to the user's query. A retrieval failure occurs when the returned chunks do not contain the information needed to answer the question. Retrieval quality is evaluated before generation begins.
Generation quality: Measures whether the language model produced an accurate, grounded response from the chunks it received. A generation failure can occur even when retrieval succeeds.
This lesson focuses exclusively on retrieval quality. 
The two dimensions must be evaluated separately: Diagnosing a generation failure as a retrieval problem, or vice versa, leads to the wrong fix.

## The target document
The knowledge base contains a section from the 2026 SME Loan Product Guide with the following content.
Payment Difficulties and Restructuring Options: Contigo GmbH clients experiencing temporary payment difficulties may apply for a loan restructuring arrangement. Applications must be submitted in writing to the client's assigned relationship manager. Restructuring options include a payment holiday of up to three months, a temporary reduction in monthly instalment amount, or an extension of the loan term by up to 24 months. Restructuring is available once per loan agreement. Clients must not be in arrears for more than 60 days at the time of application.
This is the chunk the retrieval pipeline should return for queries related to payment difficulties, missed payments, loan restructuring, and financial hardship.
The simulated retrieval logs
The QA team ran five test queries against the knowledge base. The logs below show which chunk Qdrant returned for each query.
![image]((notion-hosted file))

## Your Tasks

> 🔥 Template: Contigo Retrieval Evaluation worksheet — make a copy (File → Make a copy) and use it to classify each of the five query outcomes, diagnose the Q3 and Q4 failures, and propose targeted improvements.

#### Task A: Evaluate retrieval success and failure
Review all five query results. For each query, classify the retrieval outcome as one of the following:
- Success: The correct chunk was returned with sufficient similarity to support an accurate response
- Partial success: An adjacent or related chunk was returned that contains some relevant information but misses key content
- Failure: An incorrect or irrelevant chunk was returned
For each failure or partial success, write one to two sentences explaining why the semantic mismatch occurred. Consider how the vocabulary of the query compares to the vocabulary of the target chunk, and whether the returned chunk shares surface-level similarity with the query without matching its intent.

#### Task B: Diagnose the retrieval failures
Queries 3 and 4 returned incorrect chunks despite being semantically related to the target content. Diagnose each failure specifically.
For Query 3, explain why the phrase "take a break from paying" is semantically distant from the target chunk's vocabulary, and identify which term in the query may have pulled the retrieval toward the loan application section.
For Query 4, explain why a business context query about a "difficult quarter" and "flexibility" may have produced a higher similarity score for the eligibility criteria section than for the payment difficulties section.

#### Task C: Propose retrieval improvements
For each of the three non-successful queries, propose one specific improvement to address the retrieval failure. Your proposals must come from the following categories:
- Query rewriting: Reformulating the client's query into standardised terminology before it reaches the vector database.
- Chunk metadata enhancement: Adding metadata fields to the target chunk that improve its retrievability for varied query phrasings.
- Knowledge base augmentation: Adding supplementary content to the knowledge base that bridges the vocabulary gap between client phrasing and document terminology.
For each proposal, explain specifically how the improvement addresses the diagnosed failure.

[toggle] Think about the following …
  🔽 Checkpoint 1: Understanding similarity scores - When two out of three retrieved chunks are relevant and one is not, the problem is usually at the boundary between content sections. Consider whether the irrelevant chunk shares enough surface-level terminology with the query to score highly despite being contextually wrong.
  🔽 Checkpoint 2: Diagnosing Query 3 - A vague query produces an imprecise vector because the embedding model has little semantic content to work with. Rewriting the query means adding the specific product name, condition type, and context that the client implied but did not state without changing what they were actually asking.
  🔽 Checkpoint 3: Diagnosing Query 4 - When two document versions share similar terminology, semantic similarity alone cannot distinguish between them. The payload index you created during setup is the mechanism that allows retrieval to be filtered by a specific metadata field value rather than similarity score alone.
  🔽 Checkpoint 4: Evaluating Query 5 - When the fallback phrase triggers for a clearly in-scope query, the retrieval pipeline is working correctly. It found nothing relevant to return. The problem is not retrieval but coverage. Consider whether the knowledge base contains a document that addresses this topic at all.

## Check for Understanding
Question 1
>  Contigo's QA team wrote five test queries based on anticipated client phrasing. Real client queries in production use language the team did not anticipate. Which process most effectively expands the retrieval test set using production data?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/621240a9-680f-459e-a346-38f7f8ac9121

Question 2
>  Contigo is evaluating whether to add a query rewriting step before retrieval. The knowledge base is relatively stable and clients expect fast response times. Which criterion most accurately determines whether query rewriting is justified for this specific deployment?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/37a159a8-0977-40b0-83e9-1a765baa1efe


> 💡 Takeaway: 
  Retrieval quality cannot be assumed from a working pipeline. It must be tested systematically across the range of phrasings real users will actually produce. 
  A system that retrieves correctly for developer-written queries but fails for client-written queries is not a reliable system. The gap between those two query styles is where most retrieval failures occur.