# Context-Window-Management

Notion page: https://app.notion.com/p/Context-Window-Management-3779418319f380b8b427c33444001093
Backed up before n8n migration

> 💡 In dieser Lektion evaluierst du zwei unterschiedliche Strategien für das Kontextmanagement eines Business-Agenten. Auf Basis deiner Überlegungen entwirfst du einen konkreten Ansatz und implementierst diesen anschließend direkt in deinen Chatflow, indem du einen Buffer-Window-Memory-Node konfigurierst.

## Was passiert
Der Support-Agent der Contigo GmbH behält jetzt den Gesprächsverlauf und isoliert Sessions korrekt. Beim Testen ist jedoch ein neues Problem aufgetreten.
Während langer Troubleshooting-Gespräche verschlechtert sich die Leistung des Agenten nach fünfzehn oder zwanzig Austauschen spürbar. In manchen Fällen beginnt er, Anweisungen zu widersprechen, die ihm früher im Gespräch gegeben wurden. In anderen Fällen scheitert er bei einem späten Turn vollständig, sodass der Kunde von vorn anfangen muss.
Die Ursache dafür liegt im sogenannten Context Window (Kontextfenster). Jede neue Nachricht im Chat-Verlauf verlängert den Prompt. Irgendwann wird dieser so umfassend, dass das Modell ihn nicht mehr zuverlässig verarbeiten kann. Schon lange vor dem eigentlichen Token-Limit lässt die Konzentration des Modells spürbar nach: Der Agent verliert den Überblick über frühere Inhalte und priorisiert aktuelle Nachrichten auf Kosten des wichtigen Kontexts, der zu Beginn der Session aufgebaut wurde.
Das Team der Contigo GmbH benötigt eine klare Strategie, um das Verhalten des Agenten gezielt zu steuern, bevor dieser in den Live-Betrieb geht. Deine Aufgabe ist es nun, die verschiedenen Optionen sorgfältig abzuwägen, eine fundierte Designentscheidung zu treffen und diese direkt in deinem Chatflow umzusetzen.

## Die zwei Hauptansätze
Du kennst jetzt zwei Kontextmanagement-Strategien, die Flowise dir anbietet. Bevor du dich entscheidest, muss klar sein, was jede Strategie tut und welche Kosten sie verursacht.
1. Buffer Window Memory - Sliding-Window-Trunkierung:
Dieser Node behält nur die letzten K Nachrichten im aktiven Kontext und verwirft alles Ältere.
Er ist einfach zu konfigurieren und verursacht keinen zusätzlichen Overhead. Zudem garantiert er, dass der Prompt nie eine definierte Größe überschreitet. Der Trade-off ist grob: Ältere Inhalte werden vollständig verworfen, unabhängig davon, ob sie wichtig waren. Diesen Node wirst du in dieser Lektion konfigurieren.
1. Conversation Summary Memory - Kompression über einen sekundären Modellaufruf:
Dieser Node verwendet das Sprachmodell, um ältere Teile des Gesprächs fortlaufend zusammenzufassen, während neue Nachrichten eintreffen.
Die Zusammenfassung ersetzt den Rohdialog und bewahrt die allgemeine Bedeutung, ohne den vollständigen ausführlichen Austausch zu behalten.
Der Trade-off sind Kosten und Latenz. Jeder Zusammenfassungsschritt braucht einen zusätzlichen Modellaufruf. Die Zusammenfassung ist zudem nur eine Annäherung, bei der Kompression können Details verloren gehen. Diese Option wird in der nächsten Lektion als Best-Practice-Überlegung behandelt.
![image]((notion-hosted file))
## Deine Aufgaben
### Teil A: Die Strategien evaluieren
Lies die folgenden zwei Szenarien und beantworte die Fragen zu jedem. Schreibe sie auf, damit du deine Antworten später analysieren kannst.

