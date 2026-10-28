# Tool-Fehler und Endlosschleifen behandeln

Notion page: https://app.notion.com/p/Tool-Fehler-und-Endlosschleifen-behandeln-3779418319f380099057cc7c61cfc543
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Schutzmechanismen entwerfen, die wiederholte Tool-Aufrufe nach einem Fehler stoppen, und einen kundenfreundlichen Fallback definieren, bevor zusätzliche Tools mit dem Contigo-Agenten verbunden werden.

## Die Ausgangslage
Ein Agent mit Tools kann auf eine neue Art scheitern: Das Modell kann ein Tool immer wieder aufrufen, weil die angeforderte Aufgabe noch nicht gelöst ist.
Stell dir vor, der Kreditstatus-Service ist nicht verfügbar. Der Agent ruft ihn auf, erhält einen Fehler, erkennt, dass der Status weiterhin fehlt, und versucht es erneut. Ohne Grenze kann der Workflow Zeit und Tokens verbrauchen, ohne dem Kunden eine hilfreiche Antwort zu liefern.
Ein produktionsnahes Design benötigt deshalb zwei Ebenen:
1. eine deterministische Iterationsgrenze im AI Agent;
1. eine klare Anweisung, wie bei einem nicht nutzbaren Tool-Ergebnis reagiert wird.

## Ebene 1: Max Iterations
Der n8n AI Agent besitzt die Option Max Iterations. Sie begrenzt, wie viele Reasoning-/Tool-Zyklen das Modell für eine Anfrage ausführen darf.
Für diese Contigo-Übung setzt du:
Options → Max Iterations = 4
Vier Iterationen lassen genug Spielraum für die einfachen Multi-Tool-Szenarien dieses Sprints und verhindern gleichzeitig lange Wiederholungsschleifen. Der konkrete Produktionswert ist eine Architekturentscheidung, sollte aber immer bewusst gewählt werden.
> ➡️ Wichtig: Max Iterations ist ein Circuit Breaker, aber keine vollständige Fehlerbehandlung. Die Grenze stoppt die Schleife; die System Message muss zusätzlich festlegen, was der Kunde hört, wenn ein Tool nicht verfügbar ist.

## Ebene 2: Strukturierte Tool-Fehler
Wenn du einen Tool-Workflow selbst kontrollierst, sollte er einen strukturierten Fehler zurückgeben, den der Agent eindeutig interpretieren kann, zum Beispiel:
```json
{
  "success": false,
  "error": "service_unavailable"
}
```
Lass das Modell Erfolg nicht aus einer leeren oder fehlerhaften Antwort ableiten. Ein eindeutiges Erfolgsfeld macht den Fehlerzustand beobachtbar und testbar.
Der Kreditstatus-Sub-Workflow der nächsten Lektion enthält einen simulierten Fehlerfall, damit du dieses Verhalten sicher testen kannst.

## Deine Aufgaben
### Aufgabe A: Circuit Breaker konfigurieren
Öffne den AI Agent im Contigo-Workflow und füge unter den Optionen Max Iterations = 4 hinzu.
Begründe in zwei Sätzen, warum dieser Wert zur aktuellen Architektur passt. Berücksichtige, dass die meisten Anfragen null oder einen Tool-Aufruf benötigen und nur wenige Retrieval mit einem weiteren Tool kombinieren.

### Aufgabe B: Fehleranweisung schreiben
Ergänze die System Message um eine kurze Regel für nicht verfügbare Tool-Ergebnisse und eine ausgeschöpfte Reasoning-Schleife.
Eine starke Version deckt drei Anforderungen ab:
- Keine Erfindungen: Niemals einen Kreditstatus erfinden oder behaupten, ein Tool sei erfolgreich gewesen.
- Keine technischen Details: Keine internen Fehler, Node-Namen, Stack Traces oder Implementierungsdetails zeigen.
- Klarer nächster Schritt: Dem Kunden sagen, was er stattdessen tun kann.
Beispiel:
> „Wenn ein benötigtes Tool nicht verfügbar ist oder kein nutzbares Ergebnis liefert, rate nicht und behaupte nicht, die Aktion sei erfolgreich gewesen. Sage dem Kunden: 'Ich kann diese Information im Moment nicht abrufen. Bitte versuche es später erneut oder wende dich an deine Contigo-Ansprechperson.'"

### Aufgabe C: Beobachtbaren Fehlervertrag definieren
Definiere vor dem Bau des Kreditstatus-Tools die erwarteten Ausgaben:
[TABLE]
  | Bedingung | Erwartetes Ergebnis |
  | Status gefunden | success = true plus Antragsreferenz, Status, Detail und nächster Schritt |
  | Referenz unbekannt | success = false, error = not_found |
  | Service nicht verfügbar | success = false, error = service_unavailable |
Dieser Vertrag macht die späteren Tests deterministisch.

## Check for Understanding
> 💡 Ein Status-Tool liefert wiederholt ein Nicht-verfügbar-Ergebnis und der Agent ruft es immer wieder auf. Welcher Schutzmechanismus sollte die Reasoning-Schleife stoppen, selbst wenn das Modell weiter versucht?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e820b00b-4cf0-4abe-8c70-96b6bf6aafc0

> 💡 Takeaway: Zuverlässige Tool-Nutzung braucht sowohl Modellanweisungen als auch deterministische Ausführungsgrenzen. Max Iterations begrenzt die Schleife; strukturierte Tool-Ergebnisse und eine präzise Fehleranweisung bestimmen, was danach passiert.