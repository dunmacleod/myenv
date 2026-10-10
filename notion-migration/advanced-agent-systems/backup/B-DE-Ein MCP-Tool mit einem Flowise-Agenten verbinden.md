# Ein MCP-Tool mit einem Flowise-Agenten verbinden

Notion page: https://app.notion.com/p/Ein-MCP-Tool-mit-einem-Flowise-Agenten-verbinden-4da9418319f383afbd138170b4ce228e
Backed up before n8n migration

Sofias Intake-Agent kann jetzt strukturierten Kontext übergeben, aber er kann noch kein externes System eigenständig erreichen. Um Kundenprobleme bei Cascadia tatsächlich zu lösen, braucht der Agent Tools, beginnend mit etwas Einfachem. In diesem Walkthrough verbindest du einen einzelnen MCP-Server mit einem Flowise-Agenten und prüfst, ob der Agent ihn korrekt entdecken und nutzen kann.
## Szenario
Sofia möchte sehen, dass das MCP-Integrationsmuster funktioniert, bevor sie Cascadias Geschäftssysteme anschließt. Sie richtet den kleinstmöglichen Test ein: einen Flowise-Agenten, einen MCP-Server, eine Anfrage, die das Tool erfordert. Wenn der Agent das Tool entdeckt, es aufruft und die Antwort verwendet, weiß sie, dass das Muster halten wird, wenn sie später echte Cascadia-Tools anschließt.
Nutz für diesen Walkthrough einen einfachen MCP-Server wie den Sequential Thinking MCP Server, der in deinem Flowise-Setup bereits verfügbar ist.
## Instructor-Walkthrough
### Schritt 1: Einen neuen Agentflow erstellen
Öffne Flowise und erstelle einen neuen Agentflow V2-Workflow. Füge einen Start-Node und ein Chat Input-Feld hinzu, falls deine Canvas diese noch nicht enthält.
![image]((notion-hosted file))
### Schritt 2: Einen Agent-Node hinzufügen
Füge einen Agent-Node hinzu und verbinde ihn mit dem Start-Node.
![image]((notion-hosted file))
Du kannst deinen Agenten zum Beispiel Agent with Sequential MCP nennen. Wähl das LLM deiner Wahl (Gemini oder Ollama) und nutz im System-Prompt (Add Message-Button):
> 💬 You are an IT support assistant.
  Your job is to answer the user’s request.
  When an MCP tool is useful, call the tool before answering.
  When no tool is needed, answer directly.
![image]((notion-hosted file))
Halt den Prompt einfach. Das Ziel ist zu zeigen, dass der Agent ein MCP-Tool nutzen kann.
---
### Schritt 3: Das MCP-Tool verbinden
Öffne in der Konfiguration des Agent-Node den Tool-Bereich und füg das verfügbare MCP-Tool bzw. den MCP-Server für Sequential Thinking hinzu:
![image]((notion-hosted file))
Wähl im Bereich Available actions die Option SEQUENTIAL THINKING.
![image]((notion-hosted file))
### Schritt 4: Tool Discovery testen
Speicher den Flow und führ ihn mit einem Prompt aus, der das MCP-Tool eindeutig erfordert. Nutz für Sequential Thinking MCP zum Beispiel:
> 💬 Break this problem into steps: I need to diagnose why a user cannot access their company email.
Der Agent sollte nicht nur aus dem Memory antworten. Er sollte das MCP-Tool aufrufen oder zeigen, dass er die verbundene Fähigkeit genutzt hat.
### Schritt 5: Das Ergebnis beobachten
![image]((notion-hosted file))
Öffne die Ausführungsdetails oder die Node-Ausführungsausgabe. Achte auf Folgendes:
- ob der Agent das MCP-Tool ausgewählt hat,
- welche Eingabe er an das Tool übergeben hat,
- welches Ergebnis zurückkam,
- wie die finale Antwort das Ergebnis verwendet hat.
Das ist der zentrale Lernmoment: MCP ist nur dann erfolgreich, wenn der Agent das Tool während des Workflows tatsächlich aufrufen kann.
## Häufige Fehlerstellen
[TABLE]
  | Problem | Was Lernende sehen | Wie man es behebt |
  | MCP-Tool erscheint nicht | Keine verfügbaren MCP-Aktionen in Flowise | Prüfen, ob der MCP-Server installiert ist, läuft und mit Flowise verbunden ist |
  | Agent ignoriert das Tool | Die Antwort erscheint, aber kein Tool-Aufruf ist sichtbar | Den Prompt expliziter machen und nach einer Aufgabe fragen, die das Tool erfordert |
  | Authentifizierung schlägt fehl | Tool-Aufruf gibt einen Auth-Fehler zurück | Zugriffstoken, Umgebungsvariablen oder Provider-Login prüfen |
  | Lokaler Server nicht verfügbar | Verbindungs- oder Timeout-Fehler | MCP-Server und Flowise-Container neu starten |
  | Falscher Node-Typ | Tool kann nicht angehängt werden | Einen Agent-Node verwenden, der Tools unterstützt, keinen einfachen LLM-Node |
## Gelöstes Referenzverhalten
Ein erfolgreicher Durchlauf sollte dieses Muster zeigen:
![image]((notion-hosted file))
Die genaue Ausgabe hängt vom MCP-Server ab, aber das Run Log sollte klar zeigen, dass das MCP-Tool aufgerufen wurde.
## Debrief-Perspektive
Der wichtige Unterschied liegt zwischen ein Tool konfiguriert haben und einen Agenten haben, der das Tool korrekt nutzt. Ein in Flowise gelistetes Tool ist nur potenzielle Fähigkeit. Der echte Test ist, ob der Agent es im richtigen Moment aufruft und das Ergebnis in der finalen Antwort verwendet.
## Zusammenfassung
Du hast ein MCP-Tool mit einem Flowise-Agenten verbunden und beobachtet, wie er es entdeckt, aufruft und das Ergebnis verwendet. Das ist das grundlegende Integrationsmuster hinter fortgeschritteneren Agentensystemen. In der nächsten Lektion betrachten wir, was passiert, wenn Sofias Agenten mit dem Agenten eines anderen Teams sprechen müssen: ein anderes Problem, das MCP allein nicht löst.