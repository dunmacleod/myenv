# Häufige Multi-Agent-Muster

Notion page: https://app.notion.com/p/H-ufige-Multi-Agent-Muster-3779418319f3809e827fd64f5126a1fb
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Die Ergebnisse deiner acht Validierungstests aus der vorherigen Lektion nutzen, um Schwachstellen in deinem System-Prompt zu diagnostizieren, die Anweisungen umschreiben, die unerwartetes Verhalten verursacht haben, erneut testen, bis alle acht Tests bestanden werden, und einen finalisierten System-Prompt erstellen, der bereit für die Bewertung von Sprint 3 ist.

## Die Ausgangslage
Contigo GmbHs Support-Agent läuft auf dem Tool-Agent-Node mit angeschlossenem Speicher, Abfrage und Tools. Die acht Validierungstests haben dir den ersten echten Beleg dafür geliefert, wie sich dein System-Prompt unter realistischen Anfragebedingungen verhält.
Manche Tests werden sauber bestanden worden sein. Andere haben möglicherweise Lücken aufgedeckt, etwa eine Anfrage, die das falsche Tool ausgelöst hat, eine Ausweichformulierung, die nicht ausgelöst wurde, obwohl sie es hätte tun sollen, oder eine Anweisung zur Grenze bei Kontoaktionen, die zu vage war, um zu verhindern, dass der Agent suggeriert, er könne eine Schreiboperation ausführen.
In dieser Lektion setzt du diese Erkenntnisse in die Tat um. Ein System-Prompt, der einen kontrollierten Testsatz einmal besteht, ist ein Ausgangspunkt. Ein System-Prompt, der diagnostiziert, überarbeitet und gegen bekannte Fehlerfälle erneut getestet wurde, ist ein produktionsreifer Anweisungssatz.
Die Arbeit, die du hier leistest, fließt direkt in die Bewertung von Sprint 3 ein. Der finalisierte System-Prompt, den du in dieser Lektion erstellst, ist genau das, was in der Sprint-3-Bewertung geprüft wird.
## Das Rahmenwerk zur Überprüfung des System-Prompts
Bevor du deine Testergebnisse diagnostizierst, wende das folgende Vier-Fragen-Rahmenwerk auf deinen aktuellen System-Prompt an. Lies jede Anweisung im Licht jeder Frage und markiere jede Anweisung, die nicht alle vier klar beantworten kann.
- Frage 1: Ist der Umfang eindeutig festgelegt? Legt die Anweisung genau fest, was der Agent in dieser Situation tun soll und was nicht? Eine Anweisung wie „Antworte hilfreich" hat keinen eindeutig festgelegten Umfang. Eine Anweisung wie „Antworte ausschließlich anhand der aus der Qdrant-Wissensdatenbank abgerufenen Inhalte und nutze kein allgemeines Trainingswissen" hat einen eindeutig festgelegten Umfang.
- Frage 2: Ist die Auslösebedingung konkret? Legt die Anweisung die genaue Bedingung fest, die erfüllt sein muss, bevor der Agent die beschriebene Handlung ausführt? Bei Tool-Beschreibungen bedeutet das die konkrete Eigenschaft der Anfrage, die den Aufruf auslöst. Bei System-Prompt-Anweisungen bedeutet das die konkrete Situation, die die Anweisung regelt.
- Frage 3: Ist der Ausschluss festgelegt? Sagt die Anweisung sowohl, was der Agent tun soll, als auch, was er nicht tun soll? Anweisungen, die nur das gewünschte Verhalten beschreiben, überlassen es dem Agenten, zu erschließen, was untersagt ist. Ausdrückliche Ausschlüsse beseitigen dieses Erschließen.
- Frage 4: Ist die Grenze zwischen den Anweisungen klar? Lies alle deine Anweisungen zusammenhängend. Gibt es eine Anfrage, die zwei Anweisungen gleichzeitig erfüllen könnte? Gibt es Formulierungen, die im Geltungsbereich mehr als einer Anweisung vorkommen? Unklare Grenzen sind die häufigste Ursache für inkonsistentes Verhalten in System-Prompts mit mehreren Anweisungen.
## Deine Aufgaben
## Aufgabe A: Das Rahmenwerk auf deinen aktuellen System-Prompt anwenden
Prüfe jede der drei zentralen Anweisungen in deinem Tool-Agent-System-Prompt (Anweisung zum Abfrageumfang, Anweisung zur Grenze bei Kontoaktionen und Anweisung zum Ausweichverhalten) anhand der vier oben genannten Rahmenwerk-Fragen.
Fülle für jede Anweisung folgende Tabelle aus:
[TABLE]
  |  | Abfrageumfang | Grenze bei Kontoaktionen | Ausweichverhalten |
  | Umfang eindeutig? |  |  |  |
  | Auslösebedingung konkret? |  |  |  |
  | Ausschluss festgelegt? |  |  |  |
  | Grenze klar? |  |  |  |
