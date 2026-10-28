# Informationen zur Projektabgabe

Notion page: https://app.notion.com/p/Informationen-zur-Projektabgabe-3c79418319f3818ea05be923cfafefba
Backed up before n8n migration

## 1. Intro
Das Modulprojekt ist der interne Support-Agent von Meridian Consulting: ein Agentflow v2 auf einer selbst gehosteten Flowise-Instanz, der Fragen der Consultants aus dem Material der Firma beantwortet, den Live-Status von Engagements abruft, vor folgenreichen Aktionen auf menschliche Freigabe wartet und innerhalb des Scope bleibt, den Meridian für ihn gesetzt hat. Über vier Sprints hinweg hast du ihn Fähigkeit für Fähigkeit auf einer einzigen Canvas gebaut, Meridian Base Agent, und in Sprint 4 so weit gebracht, dass er den Kontakt mit einem Stakeholder übersteht.
Die Fähigkeiten, die du über das Modul hinweg geübt hast:
- Einen System-Prompt schreiben, der Rolle, Scope, harte Grenzen und Eskalationsverhalten festlegt — und ihn dann gegen Prompts testen, die genau diese Grenzen überschreiten wollen
- Die Antworten eines Agenten in einem Document Store verankern, damit sie aus Meridians eigenem Material kommen und nicht aus den Trainingsdaten des Modells
- Eine Anfrage mit einem Condition Agent Node an die richtige Fähigkeit routen und jedem Pfad einen eigenen Spezialagenten mit nicht überlappendem Prompt geben
- Eine Live-Datenquelle über einen HTTP Node anbinden und das Verhalten für den Fall entwerfen, dass diese Quelle ausfällt
- Einen Human Input Node als Freigabe-Gate, Retry-Logik und Sub-Flow-Aufrufe ergänzen, damit der Flow kontrolliert degradiert statt zu raten
- Eine Canvas end-to-end über mehrere getrennte Sessions validieren, statt nur zu prüfen, ob die einzelnen Nodes konfiguriert sind
- Eine Plattformentscheidung gegen benannte Alternativen verteidigen — anhand der Kriterien, die für das Business tatsächlich zählen
Die Canvas, die du abgibst, ist die verfeinerte Version derjenigen, die du die ganze Zeit gebaut hast, kein Neuaufbau. Bewertet wird, ob sie sich so verhält, wie du es beschreibst, und ob du erklären kannst, warum sie so gebaut ist, wie sie gebaut ist.
## 2. Aufgaben
Das ist die Arbeit, auf der die Abgabe aufbaut, Sprint für Sprint.
1. Sprint 1: Fundament und Verhalten. Die Flowise- und Qdrant-Container aufsetzen, die Gemini- und OpenRouter-Credentials verbinden und Meridian Base Agent als Start Node → Agent Node → Direct Reply Node bauen. Den System-Prompt mit den drei Säulen schreiben: Rolle und Persona, Scope, Limitationen und Eskalation. In einer einzigen durchgehenden Session gegen Kontexterhalt, Scope-Durchsetzung und Grenzbeachtung testen.
1. Sprint 2: Wissen, Routing und Tools. Den Document Store meridian-knowledge aus den drei Meridian-Quelldateien aufbauen und Retrieval dagegen verifizieren. Den System-Prompt auf vier Elemente umschreiben und Routing-Anweisungen sowie die definierte Fallback-Formulierung ergänzen. Intent-basiertes Routing mit einem Condition Agent Node hinzufügen und den Live-Pfad verdrahten: HTTP Node → Agent Node B → Direct Reply B. Den Sechs-Exchange-Session-Test durchführen, inklusive eines absichtlich erzeugten HTTP-Fehlers.
1. Sprint 3: Orchestrierung. Das Human-Input-Freigabe-Gate, den Retry-Zähler im Custom Function Node, den Loop Node und den Iteration-Sub-Flow Meridian Engagement Briefing ergänzen. Flow State seeden. Die Canvas-Verifikationsliste durchgehen und dann den Fünf-Exchange-Session-Test mit Freigabe, Ablehnung und erzwungenem Fehler fahren.
1. Sprint 4: Refinement, Validierung und Vergleich. Die drei dokumentierten Fehler beheben: die Modellkonfiguration hinter dem Latenz- und Kostenproblem, das Fehlrouting durch schwache Tool- und Knowledge-Beschreibungen und den erfundenen Status bei einem fehlgeschlagenen Lookup. Jeden Fix einzeln validieren. Den Sieben-Exchange-End-to-End-Test über drei getrennte Sessions fahren, bis alle sieben bestehen. Dann die Plattform-Vergleichsmatrix und das Justification Brief, das Business-Readiness-Audit, das Fünf-Turn-Demo-Skript und die schriftliche Plattform-Verteidigung erstellen.
## 3. Projektartefakte
Drei Ebenen: was du gebaut hast, der Nachweis, dass es funktioniert, und wie gut du die Entscheidungen dahinter erklären kannst.
### Technische Artefakte
Bis zum Abgabetag solltest du Folgendes haben:
- Die Canvas als JSON exportiert — die Version, die alle sieben End-to-End-Exchanges bestanden hat, ladbar in einer frischen Flowise-Instanz ohne fehlende Konfiguration.
- Den System-Prompt im Stand nach dem Refinement aus Sprint 4 — die vier Elemente plus die Ergänzung zur ehrlichen Fehlerbenennung.
- Die Dokumentation der Document-Store-Konfiguration — die drei Quelldateien mit ihren source-Metadatenwerten sowie die Embeddings-, Vector-Store- und Record-Manager-Einstellungen beim Upsert.
- Die Ergebnistabelle des End-to-End-Tests aus Sprint 4 — sieben Zeilen, jeweils mit genommenem Pfad, Pass oder Fail und Notizen.
- Die drei Refinement-Notizen aus Sprint 4 — die Änderung der Modellkonfiguration mit der projizierten monatlichen Kostenwirkung, die neu geschriebenen Beschreibungen für Describe Knowledge und den HTTP Node sowie die Ergänzung im System-Prompt.
- Die Plattform-Vergleichsmatrix — vier Plattformen gegen Meridians fünf Bewertungskriterien — und das dreiteilige Justification Brief, adressiert an Meridians CTO.
- Den Business-Readiness-Auditbericht — 250 bis 300 Wörter über die fünf Dimensionen, jede mit einem konkreten architektonischen Fix.
- Das Fünf-Turn-Demo-Skript und die schriftliche Plattform-Verteidigung.
### Analytisches Reasoning
Für deine Präsentation solltest du erklären können:
- Warum die Routing-Entscheidung in einem Condition Agent Node liegt und nicht in Keyword-Matching. Was hat sich im Verhalten des Agenten geändert, als du sie dorthin verlegt hast?
- Was der Agent tut, wenn der Live-Lookup fehlschlägt — und warum dieses Verhalten entworfen wurde, statt es dem Modell zu überlassen.
- Warum das Freigabe-Gate dort sitzt, wo es sitzt. Was würde schiefgehen, wenn der Flow zuerst handelt und danach berichtet?
- Was die sieben End-to-End-Exchanges belegt haben — und was sie nicht abgedeckt haben.
- Warum Flowise für Meridian die richtige Plattform war, welche der drei Alternativen am nächsten kam und an welchem Kriterium sie gescheitert ist.
- Was sich ändern müsste, damit diese Canvas 43 Consultants in drei Jurisdiktionen bedient und nicht eine Lernende auf http://localhost:3000.
### Schriftliche Zusammenfassung
Ein kurzes PDF, ein bis zwei Seiten, das das ganze Projekt zusammenbindet. Enthalten sein sollte:
- Ein Absatz zur Problemrahmung: was Meridians Consultants gemacht haben, bevor es den Agenten gab, und warum die Firma ihn wollte.
- Ein Absatz als Lösungsüberblick: die Pfade, die eine Anfrage durch die Canvas nehmen kann, und wo sie enden kann.
- Zwei oder drei Bulletpoints, die die folgenreichsten Entscheidungen der vier Sprints benennen — mit der Alternative, die du erwogen und verworfen hast.
- Ein Absatz Reflexion darüber, was der End-to-End-Test sichtbar gemacht hat, und eine Limitation, die du nicht auflösen konntest.
Die Zusammenfassung ist für jemanden, der deine Präsentation nicht gesehen hat. Sie muss für sich allein lesbar sein.
## 4. Präsentationskontext
Die Präsentation ist verpflichtend und die zentrale Bewertungsmethode für dieses Projekt.
Format: Live, vor der Kohorte, mit Q&A. Dein Instructor bestätigt die genaue Länge deines Slots.
Die Präsentation hat drei Komponenten. Alle drei sind erforderlich. Eine Demonstration ohne die Plattform-Verteidigung, oder eine Verteidigung ohne die laufende Canvas dahinter, ist unvollständig.
### Komponente 1: Die Canvas, live
Führe das Demo-Skript gegen die laufende Canvas aus. Die fünf Turns decken Knowledge Retrieval, Kontexterhalt über Turns hinweg, Live-Lookup mit Freigabe-Gate, kontrolliertes Scheitern und eine Scope-Grenze ab — in einer durchgehenden Session. Der Execution Trace in Flowise zeigt, welche Nodes aktiviert wurden und in welcher Reihenfolge, und genau das liest der Raum neben dem Antworttext mit.
Vor der Präsentation bestätigen: beide Container laufen, der HTTP Node zeigt nach den Fehlertests wieder auf den funktionierenden Endpunkt, und die Canvas ist ohne ungespeicherte Änderungen gespeichert.
### Komponente 2: Die Plattform-Verteidigung
Die drei Argumente, in dieser Reihenfolge: warum selbst gehostetes Flowise der richtige Produktionsweg ist, warum die kostenlose Modell-Stufe ein Upgrade braucht, bevor echte Client-Daten darüber laufen, und warum Copilot Studio speziell für Meridian nicht passt. Verankere jedes Argument in Meridians Rahmenbedingungen — ein JavaScript- und TypeScript-Team ohne Python-Data-Engineers, kein Microsoft-365-Bestand, die Self-Hosting-Anforderung und Clients in drei EU-Jurisdiktionen.
### Komponente 3: Die Readiness-Einschätzung
Was der End-to-End-Test belegt hat und was dir das Business-Readiness-Audit über das Lesen eines Agenten beigebracht hat, den du nicht selbst gebaut hast. Benenne die Lücke zwischen Prototyp und Produktion ehrlich: Canvas-Logik, System-Prompt, Document-Store-Konfiguration und Routing-Architektur tragen weiter. Die Infrastrukturebene nicht.
### Vorgeschlagener Aufbau
- Beginne mit Meridians Problem in einem Satz und der Form der Canvas in einem weiteren.
- Führe das Demo-Skript live aus und kommentiere den Trace, während er läuft — welcher Node klassifiziert, welcher Spezialagent antwortet, wo der Flow auf Freigabe wartet.
- Benenne zwei oder drei Erkenntnisse aus dem End-to-End-Test: eine, die eine Designentscheidung bestätigt hat, und eine, die eine Lücke sichtbar gemacht und eine Änderung erzwungen hat.
- Gib die Plattform-Verteidigung, drei Argumente in Reihenfolge.
- Schließe mit dem, was vor echtem Einsatz noch fehlt, und nimm dann Fragen.
Fokussiere dich auf Reasoning und Kommunikation. Die Präsentation ist keine Node-by-Node-Tour. Öffne nicht jedes Konfigurationspanel. Lies den System-Prompt nicht laut vor. Zeige das Denken hinter der Architektur — die Entscheidungen, die du getroffen hast, warum du sie getroffen hast, und was du anders machen würdest.
## 5. Qualitätsanforderungen / Bewertung
Deine Bewertung basiert auf der Präsentation, gestützt durch die abgegebenen Artefakte. Die Artefakte erlauben dem Reviewer zu überprüfen, was du sagst, und deine Canvas bei Bedarf auszuführen.
Die Bewertung umfasst fünf Dimensionen:
[TABLE]
  | Dimension | Worauf der Evaluator achtet |
  | Abdeckung der Fähigkeiten | Übt die Canvas Retrieval, Intent-Routing, Live-Lookup, Freigabe-Gate, Retry und die Scope-Grenze tatsächlich aus — oder ist manches konfiguriert, aber nie demonstriert? |
  | Fehlerverhalten | Benennt der Agent beim Ausfall der Live-Quelle den Fehler und bietet einen konstruktiven nächsten Schritt, oder erfindet er einen Status? War dieses Verhalten entworfen oder Zufall? |
  | Qualität der Evidenz | Sind die sieben Exchanges mit dem erwarteten Pfad vor dem Lauf und dem tatsächlichen Verhalten nach dem Lauf dokumentiert? Zeigt der Testnachweis, dass die Canvas ausgeführt und nicht nur beschrieben wurde? |
  | Begründung der Entscheidungen | Ist jede Entscheidung in etwas Spezifischem über Meridian verankert — der Stack des Teams, die Jurisdiktionen, das fehlende Microsoft-Bestand — oder auf der Ebene allgemeiner Prinzipien formuliert? |
  | Produktionsurteil | Kann die Lernende benennen, was fehlt, bevor 43 Consultants das nutzen, und unterscheiden, was weiterträgt und was neu gebaut werden muss? |
