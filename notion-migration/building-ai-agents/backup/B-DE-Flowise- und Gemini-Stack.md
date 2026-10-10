# Flowise- und Gemini-Stack

Notion page: https://app.notion.com/p/Flowise-und-Gemini-Stack-3789418319f38044ad03f6374b5df510
Backed up before n8n migration

> OpenRouter statt Gemini verwenden
  Einige AI-Kursmaterialien zeigen möglicherweise ein direktes Gemini-Setup in Tools wie n8n, Flowise oder Cursor. In diesem Programm verwendest du stattdessen deinen von Masterschool bereitgestellten OpenRouter-Key. Die Workflow-Logik bleibt gleich, aber die Modellverbindung kann sich ändern.
  Lies vor dem Start den Setup-Guide: How-To: OpenRouter statt Gemini verwenden
> 💡 Was du am Ende dieser Lektion verstehen wirst: Wie Flowise, Gemini und Wissensspeicher als selbst gehosteter Stack zusammenpassen und warum Agentflow v2 die richtige Build-Umgebung ist, um einen Business-tauglichen AI-Agenten-Workflow zu erstellen.
## Der Ausgangspunkt
Meridian Consulting ist eine Berliner Operations-Beratung, die mit mittelständischen Unternehmen in Deutschland, Polen und der Tschechischen Republik arbeitet. Ihre Kunden führen schlanke Teams und verlassen sich stark auf Meridians Berater für Prozessdesign, Anbieterauswahl und operative Fehlerbehebung.
Das Unternehmen entwickelt einen internen KI-Agenten für sein Beratungsteam. Das System beantwortet Routinefragen schneller, bereitet Fallhistorien übersichtlich vor und leitet komplexe Anfragen direkt an Experten weiter. Für die Umsetzung nutzt das Team das visuelle Open-Source-Tool Flowise. Da die Software lokal auf eigenen Servern läuft, fallen keine Kosten für eine verwaltete Cloud-Infrastruktur an.
Alles beginnt mit den passenden Tools. Das Team hat mehrere Optionen verglichen und setzt auf ein Zusammenspiel aus Flowise und Googles Gemini-Modellen. Bevor die technische Einrichtung startet, muss das Team verstehen, wie diese Komponenten zusammenwirken und welche Rolle sie im System spielen.
## Warum ein visueller Builder?
Wer KI-Workflows von Grund auf in reinem Python oder JavaScript baut, behält die volle Kontrolle. Allerdings erfordert das viel Boilerplate-Code für jede API-Integration, jede Prompt-Kette, jedes Memory-Modul und jede Tool-Verbindung. Zudem muss dieser Code laufend gewartet werden, während sich die zugrunde liegenden Modelle und APIs weiterentwickeln.
Flowise ist ein visueller Open-Source-Low-Code-Builder für LLM-gestützte Anwendungen. Auf einer Drag-and-Drop-Oberfläche verbindest du Komponenten, die als Nodes dargestellt sind, rein visuell miteinander. Die zugrunde liegende Logik gleicht einer Code-Implementierung. Doch hier bleibt die Architektur sichtbar, lässt sich direkt debuggen und verändern, ohne den Anwendungscode anzufassen.
Für Meridians Team ist das der entscheidende Vorteil. Zu ihm gehören auch Berater, die keine Softwareentwickler sind. Menschen, die das Geschäftsproblem verstehen, bauen, testen und verfeinern den Agenten selbst. Für Änderungen brauchen sie kein eigenes Engineering-Team.
Flowise ist Open Source und läuft daher kostenlos lokal mit Node.js und npm. Dieses Setup nutzt du im gesamten Kurs. Du führst die Software direkt auf deinem eigenen Rechner aus. Ein Abonnement brauchst du dafür nicht.

## Warum Agentflow v2?
Flowise stellt zwei Build-Umgebungen bereit: Chatflow und Agentflow v2.
Chatflow ist für einfachere, lineare Workflows konzipiert, etwa einen einzelnen Agenten, der einer festen Abfolge von Schritten folgt. Es ist nützlich für einfache Gesprächsagenten, wird aber schnell einschränkend, wenn ein Workflow verzweigen, loopen, Wissen dynamisch abrufen oder mehrere Schritte mit gemeinsamem Kontext koordinieren muss.
Dieser Kurs nutzt Agentflow v2. Mit dieser nativen Orchestrierungsumgebung von Flowise baust du zustandsbehaftete, mehrstufige KI-Workflows auf. Jeder Schritt im Workflow stellt einen einzelnen Node auf dem Canvas dar. Die Verbindungen zwischen den Nodes definieren den Ausführungspfad explizit. Diese Architektur unterstützt:
- Bedingte Verzweigung auf Grundlage von Regeln oder AI-Reasoning
- Loops und Retry-Logik
- Wissensabruf aus Document Stores
- Gemeinsamen Kontext über Nodes hinweg über Flow State
- Human-Approval-Checkpoints
- Modulare Sub-Flows
Für Meridians Agenten ist Agentflow v2 von Anfang an die richtige Umgebung.

