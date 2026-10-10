# Integrationsarchitektur-Briefing

Notion page: https://app.notion.com/p/Integrationsarchitektur-Briefing-95f9418319f382559958817716e675dd
Backed up before n8n migration

Du entwirfst ein Multi-Agent-IT-Support-System für Halcyon Labs, ein mittelgroßes Forschungs- und Technologieunternehmen. Dort reichen Engineers, Analystinnen und Analysten sowie Forschende laufend technische Anfragen über den internen Helpdesk ein. Das System soll Nutzern helfen, technische Probleme zu melden, Anfragen zu klassifizieren, relevante Informationen abzurufen und Fälle bei Bedarf an den richtigen spezialisierten Agenten zu routen.
Eine spätere Projektphase, die du in Sprint 3 selbst umsetzt, erweitert das System um eine Research-Retrieval-Funktion. Die verbindet sich mit arXiv, dem kostenlosen Open-Access-Archiv mit fast 2,4 Millionen wissenschaftlichen Artikeln aus Physik, Mathematik, Informatik und verwandten Bereichen. Dein Architektur-Briefing muss beide Phasen abdecken: den initialen IT-Support-Workflow und die spätere arXiv-Integration.
Deine Aufgabe: ein Integrationsarchitektur-Briefing schreiben, das erklärt, welche Kommunikations- und Integrationsprotokolle das Projekt braucht. Du baust das System hier nicht.
## Projektszenario
Das Multi-Agent-IT-Support-System umfasst mehrere Agentenrollen:
Der Intake-Agent nimmt die Anfrage entgegen und identifiziert die Problemkategorie.
Der Knowledge-Agent durchsucht interne Dokumentation, Troubleshooting-Guides und bekannte Problemaufzeichnungen.
Der Ticketing-Agent erstellt oder aktualisiert Tickets im Helpdesk-System der Organisation.
Die Specialist-Agents bearbeiten spezifische Bereiche wie Zugriffsprobleme, Softwareprobleme, Hardwareanfragen und Billing-bezogene IT-Services.
Der Supervisor-Agent prüft unsichere Fälle, Eskalationen und Handoffs zwischen Agenten.
Das System muss sich möglicherweise mit internen Tools verbinden: einer Ticketing-Plattform, einer Wissensdatenbank, einem Asset-Inventar, einem Mitarbeiterverzeichnis und Kommunikationstools.
## Assessment-Aufgabe
Schreib ein Integrationsarchitektur-Briefing, das diese Frage beantwortet:
Braucht das Multi-Agent-IT-Support-System MCP, A2A oder beides?
Dein Briefing sollte folgende Abschnitte enthalten:
### 1. Integrationsbedarf des Projekts
Beschreib, womit sich das System verbinden muss. Geh dabei sowohl auf Tool- und Datenanforderungen als auch auf Anforderungen an die Agentenkommunikation ein, wo relevant.
### 2. MCP-Entscheidung
Gib an, ob MCP nötig ist. Begründe deine Entscheidung: Brauchen die Agenten Zugriff auf Tools, APIs, Datenbanken, Dateien oder Wissensquellen?
### 3. A2A-Entscheidung
Gib an, ob A2A nötig ist. Begründe deine Entscheidung: Müssen unabhängig bereitgestellte Agenten über Systeme, Teams, Frameworks oder Anbieter hinweg kommunizieren?
### 4. Finale Architekturentscheidung
Wähl eine Option:
- Nur MCP
- Nur A2A
- Sowohl MCP als auch A2A
- Weder noch
Erklär deine finale Entscheidung klar.
### 5. Verworfene Option
Begründe, welche Option du verwirfst und warum. Wenn du sowohl MCP als auch A2A wählst, erklär, warum "nur MCP" und "nur A2A" allein nicht reichen würden. Wenn du dich nur für eines von beiden entscheidest, erklär, warum das andere für dieses Projekt nicht gebraucht wird.
## Erwartete Antwortrichtung
Eine gute Antwort kommt in der Regel zu dem Schluss, dass dieses Projekt MCP braucht und je nach Deployment-Annahmen möglicherweise auch A2A.
MCP ist nötig, weil die Agenten auf externe Tools und Datenquellen zugreifen müssen: das Ticketing-System, die Dokumentation, das Asset-Inventar, das Mitarbeiterverzeichnis und eventuell Kommunikationsplattformen.
A2A brauchst du nur, wenn die Specialist-Agents separat bereitgestellte Systeme sind, die über Teams, Frameworks oder Anbieter hinweg zusammenarbeiten müssen. Laufen alle Agenten in einem Flowise-Workflow oder einer gemeinsamen Orchestrierungsumgebung, reicht interne Nachrichtenweitergabe. A2A kannst du für diese Version dann streichen.
Eine gute Architekturentscheidung sieht dann so aus:
Nutz MCP jetzt für Tool- und Datenintegration. Verzicht in der ersten Version auf A2A, außer die Agenten werden unabhängig über verschiedene Systeme hinweg bereitgestellt. Behalt A2A als Option für später im Kopf, falls der Support-Workflow zu separat verantworteten oder separat bereitgestellten Agenten heranwächst.
## Abgabeformat
Reich ein kurzes Architektur-Briefing mit 400 bis 700 Wörtern ein. Nutz klare Abschnittsüberschriften. Schreib keine Implementierungsschritte und beschreib nicht, wie man Flowise konfiguriert. Konzentrier dich auf die Architektur-Begründung.
## Assessment-Checkliste
Deine Abgabe sollte klar beantworten:
- Welche externen Tools oder Datenquellen braucht das System?
- Warum ist MCP nötig oder nicht nötig?
- Warum ist A2A nötig oder nicht nötig?
- Welche Option wählst du?
- Welche Option verwirfst du?
- Warum passt die verworfene Option nicht zum aktuellen Projekt?
## Abschluss
Dieses Assessment prüft, ob du eine echte Architekturentscheidung treffen kannst und nicht nur Protokolle aufzählst. Ein gutes Briefing zeigt, dass du verstehst, womit sich das System verbinden muss, wie die Agenten kommunizieren müssen und welche Integrationsschicht für dieses Projekt wirklich gebraucht wird.