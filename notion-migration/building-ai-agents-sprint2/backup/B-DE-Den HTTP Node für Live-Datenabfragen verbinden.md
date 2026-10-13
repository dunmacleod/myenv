# Den HTTP Node für Live-Datenabfragen verbinden

Notion page: https://app.notion.com/p/Den-HTTP-Node-f-r-Live-Datenabfragen-verbinden-3789418319f3802d99fee87121dfbb6c
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du ersetzt den Platzhalter-Direct-Reply-Node von Pfad B durch einen HTTP Node. Dieser verbindet sich mit einem Mock-API-Endpunkt und schließt so den Live-Datenabfragepfad im Meridian Agentflow v2 ab.

## Den Rahmen setzen
Meridians Routing funktioniert jetzt einwandfrei. Der Condition Agent Node ordnet Consultant-Queries nach ihrer Absicht ein und leitet sie zuverlässig auf den richtigen Pfad. Die Knowledge Queries gehen zum Agent Node mit Document-Store-Retrieval. Die Statusanfragen gehen zu Pfad B, der aktuell eine Platzhalternachricht zurückgibt, die dem Consultant sagt, er solle sich direkt an seinen Engagement Manager wenden.
Dieser Platzhalter war immer nur temporär. Klaus Brandt hat jetzt bestätigt, dass Meridians Operations-Team eine einfache interne API hat, die Engagement-Statusdaten für einen gegebenen Kundennamen zurückgibt. Die nächste Aufgabe des Entwicklungsteams besteht darin, Pfad B mit dem HTTP Node mit dieser API zu verbinden, sodass der Agent sie tatsächlich abruft, wenn ein Consultant Live-Engagement-Status anfragt.
Für diese Lektion wird eine öffentlich verfügbare Mock API anstelle von Meridians echter interner API verwendet. Die Konfigurationsschritte sind identisch mit denen, die mit einem echten Endpunkt verwendet würden. Nur die URL und das Antwortformat unterscheiden sich dabei.
## Was du erstellst
Einen aktualisierten Meridian Base Agent-Canvas, bei dem der Platzhalter-Direct-Reply-Node von Pfad B ersetzt wird durch:
- Einen HTTP Node, der einen GET-Request an eine Mock API sendet
- Einen Agent Node (eine zweite, schlanke Instanz), der die rohe API-Antwort in eine natürlichsprachliche Antwort formatiert
- Einen Direct Reply Node, der die formatierte Antwort an den Consultant zurückgibt
Der Pfad-A-Flow (Condition Agent Node → Agent Node → Direct Reply A) bleibt unverändert.
## Die Mock API
Diese Lektion nutzt JSONPlaceholder: eine kostenlose, öffentliche Mock-API, die verlässliche JSON-Daten liefert. Du brauchst dafür weder einen Account noch eine Authentifizierung.
Der verwendete Endpunkt ist:
```xml
https://jsonplaceholder.typicode.com/todos/1
```
Dies gibt ein JSON-Objekt zurück, das ein Task Item repräsentiert. In der Lektion wird dies als Mock-Engagement-Record behandelt. Du ordnest die Antwortfelder Meridian-Engagement-Daten zu, um die HTTP-Node-Konfiguration zu bauen und zu testen.
> ➡️ Warum eine Mock API: Meridians interne API existiert außerhalb dieses Business Case nicht. Die JSONPlaceholder ermöglicht es, die HTTP-Node-Konfiguration gegen einen echten Live-Endpunkt mit echten Antworten zu erstellen und zu testen, wodurch die technischen Schritte präzise und überprüfbar werden. Wir werden später betrachten, wie Response Handling und Fehlerlogik abgedeckt werden, die identisch für echte APIs gelten.

