# Warum Multi-Agent-Systeme entstehen

Notion page: https://app.notion.com/p/Warum-Multi-Agent-Systeme-entstehen-3779418319f3807cbbb5f55151620832
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Was passiert, wenn ein Single-Agent-n8n-Workflow an die Grenzen dessen stößt, was er zuverlässig bewältigen kann, warum diese Grenzen bestehen und was die Branche entwickelt hat, um damit umzugehen, ohne dass du dafür über deinen aktuellen n8n-Workflow hinaus etwas bauen müsstest.

## Was du gebaut hast
Contigo GmbHs Support-Agent führt inzwischen mehrstufige Gespräche, ruft präzise aus einer Wissensdatenbank ab, ruft Tools über eine ReAct-Schleife auf und setzt Grounding-Verhalten durch einen sorgfältig entworfenen System-Prompt durch. Für die Mehrheit von Contigos Kunden-Support-Anfragen (Produktfragen, Compliance-Abfragen, Kreditstatusprüfungen und Erklärungen zu Kontoverfahren) ist diese Architektur die richtige und ausreichende Wahl.
Das Führungsteam stellt jedoch eine ehrgeizigere Frage. Könnte dieselbe Architektur eine vollständige Bewertung eines Unternehmenskreditantrags übernehmen, indem sie gleichzeitig die finanzielle Lage des Kunden analysiert, die regulatorische Compliance nach geltendem EU-Recht prüft, das Kreditrisiko anhand von Contigos internen Modellen bewertet und die Kundenkommunikation entwirft, die alle drei Ergebnisse zusammenfasst?
Das Entwicklungsteam probiert es aus. Es verbindet vier zusätzliche Tools und erweitert den System-Prompt. Die ersten Tests zeigen das Problem sofort.
## Kontextverwässerung
Ein einzelner Agent verarbeitet jede Aufgabe über ein einziges Kontextfenster. Mit wachsender Komplexität der Aufgabe füllt sich dieses Kontextfenster mit einer zunehmenden Menge an Tool-Ausgaben, abgerufenen Textabschnitten, Zwischenschritten des Schlussfolgerns und Gesprächsverlauf. Wird der Kontext überfüllt, verschlechtert sich die Fähigkeit des Modells, früheren Informationen Aufmerksamkeit zu schenken.
Das wird Kontextverwässerung genannt: die Verschlechterung der Denkqualität, sobald die Menge an Informationen im Kontextfenster die effektive Aufmerksamkeitskapazität des Modells übersteigt.
Bei Contigos komplexer Antragsbewertung beginnt der Agent, Ausgaben aus unterschiedlichen Analyseschritten durcheinanderzubringen. Er ruft regulatorische Inhalte ab, wenn er eigentlich Kreditberechnungen durchführen sollte. Er erzeugt die Kundenzusammenfassung, bevor die Compliance-Prüfung abgeschlossen ist. Bei komplexen mehrstufigen Anträgen steigt seine Fehlerquote im Vergleich zu einfacheren Anfragen deutlich an.
Das Kontextfenster hat dabei sein hartes Token-Limit nicht erreicht. Die Aufmerksamkeit des Modells wurde jedoch über zu viele konkurrierende Eingaben gleichzeitig gespannt, wodurch die Denkqualität leidet.
## Tool-Überladung
Das zweite Fehlerverhalten hängt damit zusammen. Ist ein einzelner Agent mit vielen Tools verbunden, um unterschiedliche Aufgaben zu bewältigen, beanspruchen bereits die Tool-Beschreibungen selbst Platz im Kontextfenster. Entscheidender noch: Die Genauigkeit der Weiterleitung des Modells sinkt, je mehr Tools angeschlossen sind.
Das ist Tool-Überladung: die Verschlechterung der Genauigkeit bei der Tool-Auswahl, sobald die Zahl der angeschlossenen Tools die zuverlässige Unterscheidungsfähigkeit des Modells übersteigt.
Eine Variante davon hast du in der vorherigen Lektion erlebt, als drei vage Tool-Beschreibungen zu Fehlern bei der Weiterleitung führten. Stell dir dasselbe Problem bei zwölf Tools mit sich überschneidenden Beschreibungen vor. Die Weiterleitung des Modells wird nicht deshalb unzuverlässig, weil die Beschreibungen schlecht geschrieben sind, sondern weil es schlicht zu viele ähnliche Optionen gibt, um zwischen ihnen konsistent zu unterscheiden.
## Was Multi-Agenten-Systeme anders machen
Ein Multi-Agenten-System verteilt die kognitive Last, die einen einzelnen Agenten überfordert, auf mehrere spezialisierte Modelle. Statt dass ein Agent versucht, gleichzeitig Finanzanalyst, Regulierungsexperte, Risikobewerter und Kommunikationsverfasser zu sein, weist das System jede Rolle einem eigenen Agenten zu, mit einem eigenen fokussierten System-Prompt, einem eigenen begrenzten Tool-Satz und einem eigenen isolierten Kontextfenster.
Jeder spezialisierte Agent arbeitet innerhalb eines Kontextfensters, das nur die für seine jeweilige Rolle relevanten Informationen enthält. Der Kreditrisiko-Agent sieht Kreditdaten und Risikomodelle. Er sieht weder die regulatorische Compliance-Analyse noch den Entwurf der Kundenkommunikation. Sein Kontext ist kleiner, fokussierter, und sein Schlussfolgern entsprechend zuverlässiger.
Unabhängige Aufgaben lassen sich zudem gleichzeitig statt nacheinander mehreren Agenten zuweisen. Das verringert die gesamte Bearbeitungszeit für komplexe mehrstufige Bewertungen.
> ➡️ Multi-Agenten-Systeme sind keine einzelne Architektur. Sie sind eine Familie von Mustern, von denen jedes für eine andere Problemklasse geeignet ist. Du musst nicht verstehen, wie man sie baut, nur, dass sie existieren und welches Problem jedes davon löst.

