# Was A2A ist und wann es relevant wird

Notion page: https://app.notion.com/p/Was-A2A-ist-und-wann-es-relevant-wird-efd9418319f383f58223015d972a787a
Backed up before n8n migration

Sofias Order-Lookup-Agent greift jetzt über MCP auf Cascadias Tools zu. Aber wenn's um einen Garantieanspruch geht, reicht ein einfacher Tool-Aufruf nicht. Hier braucht's Urteilsvermögen von einem komplett eigenständigen Agenten, den Cascadias Compliance-Team betreut, der auf einer anderen Plattform läuft und eine eigene Entscheidungslogik hat. Das ist ein anderer Agent.
Wenn Agenten direkt mit anderen Agenten sprechen müssen, reicht MCP allein nicht. Dafür gibt's Agent-to-Agent (A2A). Diese Lektion stellt dir A2A vor, grenzt es von MCP ab und zeigt, wann ein System es wirklich braucht.
## Was ist A2A?
Agent-to-Agent (A2A) ist ein Standard, der sich gerade etabliert. Er ermöglicht es unabhängig deployten AI-Agenten, miteinander zu kommunizieren, sich zu koordinieren und Aufgaben aneinander zu delegieren.
Statt ein Tool oder eine API direkt aufzurufen, schickt ein Agent seine Anfrage an einen anderen Agenten, der eigene Fähigkeiten, ein eigenes Memory, eigene Ziele und einen eigenen Entscheidungsprozess mitbringt.
Kurz gesagt: A2A ist ein Protokoll für die Zusammenarbeit zwischen Agenten.
Zum Beispiel:
- Ein Kundenservice-Agent bekommt eine Anfrage zu einer verspäteten Sendung.
- Der Support-Agent kontaktiert einen Logistik-Agenten.
- Der Logistik-Agent ruft Sendungsinformationen ab und schickt eine Antwort zurück.
- Der Support-Agent kombiniert diese Informationen und antwortet dem Kunden.
Jeder Agent bleibt für seinen eigenen Bereich zuständig, aber gemeinsam lösen sie größere Aufgaben.
![image]((notion-hosted file))
## MCP vs. A2A
Viele verwechseln MCP und A2A, weil bei beiden die Kommunikation über einen einzelnen Agenten hinausgeht.
Trotzdem lösen sie unterschiedliche Probleme.
MCP
- Verbindet einen Agenten mit Tools, Daten oder Services
- Geht's um Zugriff auf Tools
- Auf der anderen Seite steht meistens ein Tool
- Nützlich für Datenbanken, APIs, Dateien und Anwendungen
- Ein Agent behält die Kontrolle
A2A
- Verbindet einen Agenten mit einem anderen Agenten
- Geht's um Zusammenarbeit
- Auf der anderen Seite steht ein weiteres reasoning-fähiges System
- Nützlich für Teams spezialisierter Agenten
- Kontrolle kann zwischen mehreren Agenten wechseln
> 💡 Eine Organisation kann beides gleichzeitig nutzen. Ein Agent kann MCP verwenden, um auf Tools zuzugreifen, und A2A, um mit anderen Agenten zusammenzuarbeiten.
## Wann reicht MCP aus?
Viele Agentensysteme brauchen A2A überhaupt nicht.
Wenn ein einzelner Agent über MCP auf alle nötigen Tools zugreifen kann, macht es das System oft nur komplizierter, wenn du weitere Agenten hinzufügst.
Ein interner HR-Assistent zum Beispiel könnte MCP nutzen, um auf Folgendes zuzugreifen:
- Mitarbeiterdaten
- Unternehmensrichtlinien
- Kalendersysteme
- Dokumenten-Repositories
In diesem Fall reicht ein einzelner Agent für die ganze Aufgabe locker aus.
## Verständnischeck
### Frage 1
>  Sofias Order-Lookup-Agent greift über MCP auf Cascadias Bestelldatenbank, Versand-API und Rückgabesystem zu. Braucht diese Konfiguration A2A?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/2040e9e9-5212-4b7d-98db-2740a2a9476a
## Wann wird A2A wertvoll?
A2A wird nützlich, wenn mehrere unabhängige Agenten zusammenarbeiten müssen. Das kommt vor allem in größeren Organisationen vor, wo verschiedene Teams ihre eigenen Agenten bauen und betreuen, Agenten in getrennten Umgebungen laufen oder jeder Agent auf einen anderen Geschäftsbereich spezialisiert ist. In solchen Fällen muss ein Agent vielleicht einen Teil einer Aufgabe an einen anderen Agenten delegieren, der Expertise, Berechtigungen oder Fähigkeiten hat, die er selbst nicht hat.
> Nimm ein Reiseunternehmen als Beispiel. Ein kundenorientierter Agent bekommt eine Anfrage von einem Reisenden, der eine bestehende Buchung ändern möchte. Statt jeden Aspekt der Anfrage selbst zu bearbeiten, kontaktiert er einen Buchungs-Agenten, der Reservierungen verwaltet, einen Payment-Agent, der Rückerstattungen oder zusätzliche Gebühren prüft, und einen Support-Agenten, der die Kundenkommunikation übernimmt. Jeder Agent kümmert sich um seinen eigenen Bereich und gibt die relevanten Informationen zurück. Der kundenorientierte Agent kombiniert die Ergebnisse anschließend und gibt dem Reisenden eine vollständige Antwort.
![image]((notion-hosted file))
Statt einen großen Agenten zu bauen, der für jede mögliche Aufgabe verantwortlich ist, ermöglicht A2A mehreren spezialisierten Agenten die Zusammenarbeit, während sie unabhängig bleiben. Dadurch werden Systeme leichter wartbar, skalierbar und erweiterbar, wenn neue Fähigkeiten hinzugefügt werden.

> 💡 Heute verwenden viele Multi-Agent-Systeme Custom Integrations für die Kommunikation. Jede Organisation baut oft ihre eigenen Nachrichtenformate, Workflows und Handoff-Mechanismen.
## Zusammenfassung
MCP und A2A lösen unterschiedliche Probleme. MCP standardisiert die Verbindung zwischen einem Agenten und einem Tool. A2A standardisiert die Verbindung zwischen zwei unabhängigen Agenten, die eigenständig reasonen und handeln müssen.
Eine nützliche Faustregel:
- Wenn ein Agent ein Tool braucht, ist MCP normalerweise die richtige Lösung.
- Wenn ein Agent die Expertise oder Fähigkeiten eines anderen Agenten braucht, wird A2A relevant.
In der nächsten Lektion baust du das Architektur-Briefing für das Sprint-1-Projekt und entscheidest, welches der beiden Protokolle dein Integrationsproblem wirklich braucht.
