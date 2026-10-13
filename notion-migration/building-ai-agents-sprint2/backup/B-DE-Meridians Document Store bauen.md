# Meridians Document Store bauen

Notion page: https://app.notion.com/p/Meridians-Document-Store-bauen-3789418319f3808682fae4c27efb8af2
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du erstellst Schritt für Schritt einen Document Store, lädst die internen Dokumente von Meridian hoch und konfigurierst sie. Anschließend prüfst du, ob die Wissensdatenbank korrekt funktioniert, bevor du sie mit dem Agenten verbindest.

## Den Kontext herstellen
Der Agent von Meridian Consulting kann jetzt ein Gespräch führen, im Scope bleiben und sich daran erinnern, was zuvor in einer Session gesagt wurde. Was er dennoch nicht kann, ist Fragen über Meridian selbst zu beantworten.
Frag ihn, wie ein Severity-2-Issue eskaliert werden sollte oder welche Sprache für eine Lieferung in Polen verwendet werden soll, und er hat nichts, worauf er zurückgreifen kann. Der System-Prompt definiert, wie sich der Agent verhält. Er enthält nicht den Meridians interne Dokumentation. Ohne einen Zugriff auf diese Dokumentation kann der Agent nur allgemein antworten. Dies ist nützlich für einen Chatbot, jedoch nutzlos für eine Beratungsfirma.
Die Lösung besteht darin, dem Agenten seine eigene durchsuchbare Kopie von Meridians internen Dokumenten zu geben. Wenn eine Frage eingeht, ruft der Agent die relevantesten Passagen ab und antwortet aus diesen, statt nur aus Trainingsdaten. Dieses Muster nennt man Retrieval, und der Ort, an dem die Dokumente liegen, ist ein Document Store.
## Was du testest
Ein Document Store ist nur nützlich, wenn Retrieval tatsächlich die richtigen Passagen für eine bestimmte Frage zurückgibt. Zwei Dinge müssen gleichzeitig funktionieren.
Die Dokumente sind mit der richtigen Granularität indexiert. Chunks müssen klein genug sein, damit ein einzelner Chunk ungefähr eine Sache behandelt, und groß genug, damit diese Sache für sich genommen Sinn ergibt. Zu große Chunks mischen nicht zusammenhängende Policies in einer Passage; zu kleine Chunks teilen eine einzelne Policy über mehrere Passagen hinweg auf. Beide Fehlermodi verschlechtern das Retrieval.
Embedding-Modell und Vector Store stimmen bei den Dimensionen überein. Das Embedding-Modell erzeugt Vektoren mit einer festen Größe. Der Vector Store muss genau diese Größe erwarten. Eine Abweichung führt zu einem sofortigen Fehler und der Upsert schlägt fehl.
Beide Bedingungen werden am Ende dieser Lektion mit drei Abruf-Test-Queries geprüft. Wenn eine davon falsch ist, geben die Queries nichts Nützliches zurück, und du wirst es bemerken, bevor der Document Store mit dem Agenten verbunden wird.
## Was du baust
Einen Flowise Document Store namens meridian-knowledge, der drei synthetische interne Meridian-Dokumente enthält. Wenn er fertig ist, ist der Store bereit, als Wissensquelle mit dem Agent Node verbunden zu werden.
## Die synthetischen Dokumente
Lade die drei Textdateien auf deinen Rechner herunter, bevor du beginnst. Sie repräsentieren Meridians interne Dokumentation.
- Datei 1: meridian_operations.txt
  https://drive.google.com/file/d/1nZKN-io5mgo02WHiynSua_ENvGDGJmr4/view?usp=drive_link
- Datei 2: meridian_engagement_standards.txt
  https://drive.google.com/file/d/1ChoCGGCj_dxbv3mZCsZTzRZJtOlsgbIB/view?usp=drive_link
- Datei 3: meridian_regional_playbook.txt
  https://drive.google.com/file/d/1LMePSCwEN7eo5BtSF5vVApecv-DtTqRs/view?usp=drive_link

## Deine Aufgaben
### Schritt 1: Flowise und Qdrant starten
Bevor du Flowise öffnest, bestätige, dass beide Container laufen. Öffne ein Terminal und führe aus:
```powershell
docker ps
```
Du solltest beide Container wie folgt aufgelistet sehen:
```powershell
flowise     running     0.0.0.0:3000->3000/tcp
qdrant      running     0.0.0.0:6333->6333/tcp
```
Wenn einer davon fehlt, starte ihn wie folgt neu:
```powershell
docker start flowise
docker start qdrant
```
Finde dann die Wi-Fi-IPv4-Adresse deines Rechners. Du brauchst sie, um Flowise mit Qdrant zu verbinden:
```powershell
ipconfig
```

Notiere die IPv4 Address unter Wireless LAN adapter Wi-Fi. Sie sieht aus wie 192.168.x.x.

