# Bedingtes Routing mit dem Condition Node

Notion page: https://app.notion.com/p/Bedingtes-Routing-mit-dem-Condition-Node-3789418319f3800cb839c741d31279be
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du fügst dem Meridian Agentflow v2 deterministisches Branching über den Condition Node hinzu. So routest du Anfragen anhand definierter Regeln über unterschiedliche Ausführungspfade.

## Den Kontext herstellen
Meridians Agent kann jetzt ein Gespräch führen, fundiertes Wissen aus internen Dokumenten abrufen und innerhalb eines klar definierten Scopes antworten. Die nächste Herausforderung, die das Entwicklungsteam identifiziert hat, ist das Routing.
Während einer Pilot-Session bat ein Consultant den Agenten, den Engagement-Status für ein bestimmtes Kundenprojekt zu prüfen. Der Agent rief einen Chunk aus dem Operations Handbook zu Projektklassifizierungsstufen ab. Das ist zwar technisch verwandt, aber nicht das, was der Consultant brauchte. Der Consultant brauchte Live-Engagement-Daten, keine Policy-Dokumentation.
Das Problem ist, dass der Agent aktuell ein einzelner Pfad ist, bei dem jede Query zum Agent Node geht, der dann entscheidet, was zu tun ist. Wenn der Agent mehr Fähigkeiten erhält, wird diese Single-Path-Architektur zu einem Bottleneck. Queries, die Live-Daten benötigen, konkurrieren mit Queries, die Dokument-Retrieval benötigen, und der Agent muss sich jedes Mal per Reasoning zum richtigen Tool durcharbeiten.
Das Conditional Routing löst dies, indem einige Entscheidungen ausdrücklich und deterministisch gemacht werden. Statt den Agenten herausfinden zu lassen, ob eine Query Live-Daten oder Knowledge Retrieval benötigt, bewertet der Condition Node eine Regel und routet die Query, bevor der Agent sie überhaupt sieht.
## Was du baust
Einen aktualisierten Meridian Base Agent-Canvas, der eingehende Queries mit einem Condition Node in zwei Pfade routet:
- Pfad A - Knowledge Queries: Queries zu Meridians internen Policies, Verfahren und regionalem Kontext gehen zum Agent Node mit Document-Store-Knowledge-Retrieval
- Pfad B - Status Queries: Queries, die spezifische Trigger-Formulierungen enthalten, die auf einen Bedarf an Live-Daten hinweisen, werden an einen separaten Direct Reply Node mit einer Platzhalterantwort geroutet
Pfad B wird später mit einem Live-HTTP-Node verbunden. Vorerst wird die Routing-Struktur gebaut und mit einem Platzhalter überprüft.
## Was der Condition Node macht
Der Condition Node routet den Workflow auf der Grundlage einer festen Regel. Er vergleicht Input-Werte mit logischen Operatoren wie equals, contains, greater than oder is empty. Wenn die Regel true ergibt, läuft die Ausführung über den true-Branch weiter; wenn false, über den false-Branch.
Das Schlüsselwort ist deterministisch. Anders als der Condition Agent Node bewertet der Condition Node eine feste Regel. Das Ergebnis ist für denselben Input immer gleich. Das macht ihn zur richtigen Wahl, wenn die Routing-Logik klar ist und keine Interpretation erfordert.
### Schritt 1: Den Meridian-Base-Agent-Canvas öffnen
Öffne Flowise unter http://localhost:3000. Klicke auf Agentflows und öffne deinen Meridian Base Agent-Canvas.
Dein Canvas sollte aktuell Folgendes zeigen:
Start Node → Agent Node → Direct Reply Node
Mit dem Document Store meridian-knowledge, der mit der Knowledge-Konfiguration des Agent Nodes verbunden ist.
### Schritt 2: Flow State im Start Node initialisieren
Alle State Keys, die im gesamten Workflow verwendet werden, müssen mit ihren Standardwerten über den Flow-State-Parameter im Start Node initialisiert werden. Dieser Schritt deklariert effektiv das Schema oder die Struktur deines Flow State für diesen Workflow.
Klicke auf den Start Node, um seine Einstellungen zu öffnen. Suche den Abschnitt Flow State und füge das folgende Key-Value-Paar hinzu:
[TABLE]
  | Key | Initial Value |
  | query_type | knowledge |
