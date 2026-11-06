# Informationen zur Projektabgabe

Notion page: https://app.notion.com/p/Informationen-zur-Projektabgabe-7669418319f3821da62101eb282bd28a
Backed up before n8n migration

Diese Seite ist die verbindliche Checkliste für die allgemeine AI-Capstone-Abgabe. Sie deckt die Artefakte ab, die jede lernende Person einreicht – unabhängig davon, ob das Projekt allein oder in einer Gruppe durchgeführt wurde und ob der Workflow lokal läuft oder extern gehostet wird.
Externes Hosting ist optional. Eine funktionsfähige Ausführung, vollständige Evidenz und die Veröffentlichung der Portfolio-Artefakte sind erforderlich.
## 1. Aufgaben
Vier Sprints Arbeit, wobei jeder Artefakte erzeugt, die auf den vorherigen aufbauen. Die Abgabe stützt sich auf alle vier.
1. Sprint 1 — Problemabgrenzung und Design. Wähle ein Geschäftsproblem oder eine Fallback-Option und grenze es ein. Definiere messbare Erfolgskriterien. Entscheide, welche Konzepte der Build braucht – RAG, Agent, agentischer Workflow, Human-in-the-Loop – und welcher Implementierungsweg passt. Erstelle Architektur und Build-Plan und führe beides durch ein Peer-Review.
1. Sprint 2 — Das Kernsystem aufbauen. Richte die Umgebung ein und verbinde jede Datenquelle – echt oder klar als synthetisch gekennzeichnet. Baue einen schlanken, funktionsfähigen End-to-End-Ausschnitt, iteriere daran, bis er zuverlässig ist, und integriere die AI-Komponenten, die deine Architektur vorsieht. Führe den Mid-Build-Checkpoint mit 5–10 diagnostischen Fällen durch und passe den Plan an die Ergebnisse an.
1. Sprint 3 — Fertigstellen, Governance und Evaluation. Ergänze Sicherheits-, Zuverlässigkeits- und menschliche Aufsichtsschichten. Führe die formale Evaluation mit mindestens 10 unterschiedlichen Szenarien und vollständiger Dokumentation durch. Identifiziere den wichtigsten Fehlermodus und schreibe den Verbesserungsplan. Schließe die Governance-Arbeit ab: EU-AI-Act-Klassifikation, Datenschutzentscheidungen und Responsible-AI-Checkliste. Veröffentliche die Projektartefakte auf GitHub.
1. Sprint 4 — Präsentation und Reflexion. Berechne den ROI und halte Messwerte und Annahmen sichtbar getrennt. Schreibe den einseitigen Business Case. Bereite Präsentation, Live-Demonstration und deine Antworten auf die geschäftlichen und technischen Fragen vor, die daraus entstehen.
## 2. Bestätigen, dass das Projekt vollständig ist
Bevor du die Abgabe zusammenstellst, bestätige, dass der finale Workflow:
- mit einem repräsentativen Input End-to-End läuft;
- den erwarteten Output erzeugt;
- der exportierten Workflow-JSON entspricht;
- Governance- und Sicherheitsprüfungen abgeschlossen hat;
- formale Evaluationsevidenz aus mindestens 10 unterschiedlichen Szenarien enthält;
- keine offengelegten Credentials, API-Keys, privaten Tokens oder vertraulichen Datensätze enthält.
## 3. Projektartefakte
### Technische Artefakte
Füge Folgendes hinzu:
- die exportierte n8n-Workflow-.json;
- den Link zum GitHub-Repository;
- das README/die Projektbeschreibung;
- das finale Architekturdiagramm;
- Screenshots oder eine kurze Demo-Aufzeichnung mit erfolgreicher Ausführung;
- Import-/Review-Anweisungen für den Workflow;
- optional einen Link zum gehosteten System, nur wenn du externes Hosting gewählt hast.
Das Architekturdiagramm muss die tatsächlichen Komponenten und den Datenfluss des finalen Workflows zeigen. Eine Tabelle oder nummerierte Liste kann es ergänzen, ersetzt es aber nicht.
### Evidenz und Begründung
Füge Folgendes hinzu:
- die formale Testszenario-Dokumentation mit allen erforderlichen Feldern;
- den Evaluierungsbericht;
- den wichtigsten Fehlermodus und den Verbesserungsplan;
- die für das Projekt relevante Evidenz zu Responsible AI, Datenschutz, Sicherheit und Governance;
- die ROI-Berechnung und den einseitigen Business Case;
- bekannte Einschränkungen sowie offengelegte Annahmen zu Mocks oder synthetischen Daten.
Halte Messwerte und Annahmen getrennt. Kennzeichne synthetische Inputs, verbleibende Mocks, nicht quantifizierbare Kosten und alle optionalen Features, die nicht abgeschlossen wurden, klar.
### Schriftliche Zusammenfassung
Eine kurze PDF von ein bis zwei Seiten, die das gesamte Projekt zusammenführt. Enthalten sein sollen:
- ein Absatz zur Problemrahmung – was das Geschäftsproblem ist und warum sich eine Automatisierung lohnt;
- ein Absatz zur Lösungsübersicht – was der Workflow tut und welche grundlegende Form er hat;
- zwei oder drei Bulletpoints zu den interessantesten Entscheidungen, die du über die vier Sprints hinweg getroffen hast, jeweils mit der Alternative, die du erwogen und verworfen hast;
- ein Absatz zur Reflexion darüber, was deine Tests gezeigt haben, und zu einer Einschränkung, die du nicht vollständig lösen konntest.
Die Zusammenfassung ist für jemanden gedacht, der deine Präsentation nicht gesehen hat. Sie muss eigenständig verständlich sein.
## 4. Präsentation
Ziel sind 5–7 Minuten für die Präsentation selbst plus Q&A. Dein Instructor bestätigt den genauen Slot für die Session.
Die Präsentation muss Folgendes enthalten:
- das Problem und warum es relevant ist;
- eine Live-Demonstration des Workflows;
- das finale Architekturdiagramm;
- Build- und Governance-Entscheidungen, die es wert sind, verteidigt zu werden;
- Evaluationsergebnisse einschließlich des wichtigsten Fehlermodus;
- Business Case, Einschränkungen und nächste Verbesserung.
Bereite einen sicheren Fallback-Screenshot oder eine Aufzeichnung vor, falls die Live-Umgebung ausfällt. Der Fallback unterstützt die Präsentation, ersetzt aber nicht die Vorbereitung einer funktionsfähigen Demonstration.
## 5. Qualitätsanforderungen
Das Projekt wird über die Präsentation und die Glaubwürdigkeit der unterstützenden Evidenz bewertet. Reviewer achten auf:
- ein klares, angemessen abgegrenztes Problem;
- einen funktionierenden und erklärbaren Workflow;
- ein korrektes Architekturdiagramm;
- vollständige und glaubwürdige Testevidenz;
- ehrliche Schlussfolgerungen und Einschränkungen;
- verantwortungsvollen Umgang mit Daten, Zugriffen, Secrets und menschlicher Aufsicht;
- einen belastbaren Business Case;
- die Fähigkeit, die wichtigsten Entscheidungen zu erklären und zu verteidigen.
Teilnahme an der Code Clinic, zusätzliche Artefakte über die Pflichtliste hinaus und dekorativer Slide-Feinschliff sind keine bewerteten Anforderungen.
## 6. Vorbereitungsliste
Schließe diese Punkte vor der Live-Session ab. Lass keinen davon bis zur Session selbst offen.
- [ ] Der Workflow läuft und die Evidenz zeigt Input, Ausführung und Output.
- [ ] Die exportierte .json entspricht dem finalen Workflow.
- [ ] Das GitHub-Repository ist öffentlich und vollständig.
- [ ] Das README enthält Problem, Lösung, Architektur, Review-/Ausführungsanweisungen, Evidenz und Einschränkungen.
- [ ] Das Architekturdiagramm entspricht dem tatsächlich gebauten Workflow.
- [ ] Die formale Evaluation enthält mindestens 10 vollständige Testdatensätze.
- [ ] Evaluierungsbericht, Business Case, ROI und Verbesserungsplan sind enthalten.
- [ ] Die Präsentation enthält eine Live-Demonstration und passt in den Zielzeitraum.
- [ ] Jede erforderliche Datei ist in Codio angehängt, und jeder eingereichte GitHub-Link bzw. optionale Link zum gehosteten System lässt sich in einem privaten Browserfenster öffnen.
- [ ] Kein Secret oder privater Datensatz wird offengelegt.
## 7. In Codio einreichen
Reiche das vollständige Projektpaket über die Course-6-Abgabeaktivität in Codio ein und folge dabei demselben Abgabeprozess wie bei den anderen Projekten des Programms.
Füge die schriftliche Projektzusammenfassung als PDF mit ungefähr 1–2 Seiten bei. Lade die erforderlichen Dateien hoch und gib den Link zum GitHub-Repository sowie gegebenenfalls den optionalen Link zum gehosteten System in den von der Codio-Aktivität vorgesehenen Feldern an.
Öffne vor dem Absenden die Codio-Abgabe noch einmal und bestätige, dass jede erforderliche Datei angehängt und jeder Link vollständig ist. Teste das GitHub-Repository sowie gegebenenfalls den optionalen Link zum gehosteten System in einem privaten oder Inkognito-Browserfenster.
Füge keine Credentials, API-Keys, privaten Tokens, privaten Organisationsdaten oder andere Secrets in den Workflow-Export, das Repository, Screenshots oder Dokumente ein.
Befolge jede operative Anweisung deines Instructors, ohne die oben genannte Pflichtliste der Artefakte zu verändern.
## Abschließender Check
Lies vor deiner Präsentation dein Architekturdiagramm und den Evaluierungsbericht noch einmal durch und stelle dir diese Fragen. Genau diese Fragen wird ein Reviewer während deiner Verteidigung stellen.
- Kannst du einen repräsentativen Input im Diagramm vom Trigger bis zum Output verfolgen und erklären, was jede Komponente damit macht?
- Entspricht das Diagramm dem Workflow, wie er jetzt tatsächlich aussieht, und nicht nur dem Stand aus der Designphase?
- Kannst du erklären, was das System bei einem fehlerhaft formatierten Input, einer fehlgeschlagenen Integration oder einer unsicheren AI-Komponente tut – und zeigen, wo das gebaut ist?
- Kannst du einen Test nennen, der dein Design verändert hat, und sagen, was dadurch geändert wurde?
- Kannst du deinen wichtigsten Fehlermodus laut aussprechen, ohne ihn weichzuzeichnen, und erklären, was du als Nächstes dagegen tun würdest?
- Wenn dich jemand fragt, warum du diesen Ansatz statt eines einfacheren gewählt hast: Kannst du auf eine konkrete Eigenschaft deines Geschäftsproblems verweisen statt nur auf ein allgemeines Prinzip?
Wenn dich eine dieser Fragen ins Stocken bringt, ist das nützliche Information. Nutze die Zeit vor der Session für genau den Punkt, bei dem du am meisten gezögert hast.
## Zusammenfassung
Deine Abgabe sollte es einem Reviewer ermöglichen, drei Dinge ohne Rätselraten zu verifizieren: Der Workflow funktioniert, die Evidenz stützt deine Aussagen und du verstehst Entscheidungen und Einschränkungen gut genug, um sie zu verteidigen. Packe nur bestätigte Artefakte ein und halte optionales Hosting klar getrennt von der erforderlichen Capstone-Evidenz.