Szenario 1: Prüfung eines Kreditantrags
- Ein Contigo-Kreditsachbearbeiter verwendet den Agenten, um einen komplexen Antrag durchzugehen. In den ersten drei Nachrichten gibt der Kunde seine Einkommenszahlen, seine Beschäftigungshistorie und die gewünschte Kreditsumme an. Das Gespräch läuft anschließend über zwanzig weitere Austausche zu Kriterien für die Kreditwürdigkeit und Dokumentenanforderungen.
- Wenn ein striktes Sliding Window der letzten sechs Nachrichten angewendet wird, welche kritischen Informationen laufen Gefahr, verloren zu gehen? Was ist die Konsequenz für die Fähigkeit des Agenten, die Aufgabe abzuschließen?

Szenario 2: Allgemeine Kontoanfrage
- Ein Kunde kontaktiert Contigo, um seine Kontaktdaten zu aktualisieren und eine Frage zu seinem aktuellen Zinssatz zu stellen. Das Gespräch ist kurz und keine der frühen Nachrichten enthält Informationen, die später benötigt werden.
- Ist für diese Art von Gespräch ein Sliding Window ausreichend? Welche Fenstergröße wäre angemessen, und warum?
- Checkpoints: Nutze diese Orientierungspunkte auf dem Weg zur richtigen Lösung
  Checkpoint 1: Die Kosten der Trunkierung. Überlege, was das Modell nach der Trunkierung sehen kann und was nicht. Es hat keine Möglichkeit zu markieren, dass früherer Kontext fehlt. Es argumentiert einfach auf Basis dessen, was es hat. Überlege, was im Szenario des Kreditantrags passiert, wenn die Einkommenszahlen aus Turn 1 bei Turn 20 nicht mehr im aktiven Fenster liegen.
  Checkpoint 2: Das Fenster auf den Use Case abstimmen. Ein zu kleines Fenster verwirft wichtigen Kontext zu früh. Ein zu großes Fenster verfehlt den Zweck des Kontextmanagements insgesamt. Denk an die typische Länge eines Contigo-Supportgesprächs. Wie viele aktuelle Nachrichten braucht es mindestens, um den Gesprächsfaden nicht zu verlieren?
  Checkpoint 3: Was niemals verworfen werden sollte. Einige Informationen, die früh in einer Session etabliert werden, sind für das gesamte Gespräch kritisch. Fallreferenzen, Kontoidentifikatoren und angegebene Präferenzen sind Beispiele. Überlege, ob ein reiner Fensteransatz diese Informationen schützen kann oder ob sie anders behandelt werden müssen.

### Teil B: Buffer Window Memory in deinem Chatflow implementieren
Auf Grundlage deiner Überlegungen aus Teil A ersetzt du nun den Buffer-Memory-Node in deinem Chatflow durch einen Buffer-Window-Memory-Node und konfigurierst ihn mit einer Fenstergröße, die deiner Designentscheidung entspricht.

### Schritt 1: Deinen bestehenden Chatflow öffnen
Öffne über dein Flowise-Cloud-Dashboard den Chatflow, an dem du gearbeitet hast. Du solltest die Conversation Chain, Google Gemini und Buffer Memory Nodes auf dem Canvas sehen.

### Schritt 2: Den Buffer-Memory-Node entfernen
Klicke auf den Buffer-Memory-Node und lösche ihn vom Canvas. Im nächsten Schritt ersetzt du ihn durch einen Buffer-Window-Memory-Node.

### Schritt 3: Einen Buffer-Window-Memory-Node hinzufügen
Klicke auf (+), um das Node-Panel zu öffnen. Suche unter dem Tab LangChain nach Buffer Window Memory und ziehe ihn auf den Canvas.

### Schritt 4: Den Node verbinden
Verbinde den Output des Buffer-Window-Memory-Nodes mit dem Memory-Eingabe-Socket der Conversation Chain, genau wie du es zuvor mit dem Buffer-Memory-Node getan hast.

