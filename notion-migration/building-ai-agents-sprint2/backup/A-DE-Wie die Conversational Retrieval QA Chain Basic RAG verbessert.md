# Wie die Conversational Retrieval QA Chain Basic RAG verbessert

Notion page: https://app.notion.com/p/Wie-die-Conversational-Retrieval-QA-Chain-Basic-RAG-verbessert-3779418319f380e981a3d7b1f5a3c303
Backed up before n8n migration

> 💡 Am Ende dieser Lektion verstehst du, warum einfaches Single-Shot-RAG in Multi-Turn-Gesprächen scheitert. Du erfährst, wie die Conversational Retrieval QA Chain dieses Problem löst, indem sie den Gesprächsverlauf nutzt, um die Query neu zu formulieren. Zudem erkennst du genau, was du in deinem Chatflow-Build kontrollieren kannst und was nicht.

## Wenn einfaches RAG nicht ausreicht
Das Entwicklungsteam der Contigo GmbH hat ein funktionierendes Verständnis der RAG-Pipeline. Dokumente werden aufgenommen, gechunkt, eingebettet und gespeichert. Zur Anfragezeit wird die Frage des Kunden in einen Vektor umgewandelt, die nächstliegenden passenden Chunks werden abgerufen, und das Sprachmodell generiert eine fundierte Antwort.
Für eine einzelne isolierte Frage funktioniert das gut. Aber Contigos Support-Agent bearbeitet keine isolierten Fragen. Er bearbeitet Gespräche, also Multi-Turn-Austausche, bei denen jede Frage auf dem aufbaut, was vorher kam.
Betrachte diesen Austausch:
Turn 1 Kunde:
> „Was sind die Kriterien für die Kreditwürdigkeit beim SME Standard Loan?“
Turn 2 Kunde:
> „Und wie sieht es mit den Rückzahlungsbedingungen dafür aus?“
In einem einfachen RAG-System wird Turn 2 genau so an die Vektordatenbank gesendet, wie er geschrieben wurde: „Und wie sieht es mit den Rückzahlungsbedingungen dafür aus?“ Die Formulierung „dafür“ hat außerhalb des Kontexts von Turn 1 keine Bedeutung. Die Vektordatenbank hat kein Wissen über den vorherigen Austausch. Sie sucht nach Chunks, die semantisch ähnlich zu „Rückzahlungsbedingungen dafür“ sind, und gibt entweder nichts Nützliches oder einen Chunk aus dem falschen Produktabschnitt zurück. Der Agent scheitert nicht, weil die Information in der Wissensdatenbank fehlt, sondern weil das Retrieval-System keine Möglichkeit hatte zu wissen, worauf sich „dafür“ bezog.
## Was die Conversational Retrieval QA Chain anders macht
Die Conversational Retrieval QA Chain löst dieses Problem durch einen zweistufigen Prozess, der stattfindet, bevor das Retrieval beginnt.
Schritt 1: Query-Reformulierung - Bevor die Query die Vektordatenbank erreicht, leitet die Chain sie zusammen mit dem aktuellen Gesprächsverlauf aus dem Buffer-Window-Memory-Node durch das Sprachmodell. Das Sprachmodell schreibt die Query in eine eigenständige Frage um, die ohne das umgebende Gespräch verstanden werden kann.
Turn 2: „Und wie sieht es mit den Rückzahlungsbedingungen dafür aus?“  … wird zu: „Was sind die Rückzahlungsbedingungen für den Contigo SME Standard Loan?“
Diese reformulierte Query wird an die Vektordatenbank gesendet. Sie enthält jetzt die spezifische Terminologie, die zum richtigen Chunk in der Wissensdatenbank passt.
Schritt 2: Retrieval und fundierte Generierung - Die reformulierte Query wird eingebettet und verwendet, um die am besten passenden Chunks aus dem Document Store abzurufen. Diese Chunks werden zusammen mit der ursprünglichen Query und dem Gesprächsverlauf an das Sprachmodell übergeben, um eine fundierte, kontextuell genaue Antwort zu generieren.
![image]((notion-hosted file))

## Was das für deinen Chatflow-Build bedeutet
Die Conversational Retrieval QA Chain kombiniert drei Komponenten, die du in A8.1 verbinden wirst:
[TABLE]
  | Komponente | Was sie beiträgt |
  | Buffer-Window-Memory-Node | Liefert den Gesprächsverlauf, der für die Query-Reformulierung verwendet wird |
  | Document Store | Liefert die Chunks, die nach der Reformulierung der Query abgerufen werden |
  | ChatGoogleGenerativeAI-Node | Führt sowohl den Reformulierungsschritt als auch die finale fundierte Generierung aus |
