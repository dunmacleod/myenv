# Memory- und State-Architektur für den Projektagenten

Notion page: https://app.notion.com/p/Memory-und-State-Architektur-f-r-den-Projektagenten-e069418319f3822d981b013d9f44d59d
Backed up before n8n migration

Nordvik Freight koordiniert Großhandelslieferungen in Norwegen, Schweden und Finnland. Das Operations-Team bearbeitet jede Woche hunderte Lieferantenanfragen. Dazu gehören Fragen zu Preisfenstern, Routenverfügbarkeit und Zoll-Compliance-Dokumentation. Bis jetzt wurden diese Anfragen manuell von drei Spezialistenteams bearbeitet. Nordviks Product Lead Astrid wurde damit beauftragt, das erste interne Multi-Agent-System des Unternehmens zu bauen, um diese Anfragen automatisch zu routen und zu beantworten.
Astrids Team hat eine Flowise-Agentflow-V2-Canvas mit folgender Struktur entworfen:
- Ein Classifier Agent (LLM-Node), der jede eingehende Lieferantenanfrage liest und in eine von drei Kategorien klassifiziert: pricing, logistics oder compliance. Er schreibt die Klassifizierung und den ursprünglichen Anfragetext in Flow State.
- Ein Condition-Node, der die Klassifizierung aus Flow State liest und zum passenden Spezialagenten routet.
- Ein Pricing Agent, ein Logistics Agent und ein Compliance Agent. Jeder ist so konfiguriert, dass er die Lieferantenanfrage aus Flow State als User-Message-Eingabe liest.
- Ein Direct-Reply-Node auf jedem Spezialistenpfad, der die Antwort des Agenten zurückgibt.
![image]((notion-hosted file))
Das System steht kurz vor dem Testing. Astrid hat dich gebeten, die Memory- und State-Architektur zu prüfen, bevor die ersten echten Anfragen verarbeitet werden. Deine Aufgabe ist es, ein vollständiges Architekturreview zu erstellen, indem du abdeckst, was geteilt und was privat ist, was nicht persistieren darf und wie Recovery aussieht, wenn etwas schiefgeht.
## Womit du arbeitest
Nordviks Canvas hat die folgende Flow-State-Konfiguration, wie sie auf dem Start-Node deklariert ist:
[TABLE]
  | Schlüssel | Standardwert | Geschrieben von |
  | query_category | unclassified | Classifier Agent (via Update Flow State) |
  | supplier_query | (leerer String) | Classifier Agent (via Update Flow State) |
  | urgency | normal | Classifier Agent (via Update Flow State) |
Das Structured-Output-Schema des Classifier:
[TABLE]
  | Schlüssel | Typ | Werte |
  | query_category | enum | pricing, logistics, compliance, unclassified |
  | supplier_query | string | Die ursprüngliche Anfrage wortgetreu |
  | urgency | enum | high, normal |
