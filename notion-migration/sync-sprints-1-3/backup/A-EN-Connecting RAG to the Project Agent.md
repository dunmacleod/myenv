# Connecting RAG to the Project Agent

Notion page: https://app.notion.com/p/Connecting-RAG-to-the-Project-Agent-3669418319f380e0a73fd6eac310d686
Backed up before n8n migration

## Connect the Knowledge Base to the Agent
Use the Contigo - Short-Term Memory agent built in Sprint 1: Chat Trigger → AI Agent, with OpenRouter Chat Model and Simple Memory connected. The previous Retrieval before generation lesson indexed two documents using Contigo - Knowledge Ingestion in Qdrant collection contigo_knowledge. No new agent or starter JSON is needed.
### 1. Connect the retrieval tool
1. Open Contigo - Short-Term Memory in n8n. Keep its model, memory, and session settings.
1. Add Qdrant Vector Store with a document retrieval operation compatible with the AI Agent Tool connection.
1. Select collection contigo_knowledge and the Qdrant credentials reachable from n8n.
1. Attach Embeddings Google Gemini and select the same Gemini API credential, embedding model, and dimensions that were used in the successful Contigo - Knowledge Ingestion workflow. Check the model ID in the imported ingestion node (for example, gemini-embedding-001 if that is the model configured). Do not use OpenRouter/OpenAI embeddings for retrieval if the documents were indexed with Gemini. Start with Top K = 4.
1. Set a clear tool description: “Search Contigo's SME Loan Product Guide and Standard Loan Application Checklist for eligibility, required documents, and product terms. Return evidence from the indexed documents.”
1. Connect it to the AI Agent's Tool input. If the installed n8n version lacks a supported direct tool operation, use a separate retrieval workflow exposed as a workflow tool or an explicit retrieval step. Inspect the execution output to confirm retrieval really happens.
### 2. Add basic retrieval instructions
Keep the existing role and memory instructions; add:
> For questions about Contigo loan products or application documents, consult the connected knowledge base before answering. Ground product-specific information in retrieved passages. If the documents do not support an answer, acknowledge the gap rather than inventing a policy.
### 3. Verify retrieval
Run both questions in the test chat and inspect tool calls, retrieved chunks, and source metadata:
- What documents must I provide for an SME loan application? — should retrieve the checklist.
- What are the eligibility criteria for Contigo's SME loan? — should retrieve the product guide.
Save the updated agent workflow. In Evidence-aware answers, you will systematically test grounding and improve the fallback.
### Completion checklist
- [ ] Existing agent, Simple Memory, and session isolation preserved
- [ ] Qdrant collection contigo_knowledge connected
- [ ] Query and ingestion embeddings models match
- [ ] Both test questions return relevant, source-labelled passages
- [ ] Updated workflow saved
## Wissensbasis mit dem Agent verbinden
Nutze den Contigo - Short-Term Memory-Agenten aus Sprint 1 (Chat Trigger → AI Agent mit OpenRouter Chat Model und Simple Memory). Im vorherigen Schritt Retrieval vor Generation wurden zwei Dokumente durch Contigo - Knowledge Ingestion in der Qdrant-Collection contigo_knowledge indexiert. Du brauchst keinen neuen Agenten und kein Starter-JSON.
### 1. Retrieval-Tool anbinden
1. Öffne Contigo - Short-Term Memory in n8n. Behalte Chat Model, Memory und Session-Einstellungen bei.
1. Füge Qdrant Vector Store mit einer mit dem AI Agent Tool-Anschluss kompatiblen Retrieval-Operation hinzu.
1. Verwende Collection contigo_knowledge und die aus n8n erreichbaren Qdrant-Credentials.
1. Verbinde Embeddings Google Gemini und verwende dasselbe Gemini-API-Credential, Embedding-Modell und dieselben Dimensionen wie im erfolgreichen Workflow Contigo - Knowledge Ingestion. Prüfe die Modell-ID im importierten Ingestion-Node (z. B. gemini-embedding-001, falls dieses Modell dort konfiguriert ist). Verwende für Retrieval keine OpenRouter-/OpenAI-Embeddings, wenn die Dokumente mit Gemini indexiert wurden. Starte mit Top K = 4.
1. Tool-Beschreibung: „Durchsuche Contigos SME Loan Product Guide und Standard Loan Application Checklist nach Voraussetzungen, benötigten Dokumenten und Produktbedingungen. Gib passende Textstellen zurück.“
1. Verbinde den Tool-Ausgang mit dem Tool-Anschluss des AI Agent. Unterstützt deine n8n-Version dies nicht direkt, nutze einen separaten Retrieval-Workflow als Workflow-Tool oder einen expliziten Retrieval-Schritt. Prüfe den echten Execution-Output.
### 2. Minimale Retrieval-Anweisung
Erhalte die Rollen- und Memory-Anweisungen und ergänze:
> Bei Fragen zu Contigos Kreditprodukten und Antragsunterlagen nutze zuerst die angeschlossene Wissensbasis. Stütze produktspezifische Aussagen auf abgerufene Dokumente. Falls die Quellen keine Antwort belegen, benenne die Wissenslücke und erfinde keine Policy.
### 3. Zwei Tests
Prüfe Tool-Aufruf, Chunks und source-Metadaten im n8n-Execution-Trace:
- What documents must I provide for an SME loan application? — die Checkliste muss passende Informationen liefern.
- What are the eligibility criteria for Contigo's SME loan? — der Product Guide muss passende Informationen liefern.
Speichere den Workflow. In Evidenzbewusste Antworten testest und verbesserst du anschließend das Grounding.
### Checkliste
- [ ] Agent aus Sprint 1 mit Memory und Session-Isolation erhalten
- [ ] Qdrant-Collection contigo_knowledge verbunden
- [ ] Embedding-Modelle bei Indexierung und Suche identisch
- [ ] Zwei Fragen liefern passende Chunks mit Quellen
- [ ] Workflow gespeichert