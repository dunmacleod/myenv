# Workflows vs. agentische Entscheidungsfindung

Notion page: https://app.notion.com/p/Workflows-vs-agentische-Entscheidungsfindung-3779418319f3801982e2d52fbda7572a
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Die Conversational Retrieval QA Chain durch einen Tool-Agent-Node ersetzen, ein Retriever-Tool für Abfragen der Wissensdatenbank sowie ein Custom Tool anschließen, das eine Kreditstatusabfrage simuliert, die System-Prompt-Anweisungen und Schutzmechanismen aus den vorherigen Lektionen umsetzen und überprüfen, dass Speicher, Abfrage und Tools als ein zusammenhängendes System funktionieren.

## Warum dieser Schritt jetzt kommt
Contigo GmbHs Support-Agent kann mehrstufige Gespräche führen, präzise aus der Wissensdatenbank abrufen und Grounding-Verhalten durchsetzen. Er kann jedoch nicht handeln. Fragt ein Kunde nach dem Status seines Kreditantrags, ruft der Agent einen Richtlinienabschnitt zu Antragslaufzeiten ab und formuliert eine professionelle Erklärung des Prozesses. Er kann das Live-System nicht abfragen.
Diese Anleitung ändert das. Am Ende wird der Agent Tools nutzen, um Anfragen zu beantworten, die Live-Daten erfordern, während er weiterhin für Richtlinien- und Produktfragen aus der Wissensdatenbank abruft, alles innerhalb desselben Chatflows, derselben Speicherkonfiguration und derselben Sitzungsisolierung, die du in Sprint 1 und 2 gebaut hast.
Die Änderungen am Canvas in dieser Lektion sind die umfangreichsten seit dem ursprünglichen Aufbau des Chatflows. Du fügst der bestehenden Chain nichts hinzu. Du ersetzt sie durch einen leistungsfähigeren Node. Die Conversational Retrieval QA Chain erledigte eine Aufgabe: abrufen und generieren. Der Tool Agent übernimmt mehrere Aufgaben: schlussfolgern, welches Tool zu nutzen ist, es aufrufen, das Ergebnis beobachten und eine fundierte Antwort generieren.
## Was du baust
Einen Flowise-Tool-Agent-Chatflow mit:
- OpenRouter-Node: das Sprachmodell, übernommen aus Sprint 1
- Buffer-Window-Memory-Node: Sitzungsspeicher, übernommen aus Sprint 1
- Qdrant-Node: der Vektorspeicher, übernommen aus Sprint 2
- Google-Gemini-Embedding-Node: Embeddings zur Abfragezeit, übernommen aus Sprint 2
- Retriever-Tool-Node: umschließt den Qdrant-Retriever, damit der Tool Agent ihn als Tool aufrufen kann
- Custom-Tool-Node: simuliert eine Kreditstatusabfrage, die Testdaten zurückgibt
- Calculator-Node: ein integriertes Tool ohne API-Schlüssel, genutzt zur Überprüfung des Tool-Aufrufs
- Tool-Agent-Node: der neue Orchestrierungs-Node, der die Conversational Retrieval QA Chain ersetzt
## Folge diesen Schritten
### Schritt 1: Öffne deinen bestehenden Chatflow
Öffne deine lokale Flowise-Instanz unter http://localhost:3000. Öffne den Chatflow, an dem du bisher gearbeitet hast. Bevor du Änderungen vornimmst, exportiere den aktuellen Chatflow als JSON-Sicherung. Klicke oben rechts auf das Settings-Symbol und wähle Export Chatflow. Speichere die Datei als contigo_sprint2_backup.json. Sollte während dieser Anleitung etwas schiefgehen, kannst du diese Datei erneut importieren und vom aktuellen funktionierenden Stand aus neu starten.
### Schritt 2: Entferne den Conversational-Retrieval-QA-Chain-Node
Klicke auf den Conversational-Retrieval-QA-Chain-Node und lösche ihn vom Canvas.
### Schritt 3: Füge den Tool-Agent-Node hinzu
Klicke auf (+), um das Node-Panel zu öffnen. Suche im Tab LangChain nach Tool Agent und ziehe ihn auf das Canvas.
Der Tool-Agent-Node hat folgende Eingänge:
- Tool Calling Chat Model (Pflichtfeld), verbinde hier die Ausgabe von ChatGoogleGenerativeAI
- Memory (Pflichtfeld), verbinde hier die Ausgabe von BufferWindowMemory
- Tools (Pflichtfeld), hier verbindest du in den nächsten Schritten die Tools
- Input Moderation (optional), vorerst leer lassen
- Chat Prompt Template (optional), vorerst leer lassen
### Schritt 4: Füge den Retriever-Tool-Node hinzu
Der Qdrant-Node auf deinem Canvas gibt einen Vektorspeicher-Retriever aus. Damit dieser Retriever dem Tool Agent als aufrufbares Tool zur Verfügung steht, musst du ihn in einen Retriever-Tool-Node einbetten. Klicke auf (+), suche im Tab LangChain nach Retriever Tool und ziehe ihn auf das Canvas.
Konfiguriere den Retriever-Tool-Node wie folgt:
- Name: contigo_knowledge_base
- Description: Trage die Anweisung zum Abfrageumfang ein, die du geschrieben hast (siehe die Checkliste in der vorherigen Lektion), also die überarbeitete Anweisung, die festlegt, dass dieses Tool Inhalte aus Contigos statischer Richtlinien- und Produktdokumentation in Qdrant abruft und aufgerufen werden soll, wenn die Anfrage nach Informationen aus dokumentierten Richtlinien, Produktleitfäden oder Compliance-Unterlagen fragt.
- Vector Store Retriever: Verbinde hier die Ausgabe Qdrant Retriever des Qdrant-Nodes
Verbinde die Ausgabe des Retriever-Tool-Nodes mit dem Eingang Tools am Tool-Agent-Node.
> ➡️ Warum das wichtig ist: Der Tool Agent kann nicht direkt aus einem Vektorspeicher lesen. Er kann nur Tools aufrufen. Der Retriever-Tool-Node ist die Brücke dazwischen. Er verpackt den Qdrant-Retriever als benanntes, beschriebenes Tool, das der Tool Agent über die ReAct-Schleife auswählen und aufrufen kann, wenn eine Anfrage eine Abfrage der Wissensdatenbank erfordert.

