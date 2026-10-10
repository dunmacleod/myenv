# Ein Single-Agent-System Ende-zu-Ende entwerfen

Notion page: https://app.notion.com/p/Ein-Single-Agent-System-Ende-zu-Ende-entwerfen-2dd9418319f382f9a06a010b4b7cdc01
Backed up before n8n migration

Die vorherigen fünf Lektionen haben Velas Team ein Framework für Architekturentscheidungen gegeben. Selin hat es angewendet und ist zu einer klaren Schlussfolgerung gekommen: Der richtige Ausgangspunkt für Vela ist ein gut entworfenes Single-Agent-System, eines, das mit expliziten Entscheidungen darüber gebaut wird, wofür der Agent da ist, was er nicht tut und wie ein Fehler aussieht. Die bestehende Canvas ist ohne Plan gewachsen und taugt dafür nicht als Vorlage.
Dieser Walkthrough baut diesen Agenten. Der Ausgangspunkt ist die Modul-Baseline, eine Agentflow-V2-Canvas mit drei Nodes, die bereits läuft, bereits mit Gemini kommuniziert und bereits zwei leere Flow-State-Schlüssel deklariert hat. Ihre Aufgabe besteht darin, eine vorhandene Canvas in eine Canvas zu verwandeln, die entworfen ist.
> 💡 Am Ende dieses Walkthroughs haben Sie ein Single-Agent-System mit dokumentiertem Scope, einem verfeinerten System-Prompt, definierten Eingaben und Ausgaben sowie einer klaren Aussage dazu, was der Agent bewusst nicht tut. Diese Dokumentation ist genauso Teil der Abgabe wie die Canvas selbst.
Ein funktionierender Agent und ein entworfener Agent sind nicht dasselbe. Der Walkthrough baut beides gleichzeitig.
### Bevor Sie beginnen
Sie benötigen:
- Flowise läuft unter http://localhost:3000. Wenn Flowise nicht läuft, öffnen Sie Docker Desktop und bestätigen Sie, dass Flowise eingeschaltet ist. Es sollte so aussehen.

![image]((notion-hosted file))
- Einen gültigen Gemini-API-Schlüssel, der im Flowise-Credentials-Manager gespeichert ist (als aktiv bestätigt; wenn Sie prüfen müssen, gehen Sie in Flowise zu Credentials und sehen Sie nach, ob der Google-Gemini-Schlüssel dort vorhanden ist)
- Die Datei aaa-c3a-baseline.json, heruntergeladen auf Ihren lokalen Rechner
Wenn Ihr Gemini-Schlüssel rot oder inaktiv angezeigt wird, geben Sie ihn unter Settings → Credentials → Add Credential → Google Generative AI erneut ein. Geben Sie Ihren Credential-Namen und den Google AI API Key ein, der aus Ihrem Konto kopiert wurde. Der Schlüssel aus dem vorherigen Kurs funktioniert hier. Es ist kein neuer Schlüssel erforderlich.
![image]((notion-hosted file))

