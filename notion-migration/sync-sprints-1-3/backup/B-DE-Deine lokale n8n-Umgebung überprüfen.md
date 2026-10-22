# Deine lokale n8n-Umgebung überprüfen

Notion page: https://app.notion.com/p/Deine-lokale-n8n-Umgebung-berpr-fen-3789418319f38080a767f0b162a255e8
Backed up before n8n migration

> 💡 In dieser Lektion überprüfst du: ob deine lokale n8n-Installation stabil funktioniert, bevor du mit KI-Workflows beginnst.
## Warum vor dem Bauen überprüfen?
Ein Konfigurationsproblem, das mitten in einer Agenten-Übung auftaucht, wird leicht fälschlich als Prompt- oder Modellproblem interpretiert. Deshalb prüfen wir zuerst die Infrastruktur.
## Aufgabe A: Container überprüfen
Führe docker ps aus. Du solltest einen Container mit dem Namen n8n und Port 5678 sehen.
Falls er gestoppt ist, führe docker start n8n aus. Für zusätzliche Details nutze docker logs n8n.
> 📸 SCREENSHOT-VORSCHLAG: docker ps mit laufendem n8n-Container und Port-Mapping.
## Aufgabe B: n8n-Oberfläche überprüfen
Öffne http://localhost:5678.
Prüfe, dass:
- die Seite ohne Fehler lädt;
- du die Workflow-Liste oder Overview öffnen kannst;
- du einen neuen Workflow erstellen kannst;
- sich der Node Picker öffnet, wenn du einen Schritt hinzufügst.
Gehe erst weiter, wenn diese Grundlagen funktionieren.
## Aufgabe C: Einen Workflow ohne KI ausführen
1. Erstelle einen neuen Workflow.
1. Füge einen Manual Trigger hinzu.
1. Füge eine Edit Fields (Set) Node hinzu.
1. Erstelle ein Textfeld status mit dem Wert n8n is working.
1. Verbinde die Nodes.
1. Wähle Execute Workflow.
Öffne den Output der Edit Fields Node und prüfe, dass der status-Wert vorhanden ist.
> 📸 SCREENSHOT-VORSCHLAG: Workflow-Canvas mit Manual Trigger → Edit Fields, beide Nodes erfolgreich ausgeführt.
> 📸 SCREENSHOT-VORSCHLAG: Output-Bereich der Edit Fields Node mit status: n8n is working.
## Aufgabe D: Persistenz prüfen
Speichere den Workflow als Environment Check.
Stoppe danach n8n, starte n8n erneut, aktualisiere localhost:5678 und prüfe, dass der gespeicherte Workflow weiterhin vorhanden ist. Damit bestätigst du, dass das Volume n8n_data funktioniert.
## Aufgabe E: Credentials prüfen
Wenn du das OpenRouter-Credential bereits erstellt hast, prüfe, ob es in der Credential-Auswahl erscheint, sobald du eine OpenRouter Chat Model Node hinzufügst.
Zeige den Key nicht an und führe noch keinen Modelltest durch. In der nächsten Lektion wird das Modell innerhalb eines echten KI-Workflows getestet.
## Checkliste vor dem Start
- [ ] Docker Desktop läuft.
- [ ] docker ps zeigt den Container n8n.
- [ ] localhost:5678 lädt.
- [ ] Ein einfacher Workflow ohne KI wird erfolgreich ausgeführt.
- [ ] Der Test-Workflow bleibt nach einem Container-Neustart erhalten.
- [ ] OpenRouter-Credentials sind vorhanden oder der Kurs-API-Key liegt zum Einrichten bereit.
> 💡 Takeaway: Infrastrukturprüfung und Agenten-Debugging sollten getrennt werden. Wenn Docker, n8n, Persistenz und grundlegende Workflow-Ausführung zuerst funktionieren, lassen sich spätere Fehler deutlich leichter lokalisieren.