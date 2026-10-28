# Den Baseline-Projektagenten neu entwerfen

Notion page: https://app.notion.com/p/Den-Baseline-Projektagenten-neu-entwerfen-8da9418319f383489d648148f175be7d
Backed up before n8n migration

Die Vela-Systems-Canvas diente über das gesamte Modul hinweg als unser zentrales Lehrbeispiel. Jedes Konzept, jede Designentscheidung und jedes Fehlerszenario haben wir zunächst an dieser gemeinsamen Canvas erprobt. So wurden die Architekturprinzipien greifbar, noch bevor du sie auf dein eigenes System übertragen musstest. In dieser Lektion entfällt nun dieses schützende Gerüst.
Ab jetzt arbeitest du mit deiner eigenen Projekt-Canvas. Diese basiert auf dem von dir gewählten Archetyp (Router, Coordinator oder Evaluator) sowie deiner individuellen Domäne. Das Fundament bilden dabei deine bisherigen Ergebnisse: das Architekturbriefing aus Sprint 1, das Multi-Agent-Design aus Sprint 2 und die Memory- und State-Spezifikation aus Sprint 3. Diese drei Dokumente definieren das Design, das du nun implementierst. Deine Aufgabe in dieser Lektion ist es, diese Vorgaben systematisch in die Praxis umzusetzen. Du gleichst den aktuellen Zustand deiner Canvas mit dem Design ab, deckst Lücken auf, schließt diese und stellst abschließend sicher, dass die Fehlerszenarien aus der vorherigen Lektion in deiner Implementierung nicht auftreten können.
Am Ende dieser Lektion sollte deine Canvas exakt die Architektur widerspiegeln, die du in den Sprints 1 bis 3 entworfen hast. Für deine Präsentation geht es dann nur noch darum, das System zu demonstrieren und deine Architekturentscheidungen fachlich zu vertreten – die eigentliche Designarbeit ist damit abgeschlossen.
> 💡 In dieser Lektion wendest du die Architektur- sowie Memory- und State-Muster aus den Sprints 1–3 an, um deinen Projektagenten neu zu entwerfen, indem du die Lücke zwischen dem von dir spezifizierten Design und der aktuell existierenden Canvas schließt.

