# Praktische Architekturmuster

Notion page: https://app.notion.com/p/Praktische-Architekturmuster-6d59418319f38275b57181c29cf2bdd5
Backed up before n8n migration

Selin weiß jetzt, dass Vela im Moment ein Single-Agent-System braucht. Der Scope ist überschaubar, die Tools sind logisch kompatibel, und der Koordinationsaufwand durch die Aufteilung in mehrere Agenten ist noch nicht gerechtfertigt. Aber „Single-Agent" ist kein vollständiges Design. Es beschreibt nur die Anzahl der Agenten. Was der Agent tut, wie er Entscheidungen trifft und was passiert, wenn er scheitert, steht auf einem anderen Blatt.
Bevor Jonas die Canvas öffnet, muss sich das Team einigen, welches Architekturmuster zum Problem passt. In Agentflow V2 nutzen verschiedene Muster unterschiedliche Kombinationen von Nodes. Wählt man das falsche Muster, muss man später neu bauen. Genau das will Vela vermeiden.
Diese Lektion stellt die sechs Muster vor, die in echten Agentensystemen am häufigsten vorkommen. Einige davon habt ihr schon auf einer Canvas gesehen, zwei sind neu.
## Die sechs Muster auf einen Blick
Jedes Muster löst ein anderes Designproblem. Der Name beschreibt die Struktur, nicht die Fähigkeit. Ein Agent, der auf einem dieser Muster aufgebaut ist, kann leistungsfähig oder schwach sein. Das Muster bestimmt, wie Entscheidungen getroffen werden und wie Arbeit fließt. Ob das zugrunde liegende Modell gut ist, ist eine andere Frage.
![image]((notion-hosted file))

## Single-Agent
- Die Struktur: ein Agent-Node, der Eingabe erhält und Ausgabe erzeugt. Reasoning, Tool-Auswahl und Antwortgenerierung passieren alle innerhalb eines Nodes.
- Wann es passt: Der Scope ist eng und stabil. Der System-Prompt kann alle Anfragetypen klar steuern. Die Tool-Nutzung ist einfach oder nicht vorhanden. Das Anfragevolumen erfordert keine Trennung.
Velas Baseline ist dieses Muster. Der Sprint-1-Walkthrough baut eine bewusst entworfene Version davon: ein Single-Agent-System mit klar definierten Eingaben, Ausgaben und Verantwortlichkeiten.
## Tool-Using-Agent
- Die Struktur: ein Agent-Node, verbunden mit einem oder mehreren Tools (einem HTTP-Node, einem Custom-Function-Node oder einem externen API-Aufruf). Der Agent entscheidet zur Laufzeit, welches Tool er wann aufruft.
- Wann es passt: Der Agent muss über sein eigenes Reasoning hinausgehen, um Live-Daten abzurufen, eine Berechnung durchzuführen oder eine Aktion auszulösen. Die Tools haben klare, sich nicht überschneidende Zwecke, sodass der Agent zuverlässig das richtige auswählen kann.
- Die zentrale Autorentscheidung: Tool-Beschreibungen. Der Agent-Node wählt Tools danach aus, wie ihr Zweck in der Konfiguration beschrieben ist. Eine vage Beschreibung wie „use this to get data" führt zu inkonsistenter Auswahl. Eine präzise Beschreibung wie „use this to retrieve the current stock level for a specific product SKU when the user asks about inventory" sagt dem Modell genau, wann es das Tool aufrufen soll.
## Workflow + Agent
- Die Struktur: eine Sequenz von Nodes. Manche Schritte sind deterministisch (ein Condition-Node, der einen Wert prüft, ein Custom-Function-Node, der Daten transformiert, ein HTTP-Node, der einen Datensatz abruft), ein oder mehrere Agent-Nodes übernehmen die Teile, die Reasoning erfordern.
- Wann es passt: Einige Schritte im Prozess sind vorhersehbar genug für feste Logik, andere brauchen Interpretation. Die Kombination aus deterministischen Schritten und agentischem Reasoning hält die Kosten niedrig und sorgt für konsistentes Verhalten bei den vorhersehbaren Teilen.
- Der Unterschied zu einem reinen Agenten: In einem Workflow-+-Agent-Muster steuert die Canvas den Ablauf. Der Agent-Node übernimmt Reasoning für seine spezifische Aufgabe innerhalb dieses Ablaufs. Der gesamte Ausführungspfad wird aber durch die Node-Verbindungen definiert, nicht durch die Laufzeitentscheidungen des Agenten.
## Router
- Die Struktur: ein Condition-Agent-Node, der die Eingabe klassifiziert und an einen von mehreren nachgelagerten Pfaden weiterleitet. Jeder Pfad bearbeitet einen bestimmten Anfragetyp.
- Wann es passt: Der Agent bekommt deutlich unterschiedliche Eingabetypen, die von unterschiedlicher Bearbeitung profitieren. Eine Anfrage zu Richtlinien braucht etwas anderes als eine Anfrage, einen Live-Status zu prüfen, und das wieder etwas anderes als eine Eskalation. Routing trennt diese am Einstiegspunkt, statt einen überlasteten Agent-Node alles bearbeiten zu lassen.
Dieses Muster kennt ihr schon. In einem früheren Kurs habt ihr den Condition-Agent-Node genutzt, um Anfragen als status_request, knowledge_query oder briefing_request zu klassifizieren. Das war ein Router. Das Muster selbst bleibt hier gleich, nur die Designentscheidungen drumherum ändern sich je nach Use Case: wie viele Routen, wie präzise jedes Szenario beschrieben wird, was auf jedem Branch passiert.
## Evaluator
- Die Struktur: ein Agent-Node (oder LLM-Node) erzeugt eine Ausgabe. Ein zweiter Node, typischerweise ein weiterer LLM-Node oder Condition-Agent-Node, bewertet, ob diese Ausgabe ein definiertes Qualitätskriterium erfüllt, bevor sie weitergeht.
- Wann es passt: Die Ausgabe des ersten Agenten muss geprüft werden, bevor sie den Nutzer erreicht oder eine nachgelagerte Aktion auslöst. Die Bewertung kann regelbasiert sein (enthält die Antwort ein Pflichtfeld?) oder modellbasiert (ist diese Antwort korrekt und innerhalb des Scope?).
- Der Unterschied zu einem Router: Ein Router entscheidet, wohin die Eingabe geschickt wird. Ein Evaluator entscheidet, ob die Ausgabe gut genug ist, um fortzufahren. Auf der Canvas sehen beide ähnlich aus, beide haben einen Entscheidungs-Node, aber sie sitzen an unterschiedlichen Punkten im Ablauf und beantworten unterschiedliche Fragen.
Ein Human-Input-Node kann als manueller Evaluator dienen, wenn die Risiken hoch genug sind, dass ein Mensch die Ausgabe erst freigeben muss.
## Supervisor-Worker
Die Struktur: Ein LLM-Node agiert als Supervisor. Er analysiert die Aufgabe, entscheidet, welcher spezialisierte Worker als Nächstes handeln soll, und schreibt diese Entscheidung in den Flow State, den Key-Value-Store zur Laufzeit, der Daten innerhalb einer einzelnen Ausführung zwischen Nodes weitergibt. Ein Condition-Node liest den Flow State und routet zum passenden Agent-Node (Worker). Jeder Worker gibt sein Ergebnis über einen Loop-Node an den Supervisor zurück. Der Supervisor prüft das Ergebnis und weist entweder den nächsten Worker zu oder schließt mit einem Final-Answer-Agent-Node ab.
Wann es passt: Die Aufgabe ist komplex genug, dass es sich lohnt, sie in Teilaufgaben zu zerlegen und an Spezialisten zu verteilen. Der Supervisor koordiniert, die Worker führen aus. Das ist das leistungsfähigste Muster in diesem Modul, und gleichzeitig das teuerste, weil Supervisor und jeder Worker einen eigenen Modellaufruf brauchen.
Dieses Muster ist neu. Gebaut habt ihr es noch nicht. Sprint 2 führt es Schritt für Schritt ein.
[TABLE]
  | Element | Rolle im Muster |
  | LLM Node | Supervisor, entscheidet, welcher Worker als Nächstes handelt; nutzt JSON Structured Output, um next und instruction in $flow.state zu schreiben |
  | Condition Node | Liest $flow.state.next und routet zum passenden Agent-Node |
  | Agent Node (×2 oder mehr) | Worker, jeder hat eine spezifische Rolle und einen System-Prompt; liest $flow.state.instruction als seine Aufgabe |
  | Loop Node | Gibt die Ausgabe des Workers zur Prüfung an den Supervisor zurück |
  | Agent Node (final) | Führt die gemeinsame Ausgabe zu einer einzigen kohärenten Antwort zusammen |