## Schritt 1: Die Baseline-Canvas importieren
Öffne Flowise in Ihrem Browser. Gehen Sie im Hauptdashboard zu den Einstellungen und wähle Load Agents.
![image]((notion-hosted file))
Wähle aaa-c3a-baseline.json von deinem lokalen Rechner aus. Flowise öffnet deinen Agentflow V2.
Du solltest drei Nodes auf der Canvas sehen:
- Start-Node links
- Agent-Node in der Mitte
- Direct-Reply-Node rechts
Warum diese Canvas der Ausgangspunkt ist und keine leere Canvas: Die Baseline steht für den minimal tragfähigen Agenten. Sie läuft, sie führt Reasoning aus, und sie hat zwei Flow-State-Schlüssel deklariert. Alles, was Sie darauf aufbauen, fügt architektonische Absicht hinzu. Hier zu beginnen bedeutet, dass Sie entwerfen, nicht nur bauen.
## Schritt 2: Die Baseline lesen, bevor Sie etwas ändern
Bevor du eine Konfiguration vornimmst, nimm die zwei Minuten Zeit, um die Canvas in deinem aktuellen Zustand zu lesen. Klicke jeden Node an und notiere, was bereits konfiguriert ist.
Start-Node: Was du beobachten solltest
- Eingabetyp: chatInput
- Deklarierte Flow-State-Schlüssel: query_type (leerer String) und status_response (leerer String)
- Ephemeral Memory: aus
Diese beiden Flow-State-Schlüssel sind leer. Sie existieren, um das Zustandsschema sichtbar zu machen. Jeder Node, der später in sie schreibt, schreibt in eine deklarierte, bekannte Struktur. Wenn du während des Walkthroughs neue Schlüssel hinzufügen, bedeutet das, sie zuerst hier zu deklarieren.
![image]((notion-hosted file))
Agent-Node: Was du beobachten sollten
- Modell: Ihr gewähltes Modell
- Memory: aktiviert, allMessages
- System-Prompt: der Vela-Systems-Platzhalter
- Document Store: keiner verbunden
- Tools: keine verbunden
![image]((notion-hosted file))
Direct-Reply-Node: Was du beobachten solltest
- Ausgabe: {{ agentAgentflow_0 }}
Das ist eine direkte Referenz auf die Ausgabe des Agent-Node. Was immer der Agent-Node erzeugt, wird zur Antwort.
![image]((notion-hosted file))
Die Architekturbeobachtung: Diese Canvas hat Orchestrierung (linear, ein Pfad), Kommunikation (direkte Ausgabereferenz, noch keine Flow-State-Schreibvorgänge) und Zustandsverwaltung (Memory standardmäßig aktiviert, zwei deklarierte, aber leere Flow-State-Schlüssel). Alle drei Pfeiler existieren, keiner wurde bewusst entworfen. Das ändert sich in den nächsten Schritten.
## Schritt 3: Die Baseline ausführen, um zu verstehen, womit du arbeitest
Bevor du umgestaltest, verstehe, was die Baseline tatsächlich tut. Öffne das Chat-Panel (das Sprechblasen-Symbol oben rechts auf der Canvas).
Sende diese zwei Nachrichten und notiere die Antworten:
Testanfrage 1: What is the current stock level for supplier K-Nord?
- PRÜFEN: Bestätige, dass der Agent-Node ungefähr so antwortet: „I don't have access to live stock data for Vela's suppliers. For current stock levels, I'd suggest checking the inventory management system directly or contacting the operations team." Der genaue Wortlaut wird variieren. Wichtig ist, dass die Antwort im Scope bleibt, ehrlich mit den Grenzen des Agenten umgeht und keine Bestandszahl erfindet.
Testanfrage 2: Can you draft a performance review for Jonas?
- PRÜFEN: Bestätige, dass der Agent-Node ungefähr so antwortet: „That's outside what I'm set up to help with. Performance reviews would be handled through Vela's HR process. I'd suggest contacting the HR team or your line manager directly." Der genaue Wortlaut wird variieren. Wichtig ist eine klare Out-of-Scope-Antwort, die den Nutzer an eine andere Stelle verweist, ohne unhilfreich abzulehnen.
Was dieser Schritt zeigt: Der Baseline-Agent verhält sich bereits vernünftig. Geminis Grund-Reasoning hält ihn grob im Scope. Aber „grob im Scope" ist keine Designentscheidung. Der System-Prompt muss diese Grenzen explizit und bewusst machen.
### Schritt 4: Den Scope des Agenten schriftlich definieren, bevor du die Canvas anfasst
Dieser Schritt hat keine Klicks. Er ist ein Designschritt und der wichtigste Schritt in diesem Walkthrough.
Bevor du den System-Prompt verfeinerst, schreib (auf Papier oder in einem Dokument) die Antworten auf vier Fragen auf:
1. Welche Eingaben wird dieser Agent erhalten?
- Für Velas Baseline-Agent: natürlichsprachliche Fragen auf Englisch oder Niederländisch von internen Operations-Teammitgliedern zu Bestandsstatus, Fulfilment-Koordination und Lieferantenkommunikation.
2. Welche Ausgaben wird dieser Agent erzeugen?
- Für Velas Baseline-Agent: Antworten in einfacher Sprache, die die Frage innerhalb des Scope beantworten, oder eine klare Weiterleitung mit vorgeschlagenem Kontakt, wenn die Frage außerhalb des Scope liegt. Keine erfundenen Daten. Keine externen Aktionen.
3. Wofür ist dieser Agent verantwortlich?
- Für Velas Baseline-Agent: Operative Anfragen beantworten, die mit dem eingebauten Wissen des Agenten und den Informationen in der Anfrage selbst beantwortet werden können. Er ist nicht verantwortlich für Live-Datenabruf, Dokumentenerstellung oder Entscheidungsfindung im Namen von Nutzern.
4. Was wird dieser Agent bewusst nicht tun?
- Für Velas Baseline-Agent: Er wird keine Live-Bestandsstände abrufen (noch keine Tool-Verbindung), keine Dokumente entwerfen (Performance Reviews, Verträge, Vorschläge), keine Zusagen im Namen von Vela oder seinen Kunden machen und keine Anfragen zu HR-, Finanz- oder Rechtsthemen beantworten.
Schreib diese vier Antworten auf. Sie werden zur Architekturdokumentation für diesen Agenten: das Briefing, das ein neues Teammitglied lesen könnte, um zu verstehen, wofür die Canvas da ist, ohne Flowise zu öffnen.

