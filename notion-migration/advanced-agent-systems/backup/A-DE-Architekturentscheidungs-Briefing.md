# Architekturentscheidungs-Briefing

Notion page: https://app.notion.com/p/Architekturentscheidungs-Briefing-18c9418319f38366aec601430bbfecee
Backed up before n8n migration

Sprint 1 hat das Framework für Architekturentscheidungen behandelt: wann ein Single-Agent sinnvoll ist und wann mehrere Agenten, welches der sechs Muster zu einem gegebenen Problem passt, warum Orchestrierung, Kommunikation und Zustandsverwaltung jeweils bewusstes Design brauchen, und wie die häufigsten Fehler aussehen, bevor sie überhaupt auf einer Canvas landen.
Diese Aufgabe verlangt von dir, dieses Framework auf ein Unternehmen anzuwenden, das du noch nicht kennst. Du denkst ein reales operatives Problem durch, triffst eine begründbare Architekturentscheidung und schreibst sie so klar auf, dass eine Kollegin oder ein Kollege danach handeln könnte. Gebaut wird hier nichts.
Das Ergebnis ist ein einseitiges Architektur-Entscheidungsbriefing.
### Das Szenario: Karmen Freight
Karmen Freight ist ein Logistikmakler mit Sitz in Wien. Das Unternehmen koordiniert grenzüberschreitende Straßentransporte für Hersteller- und Handelskunden in Österreich, Ungarn und Tschechien. Karmen besitzt selbst keine Lkw, sondern vermittelt Kunden an geprüfte Frachtführer, verwaltet die Dokumentation für die Zollabfertigung und verfolgt Sendungen vom Start- bis zum Zielort.
Das zwölfköpfige Operations-Team übernimmt die gesamte Kundenkommunikation, die Koordination mit Frachtführern und die Compliance-Arbeit. An einem durchschnittlichen Tag gehen rund 80 interne Anfragen ein, größtenteils von Account Managern, die den Status laufender Sendungen prüfen, vom Compliance-Desk, das Zollverfahren nachschlägt, und von Carrier-Koordinatoren, die Kontaktdaten oder Ratenvereinbarungen bestätigen. Diese Anfragen werden derzeit manuell bearbeitet, was täglich etwa zwei Stunden Arbeitszeit von erfahrenen Operations-Mitarbeitenden kostet.
Miriam, die Leiterin des Operations-Teams, möchte einen internen Agenten bauen, der diese Anfragen übernimmt. Sie hat den Scope wie folgt beschrieben:
- Sendungsstatus-Anfragen: „Wo befindet sich Sendung KF-2847?" Der häufigste Anfragetyp, rund 55 % des täglichen Volumens. Die Beantwortung erfordert einen Abgleich mit der Shipment-Tracking-API. Ist die API nicht erreichbar, soll der Agent das klar benennen und dem Account Manager vorschlagen, den Frachtführer direkt zu kontaktieren.
- Zollverfahrens-Anfragen: „Welche Dokumente braucht eine Pharma-Sendung für den Grenzübertritt von Österreich nach Ungarn?" Rund 30 % des täglichen Volumens. Antworten stützen sich auf dokumentiertes Wissen zu Zollverfahren. Diese Antworten ändern sich selten, müssen aber korrekt sein.
- Frachtführer-Kontaktanfragen: „Wie lautet die Kontakt-E-Mail von TransCargo Kft?" Rund 15 % des täglichen Volumens. Antworten stammen aus dem Frachtführer-Verzeichnis. Diese Antworten sind stabil und rein faktisch.
Miriam hat außerdem zwei Randbedingungen genannt:
1. Das Team ist klein. Niemand im Operations-Team hat die Kapazität, ein komplexes Multi-Agent-System zu pflegen. Was auch immer gebaut wird, muss auch für jemanden ohne technischen Hintergrund verständlich und anpassbar sein.
1. Der Agent darf niemals einen Sendungsstatus oder eine Zollanforderung erfinden. Wenn er etwas nicht weiß, muss er das sagen und die Nutzerin oder den Nutzer an die richtige Quelle verweisen.
### Deine Aufgabe
> 🔥 Mach dir zuerst eine Kopie von dieser Vorlage. Sie spiegelt die sechs Abschnitte des Briefings: Entscheidung, Muster, Ein- und Ausgaben, Die drei Pfeiler, Verworfene Alternative und Bedingungen für eine Neubewertung. Füll jeden Abschnitt direkt in der Vorlage aus.