### Schritt 5: Füge den Calculator-Node hinzu
Der Calculator ist ein integriertes Flowise-Tool, das weder API-Schlüssel noch externes Konto benötigt. Er verschafft dem Tool Agent die Fähigkeit, präzise mathematische Berechnungen durchzuführen. Klicke auf (+), suche im Tab LangChain nach Calculator und ziehe ihn auf das Canvas. Es ist keine Konfiguration erforderlich.
Verbinde die Ausgabe des Calculator-Nodes mit dem Eingang Tools am Tool-Agent-Node.
> ➡️ Warum der Calculator enthalten ist: Er bietet eine sofortige Möglichkeit ohne jede Konfiguration, zu überprüfen, ob der Tool Agent Tools über die ReAct-Schleife korrekt aufruft. Sendest du eine Rechenaufgabe und der Agent ruft den Calculator auf, statt eine Zahl aus seinen Trainingsdaten zu generieren, funktioniert die Tool-Weiterleitung korrekt. Zudem verschafft er Contigos Agenten eine wirklich nützliche Fähigkeit, indem er Kreditrückzahlungsbeträge oder Zinsbeträge auf Anfrage berechnet.
> ⚠️ Speichere deinen Chatflow, bevor du zu Schritt 6 übergehst.

### Schritt 6: Erstelle das Custom Tool als Kreditstatusabfrage und füge es hinzu
Das Kreditstatus-Tool simuliert eine Live-Abfrage zur Antragsverfolgung. Es verbindet sich nicht mit einer echten Banken-API. Es gibt Testdaten zurück, die auf der übergebenen Antragsreferenz basieren. Das reicht aus, um Tool-Aufruf, Parameterübergabe und die ReAct-Schleife in einer Kursumgebung zu testen.
Verlasse deinen Chatflow und suche im linken Navigationsbereich deines Flowise-Dashboards nach Tools. Klicke oben rechts auf Create.
Konfiguriere das Custom Tool wie folgt:
Name: loan_status_lookup
Description: Trage die Beschreibung des Kreditstatus-Tools ein, die du in der vorherigen Lektion geschrieben hast, also die überarbeitete Anweisung, die festlegt, dass dieses Tool das Live-System zur Antragsverfolgung abfragt und nur dann aufgerufen werden soll, wenn der Kunde eine konkrete Antragsreferenz angibt oder nach dem aktuellen Bearbeitungsstatus eines laufenden Antrags fragt.
Input Schema: Füge einen Eingabeparameter hinzu:
- Parameter name: application_reference
- Type: String
- Description: Die Antragsreferenznummer des Kunden, zum Beispiel APP-7741. Diese muss in der Kundenanfrage ausdrücklich angegeben sein, bevor das Tool aufgerufen wird.
- Required: Ja
![image]((notion-hosted file))
JavaScript Function: Trage den folgenden Code ein:
```javascript
const ref = $application_reference;

const mockData = {
  "APP-7741": { status: "Under review", stage: "Credit assessment", estimatedCompletion: "5 business days" },
  "APP-8841": { status: "Approved", stage: "Documentation pending", estimatedCompletion: "2 business days" },
  "APP-9921": { status: "On hold", stage: "Additional information required", estimatedCompletion: "Pending client response" }
};

if (mockData[ref]) {
  const d = mockData[ref];
  return `Application ${ref}: Status — ${d.status}. Current stage — ${d.stage}. Estimated completion — ${d.estimatedCompletion}.`;
} else {
  return `Application reference ${ref} was not found in the tracking system. Please verify the reference number and try again.`;
}
```
Wähle „Add" aus, das Tool steht nun zur Verfügung. Kehre zu deinem Chatflow-Canvas zurück. Klicke auf (+), um das Node-Panel zu öffnen. Suche im Tab LangChain nach Custom Tool und ziehe ihn auf das Canvas. Suche in den Einstellungen des Custom-Tool-Nodes das Dropdown-Menü Selected Tool. Klicke darauf und wähle loan_status_lookup aus der Liste. Falls es dort nicht erscheint, prüfe, ob du das Tool korrekt gespeichert hast, und lade die Seite neu.
Verbinde die Ausgabe des Custom-Tool-Nodes mit dem Eingang Tools am Tool-Agent-Node.
### Schritt 7: Konfiguriere den System-Prompt des Tool Agent
Öffne die Additional Parameters des Tool-Agent-Nodes und suche das Feld System Message. Trage Folgendes ein (basierend auf den Informationen, die du in den vorherigen Lektionen zusammengetragen hast):
> Du bist ein Support-Agent für die Contigo GmbH, ein Finanzdienstleistungsunternehmen mit Tätigkeit in Deutschland, Österreich und den Niederlanden. Beantworte Kundenfragen ausschließlich anhand der Informationen, die aus Contigos Wissensdatenbank abgerufen werden. Nutze kein externes Wissen und triff keine Annahmen, die über den abgerufenen Kontext hinausgehen. Du kannst Kontoverfahren und Richtlinien erklären, aber keine Änderungen an einem Kundenkonto vornehmen. Fordert ein Kunde eine Kontoänderung an, teile ihm klar mit, dass du keine Kontoänderungen vornehmen kannst, und verweise ihn darauf, seinen Contigo-Kundenbetreuer zu kontaktieren oder das Kundenportal zu besuchen. Ist die Antwort nicht im abgerufenen Kontext enthalten und liefert kein Tool ein relevantes Ergebnis, antworte mit: „Diese Information liegt mir in meiner aktuellen Wissensdatenbank nicht vor. Bitte wende dich für weitere Unterstützung direkt an einen Contigo-Berater." Gibt ein Tool einen Fehler zurück oder liefert es auch nach mehreren Versuchen kein Ergebnis, antworte mit: „Ich konnte diese Information zu diesem Zeitpunkt nicht abrufen. Bitte wende dich für Unterstützung direkt an deinen Contigo-Kundenbetreuer, mit der Referenz [nenne hier jede vom Kunden angegebene Referenznummer]." Zeige in keiner kundenseitigen Antwort Fehlercodes, API-Referenzen oder technische Details.
### Schritt 8: Setze den Parameter Max Iterations
Bleibe in den Additional Parameters und suche das Feld Max Iterations. Trage den Wert ein, den du in der vorherigen Lektion festgelegt hast. Falls du dich noch nicht entschieden hast, verwende 6 als Standardwert.
### Schritt 9: Speichern und die Validierungstests durchführen
Speichere den Chatflow und öffne die integrierte Chat-Oberfläche. Führe die folgenden acht Tests der Reihe nach durch. Notiere jede Antwort, bevor du zum nächsten Test übergehst.
Sieh unten, wie es aussehen sollte.
![image]((notion-hosted file))

