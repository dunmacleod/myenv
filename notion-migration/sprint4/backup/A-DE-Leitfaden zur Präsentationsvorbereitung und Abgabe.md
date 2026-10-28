# Leitfaden zur Präsentationsvorbereitung und Abgabe

Notion page: https://app.notion.com/p/Leitfaden-zur-Pr-sentationsvorbereitung-und-Abgabe-3779418319f380568eaae30c9843fcea
Backed up before n8n migration

> 💡 Das machst du in dieser Lektion: Du strukturierst deine Sprint-4-Präsentation, bereitest deine Projektergebnisse für die Abgabe vor und verstehst, wonach du bewertet wirst. Außerdem übst du die wichtigsten Talking Points und den Demo-Ablauf, um deinen Contigo-Chatflow vor der Klasse zu präsentieren.

## Was stellen wir uns unter dieser Präsentation vor
Die Sprint-4-Präsentation ist der zentrale Bewertungsmoment für Course 2A. Sie ist kein Rundgang durch deine Canvas-Nodes und keine zeilenweise Erklärung deines System Prompts. Es geht um eine Demonstration und Verteidigung eines funktionierenden Systems. Du zeigst, dass du etwas Funktionierendes gebaut hast. Du erklärst, warum du deine Entscheidungen so getroffen hast. Und du vermittelst, was der Agent macht und warum das im Business-Kontext wichtig ist.
## Was du präsentierst
Du hast über vier Sprints hinweg einen Support-Agenten für Contigo GmbH gebaut. Das kann dieser Agent:
- Führt Multi-Turn-Gespräche mit Session-Isolation
- Ruft präzise Informationen aus einer verifizierten Wissensdatenbank ab
- Ruft Tools für Live-Lookups und Berechnungen auf
- Erzwingt Grounding-Verhalten über einen verfeinerten System Prompt
- Fängt Prompt-Injection-Versuche ab, bevor sie das Modell erreichen
- Fragt vor sensiblen Tool-Aufrufen nach menschlicher Bestätigung
- Scheitert kontrolliert, wenn Tools nicht verfügbar sind
Das ist ein produktionsrelevantes System. Präsentiere es auch so.
## Was du einreichst
Reiche vor dem Präsentationstag Folgendes über die Kurs-Submission-Plattform ein.
[TABLE]
  | Ergebnisse | Was rein muss |
  | Public Chat URL | Deine aktive ngrok-URL, die auf deinen lokalen Flowise-Chatflow zeigt. Muss erreichbar sein, wenn der Kursleiter sie öffnet. |
  | Chatflow-Export | Der .json-Export deines Chatflows, heruntergeladen aus dem Flowise-Dashboard. Enthält Canvas-Struktur, Node-Konfiguration und Tool-Definitionen. |
  | System Prompt | Die finale, verfeinerte Version deines Tool-Agent-System-Prompts als einzelne .txt- oder .md-Datei. |
  | Architecture Brief | Eine einseitige Zusammenfassung der Architektur deines Agenten und der wichtigsten Entscheidungen dahinter. |
Das Architecture Brief sollte auf einer Seite oder weniger vier Fragen beantworten:
- Was macht der Agent, und für wen?
- Welche architektonischen Entscheidungen hast du getroffen, und warum?
- Für welche Fehlermodi hast du vorgesorgt?
- Wo liegt die Lücke zwischen deinem Prototyp und einem Produktivdeployment?
## Anleitung zur Abgabe
1. Speichere jede Datei nach der Namenskonvention YourName_2A_FinalProject_[type], zum Beispiel YourName_2A_FinalProject_Chatflow.json, YourName_2A_FinalProject_SystemPrompt.md, YourName_2A_FinalProject_Brief.pdf.
1. Lade alle Dateien in einen einzigen Google-Drive-Ordner hoch.
1. Stelle die Freigabe des Ordners auf Jeder mit dem Link kann ansehen.
1. Füge den Link zum Google-Drive-Ordner in die Submission-Plattform ein.
1. Trag deine aktive ngrok-URL als separates Feld im Abgabeformular ein.
> ⚠️ 
  ### Wichtig: Bestätige vor dem Einreichen, dass der Google-Drive-Ordner auf Anyone with the link can view gesetzt ist. Gesperrte Ordner können nicht bewertet werden und werden an dich zurückgegeben.

