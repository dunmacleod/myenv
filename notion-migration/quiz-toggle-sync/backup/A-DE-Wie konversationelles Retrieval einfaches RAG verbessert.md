# Wie konversationelles Retrieval einfaches RAG verbessert

Notion page: https://app.notion.com/p/Wie-konversationelles-Retrieval-einfaches-RAG-verbessert-3779418319f380e981a3d7b1f5a3c303
Backed up before n8n migration

> 💡 Am Ende dieser Lektion verstehst du, warum einfaches Single-Shot-RAG in Multi-Turn-Gesprächen scheitert. Du erfährst, wie die n8n-Retrieval-Pipeline dieses Problem löst, indem sie den Gesprächsverlauf nutzt, um die Query neu zu formulieren. Zudem erkennst du genau, was du in deinem n8n-Workflow kontrollieren kannst und was nicht.

## Wenn einfaches RAG nicht ausreicht
Das Entwicklungsteam der Contigo GmbH hat ein funktionierendes Verständnis der RAG-Pipeline. Dokumente werden aufgenommen, gechunkt, eingebettet und gespeichert. Zur Anfragezeit wird die Frage des Kunden in einen Vektor umgewandelt, die nächstliegenden passenden Chunks werden abgerufen, und das Sprachmodell generiert eine fundierte Antwort.
Für eine einzelne isolierte Frage funktioniert das gut. Aber Contigos Support-Agent bearbeitet keine isolierten Fragen. Er bearbeitet Gespräche, also Multi-Turn-Austausche, bei denen jede Frage auf dem aufbaut, was vorher kam.
Betrachte diesen Austausch:
Turn 1 Kunde:
> „Was sind die Kriterien für die Kreditwürdigkeit beim SME Standard Loan?“
Turn 2 Kunde:
> „Und wie sieht es mit den Rückzahlungsbedingungen dafür aus?“
In einem einfachen RAG-System wird Turn 2 genau so an die Vektordatenbank gesendet, wie er geschrieben wurde: „Und wie sieht es mit den Rückzahlungsbedingungen dafür aus?“ Die Formulierung „dafür“ hat außerhalb des Kontexts von Turn 1 keine Bedeutung. Die Vektordatenbank hat kein Wissen über den vorherigen Austausch. Sie sucht nach Chunks, die semantisch ähnlich zu „Rückzahlungsbedingungen dafür“ sind, und gibt entweder nichts Nützliches oder einen Chunk aus dem falschen Produktabschnitt zurück. Der Agent scheitert nicht, weil die Information in der Wissensdatenbank fehlt, sondern weil das Retrieval-System keine Möglichkeit hatte zu wissen, worauf sich „dafür“ bezog.
## Was konversationelles Retrieval in n8n anders macht
In n8n kannst du dieses Problem mit einer vorgeschalteten Query-Reformulierung lösen. Eine Basic LLM Chain erhält die aktuelle Frage und den relevanten Gesprächsverlauf, formuliert eine eigenständige Suchfrage und übergibt diese an Qdrant. Das geschieht nicht automatisch durch den Qdrant-Node.
Schritt 1: Query-Reformulierung - Bevor die Query die Vektordatenbank erreicht, leitet die Chain sie zusammen mit dem aktuellen Gesprächsverlauf aus dem n8n-Chat-Memory-Sub-Node durch das Sprachmodell. Das Sprachmodell schreibt die Query in eine eigenständige Frage um, die ohne das umgebende Gespräch verstanden werden kann.
Turn 2: „Und wie sieht es mit den Rückzahlungsbedingungen dafür aus?“  … wird zu: „Was sind die Rückzahlungsbedingungen für den Contigo SME Standard Loan?“
Diese reformulierte Query wird an die Vektordatenbank gesendet. Sie enthält jetzt die spezifische Terminologie, die zum richtigen Chunk in der Wissensdatenbank passt.
Schritt 2: Retrieval und fundierte Generierung - Die reformulierte Query wird eingebettet und verwendet, um die am besten passenden Chunks aus der Qdrant-Wissensbasis abzurufen. Diese Chunks werden zusammen mit der ursprünglichen Query und dem Gesprächsverlauf an das Sprachmodell übergeben, um eine fundierte, kontextuell genaue Antwort zu generieren.
![image]((notion-hosted file))

## Was das für deinen n8n-Workflow bedeutet
In n8n kannst du diese Komponenten explizit zu einem Retrieval-Workflow verbinden:
[TABLE]
  | Komponente | Was sie beiträgt |
  | n8n-Chat-Memory-Sub-Node | Liefert den Gesprächsverlauf, der für die Query-Reformulierung verwendet wird |
  | Qdrant Vector Store | Liefert die Chunks, die nach der Reformulierung der Query abgerufen werden |
  | Basic LLM Chain mit Chat Model | Führt sowohl den Reformulierungsschritt als auch die finale fundierte Generierung aus |
