# Tools zu einem einzelnen Event hinzufügen

Notion page: https://app.notion.com/p/Tools-zu-einem-einzelnen-Event-hinzuf-gen-3779418319f3803b9ef9d5b760708a19
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Wie Tools ein Sprachmodell von einem reinen Text-Generator zu einem aktiven System machen, das mit Live-Daten und externen Diensten interagieren kann.

## Die Grenze von reinem Nur-Lese-RAG
Contigo GmbHs Support-Agent ruft präzise Informationen aus der Wissensdatenbank ab und beantwortet Kundenfragen zu Kreditprodukten, Anspruchsvoraussetzungen und Compliance-Anforderungen. Bei informationellen Anfragen arbeitet er zuverlässig.
Es ist jedoch eine Kategorie von Kundenanfragen aufgetaucht, die das aktuelle System nicht bewältigen kann. Ein Kunde wendet sich an den Agenten und bittet nicht um Informationen, sondern um eine Handlung.
> „Bitte stornieren Sie meinen ausstehenden Kreditantrag und bestätigen Sie mir die Stornierung per E-Mail."
Der Agent ruft den relevanten Richtlinienabschnitt zu Antragsrückzügen ab. Er formuliert eine professionelle Erklärung des Stornierungsprozesses. Er kann den Antrag jedoch nicht stornieren. Er kann die E-Mail nicht senden. Er kann nur beschreiben, was passieren würde, wenn ein Mensch diese Handlungen ausführen würde.
Das ist die strukturelle Grenze eines reinen Abfrage-Agenten. RAG verschafft dem Agenten Zugang zu Wissen. Es verschafft dem Agenten jedoch nicht die Fähigkeit, auf Grundlage dieses Wissens in der realen Welt zu handeln. Damit Contigo von einem Agenten, der Fragen beantwortet, zu einem wird, der Anfragen tatsächlich löst, braucht der Agent ensprechende Werkzeuge.
## Was Tools sind
Tools sind externe Fähigkeiten, die ein Sprachmodell während seines Denkprozesses programmatisch aufrufen kann. Sie erweitern die Reichweite des Agenten über die reine Texterzeugung hinaus, hin zu Live-Systemen, Datenbanken und Diensten.
Tools lassen sich in drei funktionale Kategorien einteilen, die zusammen die meisten Anforderungen an Unternehmensautomatisierung abdecken.
Daten- und Informations-Tools: Diese verschaffen dem Agenten Zugriff auf aktuelle, strukturierte Daten, die nicht in der Wissensdatenbank enthalten sind und nicht als statische Dokumente eingebettet werden können.
Für Contigo umfasst das etwa die Abfrage der Kundendatenbank zum Kontostatus, die Prüfung der aktuellen Antragswarteschlange oder das Abrufen der Zahlungshistorie eines Kunden aus dem Kernbankensystem. Daten-Tools fragen Live-Systeme in Echtzeit ab.
Aktions- und Ausführungs-Tools: Diese ermöglichen es dem Agenten, den Zustand externer Systeme im Namen des Nutzers zu verändern. Das Stornieren eines Kreditantrags, das Aktualisieren der Kontaktdaten eines Kunden im CRM, das Auslösen eines Workflows zur Dokumentenerstellung oder das Versenden einer Bestätigungs-E-Mail sind allesamt Ausführungshandlungen. Diese Fähigkeiten machen aus dem Agenten einen Informationsanbieter ein System, das Anfragen tatsächlich löst.
Berechnungs-Tools: Sprachmodelle sind bei präziser Mathematik und strukturierter Logikausführung unzuverlässig. Ein Berechnungs-Tool lagert diese Aufgaben an ein deterministisches System aus und gibt das Ergebnis an den Agenten zurück, damit dieser es in seine Antwort einbauen kann.
Für Contigo könnte das bedeuten, die verbleibende Kreditlaufzeit eines Kunden anhand seiner Zahlungshistorie zu berechnen oder eine strukturierte Abfrage gegen die Datenbank der Anspruchskriterien auszuführen.
## Die ReAct-Schleife
Der Mechanismus, der bestimmt, wann und wie ein Agent ein Tool einsetzt, ist das ReAct-Framework, kurz für Reasoning and Acting. ReAct ist das Ausführungsmuster, das die meisten agentischen Frameworks, einschließlich der auf Flowise und Gemini basierenden, im Hintergrund umsetzen, sobald ein Agent mit Tools verbunden ist.
Die Schleife läuft in drei sich wiederholenden Schritten ab.
Thought (Denken): Der Agent überlegt sich den aktuellen Stand der Aufgabe. Er liest die Anfrage des Nutzers, prüft, was er bereits aus dem Gesprächsverlauf und vorherigen Tool-Ergebnissen weiß, und bestimmt, was als Nächstes zu tun ist.
Action (Handeln): Der Agent wählt ein Tool aus und ruft es mit den im Thought-Schritt festgelegten Parametern auf. In dieser Phase erzeugt er noch keine für den Nutzer sichtbare Antwort. Er ruft das Tool auf und wartet auf das Ergebnis.
Observation (Beobachten): Der Agent erhält die Ausgabe des Tools und bezieht sie in seinen Denkkontext ein. Die Schleife kehrt anschließend zum Thought-Schritt zurück. Das setzt sich fort, bis der Agent feststellt, dass er genug Informationen für eine endgültige Antwort hat.
Für Contigos Stornierungsanfrage könnte die ReAct-Schleife folgendermaßen ablaufen.
1. Der Agent denkt: Der Kunde möchte den Antrag APP-7741 stornieren und eine Bestätigungs-E-Mail erhalten.
1. Er handelt: Er ruft das Stornierungs-Tool mit der Antrags-ID auf. Er beobachtet: Das Tool gibt eine Erfolgsbestätigung und eine Referenznummer zurück.
1. Er denkt erneut: Die Stornierung ist bestätigt, jetzt das E-Mail-Tool mit der Referenznummer und der Adresse des Kunden aufrufen.
1. Er handelt erneut: Er beobachtet die E-Mail-Bestätigung. Er erzeugt die endgültige Antwort an den Kunden.
![image]((notion-hosted file))

