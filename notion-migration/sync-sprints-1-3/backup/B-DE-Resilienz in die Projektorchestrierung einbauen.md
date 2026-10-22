# Resilienz in die Projektorchestrierung einbauen

Notion page: https://app.notion.com/p/Resilienz-in-die-Projektorchestrierung-einbauen-66f9418319f383908fb8014a1ff89611
Backed up before n8n migration

Du hast jetzt die vier zentralen Resilienz-Muster kennengelernt (Timeouts, Retries, Fallbacks und Circuit Breakers) und gesehen, wie jedes dieser Patterns eine spezifische Fehlerklasse abdeckt. In dieser Lektion wendest du das Gelernte auf dein eigenes Projekt an. Ein durchdachtes Orchestrierungsdesign setzt nicht voraus, dass jeder Agent, jedes Tool oder jeder MCP-Aufruf auf Anhieb funktioniert. Stattdessen legst du nun fest, wie dein Workflow reagiert, wenn Probleme auftreten.
## Deine Aufgabe
Öffne deine Projektorchestrierung und erweitere sie um:
1. mindestens eine Timeout-Regel
1. mindestens eine Retry-Regel
1. mindestens einen Fallback-Pfad
Du musst den Workflow nicht perfekt machen. Das Ziel ist, die wichtigsten Risikopunkte sichtbar zu machen und zu zeigen, wie sich die Orchestrierung verhalten sollte, wenn etwas schiefgeht.
## Schritt 1: Riskante Nodes identifizieren
Sieh dir deinen aktuellen Projekt-Flow an und markiere die Schritte, die am wahrscheinlichsten scheitern.
Gute Kandidaten sind:
- Agent Nodes, die ein LLM aufrufen
- Tool-Aufrufe über MCP
- externe API-Aufrufe
- Such- oder Retrieval-Schritte
- Parsing- oder Formatierungsschritte
- Routing-Entscheidungen basierend auf strukturierter Ausgabe
Schreibe für jeden riskanten Schritt auf:
[TABLE]
  | Workflow-Schritt | Was könnte schiefgehen? | Auswirkung auf den User |
  | Knowledge-Retrieval-Tool | Tool antwortet nicht | User erhält keine Antwort |
  | Spezialagent | Ungültiger JSON-Output | Workflow kann nicht korrekt routen |
  | Report Generator | Dauert zu lange | User wartet ohne Feedback |
## Schritt 2: Timeout-Verhalten hinzufügen
Ein Timeout bedeutet, dass der Workflow nach einem definierten Zeitlimit aufhört zu warten.
Wähle einen riskanten Schritt und definiere:
[TABLE]
  | Frage | Deine Antwort |
  | Für welchen Node gilt ein Timeout? |  |
  | Wie lange sollte der Workflow warten? |  |
  | Was passiert nach dem Timeout? |  |
  | Sieht der User eine Nachricht? |  |
Beispiel:
> Wenn das Knowledge-Retrieval-Tool nicht innerhalb von 30 Sekunden antwortet, höre auf zu warten und wechsle zum Fallback-Pfad.
## Schritt 3: Retry-Verhalten hinzufügen
Ein Retry bedeutet, dass der Workflow denselben Schritt nach einem Fehler erneut versucht.
Wähle einen Schritt, bei dem ein Retry sinnvoll ist. Retrye nicht alles.
Definiere:
[TABLE]
  | Retry-Regel | Dein Design |
  | Trigger | Timeout, Parsing-Fehler, leere Antwort, Tool-Fehler |
  | Maximale Versuche | 2 oder 3 |
  | Was ändert sich beim Retry? | dieselbe Anfrage, vereinfachter Prompt, kleinere Abfrage, anderes Modell |
  | Stoppbedingung | Erfolg oder maximale Anzahl von Versuchen erreicht |
Beispiel:
> Wenn der Spezialagent ungültiges JSON zurückgibt, wiederhole bis zu 2-mal mit einer strengeren Formatierungsanweisung. Wenn es weiterhin scheitert, wechsle zum Fallback.
## Schritt 4: Einen Fallback-Pfad hinzufügen
Ein Fallback ist der sichere Pfad, der genutzt wird, wenn der normale Pfad nicht fortgesetzt werden kann.
Wähle einen Fallback-Typ:
[TABLE]
  | Fallback-Typ | Wann du ihn nutzt |
  | Direkte User-Nachricht | Das System kann die Aufgabe nicht sicher abschließen |
  | Einfachere Agentenantwort | Der fortgeschrittene Schritt ist gescheitert, aber eine grundlegende Antwort ist möglich |
  | Menschliche Eskalation | Das Problem muss geprüft werden |
  | Alternatives Tool | Das erste Tool ist nicht verfügbar |
  | Gecachte/statische Antwort | Das System hat eine sichere Standardantwort |
Beispiel für eine Fallback-Nachricht:
> Ich konnte die vollständige automatisierte Prüfung nicht abschließen, weil das Retrieval-Tool nicht geantwortet hat. Ich kann trotzdem zusammenfassen, was ich aus der aktuellen Unterhaltung weiß, oder du kannst es später erneut versuchen.
## Schritt 5: Dein Orchestrierungsdiagramm aktualisieren
Füge Resilienz-Elemente direkt in dein Diagramm ein.
Dein Diagramm sollte zeigen:
- den normalen erfolgreichen Pfad
- wo der Timeout angewendet wird
- wo Retries passieren
- wann der Workflow aufhört zu retryen
- wohin der Fallback-Pfad führt
![image]((notion-hosted file))
## Checkpoint-Fragen
Prüfe vor der Einreichung:
1. Hast du Resilienz an einem echten Risikopunkt hinzugefügt, nicht nur an einem zufälligen Node?
1. Ist das Retry-Limit klar?
1. Schützt der Fallback-Pfad den User vor einem kaputten oder endlosen Workflow?
1. Kann jemand anderes dein Design anhand des Diagramms verstehen?
1. Hast du erklärt, was passiert, wenn die Retries ausgeschöpft sind?
## Zusammenfassung
Damit hast du dein Projekt über den bloßen „Happy Path“ hinaus zu einem praxistauglichen Orchestrierungsdesign weiterentwickelt. Das System ist nun für verzögerte Antworten, wiederkehrende Fehler und unklare Prozesspfade gerüstet. Dies ist ein entscheidender Schritt hin zu Agenten, die im Ernstfall kontrolliert fehlschlagen, anstatt unbemerkt abzustürzen.
