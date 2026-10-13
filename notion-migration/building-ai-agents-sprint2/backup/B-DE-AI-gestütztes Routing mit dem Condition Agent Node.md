# AI-gestütztes Routing mit dem Condition Agent Node

Notion page: https://app.notion.com/p/AI-gest-tztes-Routing-mit-dem-Condition-Agent-Node-3789418319f380428eb2c377fb816e66
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du ersetzt den Condition Node durch einen Condition Agent Node. So meisterst du intent-basiertes Routing, an dem einfaches Keyword-Matching scheitert.

## Den Rahmen setzen
In der vorherigen Lektion fügte Meridians Entwicklungsteam deterministisches Routing mit dem Condition Node hinzu. Das Routing funktionierte gut für klare Statusanfragen, aber Test 3 zeigte ein echtes Problem: Die Query „What is the escalation status procedure for severity level 2 issues?“ wurde zum Live-Datenpfad geroutet, weil das Wort „status“ im Satz vorkam, obwohl die Query tatsächlich nach einem Policy-Verfahren fragte, nicht nach Live-Engagement-Daten.
Klaus Brandt prüfte die Testergebnisse und markierte das Problem sofort. Wenn ein Consultant nach einem Eskalationsverfahren fragt und eine Platzhalterantwort über eine Live-Datenabfrage erhält, ist der Agent gescheitert. Nicht wegen eines technischen Fehlers, sondern weil Keyword-Matching Intent nicht verstehen kann.
Die Schlussfolgerung des Entwicklungsteams ist, dass die Routing-Entscheidung für Meridians Agenten kein Regelproblem darstellt. Es ist ein Klassifizierungsproblem. Der Agent muss verstehen, was der Consultant erreichen möchte, statt nur Wörter in der Query abzugleichen.
Genau dafür ist der Condition Agent Node gebaut.
## Was der Condition Agent Node anders macht
Der Condition Agent Node bietet AI-gesteuertes dynamisches Branching basierend auf natürlichsprachlichen Anweisungen und Kontext. Er verwendet ein Large Language Model, um den Workflow zu routen. Er analysiert bereitgestellte Input-Daten anhand einer Reihe nutzerdefinierter Szenarien, geführt von übergeordneten natürlichsprachlichen Anweisungen, die die Entscheidungsaufgabe definieren.
Das LLM bestimmt dann, welches Szenario am besten zum aktuellen Input-Kontext passt. Dieser Node ist besonders nützlich für Aufgaben wie Nutzer-Intent-Erkennung, komplexes Conditional Routing oder nuancierte situationsbezogene Entscheidungsfindung, bei denen einfache vordefinierte Regeln nicht ausreichen.
Der Unterschied in der Praxis:
[TABLE]
  |  | Condition Node | Condition Agent Node |
  | Wie er entscheidet | Bewertet eine feste Regel | Fragt ein LLM, den Intent zu klassifizieren |
  | Input | Ein zu vergleichender Wert | Eine Textbeschreibung der Entscheidungsaufgabe |
  | Routing-Grundlage | Keyword-Vorkommen oder Value-Match | Semantisches Verständnis der Bedeutung |
  | Geschwindigkeit | Sofort: kein Modellaufruf | Langsamer: erfordert einen Gemini API-Aufruf |
  | Geht mit Mehrdeutigkeit um | Nein | Ja |
  | Am besten geeignet für | Klare, eindeutige Trigger | Intent-basiertes oder nuanciertes Routing |
Für Meridians Routing-Problem ist der Condition Agent Node das richtige Tool.
## Was du baust
Einen aktualisierten Meridian Base Agent-Canvas, bei dem der Condition Node durch einen Condition Agent Node ersetzt wird. Die zwei Output-Pfade bleiben gleich:
- Pfad A: Knowledge- und Policy-Queries → Agent Node mit Document Store
- Pfad B: Live-Engagement-Statusanfragen → Platzhalter-Direct-Reply-Node
Die Routing-Entscheidung wird jetzt dadurch getroffen, dass Gemini die Absicht des Consultants interpretiert, statt durch eine Keyword-Regel.
### Schritt 1: Den Meridian-Base-Agent-Canvas öffnen
Öffne Flowise unter http://localhost:3000. Klicke auf Agentflows und öffne deinen Meridian Base Agent-Canvas.
Dein Canvas sollte so aussehen:
![image]((notion-hosted file))

