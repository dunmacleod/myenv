# Erster Gemini-gestützter Agentflow v2

Notion page: https://app.notion.com/p/Erster-Gemini-gest-tzter-Agentflow-v2-3789418319f3806fa588f57b9f1eacb8
Backed up before n8n migration

> 💡 Was du in dieser Lektion tun wirst: Einen minimal funktionierenden Agentflow v2 in Flowise bauen und testen, indem du einen Start Node, einen mit Gemini konfigurierten Agent Node und einen Direct Reply Node verbindest, und anschließend durch einen strukturierten Zwei-Turn-Test bestätigst, dass er funktioniert.

## Warum ist das der Ausgangspunkt?
Das Team von Meridian Consulting versteht den Stack, die Oberfläche und den Agentflow-v2-Node-Graph. Nun muss das System in der Praxis überzeugen. In dieser Phase werden wir genau das bestätigen: Ein minimaler Agentflow v2, der eine Nutzernachricht empfängt, mit Gemini Reasoning ausführt und eine kohärente Antwort zurückgibt, bildet die Basis für alles Weitere.
Bevor das Retrieval, die Verzweigungen, die Tools oder die benutzerdefinierte Anweisungen dazukommen, muss der zentrale Loop korrekt funktionieren, d.h. Nutzereingabe, Agenten-Reasoning, Antwortausgabe. Wer seine Baseline nicht überprüft, arbeitet auf Basis von Annahmen.
Dieser Walkthrough führt dich Schritt für Schritt durch den Aufbau dieser Baseline.
### Schritt 1: Einen neuen Agentflow v2 erstellen
Öffne dein Flowise unter http://localhost:3000 und navigiere im linken Navigationsbereich zu Agentflows. Klicke auf + Add New, um einen leeren Canvas zu öffnen.
Gib dem Flow einen beschreibenden Namen, indem du oben auf dem Bildschirm auf das Standard-Namensfeld klickst und Meridian Base Agent eingibst. Speichere sofort über das Speichersymbol oben rechts.
> ➡️ Warum das wichtig ist: Flowise speichert nicht automatisch. Vor dem Bauen zu benennen und zu speichern verhindert, dass Arbeit verloren geht, wenn der Browser-Tab geschlossen oder der Serverprozess unterbrochen wird.

### Schritt 2: Einen Start Node hinzufügen
Wenn du einen neuen Agentflow startest, ist normalerweise bereits ein Start Node vorhanden. Falls nicht, klicke auf dem Canvas auf den (+)-Button. Suche unter der Kategorie Agentflow nach Start und füge ihn dem Canvas hinzu. Positioniere ihn auf der linken Seite des Arbeitsbereichs.
Der Start Node ist der verpflichtende Einstiegspunkt jedes Agentflow v2. Er empfängt den Input des Nutzers und gibt ihn an den Flow weiter. Ohne ihn hat der Flow keinen Einstiegspunkt und kann nicht ausgeführt werden.
Lass im Einstellungsbereich des Start Nodes vorerst die Standardkonfiguration bestehen. Der Input-Typ ist standardmäßig auf Chat gesetzt, was für diesen Agenten korrekt ist.

### Schritt 3: Einen Agent Node hinzufügen
Klicke erneut auf (+). Suche unter der Kategorie Agentflow nach Agent und füge ihn dem Canvas hinzu. Positioniere ihn rechts vom Start Node.
Der Agent Node ist die Reasoning-Engine des Flows. Er verbindet sich mit einem Sprachmodell, enthält den System-Prompt und entscheidet auf Grundlage des Inputs, den er erhält, welche Aktion ausgeführt werden soll.
Konfiguriere den Agent Node wie folgt:
- Connect Credential: Öffne den Agenten, wähle das Model aus und fülle die Details aus. Wähle den Gemini API-Key aus, der in deinem Credentials Manager gespeichert ist. Wenn er nicht angezeigt wird, navigiere im linken Navigationsbereich zu Credentials und bestätige, dass der Key korrekt gespeichert wurde.
- Model: Wähle dein Modell aus dem Modell-Dropdown aus.
- Temperature: Lass vorerst den Standardwert eingestellt.
- System Prompt: Lass dieses Feld für diesen Baseline-Test leer. Ein System-Prompt wird später hinzugefügt.

