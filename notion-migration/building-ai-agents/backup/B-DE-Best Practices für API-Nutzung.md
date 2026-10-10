# Best Practices für API-Nutzung

Notion page: https://app.notion.com/p/Best-Practices-f-r-API-Nutzung-3789418319f380b8be94c5ab4f157674
Backed up before n8n migration

>  Diese Lektion verwendet Gemini als Hauptbeispiel, aber die zugrunde liegende Logik der API-Nutzung lässt sich auch auf andere KI-Modelle und Anbieter übertragen. Konzentriere dich auf die Prinzipien: Anfragen klar strukturieren, Antworten zuverlässig verarbeiten, Fehler handhaben und Workflows so gestalten, dass sie an verschiedene Modell-APIs angepasst werden können.

> 💡 Was du am Ende dieser Lektion verstehen wirst: Wie die Gemini API in einem Geschäftskontext funktioniert, welche Rate Limits und Kostenstrukturen gelten und wie du verantwortungsvolle Entscheidungen zur Modellauswahl triffst, bevor du etwas baust.

## Bevor du einen einzigen API-Key generierst
Das Entwicklungsteam von Meridian Consulting steht in den Startlöchern. Doch bevor jemand Zugangsdaten erstellt oder einen Modell-Node in Flowise einbindet, bittet die Teamleitung zu einer kurzen Alignment Session. Der Grund dafür ist einfach: In früheren Projekten haben sich Entwickler oft direkt auf die Konfiguration gestürzt, ohne die Regeln der jeweiligen Plattform zu kennen. Die Quittung folgte prompt: unerwartete Kostenspitzen, Agenten, die unter Last wegen Rate Limits mitten im Gespräch abstürzten, und ein Vorfall, bei dem ein Prototyp durch eine Endlosschleife in nur vierzig Minuten das API-Budget eines ganzen Monats verbrauchte.
Zu verstehen, wie die Gemini API funktioniert (ihr Preismodell, ihre Rate Limits, ihre Datenverarbeitungsrichtlinien und wann sie statt eines Consumer-Abonnements verwendet werden sollte), gehört zu den notwendigen Vorbereitungen, bevor ein Projekt gestartet wird.

## API-Integration versus Consumer-Abonnement
Die erste Unterscheidung, die das Team treffen muss, liegt zwischen zwei verschiedenen Arten, auf Gemini zuzugreifen.
1. Die Gemini-Webanwendung ist für einzelne Nutzer gedacht, die manuelle Gespräche führen. Sie eignet sich gut für die Exploration und einmalige Abfragen, lässt sich jedoch weder in Anwendungen einbetten noch programmatisch auslösen oder in einen Flowise-Node-Graphen integrieren.
1. Die Gemini API ist die entwicklerorientierte programmatische Schnittstelle. Sie ermöglicht es Meridians Flowise-Agenten, einen Prompt zu senden, eine strukturierte Antwort zu erhalten, ein Tool aufzurufen und mehrere Reasoning-Schritte ohne menschliches Eingreifen miteinander zu verketten. Jeder agentische Workflow benötigt die API. Die Consumer-Oberfläche ist irrelevant, sobald das Erstellen beginnt.

## Rate Limits: Um die Grenzen herum entwerfen
Die Gemini API erzwingt Rate Limits, die je nach Modell und Preisstufe variieren. Wenn diese Limits überschritten werden, lehnt die API Anfragen ab und gibt einen 429-Fehler zurück, was in einem Live-Agenten-Workflow bedeutet, dass der Agent mitten im Gespräch scheitert.
Im kostenlosen Kontingent sind die Limits großzügig genug für Entwicklung und Tests, aber nicht ausreichend für Produktions-Traffic. Gemini 2.5 Flash und Gemini 2.5 Flash-Lite sind im kostenlosen Kontingent mit Request-Limits verfügbar, die für Entwicklung und Tests geeignet sind. Gemini 2.5 Pro ist im kostenlosen Kontingent verfügbar, aber mit konservativeren Limits, wodurch es für agentische Workflows ungeeignet ist, die schnelle sequenzielle Aufrufe erfordern. Dieser Kurs verwendet Gemini 2.5 Flash und Flash-Lite im kostenlosen Kontingent, die ausreichend Spielraum für Entwicklung, Aufbau und Tests in allen vier Sprints bieten.
Für Meridians Produktions-Deployment, bei dem mehrere Berater den Agenten gleichzeitig über den Arbeitstag hinweg abfragen können, wird eine kostenpflichtige Stufe mit höheren Rate Limits notwendig sein. Dies vor dem Deployment einzuplanen, ist eine grundlegende operative Verantwortung.

