# Einführung in Flowise

Notion page: https://app.notion.com/p/Einf-hrung-in-Flowise-3779418319f380ea99fcf1f781cb6d1b
Backed up before n8n migration

> 💡 Nach dieser Lektion verstehst du genau, was Flowise ist und warum es entwickelt wurde. Du lernst die Funktionsweise dieses visuellen Baukastens für KI-Agenten kennen und erfährst, wie wir das Tool in diesem Kurs einsetzen, um den Support-Agenten der Contigo GmbH zu bauen.

## Das Problem, das Flowise löst
Einen KI-Agenten von Grund auf selbst zu programmieren bedeutet, die gesamte Verbindungslogik für jede einzelne Komponente mühsam aufzusetzen. Das betrifft das Sprachmodell ebenso wie das Gedächtnis-Modul, die Vektordatenbank, externe Tools und die Prompt-Kette. Jede dieser Integrationen erfordert eigene API-Aufrufe, eine saubere Fehlerbehandlung und spezifische Konfigurationen. Noch bevor das eigentliche Verhalten des Agenten zum ersten Mal getestet werden kann, hat ein Entwickler bereits Hunderte Zeilen Standardcode geschrieben. Dieser sogenannte Boilerplate-Code trägt jedoch absolut nichts zur Lösung des eigentlichen Problems bei.
Für ein Team wie das von Contigo GmbH ist das ein echtes Problem. Sie müssen schnell von einer Geschäftsanforderung zu einem funktionierenden Prototyp kommen. Jede Stunde, die in Infrastruktur fließt, fehlt woanders: bei der Memory-Strategie, der Retrieval-Pipeline, den Tool-Beschreibungen oder dem Failure Handling.
Genau hier setzt Flowise an. Du bekommst eine visuelle Drag-and-drop-Umgebung, in der AI-Agentenkomponenten als Nodes auf einem Canvas liegen. Ein Sprachmodell mit einem Memory-Modul zu verbinden ist eine einzige Drag-and-drop-Bewegung. Eine Vektordatenbank in die Retrieval-Pipeline einzubinden erledigst du über ein Konfigurationspanel. Um die Infrastruktur kümmert sich Flowise. Um das Design kümmerst du dich.

## Was Flowise ist
Flowise ist ein Open-Source-Tool: ein Low-Code-Visual-Builder für Large-Language-Model-Anwendungen und AI-Agenten. Es macht den Aufbau von LLM-gestützten Systemen auch dann zugänglich, wenn du zwar dein Problem genau kennst, aber keinen Framework-Level-Integrationscode von Grund auf schreiben willst.
Flowise gibt es in zwei Hauptvarianten: als selbst gehostete Anwendung oder als Flowise Cloud. In diesem Kurs verwendest du Flowise Cloud, damit du den Builder direkt im Browser öffnen kannst, ohne etwas zu installieren oder einen Server aufzusetzen.
Bevor du fortfährst, erstelle ein Flowise-Cloud-Konto:
- Du kannst dein Konto hier erstellen: Flowise Cloud sign-up
Flowise bietet einen kostenlosen Cloud-Plan mit begrenzter Nutzung an, der ausreicht, um loszulegen und den ersten Kursaktivitäten zu folgen. Du musst für diesen Kurs keinen kostenpflichtigen Plan wählen.
- Du kannst die aktuellen kostenlosen/Testoptionen hier prüfen: Flowise pricing
Nachdem du dich angemeldet hast, nimm dir ein paar Minuten Zeit, um dich in der Oberfläche umzusehen. Du wirst hauptsächlich mit dem visuellen Builder arbeiten, in dem du Agenten und Workflows erstellst, indem du Komponenten hinzufügst und verbindest.
- Du kannst die offizielle Dokumentation zur Oberfläche hier prüfen: Flowise documentation — Introduction
> 💡 Wenn du lieber direkt die selbst gehostete Version von Flowise verwenden möchtest, kannst du den Kurs trotzdem weiterverfolgen. Der erste Teil ist jedoch auf die Cloud-Version ausgerichtet, daher können einige Screens, Einrichtungsschritte, URLs und Zugriffsoptionen anders aussehen. In diesem Fall musst du möglicherweise etwas zusätzliche DIY-Einrichtung oder Fehlerbehebung durchführen, um die Lektionsanweisungen an deine eigene Installation anzupassen.

Die Flowise-Oberfläche ist über einen Standardbrowser zugänglich. Sobald die Anwendung läuft, ist jede Komponente einer Agentenarchitektur als ziehbarer Node in der Komponentenpalette verfügbar. Die Architektur des Agenten wird gebaut, indem diese Nodes verbunden und ihre Parameter konfiguriert werden.