> ➡️ So funktioniert das in deinem Chatflow: In Flowise wird die ReAct-Schleife über den Tool-Agent-Node umgesetzt. Diesen Node nutzt du, um deine Conversational Retrieval QA Chain zu ersetzen, sobald du deinem Chatflow Tools hinzufügst. Der Tool-Agent-Node verbindet sich mit deinem Sprachmodell, deinem Speicher-Node, deinem Vektorspeicher-Retriever und deinen Tools. Zudem führt er die ReAct-Schleife automatisch für jede eingehende Anfrage aus. Die Schleife zu verstehen, bevor du den Node konfigurierst, macht deine Konfigurationsentscheidungen aussagekräftig statt rein mechanisch.

## Warum das für das Agenten-Design wichtig ist
Das Verständnis der ReAct-Schleife hat direkte Auswirkungen darauf, wie Tools konfiguriert und beschrieben werden. Der Thought-Schritt des Agenten stützt sich vollständig auf die natürlichsprachlichen Beschreibungen der einzelnen Tools, um zu bestimmen, welches Tool aufgerufen wird und welche Parameter übergeben werden. Eine Tool-Beschreibung, die vage ist oder sich mit der Beschreibung eines anderen Tools überschneidet, führt zu Fehlern bei der Weiterleitung.
Die Qualität der Tool-Beschreibung ist der wichtigste Hebel für die Zuverlässigkeit der ReAct-Schleife. Das wird später im Sprint praktisch behandelt.
RAG versus Tool-fähige Agenten
[TABLE]
  |  | RAG-Agent | Tool-fähiger Agent |
  | Primäre Fähigkeit | Informationen aus Dokumenten abrufen und darstellen | Aktionen in externen Systemen und Live-Datenbanken ausführen |
  | Datenzugriff | Statische oder periodisch aktualisierte eingebettete Dokumente | Live-APIs, Datenbanken und Echtzeit-Services |
  | Systemauswirkung | Nur Lesezugriff, kann externen Zustand nicht verändern | Lese- und Schreibzugriff, kann erstellen, aktualisieren und auslösen |
  | Beispiel, Contigo | „Welche Dokumente werden für einen Kreditantrag benötigt?" | „Storniere Antrag APP-7741 und sende eine Bestätigungs-E-Mail“ |
  | Flowise Node | Conversational Retrieval QA Chain | Tool Agent |
## Verständnis prüfen
>  Ein Contigo-Kunde bittet den Support-Agenten, seine registrierte E-Mail-Adresse zu aktualisieren. Der Agent ruft die Richtlinie zur Aktualisierung von Kontaktdaten korrekt ab, nimmt aber keine Änderung am Kundenkonto vor. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a3d41697-73fe-4f60-85a9-23d2edd4275e


> 💡 Fazit:
  RAG verschafft einem Agenten Wissen. Tools verschaffen ihm die Fähigkeit, auf Grundlage dieses Wissens zu handeln. Die ReAct-Schleife ist der Mechanismus, der Denken mit Handeln verbindet, bis die Aufgabe gelöst ist. Damit Contigos Agent vom Beantworten von Fragen zum Lösen von Anfragen übergeht, sind Tools die architektonische Voraussetzung, die den Unterschied zwischen einem hochentwickelten Informationsabrufsystem und einer echten Automatisierungsplattform ausmacht.
  In deinem Chatflow vollzieht sich dieser Übergang, sobald du die Conversational Retrieval QA Chain durch einen Tool-Agent-Node ersetzt und Contigos erstes Aktions-Tool an das Canvas anschließt.
