# Das Modulprojekt kennenlernen — Meridian Consulting

Notion page: https://app.notion.com/p/Das-Modulprojekt-kennenlernen-Meridian-Consulting-3dd9418319f381cebd28c590be93e8ab
Backed up before n8n migration

Sprint 1 war Sie und Flowise. Lokal installieren, die Gemini- und OpenRouter-Credentials aufsetzen, Ihre erste Agentflow-v2-Canvas bauen, lernen, was ein Start Node → Agent Node → Direct Reply Node tatsächlich tut, wenn Sie ihm eine Nachricht schicken.
Am Ende dieses Moduls betreibt dieselbe Plattform einen internen Agenten für eine reale Beratungsfirma. Diese Lektion ist der erste Blick darauf, wer sie sind und was der Agent können muss.
> 💭 Heute ist nichts fällig. Diese Lektion ist ein früher Blick auf das Modulprojekt, damit Sie wissen, worauf Sie zusteuern. Sprints 2 und 3 fügen die Bausteine hinzu; in Sprint 4 verfeinern, präsentieren und reichen Sie ein. Wenn ein Abschnitt hier sich anfühlt wie „Das kann ich noch nicht", ist das erwartbar — Sie sollen es auch noch nicht können.
## Das Unternehmen, für das Sie bauen werden
Meridian Consulting ist eine mittelgroße Professional-Services-Firma. Beraterinnen und Berater verbringen jede Woche einen erheblichen Teil damit, interne Handbücher, Policy-Dokumente und Live-Engagement-Daten zu durchforsten, um ihre eigenen prozessualen Fragen zu beantworten — „Wie ist unsere Sub-Contracting-Policy für Public-Sector-Arbeit?", „In welcher Phase ist das Kessler-Engagement gerade?", „Wer zeichnet Scope-Änderungen über 50.000 € ab?".
Die Firma möchte einen internen Support-Agenten, der aus Meridians eigenem Material antwortet, statt aus den Trainingsdaten des Modells, den Live-Status von Engagements auf Anfrage abruft, vor folgenreichen Aktionen auf menschliche Freigabe wartet und innerhalb des Scope bleibt, den Meridian für ihn festgelegt hat. Sie werden diesen Agenten auf einer einzigen Canvas bauen — dem Meridian Base Agent — und ihn Sprint für Sprint um Fähigkeiten erweitern.
## Was Sie am Ende des Moduls einreichen
Die Canvas, die Sie verfeinern und einreichen, ist dieselbe, die Sie bereits bauen. Bewertet wird, ob sie sich so verhält, wie Sie es beschreiben, und ob Sie das Design erklären können. Die finale Abgabe umfasst:
- Die verfeinerte Meridian-Base-Agent-Canvas — aus Flowise exportiert
- Den finalen System-Prompt — Rolle, Scope, harte Grenzen, Eskalationsverhalten, Capability-Routing
- Den Meridian Document Store — mit dem Quellmaterial befüllt, Retrieval verifiziert
- Test-Nachweise — end-to-end Durchläufe über getrennte Sessions zu Grounding, Tool-Nutzung, Prompt-Injection-Versuchen und kontrolliertem Ausfallverhalten
- Ein kurzes schriftliches Briefing — warum diese Canvas gegenüber den Alternativen gewählt wurde, gemessen an Kriterien, die für ein Business tatsächlich zählen
## Der Bogen, Sprint für Sprint
Sprint 1 — Flowise und den Gemini-Stack aufsetzen. Diesen haben Sie gerade beendet. Flowise läuft lokal, die API-Keys funktionieren und Sie haben einen ersten Agentflow, der spricht.
Sprint 2 — Memory, Retrieval und Tools in Flowise. Sie bauen den Document Store, verbinden ihn mit dem Agenten, ergänzen bedingtes Routing zwischen Capabilities und binden einen HTTP Node für Live-Datenabfragen an.
Sprint 3 — Debugging von Agenten und die Plattform-Landschaft. Sie ergänzen Human-Approval-Checkpoints, Iterations- und Retry-Logik, Custom-Logic-Nodes und Sub-Flows. Sie lernen, einen Agent-Graphen zu lesen und zu debuggen. Sie bekommen ein Gespür dafür, wann Flowise das richtige Tool ist und wann nicht.
Sprint 4 — Projekt-Finalisierung und -Vergleich. Sie härten die Canvas end-to-end, verfeinern den System-Prompt ein letztes Mal, führen Vergleichsnachweise gegen Alternativen und präsentieren und reichen dann ein.
## Presentation Day und Code Clinic
Die letzte Woche des Moduls hat zwei Live-Sessions, in dieser Reihenfolge.
Presentation Day ist der Termin, an dem Ihr Projekt bewertet wird. Sie reichen das Canvas-Paket im Voraus ein und führen dann eine Live-Demo aus — inklusive mindestens einer Konversation, die Grounding belastet, einer, die ein Tool aufruft, einer, die das Freigabe-Gate auslöst, und einer, die versucht, den Agenten aus dem Scope zu drängen. Sie verteidigen die Plattformwahl gegen eine benannte Alternative. Ihre Note für das Modulprojekt ergibt sich aus dem, was Sie einreichen, und daraus, wie Sie präsentieren.
Code Clinic findet nach dem Presentation Day statt. Sie zählt nicht in die Note — es ist eine technische Support-Session für konkrete Fragen zu Ihrem eigenen Bau. Ein Retrieval, das nicht so rankt, wie Sie es erwarten würden, ein Condition Agent Node, der immer wieder falsch routet, ein Human Input Node, der nicht dort pausiert, wo Sie es wollen. Bringen Sie die Canvas und konkrete Probleme mit, keine allgemeinen Fragen.
Das genaue Format, die Agenda und die Einreichungs-Checkliste kommen später im Modul im Detail zurück — Sie müssen heute nichts auswendig lernen.
## Zusammenfassung
Der Meridian Base Agent, den Sie in Sprint 1 begonnen haben, ist dieselbe Canvas, die Sie am Ende des Moduls präsentieren — in einem Document Store geerdet, zwischen spezialisierten Capabilities routend, durch menschliche Freigabe abgesichert und gegen Alternativen verteidigbar. Sprint 2 ergänzt Wissen und Tools, Sprint 3 ergänzt Aufsicht und Debug-Kompetenz, in Sprint 4 präsentieren Sie am Presentation Day, mit einer Code Clinic danach für tiefere technische Unterstützung.