## Deine Aufgaben
### Schritt 1: Den Meridian-Base-Agent-Canvas öffnen
Öffne Flowise unter http://localhost:3000. Klicke auf Agentflows und öffne deinen Meridian Base Agent-Canvas.
Er sollte so aussehen.
![image]((notion-hosted file))
### Schritt 2: Den Platzhalter-Direct-Reply-Node entfernen
Klicke auf Direct Reply B und lösche ihn. Lösche auch die Verbindungslinie vom status_request-Output des Condition Agent Nodes zu ihm.
Der status_request-Output-Anker des Condition Agent Nodes ist jetzt nicht verbunden.
### Schritt 3: Den HTTP Node hinzufügen
Klicke auf dem Canvas auf (+). Wähle unter der Kategorie Agentflow HTTP aus und füge ihn zum Canvas hinzu. Positioniere ihn dort, wo Direct Reply B war.
Verbinde den Condition Agent Node status_request output mit dem HTTP Node input.
### Schritt 4: Den HTTP Node konfigurieren
Klicke auf den HTTP Node, um seine Einstellungen zu öffnen. Konfiguriere ihn wie folgt:

![image]((notion-hosted file))
Wie die Antwort aussieht: JSONPlaceholder gibt für diesen Endpunkt das folgende JSON zurück:
```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```
In dieser Lektion dient dies als Mock-Engagement-Record: title steht für den Engagement-Namen, completed zeigt den Fertigstellungsstatus und id dient als Engagement-Referenznummer.
### Schritt 5: Flow State für die HTTP-Antwort aktualisieren
Klicke auf den Start Node und scrolle zu Update Flow State. Füge Folgendes hinzu:
[TABLE]
  | Key | Initial Value |
  | status_response | `` |
