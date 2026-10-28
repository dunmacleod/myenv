# End-to-End Testing und Flow Validation

Notion page: https://app.notion.com/p/End-to-End-Testing-und-Flow-Validation-3789418319f380a88449c812a9fac444
Backed up before n8n migration

> 💡 Das machst du in dieser Lektion: Du führst einen kompletten End-to-End-Test des Meridian Agentflow v2 über alle Fähigkeiten hinweg in einer einzigen verifizierten Session durch und bestätigst, dass das Canvas produktionsreif ist, bevor die Präsentationsvorbereitung beginnt.

## Die Ausgangslage
Meridians Agent ist überarbeitet und abgesichert, und die drei produktionsblockierenden Fehler sind behoben. Die Fixes wurden einzeln validiert. Modelloptimierung getestet mit einer Begrüßung. Routing getestet mit einer Account-Referenz. Fehlerbehandlung getestet mit einem erzwungenen Timeout.
Eine einzelne Validierung ersetzt keine End-to-End-Validierung. Testest du jeden Fix isoliert, bestätigst du nur, dass die jeweilige Fehlerart behoben ist. Du bestätigst damit nicht, dass die Fixes im Zusammenspiel funktionieren, dass kein Fix eine Regression in einer anderen Fähigkeit ausgelöst hat oder dass der komplette Ausführungspfad von der Consultant-Anfrage bis zur formatierten Antwort auf jedem Pfad im Canvas intakt ist.
Diese Lektion führt genau diese vollständige Validierung durch. Am Ende hast du jeden Pfad im Meridian Agentflow v2 in einer einzigen Session durchgespielt, und das Canvas ist nachweislich produktionsreif.
## Bevor du startest
Bevor du die Chat-Oberfläche öffnest, prüfe Folgendes:
Docker:
```plain text
dockerps
```
Beide Container, flowise und qdrant, müssen als laufend angezeigt werden. Falls einer davon gestoppt ist:
```plain text
dockerstartflowise
dockerstartqdrant
```
HTTP-Node-URL:
Bestätige, dass beim HTTP-Node die richtige URL eingetragen ist, nicht die Test-URL für den Fehlerfall: https://jsonplaceholder.typicode.com/todos/1
Canvas gespeichert:
Öffne das Canvas Meridian Base Agent unter http://localhost:3000 und bestätige, dass das Speicher-Symbol keine ungespeicherten Änderungen anzeigt.
## Das End-to-End-Testprotokoll
Führe alle sieben Interaktionen wie angegeben über drei getrennte Sessions aus. Lass keine Interaktion aus und kombiniere keine Sessions. Die Session-Grenzen sind Teil des Testdesigns.
### Session 1: Wissen und Kontext-Erhalt
Öffne eine neue Chat-Session.
Austausch 1 - Wissensabfrage: What is Meridian's escalation procedure for a severity level 2 client issue?
- Erwartet: Condition Node gibt an Condition Agent weiter → routet zu knowledge_query → Agent Node A ruft Daten aus dem Document Store ab → gibt das Eskalationsverfahren mit der 4-Stunden-Vorgabe zurück.
- Bestehenskriterium: Die Antwort enthält Inhalte aus meridian_engagement_standards.txt. Die Antwort erfindet keine Richtliniendetails, die nicht im Dokument stehen.
Austausch 2 - Kontext-Erhalt über mehrere Turns: How many working hours would I have left if the issue was first reported at 2pm today?
- Erwartet: Agent Node A nutzt den Session-Speicher, um das 4-Stunden-Eskalationsfenster aus Austausch 1 auf die konkrete Situation des Consultants anzuwenden, ohne den Document Store erneut abzufragen.
- Bestehenskriterium: Die Antwort rechnet korrekt anhand der abgerufenen Richtlinie, ohne eine neue Abfrage auszulösen. Die Antwort bezieht sich auf denselben Richtlinieninhalt wie in Austausch 1.
Austausch 3 - Regionale Wissensabfrage: What language should client materials be prepared in for a Poland engagement?
- Erwartet: Condition Agent routet zu knowledge_query → Agent Node A ruft Daten aus dem Regional-Playbook-Abschnitt des Document Store ab.
- Bestehenskriterium: Die Antwort verweist auf die polnische Sprachpräferenz aus meridian_regional_playbook.txt. Die Antwort erfindet keine regionalen Vorgaben.
### Session 2: Status-Pfad und Human Input
Öffne eine neue Chat-Session.
Austausch 4 - Status-Anfrage mit Human-Input-Freigabe: Can you check the current engagement status for account 1?
- Erwartet: Condition Agent routet zu status_request → HTTP Node ruft Daten ab → Condition A bestätigt, dass Daten vorhanden sind → Human Input Node pausiert mit den Buttons Proceed und Reject.
- Klick auf Proceed.
- Bestehenskriterium: Agent Node B gibt eine formatierte Engagement-Zusammenfassung in natürlicher Sprache zurück. Die Antwort enthält kein rohes JSON. Direct Reply B liefert die Antwort aus.
Austausch 5 - Freigabe ablehnen
- Öffne eine neue Session. Schick dieselbe Status-Anfrage. Wenn der Human Input Node pausiert, klick auf Reject.
- Bestehenskriterium: Es wird eine Ablehnungsmeldung zurückgegeben. Agent Node B wird nicht ausgeführt. Es werden keine Engagement-Daten angezeigt.
### Session 3: Retry-Logik und Fallback
Öffne eine neue Chat-Session.
Austausch 6 - Retry-Logik
- Ändere die URL des HTTP-Node vorübergehend auf: https://jsonplaceholder.typicode.com/invalid/9999
- Speichere das Canvas. Schick: Can you check the engagement status for the Krauss account?
- Erwartet: HTTP Node schlägt fehl → Condition A Output 0 → Custom Function erhöht den Zähler → Condition B → nach 2 Retries → Direct Reply C mit Fallback-Nachricht.
- Bestehenskriterium: Nach den Retry-Versuchen wird die Fallback-Nachricht zurückgegeben. Kein erfundener Engagement-Status in der Antwort. Es wählt Direct Reply C, nicht Direct Reply B.
- Stell die URL des HTTP-Node wieder her auf: https://jsonplaceholder.typicode.com/todos/1
- Speichere das Canvas.
Austausch 7 - Anfrage außerhalb des Scopes
- Öffne eine neue Session. Schick: Can you give me a summary of Meridian's revenue for this financial year?
- Erwartet: Condition Agent routet zu knowledge_query → Agent Node A erkennt, dass die Anfrage außerhalb seines autorisierten Scopes liegt → gibt die Fallback-Formulierung mit einem konstruktiven nächsten Schritt zurück.
- Bestehenskriterium: Der Agent erfindet keine Finanzdaten. Die Antwort enthält die definierte Fallback-Formulierung. Die Antwort bietet einen konkreten nächsten Schritt an.
## Ergebnisse festhalten
Halte zu jedem Austausch fest:
[TABLE]
  | Austausch | Genommener Pfad | Bestanden oder nicht | Notizen |
  | 1 - Wissensabfrage |  |  |  |
  | 2 - Kontext-Erhalt |  |  |  |
  | 3 - Regionales Wissen |  |  |  |
  | 4 - Status mit Freigabe |  |  |  |
  | 5 - Freigabe ablehnen |  |  |  |
  | 6 - Retry-Logik |  |  |  |
  | 7 - Außerhalb des Scopes |  |  |  |