Bestätige, dass Qdrant erreichbar ist, indem du diese URL in deinem Browser öffnest:
```powershell
http://192.168.x.x:6333/dashboard
```
Du siehst möglicherweise eine JSON-Antwort mit der Qdrant-Versionsnummer oder ein Dashboard. Wenn ja, ist es bereit.

### Schritt 2: Document Stores in Flowise öffnen
Öffne dein Flowise-Dashboard unter http://localhost:3000. Klicke im linken Navigationsbereich auf Document Stores.
Klicke auf + Add Document Store. Nenne ihn meridian-knowledge und klicke auf Save.
### Schritt 3: Den ersten Document Loader hinzufügen
Klicke in den Store meridian-knowledge. Klicke auf + Add Document Loader.
Wähle aus den Loader-Optionen Text File aus. Lade meridian_operations.txt hoch.
Füge im Metadatenfeld Folgendes hinzu:
- Key: source
- Value: operations_handbook
### Schritt 4: Den Text Splitter konfigurieren
Wähle Recursive Character Text Splitter aus und konfiguriere:
[TABLE]
  | Einstellung | Wert |
  | Chunk Size | 1000 |
  | Chunk Overlap | 100 |
Klicke auf Preview, um zu bestätigen, dass das Dokument in sinnvolle Abschnitte aufgeteilt wird. Jeder Policy-Abschnitt sollte als eigener Chunk erscheinen. Wenn ein einzelner Abschnitt über mehrere Chunks hinweg geteilt wird, erhöhe die Chunk Size. Wenn zwei Abschnitte zu einem Chunk zusammengeführt werden, verringere sie. Passe in Schritten von 200 an, bis der Split sauber aussieht, und klicke dann auf Save.
### Schritt 5: Die verbleibenden zwei Dokumente hinzufügen
Wiederhole Schritte 3 und 4 für die verbleibenden zwei Dateien mit denselben Text-Splitter-Einstellungen:
Datei 2:
- Lade meridian_engagement_standards.txt hoch
- Metadaten-Key: source, Value: engagement_standards
Datei 3:
- Lade meridian_regional_playbook.txt hoch
- Metadaten-Key: source, Value: regional_playbook
Speichere jeden Document Loader, bevor du fortfährst.
### Schritt 6: Die Upsert-Einstellungen konfigurieren
Klicke im Document Store meridian-knowledge auf Upsert Configuration. Du siehst drei Karten: Embeddings, Vector Store und Record Manager. Konfiguriere jede davon der Reihe nach.
### Embeddings - Klicke auf die Karte Embeddings und wähle Google Gemini Embedding aus.
[TABLE]
  | Feld | Wert |
  | Connect Credential | Wähle dein gespeichertes Gemini-Credential aus |
  | Model Name | gemini-embedding-001 |
  | Task Type | RETRIEVAL_DOCUMENT |
Klicke auf Save.
> ⚠️ Wichtig: Der Model Name kann von dem hier abweichen. Das ist in Ordnung, solange es das Modell ist, das du bereits verwendet hast.

### Vector Store - Qdrant
Klicke auf die Karte Vector Store und wähle Qdrant aus.
[TABLE]
  | Feld | Wert |
  | Qdrant Server URL | http://192.168.x.x:6333 — verwende deine tatsächliche Wi-Fi-IPv4-Adresse |
  | Collection Name | meridian-knowledge |
  | Vector Dimension | 3072 |
  | Metric | Cosine |
  | Top K | 2 |
  | File Upload | Off |
  | Payload Indexes | Leer lassen |
Klicke auf Save.
> ⚠️ Warum deine Wi-Fi-IP und nicht der localhost: Flowise und Qdrant laufen als getrennte Docker-Container. Wenn Flowise versucht, eine Verbindung zu localhost herzustellen, sucht es in seinem eigenen Container, wo es kein Qdrant gibt. Die Wi-Fi-IPv4-Adresse deines Rechners ist über die Port-Mappings erreichbar, die beim Starten jedes Containers konfiguriert wurden.
> ⚠️ Warum 3072 Dimensionen: Das Modell gemini-embedding-001 erzeugt Vektoren mit 3072 Dimensionen. Die Vector Dimension in Qdrant muss genau zum Embedding-Modell passen. Eine Abweichung verursacht einen Dimensionsfehler, und der Upsert schlägt fehl. Auch hier gilt: Es ist in Ordnung, wenn das Modell ein anderes ist.

### Record Manager - SQLite
Klicke auf die Karte Record Manager und wähle SQLite Record Manager aus.
[TABLE]
  | Feld | Wert |
  | Table Name | record_manager_cache |
  | Namespace | meridian-knowledge |
  | Cleanup | Incremental |
  | SourceId Key | source |
