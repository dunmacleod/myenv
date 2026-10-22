# State-Handoff zwischen Agenten entwerfen

Notion page: https://app.notion.com/p/State-Handoff-zwischen-Agenten-entwerfen-24c9418319f38374b9f9819864d9df1c
Backed up before n8n migration

Die Vela-Canvas klassifiziert jede eingehende Anfrage in eine von drei Kategorien: commercial, technical oder hybrid. Wenn der Classifier sauber läuft und das Modell einen gültigen Enum-Wert zurückgibt, routet der Condition-Node korrekt und der richtige Spezialagent antwortet. Aber der Classifier läuft nicht immer sauber.
Manchmal gibt das Modell eine Antwort zurück, die nicht zum Structured-Output-Schema passt. Das passiert etwa, wenn die Anfrage mehrdeutig ist, zu kurz zum Klassifizieren, oder so formuliert, dass das Modell sie nicht sicher interpretieren kann. In diesem Fall bleibt der Schlüssel query_type auf seinem Standardwert unclassified. Der Condition-Node hat dann keinen passenden Branch. Ohne Fallback hat die Canvas keinen sicheren Pfad. Die Kundenanfrage wird entweder still verworfen oder falsch geroutet, je nachdem, welchen Wert der State-Schlüssel gerade zufällig noch enthielt.
Das ist der Fehlermodus des veralteten Routings aus der vorherigen Lektion, angewendet auf eine echte Canvas. Er wird der vierte Branch im Condition-Node sein. Aber was dieser Branch genau tun soll, ist eine architektonische Entscheidung: Das System muss dem Kunden sicher antworten, ohne so zu tun, als hätte eine Klassifizierung stattgefunden.
Starte mit deiner Kopie der Sprint-2-Canvas (der Multi-Agent-Canvas mit Classifier + Commercial / Technical / Hybrid Handler, die du im letzten Sprint gebaut hast).
## Was State Recovery hier bedeutet
State Recovery heißt hier nicht, einen fehlgeschlagenen Run neu zu starten oder einen früheren Canvas-Zustand wiederherzustellen, sondern einen Pfad zu entwerfen, den das System nehmen kann, wenn der State, von dem es abhängt (query_type), nicht in nutzbarer Form angekommen ist.
Der Condition-Node ist der Consumer von query_type. Er hat drei Branches: commercial, technical und hybrid. Jeder Branch geht davon aus, dass der Classifier einen gültigen Wert geschrieben hat. Wird diese Annahme verletzt, weil query_type zum Beispiel unclassified ist, haben die drei Branches nichts zum Matchen, und die Canvas bleibt stehen.
Das Recovery-Muster ist ein expliziter vierter Branch, der unclassified abfängt und zu einer sicheren Antwort routet. Sicher heißt: Der Kunde bekommt eine Antwort, die Antwort ist ehrlich über die Unsicherheit des Systems, und kein Spezialagent wird für eine nicht klassifizierte Anfrage aufgerufen.
## Schritt 1: Die Canvas öffnen und den Condition-Node finden
Öffne deine Sprint-2-Canvas in Flowise. Klick auf den Condition-Node. Schau dir die bestehenden Branches an. Aktuell gibt es drei Conditions, die jeweils {{ $flow.state.query_type }} prüfen:
[TABLE]
  | Branch | Type | Value 1 | Operation | Value 2 |
  | 0 | String | {{$flow.state.query_type}} | Equal | commercial |
  | 1 | String | {{$flow.state.query_type}} | Equal | technical |
  | 2 | String | {{$flow.state.query_type}} | Equal | hybrid |
Diese Branches decken die erwarteten Ausgaben des Classifier ab. Einen Branch für unclassified gibt es nicht. Das ist der Standardwert von query_type am Start-Node, also der Wert, der übrig bleibt, wenn der Classifier kein gültiges Enum-Ergebnis liefert.
## Schritt 2: Den Fallback-Branch hinzufügen
Füge im Condition-Node einen vierten Branch mit dieser Konfiguration hinzu:
[TABLE]
  | Feld | Wert |
  | Type | string |
  | Value 1 | {{ $flow.state.query_type }} |
  | Operation | equal |
  | Value 2 | unclassified |
