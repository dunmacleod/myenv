# Das richtige Muster für einen Use Case auswählen

Notion page: https://app.notion.com/p/Das-richtige-Muster-f-r-einen-Use-Case-ausw-hlen-eec9418319f382429dd5816a5e76ed12
Backed up before n8n migration

An diesem Punkt hat Velas Team ein funktionierendes Designframework: einen Vier-Fragen-Test für Single-Agent vs. Multi-Agent, sechs benannte Muster zur Auswahl und drei Pfeiler, die bestimmen, ob ein Muster in der Produktion standhält. Selin hat das Framework genutzt, um zu bestätigen, dass Velas aktuelles Problem einen gut entworfenen Single-Agent erfordert.
Jetzt seid ihr dran, dasselbe Framework anzuwenden.
> 💡 Diese Lektion stellt vier Geschäftsszenarien vor. Jedes beschreibt ein reales operatives Problem, das ein Team mit einem Agenten lösen möchte. Eure Aufgabe: Das Entscheidungsframework für jedes Szenario durcharbeiten, das passende Architekturmuster benennen und eine kurze Begründung schreiben, die ein Kollege lesen und direkt umsetzen könnte.
In dieser Lektion baut ihr keine Canvas. Die Ausgabe ist euer Reasoning, klar genug dokumentiert, dass es zur Grundlage eines Architekturentscheidungs-Briefings werden könnte.
## Was ihr entscheidet
Beantwortet für jedes Szenario drei Fragen in dieser Reihenfolge:
1. Single-Agent oder Multi-Agent? Wendet das Vier-Fragen-Framework aus der vorherigen Lektion an. Benennt, welche Fragen die Entscheidung geprägt haben und warum.
2. Welches Muster? Benennt aus den sechs Mustern (Single-Agent, Tool-Using-Agent, Workflow + Agent, Router, Evaluator, Supervisor-Worker) dasjenige, das am besten passt. Wenn zwei plausibel sind, benennt beide und erklärt, welches ihr wählen würdet und warum.
3. Welche Pfeiler brauchen die meiste Aufmerksamkeit? Identifiziert aus den drei Pfeilern (Orchestrierung, Kommunikation, Zustandsverwaltung), welcher für diesen konkreten Use Case das bewussteste Design erfordert, und erklärt, welches Risiko entsteht, wenn er nicht gut behandelt wird.
## Die vier Szenarien
> 🔥 Bevor ihr beginnt, erstellt eine Kopie von dieser Vorlage. Sie spiegelt die Struktur dieser Lektion: ein Tab mit den vier Szenarien (Norda, Helio, Daven, Arco), jeweils mit Antwortfeldern zu den drei Fragen, plus ein kurzes Checkpoint-Tab.
### Szenario A: Norda Retail
Norda Retail ist ein mittelgroßer Bekleidungshändler mit Filialen in ganz Skandinavien. Das Kundenservice-Team erhält rund 400 Anfragen pro Tag über ein internes Chat-Tool. Etwa 60 % sind Fragen zum Bestellstatus („Wo ist meine Bestellung?"), 30 % sind Rückgabe- und Umtauschanfragen, und 10 % sind Beschwerden, die an einen menschlichen Agenten eskaliert werden müssen. Das Team möchte einen Agenten bauen, der alle drei Typen bearbeitet. Fragen zum Bestellstatus brauchen einen Live-Lookup im Order-Management-System. Rückgabe- und Umtauschanfragen folgen einer festen Richtlinie, die intern dokumentiert ist. Eskalationen müssen sofort markiert und mit einer Zusammenfassung übergeben werden.
Arbeitet die drei Fragen für Norda Retail durch. Schreibt eure Antworten, bevor ihr die Hinweise lest.
### Szenario B: Helio Engineering
Helio Engineering bietet technische Beratung für Projekte im Bereich erneuerbare Energien. Ein Consultant reicht eine Projekt-Scoping-Anfrage ein, typischerweise zwei bis drei Absätze, die den Kunden, das Problem und die Einschränkungen beschreiben. Die Aufgabe des Agenten ist es, ein strukturiertes Projekt-Briefing zu erstellen: eine Zusammenfassung des Problems, einen vorgeschlagenen Ansatz, eine Liste relevanter Fallstudien aus Helios interner Wissensdatenbank und einen Risikoabschnitt. Das Briefing muss von einem Senior Consultant geprüft werden, bevor es an den Kunden geht. Lehnt der Senior Consultant es ab, soll der Agent es überarbeiten und erneut einreichen. Die Revisionsschleife soll nach drei Versuchen stoppen.
Arbeitet die drei Fragen für Helio Engineering durch.
### Szenario C: Daven Logistics
Daven Logistics koordiniert Frachtbewegungen zwischen Lieferanten und Distributionszentren in ganz Mitteleuropa. Gesucht ist ein Agent, der eine tägliche Liste von zwanzig Sendungen überwacht, den aktuellen Status jeder Sendung über ihre Tracking-API prüft, jede Sendung markiert, die mehr als 24 Stunden verspätet ist, und einen täglichen Übersichtsbericht erstellt. Die Liste der Sendungen wird zu Beginn jedes Durchlaufs als strukturierte Daten bereitgestellt. Die Tracking-API gibt für jede Sendungs-ID einen Status und eine geschätzte Ankunftszeit zurück.
Arbeitet die drei Fragen für Daven Logistics durch.
### Szenario D: Arco Insurance
Arco Insurance bearbeitet gewerbliche Sachschadenansprüche. Wenn ein neuer Anspruch eingereicht wird, muss er drei Phasen durchlaufen, bevor ein menschlicher Schadenregulierer ihn prüft: eine initiale Vollständigkeitsprüfung (sind alle erforderlichen Dokumente vorhanden?), eine Prüfung auf Betrugssignale (passt der Anspruch zu bekannten Betrugsmustern?) und eine Deckungsprüfung (deckt die Police das ab, was geltend gemacht wird?). Jede Phase erzeugt eine strukturierte Ausgabe, von der die nächste Phase abhängt. Schlägt die Vollständigkeitsprüfung fehl, soll der Anspruch nicht zur Prüfung auf Betrugssignale weitergehen. Löst die Prüfung auf Betrugssignale eine Markierung aus, soll der Anspruch an ein Spezialteam eskaliert werden, statt mit der Deckungsprüfung fortzufahren.
Arbeitet die drei Fragen für Arco Insurance durch.
## Hinweise
  Nutzt diese erst, nachdem ihr eure eigenen Antworten geschrieben habt.
  Szenario A: Drei unterschiedliche Eingabetypen, die jeweils unterschiedliche Bearbeitung brauchen. Eine Routing-Entscheidung am Einstiegspunkt ist die natürliche Passung. Überlegt, was mit den Szenariobeschreibungen des Condition-Agent-Node passiert, wenn alle drei in einen einzigen System-Prompt gequetscht werden.
  Szenario B: Die Revisionsschleife und das menschliche Freigabegate sind die strukturellen Signale. Welcher Agentflow-V2-Node übernimmt die Freigabe (Human-Input-Node), und welcher übernimmt das Zurücksenden der Ausgabe zur Überarbeitung (Loop-Node)? Überlegt, wo die Evaluator-Rolle sitzt: beim Menschen, beim Modell oder bei beiden?
  Szenario C: Zwanzig Sendungen, einzeln verarbeitet mit strukturierten Eingabedaten. Dieses Muster kennt ihr schon. Überlegt, welcher Agentflow-V2-Node speziell dafür gebaut wurde, über eine Liste zu iterieren. Die Orchestrierungsfrage hier: Was passiert, wenn ein Element in der Liste einen Fehler von der Tracking-API zurückgibt?
  Szenario D: Drei sequenzielle Phasen, jede abhängig von der vorherigen, mit bedingten Ausstiegen in Phase eins und zwei. Denkt genau über den Unterschied zwischen einem Workflow-+-Agent-Muster und einem Supervisor-Worker-Muster nach. Die Phasen hier haben eine definierte Reihenfolge und feste Ausstiegsbedingungen. Braucht das einen Agenten, der entscheidet, was als Nächstes zu tun ist, oder soll die Canvas die Sequenz steuern?

>  
  ### 🔥 AI nutzen, wenn ihr feststeckt
  Wenn ihr unsicher seid, welches Muster zu einem Szenario passt, beschreibt die Problemstruktur einem AI-Assistenten und lasst ihn bestimmen, welches der sechs Muster passt. Fordert die Antwort danach heraus, indem ihr fragt, welcher Fehlermodus entstehen würde, wenn dieses Muster falsch wäre.
  Ein guter Prompt:
  > „Ich entwerfe einen Agenten für [beschreibt das Szenario in zwei Sätzen]. Der Agent muss [beschreibt das Kernverhalten]. Ausgehend von diesen sechs Mustern (Single-Agent, Tool-Using-Agent, Workflow + Agent, Router, Evaluator, Supervisor-Worker): Welches passt am besten, und was ist das Hauptrisiko, wenn ich das falsche wähle? Ich verwende Flowise Agentflow V2."
  Nutzt die Antwort der AI als Ausgangspunkt, nicht als endgültige Antwort. Prüft sie anschließend anhand der drei Fragen aus dieser Lektion.
## Checkpoints
Habt ihr alle vier Szenarien abgeschlossen, prüft eure Antworten anhand dieser Fragen:
- Habt ihr für jedes Szenario, in dem ihr Multi-Agent gewählt habt, einen konkreten Koordinationsmechanismus benannt: welcher Node zwischen Agenten routet und welche Daten durch Flow State übertragen werden?
- Habt ihr für jedes Szenario, in dem ihr Single-Agent gewählt habt, eine konkrete Einschränkung identifiziert, die die Entscheidung zu Multi-Agent ändern würde, wenn sie einträte?
- Habt ihr für Szenario B zwischen dem menschlichen Evaluator (Human-Input-Node) und dem modellbasierten Evaluator (Condition-Agent- oder LLM-Node) unterschieden und entschieden, welche Rolle hier gilt?
- Habt ihr für Szenario C den Fehlermodus identifiziert, wenn ein Listenelement einen API-Fehler zurückgibt, und benannt, ob das Muster ihn behandelt oder einen expliziten Fallback braucht?
- Habt ihr für Szenario D begründet, warum die Canvas die Sequenz steuert statt eines Supervisor-Agenten, und identifiziert, was sich am Szenario ändern müsste, damit Supervisor-Worker die bessere Wahl wird?
Macht ein Checkpoint eine Lücke sichtbar, überarbeitet dieses Szenario vor der nächsten Lektion. Das Architekturentscheidungs-Briefing, das ihr später in diesem Sprint erstellt, verlangt dasselbe Reasoning, angewendet auf euren eigenen Agenten.
## In eurem Projekt
Das Entscheidungsframework, das ihr hier geübt habt, ist dasselbe, das ihr in der nächsten Live-Session auf euren eigenen Agenten anwendet. Überlegt vor dieser Session, welche der drei Fragen (Scope und Zuverlässigkeit, Tool-Konflikte, Fehlerisolierung oder Koordinationsaufwand) für euren eigenen Use Case am schwierigsten zu beantworten ist. Genau darauf solltet ihr euch vorbereiten.
## Zusammenfassung
Vier Szenarien, vier Entscheidungen, vier Begründungssätze. Das Framework bleibt jedes Mal dasselbe: zuerst Single vs. Multi-Agent, dann welches Muster, dann welcher Pfeiler die bewussteste Aufmerksamkeit braucht. Die Szenarien in dieser Lektion decken unterschiedliche Teile des Frameworks ab: einen Router, einen Evaluator mit menschlichem Gate, ein Iterationsmuster und einen sequenziellen Workflow. Zusammen decken sie den Großteil dessen ab, was euch im echten Agentendesign begegnen wird.
Die nächste Lektion untersucht die Fehler, die Architekten machen, wenn sie dieses Framework unter Druck anwenden (Over-Engineering, versteckter Zustand und fragile Handoffs), und wie man sie erkennt, bevor sie die Canvas erreichen.