# Best Practices für API-Nutzung

Notion page: https://app.notion.com/p/Best-Practices-f-r-API-Nutzung-3789418319f380b8be94c5ab4f157674
Backed up before n8n migration

> 💡 Am Ende dieser Lektion verstehst du: wie Modell-APIs in n8n verantwortungsvoll genutzt werden, wie Credentials geschützt werden, wie typische Fehler behandelt werden und wie Modelleinstellungen gewählt werden, ohne veraltete Annahmen fest einzubauen.
## API-Zugriff ist etwas anderes als eine Chat-Webseite
Eine Chat-Webseite ist für Menschen gedacht, die Nachrichten manuell eingeben. Eine API ist für Software gedacht.
In n8n ruft der Workflow das Modell über die OpenRouter Chat Model Node auf. Die Authentifizierung erfolgt über ein in n8n gespeichertes OpenRouter-Credential.
## 1. Credentials gehören nicht in Workflow-Texte
Füge einen API-Key niemals in einen Prompt, einen Wert in Set/Edit Fields, eine Code Node, einen Screenshot oder einen geteilten Workflow-Export ein.
Erstelle stattdessen ein n8n-Credential und wähle es in der Node aus.
> 📸 SCREENSHOT-VORSCHLAG: OpenRouter-Credential-Formular in n8n. Das API-Key-Feld muss verborgen oder unkenntlich gemacht sein.
## 2. API-Fehler sind normal
Typische Kategorien:
- 401 / Authentifizierungsfehler: falscher, widerrufener oder fehlender Key.
- 429 / Rate Limit: zu viele Requests in kurzer Zeit oder Provider-Limit erreicht.
- Timeout: der Provider antwortet nicht innerhalb der konfigurierten Zeit.
- 5xx / Provider-Fehler: temporärer Fehler beim Anbieter.
Die OpenRouter Chat Model Node bietet Optionen wie Timeout und Max Retries. Nutze sie bewusst.
> 📸 SCREENSHOT-VORSCHLAG: OpenRouter Chat Model Node mit sichtbaren Optionen Timeout und Max Retries.
## 3. Nicht auf einen dauerhaften Modellnamen bauen
OpenRouter stellt die Modelle bereit, die für dein Konto verfügbar sind, und n8n lädt diese dynamisch.
Wähle das für den Kurs vorgesehene Modell. Wenn sich der genaue Modellname später ändert, sollte die Workflow-Architektur trotzdem funktionieren.
Denke von der Aufgabe aus:
- einfache Klassifikation oder kurze Antworten → schnelles, kosteneffizientes Modell;
- komplexes Reasoning → stärkeres Modell kann sinnvoll sein;
- maschinenlesbare Ausgabe → wenn geeignet JSON verwenden.
## 4. Ausgabelänge und Zufälligkeit kontrollieren
Nützliche Einstellungen:
- Maximum Number of Tokens — begrenzt die Antwortlänge.
- Sampling Temperature — höhere Werte erzeugen mehr Variation, aber weniger Determinismus.
- Response Format — Text oder, wenn unterstützt, JSON.
Für operative Agenten sind kurze Antworten und geringere Zufälligkeit leichter zu testen.
## 5. Kosten und Daten als Architekturthema behandeln
Vor einem produktiven Einsatz:
- schätze die Anzahl der Modellaufrufe pro Workflow-Ausführung;
- halte Prompts fokussiert;
- vermeide unkontrollierte Schleifen;
- protokolliere Fehler und Retries;
- sende nur wirklich benötigten Kontext;
- nutze im Kurs synthetische oder freigegebene Daten.
Vor einem echten Deployment müssen Datenverarbeitung und interne Sicherheitsanforderungen geprüft werden.
## Mini-Check
- Credential sofort ungültig → Authentifizierung.
- Im Einzeltest funktioniert alles, bei hoher paralleler Nutzung entstehen Fehler → wahrscheinlich Rate Limit.
- Fließtext wird geliefert, die nächste Node erwartet Felder → Ausgabeformat oder Parsing.
- Screenshot zeigt den kompletten API-Key → Key rotieren.
> 💡 Takeaway: Eine zuverlässige Modellintegration bedeutet mehr als eine erfolgreiche Testantwort. Schütze Credentials, plane Fehler ein, halte Einstellungen explizit und entkopple die Workflow-Architektur vom konkreten Modellnamen.