### Schritt 5: Den Node konfigurieren
Öffne die Einstellungen des Buffer-Window-Memory-Nodes und konfiguriere Folgendes:
- Size: Gib die Fenstergröße ein, für die du dich in Teil A entschieden hast. Der Standardwert ist 4 (letzte 4 Nachrichten). Passe ihn auf Grundlage deiner Überlegungen zur typischen Gesprächslänge bei Contigo an.
- Session ID: Gib dieselbe Session ID ein, die du zuvor konfiguriert hast (client_001), um Konsistenz mit deinem früheren Testsetup beizubehalten.
- Memory Key: Lass dies auf dem Standardwert (chat_history).
![image]((notion-hosted file))
> ➡️ Warum ist das wichtig: Der Size-Parameter ist das Herzstück dieser Nodes. Er definiert exakt, wie viele der letzten Nachrichtenpaare der Agent bei einer Gesprächsrunde im Blick behält. Jede Nachricht, die außerhalb dieses Fensters liegt, fällt automatisch aus dem aktiven Kontext heraus. Diese Zahl bewusst festzulegen, anstatt sich auf den Standardwert zu verlassen, entscheidet letztlich darüber, ob die Konfiguration optimal für deinen spezifischen Anwendungsfall funktioniert oder unter realistischen Praxisbedingungen scheitert.
![image]((notion-hosted file))

### Schritt 6: Speichern und testen
Speichere deinen Chatflow und öffne die integrierte Chat-Oberfläche. Führe folgenden Test aus. So prüfst du, ob das Fenster wie konfiguriert funktioniert.
Sende nacheinander mindestens vier Nachrichten ab, die jeweils eine neue Information enthalten – orientiere dich dabei gerne an folgenden Beispielen:
- Turn 1: „Mein Name ist Markus und meine Fallreferenz ist CG-4821.“
- Turn 2: „Ich rufe wegen einer Anfrage zur Kreditrestrukturierung an.“
- Turn 3: „Meine bevorzugte Kontaktsprache ist Englisch.“
- Turn 4: „Ich bin seit sechs Jahren Contigo-Kunde.“
- Turn 5: „Wie lautet meine Fallreferenz?“

### Worauf du achten solltest
Wenn deine Fenstergröße auf 4 gesetzt ist, sollte Turn 1 noch innerhalb des aktiven Fensters liegen, wenn Turn 5 gesendet wird, und der Agent sollte CG-4821 korrekt abrufen.
Wenn dein Fenster kleiner eingestellt ist, liegt Turn 1 möglicherweise bereits außerhalb des Fensters und der Agent kann ihn nicht mehr abrufen.
Beobachte das Ergebnis und vergleiche es mit deiner Designentscheidung aus Teil A. Erzeugt deine gewählte Fenstergröße das Verhalten, das du beabsichtigt hast?

## Teste dein Verständnis
### Frage 1
>  Ein Kunde fügt ein 3.000 Wörter langes Rechtsdokument in den Contigo-Agentenchat ein, um es zusammenfassen und mit Richtlinien abgleichen zu lassen. Welcher Umgang damit ist architektonisch am passendsten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/773365c6-1c21-43c9-bc81-053921f21463

### Frage 2
>  Welche Kategorie von Informationen sollte in einem Contigo-Finanzdienstleistungsagenten unabhängig von der Gesprächslänge niemals aus dem aktiven Context Window fallen?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e0fae8ad-f0c8-412c-bc82-0be11cda56cd

> 💡 Takeaway: 
  Das Kontextmanagement ist eine grundlegende Designentscheidung. Die von dir gewählte Fenstergröße bestimmt direkt, woran sich der Agent zu jedem Zeitpunkt des Gesprächs erinnern kann. Diese Parameter exakt auf deinen spezifischen Anwendungsfall abzustimmen, bevor der Agent in den Live-Betrieb geht, ist entscheidend: Es macht den Unterschied zwischen einer Konfiguration, die echten Praxisbedingungen standhält, und einer, die genau im kritischsten Moment unbemerkt versagt.
