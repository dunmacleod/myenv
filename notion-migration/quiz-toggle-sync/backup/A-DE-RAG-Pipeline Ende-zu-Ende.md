# RAG-Pipeline Ende-zu-Ende

Notion page: https://app.notion.com/p/RAG-Pipeline-Ende-zu-Ende-3779418319f380fcb1e3f471e340e2d6
Backed up before n8n migration

> 💡 Nach dieser Lektion verstehst du den gesamten Ablauf, der rohe Geschäftsdokumente in fundierte Agentenantworten verwandelt. Du kennst jeden einzelnen Schritt von der ersten Ingestion bis zur generierten Antwort.

## Vom Problem zum Prozess
Das Entwicklungsteam der Contigo GmbH versteht jetzt, warum RAG unentbehrlich ist. Der Agent kann sich nicht allein auf erstarrte Trainingsdaten verlassen, wenn Kunden nach Kreditprodukten, Compliance-Regeln oder internen Richtlinien fragen. Für nützliche Antworten benötigt er direkten Zugriff auf Contigos reale Dokumente.
Doch wie funktioniert dieser Zugriff in der Praxis?
Das System kann dem Agenten nicht bei jeder Kundenfrage eine riesige Datei übergeben. Stattdessen bereitet es Dokumente vor, speichert sie durchsuchbar und ruft bei Bedarf nur die relevanten Teile ab.
Hier kommt die RAG-Pipeline ins Spiel.
Diese Pipeline arbeitet in zwei Hauptphasen. Die erste Phase läuft im Hintergrund ab, noch bevor ein Nutzer eine Frage stellt. Das System lädt Dokumente, teilt sie in kleinere Chunks auf, wandelt diese in Embeddings um und speichert sie. Die zweite Phase passiert in Echtzeit, sobald eine Kundenanfrage eingeht. Das System sucht die passendsten Chunks und übergibt sie dem LLM als Kontext.
Damit das Team diesen Ablauf versteht, muss es zuerst wissen, wo diese Chunks liegen und wie die Suche funktioniert.
### Was ist eine Vektordatenbank?
Eine Vektordatenbank speichert und durchsucht Embeddings.
Klassische Datenbanken suchen nach exakten Treffern wie Keywords, IDs, Zeilenwerten oder Filtern. Eine Vektordatenbank arbeitet anders. Sie sucht nach semantischer Ähnlichkeit. Das bedeutet: Sie findet Textabschnitte mit ähnlicher Bedeutung, selbst wenn die Wörter völlig abweichen.
Eine herkömmliche Datenbank zum Beispiel findet nur einen Abschnitt, wenn dort das Wort „refund“ steht. Eine Vektordatenbank liefert auch Textstellen mit „money back“, „reimbursement“ oder „cancelled payment“, da ähnliche Embeddings dieselbe Bedeutung repräsentieren.
Genau das macht Vektordatenbanken ideal für RAG. Nutzer formulieren Fragen selten exakt wie die Quelltexte. Die Vektordatenbank schließt diese Lücke und findet Dokument-Chunks, die inhaltlich zur Frage passen.
### Was ist Chroma?
In Contigos Stack ist Chroma die Vektordatenbank.
Chroma ist eine beliebte Open-Source-Vektordatenbank für KI- und RAG-Anwendungen. In dieser Pipeline speichert sie die eingebetteten Dokument-Chunks zusammen mit dem Originaltext und Metadaten wie Dokumentname, Seitenzahl oder Abschnitt.
Für Contigo fungiert Chroma als Retrieval-Schicht des RAG-Systems. Es schreibt keine Antworten und führt kein Reasoning wie ein LLM aus. Seine Aufgabe ist enger und mechanischer: Chunks speichern, Vektoren vergleichen und die relevantesten Textstücke zurückgeben, wenn eine Anfrage eintrifft.
Sobald Chroma diese relevanten Chunks zurückgibt, kann das LLM sie als Kontext verwenden, um eine fundierte Antwort zu generieren.
## Phase 1: Die Wissensdatenbank vorbereiten
Die Hintergrundphase wandelt rohe Dokumente in ein mathematisch durchsuchbares Format um. Sie läuft beim ersten Import von Dokumenten und bei jedem Update der Wissensdatenbank. In n8n wird die erste Phase als eigener Ingestion-Workflow umgesetzt. Document Loader, Text Splitter, Embedding-Modell und Qdrant Vector Store verarbeiten und indexieren die Daten. Ein einfacher Datei-Upload macht die Dokumente noch nicht durchsuchbar.
- Schritt 1: Ingestion - Die Pipeline beginnt damit, rohe Inhalte aus der Quelle zu laden. Für Contigo könnte das bedeuten, PDFs mit Kreditproduktspezifikationen, Word-Dokumente mit Compliance-Richtlinien oder strukturierte Daten aus internen Richtliniendatenbanken zu importieren. Der Inhalt wird gelesen und in Klartext extrahiert, den das System verarbeiten kann.
- Schritt 2: Chunking - Große Dokumente werden in kleinere Segmente aufgeteilt, die Chunks genannt werden. Das ist aus zwei Gründen notwendig. Erstens haben Embedding-Modelle und Sprachmodelle Token-Limits. Ein 200-seitiges Compliance-Handbuch kann zum Beispiel nicht als einzelne Eingabe in ein Modell gegeben werden. Zweitens erzeugen kleinere Chunks präziseres Retrieval. Wenn ein Kunde also nach einer bestimmten Klausel fragt, sollte das System genau diese Klausel zurückgeben, nicht einen ganzen Dokumentabschnitt darum herum.
  Chunk-Größe und die Überlappung zwischen aufeinanderfolgenden Chunks sind Designentscheidungen, die die Retrieval-Qualität erheblich beeinflussen. Diese Entscheidungen werden später in diesem Sprint ausführlich behandelt.
