# Knowledge-, Routing- und Tool-Checkpoint

Notion page: https://app.notion.com/p/Knowledge-Routing-und-Tool-Checkpoint-3789418319f380bba119e61b67428cfc
Backed up before n8n migration

> 💡 Was diese Bewertung abdeckt: Du überprüfst, ob die drei Sprint-2-Fähigkeiten in einer einzelnen, durchgängigen Session korrekt zusammenarbeiten. Gleichzeitig stellst du eine klare Verbindung her zwischen dem, was du gebaut hast, und dem, was das finale Projekt erfordert.
## Wo wir stehen
Meridians Agentflow v2 ist von einer Drei-Node-Baseline zu einem wirklich fähigen Agenten gewachsen. Drei neue Fähigkeiten wurden in diesem Sprint erstellt, konfiguriert und isoliert getestet:
- Knowledge Retrieval: Der Document Store meridian-knowledge ist mit dem Agent Node A verbunden und gibt fundierte Antworten aus Meridians interner Dokumentation zurück
- Intent-basiertes Routing: Der Condition Agent Node klassifiziert Consultant-Queries nach Absicht und routet sie zum richtigen Pfad, bevor eine Abfrage oder ein API-Aufruf erfolgt
- Live-Datenzugriff: Der HTTP Node ruft externe Daten ab. Der Agent Node B formatiert diese anschließend in eine professionelle, natürliche Antwort.
Was noch nicht überprüft wurde, ist, ob alle drei in einer einzelnen kontinuierlichen Session korrekt zusammenarbeiten. Jede Fähigkeit wurde isoliert getestet. Eine einheitliche Session wurde noch nicht ausgeführt.
Dieser Checkpoint fordert dich auf, diese Session jetzt auszuführen, bevor Sprint 3 startet.
## Warum das für das finale Projekt wichtig ist
Das finale Projekt ist ein Agentflow v2, der alle relevanten Flowise-Features verwendet, die über die vier Sprints hinweg eingeführt wurden. Bis zum Ende von Sprint 3 wird der Agent Loops, Iteration, Human-Approval-Checkpoints und modulare Sub-Flows zusätzlich zu dem haben, was heute existiert.
Wenn die Sprint-2-Fähigkeiten nicht sauber zusammenarbeiten, lassen sich neu entstehende Probleme später nur schwer zurückverfolgen, sobald die Sprint-3-Komponenten darüber liegen. Ein Routing-Fehler lässt sich auf einem Canvas mit zwei Pfaden noch leicht finden. Derselbe Fehler vergraben in einem Ablauf mit Loops und Sub-Flows ist dagegen extrem schwer zu diagnostizieren.
Den Sprint-2-Build jetzt zu überprüfen, hält das finale Projekt debuggbar.
## Überblick
Bevor du mit dem Test loslegst: Geh kurz diese Liste durch und schau, ob du wirklich alle Skills am Start hast:
Canvas-Struktur:
[TABLE]
  | Komponente | Erwarteter Zustand |
  | Start Node | Flow State mit den Keys query_type und status_response initialisiert |
  | Condition Agent Node | Vom Start Node verbunden, zwei Szenarien definiert, Instructions-Feld ausgefüllt |
  | Agent Node A | Vom knowledge_query-Output verbunden, Document Store meridian-knowledge angehängt |
  | Direct Reply A | Mit Agent Node A verbunden, Message-Feld auf die Output-Variable von Agent Node A gesetzt |
  | HTTP Node | Vom status_request-Output verbunden, GET-Methode, JSONPlaceholder-URL, JSON Response Type |
  | Agent Node B | Mit HTTP Node verbunden, Formatting- und Failure-Recovery-Anweisungen in der System Message, kein Document Store |
  | Direct Reply B | Mit Agent Node B verbunden, Message-Feld auf die Output-Variable von Agent Node B gesetzt |
