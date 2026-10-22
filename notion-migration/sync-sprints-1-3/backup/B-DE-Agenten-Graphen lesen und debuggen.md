# Agenten-Graphen lesen und debuggen

Notion page: https://app.notion.com/p/Agenten-Graphen-lesen-und-debuggen-3789418319f380b5ab69c631970542c0
Backed up before n8n migration

> 💡 Das machst du in dieser Lektion: Du gehst drei fehlerhafte Execution-Logs von Meridians in Produktion gebrachten Agenten durch und schlägst für jede Fehlerart eine gezielte Lösung vor.

## Das Szenario
Drei Fehlerberichte sind zwei Tage nach dem Go-live des Agenten von Meridians Beratungsteam eingetroffen. Jeder beschreibt ein anderes Symptom. Deine Aufgabe ist es, jeden Execution Trace zu lesen, den spezifischen Fehlerpunkt mithilfe des Frameworks aus der vorherigen Lektion zu identifizieren und eine gezielte Korrektur vorzuschlagen.
Einen rohen Execution Trace zu lesen, ist zuverlässiger, als verschiedene Chatnachrichten in der UI zu testen. Der Trace zeigt genau, was der Agent gedacht hat, was er zu tun versucht hat und was er erhalten hat. Dadurch lässt sich der Ursprung eines Fehlers präzise lokalisieren.
## Die drei Failure Traces
### Trace Log A: Der eingefrorene Agent
## Das Szenario
Zwei Tage nach dem Go-live sind bei Meridians Consulting-Team drei Fehlermeldungen eingegangen. Jede beschreibt ein anderes Symptom. Deine Aufgabe ist es, jeden Execution-Trace zu lesen, mit dem Framework aus der letzten Lektion die genaue Fehlerquelle zu bestimmen und eine gezielte Lösung vorzuschlagen.
Einen rohen Execution-Trace zu lesen ist verlässlicher, als in der UI verschiedene Chat-Nachrichten durchzutesten. Der Trace zeigt genau, was der Agent gedacht hat, was er versucht hat und was er zurückbekommen hat. Dadurch lässt sich der Ursprung eines Fehlers präzise lokalisieren.
## Die drei Fehler-Traces
### Trace-Log A: Der eingefrorene Agent
```json
{
  "user_input": "What is the status of my laptop replacement order?",
  "agent_config": {
    "tools_connected": 15
  },
  "trace": [
    {
      "thought": "I have many tools available. I should clarify 
       what order number they are referring to before proceeding.",
      "action": null
    },
    {
      "final_output": "Could you please provide more details 
       about your order so I can assist you better?"
    }
  ]
}
```

### Trace-Log B: Die eskalierende Halluzination
```json
{
  "user_input": "Can I expense a new standing desk?",
  "trace": [
    {
      "thought": "I need to check the expense policy.",
      "action": "Document Store retrieval — query: standing desk expense",
      "observation": "0 documents found."
    },
    {
      "thought": "No policy found. I will apply the standard 
       €500 office equipment stipend based on industry norms.",
      "action": "Update Flow State — key: equipment_stipend, value: €500"
    },
    {
		  "user_followup": "Great — I will buy a €450 desk. 
		   Can you confirm the budget is available?",
		  "action": "HTTP Node — GET engagement budget check",
		  "observation": "Request sent with equipment_stipend: €500 
		  from Flow State. API returns malformed response no budget record found for assumed stipend value."
		}
  ]
}
```

### Trace Log C: Der endlose Routing-Loop
```json
{
  "trace": [
    {"node": "Agent Node", 
     "thought": "IT issue. Need employee ID before routing.",
     "action": "Pass to Loop Node"},
    {"node": "Loop Node", 
     "action": "Return to Condition Node"},
    {"node": "Condition Node", 
     "check": "Employee ID present?", 
     "result": "False — return to Agent Node"},
    {"note": "Cycle repeats until token budget exhausted."}
  ]
}
```

