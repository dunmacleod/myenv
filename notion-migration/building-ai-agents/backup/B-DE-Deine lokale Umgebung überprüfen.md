# Deine lokale Umgebung überprüfen

Notion page: https://app.notion.com/p/Deine-lokale-Umgebung-berpr-fen-3789418319f38080a767f0b162a255e8
Backed up before n8n migration

>  Diese Lektion verwendet Gemini als Hauptbeispiel, aber die zugrunde liegende Logik der API-Nutzung lässt sich auch auf andere KI-Modelle und Anbieter übertragen. Konzentriere dich auf die Prinzipien: Anfragen klar strukturieren, Antworten zuverlässig verarbeiten, Fehler handhaben und Workflows so gestalten, dass sie an verschiedene Modell-APIs angepasst werden können.
> 💡 Woran du in dieser Lektion arbeiten wirst: Du überprüfst selbstständig, ob deine lokale Flowise-Umgebung korrekt läuft und ob dein Gemini-API-Key fehlerfrei authentifiziert wird, bevor das Bauen beginnt.

## Warum die Überprüfung vor dem Bauen kommt
Das Entwicklungsteam von Meridian Consulting hat Flowise installiert, seinen API-Key generiert und ihn im Credentials Manager gespeichert. Die Versuchung an diesem Punkt ist, den Canvas zu öffnen und mit dem Verbinden von Nodes zu beginnen. Dieser Versuchung solltest du widerstehen.
Eine defekte Umgebung mitten im Build stört deutlich mehr als ein Fehler, den du vor dem ersten Node entdeckst. Konfigurationsfehler, Credential-Probleme und ungültige API-Keys erzeugen Symptome, die wie Probleme der Agentenlogik aussehen, obwohl sie reine Setup-Fehler sind. Prüfe die Umgebung zuerst. Das beseitigt diese Verwirrung komplett.

Deine Aufgabe ist es, zwei Dinge zu bestätigen:
- Deine lokale Flowise-Instanz läuft und das Dashboard ist erreichbar
- Dein Gemini API-Key ist aktiv und authentifiziert sich korrekt innerhalb von Flowise

## Was dir gegeben wurde
Lokaler Flowise-Zugriff: Dein Flowise-Server sollte bereits aus der vorherigen Lektion laufen.
Falls er nicht läuft, prüfe Folgendes:
- Bestätige, dass Docker Desktop geöffnet ist und läuft. Achte auf das Wal-Symbol in deiner Systemleiste
- Öffne ein Terminal und führe docker ps aus, um zu bestätigen, dass der Flowise-Container als laufend aufgelistet ist.
- Wenn der Container nicht läuft, starte ihn mit docker start flowise
- Wenn der Container nicht existiert, führe den vollständigen docker run-Befehl aus der vorherigen Lektion erneut aus.

## Nützliche Referenzen:
- Flowise-Dokumentation und Troubleshooting: docs.flowiseai.com
- Flowise-GitHub-Repository und offene Issues: github.com/FlowiseAI/Flowise
- Google AI Studio für Key-Management: aistudio.google.com
- Gemini-API-Referenzdokumentation: ai.google.dev/api

## Deine Aufgaben
### Aufgabe A: Flowise von deinem Laptop aus aufrufen und überprüfen
Navigiere in deinem Browser zu http://localhost:3000. Bestätige, dass das Flowise-Dashboard lädt und dass du den linken Navigationsbereich sehen kannst. Klicke auf Agentflows und bestätige, dass sich der Bereich ohne Fehler öffnet.
Dokumentiere, was du beobachtest:
- Ob das Dashboard erfolgreich geladen wurde
- Ob der Agentflows-Bereich korrekt geöffnet wurde
- Welche Fehler dir begegnet sind
Fahre nicht mit Aufgabe B fort, bis das Flowise-Dashboard vollständig erreichbar ist.

### Aufgabe B: Den Gemini API-Key validieren
Baue einen minimalen Test-Canvas in Agentflow v2, um zu bestätigen, dass dein Credential funktioniert:
1. Klicke in der linken Navigation auf Agentflows und dann auf + Add New.
1. Auf dem Canvas siehst du bereits einen Start Node. Füge einen Agent Node und einen Direct Reply Node hinzu und verbinde sie der Reihe nach.
1. Doppelklicke in den Einstellungen des Agent Nodes und öffne den Bereich Model. Wähle Google Gemini aus und füge deine Credential-Details hinzu.
1. Setze das Modell auf das, was du gewählt hast**.** Wähle Save aus.
1. Klicke auf das Chat-Symbol und sende: Hello
Wenn der Agent antwortet, ist der Key aktiv und authentifiziert sich korrekt. Wenn er einen Fehler zurückgibt, nutze Folgendes zur Diagnose:
- 401-Fehler: Der Key ist ungültig, inaktiv oder wurde nicht korrekt kopiert.
- 429-Fehler: Das Rate Limit des kostenlosen Kontingents wurde überschritten; warte eine Minute und versuche es erneut.
- 403-Fehler: Der Key hat eine Einschränkung, die diese Art von Request blockiert; prüfe die Key-Einstellungen in Google AI Studio.
- Gar keine Antwort: Bestätige, dass alle drei Nodes durch sichtbare Kanten verbunden sind und der Canvas vor dem Testen gespeichert wurde.
Dokumentiere deine Testnachricht und die Antwort, die du erhalten hast. Wenn der Key einen Fehler zurückgibt, diagnostiziere und behebe ihn mithilfe der Fehlercode-Hinweise und Referenzen oben, bevor du zur nächsten Lektion übergehst.
![image]((notion-hosted file))

## Verständnis prüfen
>  Ein Meridian-Entwickler öffnet http://localhost:3000, und die Seite lädt nicht. Docker Desktop ist installiert. Was ist die wahrscheinlichste Ursache und der richtige erste Schritt?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/dae61ac1-4a5c-4f82-94e6-69e3f6b34e98

> 💡 Takeaway: 
  Die Überprüfung der Umgebung ist der erste echte Test deines Setups. Ein Agent, der wegen eines Infrastrukturproblems scheitert, sieht genauso aus wie einer, der wegen eines Logikproblems scheitert.
  Spüre Setup-Fehler auf, noch bevor du die erste Geschäftsregel auf das Canvas setzt. Das beschleunigt deine Fehlersuche im gesamten restlichen Kurs und hält dich fokussiert.
