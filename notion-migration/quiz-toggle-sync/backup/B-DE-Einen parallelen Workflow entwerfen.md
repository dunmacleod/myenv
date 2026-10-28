# Einen parallelen Workflow entwerfen

Notion page: https://app.notion.com/p/Einen-parallelen-Workflow-entwerfen-d419418319f382cdbe8981c14a229494
Backed up before n8n migration

## Zweck der Lektion
Diese Lektion zeigt dir, wie parallele Orchestrierung funktioniert: Mehrere Agenten handeln dabei gleichzeitig. Du lernst, wann sich paralleles Design eignet und wie sich Arbeit sicher aufteilen lässt. Außerdem lernst du, wie du Ergebnisse kombinierst, ohne Verwirrung zu erzeugen.
## Lernergebnisse
Am Ende dieser Lektion kannst du:
- erklären, was einen Workflow parallel statt sequenziell macht.
- Aufgaben identifizieren, die sicher gleichzeitig laufen können.
- beschreiben, wie Outputs paralleler Agenten zu einem zuverlässigen Ergebnis zusammengeführt werden sollten.
## Einführung
Du hast bereits gesehen: Orchestrierungsmuster beschreiben, wie Agenten koordiniert werden. In dieser Lektion schauen wir uns ein Muster genauer an: parallele Orchestrierung. Parallele Workflows sind nützlich, wenn mehrere Agenten gleichzeitig an getrennten Teilen einer Aufgabe arbeiten können.
## Parallele Orchestrierung auf den Punkt gebracht
Ein paralleler Workflow sendet dieselbe Anfrage oder unterschiedliche Teile einer Anfrage gleichzeitig an mehrere Agenten und kombiniert ihre Outputs anschließend zu einem finalen Ergebnis.
In einem sequenziellen Workflow hängt jeder Schritt vom vorherigen Schritt ab. Agent B wartet auf Agent A. Agent C wartet auf Agent B. Das ist nützlich, wenn die Aufgabe eine klare Abhängigkeitskette hat.
In einem parallelen Workflow warten die Agenten während ihrer Hauptarbeit nicht aufeinander. Jeder Agent erhält seine Aufgabe, erledigt sie unabhängig und gibt ein Ergebnis zurück. Ein finaler Koordinationsschritt vergleicht, kombiniert oder priorisiert diese Ergebnisse dann.
Stell dir zum Beispiel vor, ein Kunde fragt:
> „We are thinking about automating our reporting process. What should we consider?“
Ein paralleler Workflow könnte diese Anfrage gleichzeitig an drei Agenten senden. Ein Agent prüft den Business Value, ein anderer die Data Readiness, und ein weiterer die Implementierungsrisiken. Keiner dieser Agenten muss auf die anderen warten, bevor er startet. Nachdem sie geantwortet haben, kombiniert ein finaler Agent ihre Perspektiven zu einer ausgewogenen Antwort.
![image]((notion-hosted file))
## Warum parallele Workflows nützlich sind
Parallele Orchestrierung ist nützlich, wenn eine Aufgabe mehrere unabhängige Blickwinkel hat. Du weist unterschiedlichen Agenten unterschiedliche Verantwortlichkeiten zu.
Das kann die Geschwindigkeit verbessern, weil mehrere Agenten gleichzeitig arbeiten. Es kann auch die Qualität verbessern, weil jeder Agent sich auf eine bestimmte Denkweise konzentriert. Ein Risk Agent kann nach Schwachstellen suchen, ein Business Agent kann sich auf den Nutzen konzentrieren, und ein Technical Agent kann die Machbarkeit prüfen.
Das Schlüsselwort ist unabhängig. Parallele Orchestrierung funktioniert am besten, wenn jeder Agent für sich sinnvolle Arbeit leisten kann. Er braucht dafür nicht zuerst den Output eines anderen Agenten.
## Eine einfache Struktur für parallele Workflows
Ein paralleler Workflow hat normalerweise vier Teile.
Erstens gibt es einen Input. Das ist die ursprüngliche Anfrage, das Problem oder das Dokument, das verarbeitet werden muss.
Zweitens gibt es einen Splitter. Der Splitter entscheidet, welche Agenten welchen Teil der Arbeit erhalten. Manchmal erhält jeder Agent denselben vollständigen Input. Manchmal erhält jeder Agent eine spezifische Teilaufgabe.
Drittens gibt es parallele Agenten. Diese Agenten arbeiten gleichzeitig, jeder mit einer klar definierten Rolle.
Viertens gibt es einen Merge-Schritt. Dieser Schritt führt die Outputs zusammen. Der Merge-Schritt kann zusammenfassen, vergleichen, einstufen, Konflikte auflösen oder eine finale Antwort erstellen.
Der Merge-Schritt ist das, was parallele Orchestrierung zuverlässig macht. Ohne ihn hast du nur mehrere getrennte Antworten.
## Beispiel: Paralleler Workflow für eine Business-Automation-Anfrage
Stell dir vor, der User fragt:
> „Can we use an AI agent to reduce manual work in our monthly reporting process?“
Ein paralleler Workflow könnte so entworfen werden.
Der Business Value Agent prüft, ob die Automatisierung ein echtes Problem löst. Er sucht nach Zeitersparnis, wiederholter manueller Arbeit und möglichem Business Impact.
Der Data Readiness Agent prüft, ob die benötigten Daten verfügbar, strukturiert und zuverlässig genug für Automatisierung sind.
Der Risk Agent prüft, was schiefgehen könnte. Er berücksichtigt Halluzinationsrisiko, fehlende Freigaben, unklare Zuständigkeiten und sensible Daten.
Der Final Response Agent erhält alle drei Outputs und erstellt eine Empfehlung. Er entscheidet, was am wichtigsten ist, und erzeugt eine klare Schlussfolgerung.
## Was sollte parallel laufen?
Eine gute parallele Aufgabe hat drei Eigenschaften.
Die Agenten können unabhängig arbeiten. Ein Agent benötigt das Ergebnis eines anderen Agenten nicht, bevor er starten kann.
Die Outputs ergänzen sich. Jeder Agent fügt eine andere Perspektive hinzu.
Die Ergebnisse können zusammengeführt werden. Es gibt eine klare Möglichkeit, die Outputs zu einer finalen Entscheidung, Zusammenfassung oder Empfehlung zu kombinieren.
Wenn diese drei Eigenschaften fehlen, kann parallele Orchestrierung mehr Verwirrung als Nutzen erzeugen.
## Was sollte nicht parallel laufen?
Nutze parallele Orchestrierung nicht, wenn die Aufgabe starke Abhängigkeiten hat.
Nimm zum Beispiel einen Agenten, der zuerst Kundenanforderungen extrahiert. Ein zweiter Agent baut anschließend auf Basis dieser Anforderungen eine Lösung. Das ist kein guter paralleler Workflow. Der zweite Agent benötigt den Output des ersten Agenten. Das ist sequenzielle Orchestrierung.
Die parallele Orchestrierung birgt zudem Risiken, wenn Agenten überschneidende Entscheidungen treffen können und klare Merge-Regeln fehlen. Wenn beispielsweise drei Agenten zu unterschiedlichen Endergebnissen kommen und niemand den Widerspruch auflöst, wird der gesamte Workflow unzuverlässig.
## Der Merge-Schritt
Der Merge-Schritt ist die wichtigste Designentscheidung in einem parallelen Workflow.
Ein schwacher Merge-Schritt sagt:
>  “Kombiniere die Outputs.”
Ein stärkerer Merge-Schritt sagt:
>  “Vergleiche die Outputs der Business-, Data- und Risk-Agenten. Erzeuge eine Empfehlung. Wenn die Agenten nicht übereinstimmen, erkläre die Uneinigkeit und wähle die sicherste Empfehlung.”
Der Merge-Schritt sollte definieren, was bei Übereinstimmung, Uneinigkeit, fehlenden Informationen und doppelten Informationen passieren soll. Hier wird der Workflow zu mehr als nur mehreren Agenten, die gleichzeitig laufen.
## Quiz
>  
  ### Frage 1
  Ein Lernender entwirft einen Workflow für diese Anfrage:
  > „Review this product idea and tell me whether it is worth building.“
  Welches Design passt am besten zu paralleler Orchestrierung?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e67cf65d-1aa7-4647-993c-9e2ba87fc99f
