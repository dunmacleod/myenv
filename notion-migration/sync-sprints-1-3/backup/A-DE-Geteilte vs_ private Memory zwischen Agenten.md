# Geteilte vs. private Memory zwischen Agenten

Notion page: https://app.notion.com/p/Geteilte-vs-private-Memory-zwischen-Agenten-9369418319f38396aefd815ed905b876
Backed up before n8n migration

Jonas hatte einen Screenshot geschickt. Zwei Nachrichten, dieselbe Session. Der Commercial-Agent hatte auf die Preisfrage eines Kunden mit den korrekten Tier-Details geantwortet. Zehn Sekunden später hatte der Technical-Agent demselben Kunden gesagt, dass sein Account im Free Tier sei. Beide Agenten verwendeten allMessages-Memory. Beide lasen dieselbe Konversationshistorie. Das Problem war, dass der Commercial-Agent eine Arbeitsannahme zum Account in den geteilten Kontext geschrieben hatte (etwas, das er intern nutzte, um seine Antwort zu kalibrieren), und der Technical-Agent diese Annahme als Fakt gelesen hatte.
Die Agenten waren nicht kaputt. Sie teilten Memory, die sie nicht hätten teilen sollen.
Das ist die praktische Version der Designfrage aus der vorherigen Lektion. Diesmal geht es nicht darum, wo die Memory ist, sondern darum, welche Agenten sie lesen dürfen. In einem Single-Agent-System stellt sich diese Frage gar nicht. Es gibt nur einen Leser. In einem Multi-Agent-System wie der Vela-Canvas ist das anders. Jede Information in geteilter Memory ist für jeden Agenten verfügbar, ob das beabsichtigt war oder nicht.
> 💡 Diese Lektion ist eine Designübung. Es gibt keine Canvas zu bauen. Die Aufgabe besteht darin, die Memory-Grenzen des Vela-Systems zu kartieren. Anschließend wendest du dasselbe Denken auf deinen eigenen Projektagenten an.

## Was geteilt und privat in der Praxis bedeuten
Geteilte Memory ist jede Information, die ein Agent schreibt und ein anderer Agent lesen kann. In der Vela-Canvas sind $flow.state-Schlüssel absichtlich geteilt. Jeder Node in der Canvas kann sie lesen. allMessages-Memory auf jedem Agent-Node teilt standardmäßig ebenfalls die Konversationshistorie, was bedeutet, dass ein Agent, der allMessages liest, alles sieht, was in der Session gesagt wurde, einschließlich dessen, was andere Agenten beigetragen haben.
Private Memory ist Information, die zum Ausführungskontext eines Agenten gehört. Für andere Agenten ist sie nicht zugänglich. Eine lokale Variable innerhalb eines Custom-Function-Node ist privat. Sie verschwindet, wenn der Node beendet ist. Ein System-Prompt ist ebenfalls privat. Er weist einen Agenten an und wird nicht an den nächsten weitergegeben. Bei strukturierten Ausgabefeldern kommt es auf den Zeitpunkt an. Bis sie in einen Flow-State-Schlüssel geschrieben werden, sind sie privat. Sobald sie geschrieben sind, werden sie geteilt.
Die Grenze zwischen geteilt und privat ist beim Blick auf die Canvas nicht immer offensichtlich. allMessages wirkt wie eine Einstellung pro Agent. Tatsächlich liest es aber aus der Konversationshistorie, die auch die Turns anderer Agenten enthält. Flow State wirkt wie ein technisches Detail. Tatsächlich ist es die klarste geteilte Oberfläche in der ganzen Canvas.
## Die drei Designfragen
Bevor du entscheidest, was geteilt und was privat ist, beantworte drei Fragen für jedes Informationselement im System.
1. Braucht der empfangende Agent diese Information, um seine Aufgabe zu erfüllen? Braucht der Technical-Agent die Preis-Tier-Annahme des Commercial-Agent nicht, um eine technische Anfrage korrekt zu beantworten, sollte diese Annahme nicht in geteilter Memory liegen. Bedarf ist der Test. Bequemlichkeit nicht.
1. Könnte der empfangende Agent diese Information falsch lesen? Eine Arbeitsannahme ist kein Fakt. Ein Zwischenlabel der Klassifizierung ist kein Kundenattribut. Manches ist im Kontext des einen Agenten korrekt, im Kontext eines anderen aber irreführend. Solche Informationen solltest du entweder gar nicht teilen, oder du kennzeichnest sie klar als agenteninternen Wert, falls sie doch in Flow State geschrieben werden müssen.
1. Was kostet es, wenn diese Information falsch oder veraltet ist? Manche Informationen sind risikoarm zu teilen, etwa die ursprüngliche Kundenanfrage oder die Routing-Entscheidung. Andere Informationen sind riskant. Ein Account-Status, den der Agent nur abgeleitet statt nachgeschlagen hat. Eine Berechtigungsstufe, die er aus dem Kontext geschlossen hat. Solche riskanten, abgeleiteten Informationen solltest du direkt aus der Quelle holen, statt sie zwischen Agenten weiterzugeben. Alternativ validierst du sie, bevor der nächste Agent sie nutzt.
## Die Vela-Canvas: Kartieren, was geteilt ist
Öffne die Sprint-2-Canvas. Das ist die Multi-Agent-Canvas mit Classifier, Commercial-Agent, Technical-Agent und Hybrid Handler, die du im vorherigen Sprint gebaut hast. Identifiziere jedes Informationselement, das die Canvas an einen Ort schreibt, den mehrere Agenten lesen können. Arbeite dafür die Flow-State-Schlüssel durch und die Konversationshistorie, die allMessages verfügbar macht.
Die Canvas schreibt derzeit drei Schlüssel in $flow.state:
- query_type, gesetzt durch den LLM-Classifier-Node. Wert: commercial, technical oder hybrid.
- confidence, gesetzt durch den LLM-Classifier-Node. Wert: high oder low.
- client_query, gesetzt durch den LLM-Classifier-Node. Wert: die ursprüngliche Kundennachricht.
Jeder Spezialagent (Commercial Agent, Technical Agent, Hybrid Handler) liest außerdem allMessages-Memory. Das bedeutet: Jeder Agent sieht die vollständige Konversationshistorie. Dazu gehört auch die Ausgabe des Classifier und jede vorherige Agentenantwort.
Vervollständige für jedes Informationselement diese Tabelle. Nutz die drei Designfragen, um die Spalte Begründung auszufüllen.
[TABLE]
  | Information | Aktueller Ort | Sollte sie geteilt werden? | Begründung |
  | query_type | $flow.state |  |  |
  | confidence | $flow.state |  |  |
  | client_query | $flow.state |  |  |
  | Reasoning Trace des Classifier (implizit in allMessages) | allMessages-Historie |  |  |
  | Antwort des Commercial-Agent (für nachgelagerte Agenten in allMessages sichtbar) | allMessages-Historie |  |  |
