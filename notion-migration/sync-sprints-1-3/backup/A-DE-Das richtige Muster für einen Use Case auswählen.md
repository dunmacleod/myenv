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
  Szenario A: Klassifiziert die Eingabe mit wenigen erlaubten Labels und leitet über Switch weiter. Ein Zweig kann eine API-Abfrage, eine belegte Richtlinienantwort oder eine menschliche Eskalation sein. Drei Routen erfordern nicht automatisch drei Agenten. Definiert einen Fallback für unbekannte Labels.
  Szenario B: Der Entwurf braucht menschliche Freigabe, nicht nur eine weitere Modellmeinung. Erwägt eine unterstützte Send-and-Wait-Freigabeoperation oder Wait, fortgesetzt durch ein Review-Ereignis. Haltet die Versuchszahl explizit fest: höchstens drei Entwurfs-/Review-Versuche, danach Eskalation. Das Design muss Ablehnung und ausbleibende Antwort behandeln.
  Szenario C: n8n kann eine Liste als Items verarbeiten. Nutzt Loop Over Items, wenn explizite Batch- oder Einzelsteuerung gebraucht wird; nicht jede Liste benötigt diesen Node. Prüft die 24-Stunden-Grenze deterministisch, behandelt jeden API-Fehler und fasst bestätigte Ergebnisse zusammen. Ein Agent kann den Bericht formulieren, wird aber nicht für jede Abfrage benötigt.
  Szenario D: Reihenfolge und Ausstiegsbedingungen sind festgelegt. Ein Workflow mit If/Switch kann sie erzwingen. Nutzt Modell-Reasoning nur für nötige Interpretation. Supervisor-Worker ist erst begründet, wenn die Wahl des nächsten Schritts selbst Reasoning erfordert.

> 💡 
  ### 🔥 AI nutzen, wenn ihr feststeckt
  Wenn ihr unsicher seid, welches Muster zu einem Szenario passt, beschreibt die Problemstruktur einem AI-Assistenten und lasst ihn bestimmen, welches der sechs Muster passt. Fordert die Antwort danach heraus, indem ihr fragt, welcher Fehlermodus entstehen würde, wenn dieses Muster falsch wäre.
  Ein guter Prompt:
  > „Ich entwerfe einen Agenten für [beschreibt das Szenario in zwei Sätzen]. Der Agent muss [beschreibt das Kernverhalten]. Ausgehend von diesen sechs Mustern (Single-Agent, Tool-Using-Agent, Workflow + Agent, Router, Evaluator, Supervisor-Worker): Welches passt am besten, und was ist das Hauptrisiko, wenn ich das falsche wähle? Ich verwende n8n."
  Nutzt die Antwort der AI als Ausgangspunkt, nicht als endgültige Antwort. Prüft sie anschließend anhand der drei Fragen aus dieser Lektion.
## Checkpoints
Habt ihr alle vier Szenarien abgeschlossen, prüft eure Antworten anhand dieser Fragen:
- Habt ihr für jedes Szenario, in dem ihr Multi-Agent gewählt habt, einen konkreten Koordinationsmechanismus benannt: welcher Node oder welches Tool Arbeit delegiert und welche Aufgaben- und Ergebnisfelder die Übergabe enthält?
- Habt ihr für jedes Szenario, in dem ihr Single-Agent gewählt habt, eine konkrete Einschränkung identifiziert, die die Entscheidung zu Multi-Agent ändern würde, wenn sie einträte?
- Habt ihr für Szenario B zwischen dem menschlichen Freigabegate und einem modellbasierten Evaluator unterschieden und entschieden, welche Rolle hier gilt?
- Habt ihr für Szenario C den Fehlermodus identifiziert, wenn ein Listenelement einen API-Fehler zurückgibt, und benannt, ob das Muster ihn behandelt oder einen expliziten Fallback braucht?
- Habt ihr für Szenario D begründet, warum die Canvas die Sequenz steuert statt eines Supervisor-Agenten, und identifiziert, was sich am Szenario ändern müsste, damit Supervisor-Worker die bessere Wahl wird?
Macht ein Checkpoint eine Lücke sichtbar, überarbeitet dieses Szenario vor der nächsten Lektion. Das Architekturentscheidungs-Briefing, das ihr später in diesem Sprint erstellt, verlangt dasselbe Reasoning, angewendet auf euren eigenen Agenten.
## In eurem Projekt
Das Entscheidungsframework, das ihr hier geübt habt, ist dasselbe, das ihr in der nächsten Live-Session auf euren eigenen Agenten anwendet. Überlegt vor dieser Session, welche der vier Fragen (Scope und Zuverlässigkeit, Tool-Konflikte, Fehlerisolierung oder Koordinationsaufwand) für euren eigenen Use Case am schwierigsten zu beantworten ist. Genau darauf solltet ihr euch vorbereiten.
## Zusammenfassung
Vier Szenarien, vier Entscheidungen, vier Begründungssätze. Das Framework bleibt jedes Mal dasselbe: zuerst Single vs. Multi-Agent, dann welches Muster, dann welcher Pfeiler die bewussteste Aufmerksamkeit braucht. Die Szenarien in dieser Lektion decken unterschiedliche Teile des Frameworks ab: einen Router, einen Evaluator mit menschlichem Gate, ein Iterationsmuster und einen sequenziellen Workflow. Zusammen decken sie den Großteil dessen ab, was euch im echten Agentendesign begegnen wird.
Die nächste Lektion untersucht die Fehler, die Architekten machen, wenn sie dieses Framework unter Druck anwenden (Over-Engineering, versteckter Zustand und fragile Handoffs), und wie man sie erkennt, bevor sie die Canvas erreichen.
## 📸 Screenshot-Vorschläge
- Norda: Classifier-Ausgabe und Switch mit Fallback zeigen.
- Helio: Entwurf, menschliche Freigabe und begrenzte Überarbeitungsschleife als n8n-Designskizze zeigen; attempt_count hervorheben.
- Daven: Beispiel-Items mit Sendungsstatus und markiertem API-Fehler zeigen. Arco: If-Zweige mit festen Ausstiegen zeigen.
## Wissenscheck
### 1. Was benötigt Helios Freigabeanforderung?
- A. Nur einen zweiten Modellaufruf — Falsch. Das Szenario verlangt menschliche Freigabe.
- B. Ein menschliches Gate mit begrenzten Versuchen und Eskalation — Richtig. Freigabe, Ablehnung und Grenze gehören zum Design.
- C. Einen größeren Memory-Speicher — Falsch. Memory ersetzt keine Freigabe.
### 2. Benötigen zwanzig Sendungsabfragen zwanzig Agenten?
- A. Nein, deterministische Item-Verarbeitung kann ausreichen — Richtig. Mehrere Datensätze sind keine unterschiedlichen Reasoning-Rollen.
- B. Ja, jeder Datensatz braucht einen Spezialisten — Falsch. API-Abfragen erfordern nicht automatisch Agenten.
- C. Ja, weil HTTP Request eine Modellentscheidung ist — Falsch. Ein Hauptpfad-Request kann deterministisch laufen.
### 3. Was passt zu Arcos festen Stufen und Ausstiegen?
- A. Ein durch If/Switch kontrollierter Workflow — Richtig. Die Sequenz ist bereits vorgegeben.
- B. Ein Supervisor, der die Reihenfolge frei ändert — Falsch. Das würde den Anforderungen widersprechen.
- C. Alle Prüfungen auslassen und eine Antwort generieren — Falsch. Die vorgeschriebenen Prüfungen müssen stattfinden.