# Den Document Store mit dem Agent Node verbinden

Notion page: https://app.notion.com/p/Den-Document-Store-mit-dem-Agent-Node-verbinden-3789418319f380d498f5e9d78796669d
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Die Studierenden verbinden den Document Store meridian-knowledge mit dem Agent Node auf dem Agentflow-v2-Canvas und überprüfen, dass der Agent Wissen daraus abrufen und verwenden kann.

## Den Kontext herstellen
Meridians Document Store meridian-knowledge ist befüllt, “upserted” und überprüft. Die drei internen Dokumente (Operations Handbook, Engagement Standards und Regional Playbook) sind gechunkt, eingebettet und in Qdrant gespeichert. Die Retrieval-Test-Queries haben bestätigt, dass die richtigen Chunks für die richtigen Fragen zurückkommen. Aber der Agent kann weiterhin auf nichts davon zugreifen.
Der Document Store und der Agentflow-v2-Canvas existieren unabhängig voneinander. Ein Consultant, der den Agenten nach Eskalationsverfahren fragt, erhält weiterhin eine allgemeine Antwort aus Geminis Trainingsdaten, nicht aus Meridians tatsächlichen Standards.
Diese Lektion verbindet die beiden. Am Ende wird der Meridian-Agent präzise Inhalte aus seiner eigenen internen Dokumentation abrufen und sie verwenden, um Consultant-Queries fundiert in echten Policies zu beantworten.
## Was du baust
Einen aktualisierten Meridian Base Agent Agentflow v2, bei dem der Agent Node mit dem Document Store meridian-knowledge als Wissensquelle konfiguriert ist. Die Canvas-Struktur bleibt bei drei Nodes (Start Node, Agent Node, Direct Reply Node), wobei der Knowledge Retrieval innerhalb der Agent-Node-Konfiguration hinzugefügt wird.
### Schritt 1: Den Meridian-Base-Agent-Canvas öffnen
Öffne Flowise unter http://localhost:3000. Klicke in der linken Navigation auf Agentflows und öffne deinen Meridian Base Agent-Canvas.
Dein Canvas sollte den Drei-Node-Flow aus Sprint 1 zeigen: Start Node → Agent Node → Direct Reply Node
Wenn der Canvas fehlt oder nicht gespeichert wurde, baue ihn anhand der vorherigen Lektionen erneut auf.
### Schritt 2: Die Agent-Node-Einstellungen öffnen
Klicke auf den Agent Node auf dem Canvas, um rechts auf dem Bildschirm sein Einstellungs-Panel zu öffnen.
Scrolle durch die Einstellungen nach unten, bis du den Abschnitt Knowledge findest. Er enthält zwei Unterabschnitte:
- Knowledge / Document Stores zum Verbinden von Flowise-verwalteten Document Stores
- Knowledge / Vector Embeddings zum direkten Verbinden externer Vektordatenbanken
Für diese Lektion verwendest du Knowledge / Document Stores.
### Schritt 3: Den Document Store verbinden
Klicke im Unterabschnitt Knowledge / Document Stores auf + Add Item.
Konfiguriere die zwei Felder, die erscheinen:
[TABLE]
  | Feld | Wert |
  | Document Store | Wähle meridian-knowledge aus dem Dropdown aus |
  | Describe Knowledge | Interne Dokumentation von Meridian Consulting: Projektklassifizierungsstufen und Staffing-Regeln, Severity Ratings und Eskalationsverfahren, Standards für Kundenkommunikation und Vertraulichkeit, Knowledge-Sharing-Protokolle und regionale operative Richtlinien für Deutschland, Polen, Tschechien und die nordischen Märkte, einschließlich Regeln für länderübergreifende Engagements. |
![image]((notion-hosted file))
> ⚠️ Warum die Beschreibung wichtig ist: Das Feld Describe Knowledge liefert eine natürlichsprachliche Beschreibung des Inhalts und Zwecks des Document Stores. Diese Beschreibung hilft dem Agenten zu verstehen, welche Art von Informationen der Store enthält und wann es angemessen wäre, ihn abzufragen. Eine vage Beschreibung erzeugt falsche Routing-Entscheidungen. Eine präzise Beschreibung sagt dem Agenten genau, wann er aus diesem Store abrufen soll und wann er aus allgemeinem Reasoning antworten soll.

### Schritt 4: Den System-Prompt aktualisieren
Klicke in den Agent-Node-Einstellungen auf den Abschnitt Messages. Aktualisiere den System-Prompt, sodass er ausdrückliche Anleitung zum Knowledge Retrieval enthält.
Füge die folgende Anweisung nach der Rollen- und Scope-Definition zum bestehenden System-Prompt hinzu:
> Wenn ein Consultant nach Meridians internen Policies, Verfahren, Eskalationsregeln, Projektklassifizierung, Knowledge-Sharing-Anforderungen oder regionalen operativen Richtlinien fragt, rufe die relevanten Informationen aus deiner Wissensdatenbank ab, bevor du antwortest. Verankere deine Antwort immer in den abgerufenen Inhalten. Wenn die Wissensdatenbank die benötigte Information nicht enthält, sage das klar und schlage vor, dass der Consultant sich direkt an Meridians Knowledge-Management-Team wendet.
![image]((notion-hosted file))
> ⚠️ Warum diese Anweisung nötig ist: Ohne ausdrückliche Anleitung kann der Agent Policy-Fragen aus Geminis allgemeinen Trainingsdaten beantworten, statt aus dem Document Store abzurufen. Diese Anweisung sagt dem Agenten, wann er die Wissensquelle verwenden soll und was er tun soll, wenn er die Antwort nicht findet.