Beantworte die Spalte „Sollte sie geteilt werden?" mit Ja, Nein oder Ja, mit Bedingungen. Schreib für jede Entscheidung eine Begründung in einem Satz. Es gibt nicht für jede Zeile eine einzige richtige Antwort. Die richtige Antwort hängt davon ab, wie das System funktionieren soll.
### LLM-Node JSON Structured Output
[COLUMN_LIST]
  [COLUMN]
    ![image]((notion-hosted file))
  [COLUMN]
    ![image]((notion-hosted file))
  [COLUMN]
    ![image]((notion-hosted file))

### LLM Node Update Flow State
![image]((notion-hosted file))

## Identifizieren, was privat sein sollte
Drei Kategorien von Informationen sind in den meisten Multi-Agent-Systemen Kandidaten für private Behandlung.
- Agenteninterne Arbeitswerte. Zwischenergebnisse, die der Agent auf dem Weg zu einer Antwort erzeugt, nicht die Antwort selbst. Der Confidence Score des Classifier ist grenzwertig. Er könnte für den Condition-Node nützlich sein. Er sollte aber wahrscheinlich nicht die Antworten der Spezialagenten beeinflussen. Die interne Account-Tier-Annahme des Commercial-Agent ist eindeutig intern.
- Inhalte von System-Prompts. Die Anweisungen jedes Agenten sind absichtlich privat. Sie werden nicht in Flow State oder in allMessages geschrieben. Das ist korrektes Verhalten und sollte so bleiben. Achte trotzdem auf eine Falle: Ein schlecht geschriebener System-Prompt könnte einen Agenten dazu bringen, seine eigenen Anweisungen in der Antwort zu wiederholen. Diese Antwort landet dann in allMessages und leakt so zum nächsten Agenten.
- Sensible oder flüchtige Eingaben. Teilt ein Kunde während der Session Authentifizierungsdaten, einen temporären Code oder personenbezogene Informationen, sollten diese Informationen nicht über den Turn des bearbeitenden Agenten hinaus bestehen bleiben. Speicherst du sie in Flow State oder verlässt du dich darauf, dass allMessages sie weiterträgt, entsteht ein Retentionsproblem.
Identifizier für die Vela-Canvas ein Informationselement aus jeder der oben genannten Kategorien, das ein Datenschutz- oder Zuverlässigkeitsproblem ist oder werden könnte. Schreib jeweils eine einzeilige Notiz dazu, wie du es behandeln würdest.
## Das Framework auf dein Projekt anwenden
> 🔥  Bevor du startest, erstell dir eine Kopie von dieser Vorlage. Sie spiegelt den Aufbau dieser Lektion wider: ein Tab für die Shared-or-Private-Zuordnung von Vela, eines für die drei privaten Kandidatenkategorien und eines für die Vier-Schritte-Anwendung auf dein Projekt.
Die Vela-Aufgabe dient lediglich als Übung. Die eigentliche Abgabe besteht darin, eine Memory-Boundary-Map für deinen eigenen Projektagenten zu erstellen. Dein System begann ursprünglich als Single-Agent-Ansatz. Durch Sprint 2 hast du inzwischen ein Multi-Agent-Design erarbeitet, sei es bereits implementiert oder als verworfene Alternative dokumentiert. In jedem Fall hast du dabei mindestens zwei Agentenrollen definiert. Wende die drei Designfragen nun auf dein eigenes System an.
Arbeite diese Schritte durch:
1. Schritt 1: Liste alle Agenten deines Designs auf. Falls dein Diagramm aus Sprint 2 beispielsweise einen Koordinator und zwei Spezialisten vorsieht, notiere alle drei. Solltest du dich für ein Single-Agent-System entschieden haben, erfasse nur diesen einen Agenten und betrachte einen potenziellen ‚zweiten Agenten‘ als hypothetische, zukünftige Erweiterung. Systemgrenzen konsequent zu durchdenken, ist eine Methodik, die sich nämlich auch bei Single-Agent-Systemen auszahlt.
1. Schritt 2: Liste jedes Informationselement auf, das zwischen den Agenten ausgetauscht werden könnte. Berücksichtige dabei Flow-State-Schlüssel, alles, was über llmUpdateState geschrieben wird, sowie sämtliche Daten, die durch allMessages für nachgelagerte Agenten zugänglich werden.
1. Schritt 3: Wende die drei Leitfragen auf jedes dieser Elemente an: Benötigt der empfangende Agent diese Information zwingend? Könnte er sie falsch interpretieren? Welche Konsequenzen hätte ein solcher Fehler?
1. Schritt 4: Dokumentiere deine Entscheidungen zu den Informationsgrenzen. Gib für jedes Element an, ob es geteilt wird (und warum), ob es privat bleibt (und warum) oder ob es nur unter bestimmten Bedingungen geteilt wird (und unter welchen).