Dieser Key wird vom Condition Node verwendet, um zu bestimmen, welcher Pfad genommen wird. Er ist standardmäßig knowledge ; das bedeutet, alle Queries werden als Knowledge Queries behandelt, sofern die Routing-Regel ihn nicht ändert.
Speichere die Start-Node-Einstellungen.
### Schritt 3: Einen Condition Node zum Canvas hinzufügen
Klicke auf dem Canvas auf (+). Wähle unter der Kategorie Agentflow Condition aus und füge ihn zum Canvas hinzu.
Positioniere ihn zwischen dem Start Node und dem Agent Node. Dein Canvas-Layout sollte jetzt von links nach rechts so aussehen:
Start Node → Condition Node → Agent Node → Direct Reply Node
![image]((notion-hosted file))

### Schritt 4: Den Canvas neu verbinden
Der aktuelle Edge verläuft direkt vom Start Node zum Agent Node. Das ändert sich jetzt: Der Condition Node sitzt ab sofort dazwischen.
1. Lösche die bestehende Edge zwischen Start Node und Agent Node
1. Zeichne eine neue Edge vom Start-Node-Output zum Condition-Node-Input
1. Behalte die bestehende Edge vom Agent Node zum Direct Reply Node
Die Condition Node hat zwei Output-Anker (einen für true und einen für false). Diese verbindest du in Schritt 6.
### Schritt 5: Den Condition Node konfigurieren
Klicke auf den Condition Node, um seine Einstellungen zu öffnen. Konfiguriere die Condition wie folgt:
[TABLE]
  | Feld | Wert |
  | Type | String |
  | Value 1 | {{ question }} |
  | Operation | contains |
  | Value 2 | status |
![image]((notion-hosted file))
Diese Regel prüft, ob der Input des Nutzers das Wort status enthält. Wenn true, ist die Query eine Statusanfrage und sollte zu einer Live-Datenabfrage geroutet werden. Wenn false, ist es eine Knowledge Query und sollte zum Agent Node gehen.
> Warum contains und nicht equals: Consultants formulieren Queries natürlich: „What is the status of the Krauss account?“ oder „Can you check the engagement status for Bauer?“ Das Wort status erscheint an unterschiedlichen Positionen und in unterschiedlichen Satzstrukturen. Der Operator contains erfasst all diese Fälle, ohne eine exakte Formulierung zu verlangen.
### Schritt 6: Die Condition-Node-Outputs verbinden
Der Condition Node hat zwei Output-Anker:
True Output (enthält „status“):
- Füge einen neuen Direct Reply Node zum Canvas für Pfad B hinzu
- Verbinde den true output des Condition Nodes mit diesem neuen Direct Reply Node
- Gib im Message-Feld des neuen Direct Reply Nodes ein:
Live engagement status lookup is not yet configured. Please contact your engagement manager directly for current project status.
Dies ist die Platzhalterantwort für Pfad B. Sie wird in der Lektion zu Live-Datenabfragen durch den HTTP-Node-Output ersetzt.
False Output (enthält nicht „status“):
- Verbinde den false output des Condition Nodes mit dem bestehenden Agent Node
Dein Canvas sollte jetzt Folgendes zeigen:
![image]((notion-hosted file))