Fällt ein Austausch durch, diagnostiziere ihn mit der Diagnosetabelle aus dem Sprint-3-Orchestration-Checkpoint.
## Bestehensgrenze
Alle sieben Interaktionen müssen bestehen, bevor das Canvas für die Präsentation als produktionsreif gilt. Ein Canvas mit ungelösten Fehlern ist nicht bereit für eine Demo vor einem Stakeholder. Fehler, die live während einer Präsentation auffallen, richten deutlich mehr Schaden an als Fehler, die schon während der Validierung entdeckt und behoben wurden.
## Finale Canvas-Checkliste
Bevor du diese Lektion abschließt, bestätige:
- [ ] Alle sieben Interaktionen haben bestanden
- [ ] URL des HTTP-Node wiederhergestellt auf https://jsonplaceholder.typicode.com/todos/1
- [ ] Canvas gespeichert
- [ ] Docker-Logs zeigen keine Fehler. Prüfe mit docker logs flowise --tail 20
- [ ] Keine 429-Rate-Limit-Fehler in den Logs. Falls doch, notier dir die Uhrzeit und warte vor der Präsentation
> 💡 Fazit:
  Die End-to-End-Tests machen den Unterschied zwischen einem Canvas, das konfiguriert wurde, und einem Canvas, das auch verifiziert wurde. Einzelne Node-Tests bestätigen, dass jede Komponente für sich funktioniert. Ein End-to-End-Test bestätigt, dass sie im Zusammenspiel funktionieren: Routing-Entscheidungen stimmen, Kontext wird wie erwartet zwischen Nodes übergeben, Fehlerpfade schließen sauber ab, und die Grenzen des Agenten halten auch unter realistischen Anfragebedingungen. Das ist die Validierung, die einem Stakeholder das Vertrauen gibt, dass die Demo, die er gleich sieht, ein System zeigt, das tatsächlich funktioniert.
