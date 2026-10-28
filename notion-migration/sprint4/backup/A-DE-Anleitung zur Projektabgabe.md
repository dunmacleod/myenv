# Anleitung zur Projektabgabe

Notion page: https://app.notion.com/p/Anleitung-zur-Projektabgabe-3c79418319f381bfa7bbf365ec345efb
Backed up before n8n migration

## 1. Intro
Der Redesign ist abgeschlossen und die Tests sind gelaufen. Diese Seite schließt das Modulprojekt ab: was du zusammenstellst, wie die Präsentation abläuft, worauf der Evaluator achtet und wie du die Arbeit übergibst.
Über vier Sprints hinweg hast du eine Reihe von Abgaben produziert, die aufeinander aufbauen — das Architektur-Entscheidungsbriefing, das das Pattern benennt, das Multi-Agent-Designdiagramm, das zeigt, wie die Agenten zueinander stehen, die Memory- und State-Spezifikation, die beschreibt, was das System weiß und was es vergisst, und die neu entworfene Canvas mit dem Testnachweis, der belegt, dass sie sich so verhält, wie die Spezifikation es sagt. In Sprint 4 ist das Scaffolding weggefallen. Was du abgibst, ist deine eigene Architektur auf deiner eigenen Domäne.
Die Fähigkeiten, die du über das Modul hinweg geübt hast:
- Einen Business Case lesen und in eine Architekturentscheidung übersetzen, die gegen die verworfene Alternative verteidigt werden kann
- Entscheiden, wann ein Agent genügt und wann mehrere Agenten ihre Koordinationskosten wert sind
- Spezialisierungen, Grenzen und Routing-Strategien für ein Multi-Agent-Design definieren
- Memory- und State-Grenzen ziehen — was geteilt wird, was privat bleibt, was niemals persistieren darf
- Fehlerisolation und State Recovery so entwerfen, dass das Scheitern eines Agenten den geteilten State nicht korrumpiert
- Das Design auf einer Agentflow-V2-Canvas implementieren und gegen die Fehlermodi testen, für die du es entworfen hast
- Implementierung von Validierung trennen — eine Canvas, die konfiguriert wurde, ist noch keine Canvas, die verifiziert wurde
## 2. Aufgaben
Die Abgabe stützt sich auf eine Abgabe pro Sprint, plus die Integrationsarbeit.
1. Sprint 1: Architekturentscheidung. Das einseitige Architektur-Entscheidungsbriefing mit den sechs Abschnitten — Entscheidung, Pattern, Inputs und Outputs, die drei Säulen, verworfene Alternative und die Bedingungen, unter denen du die Entscheidung neu prüfen würdest.
1. Sprint 2: Multi-Agent-Design. Das Designdiagramm mit jedem benannten Agenten, dem gezeigten Informationsfluss, markierten Routing-Entscheidungspunkten, ausgewiesenen Informationsgrenzen und mindestens einem Fallback-Pfad — plus die schriftliche Design-Begründung mit Diagnose und Rechtfertigung, Agentenrollen, Informationsgrenze und Fallback-Strategie.
1. Sprint 3: Memory- und State-Architektur. Die vierteilige Spezifikation: die Memory Boundary Map mit Persistenz-Scope, was nicht persistieren darf und wie jeder Punkt verhindert wird, das State-Recovery-Design mit Fehlerszenario und sicherem State, und die Bewertung der Fehlerisolation — welcher Agent welche State-Schlüssel schreiben darf.
1. Sprint 4: Integration und Testing. Der Redesign in vier Stages — Archetyp auf der Canvas umgesetzt, Memory-Grenzen durchgesetzt, State Handoff und Recovery verdrahtet, die fünf Schutzmaßnahmen bestätigt. Dann die neun Tests in drei Gruppen: Basisfunktion, Grenzbedingungen und architekturspezifische Validierung. Nachschärfen, bis jede Schutzmaßnahme unter dem Test hält, für den sie entworfen wurde, und die Canvas exportieren.
## 3. Projektartefakte
Drei Ebenen: was du baust, wie gut du es erklären kannst und eine kurze schriftliche Zusammenfassung, die die Teile miteinander verbindet.
### Technische Artefakte
Bis zum Abgabetag solltest du Folgendes haben:
- Die finale Canvas als JSON exportiert — die Version nach der Testarbeit, ladbar in einer frischen Flowise-Instanz ohne fehlende Konfiguration. Behalte die früheren Exporte; abgegeben wird der finale.
- Das Architektur-Entscheidungsbriefing aus Sprint 1 — eine Seite, sechs Abschnitte, gebunden an das Geschäftsproblem, das du gewählt hast.
- Das Multi-Agent-Designdiagramm — aktualisiert auf die implementierte Architektur, nicht der Entwurf aus Sprint 2. Wenn sich die Canvas im Redesign geändert hat, ändert sich das Diagramm mit.
- Die schriftliche Design-Begründung aus Sprint 2 — maximal 400 Wörter, mit der verworfenen Alternative, wo zutreffend.
- Die Memory- und State-Architekturspezifikation aus Sprint 3 — alle vier Abschnitte, aktualisiert, falls der Redesign State-Schlüssel ergänzt oder entfernt hat.
- Den Testnachweis — die neun Tests über die drei Gruppen, mit dem erwarteten Verhalten vor dem Lauf und dem tatsächlichen Verhalten danach, plus was du daraufhin geändert hast und welcher Test nicht durchführbar war und warum.
### Analytisches Reasoning
Für deine Präsentation solltest du erklären können:
- Warum du den Archetyp gewählt hast, den du gewählt hast. Welche Eigenschaft deines Geschäftsproblems machte ihn passend? Was war die verworfene Alternative, und warum wurde sie verworfen?
- Warum das Design die Verantwortlichkeiten dort teilt, wo es sie teilt. Wie lautet die Grenzaussage zwischen den Agenten, und was passiert bei einer Anfrage, die zwei davon berührt?
- Warum die Memory-Grenzen dort liegen, wo sie liegen. Was ist geteilt und warum, was ist privat und warum, was darf niemals persistieren und warum.
- Was passiert, wenn ein Spezialagent scheitert — was es erkennt, was zurückgesetzt wird und in welcher Reihenfolge die Kontrolle zurückkehrt.
- Was die Tests sichtbar gemacht haben. Wo hat einer eine Designentscheidung bestätigt, und wo hat einer eine Lücke offengelegt, die eine Änderung an Canvas oder Spezifikation erzwungen hat?
- Was du mit einer weiteren Woche tun würdest. Konkret, nicht „es besser machen".
### Schriftliche Zusammenfassung
Ein kurzes PDF, ein bis zwei Seiten, das das ganze Projekt zusammenbindet. Enthalten sein sollte:
- Ein Absatz zur Problemrahmung: was dein Geschäftsproblem ist und warum die Designarbeit dafür zählt.
- Ein Absatz als Lösungsüberblick: was deine Architektur tut und welche Form sie hat.
- Zwei oder drei Bulletpoints, die die interessantesten Entscheidungen der vier Sprints benennen — mit der Alternative, die du erwogen und verworfen hast.
- Ein Absatz Reflexion darüber, was dein Testing sichtbar gemacht hat, und eine Limitation, die du nicht vollständig auflösen konntest.
Die Zusammenfassung ist für jemanden, der deine Präsentation nicht gesehen hat. Sie muss für sich allein lesbar sein.
## 4. Präsentationskontext
Die Präsentation ist verpflichtend und die zentrale Bewertungsmethode für dieses Projekt.
Format: Live, vor der Kohorte, mit Q&A. Zielzeit: 5–7 Minuten für die Präsentation selbst, plus ein paar Minuten Q&A. Ziele auf die Mitte — knappe 6 Minuten sind besser als ausschweifende 7.
Die Präsentation hat drei Komponenten. Alle drei sind erforderlich. Eine Präsentation, die nur die Canvas ohne Diagramm abdeckt, oder das Diagramm ohne Designentscheidungen, ist unvollständig.
### Komponente 1: Die Canvas, live
Ein Live-Lauf deiner neu entworfenen Canvas. Der Execution Trace zeigt, welche Nodes aktiviert wurden, in welcher Reihenfolge und was in den State geschrieben wurde — und genau das beobachtet der Raum, nicht nur den Antworttext.
Halte zwei Anfragen bereit: eine, die den häufigsten Pfad durch deine Architektur nimmt, und eine, die eine Grenzbedingung ausübt — die Scope-Kante oder den Recovery-Pfad. Du kommst vielleicht nicht zu beiden, aber beide bereit zu haben, erlaubt dir zu antworten, wenn der Instructor einen bestimmten Pfad sehen will.
### Komponente 2: Das Systemdiagramm
Das Diagramm ist der visuelle Anker für die Verteidigung. Wenn du eine Designentscheidung laut benennst, sollte das Diagramm sie zeigen. Es braucht kein bestimmtes Tool; es muss auf einem geteilten Screen lesbar und korrekt sein. Wenn das Diagramm drei Spezialagenten zeigt und die Canvas zwei hat, ist diese Diskrepanz die erste Frage.
### Komponente 3: Die Verteidigung
Ein mündlicher Bericht über die Designentscheidungen, entlang der drei Bereiche, die den Sprint-Abgaben entsprechen:
- Architektur: warum dieser Archetyp, was die verworfene Alternative war und unter welchen Bedingungen du die Entscheidung neu prüfen würdest.
- Multi-Agent-Design: wie sich Verantwortlichkeiten teilen, welchen Koordinationsansatz du gewählt hast und warum, und was passiert, wenn ein Agent scheitert.
- Memory und State: was geteilt und was privat ist, was niemals persistieren darf, und wie das System nach einer Unterbrechung wiederherstellt.
Die Verteidigung ist ein Bericht darüber, warum diese Entscheidungen für die konkrete Domäne und das konkrete Geschäftsproblem richtig waren, das du gewählt hast — keine Aussage über allgemeine Prinzipien von Multi-Agent-Systemen.
### Wie die 5–7 Minuten strukturiert sind
Nutze das als Leitfaden.
- Minuten 0–1: Kontext und Canvas. Deine Domäne und dein Geschäftsproblem in einem Satz, dein Archetyp in einem weiteren. Dann die Anfrage auf dem häufigsten Pfad live ausführen und den Trace kurz kommentieren, während er läuft — welcher Agent klassifiziert, welcher Spezialagent antwortet, was in den State geschrieben wird.
- Minuten 1–2: Architektur und Designentscheidungen. Gehe das Diagramm durch und deck die drei Verteidigungsbereiche in Reihenfolge ab. Benenne die Entscheidung und den Grund dafür, ein bis zwei Sätze pro Punkt. Lies die Sprint-Abgaben nicht vor.
- Minuten 2–4: Testnachweis. Zwei oder drei Erkenntnisse — ein Test, der eine Designentscheidung bestätigt hat, und einer, der eine Lücke sichtbar gemacht und eine Änderung erzwungen hat. Benenne den Test, was er gezeigt hat, was du geändert hast. Das unterscheidet eine implementierte Architektur von einer beschriebenen.
- Minuten 4–5: Zweite Anfrage, wenn die Zeit reicht. Die Grenzbedingung oder die Recovery-Demonstration. Für ein technisch interessiertes Publikum ist das der überzeugendste Teil des Laufs.
- Minuten 5–7: Fragen.
Fokussiere dich auf Reasoning und Kommunikation. Die Präsentation ist kein Code-Walkthrough. Klicke nicht durch jeden Node. Lies deinen System-Prompt nicht laut vor. Zeige keine JSON-Schemas. Zeige das Denken hinter der Architektur — die Entscheidungen, die du getroffen hast, warum du sie getroffen hast, was du anders machen würdest.
## 5. Qualitätsanforderungen / Bewertung
Deine Bewertung basiert auf der Präsentation, nicht auf den Artefakten isoliert. Die Artefakte werden abgegeben, damit der Reviewer überprüfen kann, was du sagst, und deine Canvas bei Bedarf ausführen kann.
Die Bewertung umfasst vier Dimensionen:
[TABLE]
  | Dimension | Worauf der Evaluator achtet |
  | Architekturkohärenz | Fügen sich die vier Sprint-Entscheidungen zu einem Design zusammen, oder lesen sie sich als unabhängige Übungen, die nie miteinander abgeglichen wurden? |
  | Begründung der Entscheidungen | Ist jede wesentliche Entscheidung in einer konkreten Eigenschaft des Geschäftsproblems und der Domäne verankert, oder auf der Ebene allgemeiner Prinzipien formuliert („Multi-Agent skaliert besser")? |
  | Implementierungsnachweis | Passt die Canvas zu den Designdokumenten? Zeigt der Testnachweis, dass die Canvas tatsächlich ausgeführt und nicht nur beschrieben wurde? |
  | Fehlerbehandlung | Kann der Lernende sagen, was das System tut, wenn etwas schiefgeht — ein Spezialagent scheitert, ein Classifier liefert fehlerhaften Output, ein State-Schlüssel hält einen veralteten Wert? |
Es gibt keine einzige richtige Architektur. Die Bewertung prüft nicht, welchen Archetyp du gewählt hast. Sie prüft, ob die Architektur, die du gewählt hast, angesichts des Geschäftsproblems, das du in Sprint 1 beschrieben hast, kohärent, implementiert und verteidigbar ist.
## 6. Vorbereitungsliste
Erledige diese Punkte vor der Live Session. Lass keinen Punkt für die Session selbst übrig.
- [ ] Finale Canvas als JSON exportiert und in einer frischen Flowise-Instanz als ladbar bestätigt
- [ ] Systemdiagramm auf die implementierte Architektur aktualisiert — Rollen, State Flow, Recovery-Pfad
- [ ] Zwei Anfragen vorbereitet: eine für den häufigsten Pfad, eine für eine Grenzbedingung oder den Recovery-Pfad
- [ ] Alle vier Sprint-Abgaben durchgesehen, sodass die zentralen Entscheidungen im Kopf sind und nicht nur in Dokumenten
- [ ] Testnachweis durchgesehen, mit mindestens einem bestätigenden und einem lückenaufdeckenden Ergebnis parat
- [ ] Antwort auf die wahrscheinlichste harte Frage vorbereitet: warum dieser Archetyp und nicht die verworfene Alternative
- [ ] Für jede Schutzmaßnahme, die auf deine Architektur nicht zutrifft, liegt die Ein-Satz-Begründung schriftlich vor
- [ ] Schriftliche Zusammenfassung entworfen, ein bis zwei Seiten, als PDF exportiert
- [ ] Präsentation einmal end-to-end gegen die 5–7-Minuten-Struktur getimt
- [ ] Keine Credentials, API-Keys oder privaten Tokens im Export oder in den Dokumenten
## 7. Abgabe- / Lieferanweisungen
Die Abgabe dient Zugriff und Review. Die Bewertung findet während der Präsentation statt. Das sind zwei getrennte Schritte.
### Was abgegeben werden muss
Bündle alles in einem einzigen Abgabepaket (einem geteilten Google-Drive-Ordner):
1. Die finale Canvas als JSON exportiert, oder ein Link auf die Canvas in deiner Flowise-Instanz, sofern der Link für den Reviewer zugänglich ist.
1. Ein Dokument (.md oder .pdf) mit den folgenden Inhalten, in dieser Reihenfolge:
  1. Das Architektur-Entscheidungsbriefing
  1. Das Multi-Agent-Designdiagramm
  1. Die schriftliche Design-Begründung
  1. Die Memory- und State-Architekturspezifikation
  1. Den Testnachweis
1. Die schriftliche Zusammenfassung als PDF.
### Wo und wann
Gib deine Arbeit als Link auf einen Google-Drive-Ordner ab. Lege alle Artefakte hinein und teile den Link in der Abgabelektion.
> ⚠️ Wichtig: Stelle sicher, dass die Ordnerberechtigungen es allen Personen mit dem Link erlauben, jede Datei darin zu öffnen. Teste den Link in einem Inkognito-Fenster, bevor du ihn abgibst. Nimm keine Credentials, API-Keys oder privaten Tokens in den Export oder in die Dokumente auf.
### Was nicht Teil der Bewertung ist
- Teilnahme an der Code Clinic. Nicht bewertet.
- Die Anzahl der Artefakte, die du über die gelisteten hinaus produzierst.
- Die visuelle Politur deiner Slides. Klare Gedanken zählen mehr als schöne Slides — was nicht heißt, dass sie lieblos zusammengestellt sein sollten.
## Finaler Check
Lies vor deiner Präsentation dein Systemdiagramm durch und stelle dir diese Fragen. Es sind die Fragen, die der Instructor während deiner Verteidigung stellen wird.
- Kannst du jeden Agenten im Diagramm benennen und sagen, wofür er verantwortlich ist, ohne auf die Canvas zu schauen?
- Erscheint jeder State-Schlüssel der Canvas in deiner Spezifikation, und hat jeder genau einen festgelegten Schreiber?
- Kannst du sagen, was nach einem Fehler zurückgesetzt wird, bevor die Kontrolle zurückkehrt, und warum die Reihenfolge zählt?
- Passt das Diagramm zur Canvas im heutigen Stand, nicht zum Stand aus Sprint 2?
- Kannst du einen Test benennen, der dein Design verändert hat, und sagen, was er verändert hat?
Wenn eine dieser Fragen Unsicherheit auslöst, ist das nützliche Information. Nutze die Zeit vor der Session für die, bei der es am meisten gehakt hat.
## Zusammenfassung
Das Modulprojekt bewegt sich von einer Reihe von Designdokumenten und einer Canvas zu etwas, hinter dem du stehen und das du erklären kannst. Das Briefing hat ein Pattern benannt, das Diagramm hat die Beziehungen gezeigt, die Spezifikation hat die Grenzen gezogen, und die Testarbeit hat aus all dem eine Behauptung mit Evidenz gemacht.
Worauf es jetzt ankommt, ist Kohärenz: Canvas, Diagramm, Spezifikation und der Bericht, den du darüber gibst, beschreiben dasselbe System. Stelle die Artefakte zusammen, timee den Durchlauf einmal, und sei bereit zu sagen, was du ändern würdest.