# Nachrichtenweitergabe und Handoff-Verträge

Notion page: https://app.notion.com/p/Nachrichtenweitergabe-und-Handoff-Vertr-ge-ffb9418319f3837e89de01d87df3bbcb
Backed up before n8n migration

## Eine Abrechnungsübergabe in n8n bauen
Dies ist die erste ausführbare Übergabeübung für Cascadia. Beginnen Sie mit dem Unternehmens- und Entwurfsbeispiel in Warum Agenten strukturierte Kommunikation brauchen. Hier bauen Sie einen neuen Workflow, der Fragen zu Bestellzahlungen von Intake an Billing Specialist weitergibt. Der vorherige Garantievertrag erklärt das Prinzip; diese Übung nutzt einen kleineren Vertrag mit drei Feldern, damit Sie das Routing ohne Bestelldatenbank oder Garantierichtlinie testen können.
Verwenden Sie für beide Rollen Basic LLM Chain. Die Schritte klassifizieren oder schreiben Text und benötigen keine autonome Tool-Auswahl. Es sind zwei Denkrollen in einem festen Workflow. Die spätere MCP-Lektion nutzt AI Agent, weil dort ein Tool ausgewählt und aufgerufen werden muss.
## 1. Workflow und Modellverbindungen erstellen
Erstellen Sie einen neuen Workflow mit Chat Trigger. Wählen Sie als Antwortmodus When Last Node Finishes. Fügen Sie eine Basic LLM Chain namens Intake hinzu und verbinden Sie den Trigger damit. Schließen Sie OpenRouter Chat Model mit den Schulzugangsdaten und einem zugelassenen Modell an.
Wählen Sie für den Intake-Prompt Connected Chat Trigger Node (in manchen Versionen Take from previous node automatically). Wenn Chat Trigger direkt mit Intake verbunden ist, liest der Node chatInput automatisch. Ergänzen Sie unter Chat Messages eine Systemnachricht:
```plain text
Sie klassifizieren Supportanfragen für Cascadia.
Geben Sie nur die strukturierten Felder des Ausgabeschemas zurück.
customer_intent muss billing, other oder needs_clarification sein.
Nutzen Sie billing für Bestellabbuchungen, Rechnungen, doppelte Zahlungen
oder Rückfragen zu Erstattungen.
Nutzen Sie other für eindeutig andere Anliegen.
Nutzen Sie needs_clarification bei unzureichenden Informationen.
issue_summary fasst die Kundenaussage kurz und sachlich zusammen.
handoff_reason erklärt den gewählten Pfad. Erfinden Sie keine
Kontodaten, IDs, Erstattungsfreigaben, erledigten Aktionen oder Richtlinien.
```
Aktivieren Sie Require Specific Output Format, verbinden Sie Structured Output Parser und wählen Sie Define using JSON Schema:
```json
{
  "type": "object",
  "properties": {
    "customer_intent": {
      "type": "string",
      "enum": [
        "billing",
        "other",
        "needs_clarification"
      ]
    },
    "issue_summary": {
      "type": "string"
    },
    "handoff_reason": {
      "type": "string"
    }
  },
  "required": [
    "customer_intent",
    "issue_summary",
    "handoff_reason"
  ],
  "additionalProperties": false
}
```
„Generate from JSON Example“ leitet Feldtypen ab, erzwingt aber nicht die zulässigen Enum-Werte.
![image]((notion-hosted file))
## 2. Übergabe zuordnen und validieren
### Vor der Zuordnung ein Beispiel laden
Die Chat-Eingabe beginnt als chatInput; die drei Vertragsfelder entstehen erst nach der Ausführung von Intake. Ist das Eingabefenster in Map Handoff leer, liegen dort noch keine anzeigbaren Ausführungsdaten vor.
1. Lassen Sie für diesen ersten Test Chat Trigger → Intake mit Modell und Parser verbunden. Öffnen Sie den Workflow-Chat und senden Sie: „Meine Jackenbestellung wurde zweimal abgebucht.“
1. Warten Sie, bis Intake fertig ist. Öffnen Sie Intake und wählen Sie OUTPUT → JSON. Prüfen Sie das geparste Ergebnis, statt sich auf die Chat-Antwort zu verlassen.
1. Klicken Sie im Ausgabefenster von Intake auf Pin data, um das Ergebnis während der Konfiguration des nächsten Nodes zu behalten. Pinnen Sie den Hauptnode Intake, nicht den Structured-Output-Parser-Subnode.
1. Verbinden Sie nach Intake Edit Fields (Set) namens Map Handoff und öffnen Sie ihn erneut. Das gepinnte Intake-Ergebnis liefert stabile Eingabedaten für die Zuordnung.
Der Vertragsinhalt sollte diesem fiktiven Beispiel ähneln. Der genaue Wortlaut der beiden Zusammenfassungen kann abweichen:
```json
[
  {
    "customer_intent": "billing",
    "issue_summary": "Der Kunde berichtet, dass die Jackenbestellung zweimal abgebucht wurde.",
    "handoff_reason": "Das gemeldete Problem betrifft eine doppelte Bestellzahlung."
  }
]
```
![image]((notion-hosted file))
![image]((notion-hosted file))
Das Beispiel zeigt die drei Felder auf oberster Ebene eines Items. Ihre Intake-Ausgabe kann das Objekt unter text oder output enthalten; verwenden Sie die passende Spalte unten.
### Die Zuordnung ausdrücklich eingeben
Wählen Sie in Map Handoff den Modus Manual Mapping. Fügen Sie die folgenden drei Felder mit Typ String hinzu. Lassen Sie den jeweiligen Feldnamen fest und stellen Sie den Wert auf Expression. Sie können den Ausdruck direkt einfügen; sichtbare Daten müssen nicht per Drag-and-drop zugeordnet werden.
[TABLE]
  | Feldname | Felder auf oberster Ebene | Objekt unter text | Objekt unter output |
  | customer_intent | {{ $json.customer_intent }} | {{ $json.text.customer_intent }} | {{ $json.output.customer_intent }} |
  | issue_summary | {{ $json.issue_summary }} | {{ $json.text.issue_summary }} | {{ $json.output.issue_summary }} |
  | handoff_reason | {{ $json.handoff_reason }} | {{ $json.text.handoff_reason }} | {{ $json.output.handoff_reason }} |
