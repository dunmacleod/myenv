# Observability und System-Monitoring

Notion page: https://app.notion.com/p/Observability-und-System-Monitoring-3779418319f38082a41ed363c770b3cb
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du verstehst, warum klassisches Software-Monitoring für KI-Agenten nicht ausreicht. Du lernst, was geloggt werden muss, damit ein Agent überhaupt debuggbar ist. Und du erkennst, welche Telemetrie-Signale auf ein Problem hinweisen, das menschliches Eingreifen braucht.

## Das Black-Box-Problem
Der Agent von Contigo GmbH nähert sich der Präsentationsreife. Die Canvas ist konfiguriert, die Tools sind verbunden, die Guardrails stehen, und der System Prompt wurde anhand echter Testergebnisse verfeinert. Sobald der Agent aber öffentlich zugänglich ist und echte Kundeninteraktionen bearbeitet, stellt sich eine neue operative Frage: Woher weiß das Team, wenn etwas schiefläuft?
In klassischer Software erzeugt ein Fehler einen Stack Trace: einen präzisen, deterministischen Nachweis genau dazu, welche Funktion in welcher Zeile mit welchem Input versagt hat. Der Fix lässt sich lokalisieren und reproduzieren. Ein KI-Agent versagt anders. Eine Pipeline kann durchlaufen, ohne einen einzigen Fehler zu werfen, und trotzdem eine völlig falsche Antwort liefern. Zum Beispiel eine mit einer erfundenen regulatorischen Zahl, dem falschen aufgerufenen Tool oder einer komplett ignorierten Grounding-Anweisung. Es wird keine Exception ausgelöst. Kein Alert feuert. Der Kunde bekommt falsche Informationen, und das Monitoring-Dashboard zeigt eine erfolgreiche Ausführung an.
Das ist das Black-Box-Problem. Und die Lösung heißt Observability: tiefe, strukturierte Einsicht in die Gründe für jede Entscheidung des Agenten, nicht nur ob die Pipeline gelaufen ist.
## Was Flowise bereits eingebaut mitbringt
Bevor wir zu den Anforderungen an Produktiv-Observability kommen, lohnt sich ein Blick darauf, was deine lokale Flowise-Instanz schon mitbringt.
- Chat History: Jeder Gesprächsturn wird geloggt und ist im Chatflow-Einstellungspanel unter View Messages einsehbar. Du kannst den genauen Austausch zwischen Kunde und Agent für jede Session nachvollziehen, gefiltert nach Session ID.
- Execution Traces: Ist Return Source Documents am Tool-Agent-Node aktiviert, zeigt Flowise für jeden Turn, welche Chunks abgerufen und welche Tools aufgerufen wurden. Das gibt dir während des Testens einen grundlegenden Einblick in Tool-Auswahl und Retrieval-Verhalten des Agenten.
- Analytics-Integrationen: Flowise unterstützt Integrationen mit Observability-Plattformen wie Arize, Phoenix, LangWatch, Langfuse, Lunary und Opik für tiefere Telemetrie-Erfassung. Diese gehen über das hinaus, was die eingebaute Oberfläche zeigt, und sind der Ausgangspunkt für produktionsreife Observability.
Diese eingebauten Funktionen reichen für den Kurs-Build und die Sprint-4-Präsentation aus. Für ein Produktivdeployment mit Hunderten gleichzeitigen Kundensessions reichen sie nicht.
## Was geloggt werden muss
Jeder Agent-Aufruf in einem Produktivdeployment sollte einen strukturierten Trace mit einer eindeutigen Trace ID erzeugen. Vier Kategorien von Telemetrie sind dabei unverzichtbar.
- Vollständiges Prompt- und Response-Logging: Der exakte Text, der an das Sprachmodell geschickt wird, und die rohe Antwort müssen geloggt werden. Das schafft die Grundlage dafür, zu vergleichen, was das Modell gefragt wurde und was es tatsächlich geliefert hat. Ohne das lässt sich nicht diagnostizieren, ob ein Fehler am Prompt lag oder am Reasoning des Modells. Eine falsche Antwort kann an einem schlecht formulierten System Prompt liegen, an einer mehrdeutigen Anfrage oder an einem Reasoning-Fehler des Modells. Das sind drei unterschiedliche Ursachen, die drei unterschiedliche Lösungen brauchen.
- Retrieved-Chunk-Logging: Fragt der Agent die Wissensdatenbank ab, müssen die exakten zurückgegebenen Dokument-Chunks zusammen mit der auslösenden Anfrage geloggt werden. Eine falsche Antwort kann an einem Retrieval-Fehler liegen statt an einem Generation-Fehler. Ohne das Logging des abgerufenen Inhaltes lassen sich diese beiden Fehlerarten allein aus dem Output nicht unterscheiden. Nennt der Agent ein falsches Kreditlimit, zeigt das Chunk-Log genau, woran es lag. Vielleicht enthielt die Wissensdatenbank veralteten Inhalt, vielleicht hat der Abruf die falschen Chunks zurückgegeben, oder das Modell hat den abgerufenen Inhalt ignoriert und stattdessen aus Trainingsdaten generiert.
- Tool-Call- und Result-Logging: Jeder Tool-Aufruf muss geloggt werden, inklusive Tool-Name, den exakt übergebenen Parametern, dem zurückgegebenen Response- oder Error-Code und der Execution Latency. Hohe Tool-Fehlerraten und fehlerhafte Parametermuster lassen sich beide aus diesen Daten diagnostizieren. Ein Loan-Status-Tool, das bei 15 % der Anfragen still versagt, bleibt ohne dieses Log unsichtbar. Mit ihm lässt sich das Fehlermuster erkennen.
- Reasoning-Trace-Logging: Die interne Gedankenkette des Agenten, also die Thought-Action-Observation-Sequenz aus dem ReAct Loop, muss erfasst werden. So können Entwickler die Logik des Agenten Schritt für Schritt nachvollziehen und genau erkennen, wo das Reasoning vom gewünschten Verhalten abgewichen ist. Ein Tool-Routing-Fehler, der im Output-Log zufällig wirkt, zeigt im Reasoning Trace oft ein klares Muster. Meist ist es eine bestimmte Formulierung in der Anfrage, die konsequent die falsche Invocation Condition auslöst.
## Signale, die ein Eingreifen erfordern
Die laufende Analyse geloggter Traces macht Muster sichtbar, die auf systemische Probleme hindeuten und menschliche Aufmerksamkeit brauchen. Die folgenden Signale sollten eine Überprüfung auslösen, bevor sie Kunden in großem Umfang erreichen.
[TABLE]
  | Signal | Was es bedeutet | Wahrscheinliche Ursache |
  | Retrieval liefert konsistent niedrige Similarity Scores | Inhalt der Wissensdatenbank passt nicht zu den Anfragemustern | Chunking-Strategie passt nicht oder Dokumente sind veraltet |
  | Tool-Fehlerrate über 5 % | Instabiler Tool-Endpoint oder Fehler bei der Parameterextraktion | API-Zuverlässigkeitsproblem oder Invocation Condition zu breit |
  | Fallback-Phrase löst bei Anfragen im Scope aus | Grounding-Anweisung zu restriktiv oder Abruf findet relevanten Inhalt nicht | System Prompt zu stark eingeschränkt oder Lücke in der Wissensdatenbank |
  | Token-Kosten pro Session steigen über die Zeit | Context Window sammelt sich an, Sliding Window begrenzt nicht effektiv | Window Size zu groß oder Retrieval injiziert zu viele Chunks |
  | Reasoning Trace zeigt wiederholte Tool-Re-Invocations | Tool-Output befriedigt den Reasoning Loop des Modells nicht | Tool-Beschreibung passt nicht oder Max Iterations zu hoch |
  | Grounding-Anweisung wird in späten Turns ignoriert | Context Drift, Aufmerksamkeit für den System Prompt verdünnt sich mit wachsendem Verlauf | Window Size zu groß im Verhältnis zur Session-Länge |