Klicke auf Save.
> ⚠️ Warum SQLite: SQLite benötigt keine externe Datenbank und keinen zusätzlichen Docker-Container. Es speichert Chunk-Hash-Records in einer Datei innerhalb des bestehenden Flowise-Docker-Containers und ist damit die einfachste Wahl für ein selbst gehostetes Entwicklungs-Setup.
> ⚠️ Warum Incremental cleanup: Beim erneuten Upsert werden nur neue oder geänderte Chunks verarbeitet. Unveränderte Chunks werden übersprungen. Dadurch wird verhindert, dass sich doppelte Vektoren in Qdrant ansammeln, jedes Mal, wenn du ein Dokument aktualisierst und den Upsert erneut ausführst.

### Schritt 7: Die Dokumente “upserten”
Sobald alle drei Karten gespeichert sind, klicke auf Upsert. Flowise verarbeitet jedes Dokument automatisch durch die vollständige Pipeline:
1. In Chunks aufteilen mit den Text-Splitter-Einstellungen
1. Jeden Chunk mit Gemini gemini-embedding-001 embedden
1. Vektoren in Qdrant unter der Collection meridian-knowledge speichern
1. Den Hash jedes Chunks in der SQLite-Datenbank aufzeichnen
Nach Abschluss aktualisiert sich der Document-Store-Status und zeigt die Anzahl der gespeicherten Chunks an.
> ⚠️ Wenn du einen Dimension-Mismatch-Fehler erhältst: Das bedeutet, dass Qdrant die Collection bei einem früheren fehlgeschlagenen Versuch mit den falschen Dimensionen erstellt hat. So behebst du das:
  1. Öffne http://192.168.x.x:6333/dashboard in deinem Browser
  1. Finde die Collection meridian-knowledge und lösche sie
  1. Kehre zu Flowise zurück und klicke erneut auf Upsert

### Schritt 8: Die Wissensdatenbank überprüfen
Klicke auf Retrieval Query und führe die folgenden drei Test-Queries nacheinander aus:
[TABLE]
  | Query | Erwartete Quelle |
  | What are the project classification tiers at Meridian? | meridian_operations.txt  Abschnitt Project Classification |
  | How quickly must a severity level 2 issue be escalated? | meridian_engagement_standards.txt Abschnitt Severity Ratings |
  | What are Meridian's language guidelines for Poland? | meridian_regional_playbook.txt  Abschnitt Poland |
Bestätige für jede Query:
- Mindestens ein zurückgegebener Chunk enthält Inhalte, die für die Frage relevant sind
- Die Metadaten zeigen die richtige Quelldatei
> ⚠️ Hinweis zu den Ergebnissen: Bei kurzen synthetischen Dokumenten erzeugt jede Datei etwa zwei bis drei Chunks. Top K ist auf 2 eingestellt, sodass jede Abfrage die zwei semantisch ähnlichsten Chunks zurückgibt. Falls die Ergebnisse unpassend wirken, prüfe, ob der Upsert fehlerfrei abgeschlossen wurde und das richtige Embedding-Modell ausgewählt ist.

### Checkliste: Vor dem Fortfahren bestätigen
- [ ] Beide Container flowise und qdrant mit docker ps als laufend bestätigt
- [ ] Wi-Fi-IPv4-Adresse mit ipconfig bestätigt
- [ ] Qdrant erreichbar unter http://192.168.x.x:6333
- [ ] Document Store meridian-knowledge in Flowise erstellt
- [ ] Alle drei Dokumente mit korrekten Metadaten-Keys hochgeladen
- [ ] Recursive Character Text Splitter konfiguriert: Chunk Size 1000, Overlap 100
- [ ] Embeddings konfiguriert: gemini-embedding-001, Task Type RETRIEVAL_DOCUMENT, Gemini-Credential verbunden
- [ ] Qdrant konfiguriert: Wi-Fi-IP, Collection meridian-knowledge, Dimension 3072, Top K 2
- [ ] SQLite Record Manager konfiguriert: Table record_manager_cache, Namespace meridian-knowledge, Cleanup Incremental
- [ ] Upsert erfolgreich abgeschlossen: Chunk-Anzahl angezeigt
- [ ] Alle drei Retrieval-Test-Queries geben relevante Chunks zurück

> 💡 Takeaway: 
  Ein Document Store ist nur so nützlich wie die Sorgfalt, mit der er konfiguriert wird. Drei Entscheidungen während der Einrichtung (Chunk Size, Embedding-Modell und Vector Dimension) bestimmen direkt, ob Retrieval korrekt funktioniert, wenn der Agent es braucht.
  Die Wissensdatenbank mit Test-Queries zu überprüfen, bevor sie mit dem Canvas verbunden wird, bestätigt, dass die Pipeline end to end funktioniert und nicht nur technisch verbunden ist.