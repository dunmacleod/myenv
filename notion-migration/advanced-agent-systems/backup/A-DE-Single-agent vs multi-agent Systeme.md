# Single-agent vs multi-agent Systeme 

Notion page: https://app.notion.com/p/Single-agent-vs-multi-agent-Systeme-5d19418319f382a08df78130eb29cd3a
Backed up before n8n migration

Nachdem Selin überprüft hatte, was bei der ersten Version von Velas Agent schiefgelaufen war, setzte sie eine kurze Planungssitzung mit Jonas und Petra an. Die Schlussfolgerung aus der vorherigen Lektion war klar: Der Agent scheiterte, weil er keinen Architekturplan hatte. Jetzt muss das Team seine erste echte Designentscheidung treffen, bevor es irgendetwas auf der Canvas neu aufbaut.
Ein Kollege aus einem anderen Team hat vorgeschlagen, dass die Lösung einfach sei: „Fügt einfach mehr Agenten hinzu." Selin ist nicht überzeugt. Mehr Agenten bedeuten mehr Nodes, mehr Koordinationslogik, mehr Stellen, an denen etwas schiefgehen kann, und mehr API-Aufrufe pro Anfrage. Das hat Kosten, bei der Latenz, bei den Token und beim Debugging-Aufwand. Die Frage ist, ob Velas Problem tatsächlich eines erfordert.
Diese Lektion gibt dem Team (und Ihnen) das Framework, um diese Frage zu beantworten.
## Was ein Single-Agent-System ist
Ein Single-Agent-System hat einen Agent-Node, der das gesamte Reasoning übernimmt. Er erhält die Eingabe des Nutzers, entscheidet, was zu tun ist, nutzt alle Tools oder Wissensquellen, auf die er Zugriff hat, und erzeugt eine Antwort. Der gesamte Entscheidungsweg läuft durch einen Node.
Das ist keine Einschränkung. Ein gut entworfenes Single-Agent-System kann Routing-Logik, Tool-Nutzung, Memory über mehrere Gesprächsrunden hinweg und verschiedene Anfragetypen verarbeiten, alles innerhalb eines Agent-Node, gesteuert durch einen klaren System-Prompt und verbunden mit den richtigen Eingaben.
Velas aktuelle Baseline ist ein Single-Agent-System. Ein Start-Node, ein Agent-Node, ein Direct-Reply-Node. Der Agent-Node nutzt Gemini, um über jede Anfrage nachzudenken und zu antworten. An dieser Struktur ist nichts falsch. Die Frage ist, ob sie für Velas Anforderungen ausreicht.
## Was ein Multi-Agent-System ergänzt
Ein Multi-Agent-System hat mehr als einen Agent-Node, jeweils mit einer definierten Rolle. Ein Agent könnte Informationsanfragen bearbeiten. Ein anderer bearbeitet Aktionsanfragen. Ein Supervisor-Agent könnte anhand der eingehenden Anfrage entscheiden, welcher Spezialagent eingebunden wird. Die Agenten koordinieren sich: Sie übergeben Kontext, Ergebnisse und Kontrolle über die Canvas aneinander.
Multi-Agent-Systeme lösen eine bestimmte Gruppe von Problemen, die einzelne Agenten tatsächlich nicht lösen können:
- Spezialisierung in großem Maßstab. Wenn ein einzelner Agent zu viele verschiedene Aufgabentypen bearbeitet, wird sein System-Prompt lang, seine Tool-Liste wächst, und seine Routing-Entscheidungen werden unzuverlässig. Die Aufteilung der Arbeit auf Spezialagenten (jeweils mit engem, klar definiertem Scope) führt zu konsistenteren Ergebnissen.
- Parallele oder sequenzielle Arbeit. Manche Aufgaben erfordern, dass ein Schritt abgeschlossen ist, bevor ein anderer beginnen kann, oder dass zwei Schritte gleichzeitig laufen. Ein einzelner Agent erledigt jeweils eine Sache in einer linearen Schleife. Multi-Agent-Architekturen können die Arbeit anders strukturieren.
- Fehlerisolierung. Wenn ein Agent in einem Multi-Agent-System scheitert, beschädigt sein Fehler nicht zwangsläufig die anderen. Ein Fehler in einem Single-Agent-System ist ein vollständiger Fehler.
Diese Vorteile sind mit konkreten Kosten verbunden: mehr Nodes, mehr Koordinationslogik, höhere Latenz pro Anfrage, mehr verbrauchte Token pro Interaktion und schwierigeres Debugging, wenn etwas zwischen Agenten schiefgeht statt innerhalb eines einzelnen Agenten.
## Das Entscheidungsframework
Die Wahl zwischen Single-Agent und Multi-Agent sollte sich aus dem Problem ergeben, nicht aus einer Vorliebe für Komplexität. Vier Fragen machen die Entscheidung klar.
![image]((notion-hosted file))
1. Kann ein gut abgegrenzter Agent die gesamte Bandbreite der Eingaben zuverlässig bearbeiten?
Wenn der Scope des Agenten eng genug ist, dass ein klarer System-Prompt alle Anfragetypen steuern kann, ohne unhandlich zu werden, ist ein einzelner Agent angemessen. Velas Agent beantwortet Fragen zu Bestand, Auftragsabwicklung und Lieferantenkommunikation; drei verwandte Bereiche, die Kontext teilen. Ein gut abgegrenzter Agent könnte alle drei abdecken.
2. Erfordert die Arbeit Spezialwissen oder Tools, die miteinander in Konflikt stehen?
Wenn unterschiedliche Anfragetypen grundlegend unterschiedliche Tools, Zugriffsebenen oder Reasoning-Ansätze benötigen (und ihre Kombination Routing-Verwirrung erzeugt), liefern spezialisierte Agenten bessere Ergebnisse. Wenn Tools und Wissen gut in einem System-Prompt zusammenarbeiten, müssen sie nicht aufgeteilt werden.
3. Muss ein Fehler in einem Teil vom Rest isoliert werden?
Wenn ein Fehler nicht dazu führen sollte, dass der gesamte Agent stoppt, bietet Multi-Agent Isolationsgrenzen. Wenn ein vollständiger Fehler bei einer Anfrage akzeptabel und behebbar ist, reicht Single-Agent aus.
4. Ist der Komplexitätsaufwand durch den Zuverlässigkeitsgewinn gerechtfertigt?
Multi-Agent-Systeme sind schwieriger zu bauen, zu testen und zu debuggen. Wenn der Zuverlässigkeitsgewinn durch die Aufteilung in Agenten den eingeführten Koordinationsaufwand nicht überwiegt, ist die Komplexität nicht verdient. Standardmäßig sollte das einfachere System gewählt werden, bis das Problem mehr verlangt.
[TABLE]
  | Signal | Weist eher auf |
  | Der Scope ist eng und stabil | Single-Agent |
  | Der System-Prompt wird lang und unzuverlässig | Multi-Agent |
  | Alle Tools gehören logisch zusammen | Single-Agent |
  | Tools stehen in Konflikt oder erzeugen Routing-Verwirrung | Multi-Agent |
  | Ein Fehler sollte die gesamte Antwort stoppen | Single-Agent |
  | Ein Fehler in einem Teil sollte andere nicht stoppen | Multi-Agent |
  | Der Koordinationsaufwand ist im Verhältnis zum Zuverlässigkeitsgewinn gering | Multi-Agent |
  | Der Koordinationsaufwand übersteigt den Zuverlässigkeitsvorteil | Single-Agent |