- Schritt 3: Embedding - Jeder Chunk wird in ein Vector Embedding umgewandelt, also ein numerisches Array, das die semantische Bedeutung des Textes erfasst. Ein Embedding-Modell führt diese Umwandlung durch. Die resultierenden Vektoren repräsentieren den Inhalt mathematisch, in einer Form, die das System vergleichen und durchsuchen kann.
- Schritt 4: Speicherung - Das System speichert die Vektoren zusammen mit dem Originaltext und nützlichen Metadaten wie Quelldokument, Seitenzahl, Abschnitt oder Dateiname in einer Vektordatenbank. Bei Contigo übernimmt Qdrant diese Aufgabe.
  An diesem Punkt hat jeder Chunk drei wichtige Teile: den Embedding-Vektor, der die Bedeutung des Chunks repräsentiert; den Originaltext, der später als Kontext zurück an das Sprachmodell gesendet werden kann; und die Metadaten, die helfen nachzuvollziehen, woher die Information stammt. Die Datenbank ist jetzt bereit, Anfragen zu empfangen.
  Wenn ein Nutzer eine Frage stellt, wird die Frage ebenfalls in einen Vektor umgewandelt. Qdrant vergleicht dann diesen Query-Vektor mit den gespeicherten Chunk-Vektoren und gibt die Chunks zurück, die semantisch am ähnlichsten sind. Diese abgerufenen Chunks werden zu dem Kontext, den das LLM verwendet, um eine fundierte Antwort zu generieren.
## Phase 2: Eine Anfrage zur Laufzeit beantworten
Die Laufzeitphase startet jedes Mal, wenn ein Kunde eine Nachricht sendet. In n8n kann die Laufzeitphase mit einem Vector-Store-Retriever und einer Frage-Antwort-Kette oder einem Retrieval-Tool am AI Agent umgesetzt werden. Die tatsächliche Laufzeit hängt vom Modell, Datenbestand und Hosting ab.
- Schritt 5: Query Embedding - Die Frage des Kunden wird durch dasselbe Embedding-Modell geleitet, das während der Ingestion verwendet wurde. Dadurch wird die Anfrage mit identischen mathematischen Repräsentationen in einen Vektor umgewandelt, was entscheidend ist. Wenn zur Anfragezeit ein anderes Embedding-Modell verwendet würde, würden die Ähnlichkeitsvergleiche bedeutungslose Ergebnisse liefern.
- Schritt 6: Retrieval - Der Query-Vektor wird mit allen gespeicherten Dokumentvektoren in der Datenbank verglichen. Das System berechnet mathematisch, welche gespeicherten Vektoren dem Query-Vektor am nächsten liegen, und gibt die am besten passenden Chunks zurück. Das ist semantische Suche, mit der du Inhalte finden kannst, die dasselbe bedeuten wie die Anfrage, auch wenn die exakten Wörter unterschiedlich sind.
- Schritt 7: Generation - Die abgerufenen Chunks werden an die ursprüngliche Anfrage des Kunden angehängt, um einen angereicherten Prompt zu bilden. Das Sprachmodell erhält diese kombinierte Eingabe und generiert eine Antwort, die in den abgerufenen Inhalten verankert ist. Der System-Prompt weist das Modell an, nur auf Grundlage des bereitgestellten Kontexts zu antworten und anzuerkennen, wenn die Information nicht verfügbar ist.
## Die vollständige Pipeline auf einen Blick
![image]((notion-hosted file))
[TABLE]
  | Phase | Schritt | Was passiert | Output |
  | Hintergrund | Ingestion | Dokumente werden geladen und extrahiert | Rohtext |
  | Hintergrund | Chunking | Text wird in Segmente aufgeteilt | Text-Chunks |
  | Hintergrund | Embedding | Chunks werden in Vektoren umgewandelt | Vector Embeddings |
  | Hintergrund | Speicherung | Vektoren werden mit Metadaten gespeichert | Befüllte Vektordatenbank |
  | Laufzeit | Query Embedding | Kundenanfrage wird in einen Vektor umgewandelt | Query-Vektor |
  | Laufzeit | Retrieval | Datenbank gibt die nächstliegenden passenden Chunks zurück | Relevanter Inhalt |
  | Laufzeit | Generation | LLM antwortet mithilfe des abgerufenen Inhalts | Fundierte Antwort |
## Verständnis prüfen
> 💡 Warum muss die Anfrage während der Laufzeitphase einer RAG-Pipeline mit demselben Modell eingebettet werden, das während der Ingestion die Dokumente eingebettet hat?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/9032e509-8dac-488c-91d7-af634822d7fc

> 💡 Takeaway: 
  Die RAG-Pipeline ist genauso ein Data-Engineering-System wie ein AI-System. Die Qualität der Antworten des Agenten hängt vollständig davon ab, wie gut die Pipeline die zugrunde liegenden Inhalte vorbereitet, speichert und abruft. Ein gut konfigurierter Generierungsschritt kann schlechtes Chunking, nicht übereinstimmende Embedding-Modelle oder eine unvollständige Wissensdatenbank nicht ausgleichen, bevor der Agent zuverlässig funktionieren kann.
  In n8n sind Indexierung und Retrieval getrennte Workflow-Aufgaben. Verwende dieselbe Qdrant-Collection und kompatible Embeddings. Prüfe die zurückgegebenen Textstellen und Quellen, bevor du der generierten Antwort vertraust.