## Deine Aufgaben
### Aufgabe A: Trace-Log A diagnostizieren
Der Agent hatte fünfzehn Tools zur Verfügung, hat aber keines davon aufgerufen.
Beantworte Folgendes:
- Welche architektonische Bedingung hat dazu geführt, dass der Agent Node nachgefragt hat, statt das richtige Tool aufzurufen?
- Welche konkrete Änderung an der Canvas würde das Problem lösen?
> ➡️ Checkpoint: Der Gedanke des Agent Node begann mit „I have many tools available“. Wenn zu viele Tools mit überlappenden Beschreibungen verbunden sind, kann das Modell nicht mehr sicher das richtige auswählen. Überlege, wie eine sinnvolle Obergrenze für gut abgegrenzte Tools an einem einzelnen Agent Node aussehen könnte.

### Aufgabe B: Trace-Log B diagnostizieren
Eine Halluzination wurde in den Flow State geschrieben und anschließend vom HTTP Node verarbeitet. Dadurch entsteht ein echtes Rückerstattungsticket, das auf einem erfundenen Richtlinienwert basiert.
Beantworte Folgendes:
- An welchem genauen Schritt wurde der Fehler unumkehrbar? Bestimme die Aktion, die aus einem Denkfehler einen strukturellen Fehler gemacht hat. Gemeint ist der Moment, in dem der erfundene Wert die Reasoning-Ebene verlassen hat und als Eingabewert bei einem Node ankam, der im weiteren Verlauf ausgeführt wird.
- Formuliere eine Ergänzung von zwei Sätzen für den System-Prompt des Agent Node. Sie soll verhindern, dass er angenommene oder abgeleitete Informationen in den Flow State schreibt, wenn die Retrieval null Treffer liefert.
> ➡️ Checkpoint: Die Halluzination lief in zwei Stufen ab. Der Agent hat sich eine Zahl ausgedacht und sie dann in den Flow State geschrieben. Welcher dieser Schritte war der Punkt ohne Umkehr? Sobald ein erfundener Wert im Flow State steht, behandelt ihn jeder Node, der im weiteren Verlauf von diesem Key liest, als gesicherte Tatsache.

### Aufgabe C: Trace-Log C diagnostizieren
Die Loop lief endlos, weil die Exit-Bedingung nie erfüllt wurde.
Beantworte Folgendes:
- Der Loop Node in Agentflow v2 hat keinen Forward-Output-Anker. Seine einzige Funktion ist es, die Ausführung zurückzuleiten. Der Exit-Pfad kann deshalb nicht vom Loop Node selbst kommen. Welcher Node in Trace-Log C ist für den Exit-Pfad zuständig, und was fehlt in seiner Konfiguration?
- Schlage zwei Änderungen vor, eine auf Canvas-Ebene und eine auf Prompt-Ebene. Beide sollen verhindern, dass diese Loop das Token-Budget aufbraucht.
> ➡️ Checkpoint: Der Condition Node ist binär, er hat nur zwei Outputs. Der Exit muss um genau diese zwei Outputs herum gebaut werden, nicht durch einen dritten. Das Muster dafür ist ein Retry-Counter, der bei jeder Iteration hochzählt. Dazu kommt ein Condition Node, der den Counter mit einem Maximum vergleicht. Solange der Counter unter dem Maximum liegt, führt der False-Branch zurück durch den Loop Node für einen weiteren Versuch. Erreicht der Counter das Maximum, feuert derselbe Condition Node seinen anderen Branch in einen Direct Reply Node mit einer Fallback-Nachricht. Der Counter macht einen binären Condition Node ausreichend für einen kontrollierten Exit.

## Verständnischeck
>  In Trace-Log B hat der Agent einen angenommenen Richtlinienwert in den Flow State geschrieben, nachdem die Retrieval null Treffer geliefert hatte. Warum macht genau diese Aktion den Fehler deutlich gefährlicher, als wenn die Annahme nur in der aktiven Reasoning-Ebene des Agenten geblieben wäre?

  [EMBED] https://app.masterschool.com/campus/multi-choice-question/3ad4810d-8c7e-4506-bbe5-ce3d8073e38a


> 💡 Fazit:
  Einen Execution-Trace zu lesen ist das präziseste Debugging-Tool, das es für einen visuellen Agenten gibt. Er zeigt genau, was der Agent gedacht hat, was er versucht hat und was er zurückbekommen hat. Die drei Fehlerarten in diesen Traces sind die häufigsten Produktionsfehler bei visuellen Agent-Builds. Sie in einem Trace-Log zu erkennen, ist der erste Schritt, um sie auf der Canvas zu verhindern.