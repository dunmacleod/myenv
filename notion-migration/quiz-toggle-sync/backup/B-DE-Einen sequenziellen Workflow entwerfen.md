# Einen sequenziellen Workflow entwerfen

Notion page: https://app.notion.com/p/Einen-sequenziellen-Workflow-entwerfen-cd69418319f382a79f5f811d07e40f1d
Backed up before n8n migration

Bei Cascadia laufen die meisten Supportanfragen durch eine vorhersehbare Reihe von Schritten: Nachricht klassifizieren, Bestellung nachschlagen, Garantie prüfen, Antwort entwerfen. Jeder Schritt hängt vom vorherigen ab. Sofia weiß: Dafür braucht sie keine Agenten, die spontan miteinander sprechen. Sie braucht einen sequenziellen Workflow. Ein Schritt wird abgeschlossen, dann beginnt der nächste und nutzt den Output des vorherigen Schritts.
Sequenzielle Orchestrierung (auch Chaining genannt) ist das einfachste Orchestrierungsmuster und der natürliche Ausgangspunkt, wenn Aufgaben klare Abhängigkeiten haben. Diese Lektion zeigt, wie sequenzielle Workflows funktionieren, wann sie passen und wo sie an Grenzen stoßen.
In n8n entsteht ein sequenzieller Workflow durch Nodes, die in Ausführungsreihenfolge verbunden sind. Jeder Node erhält Daten vom vorherigen Schritt; spätere Nodes können über Expressions auf frühere Outputs zugreifen. 
## Die Kernidee
Sequenzielle Orchestrierung folgt einer einfachen Regel:
> Ein Schritt wird abgeschlossen, bevor der nächste Schritt beginnt.
Jeder Agent erhält Informationen, führt seine Aufgabe aus und gibt das Ergebnis weiter.
Stell es dir wie einen Staffellauf vor.
Der erste Läufer beendet seinen Abschnitt und übergibt den Staffelstab an den zweiten Läufer. Der zweite Läufer kann erst starten, wenn er den Staffelstab erhalten hat.
Dasselbe Prinzip gilt für Agenten.
![image]((notion-hosted file))
## Beispiel: Eine Kundenanfrage bearbeiten
Stell dir vor, ein Unternehmen erhält ein Customer-Support-Ticket.
Der Workflow könnte so aussehen:
1. Request Analyzer identifiziert die Art der Anfrage.
1. Priority Agent bestimmt die Dringlichkeit.
1. Response Agent entwirft eine Antwort.
1. Review Agent prüft die Qualität.
1. Final Response wird an den Kunden zurückgegeben.
Jeder Schritt benötigt Informationen aus dem vorherigen Schritt.
Der Response Agent kann keine Antwort erstellen, bevor die Anfrage analysiert wurde.
Der Review Agent kann keine Antwort prüfen, die noch nicht existiert.
![image]((notion-hosted file))
## Wie Informationen fließen
Ein Grund, warum sequenzielle Workflows beliebt sind, ist, dass der Informationsfluss leicht nachzuvollziehen ist.
Jeder Schritt erhält:
- die ursprüngliche Anfrage
- vorherige Outputs
- geteilten Workflow-State
Dann fügt er neue Informationen hinzu, bevor er alles weitergibt.
In n8n stehen Outputs früherer Nodes als Ausführungsdaten zur Verfügung. Mit Set (Edit Fields) lassen sich benannte Felder ablegen; Expressions lesen Werte aus vorherigen Schritten. Agenten teilen nicht automatisch ein gemeinsames Memory-Objekt. Prüfe die Ein- und Ausgaben jedes Nodes unter Executions.
Beispiel für State Evolution
[TABLE]
  | Schritt | State |
  | User Request | „My order hasn't arrived." |
  | After Analyzer | + Category = Shipping Issue |
  | After Priority Agent | + Priority = High |
  | After Response Agent | + Draft Response |
  | After Review Agent | + Approved Response |
## Warum sequenzielle Orchestrierung beliebt ist
Sequenzielle Workflows bieten mehrere Vorteile.
### Vorhersehbarkeit
Der Ausführungspfad ist im Voraus bekannt.
Du weißt immer, welcher Schritt als Nächstes läuft.
### Einfacheres Debugging
Wenn etwas schiefgeht, kannst du jede Phase einzeln untersuchen.
Das macht Troubleshooting deutlich einfacher als in stark dynamischen Systemen.
### Schrittweise Verfeinerung
Jeder Agent konzentriert sich auf eine einzelne Verantwortung.
Statt das gesamte Problem auf einmal zu lösen, verbessert das System das Ergebnis Schritt für Schritt.
![image]((notion-hosted file))
## Wann sequenzielle Orchestrierung am besten funktioniert
Sequenzielle Orchestrierung ist am effektivsten, wenn Aufgaben klare Abhängigkeiten haben.
Gute Beispiele sind:
- Customer-Support-Workflows
- Document-Review-Pipelines
- Datenextraktion gefolgt von Validierung
- Content Generation gefolgt von Qualitätsprüfungen
- mehrstufige Freigabeprozesse
Ein nützlicher Test ist:
> „Kann der nächste Schritt beginnen, bevor der vorherige Schritt abgeschlossen ist?"
Wenn die Antwort nein ist, ist ein sequenzieller Workflow wahrscheinlich passend.
## Einschränkungen
Sequenzielle Workflows sind einfach, aber sie sind nicht immer die schnellste Option.
Da jeder Schritt wartet, bis der vorherige abgeschlossen ist:
- steigt die Ausführungszeit, wenn mehr Schritte hinzugefügt werden.
- kann ein Fehler früh in der Chain den gesamten Workflow blockieren.
- können unabhängige Aufgaben nicht gleichzeitig verarbeitet werden.
Diese Einschränkungen sind der Grund, warum fortgeschrittenere Orchestrierungsmuster existieren, aber sequenzielle Workflows bleiben die Grundlage vieler Produktionssysteme.
## Verständnischeck
### Frage 1
>  Ein Legal-Document-Review-Workflow bei Cascadia hat diese Schritte:
  1. Text aus einem PDF-Vertrag extrahieren.
  1. Klauseln identifizieren.
  1. Klauseln gegen Unternehmensrichtlinien prüfen.
  1. Einen Compliance-Bericht generieren.
  Warum ist sequenzielle Orchestrierung hier passend?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/28c8a718-1fac-4d90-bd28-d36eb2a8e86f
## Zusammenfassung
Sequenzielle Orchestrierung ist das natürliche Muster, wenn Aufgaben klare Abhängigkeiten haben. Sie ist vorhersehbar, leicht zu debuggen und lässt sich einfach Schritt für Schritt erweitern. Dafür ist sie auch am langsamsten, wenn sich Schritte eigentlich parallelisieren ließen. In der nächsten Lektion schauen wir uns hierarchische Orchestrierung an. Dabei sitzt ein Coordinator über den Spezialisten.