## Zwischen ihnen wählen
Kein Muster ist grundsätzlich besser als ein anderes. Die Wahl ergibt sich aus dem Problem:
[TABLE]
  | Wenn folgende Probleme bestehen | Zu erwägendes Muster |
  | Eine enge, gut abgegrenzte Menge von Anfragen ohne komplexes Routing | Single-Agent |
  | Anfragen, die Live-Daten oder externe Aktionen brauchen | Tool-Using-Agent |
  | Ein Prozess mit vorhersehbaren Schritten, gemischt mit Reasoning-Schritten | Workflow + Agent |
  | Eingaben, die in deutlich unterschiedlichen Typen eintreffen | Router |
  | Ausgaben, die geprüft werden müssen, bevor sie den Nutzer erreichen | Evaluator |
  | Eine komplexe Aufgabe, die von spezialisierten Teilaufgaben profitiert | Supervisor-Worker |
Für Velas aktuelles Problem, interne Anfragen über drei verwandte Bereiche, Single-Agent bestätigt, ist das richtige Muster ein gut entworfener Single-Agent, eventuell mit einem oder zwei angebundenen Tools, falls Live-Bestand oder Lieferantendaten nötig werden. Genau dieses Muster baut der Sprint-1-Walkthrough.
## Verständnischeck
>  Selin prüft eine neue Anforderung aus Velas Operations-Team. Wenn ein Consultant eine Anfrage an den Agenten sendet, entwirft der Agent eine Antwort. Bevor sie ausgeliefert wird, muss aber geprüft werden, dass sie keine veralteten Lieferantenbedingungen erwähnt. Welches Muster bearbeitet diese Anforderung?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7d9db5bc-8ba6-4d1b-b53a-e91531f4eb9b
## Zusammenfassung
Sechs Muster decken den Großteil realer Agentenarchitekturen ab: Single-Agent, Tool-Using-Agent, Workflow + Agent, Router, Evaluator und Supervisor-Worker. Jedes löst ein anderes Designproblem. Router und Evaluator sind leicht zu verwechseln, weil beide einen Entscheidungs-Node beinhalten. Der Unterschied liegt darin, ob sich die Entscheidung auf die eingehende Eingabe oder die ausgehende Ausgabe bezieht.
Für den Moment ist Velas Antwort ein gut entworfener Single-Agent. Die nächste Lektion ergänzt die zweite Ebene: Sobald ein Muster gewählt ist, bestimmen drei Designpfeiler, Orchestrierung, Kommunikation und Zustandsverwaltung, ob die Canvas, die auf diesem Muster aufgebaut wird, in der Produktion auch wirklich standhält.