Deshalb wird der Buffer-Window-Memory-Node, den du in Sprint 1 konfiguriert hast, in Sprint 2 weiterverwendet. Ohne ihn hat die Chain keinen Gesprächsverlauf, auf den sie zurückgreifen kann, und Query-Reformulierung kann nicht stattfinden. Die RAG-Pipeline und die Memory-Konfiguration hängen voneinander ab.
## Was du in deinem Chatflow kontrollieren kannst
Innerhalb der Conversational Retrieval QA Chain hast du direkte Kontrolle über die folgenden Hebel für Retrieval-Qualität:
- Top K: Die Anzahl der Chunks, die pro Query abgerufen werden. Ein höherer Wert gibt dem Sprachmodell mehr Kontext, riskiert aber, das Signal mit locker verwandten Chunks zu verwässern. Ein niedrigerer Wert hält den Kontext fokussiert, riskiert aber, relevante Informationen zu verpassen.
- System-Prompt-Grounding: Die Anweisung, die dem Sprachmodell sagt, wie streng es die abgerufenen Chunks verwenden soll. Eine schwache Anweisung erlaubt dem Modell, mit seinen Trainingsdaten zu ergänzen. Ein starkes Verbot verhindert das.
- Chunk-Qualität: Bestimmt durch die getroffenen Chunking- und Vorbereitungsentscheidungen. Die Conversational Retrieval QA Chain ruft ab, was im Document Store liegt. Wenn die Chunks schlecht vorbereitet sind, kann Query-Reformulierung das nicht ausgleichen.
- Konsistenz des Embedding-Modells: Während der Ingestion und zur Anfragezeit muss dasselbe Embedding-Modell verwendet werden. Eine Abweichung erzeugt bedeutungslose Ähnlichkeitswerte, unabhängig davon, wie gut die Query reformuliert wurde.
## Was außerhalb des Umfangs dieses Chatflows liegt
Die Conversational Retrieval QA Chain folgt einer festen Abfolge. Sie reformuliert die Query, ruft einmal ab und generiert. Sie bewertet nicht, ob die abgerufenen Chunks ausreichen, fragt nicht erneut ab, wenn sie nicht ausreichen, und routet Queries nicht auf Grundlage ihres Inhalts an verschiedene Wissensdatenbanken.
Diese Fähigkeiten gehören zu einer fortgeschritteneren Architektur namens agentisches RAG. Agentisches RAG führt eine autonome Reasoning-Schicht in den Retrieval-Prozess selbst ein, wodurch das System planen, bewerten und iterieren kann, bevor es eine Antwort generiert. Das liegt außerhalb des Umfangs deines aktuellen Chatflow-Builds, zeigt aber die Richtung, in die sich die Branche bei komplexen Multi-Source-Retrieval-Aufgaben bewegt.
Für Contigos Support-Agenten, wie er in diesem Kurs gebaut wird, ist die Conversational Retrieval QA Chain die richtige und ausreichende Architektur.
## Prüfe dein Verständnis
>  Ein Contigo-Kunde sendet in Turn 4 eines Gesprächs die folgende Nachricht: „Gilt das für dasselbe Produkt?“ Der Agent gibt einen irrelevanten Chunk zurück. Ein Entwickler schlägt vor, den Top-K-Wert zu erhöhen, um das Problem zu beheben. Warum ist das die falsche Diagnose, und was ist die tatsächliche Ursache des Retrieval-Fehlers?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/83a96f57-dfb6-423e-9d3d-47dff4deefbb


> 💡 Takeaway: 
  Die Conversational Retrieval QA Chain verbessert einfaches RAG, indem sie mehrdeutige Folgefragen in eigenständige Fragen reformuliert, bevor das Retrieval beginnt. Dadurch werden Multi-Turn-Gespräche auf eine Weise zuverlässig, wie Single-Shot-RAG es nicht leisten kann.
  Die Reformulierung hängt vollständig vom Gesprächsverlauf ab, der durch den Buffer-Window-Memory-Node bereitgestellt wird. Deshalb sind Memory-Konfiguration und Retrieval-Konfiguration in deinem Chatflow keine zwei getrennten Themen. Sie sind ein zusammenhängendes System.
