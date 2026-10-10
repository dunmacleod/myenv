# Conversation History und Context Windows

Notion page: https://app.notion.com/p/Conversation-History-und-Context-Windows-3779418319f380fbbce6c1752dde2a86
Backed up before n8n migration

> 💡 In dieser Lektion stattest du deinen Flowise-Agenten mit einem Memory-Node aus, damit er den roten Faden über mehrere Runden hinweg nicht verliert. Anschließend prüfst du direkt im Praxistest, ob das System fehlerfrei läuft.

## Warum dieser Schritt jetzt kommt
Das Team der Contigo GmbH hat definiert, woran sich der Agent erinnern sollte, und eine Memory-Retention-Policy entworfen. Der nächste Schritt ist die Implementierung. Bevor etwas Komplexeres gebaut wird, braucht der Agent eine funktionierende Grundlage: die Fähigkeit, ein Gespräch über mehrere Turns hinweg zu führen, ohne Kontext zu verlieren.
Genau darum geht es in diesem Walkthrough. Du fügst einem Flowise-Agenten einen Memory-Node hinzu, verbindest ihn korrekt und führst einen einfachen Test aus, um zu bestätigen, dass die Konfiguration funktioniert, bevor du weitermachst.

## Was du baust
Einen Flowise-Chatflow mit einem Buffer-Memory-Node, der mit einer Conversational Chain verbunden ist. Der Memory-Node erfasst den laufenden Dialog und injiziert ihn zurück in jeden neuen Prompt, sodass das Sprachmodell Zugriff darauf hat, was in der aktuellen Session bereits gesagt wurde.
Das ist nur Kurzzeit-Memory. Es existiert für die Dauer der aktiven Session und wird gelöscht, wenn die Session endet. Persistentes, sessionübergreifendes Memory wird später in diesem Sprint behandelt.

> ✅ Wichtig: Bevor du an den folgenden Schritten arbeitest, stelle sicher, dass deine Gemini-API-Umgebung eingerichtet ist. Gehe für Anweisungen zu diesem Link.

### Schritt 1: Deinen Flowise-Canvas öffnen
Öffne dein Flowise-Dashboard und navigiere zu Chatflows. Öffne entweder deinen bestehenden Projekt-Canvas oder erstelle einen neuen Chatflow, indem du auf + Add New klickst.
Wenn du mit einem leeren Canvas beginnst, siehst du einen leeren Arbeitsbereich. Auf Komponenten greifst du zu, indem du auf dem Canvas auf den (+)-Button klickst.
![image]((notion-hosted file))

### Schritt 2: Einen Conversational-Chain-Node hinzufügen
Gehe zu (+) und suche unter LangChain in der Suchleiste nach Conversation Chain. Ziehe ihn auf den Canvas.
Die Conversation Chain fungiert als zentraler Orchestrator für diesen Flow. Sie verwaltet das Hin und Her zwischen Nutzer und Sprachmodell und hat eigene Eingabe-Sockets sowohl für ein Chatmodell als auch für eine Memory-Komponente.
![image]((notion-hosted file))

### Schritt 3: Ein Chatmodell hinzufügen und verbinden
Gehe zu (+) und suche unter LangChain in der Suchleiste nach deinem bevorzugten Chatmodell-Node (Google Gemini) und ziehe ihn auf den Canvas.
Verbinde den ChatGoogleGenerativeAI-Output des Google-Gemini-Knotens mit dem Chat Model-Input-Socket der Conversation Chain. Ein Socket ist der typisierte Verbindungspunkt eines Knotens, der einen kompatiblen Input oder Output eines anderen Knotens akzeptiert. Diese Verbindung teilt der Conversation Chain mit, welches Chat-Modell sie für die Generierung von Antworten verwenden soll.
Gehe zum Google-Gemini-Node, wähle Connect Credential aus und füge den Credential-Namen und deinen Google AI API Key hinzu. Stelle sicher, dass du diesen Schritt abschließt, bevor du fortfährst.
![image]((notion-hosted file))
> ✅ Gehe zu diesem Weblink, um einen Überblick über die Gemini-API-Modelle zu erhalten: https://ai.google.dev/gemini-api/docs/models

### Schritt 4: Einen Buffer-Memory-Node hinzufügen
Gehe zu (+) und suche unter LangChain in der Suchleiste in der Kategorie Memory nach Buffer Memory. Ziehe ihn auf den Canvas.
Verbinde den Output des Buffer-Memory-Nodes mit dem Memory-Eingabe-Socket der Conversation Chain.
![image]((notion-hosted file))
> ➡️ Warum  ist das wichtig : Der Buffer-Memory-Node erfasst den aktuellen Dialog und injiziert ihn in den Hintergrundkontext jedes neuen Prompts. Ohne diese Verbindung hat die Chain keinen Zugriff auf frühere Nachrichten und behandelt jede Nutzereingabe als Beginn eines neuen Gesprächs.

### Schritt 5: Eine Session ID konfigurieren
Wähle im Buffer-Memory-Node Additional Parameters aus und suche das Feld Session ID. Gib vorerst einen festen Testwert wie client_001 ein.
![image]((notion-hosted file))
> ➡️ Warum ist das wichtig: Die Session ID gruppiert den gesamten Gesprächsverlauf unter einer Kennung. In einer bereitgestellten Anwendung würde diese dynamisch pro Nutzer gesetzt werden, aber für Testzwecke reicht ein fester Wert aus. Die korrekte Session-Isolation konfigurierst du in der nächsten Lektion.

### Schritt 6: Speichern und testen
Speichere deinen Chatflow und öffne das integrierte Chatfenster, indem du oben rechts in der Oberfläche auf das Chat-Symbol klickst. Führe den folgenden Zwei-Turn-Test aus, um zu überprüfen, ob Memory funktioniert:
![image]((notion-hosted file))

> Turn 1: Mein Name ist Markus und meine Fallreferenz ist CG-7741.
> Turn 2: Wie lautet meine Fallreferenz?

## Worauf du achten solltest:
- Wenn der Agent mit CG-7741 antwortet, erfasst und injiziert der Memory-Node den Session-Kontext korrekt.
- Wenn der Agent erneut nach der Referenz fragt, überprüfe, ob der Output des Buffer-Memory-Nodes sicher mit dem Memory-Eingabe-Socket der Conversation Chain verbunden ist und ob der Canvas vor dem Testen gespeichert wurde.

## Checkliste: Vor dem Weitermachen bestätigen
- [ ] Buffer-Memory-Node zum Canvas hinzugefügt
- [ ] Output des Memory-Nodes mit dem Memory-Eingang der Conversation Chain verbunden
- [ ] Chatmodell-Node mit dem Language-Model-Eingang verbunden
- [ ] Session ID im Buffer-Memory-Node konfiguriert
- [ ] Zwei-Turn-Test abgeschlossen und Memory-Recall bestätigt

> 💡 Takeaway: 
  Ein Memory-Node ist die einfachste und grundlegendste Ergänzung für einen Flowise-Agenten. Ohne ihn beginnt jedes Gespräch bei null. Mit ihm kann der Agent Kontext über Turns hinweg halten, was die Voraussetzung für jedes komplexere Memory-Verhalten ist, das später in diesem Sprint behandelt wird.
