# Modulare Flows mit dem Execute Flow Node

Notion page: https://app.notion.com/p/Modulare-Flows-mit-dem-Execute-Flow-Node-3819418319f380249c4cda756926d5d1
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du verstehst, was der Execute Flow Node macht, warum modulares Flow-Design wichtig ist und wie du ihn richtig konfigurierst.
## Ausgangslage
Meridians Canvas ist über drei Sprints hinweg deutlich gewachsen. Der Meridian Base Agent übernimmt inzwischen Knowledge Retrieval, Intent Routing, Live-Datenabfragen, Retry-Logik, Iteration und menschliche Freigabe-Checkpoints, alles in einer einzigen Canvas.
Mit wachsender Komplexität der Agent-Workflows taucht ein neues Problem auf. Logik, die in einem Flow nützlich ist, wird oft auch in einem anderen gebraucht. Die gebaute Engagement-Briefing-Logik ist ein gutes Beispiel dafür. Sie funktioniert als eigenständiges wöchentliches Tool, aber auch als Fähigkeit, die der Base Agent bei Bedarf aufrufen können sollte. Dieselbe Logik in jedem Flow neu zu bauen, der sie braucht, ist auf Dauer nicht wartbar. Ändert sich die Briefing-Logik, muss jede Kopie aktualisiert werden. Wird ein Bug gefunden, muss er an mehreren Stellen behoben werden. Genau dieses Problem löst modulares Flow-Design.
## Was der Execute Flow Node macht
Der Execute Flow Node funktioniert als Sub-Workflow-Caller und fördert so modulares Design und Wiederverwendbarkeit von Logik. Er erlaubt es dem aktuellen Workflow, einen separaten, bereits bestehenden Workflow auszulösen. Dabei übergibt er ihm einen Start-Input, kann für den jeweiligen Lauf optional bestimmte Konfigurationen des Ziel-Flows überschreiben und holt sich am Ende dessen finalen Output zurück in den aufrufenden Workflow, um die Verarbeitung fortzusetzen.
![image]((notion-hosted file))
Praktisch bedeutet das: Ein Flow ruft einen anderen auf, wartet, bis dieser abgeschlossen ist, und verwendet seinen Output so, als wäre er lokal erzeugt worden. Der aufrufende Flow muss nicht wissen, wie der Sub-Flow intern funktioniert, sondern nur, welchen Input er erwartet und welchen Output er zurückgibt.
## Warum das für Meridian wichtig ist
Meridians Entwicklungsteam kann dieses Muster für Folgendes nutzen:
- Den Flow Meridian Engagement Briefing vom Base Agent aus aufrufen, ohne die Iterationslogik neu zu bauen
- Spezialisierte Sub-Flows für regionale Anfragen aus Deutschland, Polen und Tschechien bauen und je nach Routing den passenden aufrufen
- Komplexe Logik an einer zentralen Stelle bündeln und bei neuen Anforderungen nur einmal aktualisieren
Wird der Sub-Flow aktualisiert, profitiert der aufrufende Flow automatisch davon, ohne dass am Execute Flow Node irgendetwas geändert werden muss. Das ist der zentrale Wartungsvorteil von modularem Design.
## Den Execute Flow Node konfigurieren
[TABLE]
  | Field | Zweck |
  | Select Flow | Wähle den Ziel-Agentflow-v2 oder Chatflow aus der Dropdown-Liste aller Flows in deiner Flowise-Instanz |
  | Input | Die Daten, die als Start-Input an den Sub-Flow übergeben werden, entweder als reiner Text oder als Flow-State-Variable |
  | Base URL | Die URL der Flowise-Instanz, auf der der Ziel-Flow läuft. Bei Docker erforderlich, dort auf http://host.docker.internal:3000 setzen |
  | Return Response As | Ob der Output des Sub-Flows im aufrufenden Flow als User Message oder als Assistant Message behandelt wird |
  | Update Flow State | Optional: den Output des Sub-Flows in einem Flow-State-Key speichern, damit nachgelagerte Nodes ihn lesen können |
> 💡 Für Docker-Nutzer: Der Execute Flow Node kann nicht über localhost einen anderen Flow aufrufen, weil beide Flows im selben Docker-Container laufen. Setze die Base URL deshalb immer auf http://host.docker.internal:3000, wenn du Flowise lokal über Docker betreibst.

## Wie er sich in die Meridian-Canvas einfügt
Der Execute Flow Node sitzt auf einem eigenen Routing-Pfad. Der Condition Node erkennt Briefing-Anfragen anhand von Keywords und leitet sie an den Execute Flow Node weiter. Dieser ruft den Sub-Flow Meridian Engagement Briefing auf und gibt das Ergebnis an einen Direct Reply Node zurück.
Die bestehenden Knowledge- und Status-Pfade bleiben komplett unverändert. Der Execute Flow Node fügt einen dritten Pfad hinzu, ohne etwas an dem bereits Gebauten zu verändern.
## Bekannte Plattform-Einschränkung
In komplexen Canvases mit mehreren HTTP-Pfaden kann sich das Input-Feld des Execute Flow Node automatisch mit Variablenreferenzen aus anderen Pfaden füllen und beim Speichern wieder zurücksetzen. Das ist ein bekanntes Flowise-Verhalten bei bestimmten Canvas-Konfigurationen. Solltest du das auf deiner Canvas erleben, wird die vollständige Umsetzung in der Live-Session an einer sauberen Canvas gezeigt, auf der dieser Konflikt nicht auftritt. Die Konfigurationsschritte oben sind korrekt. Das Problem liegt an Canvases mit widersprüchlichen Node-ID-Bindungen, nicht am Execute Flow Node selbst.
## Verständnischeck
>  Ein Entwickler aktualisiert den Sub-Flow Meridian Engagement Briefing so, dass er statt drei nun fünf Engagement-Records enthält. Was muss dafür in der Canvas von Meridian Base Agent geändert werden?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/05540576-106f-4813-9f03-7a5c407ba00e


> 💡 Fazit:
  Der Execute Flow Node macht aus isolierten Agentflow-v2-Builds wiederverwendbare Bausteine. Einmal gebaute Logik lässt sich aus jedem anderen Flow aufrufen, ohne sie neu zu bauen. Ändert sich der Sub-Flow, profitiert automatisch jeder, der ihn aufruft. Je mehr Meridians Canvas wächst, desto wichtiger werden modulare Sub-Flows. Sie halten einzelne Komponenten fokussiert, unabhängig testbar und wartbar, ohne dass sich Änderungen kaskadenartig durch den gesamten Build ziehen.