# Demo-Script und Defense

Notion page: https://app.notion.com/p/Demo-Script-und-Defense-3789418319f3806a8adece08fab85f0c
Backed up before n8n migration

> 💡 Darum geht es in diesem Assessment: Dieses Assessment prüft, ob du einen funktionierenden Agenten vor einem nicht-technischen Stakeholder präsentieren kannst, und zwar mit einem strukturierten Demo-Skript, das die zentralen Fähigkeiten zeigt, und einer formalen Verteidigung der Plattform-Entscheidungen gegen Enterprise-Anforderungen. Beide Aufgaben sind erforderlich.
## Darum geht es in diesem Assessment
Meridians Agent ist gebaut, überarbeitet, abgesichert, End-to-End getestet und auditiert. Die Plattform-Entscheidung ist dokumentiert und schriftlich verteidigt. Der letzte Schritt vor der Freigabe zur Produktion ist die Stakeholder-Präsentation.
Meridians CIO hat für das Review dreißig Minuten eingeplant. Die ersten zehn Minuten sind eine Live-Demo der Fähigkeiten des Agenten. Die restlichen zwanzig sind eine formale architektonische Verteidigung. Dem CIO reicht es nicht, dass der Agent funktioniert. Er will wissen, warum er so gebaut wurde, wie er gebaut wurde, und ob man dieser Architektur vertrauliche operative Kundendaten anvertrauen kann.
Das ist der Moment, in dem technische Entscheidungen zu organisatorischen Verpflichtungen werden. Eine Demo, die nur den sauberen Happy Path zeigt und die Fehlerbehandlung ausspart, schafft kein Vertrauen. Eine Verteidigung, die die Plattform-Wahl nicht gegen konkrete Enterprise-Anforderungen erklären kann, bekommt keine Freigabe. Beides muss präzise, ehrlich und in der tatsächlichen Architektur des Agenten verankert sein.
### Aufgabe 1: Das Demo-Skript schreiben
Schreib ein strukturiertes Gesprächsskript mit fünf Turns, das Meridians Agentflow v2 dem CIO in der Live-Demo vorstellt. Das Skript muss alle fünf folgenden Fähigkeiten der Reihe nach in einer einzigen durchgehenden Session zeigen.
#### Turn 1 - Wissensabfrage
Im ersten Turn muss der Agent Inhalte aus dem Document Store meridian-knowledge abrufen. Die Anfrage muss so konkret sein, dass der Agent sie nicht allein aus den Trainingsdaten von Gemini beantworten kann. Er muss aus den eingelesenen Dokumenten abrufen.
Formatiere Turn 1 so:
- User: die Anfrage des Consultants
- Agent Thought: die interne Überlegung des Agenten, welcher Pfad der richtige ist und warum die Wissensdatenbank die richtige Quelle ist
- Agent Output: die Antwort an den Nutzer, mit einem kurzen Hinweis darauf, welcher Dokumentabschnitt abgerufen wurde
#### Turn 2 - Kontext-Erhalt über mehrere Turns
Im zweiten Turn muss der Agent zeigen, dass er den Kontext aus Turn 1 behält, ohne den Document Store erneut abzufragen. Die Anfrage muss auf Informationen aus Turn 1 aufbauen, und zwar so, dass sie nur mit Session-Memory korrekt beantwortet werden kann.
Formatiere Turn 2 so:
- User: die Folgeanfrage des Consultants
- Agent Thought: die Überlegung des Agenten, die bestätigt, dass der Kontext aus Turn 1 verfügbar ist, ohne eine neue Abfrage
- Agent Output: die Antwort an den Nutzer, die den Kontext aus Turn 1 auf die neue Frage anwendet
#### Turn 3 - Live-Datenabfrage mit Human-Input-Freigabe
Im dritten Turn muss der Agent den HTTP Node für eine Live-Abfrage des Engagement-Status aufrufen. Die Anfrage muss eine konkrete Account-Referenz enthalten. Der Agent muss am Human Input Node pausieren und die abgerufenen Daten zur Freigabe vorlegen, bevor er sie formatiert und zurückgibt.
Formatiere Turn 3 so:
- User: die Status-Anfrage des Consultants
- Agent Thought: die Überlegung des Agenten, die erkennt, dass es sich um eine Live-Datenanfrage und nicht um eine Wissensabfrage handelt
- Human Input Node Pause: die Nachricht, die dem Consultant mit den Rohdaten und der Proceed/Reject-Abfrage angezeigt wird
- Agent Output (nach Proceed): die formatierte Engagement-Zusammenfassung, die an den Consultant zurückgegeben wird
#### Turn 4 - Sauberes Abfangen von Fehlern
Im vierten Turn muss der Agent zeigen, wie er sich verhält, wenn der HTTP Node einen Fehler zurückgibt. Bevor du diesen Turn schreibst, ändere die URL des HTTP-Node vorübergehend auf einen ungültigen Endpunkt, um den Fehler zu simulieren, und stell sie danach wieder her.
Formatiere Turn 4 so:
- User: eine Status-Anfrage für einen anderen Account
- Agent Thought: die Überlegung des Agenten, die den HTTP-Fehler erkennt und die Fallback-Anweisung anwendet
- Agent Output: die Fallback-Antwort, die anerkennt, dass die Information gerade nicht verfügbar ist, und einen konkreten nächsten Schritt anbietet, ganz ohne erfundene Engagement-Details
> ⚠️ Stell nach dem Schreiben und Testen dieses Turns die URL des HTTP-Node wieder auf https://jsonplaceholder.typicode.com/todos/1 und speichere das Canvas, bevor du weitermachst.
#### Turn 5 - Scope-Grenze
Im fünften Turn muss der Agent zeigen, wie er sich am Rand seines autorisierten Scopes verhält. Schick eine Anfrage, die ein Consultant durchaus stellen könnte, die aber außerhalb der definierten Fähigkeiten des Agenten liegt.
Formatiere Turn 5 so:
- User: die Anfrage außerhalb des Scopes
- Agent Thought: die Überlegung des Agenten, die erkennt, dass die Anfrage außerhalb seines autorisierten Scopes liegt
- Agent Output: die Fallback-Formulierung mit einem konstruktiven nächsten Schritt, ganz ohne erfundene Antwort und ohne den Versuch, außerhalb der definierten Grenzen zu antworten
### Aufgabe 2: Die Plattform-Verteidigung schreiben
Nach der Demo äußert der CIO folgendes Bedenken:
> "This looks capable. But I need to understand the governance picture before I approve production deployment. We handle confidential client operational data across three EU jurisdictions. I need to know: can this run in a properly governed environment? And a colleague has suggested we rebuild this in Microsoft Copilot Studio because of its enterprise governance features. What is your recommendation?"
Schreib eine formale Plattform-Verteidigung, die direkt auf das Bedenken des CIOs eingeht. Die Verteidigung muss die folgenden drei Argumente in dieser Reihenfolge abdecken.
Argument 1 - Warum selbst gehostetes Flowise der richtige Weg in die Produktion ist
Erklär, was der aktuelle selbst gehostete Docker-Prototyp schon leistet und was für Produktion noch fehlt. Beziehe dich auf die vier Infrastruktur-Dimensionen: Hosting, Observability, Sicherheit im Produktionsmaßstab und Governance. Erklär, warum die Migration vom aktuellen Docker-Prototyp zu einem produktionsreifen Flowise-Deployment ein klar definierter Weg ist und kein Neubau. Canvas-Logik, System-Prompt, Document-Store-Konfiguration und Routing-Architektur bleiben dabei erhalten. Nur die Infrastrukturebene ändert sich.
Argument 2 - Warum das aktuelle Gemini-API-Setup ein Produktions-Upgrade braucht
Der aktuelle Build nutzt den kostenlosen Gemini-API-Tarif über Google-AI-Studio-Credentials. Erklär, welche Konsequenzen das für die Datenverarbeitung bei einer Beratung hat, die vertrauliche operative Kundendaten verarbeitet. Geh auf das konkrete Problem ein: Im kostenlosen Tarif kann Google die an die API gesendeten Daten zur Verbesserung seiner Modelle nutzen. Erklär, wie der Upgrade-Pfad aussieht, also der Wechsel zu einem bezahlten Gemini-API-Tarif oder zur Gemini Enterprise Agent Platform, und was das in Sachen Datenschutz, SLAs und DSGVO-Konformität bringt.
Argument 3 - Warum Microsoft Copilot Studio für Meridian die falsche Wahl ist
Geh direkt auf den Vorschlag des Kollegen ein. Dein Argument muss konkret diese drei Punkte abdecken:
- Die Governance-Vorteile von Copilot Studio setzen ein bestehendes Microsoft-365-Ökosystem voraus, Azure AD, SharePoint, Teams, das Meridian nicht nutzt. Für eine Organisation ohne diese Infrastruktur bringen die geerbten Governance-Kontrollen keinen Mehrwert.
- Das Connector-Ökosystem von Copilot Studio ist auf Microsoft-Tools optimiert. Die Integration mit Meridians individuellen internen APIs und dem bereits validierten Gemini-Modell würde eigene Connector-Entwicklung erfordern, was den Low-Code-Governance-Vorteil zunichtemacht.
- Ein Neubau in Copilot Studio würde bedeuten, drei Sprints validierter Canvas-Logik aufzugeben, etwa die Document-Store-Konfiguration, das Routing über den Condition Agent Node, die Retry-Logik und den Human-Input-Freigabe-Checkpoint, und alles kurz vor dem Deployment auf einer unbekannten Plattform neu aufzubauen. Das Risiko dieser Entscheidung steht in keinem Verhältnis zum Governance-Nutzen, der ohne ein Microsoft-Ökosystem ohnehin nicht eintritt.
> 💡 Fazit: Das Demo-Skript zeigt, dass der Agent unter realistischen Bedingungen funktioniert, Fehlerfälle eingeschlossen. Die Plattform-Verteidigung zeigt, dass die architektonischen Entscheidungen dahinter bewusst getroffen, belegt und gegen Enterprise-Anforderungen verteidigbar sind. Zusammen stehen sie für die zwei Fähigkeiten, die zählen, wenn ein KI-Agent vom Projekt zum Produkt wird: zeigen zu können, dass er funktioniert, und erklären zu können, warum er so gebaut wurde, wie er gebaut wurde.
#### Willkommen auf der Zielgeraden von Kurs 2B! Das ist deine letzte Campus-Lektion! In den kommenden Live-Sessions (Presentation Day & Code Clinic) bekommt dein Agent den finalen Feinschliff, bevor du ihn vor echtem Stakeholder-Publikum ins Rennen schickst. Alles, woran du vier Sprints lang getüftelt hast, von der kleinen Drei-Node-Baseline in Sprint 1 bis zum voll orchestrierten, RAG-gestützten Power-Agenten, zahlt genau auf diesen einen Augenblick ein.
