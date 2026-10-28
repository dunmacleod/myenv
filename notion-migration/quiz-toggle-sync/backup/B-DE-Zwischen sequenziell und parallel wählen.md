# Zwischen sequenziell und parallel wählen

Notion page: https://app.notion.com/p/Zwischen-sequenziell-und-parallel-w-hlen-f6d9418319f3823097af011c3c5c1d3a
Backed up before n8n migration

## Zweck der Lektion
Die Wahl des richtigen Orchestrierungsmusters ist eine der wichtigsten Designentscheidungen in einem Multi-Agent-System. In dieser Lektion lernst du, wann Agenten nacheinander arbeiten sollten (sequenzielle Orchestrierung) und wann sie gleichzeitig arbeiten sollten (parallele Orchestrierung).
## Lernergebnisse
Am Ende dieser Lektion kannst du:
- Situationen identifizieren, in denen sequenzielle Orchestrierung die bessere Wahl ist.
- Situationen identifizieren, in denen parallele Orchestrierung die bessere Wahl ist.
- die Abwägungen zwischen Geschwindigkeit, Abhängigkeit und Koordination erklären.
- ein Orchestrierungsmuster für typische Business-Szenarien auswählen.
## Einführung
Sequenzielle und parallele Orchestrierung lösen unterschiedliche Probleme. Ein häufiger Fehler ist, ein Muster nach technischer Vorliebe auszuwählen. Richtig ist es, sich an den Anforderungen der Aufgabe zu orientieren.
Die zentrale Frage ist einfach:
> Kann die nächste Aufgabe beginnen, bevor die vorherige Aufgabe abgeschlossen ist?
Wenn die Antwort nein ist, nutze sequenzielle Orchestrierung.
Wenn die Antwort ja ist, kann parallele Orchestrierung die bessere Wahl sein.
## Zwei unterschiedliche Arten, Arbeit zu organisieren
### Sequenzielle Orchestrierung
In einem sequenziellen Workflow hängt jeder Agent vom Output des vorherigen ab. Arbeit bewegt sich Schritt für Schritt durch das System.
![image]((notion-hosted file))
Der Recommendation Agent kann erst starten, wenn die Risikobewertung abgeschlossen ist. Jeder Schritt baut auf dem vorherigen Schritt auf.
### Parallele Orchestrierung
In einem parallelen Workflow erhalten mehrere Agenten denselben Input und arbeiten gleichzeitig unabhängig voneinander.
Beispiel:
![image]((notion-hosted file))
Jeder Spezialagent arbeitet gleichzeitig. Die Ergebnisse werden zusammengeführt, sobald alle Agenten fertig sind.
## Wie du entscheidest
Eine nützliche Regel ist, nach Abhängigkeiten zu suchen.
Nutze sequenzielle Orchestrierung, wenn:
- ein Agent Informationen benötigt, die ein anderer Agent erzeugt hat.
- der Workflow einem klaren Entscheidungspfad folgt.
- spätere Schritte von früherer Validierung abhängen.
- Genauigkeit wichtiger ist als Geschwindigkeit.
Nutze parallele Orchestrierung, wenn:
- Agenten unabhängig arbeiten können.
- mehrere Perspektiven benötigt werden.
- Geschwindigkeit wichtig ist.
- Ergebnisse später kombiniert werden können.
## Die Trade-offs vergleichen
[TABLE]
  | Faktor | Sequenziell | Parallel |
  | Geschwindigkeit | Langsamer | Schneller |
  | Koordinationskomplexität | Geringer | Höher |
  | Umgang mit Abhängigkeiten | Ausgezeichnet | Begrenzt |
  | Ressourcennutzung | Geringer | Höher |
  | Am besten geeignet für | Abhängige Aufgaben | Unabhängige Aufgaben |
>  Beachte, dass parallele Orchestrierung nicht automatisch besser ist, nur weil sie schneller ist. Wenn Agenten von den Outputs der anderen abhängen, kann parallele Ausführung unvollständige oder falsche Ergebnisse erzeugen.
## Quiz
### Frage 1
>  Ein Cascadia-Kunde reicht ein Ticket ein und schreibt:
  > „Meine Zahlung wurde doppelt abgebucht und meine Bestellung ist nie angekommen.“
  Welches Orchestrierungsmuster würdest du für die Untersuchung wählen?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/92e89a05-f839-4743-a1e4-f03f19e35f68
## Beispiel aus der Praxis
Betrachte ein E-Commerce-Unternehmen, das Produktretouren bearbeitet.
Ein sequenzielles Design könnte so funktionieren:
![image]((notion-hosted file))
Jeder Schritt hängt vom vorherigen Ergebnis ab.
Ein paralleles Design könnte so funktionieren:
![image]((notion-hosted file))
## Zusammenfassung
Bei der Entscheidung zwischen sequenzieller und paralleler Orchestrierung zählen vor allem die Abhängigkeiten. Sequenzielle Orchestrierung funktioniert am besten, wenn jeder Schritt Informationen aus dem vorherigen Schritt benötigt. Parallele Orchestrierung funktioniert am besten, wenn mehrere Agenten unterschiedliche Aspekte eines Problems unabhängig untersuchen können.
Die effektivsten Multi-Agent-Systeme kombinieren oft beide Ansätze: Parallele Zweige bearbeiten unabhängige Arbeit, während sequenzielle Phasen Entscheidungen koordinieren und das finale Ergebnis zusammensetzen. Diese Fähigkeit, das Orchestrierungsmuster auf das Business-Problem abzustimmen, ist ein zentraler Teil beim Design zuverlässiger Agentensysteme.