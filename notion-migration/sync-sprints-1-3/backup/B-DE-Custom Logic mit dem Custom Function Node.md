# Custom Logic mit dem Custom Function Node

Notion page: https://app.notion.com/p/Custom-Logic-mit-dem-Custom-Function-Node-3789418319f380659b21ce4ecb757363
Backed up before n8n migration

> ⚠️ Das machst du in dieser Lektion: Du verstehst, was der Custom Function Node macht, wann du ihn einsetzt und wie er im bisherigen Meridian-Build schon verwendet wurde.
## Ausgangslage
In Sprint 2 und Sprint 3 ist der Custom Function Node an mehreren zentralen Stellen in Meridians Canvas aufgetaucht. In der Loop-Node-Lektion hat er den Retry Counter erhöht, in der Iteration-Node-Lektion die Engagement-Liste geparst. In beiden Fällen hat er eine spezifische Transformation übernommen, die kein anderer Node sauber hinbekommen hätte.
Diese Lektion zoomt raus und erklärt den Custom Function Node als Konzept: was er ist, wann er das richtige Werkzeug ist und wo seine Grenzen liegen. Das passiert, bevor du ihn im Sprint-3-Assessment eigenständiger einsetzt.
## Was der Custom Function Node macht
Der Custom Function Node bietet einen Mechanismus, um innerhalb des Workflows eigenen serverseitigen JavaScript-Code auszuführen. Damit lassen sich beliebige JavaScript-Snippets schreiben und ausführen. Das eignet sich gut für komplexe Datentransformationen, individuelle Business-Logik oder Interaktionen mit Ressourcen, die andere Standard-Nodes nicht direkt unterstützen.
Praktisch gesagt springt der Custom Function Node mit Code ein, wenn die visuellen Nodes nicht das können, was der Workflow braucht.
### Wie er funktioniert
Der Custom Function Node führt JavaScript auf dem Flowise-Server aus. Er hat Zugriff auf drei Kategorien von Daten:
1. Input Variables: Werte, die explizit aus dem Canvas an die Funktion übergeben werden.
```plain text
// If you define an input variable called "retryCount"
// it is accessible as $retryCount inside the function
constcount=parseInt($retryCount)||0;
```
1. Flow Context: Standardvariablen, die immer verfügbar sind.
```plain text
$flow.input// the user's original message
$flow.sessionId// current session ID
$flow.state// the entire Flow State object
```
1. Flow-State-Keys: Einzelne State-Werte.
```plain text
$flow.state.retry_count
$flow.state.engagement_list
$flow.state.status_response
```
Die Funktion muss am Ende ihrer Ausführung einen String zurückgeben. Ist der Output eine Zahl, ein Array oder ein Objekt, muss er vor der Rückgabe in einen String umgewandelt werden:

```plain text
returnString(count+1);// number to string
returnJSON.stringify(dataArray);// array to string
```
## Wann du ihn einsetzt
Der Custom Function Node ist in vier Situationen die richtige Wahl:
[TABLE]
  | Situation | Beispiel aus dem Meridian Build |
  | Counter- oder Arithmetiklogik | retry_count in der Loop-Node-Lektion inkrementieren |
  | Datenparsing oder Transformation | Engagement-List-JSON in der Iteration-Node-Lektion parsen |
  | String-Manipulation | Ein bestimmtes Feld aus einer API Response extrahieren |
  | Conditional Logic, die zu komplex für den Condition Node ist | Mehrere Felder aus dem Flow State gleichzeitig evaluieren |
Er ist nicht die richtige Wahl, wenn ein Standard-Node die Aufgabe bereits übernimmt. Einen Custom Function Node für einen HTTP Call zu nutzen, obwohl es den HTTP Node gibt, schafft unnötige Komplexität. Dasselbe gilt für den Zugriff auf einen Document Store, wenn dafür eigentlich der Retriever Node da ist. Das macht die Canvas nur schwerer lesbar.
## Was er nicht kann
Zwei wichtige Einschränkungen:
- Er kann keine neuen Flow-State-Keys anlegen. Operative Nodes können keine neuen Keys erstellen, sondern nur bereits definierte Keys aktualisieren. Jeder Key, den der Custom Function Node beschreibt, muss zuerst im Start Node initialisiert werden.
- Er kann keine Nicht-String-Werte direkt zurückgeben. Der Output-Socket des Custom Function Node liefert immer einen String. Erwartet ein nachgelagerter Node eine Zahl oder ein geparstes Objekt, muss die Umwandlung in diesem Node passieren, nicht im Return-Wert des Custom Function Node.
### Wie er sich mit dem Flow State verbindet
Der Custom Function Node kann den Flow State sowohl lesen als auch beschreiben:
Lesen:
```plain text
constcurrentCount=parseInt($flow.state.retry_count)||0;
```
Schreiben über Update Flow State:
Nachdem die Funktion gelaufen ist, ordnet die Update-Flow-State-Konfiguration den Output einem vordefinierten Key zu:
[TABLE]
  | Key | Value |
  | retry_count | {{ customFunctionAgentflow_0.output }} |
Genau dieses Muster kommt in der Lektion zur Retry-Logik mit dem Loop Node zum Einsatz. Dort gibt die Funktion den erhöhten Zähler als String zurück, und Update Flow State schreibt ihn zurück in retry_count, damit der Condition Node ihn lesen kann.
## Verständnischeck
>  Ein Custom Function Node gibt direkt die Zahl 3 zurück, ohne sie in einen String umzuwandeln. Was passiert?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/33e68568-49e1-47c5-83f4-16224eef9ee3


> 💡 Fazit:
  Der Custom Function Node ist der Notausgang für Logik, die sich mit den visuellen Nodes nicht abbilden lässt. Gerade weil er uneingeschränkt ist, ist er so mächtig. Diese Freiheit hat eine feste Grenze: Er muss immer einen String zurückgeben. Jeder andere Node auf der Canvas erwartet String-Output vom Custom Function Node, und stille Type-Mismatches gehören zu den Fehlerarten, die sich in einem laufenden Flow am schwersten diagnostizieren lassen.