## Häufiger Designfehler
Ein häufiger Fehler ist anzunehmen, dass „mehr Agenten" automatisch „besserer Workflow" bedeutet.
Das Ziel paralleler Orchestrierung ist eine sinnvolle Arbeitsteilung. Generieren zwei Agenten voraussichtlich dieselbe Antwort, sollten sie nicht beide im Workflow aktiv sein. Lassen sich ihre Ergebnisse zudem nicht eindeutig zusammenführen, leidet die Wartbarkeit des gesamten Systems.
Ein optimaler Workflow funktioniert wie ein gutes Team: Jeder kennt seine Rolle, arbeitet unabhängig und trägt zum Gesamterfolg bei.
## Zusammenfassung
Parallele Orchestrierung ist nützlich, wenn sich eine Aufgabe in unabhängige Teile aufteilen lässt. Jeder Teil profitiert dann von einer eigenen Perspektive. Die zentrale Designherausforderung besteht darin, die Outputs mehrerer gleichzeitig laufender Agenten zuverlässig zusammenzuführen.
Du hast jetzt ein praktisches mentales Modell fürs Design paralleler Workflows: Teile nur auf, wenn die Arbeit wirklich unabhängig ist. Gib jedem Agenten eine eigene Rolle. Und definiere den Merge-Schritt, bevor du den Workflow ausführst.