> ➡️ Dieses Dokument ist der Memory-Boundary-Abschnitt deiner Sprint-3-Projektabgabe. Bewahr es gut auf. In der Lektion zur Sprint-3-Projektabgabe integrierst du es mit dem Rest der Architekturspezifikation.

>  
  ### 🔥 AI nutzen, wenn du feststeckst
  Fällt es dir schwer zu entscheiden, ob ein bestimmtes Informationselement geteilt oder privat sein sollte, beschreib die Situation klar für AI:
  - Nenn die zwei beteiligten Agenten.
  - Beschreib die fragliche Information: was sie ist, woher sie kommt und was ein nachgelagerter Agent damit tun würde.
  - Frag, ob das Teilen ein Zuverlässigkeits- oder Interpretationsproblem verursachen könnte.
  Zum Beispiel: „In a Flowise multi-agent system, the first agent classifies a client query and writes a confidence score to $flow.state. The second agent is a specialist that responds to the query. Should the specialist read the confidence score? What could go wrong if it does?"
  Nutz die Antwort, um deine Entscheidung einem Pressure Test zu unterziehen, nicht um sie zu ersetzen.

## Worauf du achten solltest
- allMessages als standardmäßig sicher behandeln. allMessages ist ein Node-Level-Schalter und fühlt sich wie eine Einstellung pro Agent an. Deshalb nimmt man leicht an, jeder Agent habe seine eigene, isolierte Memory. Das stimmt nicht. Jeder Agent-Node mit aktiviertem allMessages liest aus derselben Session-Konversationshistorie. Hat ein Agent etwas Irreführendes in diese Historie geschrieben, übernimmt der nächste Agent automatisch das Problem.
- „Dieser Agent hat es geschrieben" mit „dieser Agent besitzt es" verwechseln. Einen Wert in $flow.state zu schreiben bedeutet nicht, dass nur dieser Agent ihn nutzen wird. Jeder nachgelagerte Node kann ihn lesen. Behandle Flow-State-Schreibvorgänge deshalb wie ein Veröffentlichen, nicht wie ein Speichern.
- Die Grenzentscheidung implizit lassen. Die häufigste Quelle von Memory-Bugs in Multi-Agent-Systemen ist gar keine bewusste Entscheidung. Wurde die Grenze nicht explizit gewählt, gilt standardmäßig „alles geteilt". Das war selten beabsichtigt.
## Zusammenfassung
Geteilte Memory in einem Multi-Agent-System ist nicht nur eine Bequemlichkeit. Sie ist eine Designoberfläche. Sie bestimmt, was jeder Agent weiß. Sie bestimmt, was er falsch lesen könnte. Und sie bestimmt, was passiert, wenn Informationen aus dem Kontext eines Agenten in den eines anderen leaken. Die drei Fragen aus dieser Lektion (Bedarf, Risiko des falschen Lesens und Kosten eines Fehlers) geben dir ein Framework. Mit ihm triffst du diese Entscheidungen explizit, statt einfach die Defaults zu akzeptieren.
Die Boundary Map, die du im Abschnitt „Das Framework anwenden" erstellt hast, ist die erste konkrete Ausgabe deiner Sprint-3-Projektabgabe. Die nächste Lektion fügt eine zweite Ebene hinzu. Es geht dann nicht mehr nur darum, was geteilt und was privat ist. Es geht darum, was überhaupt niemals gespeichert werden darf. Das sind Informationen, die über den Agenten-Turn hinaus, der sie bearbeitet hat, keine Spur hinterlassen sollten.