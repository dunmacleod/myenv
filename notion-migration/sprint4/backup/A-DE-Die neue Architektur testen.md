# Die neue Architektur testen

Notion page: https://app.notion.com/p/Die-neue-Architektur-testen-e079418319f382adaf44812c29641c55
Backed up before n8n migration

Die Canvas, die du am Ende der vorherigen Lektion exportiert hast, repräsentiert deine getroffenen Architekturentscheidungen. Implementierung ist nicht dasselbe wie Validierung. Eine Canvas, die auf dem Papier korrekt konfiguriert ist, kann sich unter echten Eingaben trotzdem unerwartet verhalten, und der einzige Weg, das herauszufinden, ist, sie auszuführen.
Diese Lektion dreht sich um strukturiertes Testing und eine geplante Reihe von Szenarien, die jeweils eine spezifische Frage beantworten sollen.
Die Frage ist immer dieselbe:
> Verhält sich die Canvas so, wie die Architektur es spezifiziert, oder nicht? Wenn ja, hast du Evidenz dafür, dass das Design hält. Wenn nicht, hast du einen Fehlerpunkt, den du untersuchen und beheben kannst.
Die Testszenarien in dieser Lektion sind in drei Gruppen organisiert.
- Die erste Gruppe testet, ob die Architektur unter normalen Eingaben korrekt funktioniert.
- Die zweite Gruppe testet gezielt jene Grenzbedingungen, welche die identifizierten Fehlerszenarien aufdecken. Anhand solcher Edge Cases wird deutlich, ob die Schutzmaßnahmen in der Praxis auch wirklich greifen und nicht bloß auf dem Papier konfiguriert sind.
- Die dritte Gruppe testet gezielt deine individuellen Designentscheidungen aus dem Briefing in Sprint 1, dem Diagramm in Sprint 2 sowie der Spezifikation in Sprint 3. Dabei wird geprüft, ob die Architektur tatsächlich exakt nach deinen Vorgaben arbeitet und nicht lediglich das ausführt, was die Standard-Canvas ohnehin schon leistet.
Am Ende dieser Lektion hast du einen dokumentierten Testnachweis: welche Szenarien bestanden wurden, welche Fehler sichtbar gemacht haben, was du geändert hast und was noch adressiert werden muss. Dieser Nachweis ist das Rückgrat deiner Presentation-Day-Verteidigung.
> 💡 In dieser Lektion validierst du, dass deine neu entworfene Architektur die Einschränkungen der Baseline durch gezielte Testszenarien löst, und dokumentierst die Ergebnisse für deine LS-15-Verteidigung.
## Bevor du beginnst
Öffne die post-lesson-26.json-Canvas, die du am Ende der vorherigen Lektion exportiert hast. Bestätige, dass sie korrekt lädt und dass die Node-Struktur dem entspricht, was du in den vier Redesign-Phasen abgeschlossen hast.
Nutze parallel zu Flowise ein Dokument. Du wirst das Ergebnis jedes Tests in diesem Dokument festhalten. Der Testnachweis ist eine Abgabe, keine optionalen Notizen. Während der Präsentation wirst du gefragt, welche Tests du durchgeführt hast, was sie sichtbar gemacht haben und was du bei Fehlern unternommen hast.
## Gruppe 1: Baseline-Funktionstests
Diese drei Tests bestätigen, dass die Canvas normale Eingaben für jeden der zentralen Pfade deiner Architektur korrekt verarbeitet. Sie sollten ohne Fehler bestehen. Wenn einer davon fehlschlägt, ist die Implementierung aus der vorherigen Lektion unvollständig. Stoppe, behebe die Lücke und führe den fehlgeschlagenen Test erneut aus, bevor du zu Gruppe 2 übergehst.
### Test 1.1: Standardanfrage, korrektes Routing
Sende eine Anfrage, die eindeutig zu einem deiner Spezialagenten passt. Für einen Router bedeutet das eine Anfrage, deren query_type eindeutig ist. Für einen Coordinator eine Aufgabe, die der Supervisor an einen spezifischen Worker delegieren sollte. Für einen Evaluator eine Anfrage, die der Generator unkompliziert bearbeiten sollte und die der Evaluator freigeben sollte.
- Was beobachten: Routet die Canvas zum richtigen Agenten? Erzeugt dieser Agent eine Antwort, die zu seinem System-Prompt-Scope passt? Wird die Session ohne Fehler abgeschlossen (ein Logeintrag an Position 4 geschrieben)?
- Protokolliert werden müssen: die ursprüngliche Eingabe, der bearbeitende Agent, die Einhaltung des Scopes sowie der saubere Abschluss der Session.
### Test 1.2: Zweite Anfrage in derselben Session, anderer Routing-Pfad
Sende, ohne die Session zu schließen, eine zweite Anfrage, die zu einem anderen Spezialisten passt als die erste. Damit testest du, ob der Routing-Schlüssel zwischen Anfragen innerhalb einer Session korrekt zurückgesetzt wird.
- Was beobachten: Klassifiziert die Canvas die zweite Anfrage korrekt, unabhängig von der ersten? Routet der Condition Node zu einem anderen Spezialisten als in Test 1.1? Wird die zweite Session sauber abgeschlossen?
- Festhalten: Beide Anfragen, beide Routing-Ergebnisse und ob das Routing der zweiten Anfrage durch den Inhalt der zweiten Anfrage bestimmt wurde oder durch einen Restwert aus der ersten.
### Test 1.3: Anfrage am Rand des Scopes eines Spezialisten
Sende eine Anfrage, die nah an der Grenze zwischen zwei Spezialistenverantwortlichkeiten liegt. Mache sie so mehrdeutig, dass der Classifier sie auf beide Arten klassifizieren könnte. Für einen Router mit einem Account-Spezialisten und einem Support-Spezialisten könnte das sein: „The client mentioned their account is performing well but also raised a support question in passing." Für einen Coordinator eine Aufgabe, die teilweise die definierten Verantwortlichkeiten zweier Worker überlappt. Für einen Evaluator eine Anfrage, die grenzwertig akzeptabel ist: eine, die der Evaluator entweder freigeben oder ablehnen könnte.

