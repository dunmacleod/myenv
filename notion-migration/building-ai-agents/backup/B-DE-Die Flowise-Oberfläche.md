# Die Flowise-Oberfläche

Notion page: https://app.notion.com/p/Die-Flowise-Oberfl-che-3789418319f380ab9000f5a81eb96a64
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Wie du dich in der Flowise-Oberfläche zurechtfindest, wie du einen Agentflow-v2-Node-Graph liest und warum Agentflow v2 die richtige Build-Umgebung für diesen Kurs ist.

## Von der Infrastruktur zum Arbeitsbereich
Die Umgebung von Meridian Consulting ist überprüft. Die lokale Flowise-Umgebung läuft in einem lokalen Browser, der Gemini API-Key ist aktiv, und das Team ist bereit, mit dem Bauen zu beginnen. Bevor jemand einen einzigen Node auf den Canvas zieht, ruft die Teamleitung eine zehnminütige Orientierung ein. Der Grund ist vertraut: In früheren Projekten haben Entwickler, die die Orientierung übersprungen haben, die erste Stunde damit verbracht, sich durch die Oberfläche zu klicken, um Komponenten zu finden, Nodes falsch zu verbinden und im völlig falschen Flow-Typ zu bauen.
Den Flowise-Arbeitsbereich danach zu verstehen, was die Oberfläche enthält, wie der Canvas funktioniert und wofür die verschiedenen Build-Modi gedacht sind, dauert weniger lange, als die Verwirrung wieder zu beheben, die durch das Überspringen entsteht. Diese Lektion liefert diese Orientierung.

## Das Flowise-Dashboard
Wenn du Flowise in deinem Browser unter http://localhost:3000 öffnest, ist das Dashboard der erste Bildschirm, den du siehst.
Der Navigationsbereich enthält vier Hauptbereiche.
- Chatflows ist der Bereich, in dem Single-Agent-Workflows und einfache LLM-Chains gebaut und verwaltet werden.
- Agentflows v2 ist der Bereich, in dem Multi-Agent-Systeme und komplexe Orchestrierungsworkflows konstruiert werden.
Marketplaces stellt vorgefertigte Flow-Vorlagen bereit, die als Ausgangspunkte importiert und angepasst werden können. Credentials ist der Bereich, in dem API-Keys und Authentifizierungsdetails sicher gespeichert werden. Hier befindet sich der zuvor konfigurierte Gemini-Key.

