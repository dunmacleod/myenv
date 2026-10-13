# Retrieval vor Generation

Notion page: https://app.notion.com/p/Retrieval-vor-Generation-3779418319f380c1b2b4eb3964361849
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du baust den Contigo-Support-Agenten von einer einfachen Conversational Chain zu einer RAG-gestützten Pipeline aus. Dafür verbindest du einen Vector Store, bindest ein Embedding-Modell ein und stellst über den System-Prompt fundierte, kontextbasierte Antworten sicher.

## Warum dieser Schritt jetzt kommt
Der Support-Agent der Contigo GmbH hat Memory, Session-Isolation und eine gut entworfene Retention-Policy. Was er immer noch nicht kann, ist Abrufen. Wenn ein Kunde nach Contigos SME-Kreditprodukten fragt, greift der Agent auf das allgemeine Training des Sprachmodells zurück statt auf die tatsächliche Produktdokumentation.
Dieser Walkthrough ändert das nun. Am Ende ruft der Agent relevante Dokument-Chunks aus einer Wissensdatenbank ab, bevor er eine Antwort generiert, und sein System-Prompt setzt durch, dass er nur aus dem antwortet, was er abruft.
Der Build erfolgt in zwei Teilen.
- Zuerst richtest du den Document Store ein (Flowises dedizierte Ingestion-Pipeline), um deine Dokumente zu laden, zu chunken, einzubetten und zu speichern.
- Danach aktualisierst du deinen Chatflow-Canvas, um die Conversation Chain durch eine Conversational Retrieval QA Chain zu ersetzen, die mit diesem Document Store verbunden ist.
> ⚠️ Wichtig: Ab diesem Punkt findet die gesamte Arbeit auf deiner lokalen Flowise-Instanz unter http://localhost:3000 statt. Stelle sicher, dass dein Docker-Container läuft, bevor du beginnst. Falls nicht, öffne ein Terminal und führe docker start flowise aus.
## Teil A: Den Document Store einrichten
Der Document Store übernimmt die gesamte Indexing-Pipeline: Dokumente aus Quellen laden, chunken, in einer Vektordatenbank speichern bzw. aktualisieren und mit den Daten synchronisieren. Hier findet die gesamte Ingestion-Arbeit statt, vollständig getrennt vom Chatflow-Canvas.
### Schritt 1: Einen neuen Document Store erstellen
Klicke in deinem lokalen Flowise-Dashboard im linken Navigationsbereich auf Document Stores. Klicke oben rechts auf Add New. Nenne ihn Contigo-Knowledge und klicke auf Add.
### Schritt 2: Einen Document Loader auswählen
Öffne den Document Store, den du gerade erstellt hast, und klicke auf Add Document Loader. Da deine Wissensdatenbank-Dokumente PDFs sind, wähle PDF File aus der Liste aus.
Lade dein erstes Dokument hoch. Den 2026 SME Loan Product Guide. Füge im Metadatenfeld einen eindeutigen Key hinzu, um dieses Dokument zu identifizieren:
- Key: source
- Value: sme_loan_product_guide_2026
> ➡️ Warum das wichtig ist: Der Metadaten-Key ermöglicht dir zu filtern und zu identifizieren, aus welchem Dokument ein abgerufener Chunk stammt. Das ist besonders wichtig, wenn mehrere Dokumente im selben Document Store liegen. Du kannst genau nachvollziehen, welche Quelle die Antwort des Agenten informiert hat.

### Schritt 3: Den Text Splitter konfigurieren
Klicke auf den Abschnitt Text Splitter und wähle Recursive Character Text Splitter. Konfiguriere die folgenden Parameter basierend auf den Chunking-Entscheidungen, die du in A7.1 getroffen hast:
- Chunk Size: 500
- Chunk Overlap: 50
> ➡️ Warum das wichtig ist: Der Recursive Character Text Splitter respektiert natürliche Inhaltsgrenzen wie Satzenden, Absatzumbrüche und Abschnittsübergänge, bevor er auf Character-Level-Splitting zurückfällt. Das macht ihn zur geeignetsten Wahl für Contigos strukturierte Finanzdokumente.

### Schritt 4: Deine Chunks prüfen
Klicke auf Preview, um zu sehen, wie dein Dokument geteilt wird, bevor du die Konfiguration festlegst. Prüfe die ersten mehreren Chunks sorgfältig:
- Schneiden Chunks mitten im Satz oder mitten in einer Klausel ab?
- Bleiben Kriterien für die Kreditwürdigkeit und Zinsstrukturen im selben Chunk, wenn sie gemeinsam referenziert werden?
- Haben die Chunks eine angemessene Länge? Nicht zu kurz, sodass Bedeutung verloren geht, und nicht zu lang, sodass Retrieval-Präzision verwässert wird?
Wenn die Chunks falsch aussehen, passe die Werte für die Chunk Size und den Overlap an und prüfe erneut. Fahre nicht mit dem nächsten Schritt fort, bis das Chunking korrekt aussieht. Klicke auf Process, sobald du mit der Chunking-Vorschau zufrieden bist.
Sobald du mit dem Chunking zufrieden bist, klicke auf Actions und wähle Upsert All Chunks. Du wirst durch drei Konfigurationsschritte geführt.
### Schritt 5: Das Embedding-Modell und den Vector Store konfigurieren
Gehe zurück zu deinem Chatflow.
1. Embeddings auswählen:
  - Wähle Google Gemini Embeddings.
  - Verbinde dein Credential Contigo Gemini Key. Das Modell ist voreingestellt.
  - Setze Task Type auf RETRIEVAL_DOCUMENT.