- Was beobachten: Welchen Pfad nimmt die Canvas? Ist die Routing- oder Delegationsentscheidung konsistent mit dem, was dein Sprint-2-Design für Grenzfälle spezifiziert hat? Wenn sich die Canvas unerwartet verhält, liegt es daran, dass die System-Prompt-Grenze unklar ist, oder daran, dass der Classifier nicht präzise genug unterscheidet?
- Festhalten: Die Anfrage, das Routing-Ergebnis, ob das Ergebnis deiner Sprint-2-Spezifikation entspricht, und, falls nicht, ob die Lücke im System-Prompt oder in der Klassifizierungslogik liegt.
## Gruppe 2: Grenzbedingungstests
Diese Tests decken gezielt die Edge Cases auf, um die Wirksamkeit deiner Schutzmaßnahmen zu überprüfen. Sie erzeugen genau jene kritischen Systemzustände, die in der Lektion über Memory- und State-Fehlerquellen identifiziert wurden. So lässt sich verifizieren, ob deine Implementierung diese Fehler tatsächlich verhindert oder effektiv eindämmt. Führe jeden Test durch und protokolliere das Ergebnis absolut objektiv. Falls eine Schutzmaßnahme einer solchen Grenzbedingung nicht standhält, ist das kein Scheitern der Lektion, sondern eine wertvolle Erkenntnis für deine Architektur.
### Test 2.1: Schnelle aufeinanderfolgende Anfragen, gleiche Session
Sende drei Anfragen schnell hintereinander innerhalb derselben Session, ohne zu warten, bis die vorherige Antwort vollständig abgeschlossen ist. Damit testest du, ob gleichzeitige oder nahezu gleichzeitige Schreibvorgänge in Flow State zu Contamination zwischen Anfragen führen.
- Was beobachten: Erhält jede Anfrage eine Antwort basierend auf ihrem eigenen Inhalt, oder enthält irgendeine Antwort Inhalte, die zu einer anderen Anfrage in der Sequenz gehören? Enthält der Routing-Schlüssel den korrekten Wert für den Pfad jeder Anfrage, oder überschreibt ein schneller zweiter Schreibvorgang einen ersten Schreibvorgang, der noch nicht gelesen wurde?
- Festhalten: Alle drei Eingaben, alle drei Ausgaben und ob irgendeine Ausgabe Inhalte zu enthalten schien, die zu einer anderen Anfrage in der Sequenz gehörten.
### Test 2.2: Simulation eines absichtlichen Spezialistenfehlers
Dieser Test erfordert, dass du einen Spezialagenten temporär so beschädigst, dass er nicht abschließen kann. Die einfachste Methode ist, einen ungültigen Modellnamen einzutragen oder ein erforderliches Konfigurationsfeld auf einem Spezialisten-Node zu entfernen, eine Anfrage auszuführen, die zu diesem Spezialisten routen würde, und die Konfiguration nach Beobachtung des Ergebnisses wiederherzustellen.
- Was beobachten: Wenn der Spezialist mitten in der Ausführung scheitert, aktiviert sich der Recovery-Pfad? Wird der Routing-Schlüssel zurückgesetzt, bevor der Recovery-Pfad die Kontrolle zurückgibt? Erhält der Nutzer eine Recovery-Nachricht, oder hängt die Session? Falls eine Recovery-Nachricht erscheint, passt ihr Text zum tatsächlichen Fehler, oder beschreibt sie den falschen Agenten oder Pfad?
- Festhalten: der gezielt zum Absturz gebrachte Spezialist, das genaue Verhalten der Canvas beim Auftreten des Fehlers, die erfolgreiche Aktivierung des Recovery-Pfads inklusive des zurückgesetzten Routing-Schlüssels sowie die anschließende Wiederherstellung der Session in einen nutzbaren Zustand.
Stelle nach dem Test die korrekte Konfiguration des Spezialisten wieder her und bestätige, dass Test 1.1 weiterhin besteht.
### Test 2.3: Eingabe, die die Persistent-Store-Grenze testet
Wenn deine Canvas in einen persistenten Store schreibt, sende eine Anfrage, die normalerweise einen Schreibvorgang in den persistenten Store auslösen würde, formuliere die Anfrage aber so, als enthielte sie session-spezifische oder identifizierende Inhalte: „My name is [test name] and I need to escalate this." Beobachte, was, falls überhaupt etwas, in den persistenten Store geschrieben wird.
- Was beobachten: Filtert die Schreibkonfiguration session-spezifische oder nutzeridentifizierende Inhalte heraus, oder wird die rohe Eingabe unverändert geschrieben? Wenn du den persistenten Store öffnest und den letzten Schreibvorgang inspizierst, was enthält er?
  - Wenn deine Canvas nicht in einen persistenten Store schreibt, ersetze diesen Test durch eine Prüfung des last_account_summaryPatterns aus der vorherigen Lektion: Bestätige, dass jeder von einem Spezialisten geschriebene Zwischenergebnis-Schlüssel am Anfang einer neuen Anfrage zurückgesetzt wird und nicht aus einer vorherigen Anfrage weitergetragen wird.
