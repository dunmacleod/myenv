# Orchestrierung vs. Choreografie

Notion page: https://app.notion.com/p/Orchestrierung-vs-Choreografie-0999418319f3835b9ae3017ff59f6487
Backed up before n8n migration

Cascadias Support-Flow hat jetzt mehrere Agenten: einen Intake Agent, der eingehende Nachrichten klassifiziert, einen Warranty Agent und einen Returns Agent. Sofia muss jetzt entscheiden, wie diese miteinander sprechen.
Sie hat zwei grundverschiedene Optionen vor sich. In der einen sitzt ein Coordinator über den Spezialisten und entscheidet, wer was macht. In der anderen sprechen die Spezialisten direkt miteinander, ganz ohne Coordinator in der Mitte.
Es gibt zwei gängige Antworten darauf. Der eine Ansatz nutzt einen zentralen Coordinator, der steuert, wie die Arbeit durchs System läuft. Beim anderen interagieren die Agenten direkt und passen sich dynamisch an. Diese zwei Stile heißen Orchestrierung und Choreografie. Welchen Stil du wählst, bestimmt, wie sich der ganze Workflow später verhält.
## Orchestrierung: Ein Agent koordiniert die Arbeit
In einem orchestrierten System agiert ein zentraler Agent als Coordinator. Er erhält die Anfrage, entscheidet, welcher Agent welche Aufgabe übernimmt, sammelt die Ergebnisse ein und bestimmt den nächsten Schritt.
Denk an ein Orchester. Die Musiker spielen verschiedene Instrumente, aber der Dirigent entscheidet, wann welche Gruppe startet, stoppt oder das Tempo wechselt. Die Musiker konzentrieren sich auf ihren eigenen Part, der Dirigent steuert die gesamte Aufführung.
In einem Multi-Agent-System übernimmt der Orchestrator genau diese Rolle. Die einzelnen Agenten bleiben spezialisiert, aber ein zentraler Coordinator steuert den Workflow.
### Typischer Orchestrierungs-Flow
1. Ein Nutzer sendet eine Anfrage.
1. Der Orchestrator nimmt sie entgegen.
1. Der Orchestrator weist einem oder mehreren Agenten Arbeit zu.
1. Die Agenten liefern ihre Ergebnisse zurück.
1. Der Orchestrator kombiniert die Outputs und liefert die finale Antwort.
![image]((notion-hosted file))
## Choreografie: Agenten koordinieren sich direkt
In einem choreografierten Multi-Agent-System gibt es keinen zentralen Coordinator, der für die Steuerung des Workflows verantwortlich ist. Stattdessen versteht jeder Agent seine eigene Rolle und kommuniziert direkt mit anderen Agenten, wenn zusätzliche Informationen oder Fähigkeiten benötigt werden. Wenn eine Anfrage ins System eingeht, beginnt ein Agent mit der Verarbeitung und entscheidet, welche anderen Agenten beteiligt werden sollten. Diese Agenten tauschen Informationen miteinander aus, bringen ihre spezialisierte Expertise ein und arbeiten weiter zusammen, bis die Aufgabe abgeschlossen ist. Das finale Ergebnis entsteht aus der gemeinsamen Arbeit der Agenten, statt von einem zentralen Controller zusammengesetzt zu werden.
Dieser Ansatz kann sehr flexibel sein, weil Agenten dynamisch basierend auf den Anforderungen der Aufgabe interagieren können. Er vermeidet außerdem einen einzelnen Koordinations-Bottleneck, was die Skalierbarkeit in größeren Systemen verbessern kann. Da Entscheidungen und Kommunikation jedoch über mehrere Agenten verteilt sind, können choreografierte Systeme schwieriger zu überwachen, zu debuggen und zu verstehen sein als orchestrierte Systeme.
### Typischer Choreografie-Flow
1. Eine Nutzeranfrage geht ins System ein.
1. Ein Agent beginnt mit der Verarbeitung.
1. Dieser Agent kontaktiert bei Bedarf andere Agenten.
1. Agenten tauschen Informationen direkt aus.
1. Das finale Ergebnis entsteht aus ihrer Zusammenarbeit.
![image]((notion-hosted file))
## Vergleich der beiden Ansätze
### Orchestrierung
- Ein zentraler Coordinator
- Workflow wird explizit gesteuert
- Einfacher zu überwachen und zu debuggen
- Einfacher für vorhersehbare Prozesse
- Zentraler Kontrollpunkt
### Choreografie
- Kein zentraler Coordinator
- Workflow entsteht aus Interaktionen
- Flexibler und dezentraler
- Besser für dynamische Umgebungen
- Kein einzelner Fehlerpunkt
## Verständnischeck
### Frage 1
>  Ein Cascadia-Workflow hat drei Agenten:
  - Ein Research Agent sammelt Informationen.
  - Ein Compliance Agent prüft Vorschriften.
  - Ein Report Agent erstellt das finale Dokument.
  Ein vierter Agent erhält jede Anfrage, entscheidet, welcher der drei daran arbeiten soll, sammelt die Outputs und gibt die finale Antwort zurück. Welcher Koordinationsstil ist das?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/caae56e4-716c-45ea-817b-3b22a81492af
## Zusammenfassung
Orchestrierung und Choreografie lösen dasselbe Koordinationsproblem auf unterschiedliche Weise. Orchestrierung setzt einen Coordinator in die Mitte. Das macht das System vorhersehbarer und leichter zu debuggen, kostet aber einen zentralen Komplexitätspunkt. Choreografie lässt Agenten direkt miteinander interagieren. Das macht das System flexibler und robuster, kostet aber Sichtbarkeit darüber, wie es sich verhält. Für Cascadias Support-Flow startet Sofia in den nächsten Lektionen mit Orchestrierung. Das Pattern passt, wenn die Spezialisten von vornherein feststehen und du einem Coordinator zutraust, sie zu routen.