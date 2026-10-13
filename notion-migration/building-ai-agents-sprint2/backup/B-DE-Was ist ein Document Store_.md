# Was ist ein Document Store?

Notion page: https://app.notion.com/p/Was-ist-ein-Document-Store-3789418319f3803fbd05f2757fec58e8
Backed up before n8n migration

> 💡 In dieser Lektion lernst du, was ein Document Store ist und warum wir ihn brauchen. Du erfährst, wie er sich in die Agentflow-v2-Architektur einfügt, bevor du mit der ersten Konfiguration startest.

## Wo wir stehen
Der Meridian Consultings Agentflow v2 kann eine Unterhaltung führen, auf Anweisungen reagieren und innerhalb seines definierten Scopes bleiben. Doch er kennt nur die Daten, mit denen Gemini trainiert wurde. Fragst du ihn nach Meridians internen Projektklassifizierungs-Tiers, Eskalationsverfahren oder Knowledge-Sharing-Protokollen, wird er entweder raten oder ausweichen.
Als Nächstes erhält der Agent eine neue Fähigkeit: Knowledge Retrieval. Wir geben ihm Zugriff auf die echten internen Dokumente von Meridian. So liefert er exakte, spezifische Informationen, statt sich auf allgemeines Reasoning zu verlassen.
Bevor du Elemente auf der Canvas verbindest, solltest du verstehen, was ein Document Store ist und warum wir ihn nutzen.
## Das Problem, wenn du Dokumente direkt an ein Sprachmodell übergibst
Ein Sprachmodell hat ein Context Window, also eine maximale Textmenge, die es in einer einzelnen Anfrage verarbeiten kann. Eine vollständige Dokumentbibliothek in jeden Prompt zu senden, ist nicht praktikabel. Es ist teuer, langsam und stößt schnell an seine Grenzen.
Die Lösung besteht darin, die Dokumente in einem Format zu speichern, das semantisch durchsucht werden kann, indem die relevanten Abschnitte für eine spezifische Query gefunden werden, statt alles auf einmal zu laden. Genau das macht ein Document Store.
## Was ist ein Document Store?
Die Document Stores von Flowise erleichtern das Datenmanagement sehr. Du lädst einfach deinen Datensatz an einem zentralen Ort hoch, teilst ihn auf, bereitest ihn vor und hältst ihn flexibel auf dem neuesten Stand.
Dieser zentralisierte Ansatz vereinfacht das Datenhandling und ermöglicht eine effiziente Verwaltung verschiedener Datenformate, wodurch es leichter wird, deine Daten innerhalb der Flowise-App zu organisieren und darauf zuzugreifen.
Praktisch gesehen ist ein Document Store innerhalb von Flowise ein eigenständiger Wissenscontainer. Alles, was nötig ist, um ein Dokument durchsuchbar zu machen (Upload, Chunking, Embedding und Indexing), passiert innerhalb des Stores über eine einzelne Oberfläche. Es gibt keine externe Vector Database, die separat konfiguriert oder verwaltet werden muss.
## Was in einem Document Store passiert
Wenn ein Dokument zu einem Document Store hinzugefügt wird, durchläuft es vier Stufen, bevor es durchsuchbar wird:
[TABLE]
  | Stufe | Was passiert | Warum es wichtig ist |
  | Upload | Die rohe Dokumentdatei wird in Flowise geladen | Macht den Inhalt für die Verarbeitung verfügbar |
  | Chunking | Das Dokument wird in kleinere Segmente aufgeteilt | Ermöglicht präzises Retrieval relevanter Abschnitte statt ganzer Dokumente |
  | Embedding | Jeder Chunk wird durch ein Embedding-Modell in einen numerischen Vektor umgewandelt | Ermöglicht semantische Ähnlichkeitssuche; Bedeutung finden, nicht nur Keywords |
  | Upserting | Die Vektoren und ihr Source Text werden im Vector Store gespeichert | Macht die Chunks zur Query-Zeit abrufbar |
![image]((notion-hosted file))

Chunking einfach erklärt: Stell dir das Meridians Operations Handbook als ein langes Dokument vor. Ein Consultant, der nach Eskalationsverfahren fragt, braucht nicht das gesamte Handbook, sondern nur den relevanten Abschnitt. Chunking teilt das Dokument in fokussierte Segmente, damit das Abruf-System genau das zurückgeben kann, was relevant ist, ohne alles laden zumüssen.
## Wie es mit Agentflow v2 verbunden wird
Mit einem Agent Node kannst du den Document Store direkt über die Knowledge-Konfiguration in den Agent-Node-Einstellungen hinzufügen. Sobald er verbunden ist, kann der Agent den Store abfragen, wann immer die Eingabe eines Nutzers Informationen aus diesen Dokumenten erfordert.
Der Agent Node entscheidet basierend auf seinem Reasoning und der Beschreibung, die du für die Knowledge Source bereitstellst, wann er den Store abfragt. Eine gut geschriebene Beschreibung sagt dem Agent, welche Art von Informationen der Store enthält und wann es angemessen ist, daraus abzurufen.
## Was Meridians Document Store enthalten wird
Für diesen Sprint werden drei synthetische interne Meridian-Dokumente in einen einzelnen Document Store geladen:
[TABLE]
  | Dokument | Inhalt |
  | Operations Handbook | Projektklassifizierungsrichtlinie, Knowledge-Sharing-Protokoll, Eskalationsverfahren |
  | Engagement Standards | Definitionen von Severity Ratings, Richtlinien für Kundenkommunikation |
  | Regional Playbook | Operativer Kontext für Engagements in Deutschland, Polen und Tschechien |
Diese Dokumente geben dem Agent genügend grounded Content, um echte Consulting-Queries zu beantworten, ohne Policy-Details zu erfinden.
## Verständnisprüfung
>  Ein Meridian-Developer fügt einen Document Store hinzu und lädt drei Dateien hoch, klickt aber nicht auf Upsert. Ein Consultant fragt den Agent dann nach Eskalationsverfahren. Was gibt der Agent zurück?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/1737df9f-57a0-440f-970f-56a9ccf66ed0


> 💡 Takeaway: 
  Ein Document Store ist keine Dateibibliothek. Er ist eine verarbeitete, durchsuchbare Wissensdatenbank. Die vier Phasen (Upload, Chunking, Embedding und Upsert) verwandeln rohe Dokumente in etwas, das der Agent sinnvoll abfragen kann. Diese Phasen zu verstehen, bevor du sie konfigurierst, macht den Unterschied zwischen einer Wissensdatenbank, die präzise Inhalte liefert, und einer, die irrelevante Chunks oder gar nichts zurückgibt.