- Festhalten: Was in den persistenten Store geschrieben wurde (oder was der Zwischenschlüssel nach einer zweiten Anfrage enthielt) und ob der geschriebene Inhalt der Regel entspricht, die du in Sprint 3 spezifiziert hast.
## Gruppe 3: Architekturspezifische Validierungstests
Diese Tests beziehen sich spezifisch auf deine Designentscheidungen. Auf die Entscheidungen, die deine Implementierung von der Baseline-Canvas unterscheiden. Jeder Test in dieser Gruppe ist einer Zusage zugeordnet, die du in einer deiner drei Sprint-Abgaben gemacht hast. Der Test prüft, ob die Implementierung diese Zusage tatsächlich einhält.
### Test 3.1: Archetyp-Strukturtest
Dieser Test ist für jeden Archetyp anders.
Wenn du den Router gewählt hast:
Sende nacheinander je eine Anfrage, die der Classifier zu jedem deiner drei Spezialistenpfade routen sollte.
Bestätige, dass alle drei Pfade erreichbar sind und dass der System-Prompt-Scope jedes Spezialisten klar unterscheidbar ist. Eine Anfrage, die für Specialist A gedacht ist, sollte keine Ausgabe erzeugen, die auf die Domäne von Specialist B zurückgreift.
Wenn du den Coordinator gewählt hast:
Sende eine Aufgabe, die verlangt, dass beide Worker zur finalen Antwort beitragen.
Vergewissere dich, dass der Supervisor gemäß der Sequenz deines Sprint-2-Designs an beide Worker delegiert. Der Loop Node muss unvollständige Arbeit verlässlich an den Supervisor zurückspielen, anstatt sie direkt an den Reply-Node weiterzugeben. Stelle zudem sicher, dass die finale Antwort die Outputs beider Worker sauber synthetisiert.
Wenn du den Evaluator gewählt hast:
Sende eine Anfrage, die der Generator bearbeitet und die der Evaluator ablehnen sollte; eine Anfrage, die nah an akzeptabel ist, aber nicht ganz.
Bestätige, dass der Evaluator-Node eine Ablehnung zurückgibt, dass der Loop Node die abgelehnte Ausgabe mit sichtbarem Feedback des Evaluator zurück zum Generator routet und dass der zweite Versuch des Generators das Feedback einarbeitet.
Bestätige, dass das Human-Input-Gate die überarbeitete Ausgabe erhält und korrekt zur Freigabe auffordert.
- Festhalten: Die verwendeten Eingaben, die Sequenz der Agentenaktivierungen, die im Flowise-Ausführungstrace beobachtet wurde, und ob die Sequenz dem Sprint-2-Multi-Agent-Designdiagramm entspricht.
### Test 3.2: Compliance mit der Memory-Spezifikation
Kehre zu deiner Sprint-3-Memory- und State-Architekturspezifikation zurück. Finde die drei Elemente, die du in der Shared/Private-Boundary als höchste Priorität ausgewiesen hast: den Schlüssel, der zwischen Agenten geteilt werden muss, den Schlüssel, der privat für einen Agenten bleiben muss, und das Element, das niemals persistieren darf. Entwirf eine Anfrage, die jedes dieser drei Elemente auslöst. Führe die Anfrage aus. Inspiziere Flow State, nachdem die Session abgeschlossen ist.
- Was beobachten: Ist der geteilte Schlüssel für alle Agenten lesbar, die darauf zugreifen sollten? Fehlt der private Schlüssel in Flow State und ist er nur im Kontextfenster des owning Agent sichtbar? Fehlt das Element, das niemals persistieren darf, in jedem Flow-State-Schlüssel und im persistenten Store?
- Festhalten: Welche drei Elemente du getestet hast, was du für jedes in Flow State und im persistenten Store beobachtet hast und ob die Beobachtung der Spezifikation entspricht.
### Test 3.3: Begründungstest
Dein Sprint-1-Briefing hat die gewählte Architektur gegenüber der verworfenen Alternative begründet. Die Begründung nannte mindestens einen konkreten Vorteil, den dein gewähltes Design gegenüber der nicht gewählten Alternative hat.
Entwirf eine Anfrage, die diesen Vorteil direkt auf die Probe stellt. Falls deine Prämisse war, dass der Router für deinen Use Case schneller als der Coordinator arbeitet, weil das Routing stateless erfolgt und die Delegation keine Schleife erfordert, sende eine Anfrage und miss die exakte Antwortzeit. Wenn du hingegen dargelegt hast, dass der Evaluator qualitativ hochwertigere Ergebnisse liefert als eine Single-Agent-Lösung, sende eine Anfrage und vergleiche die finale Output-Qualität direkt mit den Resultaten einer klassischen Single-Agent-Canvas.
- Was beobachten: Erzeugt die Canvas Verhalten, das die Begründung unterstützt, die du in Sprint 1 geschrieben hast? Das ist kein Pass/Fail-Test, sondern Evidenzsammlung für deine Verteidigung. Eine Begründung, die unter einem Live-Test hält, ist eine stärkere Verteidigung als eine, die nur im Designdokument steht.
- Festhalten: Die verwendete Anfrage, was die Canvas erzeugt hat und ob das Ergebnis die Begründung aus Sprint 1 unterstützt oder kompliziert.
## Checkpoints
Gehe nach Abschluss aller neun Tests diese Fragen durch, bevor du die Lektion schließt:
- [ ] Wie viele Tests wurden ohne Fehler bestanden? Liste sie auf.
- [ ] Wie viele Tests haben einen Fehler oder unerwartetes Verhalten sichtbar gemacht? Hast du für jeden die Ursache identifiziert? Hast du einen Fix implementiert? Ändert der Fix irgendetwas an den Phasen 1–4 aus der vorherigen Lektion?
- [ ] Gibt es einen Test, den du nicht ausführen konntest, weil die Canvas-Konfiguration ein Tool oder einen Service erforderte, auf den du keinen Zugriff hast? Notiere es — und notiere, wie du den Test ausführen würdest, wenn die Ressource verfügbar wäre.
- [ ] Geben dir die Ergebnisse der Gruppe-3-Tests Evidenz, die du für deine Präsentation nutzen kannst? Wenn ein Test Output erzeugt hat, der eine Designentscheidung direkt unterstützt, notiere, was du am Presentation Day demonstrieren solltest.
Exportiere die finale Canvas als [your-canvas-name]__post-lesson-27.json. Das ist die Version, die du zur Live Session vor Presentation Day mitbringst.
## Verständnischeck
### Frage 1
>  Während Test 2.1 führt ein Lernender drei schnelle Anfragen in derselben Session aus und stellt fest, dass die dritte Antwort das Routing-Ergebnis der zweiten Anfrage enthält, statt der dritten. Die Canvas des Lernenden verwendet einen einzelnen globalen query_type-Schlüssel, nicht nach Session namespaced. Was ist die wahrscheinlichste Ursache der Contamination?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/95bd7017-0be5-46c8-92ca-874dd2bd545a
## Zusammenfassung
Strukturiertes Testen bildet die finale Prüfung, um aus einer rein entworfenen Architektur eine fachlich fundierte und belastbare Architektur zu machen. Die neun Szenarien dieser Lektion decken dabei drei wesentliche Ebenen ab: die Basis-Funktionalität unter Normalbedingungen, die Grenzbedingungen zur Überprüfung deiner Schutzmaßnahmen im Ernstfall sowie die architekturspezifische Validierung, ob die Implementierung die Designversprechen aus den Sprints 1 bis 3 einhält.
Die in dieser Lektion erbrachten Testnachweise dienen als solides Fundament für deine spätere Präsentation. Der Präsentationstag ist die Gelegenheit, deine Architekturentscheidungen und deren Entstehungsprozess fachlich zu vertreten – und die heute durchgeführten Tests liefern dir dafür die konkreten Argumente.
In der nächsten Lektion präsentierst du schließlich deinen neu entworfenen Agenten, gehst das Systemdiagramm im Detail durch und begründest deine Architektur-, Memory- und State-Entscheidungen vor deinen Peers und dem Instructor.
## 