Deshalb wird der n8n-Chat-Memory-Sub-Node, den du in Sprint 1 konfiguriert hast, in Sprint 2 weiterverwendet. Ohne verfügbaren Gesprächsverlauf kann ein Reformulierungs-Node Bezüge wie „dafür“ nicht zuverlässig auflösen. Prüfe, ob die relevanten vorherigen Nachrichten tatsächlich in den Reformulierungs-Prompt gelangen. Die RAG-Pipeline und die Memory-Konfiguration hängen voneinander ab.
## Was du in deinem n8n-Workflow kontrollieren kannst
In n8n steuerst du diese Qualitätsfaktoren über die Konfiguration von Loader, Splitter, Embeddings, Retriever und Prompt:
- Top K: Die Anzahl der Chunks, die pro Query abgerufen werden. Ein höherer Wert gibt dem Sprachmodell mehr Kontext, riskiert aber, das Signal mit locker verwandten Chunks zu verwässern. Ein niedrigerer Wert hält den Kontext fokussiert, riskiert aber, relevante Informationen zu verpassen.
- System-Prompt-Grounding: Die Anweisung, die dem Sprachmodell sagt, wie streng es die abgerufenen Chunks verwenden soll. Eine schwache Anweisung erlaubt dem Modell, mit seinen Trainingsdaten zu ergänzen. Ein starkes Verbot verhindert das.
- Chunk-Qualität: Bestimmt durch die getroffenen Chunking- und Vorbereitungsentscheidungen. Der n8n-Retriever ruft ab, was in Qdrant indexiert wurde. Wenn die Chunks schlecht vorbereitet sind, kann Query-Reformulierung das nicht ausgleichen.
- Konsistenz des Embedding-Modells: Während der Ingestion und zur Anfragezeit muss dasselbe Embedding-Modell verwendet werden. Eine Abweichung erzeugt bedeutungslose Ähnlichkeitswerte, unabhängig davon, wie gut die Query reformuliert wurde.
## Was außerhalb des Umfangs dieses Workflows liegt
Der hier besprochene n8n-Ablauf folgt einer festen Abfolge: Query umformulieren, einmal abrufen, Antwort generieren. Sie bewertet nicht, ob die abgerufenen Chunks ausreichen, fragt nicht erneut ab, wenn sie nicht ausreichen, und routet Queries nicht auf Grundlage ihres Inhalts an verschiedene Wissensdatenbanken.
Diese Fähigkeiten gehören zu einer fortgeschritteneren Architektur namens agentisches RAG. Agentisches RAG führt eine autonome Reasoning-Schicht in den Retrieval-Prozess selbst ein, wodurch das System planen, bewerten und iterieren kann, bevor es eine Antwort generiert. Das liegt außerhalb des Umfangs deines aktuellen n8n-Builds, zeigt aber die Richtung, in die sich die Branche bei komplexen Multi-Source-Retrieval-Aufgaben bewegt.
Für Contigos aktuellen Sprint genügt eine kontrollierte n8n-Retrieval-Pipeline mit optionaler Query-Reformulierung. Ein agentischer Ansatz mit Wiederholungsschleifen ist hier nicht notwendig.
## Prüfe dein Verständnis
> 💡 Ein Contigo-Kunde sendet in Turn 4 eines Gesprächs die folgende Nachricht: „Gilt das für dasselbe Produkt?“ Der Agent gibt einen irrelevanten Chunk zurück. Ein Entwickler schlägt vor, den Top-K-Wert zu erhöhen, um das Problem zu beheben. Warum ist das die falsche Diagnose, und was ist die tatsächliche Ursache des Retrieval-Fehlers?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/83a96f57-dfb6-423e-9d3d-47dff4deefbb


> 💡 Takeaway: 
  Eine explizite Query-Reformulierung in n8n verbessert einfaches RAG, indem sie mehrdeutige Folgefragen in eigenständige Fragen reformuliert, bevor das Retrieval beginnt. Dadurch werden Multi-Turn-Gespräche auf eine Weise zuverlässig, wie Single-Shot-RAG es nicht leisten kann.
  Die Reformulierung braucht relevanten Gesprächsverlauf, der im n8n-Workflow aus dem Memory-Kontext an den Reformulierungs-Node übergeben wird. Deshalb sind Memory-Konfiguration und Retrieval-Konfiguration in deinem n8n-Workflow keine zwei getrennten Themen. Sie sind ein zusammenhängendes System.