## Das Framework auf Vela anwenden
Selin geht die vier Fragen anhand von Velas tatsächlichem Problem durch.
Der Agent bearbeitet drei verwandte Bereiche: Bestand, Auftragsabwicklung und Lieferantenkommunikation. Diese teilen genug Kontext, sodass ein System-Prompt alle drei steuern kann, ohne unüberschaubar zu werden. Die Tools, die Vela benötigt, sind logisch kompatibel. Ein Fehler bei einem Anfragetyp muss nicht von den anderen isoliert werden. Und das Team ist klein; Jonas und Petra werden diesen Agenten betreuen, und Koordinationslogik zwischen mehreren Agenten einzuführen, erzeugt Arbeit, die sie im Moment nicht auffangen können.
Die Antwort für Vela ist in dieser Phase ein gut entworfenes Single-Agent-System, weil das Problem die Kosten eines Multi-Agent-Systems noch nicht rechtfertigt.
Diese Schlussfolgerung kann überarbeitet werden. Wenn Velas Agent-Scope erheblich erweitert wird, oder wenn der System-Prompt inkonsistentes Routing erzeugt, oder wenn das Team wächst und komplexere Infrastruktur unterstützen kann, dann ändert sich die Entscheidung. Architekturentscheidungen sind nicht dauerhaft. Sie sind dem Problem zu dem Zeitpunkt angemessen, zu dem sie getroffen werden.
In Ihrer Live-Session wenden Sie dasselbe Framework auf Ihr eigenes Projekt an. Die Entscheidung, die Sie dort treffen, wird die Grundlage Ihres Architektur-Briefings für Sprint 1.
## Zusammenfassung
Der Unterschied zwischen einem Single-Agent- und einem Multi-Agent-System ist eine Frage der Passung. Ein einzelner Agent mit klarem Scope, gut geschriebenem System-Prompt und den richtigen Tools kann ein Multi-Agent-System übertreffen, das für das vorliegende Problem überentwickelt ist.
Das Vier-Fragen-Framework (Scope, Spezialisierung, Fehlerisolierung und Koordinationsaufwand) macht daraus eine vertretbare Entscheidung statt eines Bauchgefühls. Velas Antwort lautet vorerst: Single-Agent. Die nächste Lektion stellt die gesamte Bandbreite verfügbarer Architekturmuster vor, damit Sie sehen können, wo Single-Agent und Multi-Agent in eine breitere Auswahl von Designentscheidungen passen.