# Choosing source documents

Notion page: https://app.notion.com/p/Choosing-source-documents-3669418319f3803bb1fcf755374795f9
Backed up before n8n migration

> 💡 What you will work on in this lesson: Evaluating a set of candidate documents for inclusion in a business knowledge base and justifying each decision using clear criteria for relevance, accuracy, and safety.

## The Scenario
Contigo GmbH's development team is ready to build the knowledge base that will power the support agent's retrieval pipeline. The compliance team has signed off on the RAG architecture. Before any document enters the retrieval pipeline, it must be evaluated against clear inclusion criteria. The question facing the team now is deceptively straightforward: Which documents should actually go into the knowledge base? 
The answer matters more than it might appear. A RAG system retrieves content based on semantic similarity. It finds the chunks that are mathematically closest to the user's query and passes them to the language model as context. It has no built-in understanding of whether a document is current, approved, or appropriate for client-facing use. If an outdated policy document, an internal draft, or a file containing sensitive personal data is included in the knowledge base, the agent will retrieve from it with the same confidence it retrieves from a verified, current policy.
The principle here is simple: 
> ➡️ The quality of the agent's answers is bounded by the quality of the documents it has access to. Getting document selection right before ingestion is significantly easier than correcting retrieval failures after deployment.

## The three criteria
Before classifying any document, establish the criteria you will apply consistently across all candidates.
- Relevance: Does this document contain information the agent will be asked about? A document that is accurate and current but covers topics outside the agent's defined scope adds noise to the knowledge base without adding value. Irrelevant chunks compete with relevant ones during retrieval and reduce precision.
- Accuracy and currency: Is the information in this document correct and up to date? An outdated document that contradicts current policy is more dangerous than a missing document. The agent will retrieve it, cite it, and give clients incorrect information with apparent authority.
- Safety and appropriateness: Is this document safe to include in a system that will surface its content to clients or client-facing staff? Documents containing personal data, internal communications, unapproved drafts, or sensitive commercial information should not be in a retrieval system unless access controls are applied that the RAG pipeline itself cannot enforce.
![image]((notion-hosted file))
## The candidate documents
Contigo's operations team has compiled the following seven files as candidates for the knowledge base. Review each one carefully before beginning the classification task.
1. 2026 SME Loan Product Guide (PDF): The current, approved product documentation covering loan limits, eligibility criteria, interest rate ranges, and application requirements for Contigo's SME financing products across Germany, Austria, and the Netherlands.
1. 2023 SME Loan Product Guide (PDF): A previous version of the same document. Several loan limits and eligibility thresholds have changed since this version was published.
1. EU Consumer Credit Directive Summary (PDF): A two-page internal summary of the key obligations under the EU Consumer Credit Directive, prepared by Contigo's legal team and marked as approved for operational use.
1. Client Transaction Export Q1 2026 (CSV): A structured data export containing client names, account numbers, loan amounts, and payment histories for all active accounts in the first quarter of 2026.
1. Internal Slack Export Compliance Channel (TXT): A raw text export of one month of internal Slack messages from the compliance team, including discussions of regulatory interpretations, unresolved questions, and informal opinions from individual staff members.
1. Standard Loan Application Checklist (PDF): A one-page checklist of the documents clients must submit with a loan application, updated in January 2026 and approved for client-facing use.
1. Draft Client Communication Template [Netherlands (DOCX)]: A template for client-facing letters related to Dutch loan applications, currently under legal review and not yet approved for use.

## Your Tasks

> 🔥 
  ### Template: Contigo KB Evaluation worksheet 
  Make a copy and use it to capture your criteria and your seven Include/Exclude decisions as you work through the tasks below.

#### Task A: Define your inclusion criteria
Write two to three sentences defining what qualifies a document for inclusion in Contigo's RAG knowledge base. Your criteria should be specific enough to apply consistently across all seven candidates; a rule that produces a clear decision for each file.

#### Task B: Classify each document
Apply your criteria to all seven candidates. For each one, decide whether to Include or Exclude, and write one sentence explaining how your criteria justify that decision.
Pay particular attention to documents where the decision is not immediately obvious. A document can be accurate and relevant but still inappropriate for inclusion. A document can be inappropriate for the current knowledge base but appropriate in a different configuration.
[toggle] Think about the following …
  🔽 Checkpoint 1: Think about conflicting versions - Consider that the retrieval system has no concept of "current" or "outdated." It returns chunks based on semantic similarity alone. If two versions of the same document are in the knowledge base and they contain different figures for the same loan limit, the agent will retrieve from both and the client will receive whichever version happened to score higher in that query. There is no warning that a conflict exists.
  🔽 Checkpoint 2: Thinking about personal data - RAG retrieves based on semantic similarity, not document type or sensitivity level. A client asking about account management could receive chunks containing another client's name, account number, or financial history if that data is in the knowledge base. Under GDPR, surfacing personal data about one individual in a response to another is not a retrieval configuration problem. It is a data protection violation.
  🔽 Checkpoint 3: Thinking about unstructured informal content - Think about the difference between a formally approved policy document and an informal Slack message where a compliance officer speculates about a regulatory interpretation. The agent cannot distinguish between the two. It retrieves based on semantic relevance. If an informal, unapproved interpretation is retrieved and presented to a client as a response, it carries the same apparent authority as verified policy content.
  🔽 Checkpoint 4: Thinking about draft documents - A document under legal review has not been approved for use. If the agent retrieves it and uses it to answer a client query, there is no visible indicator in the response that the content was provisional. From the client's perspective, the answer looks exactly the same as one drawn from an approved document. 

## Check for Understanding
### Question 1
>  Contigo's knowledge base contains a loan product guide that becomes outdated when rates are revised quarterly. Which process most effectively keeps the knowledge base current without requiring a full re-ingestion each time?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/07fb5bff-a434-4fd1-b13d-e219e72a4ab4

### Question 2
>  A Contigo agent needs access to a client's loan amount and payment history to personalise its responses. Which architectural approach allows this without ingesting that data into the RAG knowledge base?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cbd9842a-ec80-44ad-9870-ef83b516e052

> 💡 Takeaway: 
  A RAG system is only as reliable as the documents it retrieves from. Including an outdated policy creates a misinformation risk. Including personal data creates a compliance risk. Including unapproved drafts creates a legal risk. None of these risks are visible in the agent's output until something goes wrong.