Es gibt keine einzige richtige Canvas. Die Bewertung prüft nicht, ob deine Routing-Logik der von jemand anderem entspricht. Sie prüft, ob der Agent, den du gebaut hast, sich wie spezifiziert verhält, ehrlich scheitert und gegen die Alternativen verteidigt werden kann, die du verworfen hast.
## 6. Vorbereitungsliste
Erledige diese Punkte vor der Abgabe und der Live Session. Lass keinen Punkt für den Präsentationstag selbst übrig.
- [ ] Alle sieben End-to-End-Exchanges bestehen, Ergebnistabelle ausgefüllt
- [ ] HTTP-Node-URL nach den Fehlertests auf den funktionierenden Endpunkt zurückgesetzt
- [ ] Canvas gespeichert, und docker ps zeigt die Container flowise und qdrant als laufend
- [ ] docker logs flowise --tail 20 geprüft — keine Fehler und keine 429-Rate-Limit-Meldungen kurz vor deinem Slot
- [ ] Canvas als JSON exportiert und in einer frischen Flowise-Instanz als ladbar bestätigt
- [ ] Demo-Skript einmal gegen die laufende Canvas geprobt, nicht von der Seite abgelesen
- [ ] Plattform-Verteidigung durchgegangen, sodass alle drei Argumente ohne Notizen sitzen
- [ ] Schriftliche Zusammenfassung entworfen, ein bis zwei Seiten, als PDF exportiert
- [ ] Keine API-Keys oder Credential-Werte im Export oder in den Dokumenten
## 7. Abgabe- / Lieferanweisungen
Die Abgabe dient Zugriff und Review. Die Bewertung findet während der Präsentation statt. Das sind zwei getrennte Schritte.
### Was abgegeben werden muss
Bündle alles in einem einzigen Abgabepaket (einem geteilten Google-Drive-Ordner):
1. Die Canvas als JSON exportiert.
1. Ein Dokument (.md oder .pdf) mit den folgenden Inhalten, in dieser Reihenfolge:
  1. Den System-Prompt nach dem Refinement
  1. Die Dokumentation der Document-Store-Konfiguration
  1. Die Ergebnistabelle des End-to-End-Tests
  1. Die drei Refinement-Notizen aus Sprint 4
  1. Die Plattform-Vergleichsmatrix und das Justification Brief
  1. Den Business-Readiness-Auditbericht
  1. Das Fünf-Turn-Demo-Skript
  1. Die schriftliche Plattform-Verteidigung