![image]((notion-hosted file))
Dieser Branch fängt jeden Run ab, bei dem der Classifier ein unbrauchbares Ergebnis zurückgegeben hat, einschließlich des Standardwerts des Start-Node selbst. Das bedeutet, er fängt auch den Fall ab, in dem der Classifier gar nicht gelaufen ist.
## Schritt 3: Einen Fallback-Direct-Reply-Node hinzufügen
Füge der Canvas einen neuen Direct-Reply-Node hinzu und verbinde ihn mit dem vierten (unclassified) Output des Condition-Node.
![image]((notion-hosted file))
Setz die Nachricht des Direct-Reply-Node auf:
```plain text
I wasn't able to determine the type of your query. Could you rephrase or give me a bit more detail so I can connect you with the right team?
```
Diese Antwort tut drei Dinge: Sie bestätigt dem Kunden, dass seine Anfrage angekommen ist, sie ist ehrlich über die Unsicherheit des Systems, und sie gibt dem Kunden eine klare nächste Aktion. Sie routet nicht zu einem Spezialagenten und tut nicht so, als hätte eine Klassifizierung stattgefunden.
![image]((notion-hosted file))

## Schritt 4: Mit einer mehrdeutigen Anfrage testen
Speicher deine Canvas, öffne den Chat, und schick eine Testnachricht durch die Canvas.
Testnachricht: Hi
Eine Begrüßung mit nur einem Wort gibt dem Classifier sehr wenig Signal zur Klassifizierung.
Erwartetes Verhalten:
1. Der LLM Classifier läuft. Das Modell kann commercial, technical oder hybrid nicht sicher zuweisen. Es gibt unclassified als strukturierten Ausgabewert für query_type zurück.
1. Die Update-Flow-State-Einträge schreiben query_type: "unclassified" in $flow.state.
1. Der Condition-Node wertet alle vier Branches aus. Der vierte Branch matcht.
1. Der Fallback Direct Reply feuert mit der Klärungsnachricht.
Prüf nach dem Run die Flow-State-Werte. So bestätigst du, dass query_type wirklich unclassified enthält.
![image]((notion-hosted file))

