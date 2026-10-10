# Warum Agenten strukturierte Kommunikation brauchen

Notion page: https://app.notion.com/p/Warum-Agenten-strukturierte-Kommunikation-brauchen-c539418319f3836ca161817f320d5f74
Backed up before n8n migration

> OpenRouter statt Gemini verwenden
  Einige AI-Kursmaterialien zeigen möglicherweise ein direktes Gemini-Setup in Tools wie n8n, Flowise oder Cursor. In diesem Programm verwendest du stattdessen deinen von Masterschool bereitgestellten OpenRouter-Key. Die Workflow-Logik bleibt gleich, aber die Modellverbindung kann sich ändern.
  Lies vor dem Start den Setup-Guide: How-To: OpenRouter statt Gemini verwenden

Sofia macht den ersten End-to-End-Test der neuen Support-Automatisierung von Cascadia Outfitters. Eine Kundennachricht kommt rein: „My order arrived damaged, I have a two-year warranty — can you replace it?" Sofias Kundenservice-Agent erkennt das als Garantiefall und gibt sie an den Warranty-Agent weiter, der beim Compliance-Team von Cascadia liegt. Der Warranty-Agent scheitert lautlos. Beide Agenten funktionieren für sich genommen einwandfrei. Kaputt ist die Nachricht zwischen ihnen: Sofias Agent sendet order_id, der Warranty-Agent erwartet orderNumber. Gleiche Information, anderes Label. Der Warranty-Agent schaut sich an, was ankommt, findet die Felder nicht, die er braucht, und gibt eine leere Antwort zurück.
Genau das muss Sofia zuerst lösen, bevor Cascadia irgendeinen Multi-Agent-Workflow live schalten kann: dafür sorgen, dass die Agenten zuverlässig miteinander reden. Diese Lektion zeigt dir, warum das einen Kommunikationsvertrag braucht, was so ein Vertrag ist und was ohne ihn kaputtgeht.
## Ein Beispiel: eine AI-gestützte Anfrage
Lena schickt folgende Anfrage ins System: „Analyze this month's returns data and send me a summary." Für einen Menschen sind die Schritte sofort klar:
1. Auf die Rückgabedaten zugreifen.
1. Sie analysieren.
1. Eine Zusammenfassung schreiben.
1. Das Ergebnis verschicken.
Ein AI-System kann diese Schritte auch erledigen, aber nur, wenn jede Komponente weiß, welche Informationen sie bekommt, welche sie zurückgibt und in welchem Format. Fehlen klare Kommunikationsregeln, wird das System schnell unzuverlässig.
## Ein einfaches Kommunikationsproblem
Zwei Agenten im Support-System von Cascadia:
- Der Order-Lookup-Agent: ruft Details zu einer bestimmten Bestellung ab.
- Der Warranty-Agent: entscheidet, ob ein Garantiefall abgedeckt ist, und formuliert eine Antwort.
![image]((notion-hosted file))
Der Warranty-Agent erwartet:
```json
{
  "month": "May",
  "revenue": 125000
}
```
Der Order-Lookup-Agent sendet aber:
```json
{
  "sales_month": "May",
  "total_sales": 125000
}
```
Beide Nachrichten enthalten dieselbe Information. Trotzdem scheitert der Warranty-Agent, weil er die erwarteten Felder nicht findet. Kommunikation, nicht Intelligenz, ist hier das Problem.
![image]((notion-hosted file))
## Was ein Kommunikationsvertrag ist
Ein Kommunikationsvertrag ist eine Vereinbarung zwischen Komponenten. Er legt fest:
[TABLE]
  | Element | Beispiel |
  | Eingabeformat | JSON |
  | Pflichtfelder | month, revenue |
  | Datentypen | text, number |
  | Erwartetes Verhalten | Zusammenfassung zurückgeben |
  | Fehlerbehandlung | Fehlermeldung zurückgeben |
> 💡 
  Der Vertrag beschreibt nur, was reingeht und was rauskommt, nicht wie die Komponente intern arbeitet.
Kurz gesagt:
  > „If you send me this, I will return that."
  Dadurch können verschiedene Komponenten zusammenarbeiten, ohne die interne Implementierung der jeweils anderen kennen zu müssen.
## Warum Verträge wichtig sind
Stell dir vor, ein Team bei Cascadia baut eine neue Version des Order-Lookup-Agenten. Die Entwickler:innen benennen das Feld revenue in total_revenue um, weil sie das klarer finden. Klingt nach einer kleinen, harmlosen Änderung. Der Warranty-Agent erwartet aber weiterhin ein Feld namens revenue. Sobald die neue Version live geht, bricht der Workflow.
Solche Probleme häufen sich, sobald Systeme wachsen. Unterschiedliche Teams bauen unterschiedliche Komponenten, Agenten entwickeln sich weiter, neue Tools kommen zu bestehenden Workflows dazu. Ohne gemeinsamen Kommunikationsstandard riskiert jede Änderung, dass eine Komponente eine andere nicht mehr versteht.
Kommunikationsverträge senken dieses Risiko, weil sie eine klare Vereinbarung zwischen Komponenten schaffen. Solange ein Agent sich an den Vertrag hält, kann sich seine interne Umsetzung ändern, ohne den Rest des Systems zu beeinflussen. Ein Team kann einen Agenten verbessern, eine Datenbank austauschen oder ein neues Tool einbauen, ohne dass alle anderen Komponenten neu geschrieben werden müssen.
Verträge machen auch die Fehlersuche einfacher. Wenn etwas schiefläuft, prüfen Entwickler:innen zuerst, ob die gesendete Nachricht dem vereinbarten Format entspricht. Statt das ganze System zu durchsuchen, konzentrieren sie sich auf genau die Stelle, an der der Vertrag gebrochen wurde.
Dasselbe Prinzip kennst du von APIs. Eine API verlangt nicht, dass du verstehst, wie ein Service intern funktioniert. Du musst nur wissen, welche Informationen du sendest und welche Antwort du erwarten kannst. Bei Agenten läuft die Kommunikation nach demselben Muster.
## Verständnischeck
### Frage 1
>  Was ist der Hauptzweck eines Kommunikationsvertrags?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/140275a8-e1b7-413e-840c-ad49de56e90a
### Frage 2
>  Sofias Order-Lookup-Agent läuft erfolgreich durch und sendet seine Ausgabe an den Warranty-Agent. Der Warranty-Agent läuft ebenfalls erfolgreich durch, gibt aber eine leere Antwort zurück. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/85cf10fe-77db-47ea-8b28-a519fbcea4a1
### Frage 3
>  Ein Kommunikationsvertrag zwischen zwei Agenten legt typischerweise fest:
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a3140898-e8ff-41a1-8098-dd435177ee26
## Zusammenfassung
Cascadias Support-Automatisierung scheitert nicht an einem einzelnen fehlerhaften Agenten, sondern daran, dass sich zwei Agenten nicht über die Form der ausgetauschten Nachricht einig sind. Strukturierte Kommunikation, also ein Vertrag zwischen Komponenten, macht Multi-Agent-Systeme zuverlässig genug für den Produktivbetrieb.
In der nächsten Lektion schauen wir uns an, wie solche Verträge in der Praxis aussehen: wenn Sofia den konkreten Handoff zwischen dem Kundenservice-Agenten und den nachgelagerten Spezialagenten gestaltet.