### Schritt 5: Den Direct Reply Node aktualisieren
Klicke auf den Direct Reply Node, um seine Einstellungen zu öffnen. Bestätige, dass das Feld Message auf die Output-Variable des Agent Nodes gesetzt ist:
```powershell
{{ agentAgentflow_0.output }}
```
Wenn es leer ist oder auf eine andere Variable gesetzt ist, aktualisiere es jetzt. Speichere den Canvas.
### Schritt 6: Den Knowledge-Retrieval-Test ausführen
Klicke oben rechts auf das Chat-Symbol, um die eingebaute Testoberfläche zu öffnen. Führe die folgenden vier Queries in einer einzigen Session aus:
Query 1 - Policy Retrieval: What are the three project classification tiers at Meridian and what does each one cover?
- Erwartetes Verhalten: Der Agent ruft aus dem Document Store ab und antwortet mit den Definitionen für Tier 1, Tier 2 und Tier 3 aus dem Operations Handbook. Er erfindet keine zusätzlichen Tiers und keine Klassifizierungskriterien.
Query 2 - Procedural Retrieval: How quickly does a severity level 2 client issue need to be escalated?
- Erwartetes Verhalten: Der Agent ruft das Eskalationsverfahren aus dem Dokument Engagement Standards ab und antwortet mit der Anforderung von vier Arbeitsstunden.
Query 3 - Regional Context Retrieval: What should I know about running an engagement in Poland?
- Erwartetes Verhalten: Der Agent ruft den Polen-Abschnitt aus dem Regional Playbook ab und behandelt Sprachpräferenzen und Engagement-Tempo.
Query 4 - Knowledge Base Gap: What is Meridian's remote work policy for consultants?
- Erwartetes Verhalten: Die Frage liegt im Scope (eine interne Meridian-Policy, nach der ein Consultant vernünftigerweise fragen könnte), aber die Antwort befindet sich nicht im Document Store. Der Agent sollte die Lücke erkennen, sie klar benennen und vorschlagen, sich direkt an Meridians Knowledge-Management-Team zu wenden, genauso wie im System-Prompt angewiesen. Er sollte keine Policy aus allgemeinem Trainingswissen erfinden.
### Worauf du achten solltest
Für Queries 1 bis 3 sollte die Antwort des Agenten:
- Spezifische Details enthalten, die nur in den synthetischen Dokumenten existieren; keine generischen Consulting-Ratschläge
- Dem Inhalt des relevanten Dokumentabschnitts eng entsprechen
- Keine Informationen hinzufügen, die nicht in den Dokumenten stehen
Wenn der Agent bei einer der Queries 1 bis 3 eine generische Antwort zurückgibt, wird der Document Store nicht abgefragt. Prüfe Folgendes der Reihe nach:
- Bestätige, dass der Document Store meridian-knowledge in der Knowledge-Konfiguration des Agent Nodes ausgewählt ist
- Bestätige, dass das Feld Describe Knowledge ausgefüllt ist
- Bestätige, dass der Canvas vor dem Testen gespeichert wurde
- Bestätige, dass der Upsert erfolgreich abgeschlossen wurde
### Checkliste: Vor dem Fortfahren bestätigen
- [ ] Meridian Base AgentCanvas geöffnet und zeigt Start Node → Agent Node → Direct Reply Node
- [ ] Document Store meridian-knowledge im Abschnitt Agent Node Knowledge / Document Stores verbunden
- [ ] Feld Describe Knowledge mit einer präzisen Beschreibung des Store-Inhalts ausgefüllt
- [ ] System-Prompt mit ausdrücklicher Knowledge-Retrieval-Anweisung aktualisiert
- [ ] Message-Feld des Direct Reply Nodes auf {{ agentAgentflow_0.output }} gesetzt
- [ ] Canvas vor dem Testen gespeichert
- [ ] Alle vier Test-Queries ausgeführt und bewertet
- [ ] Queries 1 bis 3 geben Inhalte zurück, die in den synthetischen Dokumenten verankert sind
- [ ] Query 4 gibt den Knowledge-Gap-Fallback zurück

> 💡 Takeaway: 
  Einen Document Store mit einem Agent Node zu verbinden, benötigt zwei Eingaben: die Store-Auswahl und die Wissensbeschreibung. Die Store-Auswahl sagt Flowise, woher abgerufen werden soll. Die Beschreibung sagt dem Agenten, wann er abrufen soll und was er dort zu finden erwarten kann. Beides muss präzise sein.
  Eine verbundene, aber schlecht beschriebene Wissensquelle erzeugt einen Agenten, der seine eigene Wissensdatenbank ignoriert und auf allgemeines Reasoning zurückfällt, was nicht davon zu unterscheiden ist, den Store gar nicht verbunden zu haben.