Erstelle ein einseitiges Architektur-Entscheidungsbriefing für Karmen Freights internen Anfrage-Agenten.
Das Briefing muss alle sechs Abschnitte unten abdecken. Halt es auf eine Seite begrenzt.
#### Abschnitt 1: Entscheidung: Single-Agent oder Multi-Agent
Nenn deine Entscheidung klar. Begründe sie dann anhand des Vier-Fragen-Frameworks:
- Kann ein gut abgegrenzter Agent die gesamte Bandbreite an Eingaben zuverlässig bewältigen?
- Brauchen die verschiedenen Anfragetypen Tools oder Wissen, das sich gegenseitig widerspricht?
- Muss ein Fehler bei einem Anfragetyp von den anderen isoliert werden?
- Rechtfertigt der Zuverlässigkeitsgewinn eines Multi-Agent-Designs den Koordinationsaufwand?
Nenn, welche Fragen für die Entscheidung ausschlaggebend waren und welche in diesem Fall keine Rolle gespielt haben.
#### Abschnitt 2: Muster
Benenn das Architekturmuster, das am besten passt, aus den sechs: Single Agent, Tool-Using Agent, Workflow + Agent, Router, Evaluator, Supervisor-Worker. Wenn zwei plausibel sind, nenn beide und sag, für welches du dich entschieden hast und warum.
#### Abschnitt 3: Ein- und Ausgaben
Definiere:
- Was der Agent erhält (Eingabetypen, Quelle, Sprache falls relevant)
- Was der Agent erzeugt (Ausgabeformat, was eine Weiterleitung auslöst gegenüber einer direkten Antwort)
- Was der Agent explizit nicht tut (die bewussten Ausschlüsse)
#### Abschnitt 4: Die drei Pfeiler
Nenn für jeden der drei Architekturpfeiler die zentrale Designentscheidung und das Hauptrisiko, wenn diese Entscheidung nicht bewusst getroffen wird:
- Orchestrierung: Was steuert, wann welcher Teil des Flows läuft?
- Kommunikation: Wie bewegen sich Daten zwischen den Komponenten, die du entworfen hast?
- Zustandsverwaltung: Was bleibt erhalten, was wird zurückgesetzt, und was darf niemals gespeichert werden?
#### Abschnitt 5: Bewusste Ausschlüsse und die verworfene Alternative
Beschreib den Architekturansatz, den du in Betracht gezogen, aber verworfen hast, und erklär warum. Hast du dich für Single-Agent entschieden, beschreib, wie ein Multi-Agent-Design ausgesehen hätte und warum es für Karmen Freight in diesem Stadium nicht die richtige Wahl ist. Hast du dich für Multi-Agent entschieden, beschreib die Single-Agent-Alternative und woran sie scheitert.
Dieser Abschnitt ist Pflicht. Eine Entscheidung ist nur dann begründbar, wenn die Alternative durchdacht wurde.
#### Abschnitt 6: Bedingungen für eine Neubewertung der Entscheidung
Nenn zwei oder drei konkrete, beobachtbare Veränderungen in Karmen Freights Situation, die dich dazu bringen würden, die Architekturentscheidung zu überdenken. Diese sollten präzise formuliert sein, etwa: „wenn das Anfragevolumen 200 pro Tag übersteigt und Latenz als Problem gemeldet wird" oder „wenn sich Zollanforderungen wöchentlich ändern und statisches Wissen nicht mehr ausreicht".
### Bevor du schreibst
Lies das Karmen-Freight-Szenario ein zweites Mal. Achte dabei auf Folgendes:
- Wie ähnlich oder unterschiedlich sich die drei Anfragetypen sind. Reicht ein System-Prompt für alle drei, oder brauchen sie eine spürbar unterschiedliche Behandlung?
- Was die API-Abhängigkeit bei Sendungsstatus-Anfragen für die Architektur bedeutet. Konkret: Ist der Fehlerfall (API nicht erreichbar) ein Kommunikationsproblem, ein Orchestrierungsproblem oder ein Problem der Zustandsverwaltung?
- Was Miriams erste Randbedingung (kleines Team, geringer Wartungsaufwand) ausschließt und was nicht
- Ob die Bedingung „darf niemals etwas erfinden" eine Architekturanforderung oder eine System-Prompt-Anforderung ist, und was dieser Unterschied für das Design bedeutet
Diese Fragen solltest du im Kopf behalten, während du die Entscheidungen für das Briefing triffst.
## Hinweise
  Nutze diese nur, wenn du bei einem bestimmten Abschnitt nicht weiterweißt.
  Zur Single- vs. Multi-Agent-Entscheidung: Fang bei Miriams erster Randbedingung an. Ein Multi-Agent-System braucht mehr Wartung als ein Single-Agent-System. Die Randbedingung schließt Multi-Agent nicht aus, sie legt die Messlatte für die Begründung nur höher. Frag dich, ob der Zuverlässigkeitsgewinn groß genug ist, um diese Messlatte zu reißen.
  Zum Muster: Die drei Anfragetypen haben jeweils eine andere Antwortquelle (API, dokumentiertes Wissen, Frachtführer-Verzeichnis). Das klingt nach Router. Frag dich aber, ob die Routing-Entscheidung tatsächlich am Eingangspunkt passieren muss, oder ob ein gut abgegrenzter Single-Agent mit klarem System-Prompt die Klassifizierung intern übernimmt, ganz ohne dedizierten Routing-Node.
  Zum API-Fehlerfall: Eine API, die manchmal nicht erreichbar ist, ist ein Kommunikations-Designproblem. Konkret: ein fragiler Handoff, der nur auf seinen Auftritt wartet. Das Briefing sollte klären, was der Agent tut, wenn die vorgelagerte Datenquelle nicht verfügbar ist, nicht nur, was er tut, wenn sie verfügbar ist.
  Zur verworfenen Alternative: Ein starkes Briefing würdigt die verworfene Alternative ernsthaft, erkennt ihre echten Stärken an und erklärt dann, warum genau dieser Kontext den gewählten Ansatz zur besseren Wahl macht. Ein Briefing, das nur sagt „Multi-Agent wäre komplexer", ist schwächer als eines, das sagt: „Multi-Agent würde Isolation zwischen den Anfragetypen bringen, aber die drei Typen teilen sich genug Kontext, dass der Routing-Overhead ein größeres Fehlerrisiko birgt als der Isolationsgewinn wert ist."
