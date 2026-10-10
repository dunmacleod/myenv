# Das Modulprojekt kennenlernen — Ihr erweitertes, vernetztes Agenten-System

Notion page: https://app.notion.com/p/Das-Modulprojekt-kennenlernen-Ihr-erweitertes-vernetztes-Agenten-System-3dd9418319f381118981cf556801a9c2
Backed up before n8n migration

Sprint 1 hat eingeführt, wie Agenten sprechen — miteinander und mit Tools. Strukturierte Nachrichtenweitergabe, Handoff-Verträge, MCP als Agent-zu-Tool-Integration und A2A-Awareness für Cross-Agent-Interoperabilität.
Am Ende dieses Moduls haben Sie einen Baseline-Projekt-Agenten genommen und ihn in ein vernetztes, resilientes, orchestriertes System erweitert, das mit Fehlern umgeht, ohne umzukippen. Diese Lektion ist der erste Blick darauf, was „erweitert" tatsächlich bedeutet und wie die Teile zusammenpassen.
> 💭 Heute ist nichts fällig. Diese Lektion ist ein früher Blick auf das Modulprojekt, damit Sie wissen, worauf Sie zusteuern. Sprints 2 und 3 fügen die Bausteine hinzu; in Sprint 4 integrieren, präsentieren und reichen Sie ein. Wenn ein Abschnitt hier sich anfühlt wie „Das kann ich noch nicht", ist das erwartbar — Sie sollen es auch noch nicht können.
## Das Projekt, das Sie erweitern werden
Sie starten von einem Baseline-Projekt-Agenten — einem Single-Agent-Workflow, der ein MCP-verbundenes Tool nutzt, um eine Sache gut zu tun. Das ist der Kern. Über das Modul hinweg erweitern Sie ihn zu einem Multi-Agent-System, in dem spezialisierte Agenten ihren Teil der Anfrage besitzen, sauber übergeben, externe Tools über MCP aufrufen und sich von Timeouts und Tool-Fehlern erholen, ohne den geteilten State zu korrumpieren.
Die Business-Domäne, der das erweiterte System dient, wählen Sie — ein Support-Agent für eine reale Firma, ein Recherche-Assistent, ein Triage-System, eine Fach-Beraterin. Gleiches Prinzip wie im ersten Modul: Ein enges, reales Briefing produziert ein verteidigbares System; ein vages nicht.
## Was Sie am Ende des Moduls einreichen
Vier Abgaben, die aufeinander aufbauen, plus die erweiterte Canvas, die daraus etwas Lauffähiges macht:
- Sprint-1-Abgabe — das Design für strukturierte Kommunikation und Handoff für Ihr Projekt (Message-Passing-Verträge, MCP-Integration für ein Tool, Awareness der A2A-Ebene)
- Sprint-2-Abgabe — das Orchestrierungsdesign für Ihren Projekt-Agenten (sequenzielle oder parallele Muster, Routing-Entscheidungen, wann der Orchestrator übergibt vs. selbst entscheidet)
- Sprint-3-Abgabe — die Resilienz-Ebene, angewendet auf Ihr Projekt (Timeouts, Retries, Fallback-Orchestrierung, Circuit-Breaker-artige Behandlung auf Design-Ebene)
- Sprint-4-Abgabe — die vernetzte, erweiterte Canvas end-to-end: Intake-Agent, spezialisierte Agenten, Orchestrierung, MCP-Tools, Retry- und Fallback-Logik, bewertet gegen die Fehlermodi, für die Sie designt haben
## Der Bogen, Sprint für Sprint
Sprint 1 — Kommunikations- und Integrationsprotokolle. Diesen haben Sie gerade beendet. Sie wissen, wie strukturierte Nachrichten zwischen Agenten reisen, wie MCP Agenten mit Tools verbindet und wo A2A einfügt. Ihre erste Abgabe entsteht aus der Arbeit dieses Sprints.
Sprint 2 — Orchestrierungsmuster. Sie lernen, wann Orchestrierung ihre Komplexität wert ist, den Unterschied zwischen Orchestrierung und Choreografie und wie sequenzielle vs. parallele Muster verändern, was bricht und wie. Ihre zweite Abgabe bekommt hier Form.
Sprint 3 — Resilienz und Fehlerbehandlung. Sie ergänzen Timeouts, Retries, Fallback-Orchestrierung und Circuit Breaker auf Design-Ebene. Sie lernen zu diagnostizieren, warum Orchestrierungen scheitern, ohne warten zu müssen, bis sie in der Produktion scheitern. Ihre dritte Abgabe bekommt hier Form.
Sprint 4 — Projekt-Integration. Sie verbinden alle Agenten in Ihrem Projekt, führen end-to-end Fehleranalyse durch, debuggen über die Protokoll- und Orchestrierungsschichten hinweg, evaluieren den erweiterten Agenten und präsentieren und reichen dann ein.
## Presentation Day und Code Clinic
Die letzte Woche des Moduls hat zwei Live-Sessions, in dieser Reihenfolge.
Presentation Day ist der Termin, an dem Ihr Projekt bewertet wird. Sie reichen die vier Abgaben im Voraus ein und präsentieren dann live — die Architektur, das Orchestrierungsmuster, die Resilienz-Entscheidungen, die Canvas, die end-to-end auf realistischen Nutzeranfragen läuft. Sie verteidigen das Muster gegen die Alternative, die Sie verworfen haben. Ihre Note für das Modulprojekt ergibt sich aus dem, was Sie einreichen, und daraus, wie Sie präsentieren.
Code Clinic findet nach dem Presentation Day statt. Sie zählt nicht in die Note — es ist eine technische Support-Session für konkrete Fragen zu Ihrem eigenen Bau. Ein Orchestrierungspfad, der nicht dort routet, wo Sie ihn erwartet hätten, eine Retry-Schleife, die niemals aufgibt, ein Handoff-Vertrag, der immer wieder Kontext verliert. Bringen Sie die Canvas und konkrete Probleme mit, keine allgemeinen Fragen.
Das genaue Format, die Agenda und die Einreichungs-Checkliste kommen später im Modul im Detail zurück — Sie müssen heute nichts auswendig lernen.
## Zusammenfassung
Der Baseline-Single-Agent-Workflow wird zu einem erweiterten, vernetzten, orchestrierten System, das Sie am Ende des Moduls präsentieren. Sprint 2 gibt Ihnen das Orchestrierungsdesign, Sprint 3 gibt Ihnen die Resilienz-Ebene, Sprint 4 integriert alles und endet mit dem Presentation Day für die Bewertung und einer Code Clinic danach für Support.