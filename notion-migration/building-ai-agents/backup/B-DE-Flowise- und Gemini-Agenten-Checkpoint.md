# Flowise- und Gemini-Agenten-Checkpoint

Notion page: https://app.notion.com/p/Flowise-und-Gemini-Agenten-Checkpoint-3789418319f38062ad29f4755eae397a
Backed up before n8n migration

> 💡 Was dieses Assessment abdeckt: Dieses Assessment validiert deine Fähigkeit, einen funktionierenden Flowise- und Gemini-Agenten zu konfigurieren, seinen Zweck und seine Grenzen klar zu definieren und zu zeigen, dass er sich sowohl unter Standardbedingungen als auch unter adversarialen Bedingungen wie beabsichtigt verhält. Alle drei Aufgaben sind erforderlich.

> 🔥 Bevor du beginnst, erstelle eine Kopie dieser Google-Sheets-Vorlage. Drei Tabs entsprechen den Aufgaben 1 und 2: Agentenspezifikation, Canvas + Gesprächsprotokoll und Verhaltensbewertung. Das Wissensquiz (Aufgabe 3) wird auf der Plattform abgeschlossen, nicht in der Vorlage.

## Kontext
Während dieses Sprints hat sich das Entwicklungsteam von Meridian Consulting vom Infrastruktur-Setup bis zu einem funktionierenden, eingeschränkten Agenten vorgearbeitet. Die Umgebung wurde überprüft, der Stack wurde verstanden, der Baseline-Agent wurde gebaut, und der System-Prompt wurde gegen grenzüberschreitende Szenarien getestet.
Dieser Checkpoint fordert dich auf, diese Elemente zu einer einzigen kohärenten Abgabe zusammenzuführen. Der Agent, den du erstellst, ist die Grundlage, auf der Retrieval, Memory, Tools und Plattformvergleichsarbeit in den kommenden Sprints aufgebaut werden. Es ist wichtig, ihn jetzt korrekt hinzubekommen.

## Aufgabe 1: System-Prompt und Agentendokumentation
Bevor du deinen Agenten einreichst, dokumentiere sein beabsichtigtes Design schriftlich. Diese Dokumentation erfüllt zwei Zwecke: Sie erzwingt Klarheit darüber, was der Agent tun soll, und sie bietet einen Bezugspunkt, um zu bewerten, ob das tatsächliche Verhalten des Agenten der Absicht entspricht.
Schreibe eine kurze Agentenspezifikation, die die folgenden drei Abschnitte abdeckt.
- Rolle und Persona: Beschreibe, wer der Agent ist, wem er dient und wie er kommuniziert. Sei spezifisch genug, dass jemand, der mit dem Projekt nicht vertraut ist, diesen Abschnitt lesen und die Identität und den Ton des Agenten verstehen könnte, ohne den System-Prompt selbst sehen zu müssen.
- Scope: Liste die spezifischen Aufgaben und Themenbereiche auf, die der Agent bearbeiten darf. Nenne die Kategorien von Anfragen, auf die der Agent eingehen sollte, und, wo relevant, die Kategorien, auf die er nicht eingehen sollte.
- Grenzen und Eskalation: Beschreibe, was der Agent tut, wenn eine Anfrage außerhalb seines definierten Scopes liegt. Lege das Eskalationsverhalten fest. Leitet er an einen menschlichen Kollegen weiter, erklärt er die Grenze und stoppt, oder stellt er eine Klärungsfrage? Erkläre, warum du dieses Verhalten für den Meridians Kontext gewählt hast.

## Aufgabe 2: Flowise-Canvas-Einreichung und Testbericht
### Teil A: Canvas-Screenshot
Zu diesem Zeitpunkt muss dein Canvas alle folgenden Komponenten korrekt verbunden zeigen:
- Einen Start Node als Einstiegspunkt des Flows
- Ein Agent-Node, der mit deinem API-Key authentifiziert ist, für die Nutzung deines KI-Modells konfiguriert wurde und deinen eigenen System Prompt im Feld „System Prompt“ enthält.
- Einen Direct Reply Node, der mit dem Output des Agent Nodes verbunden ist
- Alle drei Nodes durch sichtbare Edges verbunden, die einen durchgehenden Ausführungspfad bilden: Start Node → Agent Node → Direct Reply Node

