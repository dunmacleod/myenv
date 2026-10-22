# Orchestration Checkpoint

Notion page: https://app.notion.com/p/Orchestration-Checkpoint-3829418319f3801fa6a2de246ce16d65
Backed up before n8n migration

> 💡 Worum es hier geht: Du überprüfst, dass die Sprint-3-Orchestrierungsfunktionen sauber zusammenspielen und dass die Canvas in einem verifizierten Zustand ist, bevor Sprint 4 startet.

## Wo wir stehen
Der Meridian Agentflow v2 verfügt jetzt über vollständige Orchestration-Fähigkeiten, die auf die Sprint-2-Intelligence-Grundlage aufgesetzt wurden, mit der Fertigstellung oder dem Wissen über die folgenden Nodes:
- Loop Node: Retry-Logik für transiente HTTP-Fehler mit kontrolliertem Exit Path
- Iteration Node: Verarbeitung von Collections von Engagement Records in einer einzigen Execution
- Human Input Node: Approval Checkpoint, bevor sensitive Engagement-Daten angezeigt werden
- Execute Flow Node: Modularer Sub-Flow-Aufruf für wiederverwendbare Logik
- Custom Function Node: Custom JavaScript für Transformationen, die kein Standard-Node verarbeitet
- MCP: Universeller Standard, um Agenten frameworkübergreifend mit externen Tools zu verbinden
## Canvas Verification Checklist
Arbeite jeden Punkt durch, bevor du den Unified Test ausführst. Überspringe keine Punkte, denn die häufigsten Fehler in Sprint 3 können von grundlegenden Fehlern wie falsch geschriebenen Keys oder falschen Verbindungen kommen.
## Wo wir stehen
Der Meridian-Agentflow-v2 verfügt jetzt über volle Orchestrierungsfähigkeiten, aufbauend auf dem Intelligence-Fundament aus Sprint 2. Vorausgesetzt sind die folgenden Nodes, entweder abgeschlossen oder zumindest inhaltlich bekannt:
- Loop Node: Retry-Logik für transiente HTTP-Fehler mit einem kontrollierten Exit-Pfad
- Iteration Node: Verarbeitung von Sammlungen aus Engagement-Records in einem einzigen Durchlauf
- Human Input Node: Freigabe-Checkpoint, bevor sensible Engagement-Daten ausgegeben werden
- Execute Flow Node: Modularer Aufruf von Sub-Flows für wiederverwendbare Logik
- Custom Function Node: Eigener JavaScript-Code für Transformationen, die kein Standard-Node übernimmt
- MCP: Universeller Standard, um Agenten frameworkübergreifend mit externen Tools zu verbinden
## Canvas-Verifizierungscheckliste
Geh jeden Punkt durch, bevor du den Gesamttest startest. Überspring nichts, denn die häufigsten Fehler in Sprint 3 entstehen aus simplen Dingen wie falsch geschriebenen Keys oder falschen Verbindungen.
> ⚠️ Bitte beachte, dass diese Liste zwar umfangreich ist, du aber auch auf vorherige Lektionen zurückgreifen kannst, um sicherzustellen, dass dein Agent korrekt konfiguriert ist.

Start Node
- [ ] Flow State enthält alle diese Keys mit korrekten Initialwerten:
[TABLE]
  | Key | Initialwert |
  | query_type | knowledge |
  | routing_decision | `` |
  | status_response | `` |
  | retry_count | 0 |
  | engagement_list | [{"id":1,"title":"Krauss Manufacturing","completed":false},{"id":2,"title":"Bauer Logistics","completed":true},{"id":3,"title":"Novak Retail","completed":false}] |
  | briefing_output | `` |
  | approval_status | `` |
- [ ] Input Type: Chat Input
- [ ] Ephemeral Memory: Off
- [ ] Mit Condition Node verbunden

Condition Agent Node (top-level routing)
- [ ] Input: {{ $flow.input }} , manuell eingegeben, nicht aus dem Dropdown ausgewählt
- [ ] Vom Start Node verbunden
> ⚠️ Löst sich {{ $flow.input }} nicht korrekt auf, setze Value 1 vorübergehend auf eine feste Testphrase wie generate the weekly engagement briefing. Damit prüfst du, ob die Keyword-Prüfung funktioniert. Stelle danach {{ $flow.input }} wieder her.

