# Fallback-Muster

Notion page: https://app.notion.com/p/Fallback-Muster-da09418319f382fcb8a8011e85010604
Backed up before n8n migration

Timeouts verhindern, dass der Workflow ewig wartet. Retries geben ihm eine zweite Chance. Aber manche Fehler sind nicht temporär und erholen sich auch bei einem Retry nicht. Die Warranty-Datenbank ist wegen Wartungsarbeiten offline. Oder die Anfrage eines Kunden lässt sich von keinem einzelnen Spezialisten beantworten. Was soll der Workflow dann tun? Einfach scheitern? Sofia weiß, was das bedeutet: Ein Kunde wartet. Ein Agent wirkt kaputt. Lena muss manuell eingreifen.
Genau hier kommt das dritte Resilienz-Pattern ins Spiel: der Fallback. Ein alternativer Pfad, den der Workflow nimmt, wenn der bevorzugte Pfad nicht klappt.
## Was ist ein Fallback?
Ein Fallback ist ein alternativer Pfad. Du nutzt ihn, wenn der bevorzugte Pfad die Aufgabe nicht zuverlässig abschließen kann.
In einem Agenten-Workflow ist der Hauptpfad normalerweise die beste Option: das leistungsfähigste Modell, das genaueste Tool oder der vollständigste Prozess. Scheitert dieser Pfad, sollte der Workflow trotzdem nicht immer zusammenbrechen. Ein Fallback gibt dem System eine weitere sichere Option.
Cascadias Order Lookup Agent versucht zuerst, die Live-Bestelldatenbank über ein verbundenes Tool abzufragen. Ist dieses Tool durch Rate Limiting eingeschränkt oder nicht verfügbar, wechselt der Workflow auf einen Fallback-Pfad. Zum Beispiel gibt er den zuletzt zwischengespeicherten Bestellstatus zurück, mit dem Hinweis, dass die Daten ein paar Minuten alt sein können.
Der Fallback bleibt ehrlich: Er liefert die beste sichere Antwort, die unter den aktuellen Bedingungen möglich ist.
## Timeout, Retry und Fallback
Diese drei Patterns hängen zusammen, lösen aber unterschiedliche Probleme.
[TABLE]
  | Pattern | Zentrale Frage | Was es tut |
  | Timeout | „Wie lange sollten wir warten?“ | Stoppt einen Schritt, der zu lange dauert. |
  | Retry | „Sollten wir denselben Pfad erneut versuchen?“ | Wiederholt dieselbe Aktion, wenn der Fehler temporär sein könnte. |
  | Fallback | „Was sollten wir stattdessen tun?“ | Wechselt zu einem alternativen Pfad, wenn der Hauptpfad nicht zuverlässig ist. |
Ein Timeout schützt den Workflow davor, ewig zu warten. Ein Retry gibt demselben Pfad eine weitere Chance. Ein Fallback ändert die Strategie.
## Warum Fallback wichtig ist
Ohne Fallback-Logik hat ein Workflow oft nur zwei Ergebnisse: Erfolg oder Fehler. Das ist für reale Systeme zu fragil.
Ein Fallback-Pattern schafft eine mittlere Option. Das System kann den idealen Pfad vielleicht nicht abschließen, aber trotzdem nützlich, sicher und transparent antworten.
Ein Beispiel dazu:
Cascadias Warranty Agent versucht, den Warranty-Records-Service zu erreichen. Die Anfrage scheitert, weil der Service nicht verfügbar ist. Der Workflow versucht es zweimal erneut. Der Service scheitert weiterhin. Statt endlos weiterzulaufen oder eine verwirrende Fehlermeldung zurückzugeben, wechselt der Workflow auf einen Fallback-Pfad. Er schickt dem Kunden eine Bestätigung, dass sich ein Spezialist innerhalb eines Werktags manuell meldet.
Das macht die Erfahrung für den User besser und für das System sicherer.
## Häufige Fallback-Optionen
Ein Fallback kann je nach Aufgabe unterschiedliche Formen annehmen.
Eine Option ist ein einfacherer Modellpfad. Nutzt der Hauptagent ein Tool und das Tool fällt aus, kann der Workflow zu einer reinen Modellantwort wechseln, mit einer klaren Einschränkung dazu.
Eine andere Option ist ein anderes Tool. Ist ein Such-Tool nicht verfügbar, kann der Workflow eine andere Quelle versuchen.
Eine dritte Option ist eine Nachricht an den User, die erklärt, wie es weitergeht. Kann das System nicht sicher fortfahren, sollte es sagen, was passiert ist und was der User als Nächstes tun kann.
Wichtig dabei: Der Fallback muss bewusst gestaltet sein. Er darf den Fehler nicht verstecken oder Ergebnisse erfinden.
## Wie Fallback in einen Loop passt
Fallbacks werden oft nach Retries genutzt.
Eine häufige Struktur sieht so aus:
Beginne mit dem Hauptagenten. Prüfe, ob das Ergebnis gültig ist. Zeigt das Ergebnis einen temporären Fehler, versuche denselben Pfad erneut. Erreicht der Workflow das Retry-Limit, hör auf, es erneut zu versuchen, und wechsle zum Fallback-Pfad.
Das verhindert Endlosschleifen. Gleichzeitig vermeidet es, zu früh aufzugeben.
## Schnelle Entscheidungsregel
Nutze einen Timeout, wenn das System zu lange wartet.
Nutze einen Retry, wenn derselbe Pfad beim nächsten Versuch wahrscheinlich funktioniert.
Nutze einen Fallback, wenn derselbe Pfad oft genug gescheitert ist oder nicht sicher vertrauenswürdig ist.
Ein resilienter Workflow kombiniert oft alle drei: Timeout begrenzt die Wartezeit, Retry fängt temporäre Probleme ab, und Fallback sorgt für Erholung, falls der Hauptpfad die Aufgabe nicht schafft.
## Quiz
### Frage 1
>  Ein Agent ruft ein Tool auf, aber das Tool braucht zu lange für eine Antwort. Welches Pattern behandelt diese Situation direkt?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/39b09fb7-59ab-4404-9a2f-2d3034071805
### Frage 2
>  Ein Archiv-Such-Tool gibt einen Rate-Limit-Fehler zurück. Der Workflow sendet dieselbe Anfrage nach kurzer Wartezeit erneut. Welches Pattern wird verwendet?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/992114ed-4e69-4816-9395-7c29c9046098
### Frage 3
>  Ein Workflow versucht einen fehlgeschlagenen Tool-Aufruf dreimal erneut. Nach dem dritten Fehlschlag wechselt er zu einer einfacheren Antwort, die dem User die Einschränkung erklärt. Welches Pattern ist dieser finale Wechsel?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/0236274d-9190-48fc-9ad9-0667e14308a2
### Frage 4
>  Warum sollte eine Fallback-Antwort transparent sein?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/da213826-716d-4460-b3c5-0535774775f4
### Frage 5
>  Welches Workflow-Design ist am resilientesten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d2d8e4e1-cfa7-4348-a689-f61ddd1829df
## Zusammenfassung
Fallback-Muster erhöhen die Resilienz von Agenten-Workflows, wenn der primäre Pfad eine Aufgabe nicht erfolgreich abschließen kann. Ein Timeout begrenzt die maximale Wartezeit. Ein Retry stößt einen erneuten Versuch auf demselben Pfad an. Ein Fallback wechselt die Strategie, sobald das Festhalten am ursprünglichen Weg keinen Sinn mehr macht. Zusammen machen diese drei Muster orchestrierte Systeme zuverlässiger und robuster und stärken das Vertrauen der Endanwender.