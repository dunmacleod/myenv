# Den Baseline-Projektagenten erweitern

Notion page: https://app.notion.com/p/Den-Baseline-Projektagenten-erweitern-ac39418319f3825382e9014394a3f1ab
Backed up before n8n migration

Der Baseline-Projektagent nutzt bereits ein MCP-verbundenes arXiv-Tool, um nach Research Papers zu suchen. In dieser Übung erweiterst du diesen Flow so, dass das System Papers nicht nur abruft, sondern dem User auch hilft zu verstehen, was er zuerst lesen sollte und warum.
Der neue Flow sollte so aussehen:

![image]((notion-hosted file))

Beachte, dass der Summary Agent nur ausgeführt wird, wenn die Suche erfolgreich abgeschlossen wurde.
## Deine Aufgabe
Modifiziere den bestehenden Workflow, indem du den Branch To_User_Chat um einen neuen Research Summary Agent erweiterst.
Der neue Agent sollte die erfolgreichen Suchergebnisse erhalten und sie in eine strukturierte Antwort umwandeln.
## Schritt 1: Den gesunden Ausführungspfad finden
Öffne deinen bestehenden Workflow.
Finde den Node Evaluate Network State.
Suche den Branch mit der Bezeichnung:
```plain text
To_User_Chat
```
Im Moment endet dieser Branch damit, dass die Suchergebnisse an den User zurückgegeben werden.
Das ist der Teil des Workflows, den du erweitern wirst.
## Schritt 2: Die Zusammenfassungsaufgabe an einen Research Summary Agent delegieren
Sobald der Workflow bestätigt hat, dass die arXiv-Suche erfolgreich war, soll der Search Agent die abgerufenen Papers an einen spezialisierten Research Summary Agent weitergeben. Dieser Agent sucht nicht erneut. Er organisiert und fasst die Ergebnisse zusammen und gibt sie dann an den Search Agent zurück.
Verbinde einen neuen Agent Node nach dem Branch To_User_Chat.
Nenne ihn:
```plain text
Research Summary Agent
```
Dieser Agent sollte keine weitere Suche durchführen.
Seine einzige Verantwortung ist es, die Papers zu organisieren, die bereits vom arXiv Search Agent abgerufen wurden.
## Schritt 3: Den Agenten-Handoff konfigurieren
> ☝ Konfiguriere den Workflow so, dass der Search Agent die abgerufenen Papers nach dem gesunden Branch des Workflows an den Research Summary Agent übergibt. Der Summary Agent sollte den Konversationsverlauf und die Paper-Ergebnisse erhalten, seine Aufgabe abschließen und die strukturierte Antwort an den Search Agent zurückgeben.
Füge einen System-Prompt hinzu:
Du bist der Research Summary Agent.
Der Search Agent hat bereits eine erfolgreiche arXiv-Suche abgeschlossen und delegiert die Zusammenfassungsaufgabe an dich.
Deine Verantwortlichkeiten sind:
- nur die Papers zu analysieren, die du erhältst
- eine logische Lesereihenfolge zu empfehlen
- eine kurze Research-Zusammenfassung zu erstellen
Führe keine weitere Suche durch.
Antworte nicht direkt dem User.
Gib deine Arbeit als gültiges JSON an den Search Agent zurück.
```json
{ "topic": "string", 
 "order_of_reading_papers": [ "paper title", "paper title", "paper title" ], 
 "summary": "One paragraph summarizing the research area 
						 and explaining why the papers are ordered this way." }
```
Regeln:
- Führe keine weitere Suche durch.
  - Erfinde keine Papers.
- Empfiehl eine logische Lesereihenfolge, beginnend mit dem einführendsten Paper.
- Gib nur ein gültiges JSON zurück.
> ☝ Du kannst auch direkt einen JSON-Output zu deinem Agenten hinzufügen. Das hilft sicherzustellen, dass der Flow konsistent ist.
## Schritt 4: Testen der Zusammenarbeit der Agenten
Führe den Workflow mit einer Anfrage wie dieser aus:
```plain text
Find papers about resilient multi-agent orchestration.
```
Prüfe, ob sich der Workflow korrekt verhält.
Wenn die Suche scheitert, sollte der Retry Loop genau wie zuvor weiter funktionieren.
Wenn die Suche erfolgreich ist, sollte der Workflow zum Research Summary Agent weiterlaufen, der einen Output ähnlich diesem zurückgeben sollte:
```json
{ "topic": "Resilient Multi-Agent Orchestration", 
	"order_of_reading_papers": [ "...", "...", "..." ], 
	"summary": "..." }
```
## Prüfe deine Arbeit
Bevor du abschließt, bestätige Folgendes:
- Der Retry Loop funktioniert weiterhin genau wie zuvor.
- Fehlgeschlagene Suchen erreichen den Summary Agent nie.
- Der Summary Agent verarbeitet nur erfolgreiche Suchergebnisse.
- Die finale Antwort ist gültiges JSON.
- Die Lesereihenfolge ist logisch statt zufällig.
## Zusammenfassung
Du hast den gesunden Ausführungspfad deiner Orchestrierung erweitert. Die Resilienzlogik hast du dabei nicht verändert. Der arXiv Search Agent bleibt weiterhin für das Abrufen der Papers zuständig. Der Research Summary Agent wandelt erfolgreiche Suchergebnisse in ein strukturiertes Research Briefing um. Diese Aufteilung ist ein gängiges Orchestrierungsmuster: Jeder Agent übernimmt eine fokussierte Aufgabe, und der Workflow steuert, wann welcher Agent zum Einsatz kommt.
