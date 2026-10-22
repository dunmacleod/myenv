# Datensätze mit dem Iteration Node verarbeiten

Notion page: https://app.notion.com/p/Datens-tze-mit-dem-Iteration-Node-verarbeiten-3789418319f3802686f5c7ab2a4a479c
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du fügst einem neuen Agentflow v2 einen Iteration Node hinzu, der eine Liste von Engagement-Records verarbeitet und für jeden einzelnen eine Zusammenfassung erstellt.

## Ausgangslage
Meridians Operations Manager wünscht sich eine neue Funktion: ein wöchentliches Engagement-Briefing, das eine Liste aktiver Kundenkonten durchläuft und für jedes eine einzeilige Statuszusammenfassung erstellt. Statt dass ein Consultant jedes Konto einzeln manuell abfragt, soll der Agent die gesamte Liste in einem einzigen Durchlauf verarbeiten und alle Zusammenfassungen gemeinsam zurückgeben.
Das ist ein grundlegend anderes Muster als alles, was bisher gebaut wurde. Die bestehende Canvas verarbeitet immer nur eine Anfrage auf einmal. Für die Verarbeitung einer ganzen Sammlung von Elementen braucht es einen anderen Node, den Iteration Node.
## Was der Iteration Node macht
Der Iteration Node führt für jedes Element in einem Input-Array einen definierten Sub-Flow aus, also eine Sequenz von Nodes, die in ihm verschachtelt sind. Das entspricht einer For-each-Schleife. Für jedes einzelne Element im Array führt der Iteration Node nacheinander die Nodes aus, die visuell innerhalb seiner Grenzen auf der Canvas platziert sind.
Das macht ihn zum richtigen Werkzeug für jede Aufgabe, bei der dieselbe Operation wiederholt über eine Sammlung von Inputs laufen muss. Das gilt zum Beispiel für das Verarbeiten mehrerer Dokumente, das Zusammenfassen mehrerer Records oder das Validieren einer Liste von Werten.
## Was du baust
Ein neuer eigenständiger Agentflow v2 namens Meridian Engagement Briefing. Er nimmt eine hartcodierte Liste von Engagement-Records, iteriert mit einem LLM Node innerhalb des Iteration Node über jeden einzelnen und gibt am Ende eine kombinierte Briefing-Zusammenfassung zurück.
Das Ganze wird als separater Flow gebaut, damit die beiden Use Cases sauber und unabhängig voneinander bleiben.
### Schritt 1: Einen neuen Agentflow v2 anlegen
Klicke links in der Navigation auf Agentflows und dann auf + Add New. Nenne ihn Meridian Engagement Briefing und speichere sofort.
### Schritt 2: Zum Start Node gehen und Flow State initialisieren
[COLUMN_LIST]
  [COLUMN]
    Füge einen Start Node hinzu. Ergänze im Flow-State-Bereich Folgendes:
    [TABLE]
      | Key | Initialwert |
      | engagement_list | [{"id":1,"title":"Krauss Manufacturing","completed":false},{"id":2,"title":"Bauer Logistics","completed":true},{"id":3,"title":"Novak Retail","completed":false}] |
      | briefing_output | `` |
    
  [COLUMN]
    > ➡️ Der Key engagement_list enthält ein JSON-Array mit drei Beispiel-Engagement-Records. Der Key briefing_output sammelt die Zusammenfassungen, während die Iteration läuft.
    Speichere deinen Start Node.

### Schritt 3: Einen Custom Function Node zum Parsen der Liste hinzufügen
Füge nach dem Start Node einen Custom Function Node hinzu.
Input-Variablen:
[TABLE]
  | Variablenname | Variablenwert |
  | engagementList | {{ $flow.state.engagement_list }} |
JavaScript-Funktion:
```javascript
const list = JSON.parse($engagementList);
return JSON.stringify(list);
```
Flow State aktualisieren:
[TABLE]
  | Key | Wert |
  | engagement_list | {{ customFunctionAgentflow_0.output }} |
Das bestätigt, dass die Liste gültiges JSON ist, bevor sie an den Iteration Node übergeben wird.
### Schritt 4: Einen Iteration Node hinzufügen
Füge nach dem Custom Function Node einen Iteration Node hinzu.
Konfiguriere ihn:
[TABLE]
  | Field | Wert |
  | Array Input | {{ $flow.state.engagement_list }} |
Der Array Input legt fest, über welches Array der Node iteriert. Dazu referenzierst du eine Variable, die ein Array enthält, entweder aus dem Output eines vorherigen Nodes oder aus dem Flow State.
### Schritt 5: Einen LLM Node innerhalb des Iteration Node hinzufügen
Platziere einen LLM Node innerhalb der Grenzen des Iteration Node auf der Canvas.
Konfiguriere ihn:
- Model: Wähle dein Modell und die API-Credential aus.
- Messages - System role: You are a briefing assistant for Meridian Consulting. Generate a single sentence engagement status summary from the data provided. Be concise and professional.
- Messages - User role: Engagement data: {{ $iteration.item }}. Generate a one-sentence status summary.
> ➡️ Hinweis: {{ $iteration.item }} ist die Variable, die das aktuell verarbeitete Element innerhalb des Iteration Node enthält. Bei jedem Durchlauf der Schleife enthält diese Variable einen Engagement-Record aus dem Array.

### Schritt 6: Einen Direct Reply Node hinzufügen
Der Iteration Node hat genau einen Output Anchor. Der wird erst aktiv, wenn der verschachtelte Sub-Flow für alle Elemente im Input-Array durchgelaufen ist. Füge nach dem Output des Iteration Node einen Direct Reply Node hinzu. Tippe im Message-Feld {{ ein und wähle die Output-Variable des Iteration Node aus.
Das sollte {{iterationAgentflow_0}} sein.
Speichere die Canvas. So sollte sie am Ende aussehen.
![image]((notion-hosted file))

### Schritt 7: Testen
Öffne das Chat-Interface und sende: Generate the weekly engagement briefing
- Erwartet: Der Iteration Node verarbeitet alle drei Engagement-Records, der LLM Node erzeugt für jeden eine Ein-Satz-Zusammenfassung, und der Direct Reply Node gibt am Ende alle drei Zusammenfassungen gemeinsam zurück.

> 💡 Fazit:
  Der Iteration Node übernimmt die Verarbeitung von Sammlungen, für die man sonst mehrere manuelle Anfragen oder eine eigene gescriptete Schleife bräuchte. Dabei gilt ein zentrales Designprinzip. Die Nodes innerhalb der Iteration-Node-Grenze laufen pro Element, Nodes außerhalb laufen einmal, nachdem alle Elemente verarbeitet wurden. Genau dieses Verständnis der Grenze macht den Unterschied. Ein Flow, der sie richtig nutzt, verarbeitet die Liste korrekt. Einer, der sie ignoriert, verarbeitet nur das erste Element oder lässt alle Elemente in einen einzigen Durchlauf zusammenfallen.