Verwenden Sie eine Spalte, die zum Intake-JSON passt. Tragen Sie Beispielwerte wie billing nicht als feste Zuordnungswerte ein: Die Ausdrücke müssen jedes neue Ergebnis lesen. Ist text eine JSON-Zeichenfolge in Anführungszeichen statt eines Objekts, beheben Sie zunächst das Parser-/Ausgabeformatproblem, bevor Sie einen Objektpfad verwenden.
Behalten Sie nur die drei zugeordneten Felder: Deaktivieren Sie Include Other Input Fields oder aktivieren Sie Keep Only Set Fields, wenn Ihre Version diese Bezeichnung verwendet. Führen Sie Map Handoff aus und prüfen Sie, dass die Ausgabe genau die drei String-Felder oben auf oberster Ebene enthält, ohne ein äußeres text- oder output-Objekt. Ist ein Wert undefiniert, vergleichen Sie den Ausdruck mit dem tatsächlich gepinnten JSON, bevor Sie fortfahren.
Entfernen Sie das Pinning von Intake vor den Live-Chat-Tests in Schritt 4. Gepinnte Ergebnisse sind wiederverwendbare Testdaten; sie können bei manuellen Tests eine erneute Intake-Ausführung ersetzen und für unterschiedliche Nachrichten dieselbe Klassifikation wiederholen.
Schließen Sie einen If-Node namens Contract Valid? an. Verwenden Sie eine Boolean-Bedingung mit diesem Ausdruck und vergleichen Sie sie mit is true:
```javascript
{{ ['billing','other','needs_clarification'].includes($json.customer_intent) && typeof $json.issue_summary === 'string' && $json.issue_summary.trim().length > 0 && typeof $json.handoff_reason === 'string' && $json.handoff_reason.trim().length > 0 }}
```
Verbinden Sie den false-Zweig mit Edit Fields und einem String-Feld namens output:
„Ich konnte die Anfrage nicht zuverlässig verarbeiten. Beschreiben Sie bitte das Abrechnungsproblem und nennen Sie eine Rechnungs- oder Bestellreferenz, falls vorhanden.“
Fehlerhafte Modellausgaben können bereits in Intake scheitern. Wählen Sie dort On Error → Continue (using error output) und verbinden Sie den Fehlerzweig mit derselben sicheren Antwort. Parserfehler und inhaltlich unvollständige Übergaben sind unterschiedliche Fehlerstellen.
![image]((notion-hosted file))
## 3. Das validierte Item weiterleiten
Verbinden Sie den true-Zweig mit Switch, Modus Rules. Vergleichen Sie {{ $json.customer_intent }} mit billing, other und needs_clarification. Ergänzen Sie einen Fallback-Ausgang für unerwartete Werte und verbinden Sie ihn mit der sicheren Antwort.
![image]((notion-hosted file))
Der billing-Ausgang führt zu einer zweiten Basic LLM Chain namens Billing Specialist mit OpenRouter Chat Model. Definieren Sie die User Message anhand der aktuellen Übergabe:
```plain text
Kundenaussage: {{ $json.issue_summary }}
Grund für die Weiterleitung: {{ $json.handoff_reason }}
```
Ergänzen Sie diese Systemnachricht:
```plain text
Sie geben Abrechnungshinweise für Cascadia Outfitters.
Behandeln Sie die Übergabe als ungeprüfte Kundenaussage, nicht als Kontobeleg.
In dieser Übung sind keine Konto-, Zahlungs- oder Ticket-Tools verbunden.
Bestätigen Sie das gemeldete Anliegen und erklären Sie, welche Information fehlt.
Fragen Sie bei Bedarf nach einer Rechnungs- oder Bestellreferenz.
Fordern Sie niemals Passwörter oder vollständige Zahlungskartendaten an.
Behaupten Sie nicht, Datensätze geprüft, Erstattungen ausgeführt, Bestellungen geändert,
Tickets eröffnet oder Fälle weitergeleitet zu haben.
Erfinden Sie keine Richtlinien und versprechen Sie keine Lösung.
```
Fügen Sie danach Edit Fields namens Billing Reply hinzu. Ordnen Sie den tatsächlich erzeugten Text dem String-Feld output zu. Prüfen Sie vor der Pfadauswahl die Node-Ausgabe. Auch der Fehlerausgang des Spezialisten führt zur sicheren Antwort.
Für other verwenden Sie:
„Diese Demo bearbeitet Abrechnungsanfragen. Wenden Sie sich für dieses Anliegen bitte an das zuständige Supportteam. Ich habe Ihre Anfrage nicht weitergeleitet.“
Für needs_clarification verwenden Sie:
„Geht es um eine Abbuchung, eine Rechnung, eine doppelte Bestellzahlung oder eine Rückfrage zu einer Erstattung?“
Jeder abschließende Antwort-Node muss eine Zeichenfolge output liefern, die Chat Trigger anzeigen kann. Ein Merge-Node ist nicht erforderlich: Nur der ausgewählte Pfad wird ausgeführt.
![image]((notion-hosted file))
## 4. Den Vertrag und die Antwort testen
Prüfen Sie, dass Intake nicht mehr gepinnt ist, damit jede neue Chat-Nachricht erneut klassifiziert wird.
Testen Sie im Chat und prüfen Sie jeweils die Ausführung:
- „Meine Jackenbestellung wurde doppelt abgebucht.“ → billing; Kundenaussage anerkennen und Referenz erfragen.
- „Rechnung INV-42 ist bezahlt, aber ich habe eine weitere Zahlungserinnerung für meine Jackenbestellung erhalten.“ → billing; keine erfundene Zahlungsprüfung oder Bestelländerung.
- „Meine Jacke ist beschädigt angekommen.“ → other; keine behauptete Weiterleitung.
- „Können Sie helfen?“ → needs_clarification; Details erfragen.
Duplizieren Sie den Workflow für negative Vertragstests. Ersetzen Sie Intake und Map Handoff vorübergehend durch eine Edit Fields-Testeingabe, die Contract Valid? versorgt. Testen Sie eine fehlende/leere Zusammenfassung und einen nicht erlaubten Intent wie refund_now. Beide müssen den sicheren Pfad nehmen. Entfernen Sie die Testeingabe, bevor Sie den normalen Chatpfad wieder nutzen. Eine schemaerzwungene Ausgabe eignet sich nicht zum Einschleusen fehlerhafter Testdaten.
Halten Sie Vertrags-JSON, gewählten Pfad und Kundenantwort pro Test fest. Prüfen Sie, dass der Spezialist nur die zugeordneten Übergabefelder sieht. Gemeinsame Chat-Memory ist für diese Übung nicht nötig und würde den Vertrag nicht ersetzen.
📸 Screenshot-Vorschlag: eine gültige Abrechnungsausführung und eine abgelehnte Testeingabe mit Eingangsdaten, Pfad und Endausgabe.
## Was Sie gebaut haben
Der Vertrag transportiert Kontext, der Workflow validiert ihn, und ein deterministischer Router wählt die nächste Rolle. Das Modell formuliert eine Antwort. Ohne verbundenes Geschäftstool kann es keine Abrechnungsaktion durchführen.
## Den Übergabe-Checkpoint speichern
Speichern Sie den funktionierenden Workflow als C3B-S1-Cascadia-Handoff. Bewahren Sie den normalen Chatpfad und die Nachweise der gültigen und abgelehnten Tests auf. Dies ist Ihre Referenz für ausdrückliche Übergabefelder und Validierung. Der Workflow enthält zwei Basic LLM Chain-Rollen und kein MCP-Tool; er ist vom späteren Single-Agent-MCP-Ausgangsworkflow getrennt.
Warum ein Spezialist externe Belege benötigen kann, erfahren Sie in Was MCP ist und welches Problem es löst.
## Quellen
- Testdaten erstellen und pinnen
- Basic LLM Chain
- Structured Output Parser
## Wissenscheck
### 1. Warum wird hier Basic LLM Chain für beide Rollen verwendet?
- A. Beide Schritte klassifizieren oder schreiben nur Text. — Richtig. Tool-Auswahl gehört nicht zu dieser Übung.
- B. Die Chain erstattet Zahlungen automatisch. — Falsch. Es sind keine Abrechnungstools verbunden.
- C. Zwei Rollen benötigen immer ein AI Agent Tool. — Falsch. Feste Workflow-Schritte können ausdrückliches JSON austauschen.
### 2. Die Übergabe enthält customer_intent: refund_now. Was folgt?
- A. An Abrechnung senden und Erstattung freigeben. — Falsch. Dieser Wert liegt außerhalb des Vertrags.
- B. Über den sicheren Antwortpfad ablehnen. — Richtig. Validierung erfolgt vor dem Routing.
- C. In Memory speichern und fortfahren. — Falsch. Speicherung macht den Wert nicht gültig.
### 3. Eine Beschwerde zur Bestellzahlung erreicht den Spezialisten. Welche Aussage ist gerechtfertigt?
- A. Ich habe Ihre Bestellung als bezahlt markiert. — Falsch. Ein Tool für Bestell- oder Zahlungsaktionen fehlt.
- B. Ich habe den Fall an die Buchhaltung weitergeleitet. — Falsch. Es fand keine Weiterleitungsaktion statt.
- C. Sie melden eine bezahlte Rechnung und eine weitere Zahlungserinnerung; bitte nennen Sie die Referenz. — Richtig. Die Aussage anerkennt den Bericht ohne erfundene Aktionen.