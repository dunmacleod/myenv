# Approval Checkpoints mit dem Human Input Node bauen

Notion page: https://app.notion.com/p/Approval-Checkpoints-mit-dem-Human-Input-Node-bauen-3819418319f38088840af209a617615d
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du fügst dem Meridian-Agentflow-v2 einen Human Input Node hinzu und schaffst damit einen Freigabe-Checkpoint, bevor der Agent eine sensible Antwort zurückgibt.
## Ausgangslage
Meridians Senior Partner Klaus Brandt hat ein Governance-Bedenken geäußert. Fragt ein Consultant Engagement-Status-Daten ab, ruft der Agent sie ab und gibt sie sofort zurück. Es gab bisher weder eine Prüfung noch eine Bestätigung. Bei Routineanfragen ist das kein Problem. Geht es aber um sensible, für eine Eskalation markierte Kundenkonten, soll der Agent innehalten und vor dem Fortfahren um Bestätigung bitten.
Der Human Input Node stoppt den automatisierten Ablauf des Workflows und zeigt einem menschlichen Nutzer über das Chat-Interface eine Information oder eine Frage an. Sobald der Nutzer eine Auswahl trifft und seine Antwort abschickt, läuft der Workflow entlang des Output-Pfads weiter, der zu seiner gewählten Aktion gehört.
Das ist das Human-in-the-Loop-Muster. Der Agent hält an einem definierten Checkpoint an und zeigt, was er als Nächstes vorhat. Dann wartet er auf eine explizite Freigabe, bevor er weitermacht.
## Was du baust
Ein aktualisierter Path B, der zwischen Condition A und Agent Node B einen Human Input Node einfügt. Liefert der HTTP Node erfolgreich Daten, zeigt der Agent dem Consultant den rohen Engagement-Record und bittet um Bestätigung, bevor er die finale Antwort formatiert und zurückgibt.
### Schritt 1: Die Meridian-Base-Agent-Canvas öffnen
Öffne Flowise unter http://localhost:3000 und öffne deine Meridian Base Agent-Canvas.
### Schritt 2: Condition A Outputs 0 und 1 trennen und neu verbinden
- Lösche die Verbindung zwischen Condition A output 0 und dem Agent 2Node. Verbinde Output 0 stattdessen mit dem Custom Function Node.
- Lösche die Verbindung zwischen Condition A output 1 und dem Custom FunctionNode.
> ➡️ Warum machen wir das? Der Human Input Node ist ein Review Checkpoint. Er bietet nur dann Mehrwert, wenn es etwas zu prüfen gibt. Wenn du dich an die vorherigen Lektionen erinnerst: Bei einem fehlgeschlagenen HTTP Call zu pausieren und zu fragen „möchtest du fortfahren?“, wenn keine Daten vorhanden sind, mit denen fortgefahren werden kann, würde den Consultant verwirren und keinen Zweck erfüllen. Wenn die Condition also fehlgeschlagen ist, wird kein Mensch benötigt. Wenn sie aber erfolgreich ist, dann brauchst du Review.

### Schritt 3: Einen Human Input Node hinzufügen
Klicke auf (+) und füge der Canvas einen Human Input Node hinzu. Platziere ihn zwischen Condition A und dem Agent-2-Node. Verbinde Condition A output 1 mit dem Input des Human Input Node.
### Schritt 4: Den Human Input Node konfigurieren
Klicke auf den Human Input Node, um seine Einstellungen zu öffnen.
- Description Type: Wähle Fixed
- Description: The following engagement data has been retrieved. Do you want to proceed with generating the summary? {{ httpAgentflow_0.data }}
- Feedback: Auf On stellen
> ➡️ Warum Feedback aktivieren: Ist Feedback aktiviert, bekommt der Nutzer ein Feedback-Fenster angezeigt, in dem er eine Rückmeldung hinterlassen kann. Diese wird dann an den Output des Node angehängt. Dadurch kann der Consultant eine Notiz hinzufügen. Zum Beispiel kann er darauf hinweisen, dass die Daten falsch aussehen, bevor der Agent die Antwort formatiert.
Der Human Input Node stellt zwei Output Anchor bereit, die den unterschiedlichen Nutzeraktionen entsprechen (Proceed und Reject).
### Schritt 5: Die Outputs des Human Input Node verbinden
- Proceed Output: Mit Agent Node B verbinden
- Reject Output: Einen neuen Direct Reply Node hinzufügen mit der Nachricht: Understood. The engagement summary has not been generated. Please contact your engagement manager directly if you need further information about this account.
### Schritt 6: Flow State des Start Node aktualisieren
Klicke auf den Start Node und lege dort schon jetzt einen neuen Key an, der erst in einer späteren Lektion gebraucht wird. Kein Node in dieser Lektion schreibt darauf oder liest davon. Er ist als Platzhalter reserviert, damit der Flow State konsistent mit den Keys bleibt, die später im Sprint dazukommen.
[TABLE]
  | Key | Initialwert |
  | approval_status | `` |
Speichere den Start Node.
![image]((notion-hosted file))

### Schritt 7: Speichern und testen
Speichere den Canvas. Öffne die Chat-Oberfläche und sende: Can you check the engagement status for account 1?
Erwarteter Ablauf:
1. Condition Agent Node routet zum HTTP-Pfad
1. HTTP Node ruft die Daten ab
1. Condition A bestätigt, dass Daten vorhanden sind
1. Human Input Node pausiert und zeigt die rohen Engagement-Daten mit Proceed- und Reject-Buttons an
1. Klick auf Proceed. Agent Node B formatiert die Antwort und Direct Reply B gibt sie zurück.
1. Öffne eine neue Session, stelle dieselbe Anfrage und klicke auf Reject. Direct Reply gibt die Ablehnungsnachricht zurück.
### Checkliste: Vor dem Weitermachen bestätigen
- [ ] Human Input Node zwischen Condition A output 1 und Agent Node B eingefügt
- [ ] Description Type auf Fixed gesetzt, mit Bestätigungsnachricht und HTTP-Datenvariable
- [ ] Feedback aktiviert
- [ ] Proceed Output mit Agent Node B verbunden
- [ ] Reject Output mit einem neuen Direct Reply Node mit Ablehnungsnachricht verbunden
- [ ] Key approval_status zum Flow State des Start Node hinzugefügt
- [ ] Proceed-Pfad gibt formatierte Engagement-Zusammenfassung zurück
- [ ] Reject-Pfad gibt Ablehnungsnachricht zurück

> 💡 Fazit:
  Der Human Input Node macht aus einem vollautomatischen Pfad einen überwachten. Der Agent übernimmt die Recherche. Die finale Entscheidung, ob es weitergeht, trifft der Consultant. Dieses Muster ist unverzichtbar für jede Aktion, die sich schwer rückgängig machen lässt oder Daten betrifft, die vor der Ausgabe eine menschliche Prüfung brauchen. Der Checkpoint kostet eine zusätzliche Interaktion, verhindert dafür aber eine ganze Kategorie automatisierter Fehler.
