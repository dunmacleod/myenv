# Retry-Logik mit dem Loop Node

Notion page: https://app.notion.com/p/Retry-Logik-mit-dem-Loop-Node-3789418319f3804f8a01ee1f4b704345
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du fügst dem Meridian-Agentflow-v2 einen Loop Node hinzu, der HTTP-Fehler mit automatischer Retry-Logik und einem kontrollierten Exit Path behandelt.

## Ausgangslage
Meridians HTTP Node auf Path B nimmt aktuell jede Antwort entgegen, egal ob Erfolg oder Fehler. Ist die Engagement-Status-API kurzzeitig nicht erreichbar, gibt Agent Node B eine Fallback-Nachricht aus, und der Consultant muss es von Hand erneut versuchen. Bei einem Tool, das über den Arbeitstag hinweg häufig genutzt wird, ist das eine Reibung, die das Entwicklungsteam beseitigen will.
Die Lösung ist eine Retry-Logik, bei der der HTTP Call automatisch mehrfach wiederholt wird, bevor ein Fallback greift. Mit dem Loop Node lassen sich Zyklen oder iterative Retries innerhalb eines Workflows abbilden. Erreicht die Execution den Loop Node, leitet er zur angegebenen Ziel-Node zurück, die schon früher im aktuellen Run gelaufen ist. Dadurch läuft dieser Teil des Flows erneut, inklusive aller nachfolgenden Nodes.
## Was du hinzufügst
Du aktualisierst Path B so, dass der HTTP Node bei einem Fehler der API bis zu zwei Mal erneut versucht, bevor er zu einem Fallback Direct Reply Node weiterleitet. Der Success Path umgeht die Retry-Logik vollständig und geht direkt zu Agent Node B für die Formatierung.
> ⚠️ Bevor du beginnst, stelle sicher, dass du Docker Desktop öffnest. Aktiviere unter Actions Flowise und Qdrant.

### Schritt 1: Den Condition Agent Node aktualisieren
Bevor du die Retry-Logik hinzufügst, braucht der Condition Agent Node zwei Updates, damit das Routing zuverlässig funktioniert.
Scenario-Reihenfolge:
- Scenario 0: status_request
- Scenario 1: knowledge_query
Outputs neu verbinden:
- Output 0 → HTTP Node
- Output 1 → Agent Node A
Ersetze das Instructions-Feld durch Folgendes:
> You are a query classifier for Meridian Consulting's internal agent.
  Classify the input as "status_request" FIRST if it contains any of these signals:
  - asks to "check", "look up", "retrieve", or "pull up"
  - mentions "account", "account number", or "account reference"
  - asks for current status of a specific project or client
  Classify as "knowledge_query" only if none of the above apply. Default to "status_request" when uncertain.
Bestätige diese Einstellungen:
- Input: {{ $flow.input }} manuell eingetippt, nicht aus dem Dropdown ausgewählt
- Memory: Off
Speichere den Canvas.
### Schritt 2: Einen Retry Counter zu Flow State hinzufügen
Klicke auf den Start Node und wähle + Add Flow State. Gib Folgendes ein:
- Key: retry_count
- Initial value: 0
### Schritt 3: Condition Node nach dem HTTP Node hinzufügen
Füge direkt nach dem HTTP Node auf Path B einen Condition Node hinzu. Verbinde den HTTP Node output mit dem Condition input.
Konfiguriere Condition A:
[TABLE]
  | Field | Value |
  | Type | String |
  | Value 1 | {{ httpAgentflow_0.data }} |
  | Operation | Is Empty |
Das prüft, ob die HTTP Response Daten enthält, bevor der Flow den nächsten Path festlegt.
- Output 0 (true: data is empty, HTTP failed): Mit dem Custom Function Node verbinden
- Output 1 (false: data exists, HTTP succeeded): Mit dem Agent 2 Node verbinden
### Schritt 4: Einen Custom Function Node nach Condition A hinzufügen
Klicke auf (+) und füge einen Custom Function Node auf dem Failure Branch von Condition A hinzu. Verbinde Condition A output 0 (den Empty/Failed Branch, den du in Schritt 3 verbunden hast) mit dem Input des Custom Function Nodes. Der Custom Function Node läuft nur, wenn der HTTP Call keine Daten zurückgegeben hat. Das ist der einzige Fall, in dem der Retry Counter erhöht werden soll.
![image]((notion-hosted file))
Konfiguriere ihn wie folgt:
Input Variables:
![image]((notion-hosted file))
JavaScript Function:
```javascript
const count = parseInt($retryCount) || 0;
return String(count + 1);
```
Update Flow State:
![image]((notion-hosted file))
Das erhöht den Retry Counter jedes Mal, wenn der HTTP Call versucht wird.
### Schritt 5: Einen Condition Node hinzufügen, um den Retry Count zu prüfen
Füge nach dem Custom Function Node einen Condition Node hinzu.
Konfiguriere ihn:
![image]((notion-hosted file))
Das bewertet, ob der Retry Count 2 überschritten hat.
- Output 0 (true: retry count exceeds 2): Mit Direct Reply C verbinden
- Output 1 (false: retry count is 2 or below): Mit dem Loop Node verbinden
### Schritt 6: Direct Reply C hinzufügen
Füge einen Direct Reply Node hinzu, der mit Condition B output 0 verbunden ist.
Gib in das Message-Feld Folgendes ein:
> The engagement status service is currently unavailable. Please contact your engagement manager directly for current project status.
### Schritt 7: Den Loop Node hinzufügen
Füge einen Loop Node hinzu, der mit Condition B output 1 verbunden ist. Konfiguriere ihn:
[TABLE]
  | Field | Value |
  | Loop Back To | Den HTTP Node auswählen |
  | Max Loop Count | 2 |
Der Loop Node hat standardmäßig keinen vorwärtsgerichteten Output Anchor. Seine Hauptaufgabe ist es, den Execution Flow rückwärts zum Loop-Back-Ziel-Node umzuleiten.
### Schritt 8: Agent Node B und Direct Reply B verbinden
Verbinde Condition A output 1 mit dem Agent 2 Node. Bestätige, dass der Agent 2 Node mit deinem Gemini-Modell, System Message und ohne verbundenen Document Store konfiguriert ist.
Verbinde den Agent 2 node output mit dem Direct Reply B Node. Tippe im Message-Feld von Direct Reply B {{ ein und wähle die Output-Variable von Agent Node B aus dem Dropdown aus.
### So sieht das komplette Diagramm aus
![image]((notion-hosted file))

### Schritt 9: Die Retry-Logik testen
Test 1: API-Fehler simulieren
Ändere die HTTP-Node-URL zu einem ungültigen Endpoint: https://jsonplaceholder.typicode.com/invalid/9999
- Speichere und sende: Can you check the engagement status for account 1?
- Erwartet: Der Flow versucht es zweimal erneut und routet dann zum Fallback Direct Reply.
Test 2: Erfolgspfad nach der Wiederherstellung bestätigen
Stelle die URL wieder her auf https://jsonplaceholder.typicode.com/todos/1
- Sende dieselbe Query.
- Erwartet: HTTP Node ist beim ersten Versuch erfolgreich und Agent Node B gibt eine formatierte Statusantwort zurück.

> 💡 Fazit:
  Der Loop Node macht Meridians Canvas widerstandsfähiger, weil er transiente Fehler automatisch abfängt. Der Loop Node übernimmt die Rückwärtsumleitung, der Condition Node übernimmt den Exit. Das ist das zentrale Designprinzip. Jeder Loop braucht beides.