## Kostenstruktur: Modellauswahl als finanzielle Entscheidung
Die Gemini API rechnet pro Token ab. Jede verarbeitete Texteinheit, ob Input oder Output. Die Wahl des Modells hat direkte und erhebliche Auswirkungen auf die Betriebskosten.
Gemini 2.5 Flash kostet ungefähr $0.30 pro Million Input-Tokens und $2.50 pro Million Output-Tokens. Gemini 2.5 Pro kostet ungefähr $1.25 pro Million Input-Tokens und $10.00 pro Million Output-Tokens für Standard-Prompts, wodurch es für Routineanfragen deutlich teurer ist. Gemini 2.5 Flash-Lite ist mit $0.10 pro Million Input-Tokens und $0.40 pro Million Output-Tokens die kosteneffizienteste Option und eignet sich damit gut für hochfrequente, leichtgewichtige Schritte innerhalb eines größeren Workflows, bei denen kein tiefes Reasoning erforderlich ist.
[TABLE]
  | Modell | Input-Kosten pro 1M Tokens (USD) | Output-Kosten pro 1M Tokens (USD) | Am besten geeignet für |
  | Gemini 2.5 Flash-Lite | ~$0.10 | ~$0.40 | Hochvolumige Routineanfragen |
  | Gemini 2.5 Flash | ~$0.30 | ~$2.50 | Standardmäßige agentische Workflows |
  | Gemini 2.5 Pro | ~$1.25 | ~$10.00 | Komplexes Reasoning mit langen Dokumenten |
> 💻 Aktuelle Modellspezifikationen und aktuelle Preise findest du in der offiziellen Gemini-API-Dokumentation unter:
  - Gemini Models: ai.google.dev/gemini-api/docs/models 
  - Gemini Pricing: ai.google.dev/gemini-api/docs/pricing

## Datenschutz im kostenlosen Kontingent
Ein Aspekt, der für Meridian besonders wichtig ist, ist die Datenverarbeitungsrichtlinie im kostenlosen Kontingent. Inhalte, die über die Gemini API im kostenlosen Kontingent verarbeitet werden, können von Google verwendet werden, um seine Modelle zu verbessern. Das eignet sich für Entwicklung mit Testdaten. Für eine Beratung, die sensible operative Kundendaten verarbeitet, ist das inakzeptabel.
Ein Upgrade auf eine kostenpflichtige Stufe entfernt diese Datennutzung. Inhalte, die in kostenpflichtigen Stufen verarbeitet werden, werden nicht für Modelltraining verwendet. Für jedes Deployment, das echte Kundendaten verarbeitet, ist die kostenpflichtige Stufe nicht optional. Diese Entscheidung sollte getroffen werden, bevor das erste echte Dokument in das System geladen wird, nicht erst danach.

## Verständnis prüfen
>  Meridians Agent läuft im kostenlosen Kontingent der Gemini API und beginnt während der Spitzenzeiten mitten im Gespräch zu scheitern. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f92ddeec-e485-4aa6-85b0-aee8c3db46fd

> 💡 Takeaway: 
  Die Gemini-API ist die programmatische Schnittstelle, die Agenten-Workflows überhaupt erst möglich macht. Allerdings arbeitet sie innerhalb von Grenzen, die vor dem Start klar sein müssen: Rate Limits bestimmen, wie viele Anfragen der Agent pro Minute und Tag senden kann, bevor die API sie abweist. Die Modellauswahl entscheidet über die Betriebskosten, und die Datenverarbeitungsrichtlinien legen fest, ob echte Kundendaten sicher verarbeitet werden können. 
  Diese Faktoren zu berücksichtigen, bevor der erste Node verknüpft wird, erspart später erhebliche Probleme im Betrieb.