## Wie Flowise funktioniert
Flowise organisiert Agenten-Builds in mehrere Umgebungen, die jeweils für ein unterschiedliches Maß an architektonischer Komplexität ausgelegt sind. In diesem Kurs konzentrieren wir uns jedoch auf Chatflow.
Chatflow ist die primäre Umgebung für Single-Agent-Systeme. Es unterstützt die wichtigsten Bausteine, die du in diesem Kurs verwenden lernst: Gesprächsschritte miteinander verketten (Conversational Chains), einen Agenten aus deinen eigenen Dokumenten antworten lassen (ein Muster namens RAG), die Art von Memory, die du gerade kennengelernt hast, und Agenten mit externen Tools verbinden. Zu jedem davon bekommst du eine eigene Lektion — du musst die Namen noch nicht erkennen.
Der Ausführungspfad durch einen Chatflow ist relativ linear. Eine Nutzeranfrage fließt in einer definierten Reihenfolge durch die verbundenen Komponenten und gibt eine Antwort zurück. Das ist die Umgebung, die für den Großteil des Contigo-Agenten-Builds in diesem Kurs verwendet wird.
Jeder Knoten hat Verbindungspunkte, sogenannte Eingaben und Ausgaben. Ausgaben eines Knotens können mit kompatiblen Eingaben eines anderen Knotens verbunden werden. Flowise hilft dabei, einige Setup-Fehler zu vermeiden, indem es nur bestimmte Verbindungstypen zusammenpassen lässt. Ein Knoten, der auf der Canvas platziert ist, beeinflusst den Agenten nur dann, wenn er mit dem aktiven Flow-Pfad verbunden ist, der zur Laufzeit verwendet wird.

![image]((notion-hosted file))

## Warum Flowise existiert
Drei Veränderungen in der AI-Entwicklungslandschaft haben die Bedingungen geschaffen, die Flowise notwendig gemacht haben.
1. Der erste Grund war die wachsende Zahl beweglicher Teile in KI-Systemen. Teams mussten Sprachmodelle verbinden, die Antworten formulieren, Embedding-Modelle, die Text in durchsuchbare numerische Bedeutung umwandeln, Vektordatenbanken, die diese Bedeutung speichern und durchsuchen, Memory-Komponenten, die nützlichen Kontext behalten, und externe Tools wie APIs oder Datenbanken. Je mehr diese Komponenten wurden, desto schwieriger wurde es, alles direkt im Code zu verwalten. 
Eine visuelle Abstraktionsschicht, die diese Verbindungen übernimmt, reduziert diese Komplexität auf ein handhabbares Konfigurationsproblem.
1. Die zweite war das Aufkommen agentischer Muster. Agenten sind Reasoning-Loops, die Tools aufrufen, Ergebnisse beobachten und entscheiden, was als Nächstes zu tun ist. Diese Loops in Code darzustellen, erfordert architektonische Disziplin, die fehleranfällig und schwer zu debuggen ist. Ein Canvas, der den Loop sichtbar macht, macht es deutlich leichter, darüber nachzudenken und ihn zu korrigieren.
1. Die dritte war der Bedarf an schneller Iteration. Agentenverhalten entsteht aus dem Zusammenspiel von Prompt, Memory, Retrieval und Tools. Einen Parameter zu ändern und die Wirkung sofort in der integrierten Testoberfläche zu beobachten, ist eine schnellere Feedbackschleife als Code zu bearbeiten, neu bereitzustellen und manuell erneut zu testen.

## Wie Flowise in diesem Kurs verwendet wird
Flowise ist das primäre Tool für die Implementierung des Support-Agenten der Contigo GmbH. Jeder Sprint führt eine neue Fähigkeit und die entsprechende Flowise-Konfiguration ein, die sie umsetzt. Am Ende des Kurses wird der Flowise-Canvas eine vollständige, produktionsorientierte agentische Architektur enthalten; alles inkrementell aufgebaut, Sprint für Sprint, wobei Contigos Finanzdienstleistungskontext durchgehend als Business Case dient.
## Verständnis prüfen
>  Contigos Entwicklungsteam prüft den Flowise-Builder, bevor der Build beginnt. Ein Junior-Entwickler schlägt vor, dass der Agent, weil er später Memory, Retrieval und Tool-Verbindungen benötigen wird, zu komplex für Chatflow sein muss. Wie würdest du antworten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b1994c12-c811-4412-9e10-6cae3d22a608

> 💡 Takeaway: 
  Flowise macht die Architektur von KI-Agenten visuell greifbar, sodass du sie direkt auf einer Benutzeroberfläche konfigurieren und debuggen kannst. Das beschleunigt den gesamten Entwicklungsprozess enorm und sorgt für maximale Klarheit. Wenn du verstehst, welche Aufgabe die einzelnen Komponenten erfüllen, bevor du sie auf der Arbeitsfläche miteinander verknüpfst, macht das den entscheidenden Unterschied. Du befolgst nicht mehr nur einfach Anweisungen, sondern baust deine Agenten absolut zielgerichtet und mit System.