Condition Agent Node
- [ ] Model: Gemini-Modell und API-Credential verbunden
- [ ] Memory: Off
- [ ] Input: {{ $flow.input }} , manuell eingegeben, nicht aus dem Dropdown ausgewählt
- [ ] Scenario 0: status_request → Output 0 → HTTP Node
- [ ] Scenario 1: knowledge_query → Output 1 → Agent Node A
- [ ] Instructions enthalten einen expliziten Default zu status_request bei Unsicherheit
> ⚠️ Die Reihenfolge der Scenarios ist entscheidend. status_request muss Scenario 0 sein. Steht stattdessen knowledge_query auf Scenario 0, springt der Condition Agent Node bei mehrdeutigen Anfragen standardmäßig auf den Knowledge-Pfad.

HTTP Node (Path B)
- [ ] Method: GET
- [ ] URL: https://jsonplaceholder.typicode.com/todos/1  bestätige, dass dies NICHT die Test-Failure-URL ist
- [ ] Response Type: JSON
- [ ] Von Condition Agent Node output 0 verbunden

Condition A
- [ ] Type: String
- [ ] Value 1: {{ httpAgentflow_0.data }}
- [ ] Operation: Is Empty
- [ ] Output 0 (true — empty — HTTP failed) → Custom Function Node
- [ ] Output 1 (false — not empty — HTTP succeeded) → Human Input Node
> ⚠️ Je nachdem, an welchem Szenario du gerade arbeitest, müssen diese Outputs eventuell getauscht werden. Output 0 schlägt an, wenn die Condition true ist. Das heißt, die Daten sind leer, und das ist der Failure-Pfad. Output 1 schlägt an, wenn Daten vorhanden sind, das ist der Success-Pfad.

Human Input Node
- [ ] Description Type: Fixed
- [ ] Description enthält {{ httpAgentflow_0.data }}
- [ ] Feedback: On
- [ ] Proceed output → Agent Node B
- [ ] Reject output → Direct Reply mit Reject-Nachricht
- [ ] Von Condition A output 1 verbunden
Custom Function Node
- [ ] Input Variable: retryCount = {{ $flow.state.retry_count }}
- [ ] JavaScript gibt String(count + 1) zurück
- [ ] Update Flow State: retry_count = {{ customFunctionAgentflow_0.output }}
- [ ] Von Condition A output 0 verbunden
Condition B
- [ ] Type: Number
- [ ] Value 1: {{ $flow.state.retry_count }}
- [ ] Operation: larger
- [ ] Value 2: 2
- [ ] Output 0 (true — retries exceeded) → Direct Reply C
- [ ] Output 1 (false — retry available) → Loop Node
Loop Node
- [ ] Loop Back To: HTTP Node
- [ ] Max Loop Count: 2
- [ ] Von Condition B output 1 verbunden
Direct Reply C
- [ ] Message: Fallback-Text darüber, dass der Service nicht verfügbar ist
- [ ] Von Condition B output 0 verbunden
Agent Node A
- [ ] Model: Gemini 2.5 Flash mit gespeicherter Credential
- [ ] System message: vollständiger vierteiliger System Prompt
- [ ] meridian-knowledge Document Store verbunden
- [ ] Von Condition Agent Node output 1 verbunden
Direct Reply A
- [ ] Message: {{ agentAgentflow_0.output }}  bestätigen, dass der .outputSuffix vorhanden ist
- [ ] Von Agent Node A verbunden
Agent Node B
- [ ] Model: Gemini 2.5 Flash mit gespeicherter Credential
- [ ] System message: Formatting- und Failure-Recovery-Instructions
- [ ] Kein Document Store verbunden
- [ ] Vom Proceed output des Human Input Nodes verbunden
Direct Reply B
- [ ] Message: Output-Variable von Agent Node B mit .outputSuffix
- [ ] Von Agent Node B verbunden
Docker-Konfiguration
- [ ] Beide Container laufen, prüfbar mit docker ps
- [ ] Flowise mit HTTP_SECURITY_CHECK=false gestartet, wenn Execute Flow Node verwendet wurde
- [ ] Qdrant läuft unter http://192.168.x.x:6333
![image]((notion-hosted file))

