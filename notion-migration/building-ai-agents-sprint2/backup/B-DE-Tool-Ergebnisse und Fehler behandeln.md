# Tool-Ergebnisse und Fehler behandeln

Notion page: https://app.notion.com/p/Tool-Ergebnisse-und-Fehler-behandeln-3789418319f38086a953e0eac5a4db5d
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du entwirfst eine professionelle Ergebnisintegration und ein sauberes Failure Handling im Meridian Agentflow v2, sowohl für erfolgreiche HTTP-Antworten als auch für Fehlerzustände.

## Den Rahmen festlegen
Der Meridians Agentflow v2 routet Queries jetzt nach einer Absicht und ruft Live-Engagement-Daten über den HTTP Node ab. Wenn ein Consultant nach einem Engagement-Status fragt, wird der Flow korrekt ausgeführt. Der Condition Agent Node klassifiziert die Query, der HTTP Node ruft die Daten ab, der Agent Node B formatiert sie, und der Direct Reply B gibt die Antwort zurück.
Der Happy Path funktioniert. Doch beim erweiterten Testen treten zwei Fehlermuster auf, die die aktuelle Konfiguration nicht angemessen behandelt.
Das erste ist ein Präsentationsproblem. Wenn der HTTP Node eine erfolgreiche Antwort zurückgibt, reproduziert Agent Node B manchmal die rohe JSON-Struktur direkt, statt sie in natürliche Sprache umzuwandeln. Ein Consultant, der nach einem Engagement-Status fragt, erhält dann etwas wie:
```json
{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}
```
Das ist technisch korrekt, liest sich aber wie ein Datenbank-Dump statt wie eine professionelle Antwort eines Consulting-Tools.
Das zweite ist ein Problem beim Failure Handling. Beim Testen verwies ein Developer den HTTP Node absichtlich auf eine ungültige URL, um einen API-Ausfall zu simulieren. Statt den Fehler anzuerkennen und den Consultant an seinen Engagement Manager zu verweisen, generierte der Agent Node B einen erfundenen Status, der darin bestand zu halluzinieren, dass ein Engagement aktiv und in der Implementierungsphase sei, obwohl der HTTP Node einen Fehler zurückgegeben hatte.
Beide Probleme sind System-Prompt-Fehler. Der HTTP Node und der Agent Node B funktionieren wie konfiguriert. Der Agent verarbeitet Outputs falsch, weil ihm dafür explizite Anweisungen fehlen.
## Die zwei Output-Zustände
Deine Aufgabe umfasst das Entwerfen des Verhaltens von Agent Node B für zwei unterschiedliche Output-Zustände. Prüfe beide, bevor du beginnst.
### Output-Zustand 1: Erfolgreiche HTTP-Antwort
```xml
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```
Behandle dies als Meridians Mock-Engagement-Record, wobei:
- id = Engagement-Referenznummer
- title = Engagement-Name
- completed = ob das Engagement geschlossen ist (false = aktiv, true = geschlossen)
Der Agent Node B muss dies in eine natürliche, professionelle Antwort umwandeln, die die wichtigsten Informationen klar darstellt, ohne die rohe JSON-Struktur oder Feldnamen zu reproduzieren.
### Output-Zustand 2: HTTP-Node-Fehler
Wenn ein HTTP-Node-Request fehlschlägt, gibt Flowise eine Fehlerantwort an den nachgelagerten Node zurück. Der Fehler erscheint typischerweise als String, der den HTTP-Statuscode und die Fehlermeldung enthält, statt als erwarteter JSON-Body.
Der Agent Node B muss den Fehler klar anerkennen und in einfacher Sprache kommunizieren, was passiert ist. Die Antwort muss zu einem Consulting Professional passen und einen klaren nächsten Schritt aufzeigen, ohne einen Status zu erfinden oder den Fehler als Teilerfolg darzustellen.
## Deine Mission
### Aufgabe A: Entwerfe die erfolgreiche Ergebnisantwort
Nimm an, der Agent Node B hat die JSONPlaceholder-Antwort aus dem Output-Zustand 1 erhalten. Schreibe die genaue Antwort, die Agent Node B in natürlicher Sprache auf die folgende Consultant-Query erzeugen sollte:
> „Kannst du den aktuellen Engagement-Status für Account-Referenz 1 prüfen?“
Deine Antwort muss die folgenden Anforderungen erfüllen:
- Die wichtigsten Informationen aus dem JSON-Output in natürlicher, professionell formulierter Sprache darstellen, passend für Meridians Consulting-Umfeld
- Die rohe JSON-Struktur oder Feldnamen nicht in der Antwort reproduzieren
- Die operativ relevantesten Felder enthalten, etwa Engagement-Referenz, Name und aktiver oder geschlossener Status
- Mit einem kurzen Angebot enden, bei Bedarf weitere Details oder Unterstützung bereitzustellen
Diese Aufgabe testet deine Fähigkeit, die Art von Antwort zu schreiben, die ein gut gestalteter Agent erzeugen würde, bevor du die Anweisung schreibst, die sie erzeugt.
### Aufgabe B: Die Anweisungen zur Ergebnisbehandlung schreiben
Entwirf eine System-Prompt-Anweisung für Agent Node B, die ihm genau sagt, wie er sich verhalten soll, wenn der HTTP Node einen Fehlerzustand zurückgibt.
Entwirf eine System-Prompt-Anweisungen für den Agent Node B, die beide Output-Zustände abdecken. Dein Prompt muss spezifizieren:
1. Wie eine erfolgreiche HTTP-Antwort in die Art von natürlichsprachlicher Antwort formatiert werden soll, die du in Aufgabe A entworfen hast (einschließlich welche Felder angezeigt und welche unterdrückt werden sollen).
1. Wie er sich verhalten soll, wenn der HTTP Node einen Fehlerzustand zurückgibt (das sind die drei Anforderungen unten).
Die zwei Abschnitte zusammen ersetzen die bestehende System Message von Agent Node B. Gib dem Modell klar an, welches Verhalten wann gilt.
Deine Anweisung muss die folgenden drei Anforderungen adressieren:
Entwirf eine System-Prompt-Anweisungen für den Agent Node B, die beide Output-Zustände abdecken. Dein Prompt muss genau erklären:
- Den Fehler ehrlich anerkennen: Der Agent Node B darf den Fehler nicht als Erfolg darstellen oder einen erfundenen Status generieren. Der Consultant muss verstehen, dass die Abfrage kein Ergebnis zurückgegeben hat.
- Das relevante Detail kommunizieren: Der Agent Node B sollte in einfacher Sprache erklären, was passiert ist, ohne rohe HTTP-Statuscodes, technische Fehler-Strings oder JSON-Fehlerobjekte offenzulegen, die für einen Consulting Professional nicht aussagekräftig sind.
- Einen klaren nächsten Schritt angeben: Die Anweisung muss detailliert Erläutern, was  der Agent Node B nach der Kommunikation des Fehlers anbieten soll. Zum Beispiel vorschlagen, dass der Consultant sich direkt an seinen Engagement Manager wendet, oder anbieten, stattdessen in Meridians Wissensdatenbank nach verwandten Informationen zu suchen.
### Aufgabe C: Agent Node B aktualisieren und beide Output-Zustände testen
Öffne die Einstellungen von Agent Node B und ersetze die bestehende System Message durch die Anweisungen, die du in Aufgabe B geschrieben hast. Der vorherige Formatter-Prompt wird durch deine neue Version ersetzt, die jetzt sowohl erfolgreiche als auch fehlgeschlagene Lookups behandelt.
Gib deine Failure-Recovery-Anweisung aus der Aufgabe B in die System Message von Agent Node B auf deinem Canvas ein. Führe dann die folgenden zwei Tests in separaten Chat-Sessions aus und dokumentiere die Antworten des Agenten.
Test 1 Erfolgreicher Lookup: „Kannst du den aktuellen Engagement-Status für Account-Referenz 1 prüfen?“
Bewerte die Antwort anhand der Anforderungen in Aufgabe A. Stellt der Agent Node B die Informationen professionell dar? Vermeidet er rohe JSON-Feldnamen? Identifiziert er die operativ relevantesten Informationen?
Test 2 Simulierter HTTP-Fehler: „Kannst du den Status für Engagement ENG-9999 abrufen?“
Um einen Fehler zu simulieren, ändere vorübergehend die Target URL des HTTP Nodes auf einen ungültigen Endpunkt:
```json
https://jsonplaceholder.typicode.com/invalid/endpoint/9999
```
Dies gibt eine 404-Antwort zurück. Speichere den Canvas und sende: „Kannst du den Engagement-Status für den Bauer-Account prüfen?“
Bewerte die Antwort anhand der Anforderungen aus Aufgabe B. Erkennt der Agent Node B den Fehler an, ohne einen Status zu erfinden? Kommuniziert er in einfacher Sprache, was passiert ist? Bietet er einen klaren nächsten Schritt an?
Stelle die HTTP-Node-URL nach dem Testen wieder her:
```json
https://jsonplaceholder.typicode.com/todos/1
```
Wenn einer der Tests eine unzureichende Antwort erzeugt, identifiziere, welcher Teil der System-Prompt-Anweisung nicht das erwartete Verhalten erzeugt hat, und überarbeite ihn. Führe den Test nach jeder Überarbeitung erneut aus und dokumentiere, was sich geändert hat.
### Aufgabe D: Einen vollständigen API-Ausfall simulieren
Ändere die Target URL des HTTP Nodes auf eine Domain, die nicht existiert: https://api.meridian-internal-nonexistent.com/engagements/status
Speichere den Canvas und sende: Kannst du den Engagement-Status für den Krauss-Account prüfen?
Beobachte und dokumentiere die Antwort von Agent Node B. Bewerte, ob die aktuelle System-Prompt-Anweisung einen vollständigen Verbindungsfehler anders behandelt als eine 404-Not-Found-Antwort.
> Worüber du nachdenken solltest: Eine 404-Antwort gibt einen strukturierten HTTP-Fehler mit einem Statuscode zurück. Ein vollständiger Verbindungsfehler gibt überhaupt keine Antwort zurück. Flowise erhält einen Netzwerkfehler und gibt ihn als generischen Fehler-String nachgelagert weiter. Das sind zwei unterschiedliche Fehlermodi, die selbst mit derselben System-Prompt-Anweisung unterschiedliches Agentenverhalten erzeugen können.
Stelle die HTTP-Node-URL nach dem Testing wieder her auf: https://jsonplaceholder.typicode.com/todos/1

> 💡 Takeaway: 
  Ein Tool, das korrekt ausgeführt wird, ist nicht dasselbe wie ein Agent, der Tool-Ergebnisse gut behandelt. Die Lücke zwischen einem Fehler, den der HTTP Node zurückgibt, und einer professionellen Reaktion von Agent Node B auf diesen Fehler wird vollständig durch den System-Prompt gesteuert.
  Klare Anweisungen sowohl für erfolgreiche Ergebnisintegration als auch für Failure Recovery sind der Unterschied zwischen einem Agenten, der unter realen Bedingungen zuverlässig funktioniert, und einem, der Selbstsicherheit erfindet, wenn er Unsicherheit anerkennen sollte.