### Schritt 2: Den Condition Node entfernen
Klicke auf den Condition Node, um ihn auszuwählen. Lösche ihn vom Canvas.
Lösche auch die Linien, die mit ihm verbunden waren:
- Die Linie vom Start Node zum Condition Node
- Die Linie vom True Output des Condition Nodes zu Direct Reply B
- Die Linie vom False Output des Condition Nodes zum Agent Node
Der Start Node, Agent Node, Direct Reply A und Direct Reply B sollten alle auf dem Canvas bleiben.
### Schritt 3: Einen Condition Agent Node hinzufügen
Klicke auf dem Canvas auf (+). Wähle unter der Kategorie Agentflow Condition Agent aus und füge ihn zum Canvas hinzu. Positioniere ihn an derselben Stelle, an der der Condition Node war: zwischen dem Start Node und dem Agent Node.
### Schritt 4: Den Condition Agent Node konfigurieren
Klicke auf den Condition Agent Node, um seine Einstellungen zu öffnen. Konfiguriere ihn wie folgt:
Model: Wähle Google Gemini aus und verbinde dein gespeichertes Gemini-Credential. Setze das Modell auf gemini-2.5-flash.
Instructions:
> Du bist ein Query-Klassifizierer für den internen Agenten von Meridian Consulting. Deine Aufgabe ist es zu bestimmen, ob die Query des Consultants Live-Engagement-Statusdaten für ein spezifisches Kundenprojekt anfordert oder ob sie nach Meridians internen Policies, Verfahren, Dokumentation oder allgemeinem Wissen fragt. Klassifiziere die Query nur dann als „status_request“, wenn der Consultant ausdrücklich nach dem aktuellen Live-Status, einem Fortschrittsupdate oder Echtzeitinformationen zu einem spezifisch benannten Kunden-Engagement oder Projekt fragt. Klassifiziere die Query als „knowledge_query“ für alles andere, einschließlich Fragen zu Meridians internen Policies, Verfahren, Eskalationsregeln, regionalen Richtlinien, Projektklassifizierung oder anderen Inhalten der Wissensdatenbank, selbst wenn das Wort „status“ in einem anderen Kontext in der Query vorkommt.
Input:
```powershell
{{ $flow.input }}
```
Scenarios: Füge zwei Szenarien in dieser Reihenfolge hinzu.
[TABLE]
  | Scenario | Label |
  | Scenario 0 | knowledge_query |
  | Scenario 1 | status_request |
### Schritt 5: Den Condition Agent Node verbinden
Verbinde alles so, dass es wie folgt aussieht.
![image]((notion-hosted file))

### Schritt 6: Den Flow State des Start Nodes aktualisieren
Klicke auf den Start Node und aktualisiere den Flow State, um einen zweiten Key hinzuzufügen, der die Routing-Entscheidung für die Nutzung durch nachgelagerte Nodes in späteren Sprints nachverfolgt:
[TABLE]
  | Key | Initial Value |
  | query_type | knowledge |
  | routing_decision | `` |
Der Key routing_decision startet leer und kann in zukünftigen Erweiterungen dieses Flows durch den Output des Condition Agent Nodes aktualisiert werden. Ihn jetzt zu initialisieren stellt sicher, dass er verfügbar ist, wenn er benötigt wird. Speichere die Start-Node-Einstellungen.
### Schritt 7: Speichern und den Routing-Test ausführen
Speichere den Canvas. Öffne das Chat-Symbol und führe die folgenden fünf Queries aus. Öffne zwischen jedem Test eine neue Chat-Session.
Test 1 - Klare Knowledge Query: What are the project classification tiers at Meridian?
- Erwartung: Routet zum Agent Node. Gibt Policy-Inhalte aus dem Document Store zurück.
Test 2 - Klare Statusanfrage: Can you check the engagement status for the Krauss account?
- Erwartung: Routet zu Direct Reply B. Gibt die Platzhalterantwort zurück.
Test 3 - Mehrdeutige Query mit „status“ in einem Policy-Kontext: What is the escalation status procedure for severity level 2 issues?
- Erwartung: Routet zum Agent Node. Der Condition Agent Node interpretiert dies als Knowledge Query, da der Nutzer nach einem Verfahren fragt und nicht nach Live-Projektdaten. Genau diese Query ist zuvor fehlgeschlagen.
Test 4 - Regionale Knowledge Query: What should I know about running an engagement in Poland?
- Erwartung: Routet zum Agent Node. Gibt Inhalte aus dem Regional Playbook zurück.
Test 5 - Ausdrückliche Live-Datenanfrage: What is the current progress on the Bauer Manufacturing engagement?
- Erwartung: Routet zu Direct Reply B. Der Condition Agent Node erkennt dies als Anfrage nach Live-Projektdaten.
### Checkliste: Vor dem Fortfahren bitte bestätigen
- [ ] Condition Node und seine Edges vom Canvas entfernt
- [ ] Condition Agent Node hinzugefügt und zwischen Start Node und Agent Node positioniert
- [ ] Modell Gemini 2.5 Flash mit gespeichertem Credential konfiguriert
- [ ] Instructions-Feld mit dem vollständigen Klassifizierungs-Prompt ausgefüllt
- [ ] Input-Feld auf {{ $flow.input }} gesetzt
- [ ] Zwei Szenarien knowledge_query und status_request in der richtigen Reihenfolge konfiguriert
- [ ] Start Node mit Condition Agent Node verbunden
- [ ] knowledge_query-Output mit Agent Node verbunden
- [ ] status_request-Output mit Direct Reply B verbunden
- [ ] Key routing_decision zum Flow State im Start Node hinzugefügt
- [ ] Canvas vor dem Testen gespeichert
- [ ] Alle fünf Test-Queries ausgeführt
- [ ] Test 3 routet korrekt zum Agent Node und bestätigt, dass intent-basiertes Routing funktioniert

> 💡 Takeaway: 
  Der Condition Agent Node trifft Routing-Entscheidungen wie ein Mensch: Er versteht, was der Consultant erreichen möchte, statt nur Wörter abzugleichen.
  Das hat seinen Preis: Jede Entscheidung erfordert einen Gemini API-Aufruf. Das erzeugt Latenz im Vergleich zur sofortigen Regelprüfung des Condition Nodes. Welcher Knoten der richtige ist, hängt von deinem Problem ab: Nutze den Condition Node bei klaren, eindeutigen Triggern. Zählt der Intent mehr als Keywords, wähle den Condition Agent Node.