Wenn eine Komponente fehlt oder falsch konfiguriert ist, kehre zur relevanten Lektion zurück und korrigiere sie, bevor du den einheitlichen Test ausführst.
## Einheitlicher Session-Test
Öffne die Flowise-Chat-Oberfläche und führe alle sechs Austausche in einer einzigen Session aus, ohne den Chat zwischen den Turns zurückzusetzen oder zu schließen.
Austausch 1 - Knowledge Retrieval: What is Meridian's policy for submitting project close-out summaries after an engagement ends?
- Erwartet: Condition Agent Node routet zu Agent Node A. Agent Node A ruft den relevanten Chunk aus dem Document Store ab und antwortet aus den abgerufenen Inhalten. Der HTTP-Pfad wird nicht ausgelöst.
Austausch 2 - Kontextbeibehaltung nach Retrieval: How many working days does that give me if my engagement closed last Friday?
- Erwartet: Agent Node A verwendet Session-Kontext, um die Deadline aus Austausch 1 auf die spezifische Situation des Consultants anzuwenden, ohne den Document Store erneut abzufragen.
Austausch 3 - Live-Datenabfrage über HTTP Node: Can you check the current engagement status for account reference 1?
- Erwartet: Condition Agent Node routet zum HTTP-Pfad. HTTP Node ruft Daten von JSONPlaceholder ab. Agent Node B gibt dir eine professionelle Engagement-Zusammenfassung in natürlicher Sprache zurück.
Austausch 4 - Kontextbeibehaltung nach Tool-Nutzung: What was the name of the engagement you just retrieved?
- Erwartet: Agent Node B verwendet Session-Kontext, um den Engagement-Titel aus Austausch 3 abzurufen, ohne den HTTP Node erneut aufzurufen.
Austausch 5 - HTTP-Failure-Handling: Ändere vor diesem Austausch die Target URL des HTTP Nodes vorübergehend zu …
https://jsonplaceholder.typicode.com/invalid/endpoint/9999
Speichere den Canvas und sende dann: Can you check the status for the Bauer account?
- Erwartet: Agent Node B erkennt den Fehler ehrlich an, kommuniziert in einfacher Sprache, was passiert ist, und bietet einen klaren nächsten Schritt an, ohne einen Status zu erfinden.
Stelle nach diesem Austausch die HTTP-Node-URL wieder her auf: https://jsonplaceholder.typicode.com/todos/1
Austausch 6 - Out-of-Scope-Query: Can you give me a summary of Meridian's competitive positioning versus the major operations consultancies in Germany?
- Erwartet: Agent Node A erkennt die Query als außerhalb seines autorisierten Scopes und gibt die definierte Fallback-Formulierung mit einem konstruktiven nächsten Schritt aus.
### Deine Ergebnisse bewerten
Frage dich bei jedem Austausch:
- Hat der Condition Agent Node korrekt geroutet?
- Hat der richtige Agent Node geantwortet?
- War die Antwort in abgerufenen Inhalten oder formatierten API-Daten verankert und nicht aus allgemeinen Trainingsdaten erfunden?
- Wurde der Kontext aus dem vorherigen Turn korrekt beibehalten?
Wenn ein Austausch fehlschlägt, diagnostiziere ihn, bevor du zu Sprint 3 übergehst. Verwende Folgendes als ersten Diagnoseschritt:
[TABLE]
  | Symptom | Wahrscheinlichste Ursache |
  | Falscher Pfad vom Condition Agent Node ausgewählt | Instructions-Feld unterscheidet die zwei Szenarien nicht klar genug |
  | Agent Node A gibt generische Antwort statt abgerufener Inhalte zurück | Document Store nicht verbunden oder Describe-Knowledge-Feld zu vage |
  | Agent Node B erhält rohes JSON statt formatierter Antwort | User Message in Agent Node B referenziert nicht die richtige Variable |
  | Kontext zwischen Austauschen geht verloren | Memory ist auf dem relevanten Agent Node nicht aktiviert |
  | Agent Node B erfindet Status bei Fehler | System-Prompt enthält kein ausdrückliches Verbot von Fabrication |
### Wissensquiz

### Frage 1
>  Wie entscheidet der Condition Agent Node im Meridian Agentflow v2, über welchen Pfad eine Query geroutet wird?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a2d793da-1cdc-4491-bc73-4e23bc27a394

### Frage 2
>  Nachdem in Austausch 3 erfolgreich Engagement-Daten abgerufen wurden, ruft Agent Node B in Austausch 4 erneut den HTTP Node auf, statt Session-Kontext zu verwenden. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cf122919-e2a5-4017-b4ee-2676196127dc

### Frage 3
>  Welche zwei Komponenten bestimmen zusammen, ob der Meridian-Agent eine Query zum Document-Store-Pfad oder zum HTTP-Live-Datenpfad routet?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4f051afc-a81c-43ea-8031-35ebfba3286c

### Frage 4
>  Der Agent Node B erhält einen Netzwerkfehler vom HTTP Node und antwortet mit einem erfundenen Engagement-Status. Welche zwei Änderungen würden diesen Fehler am direktesten adressieren?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/6bfb0274-91f2-419d-87df-591fb169f478

### Sprint 2 mit Sprint 3 verbinden
Der Sprint 2 hat Agentflow v2 entscheidende Fähigkeiten verliehen: Der Agent erkennt, was ein Consultant benötigt, ruft die passenden Informationen ab und liefert eine fundierte Antwort. Sprint 3 ergänzt die Orchestrierung: die Steuerung komplexer Multi-Step-Logik, automatische Retry-Mechanismen bei Fehlern, iterative Datenverarbeitung, Pausen für menschliche Freigaben und das Aufrufen von Sub-Flows als modulare Bausteine.
Die sämtliche Logik aus Sprint 3 baut direkt auf dem Sprint-2-Canvas auf. Die Node-Anzahl steigt, die Ausführungspfade werden komplexer und der Flow State führt mehr Variablen über mehrere Schritte hinweg.
Ein Agent, der diesen Checkpoint fehlerfrei besteht, ist bereit für die nächsten Schritte. Bestehen jedoch weiterhin Routing-Fehler, Memory-Lücken oder Halluzinationen, verstärken sich diese Probleme mit wachsender Canvas-Komplexität.
Behebe daher alle Fehler aus dem einheitlichen Session-Test, bevor du mit Sprint 3 fortfährst.