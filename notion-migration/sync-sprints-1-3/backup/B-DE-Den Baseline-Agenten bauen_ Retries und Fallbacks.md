# Den Baseline-Agenten bauen: Retries und Fallbacks

Notion page: https://app.notion.com/p/Den-Baseline-Agenten-bauen-Retries-und-Fallbacks-a739418319f382bab89c81ce377a5b07
Backed up before n8n migration

> 🎯 Was du hier baust, ist die Baseline für das Sprint-4-Projekt. Am Ende dieses Walkthroughs enthält dein Flowise-Workspace den arXiv-Agenten, den Sprint 4 erweitert, evaluiert und debuggt. Speichere den Workflow.
Halcyon Labs möchte das IT-Support-System, das du in Sprint 1 entworfen hast, jetzt um eine Research-Retrieval-Fähigkeit erweitern: einen Agenten, der arXiv abfragt und Papers an interne Researcher zurückgibt. In dieser Lektion baust du genau diese Fähigkeit. Ab diesem Punkt wechselst du davon, Sofia beim Aufbau von Cascadias Support-Automatisierung als Lehrbeispiel zuzusehen, hin zum Bau deiner eigenen Projektabgabe — dem arXiv-Agenten, den Halcyon Labs braucht. Der arXiv-MCP-Server ist real und öffentlich, seine API läuft manchmal in Rate Limits oder Timeouts, und das Retrieve-then-Summarise-Pattern ist klein genug, um es in einem Walkthrough zu bauen, und real genug, um auf interessante Weise zu scheitern — genau die Bedingungen, für die die Resilienz-Patterns in diesem Sprint entworfen wurden.
Externe Tools antworten nicht immer erfolgreich. Ein MCP-Server kann durch Rate Limiting eingeschränkt, nicht verfügbar oder langsam sein. In einem Agenten-Workflow soll nicht jeder temporäre Fehler sofort zu einer fehlgeschlagenen User Experience werden. Ein Retry-Pattern gibt dem System eine zweite Chance, behält aber trotzdem die Kontrolle darüber, wie oft es versucht.
Halcyon Labs möchte das IT-Support-System aus Sprint 1 nun um eine Recherche-Komponente erweitern: einen Agenten, der arXiv nach wissenschaftlichen Arbeiten durchsucht und die Ergebnisse an das interne Research-Team weitergibt. In dieser Lektion entwickelst du genau diese Funktion. Damit wechselst du von der passiven Rolle, in der du Sofia beim Aufbau von Cascadias Support-Automatisierung über die Schulter geschaut hast, zur aktiven Umsetzung deiner eigenen Projektabgabe.
Der arXiv-MCP-Server ist real und öffentlich zugänglich; seine API stößt gelegentlich an Rate Limits oder läuft in Timeouts. Das Retrieve-then-Summarize-Muster ist kompakt genug für einen angeleiteten Walkthrough, bietet aber gleichzeitig genügend Praxisnähe, um auf unerwartete Weise fehlzuschlagen. Das sind exakt die Bedingungen, für die die Resilienz-Muster dieses Sprints konzipiert wurden. Externe Tools antworten schließlich nicht immer zuverlässig. Ein MCP-Server kann gedrosselt, temporär nicht verfügbar oder schlicht langsam sein. Innerhalb eines Agenten-Workflows sollte ein solcher vorübergehender Fehler jedoch nicht sofort das gesamte Nutzererlebnis ruinieren. Ein Retry-Muster ermöglicht dem System einen automatischen Neustart, behält dabei aber stets die strikte Kontrolle über die Anzahl der Versuche.
## Was du baust
In diesem Walkthrough baust du einen arXiv-Research-Agenten, der versucht, wissenschaftliche Papers über ein arXiv-MCP-Tool zu suchen.
Der Workflow wird:
1. eine User-Anfrage erhalten.
1. den arXiv-Agenten bitten, nach Papers zu suchen.
1. den Agenten-Output auf temporäre Fehlersignale parsen.
1. wenn die Suche funktioniert hat, das Ergebnis an den User zurückgeben.
1. wenn die Suche auf einen temporären Fehler stößt, denselben Schritt erneut versuchen.
1. nach Erreichen der maximalen Loop-Anzahl mit den Retries aufhören.
1. eine Fallback-Antwort hinzufügen.
# Workflow-Struktur
```plain text
Start
  ↓
Arxiv MCP Engine
  ↓
Parse Status & Errors
  ↓
Evaluate Network State
  ├── To_User_Chat → Direct Reply
  └── Trigger_Loop → Retry Counter Loop
                          │
                          ├── Retry Available → Arxiv MCP Engine
                          │
                          └── Max Retries Reached → Fallback Reply
```
> ☝ Die wichtige Idee ist, dass der Workflow nicht jeden Fehler blind erneut versucht. Er versucht nur dann erneut, wenn der geparste Output auf ein temporäres Problem hindeutet, zum Beispiel ein Rate Limit oder Service-Nichtverfügbarkeit.
## Schritt 1: Den arXiv-Agenten erstellen
Erstelle im Agentflows-Tab ein neues Arbeitsblatt und nenne es Arxiv Agent.
Erstelle einen Agent Node namens Arxiv MCP Engine.
Nutze das Modell Gemini Flash Lite und verbinde das arXiv-MCP-Tool.
Die Aufgabe des Agenten ist einfach: arXiv durchsuchen und nützliche Paper-Informationen an den User zurückgeben.
Füge einen System-Prompt hinzu:
```plain text
You are an expert Research Assistant Agent specializing in fetching, analyzing, and synthesizing scientific papers from arXiv using the provided Model Context Protocol (MCP) tools.

Your primary objective is to answer user queries with accurate, up-to-date academic context.

OPERATIONAL INSTRUCTIONS:


Always translate the user's research query into precise, well-formatted keywords before calling the search_papers or get_details tools.

If a query returns multiple papers, select the most relevant ones and synthesize their findings. Do not just list them blindly.

CRITICAL: TRANSIENT ERROR & RATE LIMIT HANDLING:

The arXiv API enforces strict rate limits. If you receive an error message from a tool execution containing "429", "Rate Limit", "Too Many Requests", or "503 Service Unavailable", you must immediately stop trying alternative tools and output the exact phrase: "Error: 429 Rate limit exceeded by arXiv." 

Do not attempt to guess or hallucinate data if a tool fails. Outputting this exact error string allows the orchestration system to safely trigger a workflow retry loop on your behalf.

FINAL ANSWER FORMATTING rules:

When presenting the final answer to the user, DO NOT output raw JSON, tool parameters, or programming code.
Write your response in clear, concise, professional academic markdown.
Structure your answer with clear headings, bullet points for key findings, and include the paper titles alongside their authors and publication years.


```
![image]((notion-hosted file))
# Schritt 2: Eine Parser-Funktion hinzufügen
Füge nach dem arXiv-Agenten einen Custom Function Node hinzu.
Nenne ihn Parse Status & Errors
// Grab the textual response from the agent trying to query arXiv
const assistantResponse = $input.text || "";
// Detect if arXiv rate-limited the agent or dropped the connection
if (assistantResponse.includes("429") ||
assistantResponse.includes("Rate limit") ||
assistantResponse.includes("503 Service Unavailable")) {
```plain text
return "Trigger_Loop"; // Matches the path leading to the Loop Node
```
} else {
return "To_User_Chat"; // Matches the path completing the workflow
}
![image]((notion-hosted file))
Nutze diese Funktion:
```javascript
// Grab the textual response from the agent trying to query arXiv
const assistantResponse = $input.text || "";

// Detect if arXiv rate-limited the agent or dropped the connection
if (assistantResponse.includes("429") || 
    assistantResponse.includes("Rate limit") || 
    assistantResponse.includes("503 Service Unavailable")) {
    
    return "Trigger_Loop"; // Matches the path leading to the Loop Node
} else {
    return "To_User_Chat"; // Matches the path completing the workflow
}
```
Diese Funktion wandelt eine unübersichtliche Agentenantwort in eine klare Routing-Entscheidung um. In diesem Beispiel prüfen wir auf temporäre Servicefehler, die sich oft von selbst erholen. Konkret suchen wir nach 429 (Too Many Requests), was darauf hinweist, dass ein Rate Limit erreicht wurde, nach „Rate limit“-Nachrichten, die vom Tool oder Modell zurückgegeben werden, und nach 503 Service Unavailable, was bedeutet, dass der Service vorübergehend keine Anfragen verarbeiten kann. Diese Fehler sind gute Kandidaten für Retries, weil ein zweiter oder dritter Versuch erfolgreich sein kann, sobald der temporäre Zustand vorbei ist.
Die Funktion löst das Problem nicht selbst. Sie beantwortet nur:
> Sollen wir es erneut versuchen, oder sollen wir das Ergebnis an den User zurückgeben?
Sie stellt also zwei Outputs bereit: Trigger_Loop, falls etwas kaputt war, oder To_User_Chat, falls die Ausführung des Agenten gesund war.
# Schritt 3: Den Condition Node hinzufügen
Füge einen Condition Node namens Evaluate Network State hinzu.
![image]((notion-hosted file))
Dieser Node prüft den Output des Parsers.
Erstelle zwei Branches:
- To_User_Chat
- Trigger_Loop
Wenn der Parser To_User_Chat zurückgibt, geht der Workflow zum Direct Reply Node.
Wenn der Parser Trigger_Loop zurückgibt, geht der Workflow zum Retry Loop.
Öffne den Node und füge Folgendes ein:
![image]((notion-hosted file))
Wir fügen einen Branch für Trigger_Loop hinzu, der zu Agenten-Retries führt. Der alternative gesunde Branch wird automatisch hinzugefügt, du musst also keine zweite Bedingung hinzufügen.
# Schritt 4: Den Retry Loop hinzufügen
Füge einen Loop Node namens Retry Counter Loop hinzu. Verbinde den ersten Branch des Conditional Node mit ihm.
![image]((notion-hosted file))
Setze die maximale Loop-Anzahl auf 3. Das ist wichtig. Ein Retry-Pattern muss immer ein Limit haben. Ohne maximale Anzahl könnte der Workflow immer wieder dasselbe fehlschlagende Tool aufrufen. Verbinde den Loop zurück mit Arxiv MCP Engine.
![image]((notion-hosted file))
Jetzt kann der Workflow die arXiv-Suche erneut versuchen, wenn der Fehler temporär aussieht.
# Schritt 5: Direct Reply hinzufügen
Füge einen Direct Reply Node für den erfolgreichen Pfad hinzu.
Dieser Node gibt den finalen Output des Agenten an den User zurück.
Du kannst den Standardnamen beibehalten.
![image]((notion-hosted file))
Dieser Pfad wird eingeschlagen, wenn der Parser keinen wiederholbaren Fehler erkennt. Die Nachricht des Direct-Reply-Nodes sollte die Ausgabe des Agenten enthalten:
![image]((notion-hosted file))
# Checkpoint
Teste den Workflow mit einer normalen Anfrage:
> Find recent papers on transformers
![image]((notion-hosted file))
### Schritt 6: Eine Fallback-Antwort hinzufügen
Bislang führt der Workflow bis zu drei Startversuche für die arXiv-Suche durch. Was aber geschieht, wenn alle drei Versuche fehlschlagen? Ein resilienter Workflow sollte an dieser Stelle nicht einfach unvermittelt abbrechen oder dem Nutzer einen kryptischen Error-Trace ausgeben. Stattdessen sollte er eine definierte Rückmeldung liefern, die das Problem erklärt und direkt einen sinnvollen nächsten Schritt vorschlägt.
> ☝ In Flowise routet der Loop Node den Workflow zurück zum ausgewählten Retry-Schritt. Er braucht keinen separaten „max retries reached“-Branch. Stattdessen fügen wir direkt in den Loop-Einstellungen eine Fallback-Nachricht hinzu. Wenn die maximale Loop-Anzahl erreicht ist, gibt der Workflow dadurch eine kontrollierte nutzerseitige Antwort zurück, statt weiter zu wiederholen.
Füge deinem Node eine Fallback-Nachricht hinzu:
> I’m currently unable to retrieve results from arXiv because the service may be temporarily unavailable or rate-limited.
  Please try again in a few minutes, or simplify your search query and run it again.
![image]((notion-hosted file))
# Worauf du achten solltest
Der größte Fehler ist es, blind jeden Fehler zu wiederholen. Nicht jedes Problem rechtfertigt einen erneuten Versuch. Eine fehlende Eingabe, eine ungültige Anfrage oder ein fehlerhafter Prompt werden auch beim nächsten Mal fehlschlagen. Retries sind für temporäre Probleme gedacht: Rate Limits, kurzzeitige Dienstausfälle (Service Unavailable), Verbindungsabbrüche oder Netzwerkschluckaufe. Zudem darf das Retry-Limit nicht vergessen werden: Definiere immer eine maximale Anzahl an Schleifendurchläufen.
# Zusammenfassung
Damit hast du ein kontrolliertes Retry-Muster für den arXiv-MCP-Agenten aufgesetzt. Der Workflow erkennt jetzt eigenständig, ob ein Tool-Fehler nur vorübergehend ist, führt betroffene Anfragen erneut aus und bricht nach Erreichen des Limits sicher ab. 
Genau darum geht es bei resilienter Orchestrierung: Das System reagiert gelassen auf Störungen, ohne sich in einer Endlosschleife zu verlieren.