Markiere jede Zelle mit
- ✅, wenn die Anweisung das Kriterium erfüllt, oder ❌, wenn nicht.
- Schreibe für jedes ❌ einen Satz, der beschreibt, was fehlt und welches Fehlerverhalten dieses Fehlen ermöglicht.
## Aufgabe B: Deine Testergebnisse diagnostizieren
Kehre zu den acht protokollierten Ergebnissen deiner Validierungstests zurück. Führe für jeden Test, der nicht das erwartete Verhalten erzeugt hat, folgende Diagnose durch:
### Schritt 1: Die Fehlerkategorie bestimmen
Ordne jeden Fehler einer der folgenden vier Kategorien zu:
- Falsches Tool aufgerufen: Der Agent hat ein anderes Tool ausgewählt als das, das die Anfrage eigentlich hätte auslösen sollen
- Tool nicht aufgerufen: Der Agent hat eine Antwort aus Trainingsdaten generiert, statt das passende Tool aufzurufen
- Ausweichformulierung nicht ausgelöst: Der Agent hat für eine Anfrage außerhalb des Themenbereichs eine Antwort generiert, statt die Ausweichformulierung zu liefern
- Grenzfehler: Der Agent hat suggeriert, er könne eine Handlung ausführen, zu der er nicht in der Lage ist, oder hat Informationen abgerufen, obwohl er den Kunden an einen anderen Kanal hätte verweisen sollen
### Schritt 2: Den Fehler auf seine Anweisung zurückführen
Bestimme für jeden Fehler, welche konkrete Anweisung (oder deren Fehlen) ihn verursacht hat. Nutze das Rahmenwerk aus Aufgabe A, um deine Diagnose zu leiten. Ein falsch aufgerufenes Tool lässt sich meist auf eine nicht ausreichend konkrete Auslösebedingung zurückführen. Ein Ausbleiben der Ausweichformulierung lässt sich meist auf eine Anweisung zum Abfrageumfang zurückführen, die die Nutzung von allgemeinem Trainingswissen nicht ausdrücklich untersagt.
### Schritt 3: Eine gezielte Überarbeitung schreiben
Schreibe für jeden Fehler eine überarbeitete Version der Anweisung, die ihn verursacht hat. Deine Überarbeitung muss unmittelbar auf die in Schritt 2 festgestellte konkrete Schwachstelle eingehen. Schreibe nicht den gesamten System-Prompt um. Nimm nur gezielte Änderungen vor. Eine Überarbeitung, die alles ändert, macht es unmöglich, herauszufinden, welche Änderung welches Problem behoben hat.
## Aufgabe C: Umsetzen und erneut testen
Trage deine überarbeiteten Anweisungen in das Feld System Message des Tool-Agent-Nodes ein. Speichere den Chatflow.
Führe nur die Tests aus, die zuvor fehlgeschlagen sind. Führe noch nicht alle acht Tests erneut durch. Protokolliere für jeden zuvor fehlgeschlagenen Test, ob die überarbeitete Anweisung das erwartete Verhalten hervorgebracht hat.
Besteht der Test jetzt, markiere ihn als behoben. Schlägt er weiterhin fehl, kehre zu Schritt 2 von Aufgabe B zurück und überprüfe die Anweisung erneut. Ein anhaltender Fehler nach einer gezielten Überarbeitung bedeutet meist, dass die Diagnose unvollständig war. Der Fehler wird durch eine andere Anweisung verursacht als die, die du überarbeitet hast, oder durch einen Konflikt an der Grenze zwischen zwei Anweisungen.
Sobald alle zuvor fehlgeschlagenen Tests bestanden werden, führe alle acht Tests der Reihe nach durch, um zu bestätigen, dass deine Überarbeitungen keine neuen Fehler eingeführt haben. Dieser vollständige Regressionstest ist die endgültige Bestätigung, dass dein System-Prompt stabil ist.
## Aufgabe D: Den finalisierten System-Prompt erstellen
Schreibe deinen vollständigen, finalisierten System-Prompt als ein zusammenhängendes Dokument. Das ist die Version, die du in die Sprint-3-Bewertung und die Sprint-4-Präsentation mitnimmst.
Dein finalisierter System-Prompt muss alle folgenden Elemente in dieser Reihenfolge enthalten:
1. Rollen- und Kontextangabe: Ein bis zwei Sätze, die festlegen, wer der Agent ist, welche Organisation er vertritt und in welchem Betriebskontext er steht.
1. Anweisung zum Abfrageumfang: Die überarbeitete Anweisung, die festlegt, dass der Agent ausschließlich anhand der aus der Qdrant-Wissensdatenbank abgerufenen Inhalte antwortet und kein allgemeines Trainingswissen nutzt.
1. Anweisung zur Grenze bei Kontoaktionen: Die überarbeitete Anweisung, die festlegt, was der Agent erklären kann im Gegensatz zu dem, was er nicht ausführen kann, und wohin Kunden verwiesen werden, wenn eine Kontoänderung angefragt wird.
1. Hinweis zum Tool-Aufruf: Ein bis zwei Sätze im System-Prompt, die verdeutlichen, wann das Kreditstatus-Tool aufgerufen werden soll, insbesondere dass vom Kunden zunächst eine eindeutige Antragsreferenz vorliegen muss, bevor es aufgerufen wird.
1. Anweisung zum Ausweichverhalten: Die überarbeitete Anweisung, die die exakte Ausweichformulierung, die Auslösebedingung und den nächsten Schritt für den Kunden festlegt.
1. Ausweichverhalten bei Tool-Fehlern: Die Anweisung, die festlegt, was der Agent sagt, wenn ein Tool einen Fehler zurückgibt oder die Max-Iterations-Grenze erreicht wird, unter Abdeckung von ehrlichem Eingeständnis, keinen technischen Details und einem klaren nächsten Schritt.