### Teil B: Testbericht
Führe in der Flowise-Chat-Oberfläche ein Multi-Turn-Gespräch aus, das die folgenden drei Verhaltensweisen in einer einzigen durchgehenden Session mit mindestens sieben Austauschen zeigt, wobei mindestens zwei Turns jeder der drei Verhaltenstests gewidmet sind:
- Kontextbeibehaltung: Etabliere früh im Gespräch eine spezifische Information, etwa einen Namen oder Account, und bestätige, dass der Agent sie in einem späteren Turn innerhalb derselben Session korrekt referenziert, ohne erneut dazu aufgefordert zu werden. Dies testet, ob der Agent Node den Session-Kontext korrekt beibehält.
- Scope-Durchsetzung: Reiche eine Anfrage ein, die klar außerhalb des definierten Scopes des Agenten liegt, und bestätige, dass der Agent sie entsprechend dem Eskalationsverhalten behandelt, das in deiner Spezifikation beschrieben ist.
- Grenzbeobachtung: Versuche eine Prompt Injection, indem du den Agenten anweist, seinen System-Prompt zu ignorieren oder eine neue Identität anzunehmen. Dokumentiere genau, was du gesendet hast und was der Agent geantwortet hat. Unabhängig davon, ob der Agent widersteht oder nachgibt, schreibe zwei bis drei Sätze, in denen du erklärst, warum du glaubst, dass dieses Ergebnis eingetreten ist.

Führe die Session als ein einziges durchgehendes Gespräch mit mindestens sieben Austauschen aus, mit genug Raum, um Kontext für den Test zur Kontextbeibehaltung aufzubauen, die Out-of-Scope-Anfrage einzureichen und zu bewerten sowie die Grenzbeobachtung mit einem Follow-up-Turn durchzuführen.
Schreibe eine kurze Bewertung, die alle drei Verhaltensweisen abdeckt. Notiere für jede, ob der Agent sich wie beabsichtigt verhalten hat, und identifiziere jede Lücke zwischen dem beabsichtigten Verhalten, das in deiner Spezifikation beschrieben ist, und dem tatsächlich beobachteten Verhalten. Wenn der Agent einen Test nicht bestanden hat, beschreibe die konkrete Prompt-Überarbeitung, die du daraufhin vorgenommen hast, und ob sie den Fehler behoben hat.
Ein dokumentierter Fehler mit anschließender begründeter Überarbeitung ist in dieser Phase ein gültiges und didaktisch wertvolles Ergebnis. Die Bewertung prüft deine Fähigkeit, das Verhalten des Agenten zu diagnostizieren und zu verbessern, nicht nur, ob der Agent jeden Test beim ersten Versuch bestanden hat.

## Aufgabe 3: Wissensquiz
Beantworte unten alle vier Fragen. Lies jede Option sorgfältig, bevor du deine Antwort auswählst.
### Frage 1
>  Der Agent von Meridian läuft während eines geschäftigen Vormittags im kostenlosen Kontingent der Gemini API, während mehrere Berater ihn gleichzeitig abfragen. Der Agent beginnt mitten im Gespräch zu scheitern, ohne sichtbaren Fehler im Flowise-Canvas. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/fdf8bee4-ccfd-488d-ace0-979cda7f64e9

### Frage 2
>  Ein Meridian-Berater versucht, die Identität des Agenten mitten im Gespräch zu überschreiben, indem er ihn anweist, seinen System-Prompt zu ignorieren. Der Agent kommt dem nach und beginnt, sich wie ein allgemeiner Assistent zu verhalten. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/667dd559-beb8-4036-8051-31b82b9ac60e

### Frage 3
>  In einem Agentflow v2 fügt ein Meridian-Entwickler einen Condition Node zum Canvas hinzu, um Anfragen auf unterschiedliche Pfade zu routen, vergisst aber, eine Edge vom Agent Node zum Condition Node zu zeichnen. Der Flow wird gespeichert und getestet. Was passiert zur Laufzeit?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/804d931d-b428-492c-98a2-cdcb69a1c3c1

### Frage 4
>  Welche zwei Praktiken bilden zusammen die minimale Sicherheitsbaseline für den Umgang mit einem Gemini API-Key bei der Verwendung von Flowise?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cc55e01c-d5b4-45e4-9af5-1f6e175bcac0

> 💡 Takeaway: 
  Der hier konfigurierte Agentflow v2 (Start Node, Agent Node, Direct Reply Node) ist die Grundlage, auf der Retrieval, Conditional Routing, Tools und Orchestrierungslogik in den kommenden Sprints aufgebaut werden.