1. Die schriftliche Zusammenfassung als PDF.
### Wo und wann
Gib deine Arbeit als Link auf einen Google-Drive-Ordner ab. Lege alle Artefakte hinein und teile den Link in der Abgabelektion.
> ⚠️ Wichtig: Stelle sicher, dass die Ordnerberechtigungen es allen Personen mit dem Link erlauben, jede Datei darin zu öffnen. Teste den Link in einem Inkognito-Fenster, bevor du ihn abgibst. Nimm keine API-Keys oder Credential-Werte in den Export oder in die Dokumente auf.
### Was nicht Teil der Bewertung ist
- Teilnahme an der Code Clinic. Nicht bewertet.
- Die Anzahl der Artefakte, die du über die gelisteten hinaus produzierst.
- Die visuelle Politur deiner Slides. Klare Gedanken zählen mehr als schöne Slides — was nicht heißt, dass sie lieblos zusammengestellt sein sollten.
## Finaler Check
Lies vor deiner Präsentation dein Demo-Skript und die Plattform-Verteidigung durch und stelle dir diese Fragen. Sie sind nah an den Fragen, die der Instructor stellen wird.
- Kannst du den Pfad benennen, den eine Anfrage durch die Canvas nimmt, ohne Flowise zu öffnen?
- Zeigt das Demo-Skript, dass der Agent einen fehlgeschlagenen Lookup benennt, statt einen Status zu erfinden?
- Kannst du sagen, welches der fünf Vergleichskriterien für Meridian am meisten zählte, und warum?
- Benennt das Readiness-Audit für jede der fünf Dimensionen einen konkreten architektonischen Fix, nicht nur das Problem?
- Kannst du eine Sache benennen, die der Sieben-Exchange-Test nicht abgedeckt hat?
Wenn eine dieser Fragen Unsicherheit auslöst, ist das nützliche Information. Eine Limitation, die du präzise beschreiben kannst, ist stärker als die Behauptung, alles sei gelöst.
## Zusammenfassung
Das Modulprojekt bewegt sich von einer Drei-Node-Canvas, die eine Frage beantwortet, zu einem Agenten, der aus dem Material der Firma abruft, nach Intent routet, Live-Daten prüft, vor dem Handeln auf einen Menschen wartet und die Fragen ablehnt, die nicht seine Aufgabe sind. In Sprint 4 hörte er auf, ein Build zu sein, und wurde zu etwas, das man einem Stakeholder zeigen kann.
Worauf es jetzt ankommt, ist nicht ein weiterer Node. Es ist, die Canvas sauber ausführen zu können, zu benennen, wofür jede Designentscheidung da war, und ehrlich zu sagen, was sich ändern müsste, damit Meridians Consultants sich darauf verlassen können.