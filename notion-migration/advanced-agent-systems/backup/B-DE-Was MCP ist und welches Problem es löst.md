# Was MCP ist und welches Problem es löst

Notion page: https://app.notion.com/p/Was-MCP-ist-und-welches-Problem-es-l-st-6409418319f38213af3401d82131e353
Backed up before n8n migration

Sofias Intake-Agent (aus der vorherigen Lektion) erledigt eine Aufgabe gut: Er klassifiziert eine Kundennachricht und schreibt strukturierten Kontext in Flow State. Aber das ist nur die erste Hälfte eines echten Support-Workflows. Um das Problem eines Kunden tatsächlich zu lösen, muss der Specialist-Agent die Bestellung des Kunden in Cascadias Bestelldatenbank nachschlagen, den Versandstatus über die API des Frachtführers prüfen und Garantiedatensätze aus dem System des Compliance-Teams abrufen.
Traditionell erforderte jede einzelne dieser Integrationen Custom Code. Sofias Team würde einen Connector für die Bestelldatenbank schreiben, einen weiteren für die Versand-API, einen weiteren für die Garantiedatensätze, jeweils mit eigenem Format, eigener Fehlerbehandlung und eigener Authentifizierung. Jedes neue Tool, das der Agent braucht, ist eine weitere Wartungsbelastung.
Dadurch entsteht ein bekanntes Problem: Agenten werden leistungsfähiger, aber die Anbindung an reale Systeme wird zum Engpass. Wenn die Anzahl der Tools wächst, wächst der Integrationsaufwand schneller als der Wert, den der Agent erzeugt.
Model Context Protocol (MCP) wurde entwickelt, um genau dieses Problem zu lösen.
## Das Integrationsproblem
Stell dir vor, du baust einen AI-Assistenten für ein Unternehmen. Der Assistent muss interne Dokumente durchsuchen, Dateien aus Google Drive lesen, eine PostgreSQL-Datenbank abfragen, Jira-Tickets erstellen, Slack-Nachrichten senden und Automatisierungs-Workflows auslösen. Ohne einen gemeinsamen Integrationsstandard braucht jedes System seine eigene Custom Integration. Jedes Tool kann andere Authentifizierungsmethoden, API-Designs, Anfrageformate und Antwortstrukturen verwenden. Kommen weitere Tools dazu, wächst der Integrationsaufwand schnell, und das System wird schwerer zu entwickeln, zu warten und zu skalieren. Das ist die Herausforderung, die Model Context Protocol (MCP) lösen soll.
![image]((notion-hosted file))
## Was ist MCP?
Model Context Protocol (MCP) ist ein offenes Protokoll, das AI-Modellen und Agenten ermöglicht, über eine standardisierte Schnittstelle mit externen Tools und Datenquellen zu kommunizieren.
Statt für jedes System eine Custom Connection zu bauen, implementieren Entwickler den MCP-Standard einmal.
Ein MCP-kompatibler Agent kann dann mit jedem MCP-kompatiblen Tool arbeiten.
Du kannst dir MCP wie einen universellen Reiseadapter vorstellen.
Wenn du zwischen Ländern reist, kann jedes Land andere Steckdosen haben. Ohne universellen Adapter brauchst du für jedes Reiseziel einen anderen Stecker. Je mehr Länder du besuchst, desto mehr Adapter musst du mitnehmen.
MCP funktioniert für AI-Agenten ähnlich. Statt für jedes Tool, jede Datenbank oder jede Anwendung eine andere Verbindung zu bauen, verbindet sich der Agent über einen gemeinsamen Standard. Solange ein Tool MCP unterstützt, kann der Agent damit interagieren, ohne eine Custom Integration zu brauchen.
## MCP-Architektur
Auf hoher Ebene führt MCP zwei Hauptkomponenten ein:
[TABLE]
  | Komponente | Zweck |
  | MCP-Client | Der Agent oder die Anwendung, die Zugriff anfordert |
  | MCP-Server | Das System, das Tools, Ressourcen oder Aktionen bereitstellt |
Der Agent muss keine Implementierungsdetails kennen und fragt stattdessen den MCP-Server:
- Welche Tools sind verfügbar?
- Welche Parameter braucht dieses Tool?
- Wie soll ich es aufrufen?
Der MCP-Server stellt diese Informationen in einem Standardformat bereit.
![image]((notion-hosted file))
## Womit kann MCP verbinden?
Ein MCP-Server kann einem AI-Agenten viele verschiedene Arten von Ressourcen bereitstellen. Dazu gehören Dateien wie PDFs, Tabellen und Dokumente, Datenbanken wie PostgreSQL, MySQL oder Snowflake, externe APIs wie Wetterdienste, CRM-Systeme oder ERP-Plattformen, Wissensdatenbanken wie Notion, Confluence und SharePoint, Kommunikationstools wie Slack, Microsoft Teams und Gmail, Automatisierungsplattformen wie n8n, Zapier und Make, sowie Entwickler-Tools wie GitHub, GitLab und Jira.
Der zentrale Vorteil von MCP ist, dass all diese Ressourcen aus Sicht des Agenten als auffindbare Tools erscheinen, auf die über ein konsistentes Interaktionsmuster zugegriffen wird. Dadurch kann der Agent mit vielen unterschiedlichen Systemen arbeiten, ohne für jedes einzelne eine Custom-Integration zu brauchen.
## Warum MCP für Agenten wichtig ist
MCP wird wichtig, weil Agenten selten isoliert arbeiten. Die meisten nützlichen Agenten brauchen Zugriff auf Informationen, die Fähigkeit, Aktionen auszuführen, und Verbindungen zu Geschäftssystemen, während sie über mehrere Tools und Plattformen hinweg arbeiten. Traditionell erforderte jede neue Integration eigenen Engineering-Aufwand: Entwickler mussten für jedes System separate Verbindungen bauen und warten.
MCP begegnet dieser Herausforderung, indem es Agenten eine standardisierte Möglichkeit gibt, externe Ressourcen zu entdecken und mit ihnen zu interagieren. Dadurch wird die Integration neuer Tools einfacher, die Erweiterung der Fähigkeiten eines Agenten braucht keine Änderungen an seiner Kernlogik mehr, und Organisationen profitieren von einem wachsenden Ökosystem kompatibler Tools, die von verschiedenen Anbietern gebaut werden. So können sich Entwickler auf das Design intelligenten Agentenverhaltens konzentrieren, statt Zeit mit Integrations- und Infrastrukturarbeit zu verbringen.
## Verständnischeck
### Frage 1
>  Dein Agent muss auf mehrere Systeme zugreifen:
  - Eine PostgreSQL-Datenbank
  - Ein Dateispeichersystem
  - Eine Ticketing-Plattform
  Welche Aussage beschreibt die Rolle von MCP am besten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/3e5c66c1-c6bd-44c6-90eb-3e452ddf315e
## Zusammenfassung
Vor MCP würde jedes Tool, das Sofia bei Cascadia braucht, seinen eigenen Custom Connector erfordern: einen für die Bestelldatenbank, einen weiteren für die Versand-API, einen weiteren für das Garantiesystem. MCP ersetzt diese Integrationsarbeit pro Tool durch ein Standardprotokoll, an das jedes MCP-kompatible Tool andocken kann.
In der nächsten Lektion verbindet Sofia ein echtes MCP-Tool mit einem Flowise-Agenten und beobachtet, wie der Agent es entdeckt und aufruft.