1. Vector Store auswählen: Wähle Qdrant. Konfiguriere Folgendes.
  - Qdrant Server URL: http://host.docker.internal:6333
  - Collection Name: passend zur Collection in Schritt 1
1. Record Manager auswählen: Wähle SQLite Record Manager. Konfiguriere Folgendes:
  - Table Name: record_manager_cache
  - Namespace: gleicher Name
  - Cleanup: Incremental
  - SourceId Key: source
> ⚠️ Wichtig: Das Embedding-Modell, das du hier auswählst, muss exakt dasselbe Modell sein, das zur Query-Zeit auf dem Chatflow-Canvas verwendet wird. Eine Abweichung zwischen Embedding-Modellen bei der Einpflegung und der Query-Zeit erzeugt bedeutungslose Ähnlichkeitswerte, und die Retrieval-Pipeline scheitert unbemerkt.

### Schritt 6: Deine Dokumente “upserten”
Klicke auf Upsert, um die vollständige Ingestion-Pipeline auszuführen. Flowise lädt das Dokument, teilt es in Chunks auf, generiert Embeddings für jeden Chunk und speichert die Vektoren im In-Memory Vector Store. Wenn der Upsert abgeschlossen ist, siehst du eine Bestätigung, die zeigt, wie viele Chunks gespeichert wurden.
Wiederhole die Schritte 2–6 für die Standard Loan Application Checklist, mit denselben Text-Splitter-Einstellungen und demselben Embedding-Modell. Füge einen Metadaten-Key source mit dem Value loan_application_checklist_2026 hinzu.
### Schritt 7: Den Document Store testen
Bevor du etwas mit dem Chatflow-Canvas verbindest, überprüfe, dass der Document Store korrekt abruft. Klicke im Document Store auf den Button Retrieval Query und gib ein:
„Welche Dokumente muss ein Kunde mit einem SME-Kreditantrag einreichen?“
Du solltest die am besten passenden Chunks aus der Wissensdatenbank zurückgegeben sehen. Wenn keine Chunks zurückgegeben werden oder die falschen Chunks erscheinen, überprüfe deine Chunking-Konfiguration und aktualisiere (“upserte”) sie erneut, bevor du fortfährst.
## Teil B: Den Chatflow-Canvas aktualisieren
Wenn der Document Store eingerichtet und überprüft ist, kannst du ihn jetzt mit deinem Chatflow verbinden.
### Schritt 1: Deinen bestehenden Chatflow öffnen
Öffne den Chatflow, den du in A7.3 aus Flowise Cloud importiert hast. Du solltest die Conversation Chain, Google Gemini und Buffer Window Memory Nodes auf dem Canvas sehen.
### Schritt 2: Den Conversation Chain Node entfernen
Klicke auf den Conversation Chain Node und lösche ihn aus dem Canvas. Du wirst ihn durch einen Conversational Retrieval QA Chain Node ersetzen.
### Schritt 3: Den Conversational Retrieval QA Chain Node hinzufügen
Klicke auf (+), um das Node-Panel zu öffnen. Suche unter dem Tab LangChain nach Conversational Retrieval QA Chain und ziehe ihn auf den Canvas.
Verbinde die folgenden Nodes:
- Google Gemini Node (ChatGoogleGenerativeAIOutput) → Conversational Retrieval QA Chain Node (Chat Model Input)
- Buffer Window MemoryNode (BufferWindowMemoryOutput) → Conversational Retrieval QA ChainNode (MemoryInput)
### Schritt 4: Den Document Store als Retriever verbinden
Klicke auf (+), um das Node-Panel zu öffnen. Suche unter dem Tab LangChain nach Qdrant und ziehe es auf den Canvas.
Wähle in den Document-Store-Node-Einstellungen Contigo-Knowledge aus dem Dropdown aus. Das ist der Document Store, den du in Teil A erstellt und gespeichert (”upserted”) hast.
Verbinde den folgenden Node:
- Qdrant Node (Qdrant RetrieverOutput) → Conversational Retrieval QA ChainNode (Vector Store Retriever Input)
Konfiguriere in den Qdrant-Node-Einstellungen Folgendes:
- Qdrant Server URL: http://host.docker.internal:6333
- Klicke auf Additional Parameters und füge Folgendes hinzu:
  - Vector Dimension: 3072
  - Content Key: content
  - Metadata Key: metadata
  - Similarity: Cosine
  - Top K: 4