>  
  ### 🔥 AI nutzen, um deine Scope-Definition zu stress-testen
  Sobald du deine vier Antworten geschrieben hast, füg sie in einen AI-Assistenten ein und frag:
  > „Given this scope definition for an internal agent, what types of user queries are most likely to fall into an ambiguous grey area where the agent might try to answer but should not, or where it might refuse but could reasonably help?"
  Nutze die Antwort der AI, um deine Scope-Definition zu verfeinern, insbesondere deine Antwort auf Frage 4. Graubereiche, die nicht benannt werden, sind Graubereiche, die der System-Prompt nicht explizit behandeln kann.

## Schritt 5: Den System-Prompt verfeinern
Öffne den Agent-Node. Ersetze im Feld System Prompt den Platzhaltertext durch eine verfeinerte Version, die die Scope-Definition aus Schritt 4 widerspiegelt.
Hier ist der verfeinerte Prompt für Velas Baseline-Agent:
```plain text
You are an internal operations assistant for Vela Systems.

You help members of the operations team answer questions about inventory
coordination, fulfilment processes, and supplier communications.

What you can help with:
- Questions about how inventory or fulfilment processes work at Vela
- Clarifying supplier communication procedures
- General operational queries that can be answered from what you know

What you do not do:
- Retrieve live stock levels or real-time data (you do not have tool access)
- Draft documents such as contracts, proposals, or performance reviews
- Make commitments or decisions on behalf of Vela or its clients
- Answer questions about HR, finance, or legal matters

If a question is outside this scope, say so clearly and suggest who the
person should contact instead. Do not fabricate answers for out-of-scope
questions. Do not attempt to answer questions about topics you are not
equipped to handle.

Respond in the same language the user writes in. Keep responses clear
and direct; one to three sentences for simple queries, more detail
only when the question genuinely needs it.
```
![image]((notion-hosted file))
Warum dieser Prompt besser ist als der Platzhalter: Er benennt den Scope positiv (wobei der Agent helfen kann) und negativ (was er nicht tut). Er gibt explizite Anweisungen für Out-of-Scope-Anfragen. Er legt eine Erwartung an die Antwortlänge fest. Jede Zeile spiegelt eine Entscheidung aus Schritt 4 wider, nichts im Prompt steht dort standardmäßig.
### Schritt 6: Den Scope in Flow State deklarieren
Die zwei vorab deklarierten Flow-State-Schlüssel (query_type und status_response) sind derzeit leer. Dieser Walkthrough implementiert keine Routing-Logik, aber er etabliert das Zustandsschema, das Routing später verwenden wird.
Öffne den Start-Node. Füg einen dritten Flow-State-Schlüssel hinzu:
[TABLE]
  | Schlüssel | Standardwert | Zweck |
  | query_type | "" | Will hold the classified query type when routing is added in Sprint 2 |
  | status_response | "" | Will hold a status message for the direct reply path |
  | agent_scope | "vela_operations" | Documents which agent scope applies to this execution. Useful for observability when multiple flows are running |