## Checkpoints
Bevor du dein Briefing abgibst, prüf es anhand dieser Fragen:
- [ ] Nennt Abschnitt 1 die konkreten Fragen, die ausschlaggebend waren, und nicht nur das Ergebnis?
- [ ] Benennt Abschnitt 2 das Muster präzise, statt es nur allgemein zu beschreiben?
- [ ] Enthält Abschnitt 3 die bewussten Ausschlüsse, also nicht nur, was der Agent tut, sondern auch, was er nicht tut?
- [ ] Deckt Abschnitt 4 alle drei Pfeiler ab, nicht nur die Orchestrierung?
- [ ] Enthält Abschnitt 5 eine echte Beschreibung der verworfenen Alternative, statt sie nur abzutun?
- [ ] Nennt Abschnitt 6 konkrete, beobachtbare Bedingungen statt vager Scope-Aussagen?
- [ ] Passt das Briefing auf eine Seite? Falls nicht: Was lässt sich streichen, ohne eine Entscheidung zu verlieren?
Zeigt ein Checkpoint eine Lücke auf, überarbeite den entsprechenden Abschnitt, bevor du das Briefing als fertig betrachtest.
### In deinem Projekt
Das Briefing-Format, das du im Walkthrough geübt hast, ist dasselbe Format, das du in der nächsten Live-Session verteidigst. Vergleich vor dieser Session, was du für Karmen Freight geschrieben hast, mit den Architekturentscheidungen auf deiner eigenen Projekt-Canvas. Die Fragen aus Abschnitt 5 (die verworfene Alternative) und Abschnitt 6 (Bedingungen für eine Neubewertung) sind für den eigenen Agenten oft am schwersten zu beantworten und lohnen sich, schon vor der Live-Session durchdacht zu werden.
### Letzte Prüfung
Bevor du das Briefing abschließt, lies es noch einmal mit dieser Frage im Kopf: Würde eine neue Kollegin oder ein neuer Kollege, dem Miriam dieses Briefing in die Hand drückt, wissen, was zu bauen ist, was wegzulassen ist und wann sie zurückkommen und fragen sollten, ob sich die Architektur ändern muss?
Wenn die Antwort ja ist, ist das Briefing fertig.
Denk kurz über diese Fragen nach:
1. Welcher der sechs Abschnitte war am schwersten zu schreiben, und woran lag das?
1. Gab es einen Moment, in dem das Szenario dich in eine Architekturrichtung gedrängt hat und das Framework in eine andere? Wie hast du das aufgelöst?
1. Gibt es etwas im Karmen-Freight-Szenario, das das Briefing nicht abdeckt, aber sollte?
Das sind die Fragen, die sich ein guter Architekt oder eine gute Architektin nach einer Entscheidung stellt.
### Zusammenfassung
Mit dem Karmen-Freight-Briefing wendest du zum ersten Mal das gesamte Framework aus Sprint 1 auf ein Unternehmen an, das du vorher nicht kanntest. Das Szenario wurde bewusst so gewählt, dass es Vela Systems ähnlich genug ist, um wiedererkennbar zu sein (ein Operations-Team, interne Anfragen, begrenzte Wartungskapazität), aber unterschiedlich genug, um echtes Nachdenken statt reines Pattern-Matching zu verlangen.
Ein einseitiges Briefing, das alle sechs Abschnitte abdeckt, die verworfene Alternative benennt und beobachtbare Bedingungen für eine Neubewertung festlegt, ist das Ergebnis eines bewussten Architekturprozesses. Genau darauf hat Sprint 1 hingearbeitet.
Sprint 2 führt die Entscheidung einen Schritt weiter: von „soll das Single-Agent oder Multi-Agent sein?" zu „wenn mehr als ein Agent nötig ist, wie arbeiten diese Agenten zusammen?"
