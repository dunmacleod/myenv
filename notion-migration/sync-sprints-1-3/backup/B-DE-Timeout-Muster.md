# Timeout-Muster

Notion page: https://app.notion.com/p/Timeout-Muster-2e19418319f38365b5f1015ca1e3434b
Backed up before n8n migration

Eine Woche nach Cascadias Soft Launch bringt Emil Sofia eine klare Beschwerde von Lena: Manche Kundennachrichten bleiben einfach hängen. Keine Fehlermeldung, keine Benachrichtigung. Der Workflow startet, ein Agent macht sich auf, um etwas nachzuschlagen, und danach kommt nichts mehr zurück. Sofia öffnet die Logs und sieht jedes Mal dasselbe Bild: Eine Komponente wartet auf eine andere. Die andere antwortet nie. Der ganze Workflow bleibt genau an diesem Punkt stecken.
Genau dafür gibt es Timeouts. Sie sind die Grenze, die orchestrierte Systeme gegen endloses Warten ziehen. Du siehst gleich, warum Wartezeiten entstehen, warum unbegrenztes Warten gefährlich wird und wie ein Timeout den ganzen Workflow schützt, sobald eine Komponente langsamer wird.
## Was ein Timeout bedeutet
Unter einem Timeout versteht man das maximale Zeitfenster, das einer Systemkomponente für das Warten auf die Antwort einer anderen Komponente eingeräumt wird.
Stell dir einen Flowise-Agenten vor, der hinter einem Cloud-Proxy geschaltet ist. Geht eine Anfrage ein, reicht der Proxy diese an Flowise weiter, woraufhin die Antwortgenerierung startet. Wenn der Proxy nun ein Timeout von 30 Sekunden besitzt, kappt er nach Ablauf dieser Frist die Verbindung.
Das heißt nicht zwangsläufig, dass Flowise abgestürzt ist. Es bedeutet lediglich, dass die Antwort nicht rechtzeitig fertig wurde. Solche Fehler treten auf, wenn Proxy, Backend, Agent und Frontend asynchron laufen und keine einheitliche Zeiterwartung definiert ist.
## Warum Timeouts in Agenten-Workflows wichtig sind
Agenten-Workflows können länger dauern als normale Webanfragen, weil sie mehrere Schritte umfassen können.
Ein Agent muss vielleicht die Anfrage klassifizieren, ein Tool aufrufen, auf ein externes System warten, Kontext abrufen, eine Antwort generieren oder Arbeit an einen anderen Agenten übergeben. Jeder Schritt fügt Zeit hinzu.
In einer einfachen App können 30 Sekunden ausreichen. In einem Agenten-Workflow können 30 Sekunden zu kurz sein, besonders wenn der Workflow lange Modellantworten, Tool-Aufrufe, Retrieval oder Multi-Agent-Handoffs enthält.
Dadurch entsteht ein häufiges Resilienzproblem:
Der Workflow leistet noch sinnvolle Arbeit, aber die Infrastruktur gibt zu früh auf.
## Häufige Ursachen für Timeouts
Timeouts passieren häufig, weil:
- ein Agent eine große Aufgabe verarbeitet.
- ein Tool oder eine API langsam antwortet.
- ein Service vorübergehend nicht verfügbar ist.
- eine Nachricht verloren geht und nie ihr Ziel erreicht.
Der Timeout selbst ist nicht die Ursache. Er ist ein Signal dafür, dass etwas länger gedauert hat als erwartet.
### Was passiert nach einem Timeout?
Verschiedene Systeme behandeln Timeouts unterschiedlich.
Ein Workflow könnte:
- die Aufgabe erneut versuchen.
- die Aufgabe an einen anderen Agenten senden.
- eine Fallback-Antwort verwenden.
- an einen Menschen eskalieren.
- den Workflow stoppen und einen Fehler melden.
Die richtige Wahl hängt von der Business-Situation ab. Ein Customer-Support-Chatbot könnte einen Retry versuchen.
Ein Fraud-Detection-Workflow könnte sofort eskalieren.
### Beispiel
Ein Orchestrator sendet eine Aufgabe an einen Agenten.
Erwartetes Verhalten
![image]((notion-hosted file))
Timeout-Verhalten

![image]((notion-hosted file))
> ☝ Der wichtige Punkt ist: Der Agent muss nicht zwingend gescheitert sein. Der Orchestrator hat einfach die maximale Wartezeit erreicht.
## Zusammenfassung
Timeouts sind einer der häufigsten Fehlerpunkte in orchestrierten Systemen. Sie passieren, wenn ein Teil des Systems aufhört zu warten, bevor ein anderer Teil seine Arbeit abgeschlossen hat.
Gutes Timeout-Handling bedeutet nicht nur, eine Zahl zu erhöhen. Es bedeutet zu verstehen, wie lange der Workflow realistischerweise dauern sollte, wo der Timeout erzwungen wird und was passieren soll, wenn Arbeit länger dauert als erwartet.