Jeder Spezialagent hat allMessages-Memory aktiviert und liest {{$flow.state.supplier_query}} als seine User-Message-Eingabe.
Der Compliance Agent schreibt zusätzlich über seine eigene llmUpdateState-Konfiguration einen Wert in $flow.state: Er schreibt compliance_flag: "review_required", wenn er eine Anfrage erkennt, die eine manuelle regulatorische Prüfung erfordern könnte.
Derzeit gibt es keinen Fallback-Branch im Condition-Node für unclassified.
## Behalte bei der Arbeit diese Fragen im Blick
Lies die Canvas-Beschreibung oben sorgfältig durch, bevor du die Aufgaben unten bearbeitest. Überlege:
- Welche Flow-State-Schlüssel werden zwischen Agenten geteilt; und welche Agenten brauchen welchen Schlüssel?
- Welche Informationselemente sind turn-scoped, session-scoped oder Kandidaten für persistente Speicherung?
- Was passiert mit jedem Schlüssel, wenn der Classifier scheitert, bevor er in ihn schreibt?
- Was bedeutet der compliance_flagSchreibvorgang des Compliance Agent für die anderen Agenten in derselben Session?
- Ist das Fehlen eines unclassifiedFallbacks eine Designlücke oder ein akzeptables Risiko für dieses System?
Du musst diese Fragen nicht direkt beantworten. Sie sind diagnostische Prompts. Nutze sie, um deine Analyse über die vier Aufgaben hinweg zu steuern.
## Schnelldiagnose
> 🔥 Bevor du beginnst, erstelle eine Kopie von dieser Vorlage. Sie folgt dem Aufbau dieser Lektion: ein Tab mit dem Canvas-Kontext, dann ein Tab pro Aufgabe (A: Boundary Map, B: was nicht persistieren darf, C: State Recovery, D: Fehlerisolation), und ein finales Checksheet.
### Frage 1
>  Der Logistics Agent ist mit aktivierter allMessages-Memory konfiguriert und liest {{$flow.state.supplier_query}} als seine User Message. Ein Lieferant sendet zwei Anfragen in derselben Session; zuerst zu Pricing, dann zur Routenverfügbarkeit. Was erhält der Logistics Agent bei der zweiten Anfrage als User-Message-Eingabe?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bdfb2cb8-f4dd-4164-8c6a-b14f8713319e
### Frage 2
>  Der Compliance Agent schreibt compliance_flag: "review_required" in Flow State, wenn er ein regulatorisches Problem erkennt. Im nächsten Turn derselben Session sendet der Lieferant eine Pricing-Anfrage. Der Classifier läuft und routet zum Pricing Agent. Welches Risiko erzeugt der Schlüssel compliance_flag?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/299017fa-696d-4573-ae2d-da6a1a0d9335
### Frage 3
>  Nordviks Canvas hat keinen Fallback-Branch im Condition-Node für unclassified. Ein Lieferant sendet die Nachricht "Hello, is anyone there?". Der Classifier gibt query_category: "unclassified" zurück. Was passiert?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8df46cb0-a9ac-4de3-89ae-3c436cae5831
## Aufgabe A: Die Memory-Grenzen kartieren
Erstelle für die Nordvik-Canvas eine Memory Boundary Map, die jedes Informationselement abdeckt, das sich zwischen Agenten bewegt. Nutze das Drei-Spalten-Format unten.
[TABLE]
  | Information | Geteilt oder privat | Persistenz-Scope |
  | query_category |  |  |
  | supplier_query |  |  |
  | urgency |  |  |
  | compliance_flag |  |  |
  | System-Prompt jedes Spezialagenten |  |  |
  | allMessages-Konversationshistorie |  |  |
