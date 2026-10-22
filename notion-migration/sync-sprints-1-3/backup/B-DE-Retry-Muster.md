# Retry-Muster

Notion page: https://app.notion.com/p/Retry-Muster-9939418319f382279b29813e0c79c2ad
Backed up before n8n migration

Sofia fügt Timeouts hinzu, und der Workflow bleibt nicht mehr hängen. Dabei fällt ihr etwas Neues auf. Einige Timeouts treffen Anfragen, die mit einer zweiten Chance erfolgreich gewesen wären. Die Shipping-API läuft in einen Timeout, funktioniert einen Moment später aber wieder problemlos. Die Warranty-Datenbank ist kurz überlastet und erholt sich Sekunden später. Das sind temporäre Unterbrechungen. Behandelt man sie als endgültige Fehler, verschwendet das Arbeit und frustriert Kunden. Deren Anfragen wären beim zweiten Versuch durchgegangen.
Würde jeder temporäre Fehler den gesamten Workflow stoppen, scheiterten viele Prozesse unnötig, die eigentlich sauber durchgelaufen wären.
Deshalb nutzen orchestrierte Systeme Retries. Der Workflow gibt nach einem fehlgeschlagenen Schritt nicht sofort auf. Er versucht die Operation erneut, bis zu einem definierten Limit. Erst danach gilt der Fehler als echt.
## Warum Retries existieren
Viele Fehler in verteilten Systemen sind temporär.
Cascadias Warranty-Claim-Workflow zeigt das Muster:
1. Ein User reicht eine Supportanfrage ein.
1. Ein Retrieval Agent durchsucht die Knowledge Base.
1. Die Knowledge-Base-API läuft temporär in einen Timeout.
1. Der Workflow erhält einen Fehler.
An diesem Punkt hat der Orchestrator zwei Möglichkeiten:
- den Workflow sofort scheitern lassen.
- die Operation erneut versuchen.
In vielen realen Systemen klappt der zweite Versuch, weil das zugrunde liegende Problem temporär war.
Mit Retries erholen sich Workflows von diesen kurzlebigen Fehlern, ohne dass ein Mensch eingreifen muss.
![image]((notion-hosted file))
![image]((notion-hosted file))
## Temporäre vs. permanente Fehler
Nicht jeder Fehler sollte erneut versucht werden.
Ein Retry ist sinnvoll, wenn der Fehler wahrscheinlich von selbst verschwindet.
[COLUMN_LIST]
  [COLUMN]
    > ⏱️ Beispiele für temporäre Fehler:
      - Netzwerkunterbrechungen
      - API-Timeouts
      - temporäre Agenten-Nichtverfügbarkeit
      - Rate Limiting durch einen externen Service
  [COLUMN]
    > ♾️ Beispiele für permanente Fehler:
      - ungültige User-Eingabe
      - fehlende Pflichtinformationen
      - falsche Zugangsdaten
      - Logikfehler im Workflow
Einen permanenten Fehler erneut zu versuchen, verschwendet normalerweise Zeit und Ressourcen, weil sich das Ergebnis nicht ändern wird.
Eine nützliche Frage lautet:
> „Wenn ich exakt denselben Schritt in ein paar Sekunden erneut ausführe, gibt es eine realistische Chance, dass er erfolgreich ist?“
## Häufige Retry-Strategien
Unterschiedliche Systeme nutzen unterschiedliche Retry-Policies.
Immediate Retry bedeutet, die Operation direkt nach dem Fehlschlag erneut zu versuchen, ohne Verzögerung. Begrenzte Retries bedeuten, die Operation eine feste Anzahl von Malen zu versuchen, bevor aufgegeben wird. Retry mit Verzögerung führt eine kurze Wartezeit zwischen den Versuchen ein, damit das System Zeit hat, sich zu erholen. Exponential Backoff erhöht die Wartezeit nach jedem Fehler, typischerweise durch Verdopplung der Verzögerung bei jedem Versuch.
Exponential Backoff ist bei der Arbeit mit externen APIs verbreitet, weil es den Druck auf einen bereits belasteten Service reduziert. Zum Beispiel:
![image]((notion-hosted file))
Ein Loop Node ist eine Workflow-Komponente, die die Ausführung zurück zu einem früheren Schritt leitet.
![image]((notion-hosted file))
Loops können für viele Zwecke genutzt werden, aber eine häufige Anwendung ist die Implementierung von Retries.
Wenn ein Schritt scheitert, kann der Workflow:
1. den Fehler erkennen.
1. prüfen, ob ein weiterer Retry erlaubt ist.
1. zum fehlgeschlagenen Schritt zurückspringen.
1. die Operation erneut versuchen.
Der Workflow läuft weiter, bis entweder:
- die Operation erfolgreich ist.
- das maximale Retry-Limit erreicht ist.
Der Loop Node ist daher kein Retry-Pattern an sich. Stattdessen ist er einer der Mechanismen, mit denen ein Retry-Pattern implementiert werden kann.
## Kerngedanke
Retries helfen orchestrierten Systemen, resilient zu bleiben, wenn Fehler temporär sind.
Das Ziel ist nicht, Arbeit endlos zu wiederholen. Das Ziel ist, einem Workflow eine realistische Gelegenheit zu geben, sich von kurzlebigen Problemen zu erholen und erfolgreich weiterzulaufen.
Wenn sie sorgfältig eingesetzt werden, können Retries die Zuverlässigkeit drastisch verbessern, ohne menschliche Intervention zu benötigen.
## Zusammenfassung
Fehler gehören in orchestrierten Systemen zum Normalbetrieb. Nicht jeder Fehler heißt aber, dass der Workflow sofort stoppen muss. Viele Fehler sind temporär und verschwinden, wenn die Operation erneut ausgeführt wird.
Retries sind ein verbreitetes Resilienz-Pattern. Damit erholen sich Workflows von kurzlebigen Problemen wie Netzwerkunterbrechungen, API-Timeouts oder temporär nicht verfügbaren Agenten. Der Workflow unternimmt einen weiteren Versuch, bevor er aufgibt.
Retries lohnen sich allerdings nur, wenn eine realistische Chance besteht, dass dieselbe Operation später klappt. Permanente Probleme wie ungültige Eingaben, fehlende Daten oder falsche Zugangsdaten brauchen normalerweise eine andere Lösung.
Ein Loop Node ist eine Möglichkeit, Retries in einem orchestrierten Workflow zu implementieren. Er leitet die Ausführung zu einem vorherigen Schritt zurück. So versucht der Workflow eine Operation erneut, bis sie erfolgreich ist oder das definierte Retry-Limit erreicht.
Der Kerngedanke ist einfach: Retries lassen Workflows temporäre Probleme automatisch überstehen. Das macht orchestrierte Systeme zuverlässiger und resilienter.