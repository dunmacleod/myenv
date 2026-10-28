# Debugging über Protokoll- und Orchestrierungsschichten hinweg

Notion page: https://app.notion.com/p/Debugging-ber-Protokoll-und-Orchestrierungsschichten-hinweg-c419418319f382d5b4ea816698bec464
Backed up before n8n migration

Lade das Starter-Projekt hier herunter:
Projekt herunterladen: [LINK]
Dieses Projekt sollte dir sehr vertraut vorkommen. Es basiert auf dem Workflow, den du zuvor gebaut hast:
- Ein arXiv MCP Agent ruft Research Papers ab,
- Ein Parser prüft die Antwort,
- Der Workflow entscheidet, ob er wiederholen oder weitermachen soll.
- Erfolgreiche Antworten gehen zurück an den User.
Diese Version hat einen Bug. Den haben wir absichtlich eingebaut.
Die MCP-Integration läuft sauber. Die Retry-Logik gibt es auch. Trotzdem behandelt der Workflow irgendwo in der Orchestrierung jede erfolgreiche Anfrage wie einen Fehler.
Deine Aufgabe ist nicht, den Workflow neu zu bauen. Denk wie ein Engineer, der ein Production-Problem untersucht.
# Das Debugging-Szenario
Ein User fragt:
> Find recent papers about Retrieval-Augmented Generation.
Statt die Papers direkt zurückzugeben, retryt der Workflow dreimal und stoppt dann mit dieser Nachricht:
> Loop completed after reaching maximum iteration count of 3.
Die Frage lautet:
Warum retryt der Workflow, obwohl mit dem Agenten offenbar alles stimmt?
# Schritt 1: Das Problem reproduzieren
Importiere das Projekt in Flowise.
Führe den Workflow mit einem beliebigen Research-Prompt aus.
Schau dir die Ausführung genau an.
Du solltest sehen:
- Der arXiv MCP Agent schließt erfolgreich ab.
- Der Parser läuft durch.
- Der Workflow springt in den Retry Loop.
- Nach drei Durchläufen stoppt die Ausführung.
Fang an diesem Punkt noch nicht an, Nodes zu ändern. Sammle erst Evidenz.
# Schritt 2: Herausfinden, welche Ebene scheitert
Bevor du dir einzelne Nodes ansiehst, überleg dir, welcher Teil des Systems am wahrscheinlichsten schuld ist.
Frag dich:
- Ist der arXiv MCP Agent gescheitert?
- Hat der MCP-Server einen Fehler zurückgegeben?
- Ist der Parser überhaupt gelaufen?
- Welcher Node hat entschieden, in den Retry Loop zu gehen?
Diese paar Fragen grenzen die Suche schon deutlich ein.
Liefert der Agent erfolgreich Papers zurück, funktioniert die Protokollebene wahrscheinlich einwandfrei.
Das Problem sitzt dann vermutlich in der Orchestrierung.
# Schritt 3: Den Parser-Output prüfen
Öffne die Funktion Parse Status & Errors.
Lies dir die Funktion durch und finde raus, welchen Wert sie zurückgibt, wenn kein Fehler vorliegt.
Schau dir danach die Execution Logs an.
Welcher Wert kommt tatsächlich raus?
Notier ihn dir, bevor du weitermachst.
# Schritt 4: Die Branching-Logik prüfen
Öffne als Nächstes den Node Evaluate Network State.
Dieser Node entscheidet, ob der Workflow:
- zum User weitergeht, oder
- die Anfrage retryt.
Vergleiche den Wert, den dieser Node erwartet, mit dem Wert, den der Parser tatsächlich liefert.
Stimmen beide exakt überein?
Branching-Entscheidungen hängen oft an exaktem String Matching. Schon ein winziger Unterschied in Schreibweise oder Formatierung schickt die Ausführung auf den falschen Pfad.
# Schritt 5: Den Workflow fixen
Passe den Workflow so an, dass Parser und Branching Node denselben Erfolgswert verwenden.
Führe den Workflow erneut aus.
Eine erfolgreiche Ausführung sollte jetzt:
1. Papers abrufen,
1. durch den Parser laufen,
1. direkt zum User weitergehen,
1. den Retry Loop gar nicht erst auslösen.
## Checkpoint
Beantworte nach dem Fix folgende Fragen:
1. Ist die arXiv-MCP-Integration gescheitert?
1. Welcher Node hat das falsche Verhalten tatsächlich verursacht?
1. Warum ist der Workflow in den Retry Loop gegangen?
1. War das in erster Linie ein Protokollproblem oder ein Orchestrierungsproblem? Begründe deine Antwort.
## Was ist passiert?
Der Bug zeigt ein wichtiges Prinzip von Multi-Agent-Systemen: Ein Workflow kann scheitern, obwohl jede einzelne Komponente für sich genommen korrekt arbeitet.
In diesem Projekt:
- Die MCP-Integration hat erfolgreich Informationen abgerufen.
- Der Parser hat die Antwort erfolgreich verarbeitet.
- Die Orchestrierung hat den Output des Parsers falsch interpretiert.
Deshalb hat der Workflow eine Anfrage wiederholt, die längst erfolgreich war.
Solche Orchestrierungs-Bugs kommen häufig vor. Jeder Node macht seinen Job richtig, aber der Vertrag zwischen den Nodes passt nicht zusammen.
## Zusammenfassung
In dieser Lektion hast du einen Workflow analysiert, der augenscheinlich von wiederkehrenden Agentenfehlern blockiert wurde. Bei der schrittweisen Überprüfung der Ausführung hast du jedoch festgestellt, dass während die Protokollebene einwandfrei funktionierte, lag das eigentliche Problem in der Orchestrierungslogik zwischen Parser und Branching Node.
Die Fähigkeit, Integrations- von Orchestrierungsproblemen zu unterscheiden, ist eine essenzielle Debugging-Kompetenz. Je komplexer Workflows werden, desto seltener liegt die Ursache an einem defekten Agenten oder Tool. Oftmals werden lediglich Informationen zwischen eigentlich intakten Komponenten fehlerhaft übermittelt oder missinterpretiert.
In der nächsten Lektion erweiterst du das Projekt um einen zusätzlichen spezialisierten Agenten. Damit steigerst du zwar die Leistungsfähigkeit des Systems, erhöhst aber auch die Komplexität der Orchestrierung