## Bevor du Flowise öffnest
Exportiere deine aktuelle Canvas als JSON-Backup, bevor du etwas änderst. In self-hosted Flowise geschieht das über das Canvas-Menü: Export → speichere die Datei als [your-canvas-name]__pre-lesson-26-backup.json. Wenn beim Redesign etwas schiefgeht, kannst du diese Datei wieder importieren und zum aktuellen Zustand zurückkehren.
## Was du implementierst
Die drei Sprint-Abgaben sind deine Implementierungsspezifikation. Öffne sie, bevor du die Canvas auditierst.
- Sprint 1: Architekturentscheidungsbriefing. Single-Agent- oder Multi-Agent-Entscheidung mit Begründung. Das Briefing benennt deinen gewählten Archetyp und die Domäne.
- Sprint 2: Multi-Agent-Designdiagramm. Agentenrollen, Verantwortlichkeiten, Koordinationsansatz und die verworfene Alternative.
- Sprint 3: Memory- und State-Architekturspezifikation. Was geteilt ist, was privat ist, was niemals persistieren darf und wie State nach einem Fehler recovered.
Sollte eines dieser Dokumente unvollständig sein, gilt es, genau das als Erstes zu beheben. Eine Implementierung lässt sich schließlich nicht anhand einer lückenhaften Spezifikation überprüfen. Vervollständige daher alle fehlenden Abschnitte, bevor du fortfährst.
## Das Redesign in vier Phasen
Arbeite die vier Phasen der Reihe nach durch. Jede Phase hat eine Auditfrage, eine Reihe von Aktionen, falls das Audit eine Lücke findet, und einen Checkpoint, um zu bestätigen, dass die Phase abgeschlossen ist, bevor du weitermachst.
### Phase 1: Architektur
Auditfrage: Spiegelt die aktuelle Canvas den Archetyp wider, den du in deinem Sprint-1-Briefing gewählt hast?
Öffne deine Canvas. Sieh dir die Node-Struktur an und vergleiche sie mit dem Briefing.
Für den Router:
- Die Canvas sollte einen Classifier-Node haben (oder einen LLM-Node / Condition-Agent-Node, der als Classifier fungiert), einen Condition-Node, der query_type aus Flow State liest, und mindestens zwei Spezialisten-Agent-Nodes mit klar unterschiedlichen System-Prompts und nicht überlappenden Verantwortlichkeiten. Ein Direct-Reply-Node schließt jeden Routing-Pfad ab.
Für den Coordinator:
- Die Canvas sollte einen Supervisor-LLM-Node haben, der Aufgaben explizit delegiert, mindestens zwei Spezialisten-Agent-Nodes, die als Worker arbeiten, und eine Loop-Struktur (Loop Node und Condition Node), die unvollständige Arbeit zum Supervisor zurückführt, statt sie direkt an Reply weiterzugeben.
Für den Evaluator:
- Die Canvas sollte einen Generator-Agent-Node, einen separaten Evaluator-Agent-Node mit einem eigenen Evaluationsprompt, einen Human-Input-Node, der die Freigabe steuert, und einen Loop Node haben, der abgelehnte Ausgabe zum Generator zurückführt.
Wenn die Canvas nicht zum Archetyp passt: Füge die fehlenden Nodes hinzu, konfiguriere ihre System-Prompts und verdrahte die Verbindungen, bevor du zu Phase 2 übergehst. Überspringe das nicht, auch wenn die Lücke klein wirkt.
Checkpoint Phase 1:
- [ ] Entspricht die Node-Struktur auf der Canvas dem Archetyp, der in deinem Sprint-1-Briefing genannt wird?
- [ ] Hat jeder Agent-Node einen System-Prompt, der seine Verantwortlichkeiten klar und ohne Überschneidung mit den anderen Agenten definiert?
- [ ] Sind alle Verbindungen zwischen Nodes vollständig, ohne lose Outputs und ohne nicht verdrahtete Inputs?
### Phase 2: Memory-Grenzen
Auditfrage: Erzwingt die Canvas die Memory-Grenzen, die in deinem Sprint-3-Dokument spezifiziert sind?
Öffne deine Sprint-3-Memory- und State-Architekturspezifikation. Finde den Abschnitt, der definiert, was geteilt und was privat ist.
Gehe jedes Element dieses Abschnitts durch und mache es auf der Canvas ausfindig. Ermittle für jeden geteilten Schlüssel, welcher Node ihn schreibt und welche Nodes ihn auslesen. Vergewissere dich, dass dies exakt der von dir spezifizierten Write Ownership entspricht. Stelle zudem für jedes private Element sicher, dass es ausschließlich im Kontextfenster des jeweiligen Agenten verbleibt. Es darf nicht in den Flow State geschrieben werden, wo andere Agenten darauf zugreifen könnten.
Wenn ein Schlüssel, der privat sein sollte, in Flow State geschrieben wird: Entferne ihn aus der Update-Flow-State-Konfiguration dieses Nodes. Wenn ein Schlüssel, der geteilt sein sollte, gar nicht in Flow State geschrieben wird: Füge ihn der Update-Flow-State-Konfiguration des owning Agent hinzu.
Führe nach dem Anpassen der Grenzen drei Checks aus:
- Öffne die Update Flow StateKonfiguration auf jedem Agent-Node. Liste jeden Schlüssel auf, den er schreibt. Vergleiche diese Liste mit deiner Sprint-3-Spezifikation. Jeder Schlüssel, der nicht in der Spezifikation steht, ist entweder eine Lücke in der Spezifikation (aktualisiere sie) oder ein undokumentierter Schreibvorgang, der nicht dort sein sollte (entferne ihn).
- Bestätige, dass kein Agent einen Flow-State-Schlüssel liest, den er nicht besitzt, außer Schlüssel, die explizit als geteilt ausgewiesen sind.
- Bestätige, dass query_type oder der entsprechende Schlüssel, den dein Classifier oder Coordinator schreibt, um Routing-Entscheidungen zu signalisieren, auf null zurückgesetzt wird, bevor ein neuer Anfragewert geschrieben wird. Wenn er nicht zurückgesetzt wird, hinterlässt ein fehlgeschlagener Schreibvorgang im Classifier einen veralteten Wert, den der Condition Node als gültig liest.
Checkpoint Phase 2:
- [ ] Erscheint jeder Flow-State-Schlüssel auf der Canvas in deiner Sprint-3-Spezifikation? Gibt es undokumentierte Schlüssel?
- [ ] Wird Write Ownership erzwungen, also gibt es genau einen benannten Node pro Schlüssel?
- [ ] Wird query_type (oder dein entsprechender Routing-Schlüssel) vor jedem neuen Schreibvorgang zurückgesetzt?
### Phase 3: State-Handoff und Recovery
Auditfrage: Implementiert die Canvas das State-Handoff- und Recovery-Design aus deiner Sprint-3-Spezifikation?
Öffne deine Sprint-3-Spezifikation. Finde den Abschnitt zu State Handoff und den Abschnitt zu Recovery.
State Handoff: Stelle bei jedem Handoff zwischen den Agenten sicher, dass die Canvas den erforderlichen Kontext über den Flow State weitergibt. Der empfangende Agent muss reibungslos mit genau den Werten arbeiten können, die ihm zu Beginn seiner Ausführung zur Verfügung stehen – ohne Informationen neu abfragen zu müssen, die der vorherige Agent bereits ermittelt hat. Sollten diese Übergaberegeln unvollständig sein, ergänze den fehlenden Schlüssel in der Update Flow State-Konfiguration des sendenden Agenten.
Recovery: Deine Spezifikation aus Sprint 3 hat einen sicheren State definiert. Das sind exakt die Flow State-Werte, auf die die Canvas nach dem Fehlschlag eines Spezialagenten zurückfällt. Stelle sicher, dass dies in der Canvas auch tatsächlich so implementiert ist. In Agentflow V2 wird die Recovery nach einem Fehler über die Error-Handling-Konfiguration des Flows sowie den Fallback-Pfad des Condition-Nodes gesteuert. Ein Beispiel: Wenn ein Fehler beim Specialist A dazu führt, dass query_type: "support" ohne entsprechendes Completion-Signal im Flow State verbleibt, muss ein Recovery-Pfad dieses fehlende Signal erkennen. Daraufhin sollte er den query_type auf null zurücksetzen und die Anfrage wieder an den Classifier übergeben.
Wenn auf der Canvas kein Recovery-Pfad existiert, entwirf und implementiere jetzt einen. Der minimale Recovery-Pfad ist ein Condition-Node-Fallback, der feuert, wenn ein Completion-Signal-Schlüssel fehlt, den Routing-Schlüssel zurücksetzt und die Kontrolle an den Classifier oder Coordinator zurückgibt.
Checkpoint Phase 3:
- [ ] Übergibt jeder Agent-zu-Agent-Handoff die erforderlichen Flow-State-Schlüssel wie in Sprint 3 spezifiziert?
- [ ] Hat die Canvas einen expliziten Recovery-Pfad für mindestens einen Fehler eines Spezialagenten?
- [ ] Setzt der Recovery-Pfad den Routing-Schlüssel zurück, bevor er die Kontrolle zurückgibt, nicht danach?
### Phase 4: Schutzmaßnahmen gegen Fehlermodi
Auditfrage: Implementiert die Canvas Schutzmaßnahmen gegen die Fehlermodi, die in der vorherigen Lektion identifiziert wurden?
Überprüfe die fünf Schutzmaßnahmen-Entscheidungen, die du in der vorherigen Lektion erstellt hast. Bestätige für jede, ob sie auf deine Canvas zutrifft. Nicht jeder Vela-Fehlermodus wird auf jeden Archetyp zutreffen, aber die meisten werden ein strukturelles Äquivalent haben.
Arbeite jede anwendbare Schutzmaßnahme durch und bestätige, dass sie implementiert ist:
- Reset-Timing für Routing-Schlüssel. Wird query_type (oder dein entsprechender Schlüssel) vor jedem neuen Schreibvorgang zurückgesetzt? (Phase 2 hat das adressiert; bestätige, dass es nach allen weiteren Bearbeitungen weiterhin gilt.)
- Key Contamination zwischen Anfragen. Werden Flow-State-Schlüssel verwendet, um Zwischenergebnisse über Anfragen innerhalb einer Session hinweg zu tragen? Wenn ja, wird jeder davon am Anfang einer neuen Anfrage zurückgesetzt, nicht am Ende der vorherigen?
- Schreibregeln für persistente Stores. Wenn deine Canvas in einen persistenten Store schreibt (Qdrant oder Äquivalent), schließt die Schreibkonfiguration session-spezifische Inhalte aus?
- Session-namespaced Schlüssel. Wenn deine Canvas mit mehreren gleichzeitigen Nutzern laufen soll (relevant, wenn du den Router- oder Coordinator-Archetyp gewählt hast), sind Routing- und Zwischenschlüssel nach Session-ID namespaced, statt als globale Schlüssel geschrieben zu werden?
- Genauigkeit von Diagnosemeldungen. Wenn dein Recovery-Pfad eine nutzerseitige Meldung erzeugt, leitet diese Meldung ihren Inhalt zur Laufzeit aus dem tatsächlichen Flow-State-Wert ab, statt aus hardcodiertem Text, der den falschen Agenten beschreiben könnte?
Wenn eine Schutzmaßnahme zutrifft und nicht implementiert ist: Implementiere sie jetzt. Wenn eine Schutzmaßnahme nicht auf deinen Archetyp zutrifft, notiere in einem Satz, warum. Das wird Teil deiner Verteidigung während der Präsentation sein.
Checkpoint Phase 4:
- [ ] Hast du jede anwendbare Schutzmaßnahme aus der vorherigen Lektion bestätigt oder implementiert?
- [ ] Hast du für Schutzmaßnahmen, die nicht auf deine Canvas zutreffen, den Grund notiert?
- [ ] Entspricht die Canvas nach den Bearbeitungen in Phase 4 weiterhin dem Zustand aus Phase 1 und Phase 2? (Implementierungen von Schutzmaßnahmen führen manchmal neue Verbindungen oder Schlüssel-Schreibvorgänge ein. Prüfe erneut, dass die Grenzen aus Phase 2 weiterhin korrekt sind.)
## Achtung!
- Die Backup-Datei bearbeiten statt die Live-Canvas. Öffne die richtige Datei in Flowise, bevor du Änderungen vornimmst. Wenn du unsicher bist, welche welche ist, sieh dir das Beschreibungsfeld der Canvas an. Die Live-Canvas sollte die Architekturzusammenfassung enthalten, die du in Sprint 1 geschrieben hast.
- Nodes hinzufügen, die nicht in deiner Sprint-3-Spezifikation stehen, ohne die Spezifikation zu aktualisieren. Jeder neue Flow-State-Schlüssel oder Agent-Node, der in Phase 4 hinzugefügt wird, sollte vor deiner Präsentation in der Spezifikation reflektiert werden. Eine Canvas, die von ihrer Spezifikation abgewichen ist, lässt sich nicht kohärent verteidigen.
- Den Reset-Check in Phase 2 überspringen, weil „der Classifier immer vor dem Condition Node läuft". Der Classifier läuft in einer funktionierenden Session immer vor dem Condition Node. In einer fehlgeschlagenen Session möglicherweise nicht. Der Reset schützt den Fehlerfall, nicht den funktionierenden Fall.
- Den Recovery-Pfad bei Architekturen mit nur einem Spezialisten als optional behandeln. Ein Router mit drei Spezialisten hat drei Fehleroberflächen. Ein Evaluator mit einem Generator- und einem Evaluator-Agenten hat zwei. Selbst eine minimale Multi-Agent-Canvas braucht mindestens einen Recovery-Pfad.
- Die Canvas nach Phase 2 und vor Phase 3 schließen, ohne zu exportieren. Exportiere nach jeder Phase. Ein Flowise-Crash mitten in der Session ohne Stage-Checkpoint bedeutet, dass du Arbeit wiederholen musst.
## Checkpoints
Nutze diese Fragen während der vier Phasen, um deinen Zustand zu prüfen, bevor du von einer Phase zur nächsten übergehst:
- [ ] Nach Phase 1: Kannst du die Node-Struktur deiner Canvas aus dem Gedächtnis zeichnen und sie mit deiner Archetyp-Wahl aus Sprint 1 abgleichen? Wenn die Antwort unsicher ist, ist die Architektur nicht vollständig implementiert.
- [ ] Nach Phase 2: Wenn du alle Node-Labels von der Canvas entfernen würdest und nur die Update-Flow-State-Konfigurationen betrachten würdest, könntest du rekonstruieren, welcher Agent welchen Schlüssel besitzt? Write Ownership sollte aus der Konfiguration lesbar sein, nicht durch die Node-Position impliziert werden.
- [ ] Nach Phase 3: Wenn Specialist A (oder der Spezialist, der für dein Design am zentralsten ist) vollständig scheitert, nachdem der Classifier bereits den Routing-Schlüssel geschrieben hat, was würde passieren? Gehe die Sequenz durch. Die Antwort sollte nicht „die Session hängt" oder „der Nutzer erhält einen unbehandelten Fehler" sein.
- [ ] Nach Phase 4: Exportiere die Canvas als [your-canvas-name]__post-lesson-26.json. Das ist dein Implementierungs-Checkpoint. Bewahre sowohl das Pre-Lesson-Backup als auch diesen Export auf. Du brauchst den Post-Lesson-Export als Startzustand für die nächste Lektion.