## Wo dein n8n-Workflow hineinpasst
Der n8n-Workflow, den du gebaut hast, ist keine Zwischenstufe auf dem Weg zu etwas Besserem. Er ist die richtige Architektur für Contigos Support-Anwendungsfall. Die Bedingungen, die Multi-Agenten-Komplexität rechtfertigen (gleichzeitige tiefgreifende Expertise über mehrere unzusammenhängende Fachbereiche hinweg, parallele Ausführung unabhängiger Analyseaufgaben, ein Tool-Register, das für zuverlässige Single-Agent-Weiterleitung zu groß ist), treffen auf einen Support-Agenten, der Kreditproduktanfragen, Compliance-Abfragen und Kontostandsprüfungen innerhalb einer einzigen Domäne bearbeitet, nicht zu.
Zu verstehen, wo die Grenzen liegen, macht dich zu einem umsichtigeren Architekten. Die Entscheidung, bei einem Single-Agent-n8n-Workflow zu bleiben, ist eine begründete architektonische Wahl.
![image]((notion-hosted file))

## Verständnis prüfen
> 💡 Contigos Entwicklungsteam fügt dem Support-Agenten acht zusätzliche Tools hinzu, um seine Fähigkeiten zu erweitern. Die Leistung bei komplexen mehrstufigen Anfragen verschlechtert sich deutlich. Was ist die zutreffendste Erklärung?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4f3cb68b-e322-4141-b988-37996717375c


> 💡 Fazit:
  Kontextverwässerung und Tool-Überladung sind die spezifischen Fehlerarten, die die Grenze dessen markieren, was ein Single-Agent-n8n-Workflow zuverlässig bewältigen kann. Sie zu verstehen, ist ein Grund, ihn sorgfältig zu entwerfen.
  Die Verfeinerung des System-Prompts, die du in der nächsten Lektion vornimmst, ist die praktische Antwort auf alles, was hier eingeführt wurde: den Kontext fokussiert halten, die Tool-Beschreibungen präzise halten und das Verhalten des Agenten innerhalb des Bereichs vorhersehbar halten, für den er entworfen wurde.