![image]((notion-hosted file))
Warum agent_scope jetzt hinzufügen? Dieser Schlüssel beeinflusst das Verhalten des Agenten noch nicht. Er existiert, um die Architektur lesbar zu machen, und jede Person, die den Ausführungs-Trace des Flows prüft, kann sehen, welche Agentenkonfiguration während dieses Durchlaufs aktiv war. Das ist eine kleine Observability-Entscheidung ohne Performance-Kosten.
### Schritt 7: Den verfeinerten Agenten testen
Speicher den Agentflow V2. Kehr zum Chat-Panel zurück. Sende dieselben zwei Testanfragen aus Schritt 3 plus eine dritte.
Testanfrage 1 (wiederholen): What is the current stock level for supplier K-Nord?
- PRÜFEN: Der verfeinerte Agent sollte jetzt präziser antworten. Er sollte klar benennen, dass er keinen Zugriff auf Live-Daten hat, nicht nur, dass er „doesn't have access to live stock data" hat. Die Antwort sollte bewusster wirken als die generische Antwort der Baseline.
Testanfrage 2 (wiederholen): Can you draft a performance review for Jonas?
- PRÜFEN: Der verfeinerte Agent sollte jetzt HR als die richtige Anlaufstelle benennen, konsistent mit dem Ausschluss von „HR, finance, or legal matters" im System-Prompt.
Testanfrage 3 (neu): How does Vela's process work when a supplier misses a delivery window?
- PRÜFEN: Dies ist eine legitime In-Scope-Anfrage. Eine Frage zum Fulfilment-Prozess, nicht zum Live-Datenabruf. Der Agent sollte auf Basis des allgemeinen Wissens im Modell eine vernünftige Antwort versuchen, und er sollte nicht ablehnen oder weiterleiten. Die Antwort muss nicht faktisch spezifisch für Velas tatsächlichen Prozess sein, der Agent hat noch keinen Zugriff auf interne Dokumentation. Wichtig ist, dass er mit dem Anfragetyp korrekt umgeht, statt auszuweichen.
Wie ein gutes Ergebnis aussieht: Der Agent verhält sich konsistent mit der Scope-Definition aus Schritt 4. In-Scope-Anfragen erhalten einen echten Antwortversuch. Out-of-Scope-Anfragen erhalten eine klare Weiterleitung mit benannter Anlaufstelle. Die Formulierung spiegelt die Anweisungen des Prompts wider.
### Schritt 8: Die Architektur dokumentieren
Der letzte Schritt dieses Walkthroughs ist Dokumentation, nicht Konfiguration. Öffne ein Textdokument: Das kann eine einfache Notizdatei, ein geteiltes Dokument oder das Beschreibungsfeld der Flowise-Canvas sein.
Schreib die folgende Architekturzusammenfassung für Velas Single-Agent-System:
Agentenname: Vela Systems Operations Assistant v1
Architekturmuster: Single-Agent (bewusste Entscheidung: Scope ist eng und stabil, keine Konflikte bei Spezialwissen, Fehlerisolierung in diesem Maßstab nicht erforderlich, Koordinationsaufwand würde den Zuverlässigkeitsvorteil übersteigen)
Eingaben:
- Natürlichsprachliche operative Anfragen auf Englisch oder Niederländisch
- Quelle: interne Vela-Operations-Teammitglieder über die Chat-Oberfläche
- Out-of-Scope-Eingaben: HR-Anfragen, Finanzanfragen, Rechtsanfragen, Anfragen nach Live-Daten, Anfragen nach Dokumentenerstellung
Ausgaben:
- Antworten in einfacher Sprache innerhalb des Scope (1–3 Sätze bei einfachen Anfragen)
- Klare Weiterleitungen mit benannten Anlaufstellen für Out-of-Scope-Anfragen
- Keine erfundenen Daten, keine externen Aktionen, keine Zusagen
Orchestrierung: Linear: Start → Agent → Direct Reply. Keine Branches, keine Schleifen. Angemessen für einheitliche Anfragebearbeitung im aktuellen Maßstab.
Kommunikation: Direkte Ausgabereferenz (Ausgabe des Agent-Node fließt direkt zum Direct-Reply-Node). Die Flow-State-Schlüssel query_type und status_response sind für zukünftige Routing-Nutzung deklariert. Der Schlüssel agent_scope dokumentiert den aktiven Scope pro Ausführung.
Zustandsverwaltung: Memory aktiviert mit allMessages. Angemessen für kurze, fokussierte Sessions. Risiko: Context Bleed in langen Sessions mit mehreren nicht zusammenhängenden Anfragen. Erneut prüfen, wenn die Session-Länge deutlich zunimmt.
Bewusste Ausschlüsse:
- Keine Tool-Verbindungen (kein Live-Datenzugriff, auf einen späteren Sprint verschoben, falls der Scope wächst)
- Keine Document-Store-Verbindung (kein Retrieval, verschoben)
- Keine Routing-Logik (ein Agent bearbeitet alle In-Scope-Anfragen, begründet durch den aktuellen Scope)
Dieses Dokument ist das Architekturentscheidungs-Briefing für Velas Single-Agent-System. Es zeigt, wie das Karmen-Freight-Briefing in der nächsten Lektion aussehen sollte, angewendet auf eine andere Organisation und ein anderes Problem.
### Was du gebaut hast
Ein Single-Agent-System, das entworfen und nicht nur konfiguriert ist. Die Canvas hat drei Nodes, aber der System-Prompt spiegelt jetzt eine bewusste Scope-Entscheidung wider, das Flow-State-Schema ist dokumentiert statt standardmäßig leer, und die Architekturentscheidungen sind festgehalten statt implizit.
Der Agent ist vorhersehbarer, lesbarer und besser wartbar als die Baseline. Wenn Jonas in einem zukünftigen Sprint den Scope ändern muss, kann er die Dokumentation lesen und verstehen, was sich ändert und warum, statt einen System-Prompt zu lesen und die Absicht dahinter zu erraten.
### Zusammenfassung
Beim Entwerfen eines Single-Agent-Systems zählt vor allem die Dokumentation: Die Scope-Definition und die bewussten Entscheidungen sind das eigentliche Design, die Canvas ist nur die Ausgabe davon. Dieser Walkthrough hat beides hervorgebracht: eine verfeinerte Agentflow-V2-Canvas und ein Architektur-Briefing mit vier Abschnitten, das einem neuen Teammitglied ohne Erklärung übergeben werden könnte.
In der nächsten Lektion erstellst du dasselbe Briefing für Karmen Freight, einen Logistikmakler in Wien, anhand eines Szenarios, das du noch nicht kennst. Das Framework ist dasselbe. Der Kontext ist neu.