[toggle] Checkpoints
  - Checkpoint 1: Einen falschen Tool-Aufruf diagnostizieren - Ruft der Agent das falsche Tool auf, liegt das Problem fast immer in der Auslösebedingung (was laut Beschreibung erfüllt sein muss, bevor das Tool aufgerufen wird). Lies die Auslösebedingung des fälschlicherweise ausgewählten Tools. Lies dann die Anfrage, die es ausgelöst hat. Finde die konkrete Formulierung in der Anfrage, die semantisch mit der Auslösebedingung übereinstimmte, und überarbeite die Bedingung so, dass diese Übereinstimmung ausdrücklich ausgeschlossen wird.
  - Checkpoint 2: Einen Ausweichfehler diagnostizieren - Wird die Ausweichformulierung bei einer Anfrage außerhalb des Themenbereichs nicht ausgelöst, ist die Anweisung zum Abfrageumfang meist nicht restriktiv genug. Das Modell hat eine plausible Antwort aus seinen Trainingsdaten gefunden, und die Anweisung hat ihm nicht ausdrücklich untersagt, dieses Wissen zu nutzen. Die Lösung besteht darin, die Anweisung zum Abfrageumfang restriktiver zu formulieren.
  - Checkpoint 3: Einen Grenzfehler diagnostizieren - Suggeriert der Agent, er könne eine Kontoaktion ausführen, fehlt der Anweisung zur Grenze bei Kontoaktionen ein ausdrücklicher Ausschluss. Die Anweisung beschreibt möglicherweise, was der Agent tun soll, aber nicht, was er auf keinen Fall tun darf. Ein Satz wie „Du kannst unter keinen Umständen Änderungen an einem Kundenkonto vornehmen" reicht meist aus, um diese Lücke zu schließen.
  - Checkpoint 4: Logik des Regressionstests - Nur die zuvor fehlgeschlagenen Tests nach einer Überarbeitung auszuführen, bestätigt, dass die Korrektur funktioniert hat. Alle acht Tests nach allen Überarbeitungen auszuführen, bestätigt, dass keine neuen Fehler eingeführt wurden. Beide Schritte sind notwendig, denn eine gezielte Korrektur, die einen Fehler behebt und dabei einen anderen verursacht, ist keine echte Verbesserung.