### Schritt 7: Den bestehenden Direct Reply Node bestätigen
Klicke auf den ursprünglichen Direct Reply Node (Pfad A, verbunden mit dem Agent Node) und bestätige, dass das Message-Feld weiterhin auf Folgendes gesetzt ist:
{{ agentAgentflow_0.output }}
Falls es geleert wurde, gib es mit dem {{-Variablenselektor erneut ein.
### Schritt 8: Speichern und den Routing-Test ausführen
Speichere den Canvas. Klicke auf das Chat-Symbol und führe die folgenden vier Queries in separaten Sessions aus. Öffne zwischen jedem Test eine neue Chat-Session, um Cross-Session-Kontext zu vermeiden:
Test 1 - Knowledge Query (sollte zum Agent Node routen): What are the project classification tiers at Meridian?
- Erwartung: Agent Node ruft aus dem Document Store ab und gibt Policy-Inhalte zurück.
Test 2 - Status Query (sollte zur Platzhalter-Direct-Reply routen): Can you check the engagement status for the Krauss account?
- Erwartung: Platzhalterantwort darüber, dass Live-Status noch nicht konfiguriert ist.
Test 3 - Knowledge Query mit dem Wort „status“ in einem anderen Kontext: What is the escalation status procedure for severity level 2 issues?
- Erwartung: Diese Query enthält das Wort „status“ und wird zu Pfad B routen. Notiere dieses Ergebnis, weil es eine Einschränkung der containsRegel zeigt, die mit dem Condition Agent Node adressiert wird.
Test 4 - Regionale Query (sollte zum Agent Node routen): What should I know about running an engagement in Poland?
- Erwartung: Agent Node ruft den Polen-Abschnitt aus dem Regional Playbook ab.
### Was Test 3 zeigt
Test 3 ist bewusst so gestaltet, dass er die Einschränkung deterministischen Routings sichtbar macht. Die Query ist tatsächlich eine Knowledge Query. Sie fragt nach einem Eskalationsverfahren, aber das Wort „status“ löst den falschen Pfad aus. Das ist der zentrale Trade-off des Condition Nodes:
[TABLE]
  |  | Condition Node | Condition Agent Node |
  | Routing-Methode | Feste Regel: Keyword-Match | AI-Reasoning: Intent-Interpretation |
  | Geschwindigkeit | Schnell: kein Modellaufruf | Langsamer: erfordert einen Modellaufruf |
  | Genauigkeit bei klaren Queries | Hoch | Hoch |
  | Genauigkeit bei mehrdeutigen Queries | Niedrig: Keywords können irreführen | Hoch: Intent wird verstanden |
  | Am besten geeignet für | Klare, eindeutige Trigger | Nuanciertes, Intent-basiertes Routing |
### Checkliste: Vor dem Fortfahren bitte bestätigen
- [ ] Flow State im Start Node mit Key query_type auf knowledge initialisiert
- [ ] Condition Node zwischen Start Node und Agent Node zum Canvas hinzugefügt
- [ ] Start Node mit sichtbarer Edge mit Condition Node verbunden
- [ ] Condition Node konfiguriert - Type: String, Value 1: {{ $flow.input }}, Operation: contains, Value 2: status
- [ ] True Output mit Pfad-B-Direct-Reply-Node mit Platzhalternachricht verbunden
- [ ] False Output mit Agent Node verbunden
- [ ] Agent Node mit Pfad-A-Direct-Reply-Node verbunden
- [ ] Message-Feld des Pfad-A-Direct-Reply-Nodes auf {{ agentAgentflow_0.output }} gesetzt
- [ ] Canvas vor dem Testen gespeichert
- [ ] Alle vier Test-Queries ausgeführt und Ergebnisse bewertet
- [ ] Ergebnis von Test 3 als bekannte Einschränkung deterministischen Routings notiert

> 💡 Takeaway: 
  Der Condition Node routet präzise, schnell und zuverlässig, solange die Logik eindeutig ist. Keyword-basierte Regeln funktionieren bestens, wenn sich Trigger-Begriffe klar unterscheiden und nicht in anderen Kontexten auftauchen. Bedeutet dieselbe Formulierung je nach Kontext etwas anderes, führt deterministisches Routing zu falschen Ergebnissen. Solche Fehler entstehen still und lassen sich nur schwer erkennen.
  Die nächste Lektion stellt einen neuen Routing-Ansatz vor: den Condition Agent Node. Er interpretiert den Intent, anstatt nur Strings abzugleichen.