## Session Test
Führe alle fünf Exchanges in einer einzigen Session aus, ohne zwischen den Turns zurückzusetzen.
### Exchange 1 - Knowledge Retrieval
- What is Meridian's escalation procedure for a severity level 2 issue?
- Erwartet: Condition Node → Condition Agent → Agent Node A → Direct Reply A mit Policy-Inhalt.
### Exchange 2 - Status Anfrage mit Human Input
- Can you check the engagement status for account 1?
- Erwartet: Condition Agent → HTTP Node → Condition A → Human Input Node pausiert und zeigt Daten an. Klicke auf Proceed. Agent Node B formatiert Response → Direct Reply B.
### Exchange 3 - Die Freigabe ablehnen
- Öffne eine neue Session. Sende dieselbe Status-Query. Klicke diesmal im Human Input Node auf Reject.
- Erwartet: Direct Reply gibt die Ablehnungsnachricht zurück, ohne dass Agent Node B ausgeführt wird.
### Exchange 4 - Retry-Logik
- Ändere die URL des HTTP Nodes vorübergehend auf: https://jsonplaceholder.typicode.com/invalid/9999
- Sende: Can you check the engagement status for the Krauss account?
- Erwartet: HTTP Node schlägt fehl → Custom Function inkrementiert Counter → nach 2 Retries → Direct Reply C mit Fallback-Nachricht.
- Stelle die URL wieder her zu: https://jsonplaceholder.typicode.com/todos/1
### Exchange 5 - Engagement Briefing
- Öffne eine neue Session und sende: Can you generate the weekly engagement briefing?
- Erwartet: Condition Node erkennt "briefing" → routet zum Execute Flow Node oder Briefing Path → gibt Engagement Summaries zurück.
## Diagnose-Tabelle
Schlägt ein Exchange fehl, findest du hier schnell die Ursache:
[TABLE]
  | Symptom | Wahrscheinlichste Ursache |
  | Alle Queries gehen zu Agent Node A | Condition Node ist nicht mit Start Node verbunden |
  | Status Request geht zu Agent Node A | Condition Agent Node Memory ist eingeschaltet; ausschalten |
  | Human Input Node erscheint nicht | Edge von Condition A output 1 fehlt |
  | Retry Loop beendet sich nie | Exit Path von Condition B ist nicht mit Direct Reply C verbunden |
  | Briefing geht zu Agent Node A | Condition Node Value 2 Feld hat einen Tippfehler oder zusätzliches Leerzeichen |
## Wissens-Quiz
### Frage 1 
>  Der Loop Node in Meridians Canvas hat Max Loop Count auf 2 gesetzt und leitet zurück zum HTTP Node. Der HTTP Node schlägt bei jedem Versuch fehl. Was passiert nach dem zweiten Retry?

  [EMBED] https://app.masterschool.com/campus/multi-choice-question/ddc37ddf-d184-4eec-bc6c-af814a03ac97

### Frage 2 
>  Der Human Input Node ist zwischen Condition A output 1 und Agent Node B platziert. Ein Consultant klickt auf Proceed. Was passiert als Nächstes?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/819ba9da-c37f-4d3f-86d4-d7637f5a6d3f

### Frage 3
>  Ein Custom Function Node gibt JSON.stringify(dataArray) zurück, wobei dataArray drei Engagement Records enthält. Was erhält der Downstream Condition Node?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/5b23400e-f177-44bf-838a-d11b39c9ed95

### Frage 4
>  Meridian baut einen MCP Server, der seinen Document Store bereitstellt. Eine Kundenorganisation, die Langflow verwendet, möchte dieselbe Wissensdatenbank abfragen. Was muss sie dafür tun?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/9223997d-6ed9-49d4-a9b0-942b470a4377

### Von Sprint 3 zu Sprint 4
Sprint 3 hat dem Agentflow v2 mehr Orchestrierungstiefe gegeben, etwa Loops für Resilienz, Iteration für Skalierung, menschliche Checkpoints für Governance und modulare Sub-Flows für Wartbarkeit. Die Canvas ist jetzt ein wirklich leistungsfähiges System.
In Sprint 4 geht es darum, das Bestehende produktionsreif zu machen. Dazu gehören End-to-End-Tests, System-Prompt-Feinschliff, Dokumentation und die Vorbereitung der Präsentation. Der Agent, der diesen Checkpoint sauber besteht, ist bereit für diese letzte Phase.