## Schritt 5: Mit einer zweiten mehrdeutigen Anfrage testen, dann bestehendes Routing prüfen
Schick eine zweite mehrdeutige Nachricht.
Testnachricht: Can you help me?
Dieselbe Erwartung: Der Fallback Direct Reply feuert, Flow State zeigt query_type: "unclassified".
![image]((notion-hosted file))
Schick anschließend eine klare kommerzielle Anfrage. Damit bestätigst du, dass die drei ursprünglichen Branches weiterhin korrekt funktionieren.
Testnachricht: I'd like to upgrade our plan to premium.
Erwartetes Verhalten: Der Classifier gibt query_type: "commercial" zurück, der Condition-Node routet zum Commercial-Agent, der Fallback Direct Reply feuert nicht.
![image]((notion-hosted file))
Erwartete Ausgabe: Flow State zeigt nach der dritten Testnachricht query_type: "commercial". Die Antwort des Commercial-Agent erscheint im Chat-Panel.
## Was du gebaut hast
Die Canvas hat jetzt einen expliziten Recovery-Pfad für den häufigsten Klassifizierungsfehler: eine Anfrage, die das Modell nicht sicher kategorisieren kann. Gibt der Classifier den Standardwert unclassified zurück, steht der Condition-Node nicht mehr ohne passenden State-Wert und ohne sicheren Ausgang da. Der Fallback-Branch fängt ihn ab, der Direct Reply behandelt den Kunden ehrlich, und die drei ursprünglichen Spezialistenpfade bleiben unverändert.
Das Muster lässt sich verallgemeinern. Hat ein State-Schlüssel einen Standardwert und einen nachgelagerten Consumer, der auf das Überschreiben dieses Werts angewiesen ist, braucht er einen expliziten Recovery-Branch für den Fall, dass das Überschreiben ausbleibt. query_type ist das klarste Beispiel in dieser Canvas, aber dieselbe Logik gilt für jeden Schlüssel, den der Condition-Node liest.
## Achtung!
Der Classifier gibt für sehr kurze Anfragen einen gültigen Enum-Wert zurück. Ist das Modell per Prompt so konfiguriert, dass es immer eine der drei Kategorien als beste Schätzung wählt, kann es auch für "Hi" commercial, technical oder hybrid zurückgeben. Der Fallback-Branch wird dann nie erreicht. Routen deine Testanfragen zu einem Spezialagenten statt zum Fallback, prüf den System-Prompt des Classifier auf Formulierungen wie „always classify" oder „pick the closest category". Der Fallback-Branch ist nur erreichbar, wenn das Modell unclassified zurückgeben darf.
Der Fallback Direct Reply ist mit dem falschen Condition-Output verbunden. Wurde der vierte Branch zwar hinzugefügt, aber versehentlich mit einem bestehenden Spezialagenten verbunden, wirkt die Canvas auf den ersten Blick, als würde sie funktionieren. Tatsächlich bearbeitet aber der falsche Agent die mehrdeutigen Anfragen, nicht der Fallback. Prüf nach Schritt 3 die Canvas-Verkabelung: Schau nach, mit welchem Node der vierte Condition-Output tatsächlich verbunden ist.
Vergessen zu testen, dass bestehende Branches weiterhin funktionieren. Einen vierten Branch hinzuzufügen, bricht die ersten drei nicht automatisch. Trotzdem lohnt sich der Verifikationstest aus Schritt 5. Ein Konfigurationsfehler im Condition-Node kann das Routing für gültige Anfragen unbemerkt brechen, während der Fallback ganz normal weiterläuft. Das passiert zum Beispiel, wenn versehentlich der Wert eines bestehenden Branches geändert wurde.
## Kurzreferenz
[TABLE]
  | Element | Rolle in diesem Walkthrough | Zentrale Einstellung |
  | Condition-Node: Branch | Fängt nicht klassifizierte Anfragen ab | {{ $flow.state.query_type }} equal unclassified |
  | Fallback Direct Reply | Gibt dem Kunden eine sichere Antwort zurück | Klärungsnachricht; kein Spezialagent wird aufgerufen |
  | Start-Node: query_type-Standardwert | unclassified, der Wert, den Branch 4 abfängt | Standardwert im Flow-State-Panel des Start-Node gesetzt |
  | LLM Classifier: Structured Output | Gibt unclassified zurück, wenn keine sichere Kategorie möglich ist | query_type enum: commercial, technical, hybrid, unclassified |
## Zusammenfassung
Der Condition-Node hat jetzt vier Branches statt drei. Der vierte fängt unclassified ab. Das ist der Wert, den query_type enthält, wenn der Classifier eine Anfrage nicht sicher kategorisieren kann. Von dort routet die Canvas zu einem Direct Reply, der dem Kunden ehrlich antwortet, ohne einen Spezialagenten aufzurufen.
Das ist State Recovery auf Designebene: den State-Wert erkennen, der einen Fehler signalisiert, und einen expliziten Pfad dafür bauen. So bleibt die Canvas nie ohne sicheren Ausgang.
Die nächste Lektion überträgt dieses Denken auf dein eigenes Projekt. Die Aufgabe: Du entwirfst die Recovery- und Failure-Isolation-Muster für die State-Architektur deines Projektagenten. Du bestimmst, welche State-Schlüssel Fehlermodi haben, was jeweils die sichere Antwort ist, und wie du verhinderst, dass der Fehler eines Agenten beeinflusst, was der nächste Agent liest.