## Die Reasoning-Engine: Gemini Flash und Flash-Lite
Im Zentrum jedes Agenten-Stacks steht ein Sprachmodell. Diese Komponente liest den Prompt, wertet ihn aus und generiert die Antwort. In diesem Stack übernehmen Googles Modelle Gemini 2.5 Flash und Gemini 2.5 Flash-Lite diese Rolle.
1. Gemini 2.5 Flash bietet Googles bestes Preis-Leistungs-Verhältnis. Das Modell wurde für geringe Latenzen und hohe Volumina entwickelt, die Reasoning und agentische Use Cases erfordern. Deshalb ist es das Hauptmodell für diesen Kurs. Es ist leistungsstark genug, um mehrstufiges Agenten-Reasoning innerhalb von Agentflow v2 zu bewältigen. Gleichzeitig bleibt es beim häufigen Entwickeln und Testen kosteneffizient.
1. Gemini 2.5 Flash-Lite ist das wirtschaftlichste multimodale Modell der 2.5-Familie. Es übernimmt häufige, leichtgewichtige Aufgaben, bei denen vor allem Budget und Tempo zählen. Bei Routineanfragen ohne tiefes Reasoning hält Flash-Lite die Betriebskosten niedrig. Das ist entscheidend für Meridian, da die Berater den Agenten über den gesamten Arbeitstag hinweg häufig nutzen.
Beide Modelle sind im kostenlosen Kontingent der Gemini-API enthalten. Das reicht völlig aus, um in diesem Kurs zu bauen und zu testen. Allerdings nutzt Google die gesendeten Daten in der kostenlosen Version, um seine Modelle zu verbessern. Für Meridians Live-Betrieb mit echten Kundendaten ist ein Upgrade auf die kostenpflichtige Stufe vor dem Go-live daher zwingend erforderlich.
> 🔥 Später kannst du auch andere kostenlose Modelle nutzen. Das ist völlig in Ordnung: Modellnamen ändern sich im Laufe der Zeit, aber die Setup-Logik bleibt gleich. Wähle einfach die neueste verfügbare Flash- oder Flash-Lite-Option in deinem Flowise-/Gemini-Konto. Sollte ein Modell einmal nicht verfügbar, überlastet oder veraltet sein, weiche auf das nächstneuere Modell aus der Flash-Familie aus und mach weiter.
![image]((notion-hosted file))
Zur Orientierung sieht die Preisgestaltung der kostenpflichtigen Stufe wie folgt aus:
[TABLE]
  | Model | Input (per 1M tokens) | Output (per 1M tokens) | Best suited for |
  | Gemini 2.5 Flash-Lite | $0.10 | $0.40 | Hochfrequente, leichtgewichtige Aufgaben |
  | Gemini 2.5 Flash | $0.30 | $2.50 | Agentische Workflows, die Reasoning erfordern |
  | Gemini 2.5 Pro | $1.25 | $10.00 | Komplexes Reasoning mit langen Dokumenten |
Für die aktuellen Modellstrings, vollständige Funktionsdetails und aktuelle Preise siehe die offizielle Gemini-API-Dokumentation unter ai.google.dev/gemini-api/docs/models und ai.google.dev/gemini-api/docs/pricing.

## Die Wissensschicht: Document Stores und der Retriever Node
Sprachmodelle können nicht nativ große Dokumentensammlungen durchsuchen. Um dem Agenten Zugriff auf Meridians interne Fallbibliothek, Anbieterdatenbank und operative Playbooks zu geben, müssen diese Inhalte zuerst in ein Format geladen werden, das der Agent semantisch durchsuchen kann.
In Agentflow v2 wird dies über Flowise Document Stores gehandhabt. Ein Document Store ist ein verwalteter Wissenscontainer, der in Flowise eingebaut ist. Dokumente werden in den Store hochgeladen, gechunkt, eingebettet und indexiert. Wenn ein Agent Informationen abrufen muss, fragt er den Store über den Retriever Node ab oder greift direkt über die Knowledge-Konfiguration des Agent Nodes darauf zu.
Das ist der systemeigene Agentflow-v2-Ansatz für Retrieval und die Methode, die dieser Kurs verwendet. Externe Vektordatenbanken wie Chroma können ebenfalls über die Vector-Embeddings-Konfiguration des Agent Nodes verbunden werden, aber Document Stores sind der empfohlene Ausgangspunkt und erfordern keine zusätzliche Infrastruktur zum Einrichten.

## Wie die Komponenten verbunden sind
[TABLE]
  | Komponente | Technologie | Rolle im Stack |
  | Orchestrierungsumgebung | Flowise Agentflow v2 | Expliziter Workflow-Canvas, auf dem jeder Schritt ein Node ist; steuert Ausführungsreihenfolge, Verzweigung und Zustand |
  | Reasoning-Engine | Gemini Flash / Flash-Lite | Treibt das Reasoning, die Tool-Auswahl und die Antwortgenerierung des Agent Nodes an |
  | Wissensschicht | Flowise Document Stores | Speichert Inhalte und ruft sie semantisch ab; wird vom Retriever Node oder Agent Node abgefragt |
  | Gemeinsamer Kontext | Flow State ($flow.state) | Runtime-Key-Value-Store, der Daten während einer einzelnen Ausführung zwischen Nodes weitergibt |
## Verständnis prüfen
>  Was ist in Agentflow v2 der wichtigste Unterschied zwischen einem Document Store und dem Flow State?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/3e31c67a-14a9-4883-8f33-da319e108a7c

> 💡  Takeaway: 
  Im Agentflow-v2-Stack sind die Verantwortlichkeiten klar aufgeteilt. Flowise dient als Orchestrierungsumgebung und läuft kostenlos lokal via npm. Gemini denkt nach und generiert die Antworten. Document Stores speichern das nötige Wissen, und der Flow State verknüpft alle Elemente zur Laufzeit. 
  Wer die genaue Rolle jeder einzelnen Komponente versteht, schafft die Basis für einen stabilen, wartungsfreundlichen Agenten, der problemlos mit seinen Aufgaben wachsen kann.