## Struktur der Präsentation
Teil 1: Problem und Kontext (1–2 Minuten). Steig mit dem Business-Problem ein. Erkläre, wer Contigo GmbH ist und was das Unternehmen macht, welches Problem der Support-Agent löst und was der Agent können muss, um in diesem Kontext nützlich zu sein.
Teil 2: Live-Demonstration (2–3 Minuten). Zeig, wie der Agent über deine Public Chat URL funktioniert. Führe eine Gesprächssequenz durch, die Memory, Retrieval aus der Wissensdatenbank, Tool-Einsatz, Fallback-Verhalten und Security abdeckt.
Teil 3: Chatflow-Design (1–2 Minuten). Erkläre kurz die Architektur dahinter. Geh auf die zentralen Komponenten ein, die du in der Live-Demonstration gezeigt hast.
Teil 4: Lücken und Reflexion (1 Minute). Schließe mit einer ehrlichen Beobachtung zur Lücke zwischen deinem Prototyp und einem Produktivdeployment.
## Was du vermeiden solltest
- Geh die Canvas nicht Node für Node durch. Erzähle die Konversation und erkläre die Architektur, nicht die Oberfläche.
- Lies nicht von Notizen ab. Kenn deine Talking Points gut genug, um natürlich zu sprechen.
- Halte die Demo im Fluss. Tempo zählt.
- Lass die Produktionslücke nicht aus. Sie ist das klarste Signal für architektonische Reife.
## Worauf die Bewertenden achten
Deine Präsentation wird nach Argumentation und Demonstration bewertet, nicht nach Folien-Politur oder Canvas-Ästhetik. Ein funktionierender Agent, klar demonstriert mit groben Talking Points, schneidet besser ab als ein wunderschönes Deck mit kaputter Demo.
Bewertet wird:
- Funktioniert der Agent End-to-End bei den vorbereiteten Szenarien?
- Kannst du erklären, warum du jede architektonische Komponente gewählt hast, ohne von Notizen abzulesen?
- Kannst du die Trade-offs begründen: warum ein Tool Agent statt einer Conversational Retrieval QA Chain, warum genau diese Tool-Beschreibungen, warum diese Memory-Konfiguration?
- Kannst du Fehlermodi beschreiben, die der Agent kontrolliert abfängt, und mindestens einen nennen, den er nicht abfängt?
- Kannst du architektonische Fragen beantworten, mit Herleitung statt mit Rätselraten?
## Vorbereitungs-Checkliste
Erledige das alles vor dem Präsentationstag.
Build-Verifizierung:
- [ ] Alle zwölf Turns aus der Live-Validierungskonversation von Sprint 3 bestehen
- [ ] Public Chat URL getestet und über ngrok funktionsfähig
- [ ] ngrok Inspection Dashboard unter http://localhost:4040 bestätigt
- [ ] Toggle Make Public im Tab Chatflow Configuration → Security aktiviert
- [ ] Chatflow als .json exportiert und mit der Abgabe-Namenskonvention gespeichert
- [ ] System Prompt als .mdoder .txtDatei exportiert
- [ ] Einseitiges Architektur-Kurzbeschreibung entworfen und als PDF gespeichert
Inhaltliche Vorbereitung:
- [ ] Einstieg mit der Problemstellung geübt: kannst Contigos Kontext in unter 90 Sekunden ohne Notizen erklären
- [ ] Zwölf Demo-Turns geübt: du weißt vor dem Absenden, was jeder einzelne zeigen soll
- [ ] Vier Architektur-Punkte vorbereitet: Memory, Retrieval, Tools, Safety
- [ ] Produktionslücke ausgewählt und vorbereitet: eine ehrliche, konkrete Beobachtung
- [ ] Abgabe-Ergebnisse in den Google-Drive-Ordner hochgeladen, Link-Freigabe bestätigt
Am Tag selbst:
- [ ] Docker Desktop geöffnet und alle drei Container laufen, bevor die Session beginnt
- [ ] ngrok-Tunnel aktiv, öffentliche URL als funktionsfähig bestätigt
- [ ] Public Chat URL bei Bedarf vorab mit Kursleiter oder Klasse geteilt
- [ ] Präsentations-Zeitfenster bestätigt
## Code Clinic
Vor dem Präsentationstag hast du Zugang zu einer Code-Clinic-Session. Nutze sie. Bring deinen Chatflow mit, eine Liste aller Fehler aus deiner Sprint-3-Validierung und alle architektonischen Fragen, die du bisher nicht allein lösen konntest. Die Code Clinic ist eine Support-Session. Genau der richtige Ort, um eine kaputte Tool-Beschreibung zu debuggen, einen Memory-Edge-Case durchzugehen oder deine Architecture Defense vor der Live-Präsentation auf Herz und Nieren zu prüfen.
> 💡 Fazit:
Die Präsentation ist keine Tour durch deine Flowise-Canvas. Sie zeigt, dass du etwas Funktionierendes gebaut hast. Und sie verteidigt, warum du es genau so gebaut hast.
  Jede Architekturentscheidung, die du über vier Sprints hinweg getroffen hast, war eine bewusste Wahl als Antwort auf eine spezifische Anforderung. Zu wissen, warum du jede Entscheidung getroffen hast, ist das, was eine selbstbewusste Präsentation von einer zögerlichen unterscheidet.