Für jede Zeile:
- Geteilt oder privat: Gib an, ob die Information geteilt ist (von mehr als einem Node in der Canvas lesbar), privat ist (nur vom Agenten lesbar, der sie erzeugt hat) oder geteilt mit Bedingungen ist (von mehreren Nodes lesbar, aber mit einer Einschränkung, welche Agenten danach handeln sollten).
- Persistenz-Scope: Gib an, ob die Information turn-scoped ist (nur für den Agenten-Turn gültig, der sie erzeugt hat), session-scoped ist (für die aktuelle Session gültig) oder über Sessions hinweg persistieren sollte (und falls ja, warum).
Passt das aktuelle Canvas-Design bei einer Zeile nicht zu deinem empfohlenen Design, notier die Lücke in einem einzeiligen Kommentar darunter. Zum Beispiel, wenn ein Wert derzeit geteilt ist, aber eigentlich privat sein sollte, oder session-scoped ist, aber eigentlich turn-scoped sein sollte.
## Aufgabe B: Identifizieren, was nicht persistieren darf
Drei Informationselemente in der Nordvik-Canvas sind Kandidaten für die Kategorie „darf nicht persistieren". Identifiziere sie, gib an, in welche der vier Kategorien sie fallen (flüchtiger Identifikator, abgeleitete Annahme, beiläufig geteilte PII oder Arbeitskontext), und schreibe einen Satz dazu, wie du verhindern würdest, dass sie über den angemessenen Scope hinaus persistieren.
Du musst nicht für jedes eine Canvas-Änderung vorschlagen. Eine System-Prompt-Anweisung, eine Designnotiz oder eine dokumentierte Einschränkung reicht aus.
## Aufgabe C: Das State-Recovery-Design definieren
Die Nordvik-Canvas hat zwei State-Recovery-Lücken, die in der Canvas-Beschreibung identifiziert wurden: das Fehlen eines Fallback-Branch für unclassified und der Schlüssel compliance_flag, der über Turns hinweg persistiert, ohne zurückgesetzt zu werden.
Schreibe für jede Lücke:
1. Das Fehlerszenario: Was passiert mit Flow State und mit der Erfahrung des Lieferanten, wenn die Lücke ausgelöst wird?
1. Der sichere State: Was jeder betroffene Flow-State-Schlüssel nach der Recovery enthalten sollte.
1. Der Recovery-Mechanismus: Eine spezifische Canvas-Änderung, die die Lücke adressiert. Sei präzise: Benenne den Node, den Schlüssel und den Wert.
## Aufgabe D: Fehlerisolation bewerten
Der Compliance Agent schreibt zusätzlich zum Lesen in $flow.state, konkret in den Schlüssel compliance_flag. Kein anderer Spezialagent schreibt in Flow State.
Bewerte, ob das Schreibverhalten des Compliance Agent ein Fehlerisolationsrisiko für die anderen Agenten in der Canvas erzeugt. Deine Bewertung sollte adressieren:
- Ob der compliance_flagSchreibvorgang eine benannte, dokumentierte Entscheidung oder ein impliziter Nebeneffekt ist.
- Ob der Pricing Agent oder Logistics Agent von einem veralteten compliance_flagWert betroffen sein könnten.
- Welche Isolationsgrenze du empfehlen würdest: welche Agenten unter welchen Bedingungen in $flow.state schreiben dürfen.
Schreibe deine Bewertung in maximal drei kurzen Absätzen.
## Abschlussprüfung
Prüfe deine Arbeit anhand dieser Fragen:
- Deckt deine Memory Boundary Map jedes Informationselement ab, das sich zwischen Agenten bewegt, einschließlich allMessages und des compliance_flagSchreibvorgangs?
- Hast du in Aufgabe B mindestens drei Elemente identifiziert, die jeweils einer der vier Persistenzkategorien zugeordnet sind?
- Benennt jeder Recovery-Mechanismus in Aufgabe C einen spezifischen Node, Schlüssel und Wert, oder bleibt er auf der Ebene allgemeiner Prinzipien?
- Bezieht deine Bewertung der Fehlerisolation in Aufgabe D Position (empfiehlt eine konkrete Grenze), statt nur Überlegungen ohne Schlussfolgerung aufzulisten?
## Zusammenfassung
In diesem Assessment wendest du das Framework für die Memory- und State-Architektur auf ein völlig neues System an. Das bedeutet: eine andere Organisation, eine andere Agentenstruktur und ganz neue Fehlerszenarien. Die vier Aufgaben behandeln inhaltlich zwar dieselben Themen wie die bisherigen Lektionen, allerdings anhand eines unbekannten Fallbeispiels und ohne vorgegebene Lösungen. 
Ein vollständiges Architekturreview zu verfassen, noch bevor ein System in die Testphase geht, ist exakt die Kernkompetenz, die wir in diesem Sprint aufgebaut haben. Deine hier dokumentierten Entscheidungen machen am Ende den Unterschied zwischen einem System, das lediglich in der Testumgebung funktioniert, und einem, das im Praxiseinsatz stabil läuft.