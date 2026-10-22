# Was ist MCP und wie man MCP Tools in Agentflow v2 verbindet

Notion page: https://app.notion.com/p/Was-ist-MCP-und-wie-man-MCP-Tools-in-Agentflow-v2-verbindet-3789418319f380a68d99f8aaa2b5d19b
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du verstehst, was MCP ist, warum es existiert und wie du MCP Tools mit Agentflow-v2-Nodes verbindest.

## Ausgangslage
Meridians Agent ist mit drei Fähigkeiten verbunden: einem Document Store, einem HTTP Node für Live-Daten und einem Iteration Flow für Briefings. Jede Verbindung erforderte eine individuelle Konfiguration: Credentials, URL-Endpoints, Response Handling und Fehlerlogik, die speziell für jede Integration geschrieben wurde.
Wenn Meridian morgen denselben Agenten in einem anderen Framework neu bauen würde, müsste jede Integration von Grund auf neu konfiguriert werden. Nutzt ein Kunde einen eigenen Agenten auf einer anderen Plattform und will er auf Meridians Wissensdatenbank zugreifen, müsste die gesamte Integrationsschicht komplett neu gebaut werden.
Das ist das Integrationsproblem, das MCP löst.
## Was MCP ist
Das Model Context Protocol ist ein offener Standard, der eine universelle Schnittstelle dafür definiert, wie KI-Agenten sich mit externen Tools und Datenquellen verbinden. Es wurde Ende 2024 von Anthropic eingeführt und seitdem über Agenten-Frameworks, Entwicklungsumgebungen und Enterprise-Plattformen hinweg übernommen.
Die Analogie, die es am klarsten erfasst, ist USB-C. Vor standardisierten Ports musste man beim Anschließen eines Peripheriegeräts wissen, welchen spezifischen Anschluss jedes Gerät verwendete. USB-C bietet einen universellen Verbindungsstandard, und jedes kompatible Peripheriegerät verbindet sich über denselben Port mit jedem kompatiblen Gerät. MCP tut dasselbe für KI-Agenten und externe Tools.
Ein MCP Server stellt drei Kategorien von Fähigkeiten bereit:
[TABLE]
  | Kategorie | Was sie bereitstellt |
  | Tools | Funktionen, die der Agent aufrufen kann, um Aktionen auszuführen oder Daten abzurufen |
  | Resources | Datenquellen, aus denen der Agent lesen kann |
  | Prompts | Wiederverwendbare Prompt Templates, die auf dem Server gespeichert sind |
Wenn ein neues Tool oder eine neue Resource zu einem MCP Server hinzugefügt wird, entdecken verbundene Agenten sie automatisch, ohne dass Updates an der Agentenkonfiguration erforderlich sind.
### Wie MCP in Agentflow v2 funktioniert
Agentflow v2 ermöglicht, MCP Tools als Teil des Workflows zu verbinden, statt sie ausschließlich als Agenten-Tools funktionieren zu lassen. Custom MCPs können außerdem unabhängig erstellt werden, ohne von plattformbereitgestellten Integrationen abhängig zu sein. MCP gilt weithin als Industriestandard und wird typischerweise von den offiziellen Anbietern unterstützt und gewartet.
In Agentflow v2 verbinden sich MCP Tools über die Tools-Konfiguration des Agent Nodes. Sobald ein MCP Server in Flowise konfiguriert ist, erscheinen seine Tools im Tool Selector des Agent Nodes neben nativen Flowise Tools. Der Agent kann sie dann dynamisch basierend auf Reasoning aufrufen, genau wie jedes andere Tool.
![image]((notion-hosted file))
Das bedeutet, dass Meridians Agent Node A sich mit einem Jira MCP Server verbinden und Tickets erstellen, einen GitHub MCP Server nach Repository-Kontext abfragen oder Live-Daten aus einem Brave Search MCP Server abrufen könnte. Und das alles, ohne für jedes einzelne davon Custom-API-Integrationscode zu schreiben.
### Warum MCP für das Meridian-Projekt wichtig ist
Drei spezifische Vorteile gelten direkt für das, was gebaut wurde:
- Cross-Framework-Interoperabilität: Ein MCP Server für Meridians Document Store lässt sich gleichzeitig von einem Flowise-Agenten, einem Langflow-Agenten und einer Claude-Umgebung nutzen, ohne dass die Integration für jede Plattform neu gebaut werden muss.
- Reduzierter Integrationsaufwand: Statt Custom Connectors für jedes Tool in jedem Framework zu schreiben, baut ein Team einen MCP Server pro Tool. Jeder MCP-kompatible Agent kann dann über dieselbe standardisierte Schnittstelle darauf zugreifen.
- Ökosystem-Komponierbarkeit: MCP verwandelt isolierte Agenten-Frameworks in ein verbundenes Ökosystem. Baut man ein Tool für eine Plattform, steht es damit automatisch allen anderen Plattformen zur Verfügung, die den Standard unterstützen.
### MCP versus HTTP Node
Falls du Sprint 2 schon durchgearbeitet hast, fällt dir wahrscheinlich eine Ähnlichkeit zwischen MCP Tools und dem HTTP Node auf. Beide verbinden den Agenten mit externen Systemen. Der Unterschied liegt in dem Scope und der Standardisierung:
[TABLE]
  |  | HTTP Node | MCP Tool |
  | Setup | Pro Endpoint konfigurieren | Einmal pro Server konfigurieren |
  | Discovery | Manuell: Du definierst jeden Call | Automatisch: Agent entdeckt verfügbare Tools |
  | Portabilität | Spezifisch für diesen Canvas | Für jeden MCP-kompatiblen Agenten verfügbar |
  | Am besten für | Einmalige API Calls | Wiederverwendbare Multi-Tool-Integrationen |
Der HTTP Node ist die richtige Wahl für einen einzelnen spezifischen API Call. MCP ist die richtige Wahl, wenn ein Tool wiederverwendbar, auffindbar und über mehrere Agenten-Frameworks hinweg verfügbar sein muss.
## Verständnischeck
>  Meridian baut einen einzelnen MCP Server, der seinen Document Store als Resource bereitstellt. Eine Kundenorganisation möchte aus ihrem eigenen Flowise-Agenten auf dieselbe Wissensdatenbank zugreifen. Was muss der Kunde tun?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8b1e062d-8df7-4a1f-970b-021bbd010a66


> 💡 Fazit:
  MCP tut für KI-Agenten-Integrationen, was USB-C für Hardware-Konnektivität getan hat. Es ersetzt eine fragmentierte Landschaft von Custom Connectors durch einen einzigen universellen Standard. Ein MCP Server pro Tool. Jeder kompatible Agent kann ihn verwenden. Wenn eine neue Fähigkeit zum Server hinzugefügt wird, entdecken alle verbundenen Agenten sie automatisch. Für Meridians Agenten und seine Kunden bedeutet das, dass einmal gebaute Integrationen überall verfügbar werden.