>  
  ### 🔥 AI nutzen, wenn du feststeckst
  Wenn du an einer Phase bist, in der du weißt, was die Canvas tun sollte, aber nicht herausfindest, welche Flowise-Konfiguration dafür nötig ist, nutze AI als Konfigurationshilfe, nicht als Designersatz:
  1. Beschreibe das konkrete Verhalten, das du brauchst: „When the Update Flow State step on the Classifier node fails to execute, I need the Condition Node to detect this and route to a fallback path rather than routing based on a stale value."
  1. Spezifiziere das Tool: „I am using self-hosted Flowise Agentflow V2."
  1. Frage nach dem Konfigurationsansatz: „What is the correct way to configure this in Agentflow V2, which node handles the detection, and where does the fallback path connect?"
  Bitte AI nicht darum, zu beschreiben, was deine Canvas enthalten sollte. Das ist die Sprint-3-Spezifikation, die du bereits geschrieben hast. Nutze AI, um die Lücke zwischen der Spezifikation und der Flowise-Konfiguration zu schließen, die sie implementiert.

## Zusammenfassung
[synced_block] 
  Die vier Phasen dieser Lektion schließen die Lücke zwischen dem Design, das du über die Sprints 1 bis 3 hinweg spezifiziert hast, und der Canvas, die es implementiert.
  1. Architekturphase: Die Node-Struktur muss zum Archetyp passen.
  1. Memory-Grenzen: Write Ownership und Scope müssen zur Sprint-3-Spezifikation passen.
  1. State Handoff und Recovery: Die Canvas muss Kontext korrekt zwischen Agenten übergeben und Fehler behandeln, ohne hängen zu bleiben.
  1. Schutzmaßnahmen gegen Fehlermodi: Die spezifischen Schutzmaßnahmen, die du in der vorherigen Lektion entworfen hast, müssen in der Implementierung vorhanden sein.
  Die Canvas, die du am Ende dieser Lektion exportierst, ist der Implementierungs-Checkpoint. In der nächsten Lektion validierst du, dass die Implementierung die Einschränkungen der Baseline tatsächlich löst. Dafür lässt du die Canvas gegen gezielte Testszenarien laufen und prüfst, ob sie sich so verhält, wie das Design es vorhergesagt hat. Das reine Lesen der Spezifikation reicht dafür nicht aus.