## Was Observability zeigt, was Testing nicht kann
Das End-to-End-Testskript validiert den Agenten unter kontrollierten Bedingungen mit bekannten Anfragen. Produktions-Observability zeigt dagegen, was unter unkontrollierten Bedingungen mit echten Kundenanfragen passiert. Dazu gehört der Long Tail an Anfragemustern, Grenzfälle und Fehlermodi, die ein Testskript nicht vorhersehen kann.
Drei Kategorien von Produktionsfehlern lassen sich nur durch Observability erkennen:
- Silent Degradation: Die Antwortqualität des Agenten sinkt schrittweise, wenn die Wissensdatenbank veraltet oder sich Anfragemuster verschieben. Keine einzelne Antwort wirkt offensichtlich falsch. Sichtbar wird die Verschlechterung nur in aggregierten Qualitätsmetriken über mehrere Wochen hinweg.
- Intermittent Failures: Ein Tool schlägt bei 3 % der Aufrufe unter bestimmten Lastbedingungen fehl. Beim Testen funktioniert das Tool immer. In Produktion bleibt das Muster ohne Failure-Rate-Logging über Tausende Sessions hinweg unsichtbar.
- Prompt-Injection-Varianten: Neuartige Injection-Formulierungen, die die Deny List des Moderation Node passieren, tauchen zuerst im Reasoning Trace auf. Erst danach fängt sie der System Prompt ab. Ohne Trace-Logging bleiben diese Beinahe-Treffer unsichtbar, und das erste Anzeichen für ein Problem ist dann ein erfolgreicher Kompromiss statt ein erkannter Versuch.
## Verständnischeck
>  Contigos Monitoring-Dashboard zeigt für jede Session eine erfolgreich abgeschlossene Agent-Pipeline mit normaler Latenz. Kunden-Feedback zeigt aber, dass der Agent bei etwa jeder achten Interaktion falsche Kreditlimits nennt. Welche Art von Monitoring-Fähigkeit würde die Ursache dieses Fehlers am direktesten aufdecken?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/9a613b62-933a-4b64-a90a-62af242f1e10


> 💡 Fazit:
  Einen KI-Fehler, den du nicht siehst, kannst du nicht beheben. Standard-Infrastruktur-Monitoring bestätigt, dass die Pipeline gelaufen ist. Observability bestätigt, dass sie korrekt gelaufen ist.
  Das Logging von vollständigen Prompts, abgerufenen Chunks, Tool Calls und Reasoning Traces macht aus einem undurchsichtigen Agenten ein debugbares System. In diesem System hat jede falsche Antwort eine nachvollziehbare Ursache.