Alle State Keys, die im gesamten Workflow verwendet werden, müssen mit ihren Standardwerten über den Flow-State-Parameter im Start Node initialisiert werden. Speichere den Start Node.
### Schritt 6: Einen zweiten Agent Node für Response Formatting hinzufügen
Der HTTP Node liefert rohes JSON zurück. Ein Consultant, der nach dem Engagement-Status fragt, erwartet eine natürliche Antwort und kein JSON-Objekt. Ein schlanker Agent Node nach dem HTTP Node verwandelt die Rohdaten in gut lesbaren Text. Klicke auf (+) und füge einen zweiten Agent Node auf dem Canvas hinzu. Platziere ihn rechts vom HTTP Node und verbinde den Output des HTTP Nodes mit dem Input dieses neuen Agent Nodes.
Konfiguriere den zweiten Agent Node wie folgt:
Model: Gemini 2.5 Flash mit deinem gespeicherten Gemini-Credential.
Messages - System role:
> Du bist ein Response Formatter für den internen Agenten von Meridian Consulting. Du erhältst rohe Engagement-Daten, die aus Meridians Operations API abgerufen wurden, und wandelst sie in eine klare, professionelle natürlichsprachliche Zusammenfassung für das Consulting-Team um. Formatiere die Engagement-Informationen klar. Gib die Engagement-Referenz, den Namen und den aktuellen Status an. Halte die Antwort knapp, maximal zwei bis drei Sätze. Füge keine Informationen hinzu, die nicht in den Daten enthalten sind.
Messages - User role:
> Hier sind die aus der API abgerufenen Engagement-Daten: {{httpAgentflow_0}}. Bitte formatiere dies als professionelle Engagement-Statuszusammenfassung für den Consultant.
Verbinde den Document Store meridian-knowledge nicht mit diesem Agent Node. Dieser Node hat eine einzelne Formatierungsaufgabe. Er benötigt kein Knowledge Retrieval.
### Schritt 7: Direct Reply B hinzufügen
Klicke auf (+) und füge einen Direct Reply Node zum Canvas hinzu. Positioniere ihn rechts vom zweiten Agent Node. Verbinde den Output des zweiten Agent Nodes mit diesem Direct Reply Node input.
Gib im Message-Feld {{ ein und wähle den Output des zweiten Agent Nodes aus dem Variablenselektor aus.
Der Variablenname wird {{agentAgentflow_1}} sein; bestätige den exakten Namen im Selektor.
### Schritt 8: Die vollständige Canvas-Struktur bestätigen
Dein Canvas sollte jetzt Folgendes zeigen:
![image]((notion-hosted file))
Mit dem Document Store meridian-knowledge, der nur mit Agent Node A verbunden ist. Speichere den Canvas.
### Schritt 9: Den End-to-End-Test ausführen
Öffne das Chat-Symbol und führe die folgenden Tests in separaten Sessions aus.
Test 1 - Knowledge-Pfad funktioniert weiterhin: What are the project classification tiers at Meridian?
- Erwartet: Routet zu Agent Node A. Gibt Policy-Inhalte aus dem Document Store zurück. Bestätigt, dass Pfad A von den Änderungen an Pfad B nicht betroffen ist.
Test 2 - Status-Pfad mit HTTP Node: Can you check the engagement status for the Krauss account?
- Erwartet: Routet über den Condition Agent Node zum HTTP Node. Der HTTP Node ruft Daten von JSONPlaceholder ab. Agent Node B formatiert die Antwort. Direct Reply B gibt eine natürlichsprachliche Engagement-Zusammenfassung zurück.
Test 3 - Mehrdeutige Query routet weiterhin korrekt: What is the escalation status procedure for severity level 2 issues?
- Erwartet: Condition Agent Node routet korrekt zu Agent Node A. Gibt Verfahrensinhalte aus dem Document Store zurück.
### Wie ein erfolgreicher Test 2 aussieht
Der Consultant sollte eine Antwort wie diese erhalten:
> „Der Engagement-Record zeigt die Referenznummer 1, mit dem Titel ‚delectus aut autem‘, mit aktuellem Status offen (noch nicht abgeschlossen). Bitte bestätigen Sie mit Ihrem Engagement Manager, ob dieser Record zu den Krauss-Account-Details passt.“
Die genaue Formulierung hängt davon ab, wie Gemini die Mock-Daten aufbereitet. Entscheidend ist: Die Antwort klingt natürlich und stammt direkt aus der API-Antwort.
> ⚠️ Bekannte Einschränkung: Die Flowise-GitHub-Issues weisen darauf hin, dass das direkte Weitergeben von HTTP-Node-Output an nachgelagerte Nodes über {{ variable }}-Syntax in bestimmten Flowise-Versionen manchmal als Literal String statt als aufgelöster Wert ausgewertet werden kann. Wenn der zweite Agent Node {{ httpAgentflow_0.data }} als Klartext statt der tatsächlichen JSON-Daten erhält, verwende stattdessen den in Schritt 5 bestätigten Update Flow State-Ansatz, indem du in der User Message aus {{ $flow.state.status_response }} liest. Das ist die zuverlässigere Methode, um HTTP-Node-Output nachgelagert weiterzugeben.

### Checkliste: Vor dem Fortfahren bitte bestätigen
- [ ] Platzhalter-Direct-Reply-B vom Canvas entfernt
- [ ] HTTP Node hinzugefügt und mit dem status_requestOutput des Condition Agent Nodes verbunden
- [ ] HTTP Node konfiguriert: GET-Methode, JSONPlaceholder-URL, JSON-Response-Type
- [ ] Key status_response zum Flow State des Start Nodes hinzugefügt
- [ ] HTTP Node Update Flow State so konfiguriert, dass die Antwort in status_response geschrieben wird
- [ ] Zweiter Agent Node hinzugefügt und mit dem HTTP-Node-Output verbunden
- [ ] Zweiter Agent Node mit Formatting-System-Prompt und User Message konfiguriert, die {{ $flow.state.status_response }} referenziert
- [ ] Kein Document Store mit dem zweiten Agent Node verbunden
- [ ] Direct Reply B hinzugefügt und mit dem Output des zweiten Agent Nodes verbunden
- [ ] Canvas vor dem Testen gespeichert
- [ ] Test 1 bestätigt, dass Pfad A unverändert funktioniert
- [ ] Test 2 gibt eine formatierte natürlichsprachliche Engagement-Zusammenfassung zurück
- [ ] Test 3 bestätigt, dass mehrdeutiges Routing weiterhin korrekt funktioniert

> 💡 Takeaway: 
  Ein Tool nützt nur so viel wie seine Beschreibung: Sie steuert, wann das Modell es aufruft. Mock-Code, Input-Schema und Flowise-Canvas-Konfiguration sind zwar notwendig, doch allein die Tool-Beschreibung entscheidet, ob Gemini im richtigen Moment zugreift.
  Eine zu vage Beschreibung verursacht Routing-Fehler. Überschneidet sie sich mit der Wissensdatenbank, entsteht Verwirrung. In dieser Lektion entwickeltest du die praktische Fähigkeit, zwei ähnliche Funktionen in natürlicher Sprache präzise voneinander abzugrenzen.
