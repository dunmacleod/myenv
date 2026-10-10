# Agent-Memory-Node und Thread-IDs in Flowise

Notion page: https://app.notion.com/p/Agent-Memory-Node-und-Thread-IDs-in-Flowise-3779418319f38062a784cdb516e78313
Backed up before n8n migration

> 💡 In dieser Lektion konfigurierst du die Session-ID in deinem Buffer-Memory-Node, um die Chat-Verläufe der einzelnen Nutzer sauber voneinander zu trennen. Anschließend überprüfst du direkt, ob alle Session-Daten korrekt gespeichert und isoliert werden.

## Warum dieser Schritt genau jetzt folgt
Der Buffer-Memory-Node aus der letzten Lektion gibt Contigos Agenten kurzfristigen Gesprächskontext innerhalb einer einzelnen Session. Er hat aber eine Schwachstelle. Ist standardmäßig keine Session ID angegeben, generiert Flowise für jede Interaktion eine zufällige ID. Für Single-User-Tests reicht das. In einem kundenorientierten Deployment mit mehreren gleichzeitigen Nutzern können die Gesprächsverläufe dann aber ineinander überlaufen.
Gerade in einem kundenorientierten Finanzdienstleistungskontext wie bei Contigo ist das ein ernstes Problem. Dieser Walkthrough zeigt dir, wie du den Session-ID-Parameter im Buffer-Memory-Node konfigurierst. Damit isoliert Flowise den Gesprächsverlauf jedes Kunden vollständig von dem der anderen Nutzer.

## Was du baust
Du erweiterst den Chatflow aus der letzten Lektion. Der Buffer-Memory-Node ist schon verbunden und läuft. Du hast bereits bestätigt, dass der Agent Informationen innerhalb einer einzelnen Session abrufen kann. Jetzt machst du dieses Memory fit für eine Multi-User-Umgebung, indem du eine Session ID im Buffer-Memory-Node konfigurierst.

### Schritt 1: Deinen bestehenden Chatflow öffnen
Navigiere in deinem Flowise-Dashboard zu Chatflows und öffne den Chatflow, den du in der vorherigen Lektion gebaut hast. Du solltest deinen bestehenden Canvas mit den bereits verbundenen Conversation-Chain-, ChatGoogleGenerativeAI- und Buffer-Memory-Nodes sehen.
Du musst für diese Lektion keine neuen Nodes hinzufügen. Die Änderungen passieren innerhalb der Konfiguration des Buffer-Memory-Nodes.
![image]((notion-hosted file))

### Schritt 2: Die Einstellungen des Buffer-Memory-Nodes öffnen.
Wähle ‘Additional Parameters’ aus. Du siehst zwei Parameter:
- Session ID
- Memory Key
Das Feld Session ID ist standardmäßig leer (wir haben hier schon client_001 eingetragen). Flowise generiert sonst für jede Interaktion eine zufällige ID. Für Single-User-Tests passt das. Für die Produktion mit mehreren gleichzeitig aktiven Nutzern eher nicht.

### Schritt 3: Die Session ID konfigurieren
Gib im Feld Session ID einen Wert ein, der eine eindeutige Kennung für den aktuellen Nutzer oder die aktuelle Session darstellt. Für Testzwecke behalten wir den festen Wert bei: client_001.
![image]((notion-hosted file))
> ➡️ Warum ist das wichtig : Die Session ID gruppiert den gesamten Gesprächsverlauf unter einer Kennung. Wenn eine Session ID gesetzt ist, speichert und ruft Flowise Memory nur für genau diese ID ab. Jeder Kunde erhält seinen eigenen isolierten Memory-Bereich: Kontodetails, Fallreferenzen und Präferenzen eines Kunden können nicht im Gespräch eines anderen Kunden auftauchen.

### Schritt 4: Speichern und Session-Isolation testen
Speichere deinen Chatflow und öffne die integrierte Chat-Oberfläche. Führe den folgenden Isolationstest mit zwei separaten Browser-Sessions durch, jeweils mit einer anderen Session ID, die im Buffer-Memory-Node konfiguriert ist.
Session 1 Session ID: client_001
Senden: „Meine bevorzugte Kontaktsprache ist Englisch und mein offener Fall ist CG-9921.“
Dann senden: „Wie lautet meine offene Fallreferenz?“
Der Agent sollte mit CG-9921 antworten und damit bestätigen, dass Memory für diese Session korrekt funktioniert.
![image]((notion-hosted file))

Session 2 Session ID: client_002
Öffne eine zweite Browser-Session, aktualisiere die Session ID im Buffer-Memory-Node auf client_002, speichere und sende:
„Welche Sprache bevorzugt dieser Kunde, und hat er offene Fälle?“
Worauf du achten solltest:
- Session 2 sollte keine Kenntnis von den Informationen haben, die in Session 1 angegeben wurden. Falls doch, werden die Session IDs nicht korrekt angewendet und die Sessions teilen sich denselben Memory-Bereich.
- Session 1 sollte ihre eigenen Daten korrekt über Turns hinweg abrufen, was bestätigt, dass Nachrichten unter der richtigen Session ID gespeichert und abgerufen werden.

### Schritt 5: Nachrichtenspeicherung überprüfen
Navigiere in deinem Flowise-Dashboard zum Chatverlauf für deinen Chatflow. Du kannst ihn über das Einstellungssymbol innerhalb des Chatflow-Canvas unter View Messages aufrufen. Du solltest zwei separate Gesprächs-Threads sehen, die jeweils unter ihrer eigenen Session ID gespeichert sind. Jeder Thread enthält nur die Nachrichten aus dieser Session, ohne Überschneidungen zwischen ihnen.
Damit hast du die Bestätigung, dass die Session-Isolation einwandfrei funktioniert. In einem regulierten Umfeld wie dem der Contigo GmbH ist der Nachweis, dass Kundendaten sauber getrennt werden, eine strikte Compliance-Vorgabe – und weit mehr als nur ein technisches Detail.

![image]((notion-hosted file))

## Checkliste: Bitte vor dem nächsten Schritt überprüfen
- [ ] Buffer-Memory-Node geöffnet und Feld Session ID gefunden
- [ ] Session ID mit einem eindeutigen Wert für Tests konfiguriert (z. B. client_001)
- [ ] Chatflow gespeichert, nachdem die Session ID gesetzt wurde
- [ ] Memory-Test abgeschlossen: Agent hat Fallreferenz über Turns hinweg in Session 1 abgerufen
- [ ] Isolationstest abgeschlossen: Session 2 hatte keinen Zugriff auf Daten aus Session 1
- [ ] Chatverlauf im Flowise-Dashboard überprüft, der separate Threads pro Session ID zeigt

> 💡 Takeaway: 
  Die Session ID macht Buffer Memory sicher für eine Multi-User-Umgebung. Ohne sie gibt es keine garantierte Isolation der Gesprächsverläufe zwischen Nutzern. Konfigurier sie korrekt, bevor mehr Komplexität dazukommt. Dann bleibt der Rest deines Chatflow-Builds zuverlässig.