Test 1: Speicherkontinuität
Sende: „Hallo, mein Name ist Markus Bauer und meine offene Fallreferenz lautet CG-4821." Sende anschließend: „Wie lautet meine Fallreferenz und wie habe ich dir gesagt, dass ich heiße?"
Erwartung: Der Agent erinnert sich an CG-4821 und Markus Bauer, ohne den Kunden zu bitten, eine der beiden Angaben zu wiederholen. Das bestätigt, dass der Buffer-Window-Memory korrekt mit dem Tool Agent verbunden ist.
✅ Bestanden: Der Agent erinnert sich korrekt an beides.
❌ Nicht bestanden: Prüfe, ob der Buffer-Window-Memory-Node mit dem Eingang Memory am Tool Agent verbunden ist und ob die Session ID konfiguriert ist.
Test 2: Abfrage der Wissensdatenbank über das Retriever Tool
Sende: „Welche Unterlagen muss ein Kunde bei einem KMU-Kreditantrag einreichen?"
Erwartung: Der Tool Agent ruft das Retriever-Tool contigo_knowledge_base auf und liefert eine konkrete Antwort aus der Wissensdatenbank. Prüfe die Zwischenschritte des Agenten im Chat-Panel, um zu bestätigen, dass das Retriever Tool aufgerufen wurde.
✅ Bestanden: Der Agent ruft das Retriever Tool auf und liefert eine konkrete Antwort aus der Wissensdatenbank.
❌ Nicht bestanden: Prüfe, ob der Retriever-Tool-Node korrekt mit dem Eingang Tools verbunden ist und ob die Ausgabe Qdrant Retriever mit dem Eingang Vector Store Retriever des Retriever Tools verbunden ist.
Test 3: Aufruf des Calculator-Tools
Sende: „Wenn die monatliche Kreditrate eines Kunden 847 € beträgt und die Kreditlaufzeit 36 Monate umfasst, wie hoch ist der insgesamt zurückgezahlte Betrag?"
Erwartung: Der Tool Agent ruft das Calculator-Tool auf und liefert 30.492 €. Das bestätigt, dass die Tool-Weiterleitung funktioniert und der Agent das mathematische Ergebnis nicht aus seinen Trainingsdaten generiert.
✅ Bestanden: Der Agent ruft den Calculator auf und liefert das korrekte Ergebnis.
❌ Nicht bestanden: Prüfe, ob der Calculator-Node mit dem Eingang Tools am Tool Agent verbunden ist.
Test 4: Aufruf des Kreditstatus-Tools mit gültiger Referenz
Sende: „Kannst du den Status meines Antrags mit der Referenz APP-8841 prüfen?"
Erwartung: Der Tool Agent ruft loan_status_lookup mit APP-8841 als Parameter auf und liefert den simulierten Status: Genehmigt, Dokumentation ausstehend, voraussichtlich 2 Werktage.
✅ Bestanden: Der Agent ruft das Tool auf und liefert den korrekten simulierten Status.
❌ Nicht bestanden: Prüfe, ob der Custom-Tool-Node mit dem Eingang Tools verbunden ist und ob die Tool-Beschreibung die Aufrufbedingung klar genug festlegt, um sie vom Wissensdatenbank-Tool zu unterscheiden.
Test 5: Kreditstatus-Tool mit ungültiger Referenz
Sende: „Wie ist der Status von Antrag APP-0000?"
Erwartung: Der Tool Agent ruft loan_status_lookup auf, erhält die Nicht-gefunden-Antwort der JavaScript-Funktion und teilt dem Kunden mit, dass die Referenz nicht gefunden wurde, und bittet ihn, sie zu überprüfen.
✅ Bestanden: Der Agent ruft das Tool auf, erhält die Nicht-gefunden-Antwort und kommuniziert sie professionell.
❌ Nicht bestanden: Erfindet der Agent einen Status, statt das Tool aufzurufen, muss die Aufrufbedingung in der Tool-Beschreibung konkreter formuliert werden.
Test 6: Grenze bei Kontoaktionen
Sende: „Bitte aktualisiere meine registrierte E-Mail-Adresse auf k.brandt@example.de"
Erwartung: Der Agent suggeriert nicht, die Änderung vorgenommen zu haben. Er erklärt anhand der Wissensdatenbank das Verfahren zur Aktualisierung von Kontaktdaten und verweist den Kunden an den richtigen Kanal. Er ruft weder das Kreditstatus-Tool noch den Calculator auf.
✅ Bestanden: Der Agent erklärt das Verfahren und verweist den Kunden an den Kundenbetreuer oder das Kundenportal.
❌ Nicht bestanden: Überarbeite die Anweisung zur Grenze bei Kontoaktionen in der System Message, um die Unterscheidung zwischen Information und Handlung deutlicher zu machen.
Test 7: Anfrage außerhalb des Themenbereichs
Sende: „Wie hoch ist der aktuelle Leitzins der Europäischen Zentralbank?"
Erwartung: Es wird kein Tool aufgerufen. Der Agent liefert die konfigurierte Ausweichformulierung, er nennt keine EZB-Zinszahl aus seinen Trainingsdaten.
✅ Bestanden: Der Agent liefert die Ausweichformulierung.
❌ Nicht bestanden: Verschärfe die Anweisung zum Abfrageumfang in der System Message, um die Nutzung von allgemeinem Trainingswissen ausdrücklich zu untersagen.
Test 8: Speicher und Tools im Zusammenspiel
Sende: „Kannst du anhand dessen, was ich dir vorhin gesagt habe, den Status von Fall CG-4821 prüfen und mir sagen, welche Unterlagen Markus einreichen müsste?"
Erwartung: Der Agent erinnert sich anhand des Buffer-Window-Memory-Nodes an Markus Bauer und CG-4821, ruft für den Fallstatus das Tool loan_status_lookup auf und ruft für die Dokumentenanforderungen das Retriever Tool contigo_knowledge_base auf, wobei er alle drei in einer einzigen Antwort zusammenführt.
✅ Bestanden: Der Agent verbindet Speicherkontext, Tool-Ergebnis und Abfrage der Wissensdatenbank in einer einzigen Antwort.
❌ Nicht bestanden: Diagnostiziere, welche Komponente fehlschlägt, indem du Test 1, 2 und 4 einzeln durchführst und die Ergebnisse prüfst.
## Checkliste: Vor dem Fortfahren bestätigen
- [ ] Conversational-Retrieval-QA-Chain-Node vom Canvas entfernt
- [ ] Tool-Agent-Node hinzugefügt und mit ChatGoogleGenerativeAI sowie Buffer Window Memory verbunden
- [ ] Retriever-Tool-Node hinzugefügt, mit Beschreibung der Wissensdatenbank konfiguriert und mit der Ausgabe Qdrant Retriever sowie dem Eingang Tools am Tool Agent verbunden
- [ ] Calculator-Node hinzugefügt und mit dem Eingang Tools am Tool Agent verbunden
- [ ] Custom Tool loan_status_lookup mit korrekter JavaScript-Funktion und Beschreibung erstellt
- [ ] Custom-Tool-Node zum Canvas hinzugefügt und mit dem Eingang Tools am Tool Agent verbunden
- [ ] System Message mit allen überarbeiteten Anweisungen aus A12.1 und dem Ausweichverhalten aus A12.2 konfiguriert
- [ ] Parameter Max Iterations in den Additional Parameters gesetzt
- [ ] Alle acht Validierungstests durchgeführt und Ergebnisse protokolliert
- [ ] Alle acht Tests bestanden, bevor du fortfährst
> 💡 Fazit:
  Der Tool-Agent-Node ist die architektonische Weiterentwicklung, die deinen Chatflow von einem Abfragesystem in einen handlungsfähigen Agenten verwandelt. Die ReAct-Schleife läuft bei jeder Anfrage automatisch ab. Die Qualität deiner Tool-Beschreibungen und System-Prompt-Anweisungen ist es, was diese Schleife zuverlässig macht.
  Die Speicherkonfiguration aus Sprint 1 und die Wissensdatenbank aus Sprint 2 sind beide vollständig aktiv. Der Tool Agent orchestriert sie gemeinsam mit den neuen Tools, die du gerade angeschlossen hast.
