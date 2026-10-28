# End-to-End-Fehleranalyse

Notion page: https://app.notion.com/p/End-to-End-Fehleranalyse-3969418319f38376a6e801ed03b0b4af
Backed up before n8n migration

## Der offensichtliche Verdächtige ist selten der Täter
Wenn ein orchestriertes System scheitert, liegt die Root Cause oft woanders als in der Komponente, die sichtbar ausgefallen ist.
Schau dir deinen arXiv Research Assistant an:
1. Ein User reicht eine Supportanfrage ein.
1. Der Intake Agent klassifiziert die Anfrage.
1. Der Orchestrator schickt sie an den passenden Spezialisten.
1. Der Spezialist fragt über MCP eine Knowledge Base ab.
1. Die Antwort geht zurück an den User.
Bekommt der User eine falsche Antwort, heißt das noch lange nicht, dass der Spezialagent schuld ist. Der eigentliche Fehler kann viel früher passiert sein:
- Der Intake Agent hat die Anfrage falsch klassifiziert.
- Der Orchestrator hat sie an den falschen Spezialisten geroutet.
- Der MCP-Server hat unvollständige Informationen geliefert.
- Die Knowledge Base war veraltet.
- Ein früherer Retry hat einen veralteten Status hinterlassen, der dann durch den gesamten Workflow mitgeschleift wurde.
End-to-End-Fehleranalyse heißt: Du untersuchst die gesamte Ausführungskette und findest heraus, wo der Fehler wirklich entstanden ist.
## Über einzelne Fehler hinausblicken
Wenn ein orchestriertes System scheitert, ist die Root Cause nicht immer die Komponente, die scheinbar aufgehört hat zu funktionieren.
Nimm deinen arXiv Research Assistant als Beispiel:
1. Ein User reicht eine Supportanfrage ein.
1. Der Intake Agent klassifiziert die Anfrage.
1. Der Orchestrator sendet sie an den richtigen Spezialisten.
1. Der Spezialist fragt über MCP eine Knowledge Base ab.
1. Die Antwort wird an den User zurückgegeben.
Wenn der User eine falsche Antwort erhält, muss der Spezialagent nicht tatsächlich schuld sein. Das eigentliche Problem könnte viel früher entstanden sein:
- Der Intake Agent hat die Anfrage falsch klassifiziert,
- der Orchestrator hat sie an den falschen Spezialisten geroutet,
- der MCP-Server hat unvollständige Informationen zurückgegeben,
- die Knowledge Base war veraltet,
- oder ein früherer Retry hat stale State erzeugt, der sich durch den Workflow fortgepflanzt hat.
End-to-End-Fehleranalyse bedeutet, die gesamte Ausführungskette zu untersuchen, um festzustellen, wo der Fehler tatsächlich entstanden ist.
![image]((notion-hosted file))
## Wo Fehler typischerweise passieren
Fehler treten auf mehreren Ebenen des Systems auf. Es lohnt sich, in diesen Ebenen zu denken statt in einzelnen Nodes.
[TABLE]
  | Ebene | Beispielfehler | Mögliche Gegenmaßnahme |
  | User-Eingabe | Mehrdeutige oder unvollständige Anfrage | Klärungsschritt vor dem Routing |
  | Agenten-Reasoning | Falsche Klassifizierung oder Planung | Validierungsagent oder Confidence Checks |
  | Orchestrierung | Falsches Routing oder übersprungener Schritt | Routing-Regeln und State-Validierung |
  | Tool-Integration | MCP-Server nicht erreichbar oder API-Timeout | Retries, Fallbacks, Circuit Breakers |
  | Externe Daten | Fehlende oder veraltete Informationen | Alternative Datenquelle oder gecachte Ergebnisse |
  | Finale Antwort | Halluzinierte oder unvollständige Antwort | Antwortvalidierung vor der Rückgabe |
Wichtig: Retries lösen längst nicht jedes Problem. Versteht der Intake Agent die Anfrage falsch, bringt es wenig, dieselbe Klassifizierung noch dreimal laufen zu lassen. Eine Klärungsfrage an den User ist hier meist die bessere Gegenmaßnahme.
## Vom Symptom rückwärts zur Ursache
Beim Debuggen einer Orchestrierung arbeitest du vom sichtbaren Problem aus rückwärts.
Angenommen, ein Kunde bekommt Preisinformationen statt Troubleshooting-Schritte.
Bevor du am Spezialagenten schraubst, klär erst ein paar Fragen:
- Wurde die ursprüngliche Anfrage korrekt klassifiziert?
- Wurde der richtige Spezialist ausgewählt?
- Hat der Spezialist den erwarteten Kontext bekommen?
- Hat das MCP-Tool die erwarteten Informationen geliefert?
- Wurde unerwartet ein Fallback aktiviert?
Geh den Ausführungspfad Schritt für Schritt durch. Die erste falsche Entscheidung ist fast immer die eigentliche Ursache.
## Quiz
>  Ein Workflow erzeugt folgendes Ergebnis:
  > Der User fragt, wie er sein Passwort zurücksetzen kann, erhält aber Billing-Anweisungen.
  Welche Komponente würdest du zuerst untersuchen?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/0a2b5430-6522-4a87-b519-d975b88ef232
## Checkliste für die Fehleranalyse
Wenn du einen End-to-End-Workflow analysierst, frag dich:
- Wo ist die erste falsche Entscheidung passiert?
- Hat jeder Agent die erwarteten Inputs bekommen?
- Hat jedes Tool gültige Outputs geliefert?
- Wurden Retries oder Fallbacks ausgelöst?
- Hat sich falscher State in spätere Schritte gezogen?
- Konnte sich der Workflow selbst erholen oder musste jemand manuell eingreifen?
Diese Fragen der Reihe nach abzuarbeiten bringt dich deutlich schneller ans Ziel als das isolierte Debuggen einzelner Nodes.
## Zusammenfassung
Ein zuverlässiges Multi-Agent-System braucht mehr als gut designte Agenten. Auch Integration, Orchestrierung, externe Tools und Recovery-Mechanismen bestimmen das Ergebnis. Mit End-to-End-Fehleranalyse verfolgst du ein Problem bis zu seiner Quelle zurück. So behebst du die Ursache statt nur das Symptom. Je größer deine Projekte werden, desto mehr zahlt sich dieser Blick aufs Gesamtsystem beim Debuggen aus.
