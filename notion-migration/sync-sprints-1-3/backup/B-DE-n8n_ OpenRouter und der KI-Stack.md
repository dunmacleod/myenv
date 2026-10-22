# n8n, OpenRouter und der KI-Stack

Notion page: https://app.notion.com/p/n8n-OpenRouter-und-der-KI-Stack-3789418319f38044ad03f6374b5df510
Backed up before n8n migration

> 💡 Am Ende dieser Lektion verstehst du: was n8n macht, wie n8n mit OpenRouter zusammenspielt und welche Verantwortung bei der Workflow-Plattform, dem Modell, den Zugangsdaten und späteren Wissens- oder Tool-Integrationen liegt.
## Ausgangssituation
Meridian Consulting möchte einen internen KI-Assistenten bauen, der häufige operative Fragen beantwortet, bei Bedarf Geschäftstools verwendet und später Informationen aus internen Wissensquellen abrufen kann.
Ein nützlicher Agent besteht nicht nur aus einem Sprachmodell. Er braucht eine Umgebung, die Eingaben empfängt, Dienste verbindet, Logik ausführt, Modelle und Tools aufruft und sichtbar macht, was bei einem Fehler passiert ist.
In diesem Kurs ist diese Umgebung n8n.
## Was ist n8n?
n8n ist eine Plattform zur Workflow-Automatisierung. Workflows bestehen aus verbundenen Nodes. Eine Node kann zum Beispiel eine Chat-Nachricht empfangen, eine API aufrufen, Daten transformieren, ein Modell abfragen, ein Tool verwenden oder ein Ergebnis an ein anderes System senden.
In diesem Kurs ist n8n die Orchestrierungsschicht rund um den Agenten. Die Architektur bleibt sichtbar und testbar, statt in einem großen Skript verborgen zu sein.
> 📸 SCREENSHOT-VORSCHLAG: n8n-Übersichtsseite mit der Aktion Create Workflow. Persönliche Workspace-Namen bei Bedarf aus dem Bild entfernen.
## Der Stack in Sprint 1
- n8n — Orchestrierung und Ausführung der Workflows.
- OpenRouter Chat Model — Modellzugriff über den von der Schule bereitgestellten OpenRouter-API-Key.
- Credentials in n8n — sichere Speicherung von API-Keys; Keys gehören nicht direkt in Prompts oder Workflow-Texte.
- AI Agent Node — die Agenten-Komponente, die Anweisungen erhält und ein Modell sowie Tools verwenden kann.
- Tools — Fähigkeiten, die der Agent bei Bedarf aufrufen kann. Im ersten Workflow verwenden wir ein einfaches Tool.
- Wissen und persistentes Memory — kommen in späteren Sprints hinzu.
n8n besitzt eine eigene OpenRouter Chat Model Node. Die verfügbaren Modelle werden dynamisch von OpenRouter geladen. Deshalb können sich Modellnamen ändern, während das Workflow-Muster gleich bleibt.
Offizielle Referenzen:
- n8n OpenRouter Chat Model
- n8n OpenRouter Credentials
## Warum ein visueller Workflow-Builder?
Dasselbe System könnte auch in Python oder JavaScript gebaut werden. In n8n sind die wichtigsten Integrationsschritte jedoch direkt auf dem Canvas sichtbar.
Das bringt Meridian drei Vorteile:
1. Transparenz: Das Team sieht, wie Eingaben von einem Schritt zum nächsten fließen.
1. Debugging: Jede Node zeigt Input, Output und das Ergebnis der Ausführung.
1. Iteration: Modell, Prompt, Tool oder Verzweigung können geändert werden, ohne die gesamte Anwendung neu zu bauen.
Der visuelle Canvas ersetzt kein Architekturverständnis. Er macht die Architektur leichter überprüfbar.
## Wie die Komponenten zusammenhängen
Ein einfacher KI-Workflow wird gleich so aussehen:
Chat Trigger → AI Agent
Der AI Agent erhält zusätzliche Verbindungen:
- OpenRouter Chat Model für Sprachgenerierung und Reasoning.
- Ein Tool, das der Agent aufrufen kann, wenn die Aufgabe es erfordert.
Später kommen Memory, Retrieval, Datenbanken und externe Dienste hinzu.
![image]((notion-hosted file))
## Verantwortlichkeiten sauber trennen
Wenn etwas nicht funktioniert, frage zuerst, zu welcher Schicht das Problem gehört:
- Der Workflow startet nicht → Trigger oder Workflow-Konfiguration.
- Authentifizierung schlägt fehl → Credentials oder Provider.
- Das Modell antwortet unerwartet → Anweisungen, Modellwahl oder Input.
- Der Agent kann eine Aktion nicht ausführen → fehlendes oder falsch konfiguriertes Tool.
- Ein späterer Retrieval-Schritt liefert irrelevante Informationen → Wissens- oder Retrieval-Konfiguration.
## Verständnischeck
Bevor du weitergehst, solltest du erklären können:
- Warum n8n selbst kein Sprachmodell ist.
- Warum ein API-Key in Credentials und nicht in einen Prompt gehört.
- Wofür die AI Agent Node verantwortlich ist.
- Warum auch ein visueller Workflow bewusst als Architektur entworfen werden muss.
> 💡 Takeaway: n8n ist die Orchestrierungsschicht. OpenRouter liefert den Modellzugriff. Credentials sorgen für sichere Authentifizierung. Der AI Agent verbindet Anweisungen, Chat-Modell und Tools in einem ausführbaren Workflow.