## Der Canvas
Wenn du einen Agentflow v2 öffnest, erscheint der Canvas, auf dem der Workflow visuell gebaut wird. Jeder Schritt im Workflow ist ein einzelner Node. Die Verbindungen zwischen Nodes definieren den Ausführungspfad klar, und es läuft keine versteckte Logik zwischen den Schritten.
Der Canvas hat drei Hauptelemente: Nodes, Edges und Flow State.
Nodes werden hinzugefügt, indem du auf dem Canvas auf den (+)-Button klickst. Dadurch öffnet sich ein durchsuchbares Komponentenpanel.
![image]((notion-hosted file))
In Agentflow v2 sind folgende Nodes verfügbar:
[TABLE]
  | Node | Rolle |
  | Start Node | Der verpflichtende Einstiegspunkt jedes Agentflow v2. Definiert, wie der Workflow ausgelöst wird, und richtet die Anfangsbedingungen ein. Akzeptiert Input aus der Chat-Oberfläche oder einem anpassbaren Formular. Verwaltet außerdem die Initialisierung von Flow State und Einstellungen für Conversation Memory. |
  | LLM Node | Bietet direkten Zugriff auf ein konfiguriertes Large Language Model zur Ausführung von AI-Aufgaben. Wird für Textgenerierung, Zusammenfassung, Übersetzung, Analyse und die Generierung strukturierter JSON-Ausgaben verwendet. Hat Zugriff auf Memory und kann Flow State lesen und schreiben. Verwende ihn, wenn du einen direkten Modellaufruf ohne vollständiges Agenten-Reasoning brauchst. |
  | Agent Node | Repräsentiert eine autonome AI-Entität, die reasoning-, planungs- und interaktionsfähig ist und mit Tools oder Wissensquellen arbeiten kann, um ein bestimmtes Ziel zu erreichen. Verwendet ein LLM, um dynamisch eine Abfolge von Aktionen zu entscheiden, und kann verfügbare Tools nutzen oder Document Stores abfragen. Dies ist der primäre Reasoning-Node in Meridians Agenten. |
  | Tool Node | Stellt einen Mechanismus bereit, um ein bestimmtes, vordefiniertes Flowise Tool direkt und deterministisch innerhalb der Workflow-Sequenz auszuführen. Anders als beim Agent Node, bei dem das LLM auf Grundlage von Reasoning dynamisch ein Tool auswählt, führt der Tool Node exakt das Tool aus, das der Workflow-Designer während der Konfiguration ausgewählt hat. |
  | Retriever Node | Führt gezielten Informationsabruf aus konfigurierten Document Stores durch, indem diese auf Grundlage semantischer Ähnlichkeit abgefragt werden. Eine fokussierte Alternative zur Nutzung eines Agent Nodes, wenn die einzige erforderliche Aktion Retrieval ist und keine dynamische Tool-Auswahl durch ein LLM benötigt wird. |
  | HTTP Node | Ermöglicht direkte Kommunikation mit externen Webdiensten und APIs über HTTP. Der Workflow kann GET-, POST-, PUT-, DELETE- und PATCH-Requests an externe Endpunkte senden, mit Unterstützung für Authentifizierung, benutzerdefinierte Header, Query-Parameter und verschiedene Request-Body-Typen. |
  | Condition Node | Implementiert deterministische Verzweigungslogik innerhalb des Workflows auf Grundlage definierter Regeln. Bewertet eine oder mehrere Bedingungen, die Strings, Zahlen oder boolesche Werte mit logischen Operatoren wie equals, contains, greater than oder is empty vergleichen, und leitet die Ausführung anschließend je nach Ergebnis auf unterschiedliche Pfade. |
  | Condition Agent Node | Bietet AI-gesteuerte dynamische Verzweigung auf Grundlage von natürlichsprachlichen Anweisungen und Kontext. Verwendet ein LLM, um Input-Daten anhand einer Reihe nutzerdefinierter Szenarien zu analysieren und den Workflow auf den Pfad zu leiten, der dem Szenario entspricht, das das LLM als am passendsten bestimmt. Verwende ihn, wenn feste Regeln für Routing-Entscheidungen nicht ausreichen. |
  | Iteration Node | Führt einen definierten Sub-Flow für jedes Element in einem Input-Array aus und implementiert damit eine for-each-Schleife. Nimmt ein Array als Input und führt für jedes einzelne Element sequenziell die Node-Sequenz aus, die innerhalb seiner Grenzen auf dem Canvas platziert ist. |
  | Loop Node | Leitet die Workflow-Ausführung explizit zurück zu einem zuvor ausgeführten Node und ermöglicht dadurch die Erstellung von Zyklen oder iterativen Wiederholungen. Enthält eine konfigurierbare Max Loop Count, um vor Endlosschleifen zu schützen, mit einem Standardwert von 5. |
  | Human Input Node | Pausiert die Workflow-Ausführung, um expliziten Input, eine Genehmigung oder Feedback von einem menschlichen Nutzer anzufordern. Stoppt den automatisierten Fortschritt und zeigt Informationen oder eine Frage über die Chat-Oberfläche an, dann wird die Ausführung entlang des Pfads fortgesetzt, der der gewählten Aktion des Nutzers entspricht. |
  | Direct Reply Node | Sendet eine finale Nachricht an den Nutzer und beendet den aktuellen Ausführungspfad. Nimmt eine konfigurierte Nachricht ( statischen Text oder dynamische Inhalte aus einer Variable ) und liefert sie direkt über die Chat-Oberfläche an den Endnutzer aus. Das Message-Feld muss explizit mithilfe der {{-Syntax auf die Output-Variable des vorherigen Nodes gesetzt werden. |
  | Custom Function Node | Stellt einen Mechanismus bereit, um benutzerdefinierten serverseitigen JavaScript-Code innerhalb des Workflows auszuführen. Ermöglicht das Schreiben und Ausführen beliebiger JavaScript-Snippets für komplexe Datentransformationen, maßgeschneiderte Geschäftslogik oder Interaktionen mit Ressourcen, die von anderen Standard-Nodes nicht direkt unterstützt werden. Die Funktion muss einen String-Wert zurückgeben. |
  | Execute Flow Node | Ermöglicht den Aufruf und die Ausführung eines anderen vollständigen Flowise Chatflows oder Agentflows aus dem aktuellen Workflow heraus. Funktioniert als Sub-Workflow-Caller, fördert modularen Aufbau und Wiederverwendbarkeit von Logik, indem ein separater bereits vorhandener Workflow ausgelöst, Input an ihn übergeben und sein Output zurückerhalten wird. |
Edges sind die Verbindungslinien zwischen Nodes. Eine Edge definiert die Ausführungsrichtung, d.h. welcher Node als Nächstes läuft. In Agentflow v2 sind Edges explizit und gerichtet. Ein Node, der auf dem Canvas liegt, aber nicht durch mindestens eine Edge mit dem Ausführungspfad verbunden ist, tut zur Laufzeit nichts.
Flow State ist ein gemeinsamer Key-Value-Store, der während einer einzelnen Ausführung über Nodes hinweg bestehen bleibt. Die Nodes können mithilfe von $flow.state aus Flow State lesen und in ihn schreiben. So werden die Daten zwischen den Schritten weitergegeben, ohne Werte fest in einzelne Nodes zu codieren.

![image]((notion-hosted file))

## Einen Agentflow-v2-Graph lesen
Ein Agentflow-v2-Graph wird gelesen, indem du den Edges vom Start Node bis zum Direct Reply Node folgst und den Weg nachverfolgst, den die Anfrage eines Nutzers durch den Workflow nimmt. In einem einfachen Meridian-Agenten-Graph sieht der Pfad so aus:
1. Der Start Node empfängt den Input des Nutzers und initialisiert den Flow.
1. Der Agent Node empfängt den Input, wendet den System-Prompt an, ruft Gemini auf und entscheidet, was zu tun ist.
1. Wenn der Agent genug Informationen hat, übergibt er eine Antwort an den Direct Reply Node.
1. Der Direct Reply Node gibt die Antwort an den Nutzer zurück und beendet die Ausführung.
Jeder Node im Graph hat eine Rolle in diesem Pfad. Ein Node, der nicht verbunden ist, ist inaktiv, hat keine Auswirkung auf den Flow und erzeugt keinen Fehler. Dadurch sind nicht verbundene Nodes eine häufige Quelle unentdeckter Bugs.

## Chatflow versus Agentflow v2
Flowise stellt zwei Build-Umgebungen bereit. Dieser Kurs verwendet ausschließlich Agentflow v2.
[TABLE]
  |  | Chatflow | Agentflow v2 |
  | Design | Lineare Chains mit impliziter Ausführung | Expliziter Node-Graph mit sichtbarem Ausführungspfad |
  | Verzweigung | Nicht unterstützt | Condition Node und Condition Agent Node |
  | State | Implizite Memory-Module | Flow State, geteilt über alle Nodes |
  | Loops | Nicht unterstützt | Loop Node |
  | Human Approval | Nicht unterstützt | Human Input Node |
  | Sub-Flows | Nicht unterstützt | Execute Flow Node |
  | Am besten geeignet für | Einfache Gesprächsagenten | Mehrstufige, zustandsbehaftete Business-Workflows |
Der Chatflow eignet sich für einfache Gesprächsagenten mit linearer Ausführung. Agentflow v2 ist die richtige Wahl, wenn der Workflow verzweigt, looped, Wissen dynamisch abruft oder Kontext zwischen Schritten weitergibt. Genau das beschreibt jede Anforderung im Agentenprojekt von Meridian.
Alle Canvas-Arbeiten in diesem Kurs werden in Agentflows durchgeführt und nicht in den Chatflows. Wenn du einen neuen Flow erstellst, wähle immer Add New Agentflow im Agentflows-Bereich des linken Navigationspanels aus.

## Verständnis prüfen
>  Ein Meridian-Entwickler platziert einen Condition Node auf dem Agentflow-v2-Canvas, verbindet ihn aber weder mit dem Start Node noch mit einem anderen Node. Was passiert zur Laufzeit?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/6efafc44-1c44-49a0-9406-fc26cd4a0afd

> 💡 Takeaway: 
  Der Agentflow-v2-Canvas ist der Ort, an dem die Agentenarchitektur sichtbar und klar wird. Jeder Schritt ist ein Node, jede Entscheidung ist eine Verbindung, und jedes Stück gemeinsamer Kontext lebt in der Flow State.
  Wenn du verstehst, wie diese drei Elemente zusammenarbeiten, entscheidet das darüber, ob sich dein Flow wie geplant verhält oder still und leise scheitert.