### Schritt 4: Einen Direct Reply Node hinzufügen
Klicke erneut auf (+). Suche unter der Kategorie Agentflow nach Direct Reply und füge ihn dem Canvas hinzu. Positioniere ihn rechts vom Agent Node.
Der Direct Reply Node sendet die Antwort des Agenten zurück an den Nutzer und beendet diesen Ausführungszweig.
Nachdem du den Direct Reply Node hinzugefügt hast, klicke darauf, um seine Einstellungen zu öffnen. Tippe im Feld Message {{, um den Variablenselektor zu öffnen, und wähle den Output des Agent Nodes aus. Er sollte wie folgt aussehen:
```python
{{agentAgentflow_0 }}
```
Dadurch wird die Antwort des Agenten mit der Antwort verbunden, die an den Nutzer gesendet wird. Ohne dies wird der Flow erfolgreich ausgeführt, gibt aber nichts an die Chat-Oberfläche zurück.

### Schritt 5: Die Nodes verbinden
Zeichne der Reihe nach die folgenden Verbindungen :
1. Klicke auf den Output-Socket des Start Nodes und halte ihn gedrückt. Ziehe die Edge zum Input-Socket des Agent Nodes und lasse los.
1. Klicke auf den Output-Socket des Agent Nodes und halte ihn gedrückt. Ziehe die Edge zum Input-Socket des Direct Reply Nodes und lasse los.
Dein Canvas sollte jetzt eine gerade Drei-Node-Kette zeigen: Start Node → Agent Node → Direct Reply Node
Wenn eine Edge nach dem Verbinden verschwindet, sind die Socket-Typen inkompatibel. Bestätige, dass du Output mit Input in die richtige Richtung verbindest (von links nach rechts).
Speichere den Canvas.
![image]((notion-hosted file))

### Schritt 6: Speichern und den Zwei-Turn-Test ausführen
Speichere deinen Agentflow. Klicke auf das violette Chat-Symbol oben rechts auf dem Canvas, um die integrierte Testoberfläche zu öffnen.
Führe das folgende Zwei-Turn-Gespräch aus:
> Turn 1: „Mein Name ist Lena und ich arbeite am Krauss-Manufacturing-Account.“
![image]((notion-hosted file))
> Turn 2: „An welchem Kundenaccount arbeite ich?“
![image]((notion-hosted file))
Worauf du achten solltest:
- Wenn der Agent mit Krauss Manufacturing antwortet oder in Turn 2 auf Lenas Namen Bezug nimmt, ist die Verbindung zum Gemini-Modell aktiv und der Agent Node behält den Gesprächskontext innerhalb der Session korrekt.
- Wenn der Agent einen generischen Fehler oder keine Antwort zurückgibt, ist der API-Key möglicherweise nicht korrekt verbunden. Prüfe Folgendes:
  - 401-Fehler: Kehre zu Schritt 3 zurück, bestätige, dass das Credential in den Einstellungen des Agent Nodes ausgewählt ist, speichere den Canvas und teste erneut
  - Gar keine Antwort: Bestätige, dass alle drei Nodes durch sichtbare Edges verbunden sind und der Canvas gespeichert wurde
Wenn der Agent in Turn 2 fragt, um welchen Account es geht, ist das eingebaute Session Memory des Agent Nodes nicht aktiv. Bestätige, dass das Modell korrekt konfiguriert ist und der Canvas vor dem Testen gespeichert wurde.

## Checkliste: Vor dem Weitermachen bestätigen
- [ ] Neuer Agentflow v2 erstellt, Meridian Base Agent benannt und vor dem Bauen gespeichert
- [ ] Start Node zum Canvas hinzugefügt
- [ ] Agent Node hinzugefügt, Gemini-Credential verbunden und Gemini 2.5 Flash als Modell ausgewählt
- [ ] Direct Reply Node zum Canvas hinzugefügt
- [ ] Start Node durch eine sichtbare Edge mit dem Agent Node verbunden
- [ ] Agent Node durch eine sichtbare Edge mit dem Direct Reply Node verbunden
- [ ] Canvas vor dem Testen gespeichert
- [ ] Zwei-Turn-Test abgeschlossen und Agent hat den Account-Namen in Turn 2 ohne Nachfrage abgerufen

## Verständnis prüfen
>  Ein Meridian-Entwickler führt den Zwei-Turn-Test aus, und der Agent fragt in Turn 2 erneut nach dem Account-Namen. Der Canvas wurde gespeichert. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8f4dfde2-7dbd-4c94-a202-b8ff140e500a

> 💡 Takeaway: 
  Ein funktionierender minimaler Agentflow v2 (Start Node, Agent Node, Direct Reply Node) ist die überprüfte Ausgangsbedingung für alles, was folgt. Jede Fähigkeit, die ab diesem Punkt hinzugefügt wird, baut auf diesem zentralen Loop auf.
  Ihn jetzt durch einen strukturierten Zwei-Turn-Test zu überprüfen bedeutet, dass spätere Probleme dem zugeschrieben werden können, was hinzugefügt wurde, nicht dem, was bereits vorhanden war.