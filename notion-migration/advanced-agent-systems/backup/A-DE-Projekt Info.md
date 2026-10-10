# Projekt Info

Notion page: https://app.notion.com/p/Projekt-Info-a779418319f3830297c081b0303b130c
Backed up before n8n migration

## 
## 1. Intro
Im Modulprojekt konzipierst und implementierst du eine maßgeschneiderte Agentenarchitektur für ein Geschäftsproblem deiner Wahl. Über vier Sprints hinweg hast du eine Reihe von Abgaben erarbeitet, die nahtlos aufeinander aufbauen: das Architekturentscheidungsbriefing zur Festlegung des passenden Patterns, das Multi-Agent-Designdiagramm zur Veranschaulichung der Agenten-Interaktionen, die Memory- und State-Spezifikation zur Definition des Systemwissens und des Daten-Resets sowie die finale Integrationsarbeit auf der Flowise-Canvas, die diese Entscheidungen in ein lauffähiges System verwandelt.

Die Fähigkeiten, die du über das Modul hinweg geübt hast:
- Einen Business Case (deinen eigenen) lesen und in eine Architekturentscheidung übersetzen, die gegenüber Alternativen verteidigbar ist
- Entscheiden, wann ein Agent ausreicht und wann mehrere Agenten ihre Koordinationskosten rechtfertigen
- Spezialisierungen, Grenzen und Hybrid-Query-Strategien für Multi-Agent-Designs definieren
- Memory- und State-Grenzen entwerfen — was geteilt ist, was privat ist, was niemals persistieren darf
- Fehlerisolation und State-Recovery-Pfade entwerfen, damit der Fehler eines Agenten geteilten State nicht korrumpiert
- Das Design auf einer Flowise-Agentflow-V2-Canvas implementieren und gegen die Fehlermodi testen, für die du designt hast
Die Flowise-Canvas, mit der du begonnen hast, war ein Baseline-Agentflow-V2-Template mit drei Nodes. Deine finale Canvas spiegelt die vollständige Architektur wider, die du über die vier Sprints hinweg entworfen hast. Kein Neubau von Grund auf, sondern ein bewusstes Redesign der Baseline zu etwas, das zu deinem Briefing passt.
## 2. Aufgaben
Vier Sprints Arbeit, jeder davon mit Artefakten, die du in deine finale Abgabe bündelst.
1. Sprint 1 — Architekturentscheidung. Lies deinen gewählten Business Case. Wende das Vier-Fragen-Framework an, um zwischen Single-Agent und Multi-Agent zu entscheiden. Benenne das Pattern. Schreibe ein einseitiges Architekturentscheidungsbriefing, das die sechs Abschnitte abdeckt (Entscheidung, Pattern, Inputs und Outputs, die drei Säulen, verworfene Alternative, Bedingungen für eine Neubewertung).
1. Sprint 2 — Multi-Agent-Design. Erstelle ein Designdiagramm deiner Agentenarchitektur — jeder Agent benannt, Informationsfluss gezeigt, Routing-Entscheidungspunkte markiert, Informationsgrenzen hervorgehoben, mindestens ein Fallback-Pfad. Schreibe eine Designbegründung, die Diagnose und Begründung, Agentenrollen, Informationsgrenze und Fallback-Strategie abdeckt. Notiere, falls zutreffend, die verworfene Alternative.
1. Sprint 3 — Memory- und State-Architektur. Erstelle die vierteilige Spezifikation: Memory Boundary Map (shared vs. private vs. conditional, mit Persistenz-Scope), was nicht persistieren darf (mit Kategorie und Präventionsstrategie für jedes Element), State-Recovery-Design (Fehlerszenario, sicherer State und spezifischer Recovery-Mechanismus) und Fehlerisolation (welche Agenten unter welchen Bedingungen in welche State-Schlüssel schreiben dürfen).
1. Sprint 4 — Integration und Testing. Implementiere das Design auf der Flowise-Canvas: Richte den Archetyp ein, erzwinge Memory-Grenzen, verdrahte State Handoff und Recovery und füge die spezifischen Schutzmaßnahmen hinzu, die du für die Fehlermodi entworfen hast. Führe das Testset aus (Baseline-, Boundary- und architekturspezifische Tests). Verfeinere, bis jede Schutzmaßnahme unter den Tests hält, für die sie entworfen wurde. Exportiere die Canvas.
## 3. Projektartefakte
Drei Ebenen: was du baust, wie gut du es erklären kannst und eine kurze schriftliche Zusammenfassung, die die Teile miteinander verbindet.
### Technische Artefakte
Bis zum Abgabetag solltest du Folgendes haben:
- Die Flowise-Canvas als JSON exportiert — deine finale Version nach der Integrations- und Testing-Arbeit in Sprint 4. In einer frischen Flowise-Instanz ladbar, ohne fehlende Konfiguration.
- Architekturentscheidungsbriefing aus Sprint 1 — eine Seite, sechs Abschnitte, an dein spezifisches Geschäftsproblem gebunden.
- Multi-Agent-Designdiagramm aus Sprint 2 — auf einem geteilten Bildschirm lesbar, mit Agentenrollen, Informationsfluss, Routing-Entscheidungspunkten, Informationsgrenzen und mindestens einem markierten Fallback-Pfad.
- Schriftliche Designbegründung aus Sprint 2 — maximal 400 Wörter, die Diagnose und Begründung, Agentenrollen und Verantwortlichkeiten, Informationsgrenze und Fallback-Strategie abdeckt. Verworfene Alternative notiert, falls zutreffend.
- Memory- und State-Architekturspezifikation aus Sprint 3 — die vier Abschnitte: Memory Boundary Map, was nicht persistieren darf, State-Recovery-Design, Bewertung der Fehlerisolation.
- Testnachweis aus Sprint 4 — die Tests, die du gegen die Canvas ausgeführt hast (Baseline, Boundary und architekturspezifisch), erwartetes Verhalten vor dem Ausführen notiert, tatsächliches Verhalten danach geloggt und Notizen dazu, was du als Ergebnis geändert hast.
### Analytisches Reasoning
Für deine Präsentation solltest du erklären können:
- Warum du den Archetyp gewählt hast, den du gewählt hast. Welche spezifische Eigenschaft deines Geschäftsproblems machte den gewählten Archetyp passend? Was war die verworfene Alternative und warum?
- Warum das Multi-Agent-Design die Verantwortlichkeiten dort aufteilt, wo es sie aufteilt. Was ist die Boundary-Aussage zwischen den Agenten? Was passiert bei Hybrid Queries?
- Warum die Memory-Grenzen dort gezogen sind, wo sie gezogen sind. Was ist geteilt und warum? Was ist privat und warum? Was darf niemals persistieren und warum?
- Was die Tests sichtbar gemacht haben. Wo hat ein Test bestätigt, dass eine Designentscheidung wie erwartet funktioniert? Wo hat ein Test eine Lücke sichtbar gemacht und eine Änderung an der Canvas oder Spezifikation erforderlich gemacht?
- Was du mit einer weiteren Woche tun würdest. Konkret und spezifisch. Nicht „es besser machen" , sondern „Ich würde einen Fallback für den Fall hinzufügen, dass der Structured Output des Classifier fehlerhaft ist, weil meine aktuelle Schutzmaßnahme nur den Missing-Key-Fall abfängt."
### Schriftliche Zusammenfassung
Eine kurze PDF, ein bis zwei Seiten, der das gesamte Projekt zusammenbindet. Enthält:
- Einen Absatz zur Problemrahmung — was dein Geschäftsproblem ist und warum die Designarbeit dafür wichtig ist.
- Einen Absatz zur Lösungsübersicht — was deine Agentenarchitektur tut und welche Form sie hat.
- Zwei oder drei Bullet Points, die die interessantesten Entscheidungen nennen, die du über die vier Sprints hinweg getroffen hast (keine Features — Entscheidungen, mit der Alternative, die du erwogen und verworfen hast).
- Einen Absatz Reflexion darüber, was dein Testing sichtbar gemacht hat, und eine Einschränkung, die du nicht vollständig lösen konntest.
Die Zusammenfassung ist für jemanden gedacht, der deine Präsentation nicht gesehen hat. Sie sollte unabhängig lesbar sein. Gib sie als PDF ab; exportiere sie aus dem Tool, in dem du sie geschrieben hast.
## 4. Präsentationskontext
Die Präsentation ist verpflichtend und die zentrale Bewertungsmethode für dieses Projekt.
Format: Live, vor der Kohorte, mit Q&A. Zielzeit: 5–7 Minuten für die Präsentation selbst, plus ein paar Minuten Q&A. Ziele auf die Mitte — knappe 6 Minuten sind besser als ausschweifende 7.
Die Präsentation hat drei Komponenten. Alle drei sind erforderlich. Eine Präsentation, die nur die Canvas ohne Diagramm abdeckt, oder das Diagramm ohne Designentscheidungen, ist unvollständig.
### Komponente 1: Die Canvas, live
Eine Live-Demonstration deiner neu entworfenen Agentflow-V2-Canvas in Flowise. Du wirst während der Präsentation mindestens eine Anfrage ausführen — nicht, um zu beweisen, dass der Agent funktioniert, sondern um die Architektur sichtbar zu machen. Der Execution Trace in Flowise zeigt, welche Nodes aktiviert wurden, in welcher Reihenfolge und was in Flow State geschrieben wurde. Instructor und Peers werden auf den Trace achten, nicht nur auf den Output.
Bereite vor der Session zwei Anfragen vor:
- Eine, die den häufigsten Pfad durch deine Architektur nimmt (den Pfad, den der Großteil deines Testnachweises abdeckt).
- Eine, die eine Grenzbedingung auslöst (eine Anfrage, die die Scope-Grenze oder den Recovery-Pfad testet).
Du wirst in der verfügbaren Zeit möglicherweise nicht beide nutzen, aber wenn du beide vorbereitet hast, kannst du reagieren, falls der Instructor darum bittet, einen bestimmten Pfad zu sehen.
### Komponente 2: Das Systemdiagramm
Ein Diagramm, das deine Agentenarchitektur zeigt: Agentenrollen, Verantwortlichkeiten, Koordinationsansatz, die State-Schlüssel, die zwischen Agenten fließen, und den Recovery-Pfad. Das ist der visuelle Anker für die Verteidigung. Wenn du eine Designentscheidung verbal benennst, sollte das Diagramm sie zeigen.
Das Diagramm muss nicht in einem bestimmten Tool erstellt werden. Es sollte auf einem geteilten Bildschirm lesbar und korrekt sein. Wenn das Diagramm drei Spezialisten zeigt, die Canvas aber zwei hat, wird diese Diskrepanz die erste Frage sein.
Du hast in Sprint 2 ein Multi-Agent-Designdiagramm erstellt. Das Diagramm, das du präsentierst, sollte die implementierte Architektur widerspiegeln, nicht den Sprint-2-Entwurf. Aktualisiere es jetzt, falls sich die Canvas während der Integrationsarbeit in Sprint 4 weiterentwickelt hat.
### Komponente 3: Die Verteidigung
Ein mündlicher Bericht über die Designentscheidungen, die du getroffen hast. Die Verteidigung deckt drei Bereiche ab, entsprechend den drei Sprint-Abgaben:
- Architektur (Sprint-1-Briefing): Warum hast du diesen Archetyp gewählt? Was war die verworfene Alternative, und warum wurde sie verworfen? Unter welchen Bedingungen würdest du die Entscheidung neu bewerten?
- Multi-Agent-Design (Sprint-2-Diagramm): Wie sind die Verantwortlichkeiten zwischen Agenten aufgeteilt? Welchen Koordinationsansatz hast du verwendet, und warum? Was passiert, wenn ein Agent scheitert?
- Memory und State (Sprint-3-Spezifikation): Was ist geteilt und was ist privat? Was darf niemals persistieren und warum? Wie recovered das System nach einer Unterbrechung?
Die Verteidigung ist ein Bericht darüber, warum die Entscheidungen in diesen Abgaben basierend auf der spezifischen Domäne und dem Geschäftsproblem, das du gewählt hast, getroffen wurden — keine allgemeinen Prinzipien über Multi-Agent-Systeme.
### Wie die 5–7 Minuten strukturiert sind
Nutze diese Struktur als Orientierung.
- Minuten 0–1 — Kontext und Canvas. Benenne deine Domäne und dein Geschäftsproblem in einem Satz. Benenne deinen Archetyp in einem Satz. Führe dann die erste Anfrage live aus — den häufigsten Pfad und lass den Execution Trace laufen. Während er läuft, narrativ kurz: welcher Agent klassifiziert, zu welchem Spezialisten geroutet wird, was in Flow State geschrieben wird. Die Kontext- und Archetyp-Sätze sollten fünfzehn Sekunden dauern; der Rest ist die Live-Demonstration.
- Minuten 1–2 — Architektur und Designentscheidungen. Gehe das Systemdiagramm durch. Decke die drei Verteidigungsbereiche der Reihe nach ab — Architekturwahl, Multi-Agent-Design, Memory und State. Nenne für jeden Bereich die Entscheidung und den Grund dafür. Ein oder zwei Sätze pro Entscheidung reichen. Lies die Sprint-Abgaben nicht laut vor; nutze sie als Vorbereitungsmaterial, nicht als Skript.
- Minuten 2–4 — Testnachweis. Nenne zwei oder drei Erkenntnisse aus dem Testnachweis: eine, die bestätigt hat, dass eine Designentscheidung wie erwartet funktioniert, und eine, die eine Lücke sichtbar gemacht und eine Änderung erfordert hat. Sei spezifisch — nenne den Test, was er sichtbar gemacht hat, was du geändert hast. Der Testnachweis ist das, was eine implementierte Architektur von einer beschriebenen unterscheidet.
- Minuten 4–5 — Zweite Anfrage oder Recovery-Demonstration (falls Zeit bleibt). Wenn Zeit bleibt, führe die Grenzbedingungsanfrage aus — diejenige, die den Recovery-Pfad oder eine Scope-Grenze auslöst. Das ist für ein technisch interessiertes Publikum der überzeugendste Teil der Demonstration.
- Minuten 5–7 — Fragen. Instructor und Peers werden Fragen stellen. Die häufigsten: „Warum dieser Archetyp statt [der Alternative, die du verworfen hast]?" — antworte, indem du eine spezifische Eigenschaft deines Geschäftsproblems benennst, die der gewählte Archetyp besser behandelt. „Was passiert, wenn [spezifischer Agent] scheitert?" — antworte, indem du den Recovery-Pfad im Diagramm durchgehst. „Was enthält [spezifischer Flow-State-Schlüssel] an diesem Punkt der Ausführung?" — antworte aus deiner Sprint-3-Spezifikation. „Hat einer deiner Tests ein Ergebnis erzeugt, das du nicht erwartet hast?" — antworte ehrlich aus dem Testnachweis. Ein Test, der eine Lücke sichtbar gemacht hat, ist Evidenz für Gründlichkeit, keine Schwäche.
Du musst nicht auf jede Frage eine perfekte Antwort haben. Du musst dein eigenes Design gut genug kennen, um in Echtzeit darüber nachzudenken — genau darauf haben dich die Sprint-Abgaben vorbereitet.
Fokussiere dich auf Reasoning und Kommunikation. Die Präsentation ist kein Code-Walkthrough. Öffne Flowise nicht, um durch jeden Node zu klicken. Lies deinen System-Prompt nicht laut vor. Zeige keine JSON-Schemas. Zeige das Denken hinter der Architektur. Welche Entscheidungen du getroffen hast, warum du sie getroffen hast, was du anders machen würdest.
Vermeide Line-by-Line-Walkthroughs. Eine Präsentation, die das Publikum durch jeden Node deiner Canvas führt, ist der häufigste Fehlermodus. Das Publikum muss deine Nodes nicht kennen; es muss deine Entscheidungen kennen. Wenn du dich sagen hörst: „und dann macht dieser Node X, und dann macht dieser Node Y", machst du eine Code-Tour. Tritt einen Schritt zurück: Was war der Zweck dieses Abschnitts, und welche Alternative hast du erwogen?
## 5. Qualitätsanforderungen / Bewertung
Deine Bewertung basiert auf der Präsentation, nicht auf den Artefakten isoliert. Die Artefakte werden abgegeben, damit der Reviewer überprüfen kann, was du sagst, und deine Canvas bei Bedarf ausführen kann, aber bewertet wird die Arbeit, zu erklären, was du gebaut hast und warum.
Die Bewertung deckt vier Dimensionen ab:
[TABLE]
  | Dimension | Worauf der Evaluator achtet |
  | Architekturkohärenz | Passen die vier Sprint-Entscheidungen als einheitliches Design zusammen, oder wirken sie wie unabhängige Übungen, die nie miteinander abgeglichen wurden? |
  | Entscheidungsbegründung | Ist jede wichtige Entscheidung in einer spezifischen Eigenschaft des Geschäftsproblems und der Domäne verankert, oder werden Gründe auf Ebene allgemeiner Prinzipien genannt („Multi-Agent ist skalierbarer")? |
  | Implementierungsevidenz | Passt die Canvas zu den Designdokumenten? Zeigt der Testnachweis, dass die Canvas tatsächlich ausgeführt und nicht nur beschrieben wurde? |
  | Fehlerbehandlung | Kann der Lernende beschreiben, was das System tut, wenn etwas schiefgeht — ein Spezialagent scheitert, ein Classifier erzeugt fehlerhaften Output, ein State-Schlüssel enthält einen veralteten Wert? |
Es gibt keine einzige richtige Architektur. Die Bewertung prüft nicht, ob du den Router statt des Coordinator oder Evaluator gewählt hast. Sie prüft, ob die Architektur, die du gewählt hast, angesichts des Geschäftsproblems, das du in Sprint 1 beschrieben hast, kohärent, implementiert und verteidigbar ist.
> Visuelle Politur allein reicht nicht aus — Klarheit im Denken zählt mehr.
Eine Präsentation mit groben Slides und präzisem Reasoning schlägt eine Präsentation mit schönen Slides und vagem Reasoning. Der Reviewer hört darauf, was du verstehst, nicht darauf, was du zeigst.
## 6. Vorbereitungsliste
Erledige diese Punkte vor der Live Session. Lass keinen Punkt für die Session selbst übrig.
- [ ] Finale Canvas als JSON exportiert und bestätigt, dass sie in einer frischen Flowise-Instanz ladbar ist
- [ ] Systemdiagramm aktualisiert, sodass es die implementierte Architektur widerspiegelt — Rollen, State Flow, Recovery-Pfad
- [ ] Zwei Anfragen vorbereitet: eine für den häufigsten Pfad, eine für eine Grenzbedingung oder einen Recovery-Pfad
- [ ] Alle vier Sprint-Abgaben überprüft (Architekturbriefing, Multi-Agent-Designdiagramm + Begründung, Memory- und State-Spezifikation, Testnachweis), sodass die zentralen Entscheidungen im Kopf sind, nicht nur in Dokumenten
- [ ] Testnachweis überprüft und mindestens ein bestätigendes Ergebnis und ein lückenaufdeckendes Ergebnis bereit, das du nennen kannst
- [ ] Antwort auf die wahrscheinlichste schwierige Frage vorbereitet: „Warum dieser Archetyp statt der Alternative, die du verworfen hast?"
- [ ] Schriftliche Zusammenfassung entworfen (1–2 Seiten) und als PDF exportiert
- [ ] Präsentationstiming mindestens einmal geübt (gehe die 5–7-Minuten-Struktur einmal vollständig durch, damit Kontextsatz, Demo und Verteidigung in die Zeit passen)
## 7. Abgabe- / Lieferanweisungen
Die Abgabe dient Zugriff und Review. Die Bewertung findet während der Präsentation statt. Das sind zwei getrennte Schritte.
### Was abgegeben werden muss
Bündle alles in einem einzigen Abgabepaket (einem geteilten Google-Drive-Ordner):
1. Flowise-Canvas — als JSON exportiert oder ein Link zur Canvas in deiner Flowise-Instanz (falls geteilt, stelle sicher, dass der Link zugänglich ist).
1. Architekturentscheidungsbriefing — .md oder .pdf.
1. Multi-Agent-Designdiagramm — die Diagrammdatei (Bild, PDF oder Export aus einem Zeichentool) plus die schriftliche Designbegründung als .md oder .pdf.
1. Memory- und State-Architekturspezifikation — .md oder .pdf, alle vier Abschnitte enthalten.
1. Testnachweis — .md oder .pdf, erwartetes und tatsächliches Verhalten pro Test.
1. Schriftliche Zusammenfassung — PDF, 1–2 Seiten.
### Wo und wann
Der Abgabelink und die Anweisungen dazu befinden sich in der nächsten Lektion in Codio. Gib deine Arbeit als Link zu einem Google-Drive-Ordner ab. Lege alle Artefakte hinein und teile den Link in der Abgabelektion.
> ⚠️ Wichtig: Stelle sicher, dass die Berechtigungen für den Google-Drive-Ordner so gesetzt sind, dass alle Personen mit dem Link auf deine Dateien zugreifen können. Teste den Link in einem Inkognito-Fenster, bevor du ihn abgibst.

### Was nicht Teil der Bewertung ist
- Teilnahme an der Code Clinic. Nicht bewertet.
- Die Anzahl der Artefakte, die du über die gelisteten hinaus produzierst.
- Die visuelle Politur deiner Slides. Klare Gedanken zählen mehr als schöne Slides. Das bedeutet nicht, dass sie lieblos zusammengestellt sein sollten — du brauchst trotzdem ansprechende Slides.
## Finaler Check
Lies vor deiner Präsentation dein Systemdiagramm durch und stelle dir diese Fragen. Es sind die Fragen, die der Instructor während deiner Verteidigung stellen wird.
- Zeigt das Diagramm, was passiert, wenn ein Spezialagent scheitert, nicht nur, wenn er erfolgreich ist?
- Kannst du eine spezifische Anfrage vom Eingang bis zur Antwort im Diagramm nachverfolgen und dabei den Flow-State-Schlüssel benennen, der die Routing-Entscheidung trägt, und den Schlüssel, der die Antwort trägt?
- Wenn sich das Geschäftsproblem, das du in Sprint 1 beschrieben hast, ändern würde, welcher Teil der Architektur müsste sich zuerst ändern? Kannst du ihn im Diagramm benennen?
- Enthält der Testnachweis mindestens ein Ergebnis, das du vor dem Test nicht vorhergesagt hast?
Wenn eine dieser Fragen Unsicherheit auslöst, ist das nützliche Information. Nutze die Zeit vor der Präsentation, um sie durchzuarbeiten.
## Zusammenfassung
Das Modulprojekt bewegt sich von einer Reihe von Designdokumenten und einer Canvas zu etwas, hinter dem du stehen und das du erklären kannst. Die Artefakte wurden bereits über vier Sprints hinweg erstellt. Fokussiere deine Arbeit auf Vorbereitung, nicht auf Neuschaffung: die Entscheidungen überprüfen, die Struktur üben und sicherstellen, dass das Diagramm korrekt widerspiegelt, was gebaut wurde.
Die Verteidigung ist kein Test, ob der Agent funktioniert. Sie ist ein Test, ob du verstehst, warum er so entworfen wurde, wie er entworfen wurde, und ob das Design standhält, wenn jemand die Fragen stellt, die ein echtes Architekturreview stellen würde. Die Sprint-Abgaben sind die Evidenz dafür.