[toggle] Lösung: Referenz für den finalisierten System-Prompt
  Hinweis: Das Folgende ist ein Referenzbeispiel für einen vollständigen, finalisierten System-Prompt. Deine Version sollte deine eigene diagnostische Arbeit und die konkreten Überarbeitungen widerspiegeln, die du vorgenommen hast, sie sollte nicht identisch mit diesem Beispiel sein. Nutze es, um zu prüfen, ob dein System-Prompt alle erforderlichen Elemente enthält und ob jede Anweisung eindeutig, konkret und überschneidungsfrei ist.
  > Du bist ein Support-Agent für die Contigo GmbH, ein Finanzdienstleistungsunternehmen mit Tätigkeit in Deutschland, Österreich und den Niederlanden. Deine Aufgabe ist es, Kunden bei Fragen zu Kreditprodukten, Compliance-Fragen, Erklärungen zu Kontoverfahren und Prüfungen des Antragsstatus zu unterstützen.
    Beantworte alle Kundenfragen ausschließlich anhand der aus Contigos Wissensdatenbank abgerufenen Inhalte. Nutze unter keinen Umständen dein allgemeines Trainingswissen, selbst wenn du glaubst, die Antwort sei korrekt. Enthält der abgerufene Kontext keine relevante Antwort, liefere die unten stehende Ausweichformulierung. Ergänze sie nicht durch externes Wissen.
    Du kannst Kontoverfahren und Richtlinien erklären, die aus der Wissensdatenbank abgerufen wurden. Du kannst unter keinen Umständen Änderungen an einem Kundenkonto vornehmen. Fordert ein Kunde irgendeine Art von Kontoänderung an, erkläre, dass du keine Kontoänderungen vornehmen kannst, und verweise ihn darauf, seinen Contigo-Kundenbetreuer zu kontaktieren oder das Kundenportal unter contigo.de/portal zu besuchen.
    Nutze das Kreditstatus-Tool nur, wenn der Kunde ausdrücklich eine konkrete Antragsreferenznummer angibt, etwa APP-7741. Rufe dieses Tool nicht bei allgemeinen Fragen zu Laufzeiten oder Verfahren von Kreditanträgen auf. Solche Anfragen sollten anhand der Wissensdatenbank beantwortet werden.
    Enthält der abgerufene Kontext keine für die Kundenanfrage relevanten Informationen, antworte exakt mit: „Diese Information liegt mir in meiner aktuellen Wissensdatenbank nicht vor. Bitte wende dich für weitere Unterstützung direkt an einen Contigo-Berater." Ergänze oder verändere diese Formulierung nicht.
    Gibt ein Tool einen Fehler zurück oder liefert es kein Ergebnis, antworte mit: „Ich konnte diese Information zu diesem Zeitpunkt nicht abrufen. Bitte wende dich für Unterstützung direkt an deinen Contigo-Kundenbetreuer." Zeige in keiner kundenseitigen Antwort Fehlercodes, API-Referenzen oder technische Details.
## Checkliste: Vor dem Fortfahren bestätigen
- [ ] Vier-Fragen-Rahmenwerk auf alle drei zentralen Anweisungen angewendet
- [ ] Alle Testfehler aus der Diagnose-Lektion diagnostiziert und auf konkrete Anweisungen zurückgeführt
- [ ] Gezielte Überarbeitungen für jede fehlerhafte Anweisung geschrieben
- [ ] Zuvor fehlgeschlagene Tests erneut getestet und als bestanden bestätigt
- [ ] Vollständiger Regressionstest aller acht Tests durchgeführt, ohne neue Fehler
- [ ] Finalisierter System-Prompt mit allen sechs erforderlichen Elementen geschrieben
- [ ] Finalisierter System-Prompt im Feld System Message des Tool Agent gespeichert
- [ ] Chatflow nach der finalen Aktualisierung des System-Prompts gespeichert
> 💡 Fazit:
  Ein System-Prompt ist nicht abgeschlossen, sobald die Anweisungen geschrieben sind. Er ist abgeschlossen, sobald das Verhalten des Agenten über ein vollständiges Spektrum realistischer Anfragen hinweg konsistent mit den Anweisungen übereinstimmt. Diagnose, Überarbeitung und Regressionstest sind keine zusätzlichen Schritte.
  Sie sind der eigentliche Prozess. Der finalisierte System-Prompt, den du in dieser Lektion erstellt hast, ist das wichtigste einzelne Artefakt in deinem Chatflow-Aufbau. Er entscheidet darüber, ob der Agent zuverlässig reagiert, wenn ein echter Kunde eine unerwartete Frage stellt.
