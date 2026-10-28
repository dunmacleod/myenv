# Die Projekt-Agenten verbinden

Notion page: https://app.notion.com/p/Die-Projekt-Agenten-verbinden-7ab9418319f3831aa6b88198cb240040
Backed up before n8n migration

Im Verlauf des Kurses hast du die einzelnen Bausteine des arXiv Research Assistant untersucht. 
- Kommunikationsprotokolle in Sprint 1
- Orchestrierungsmuster in Sprint 2
- Resilienz-Patterns in Sprint 3
- Im Sprint-4-Lektionen hast du den Baseline-Agenten um einen Research Summary Agent erweitert, den erweiterten Workflow evaluiert und Fehler über Protokoll- und Orchestrierungsebenen hinweg debuggt.
Jetzt führst du diese Teile zum vollständigen Projekt zusammen.
In dieser Lektion baust du den vollständigen arXiv Research Assistant. Du setzt die Agenten und Integrationen zu einem orchestrierten Workflow zusammen.
Am Ende der Lektion sollte dein Projekt Folgendes können: eine User-Anfrage empfangen, sie an den passenden Spezialisten routen, bei Bedarf externe Tools nutzen, sich von temporären Fehlern erholen und eine Antwort an den User zurückgeben.
## Deine Aufgabe
Erstelle den vollständigen Workflow für deinen arXiv Research Assistant.
Der finale Workflow sollte Folgendes enthalten:
- einen Intake Agent
- einen oder mehrere Specialist Agents
- eine Orchestrierungsebene
- die für dein Projekt erforderlichen MCP-fähigen Tools
- Agent-to-Agent-Delegation
- Retry- und Fallback-Logik, wo es Sinn ergibt
Die genaue Implementierung kann je nach deinem Projektdesign unterschiedlich sein, aber der Workflow sollte zeigen, dass all diese Fähigkeiten zusammen funktionieren.
## Schritt 1: Die Projektstruktur erstellen
Starte einen neuen AgentFlow für dein Projekt.
Erstelle den High-Level-Workflow, der die vollständige Customer Journey abbildet, beginnend mit der User-Anfrage und endend mit der finalen Antwort.
Konzentriere dich in dieser Phase auf die Gesamtarchitektur statt auf die detaillierte Konfiguration jedes einzelnen Node.
## Schritt 2: Den Intake Agent hinzufügen
Füge den Intake Agent zu deinem Workflow hinzu.
Dieser Agent sollte die Anfrage des Users empfangen, bestimmen, welche Art von Problem gemeldet wird, und die Anfrage für die Delegation vorbereiten.
Der Intake Agent sollte sich darauf konzentrieren, die Anfrage zu verstehen, statt sie zu lösen.
## Schritt 3: Die Specialist Agents hinzufügen
Erstelle die Specialist Agents, die dein Projekt benötigt.
Zum Beispiel könnte dein Workflow Agenten enthalten, die für Folgendes verantwortlich sind:
- Billing
- Technical Support
- Account Management
- Security
Jeder Spezialist sollte eine klar definierte Verantwortung haben.
Vermeide nach Möglichkeit, mehreren Agenten überlappende Rollen zu geben.
## Schritt 4: Die Orchestrierung konfigurieren
Verbinde die Agenten mit dem Orchestrierungsmuster, das du während des Projektdesigns ausgewählt hast.
Überprüfe, ob Anfragen an den richtigen Spezialisten geroutet werden und ob jeder Agent nur die Aufgabe ausführt, die ihm zugewiesen wurde.
Wenn dein Workflow mehrere spezialisierte Agenten umfasst, muss die Orchestrierung in der Lage sein, Aufgaben effizient zu delegieren.
## Schritt 5: Die MCP-fähigen Tools verbinden
Verbinde das MCP-fähige Tool oder die MCP-fähigen Tools, die dein Projekt benötigt.
Abhängig von deinem gewählten Design bieten diese Werkzeuge Schnittstellen zu externen Daten, Dokumentationen, Repositories, APIs oder weiteren Diensten.
Überprüfe, ob der passende Spezialagent bei Bedarf auf das erforderliche Tool zugreifen kann.
## Schritt 6: Agent-to-Agent-Delegation konfigurieren
Konfiguriere den Workflow so, dass Agenten Arbeit aneinander delegieren können.
Der empfangende Agent sollte über ausreichend Kontext verfügen, um seine Aufgabe abzuschließen, ohne den Nutzer zur Wiederholung bereits erfasster Informationen aufzufordern.
Jeder Agent sollte seine spezialisierte Aufgabe abschließen, bevor er das Ergebnis an den Workflow zurückgibt.
## Schritt 7: Resilienz hinzufügen
Überprüfe den Workflow und identifiziere die Schritte, bei denen Fehler am wahrscheinlichsten auftreten.
Füge dort, wo es passt, Folgendes hinzu:
- Retry-Logik für temporäre Fehler
- Fallback-Pfade, wenn Retries ausgeschöpft sind
- userfreundliche Antworten, wenn Recovery nicht möglich ist
Nicht jeder Node benötigt Resilienz. Konzentriere dich auf die Teile des Workflows, bei denen Fehler die größte Auswirkung hätten.
## Schritt 8: Den vollständigen Workflow testen
Führe dein Projekt mit mehreren unterschiedlichen Supportanfragen aus.
Prüfe für jede Anfrage, ob:
- der Intake Agent die Anfrage korrekt versteht
- die Anfrage an den richtigen Spezialisten delegiert wird
- MCP-fähige Tools eingesetzt werden, wenn es passend ist
- Agent-to-Agent-Delegation wie erwartet funktioniert
- Retry- und Fallback-Verhalten korrekt funktionieren
- der User eine vollständige Antwort erhält
Teste sowohl erfolgreiche Anfragen als auch mindestens ein Szenario, das deine Resilienzlogik auslöst.
## Häufige Probleme
Beim Testen des Workflows können einige häufige Integrationsprobleme auftreten:
- Anfragen werden an den falschen Spezialisten geroutet.
- Mehrere Agenten führen dieselbe Aufgabe aus.
- MCP-Tools sind verbunden, werden aber nie genutzt.
- Kontext geht während des Agenten-Handoff verloren.
- Retry Loops enden nie.
- Fallback-Pfade umgehen wichtige Workflow-Schritte.
Wenn du auf eines dieser Probleme stößt, verfolge den Ausführungspfad durch deinen Workflow, bevor du Änderungen vornimmst.
## Zusammenfassung
Du hast den vollständigen arXiv Research Assistant zusammengesetzt. Spezialisierte Agenten, Orchestrierung, MCP-fähige Tools, Agent-to-Agent-Delegation und Resilienzmechanismen laufen jetzt in einem einzigen Workflow zusammen. Statt einzelne Komponenten isoliert zu entwickeln, hast du dich darauf konzentriert, das gesamte System als koordinierte Lösung arbeiten zu lassen. Das ist ein wichtiger Meilenstein beim Aufbau produktionsreifer AI-Agentensysteme.
