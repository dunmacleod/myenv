# Warum Agenten Memory brauchen

Notion page: https://app.notion.com/p/Warum-Agenten-Memory-brauchen-3779418319f380dab477d2b489bf6840
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Warum zustandslose AI-Modelle - also Modelle ohne die Fähigkeit, Informationen aus früheren Nachrichten zu speichern – echte Geschäftsgespräche nicht allein bewältigen können und was Memory (das Gedächtnis eines KI-Systems) daran verändert.

## Das Ausgangsproblem
Contigo GmbH ist ein Finanzdienstleister mit Sitz in München, der in Deutschland, Österreich und den Niederlanden tätig ist. Das Unternehmen hat gerade einen AI-Support-Agenten eingeführt, der Kundenanfragen zu Kontoverwaltung, Kreditanträgen und Dokumenteneinreichungen bearbeiten soll.
Die erste Woche läuft schlecht. Kunden geben ihre Kontonummern an und werden zwei Nachrichten später gebeten, sie zu wiederholen. Kreditsachbearbeiter erhalten unvollständige Zusammenfassungen, weil der Agent frühere Details vergessen hat. Ein Kunde schließt sein Konto, nachdem er in einem einzigen Gespräch dreimal nach demselben Dokument gefragt wurde.
Das Problem ist nicht das Sprachmodell. Das Problem sind nicht die Prompts. Das Problem ist, dass der Agent kein Memory hat. Ohne Gedächtnis kann selbst ein intelligenter Agent nicht zuverlässig arbeiten.

## Warum Sprachmodelle standardmäßig zustandslos sind
Ein Large Language Model (LLM) verarbeitet den exakten Text, den es in einer bestimmten Anfrage erhält, erzeugt eine Antwort und verwirft anschließend sofort alles. Es hat keinen eingebauten Datensatz früherer Nachrichten. Wenn ein Nutzer das nächste Mal eine Nachricht sendet, behandelt das Modell sie so, als wäre es die allererste Interaktion, die es jemals mit dieser Person hatte.
Das nennt man zustandslos. Zustandslos bedeutet, dass es keinen persistenten Datensatz darüber gibt, was zuvor passiert ist. Jede Anfrage ist isoliert, wird unabhängig verarbeitet und in dem Moment vergessen, in dem eine Antwort erzeugt wird. Das ist die standardmäßige Funktionsweise von Large Language Models. Die Architektur ist für Single-Turn-Interaktionen ausgelegt, nicht für laufende Geschäftsworkflows.
Die Konsequenz für Contigo ist eindeutig. Jedes Mal, wenn ein Kunde eine neue Nachricht sendet, beginnt der Agent von vorn. Er hat keinen Zugriff darauf, was vor fünf Sekunden gesagt wurde, geschweige denn vor fünf Tagen. Er kann keinen Fortschritt verfolgen, keine redundanten Fragen vermeiden und nicht auf früherem Kontext aufbauen.

## Wie zustandslose Agenten in der Praxis aussehen
Schauen wir uns ein Beispiel an. Ein Contigo-Kunde möchte seine Rechnungsadresse aktualisieren. Das Gespräch könnte so ablaufen:
> Kunde: Meine Kontonummer ist DE-4892. Ich muss meine Rechnungsadresse aktualisieren.
> Agent: Natürlich, ich kann Ihnen dabei helfen. Könnten Sie bitte Ihre Kontonummer angeben?
Der Kunde hat sie bereits angegeben. Der Agent hat sie bereits erhalten. Aber weil das Modell jede Nachricht isoliert verarbeitet hat, ist die Kontonummer aus der ersten Nachricht verschwunden, sobald der Agent seine Antwort formuliert. Das Ergebnis ist ein frustrierendes Support-Erlebnis, weil der Agent wichtige Informationen nicht behalten kann.
Dieses Muster wiederholt sich in jedem Multi-Turn-Workflow, etwa bei Kreditanträgen, Anfragen zu Compliance-Dokumenten und Onboarding-Sequenzen. Jeder Prozess, der mehr als einen Austausch erfordert, ist in dem Moment beeinträchtigt, in dem Memory fehlt.

## Was Memory verändert
Das Hinzufügen einer Memory-Komponente gibt dem Agenten Zugriff auf das, was bereits gesagt wurde. Der Gesprächsverlauf wird außerhalb des Modells gespeichert und in jeden neuen Prompt zurückinjiziert, sodass das Modell über den vollständigen Kontext nachdenken kann, statt nur über die neueste Nachricht. Das macht Multi-Turn-Geschäftsgespräche überhaupt erst möglich.
[TABLE]
  | Turn | Ohne Memory | Mit Memory |
  | Turn 1 | Kunde gibt Kontonummer an. Agent antwortet. Daten werden verworfen. | Kunde gibt Kontonummer an. Memory speichert sie. Agent antwortet. |
  | Turn 2 | Kunde bittet darum, die Adresse zu aktualisieren. Agent fragt erneut nach der Kontonummer. | Kunde bittet darum, die Adresse zu aktualisieren. Memory injiziert die Kontonummer. Agent fährt korrekt fort. |

> 💡 Memory verwandelt einen zustandslosen Textgenerator in einen Agenten, der ein echtes Gespräch führen, einen Workflow verfolgen und einen Kunden betreuen kann, ohne ihn zu zwingen, sich zu wiederholen.

## Verständnis prüfen
>  Ein Contigo-Support-Agent fragt einen Kunden im selben Gespräch zweimal nach seiner Kontonummer. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b00615ab-8c43-42dd-9cda-a2021e0994da

> 💡 Takeaway: 
  Memory ist das, was einen zustandslosen Textgenerator von einem Agenten unterscheidet, der ein echtes Gespräch führen kann. Ohne Memory kann kein Multi-Turn-Geschäftsworkflow zuverlässig funktionieren.