### Schritt 5: Ein Google Gemini Embedding hinzufügen
Klicke auf (+), um das Node-Panel zu öffnen. Suche unter dem Tab LangChain nach Google Gemini Embedding und ziehe es auf den Canvas.
Authentifiziere es mit deinem API-Key-Credential und wähle denselben Modellnamen aus, der während der Ingestion in Teil A verwendet wurde.
Verbinde den folgenden Node:
- Google Gemini Embedding Node (GoogleGenerativeAIEmbeddingsOutput) → Qdrant Node (Embeddings Input)
### Schritt 6: Den System-Prompt aktualisieren
Suche in den Einstellungen des Conversational Retrieval QA Chain Nodes das Feld System Message und gib die folgende Grounding-Anweisung ein:
> Du bist ein Support-Agent für die Contigo GmbH, ein Finanzdienstleistungsunternehmen, das in Deutschland, Österreich und den Niederlanden tätig ist. Beantworte Kundenfragen ausschließlich anhand der Informationen, die im abgerufenen Kontext bereitgestellt werden.
  Wenn die Antwort nicht im abgerufenen Kontext enthalten ist, antworte mit: „Ich habe diese Information nicht in meiner aktuellen Wissensdatenbank. Bitte wenden Sie sich für weitere Unterstützung direkt an einen Contigo-Berater.“
  Nutze kein externes Wissen und stelle keine Annahmen über das hinaus an, was der Kontext aussagt.

> ➡️ Warum das wichtig ist: Ohne eine ausdrückliche Grounding-Anweisung greift das Sprachmodell auf sein allgemeines Training zurück, wenn die abgerufenen Chunks nicht ausreichen. Das erzeugt genau das Halluzinationsproblem, das RAG verhindern soll. Die Fallback-Formulierung gibt dem Agenten eine sichere, professionelle Antwort für Out-of-Scope-Queries.
![image]((notion-hosted file))

### Schritt 7: Speichern und den Knowledge-Boundary-Test ausführen
Speichere den Chatflow und öffne die eingebaute Chat-Oberfläche. Führe den folgenden Zwei-Turn-Test aus, um sowohl den Abruf als auch das Grounding zu validieren.
Turn 1:  In-Domain-Query:„Welche Dokumente muss ein Kunde mit einem SME-Kreditantrag einreichen?“
Worauf du achten solltest: Der Agent gibt eine spezifische, korrekte Antwort aus der Loan Application Checklist im Document Store zurück. Wenn der Agent eine generische Antwort über Kreditdokumentation im Allgemeinen zurückgibt, funktioniert der Abruf nicht. Prüfe, dass der Document-Store-Node korrekt mit dem Vector Store Retriever Input verbunden ist und dass der Upsert erfolgreich abgeschlossen wurde.
Turn 2: Out-of-Domain-Query:„Wie hoch ist der aktuelle Basiszinssatz der Europäischen Zentralbank?“
Worauf du achten solltest: Der Agent antwortet mit der konfigurierten Fallback-Formulierung, statt eine Zahl aus seinen Trainingsdaten zu nennen. Wenn er mit einem EZB-Zinssatz antwortet, schränkt die Grounding-Anweisung das Modell nicht ein. Überarbeite den System-Prompt, um die Einschränkung ausdrücklicher zu machen.
## Checkliste: Vor dem Fortfahren bestätigen
- [ ] Document Store erstellt und Contigo Knowledge Base genannt
- [ ] SME Loan Product Guide hochgeladen, gechunkt und erfolgreich upserted
- [ ] Standard Loan Application Checklist hochgeladen, gechunkt und erfolgreich upserted
- [ ] Document-Store-Retrieval-Query getestet und gibt korrekte Chunks zurück
- [ ] Conversation Chain vom Canvas entfernt
- [ ] Conversational Retrieval QA Chain hinzugefügt und mit ChatGoogleGenerativeAI und Buffer Window Memory verbunden
- [ ] Document-Store-Node mit Vector Store Retriever Input verbunden, Top K auf 4 gesetzt
- [ ] Google Generative AI Embeddings-Node mit text-embedding-004 verbunden
- [ ] System-Prompt mit Grounding-Anweisung und Fallback-Formulierung aktualisiert
- [ ] In-Domain-Query gibt eine spezifische abgerufene Antwort zurück
- [ ] Out-of-Domain-Query gibt die konfigurierte Fallback-Formulierung zurück

> 💡 Takeaway: 
  Abfragen mit dem Agenten zu verbinden, ist eine Abfolge von Abhängigkeiten über zwei getrennte Orte hinweg: den Document Store und den Chatflow-Canvas. Der Document Store muss befüllt sein, bevor die Abfragen gelingen können. Das Embedding-Modell muss zwischen Ingestion und Query-Zeit übereinstimmen.
  Die Grounding-Anweisung muss explizit sein, bevor das Sprachmodell die Einschränkung einhält. Alle drei gleichzeitig richtig umzusetzen, macht die RAG-Pipeline zuverlässig.
