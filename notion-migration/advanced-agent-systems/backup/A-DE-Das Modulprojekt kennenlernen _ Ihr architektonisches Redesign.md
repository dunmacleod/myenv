# Das Modulprojekt kennenlernen — Ihr architektonisches Redesign

Notion page: https://app.notion.com/p/Das-Modulprojekt-kennenlernen-Ihr-architektonisches-Redesign-3dd9418319f3810eb10cffd345833e17
Backed up before n8n migration

Sprint 1 hat die Bausteine eingeführt: Agenten-Architekturen, Trade-offs zwischen Single-Agent und Multi-Agent, das Vier-Fragen-Framework zur Entscheidung zwischen ihnen und eine Baseline-Agentflow-V2-Canvas mit drei Nodes als neutraler Ausgangspunkt.
Am Ende dieses Moduls ist diese Baseline verschwunden. Sie haben sie in etwas umgestaltet, das zu einem Business-Problem passt, das Sie gewählt haben — mit einer Architektur, die Sie verteidigen können, Memory-Grenzen, die Sie bewusst gezogen haben, und einer Canvas, die läuft. Diese Lektion ist der erste Blick darauf, wie das ganze Redesign aussieht, wenn es zusammengesetzt ist.
> 💭 Heute ist nichts fällig. Diese Lektion ist ein früher Blick auf das Modulprojekt, damit Sie wissen, worauf Sie zusteuern. Sprints 2 und 3 fügen die Bausteine hinzu; in Sprint 4 integrieren, präsentieren und reichen Sie ein. Wenn ein Abschnitt hier sich anfühlt wie „Das kann ich noch nicht", ist das erwartbar — Sie sollen es auch noch nicht können.
## Das Projekt, das Sie formen werden
Anders als bei einem festen Running Case wird das Projekt dieses Moduls auf einem Business-Problem gebaut, das Sie selbst wählen. Es kann ein interner Support-Agent für eine Firma sein, in der Sie gearbeitet haben, ein Recherche-Assistent für eine Domäne, die Sie kennen, ein Ops-seitiges Triage-System, eine Fach-Beraterin — die Form zählt weniger als die Konkretheit. Ein vages Briefing produziert ein vages Redesign; ein enges, reales Briefing produziert ein verteidigbares.
Ihre Aufgabe über das Modul hinweg ist es, die Baseline-Agentflow-V2-Canvas in eine Architektur zu verwandeln, die zu diesem Briefing passt. Kein Neubau von Grund auf — ein bewusstes Redesign, verteidigbar gegenüber den Alternativen, die Sie verworfen haben.
## Was Sie am Ende des Moduls einreichen
Vier Abgaben, die aufeinander aufbauen, plus die Integration auf der Canvas, die daraus etwas Lauffähiges macht:
- Architekturentscheidungs-Briefing — eine Seite: die Entscheidung, das Pattern, Inputs und Outputs, die drei Säulen, die verworfene Alternative und die Bedingungen, unter denen Sie die Entscheidung neu bewerten würden
- Multi-Agent-Designdiagramm — jeder Agent benannt, Informationsfluss gezeigt, Routing-Entscheidungspunkte markiert, Informationsgrenzen hervorgehoben, mindestens ein Fallback-Pfad
- Memory- und State-Architektur-Spezifikation — Memory-Grenzenkarte (geteilt/privat/bedingt mit Persistenz-Scope), was nicht persistieren darf, State-Recovery-Design, Fehlerisolations-Bewertung
- Die neu entworfene Flowise-Canvas — die das Design implementiert, mit einem Test-Protokoll, das zeigt, dass sie sich so verhält, wie die Spezifikation es beschreibt
## Der Bogen, Sprint für Sprint
Sprint 1 — Grundlagen der Agenten-Architektur. Diesen haben Sie gerade beendet. Sie kennen die Patterns, die Trade-offs und wie Sie eine Architektur-Entscheidung verteidigbar treffen. Ihre erste Abgabe — das Entscheidungs-Briefing — entsteht aus der Arbeit dieses Sprints.
Sprint 2 — Multi-Agent-System-Design. Sie lernen, wann Multi-Agent seine Komplexität wert ist, wie Sie Spezialisierungen und Grenzen definieren und wie Sie ein Design-Diagramm zeichnen, das ein Leser tatsächlich verstehen kann. Ihre zweite Abgabe bekommt hier Form.
Sprint 3 — Memory- und State-Architektur. Sie ziehen Memory- und State-Grenzen bewusst — was ist geteilt, was ist privat, was darf niemals persistieren — und entwerfen Fehlerisolation, damit der Fehler eines Agenten den geteilten State nicht korrumpiert. Ihre dritte Abgabe bekommt hier Form.
Sprint 4 — Projekt-Integration. Sie implementieren das Design auf Ihrer Flowise-Canvas, testen es gegen die Fehlermodi, für die Sie designt haben, und präsentieren und reichen dann ein.
## Presentation Day und Code Clinic
Die letzte Woche des Moduls hat zwei Live-Sessions, in dieser Reihenfolge.
Presentation Day ist der Termin, an dem Ihr Projekt bewertet wird. Sie reichen die vier Abgaben im Voraus ein und präsentieren dann das Redesign live — die Entscheidung, das Diagramm, die Memory-Grenzen, die Canvas, die end-to-end läuft. Sie verteidigen das Pattern gegen die Alternative, die Sie verworfen haben. Ihre Note für das Modulprojekt ergibt sich aus dem, was Sie einreichen, und daraus, wie Sie präsentieren.
Code Clinic findet nach dem Presentation Day statt. Sie zählt nicht in die Note — es ist eine technische Support-Session für konkrete Fragen zu Ihrem eigenen Bau. Eine Routing-Entscheidung, die nicht dort landet, wo Sie sie erwartet haben, eine Memory-Grenze, die auf eine Weise leckt, für die Sie nicht designt haben, ein Fehlerisolations-Pfad, der nicht sauber wieder herstellt. Bringen Sie die Canvas und konkrete Probleme mit, keine allgemeinen Fragen.
Das genaue Format, die Agenda und die Einreichungs-Checkliste kommen später im Modul im Detail zurück — Sie müssen heute nichts auswendig lernen.
## Zusammenfassung
Die Baseline-Canvas aus Sprint 1 wird zur neu entworfenen Architektur, die Sie am Ende des Moduls präsentieren — bewusst gewählt, diagrammatisch gezeichnet, in Memory begrenzt und lauffähig. Sprint 2 bringt Ihnen das Design, Sprint 3 bringt Ihnen die Memory- und State-Grenzen, in Sprint 4 präsentieren Sie am Presentation Day, mit einer Code Clinic danach für tiefere technische Unterstützung.