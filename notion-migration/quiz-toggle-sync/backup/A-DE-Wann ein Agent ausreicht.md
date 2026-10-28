# Wann ein Agent ausreicht

Notion page: https://app.notion.com/p/Wann-ein-Agent-ausreicht-3779418319f380b6a162e15a155cbcea
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Warum ein einzelner, gut ausgestatteter Agent oft die optimale architektonische Wahl ist und welche konkreten geschäftlichen Bedingungen das Hinzufügen weiterer Agenten eher zu einem Nachteil als zu einem Vorteil machen.

## Die Versuchung, zu früh zu skalieren
Das Entwicklungsteam von Contigo GmbH hat etwas wirklich Fähiges gebaut. Der Support-Agent führt Multi-Turn-Gespräche, ruft präzise aus der Wissensdatenbank ab, erzwingt Grounding und behandelt Tool-Fehler graceful. Es ist ein funktionierendes, produktionsreifes System.
Die nächste Planungssitzung des Teams bringt sofort einen Vorschlag hervor: Den Agenten in spezialisierte Sub-Agents aufteilen. Einen für Kreditprodukte. Einen für Compliance-Queries. Einen für Kunden-Account-Management. Einen, der die anderen orchestriert.
Der Compliance Lead stellt eine Frage, die den Raum zum Stillstand bringt:
> Welches Problem genau löst das Hinzufügen weiterer Agenten, das der aktuelle Agent nicht bewältigen kann?
Niemand hat eine klare Antwort. Der Vorschlag wird zurückgestellt, weil der Fall für den Bau eines solchen Systems nicht gemacht wurde. Bevor Koordinationskomplexität eingeführt wird, muss das Team genau verstehen, wann ein einzelner Agent nicht mehr ausreicht. Dieses Verständnis beginnt hier.
## Eine Single-Agent-Architektur definieren
In einem Single-Agent-Pattern fungiert ein Sprachmodell als zentrale Reasoning Engine für alle Aufgaben. Es verarbeitet jede Query über dasselbe Modell, dasselbe Memory und dasselbe Toolset. Jede Anfrage tritt in denselben Reasoning Loop ein und verlässt ihn über denselben Schritt zur Antwortgenerierung.
- Debugging: Wenn der Agent eine unerwartete Antwort erzeugt, gibt es eine Reasoning Chain zu prüfen. Der Prompt, die abgerufenen Chunks, der Tool-Output und die generierte Antwort sind alle Teil einer einzelnen, nachvollziehbaren Sequenz. In einem Multi-Agent-System könnte derselbe Fehler drei oder vier Agenten betreffen, die State untereinander weitergeben, wobei jeder einzelne die Ursache des Problems sein könnte.
- Kostenvorhersagbarkeit: Ein einzelner Agent führt pro Query eine begrenzte Anzahl von Sprachmodellaufrufen aus. Der Token-Verbrauch pro Interaktion ist vorhersagbar und handhabbar. Multi-Agent-Systeme können für dieselbe zugrunde liegende Aufgabe zehn- bis fünfzehnmal mehr Tokens verbrauchen, weil Koordination, Delegation und Synthese alle zusätzliche Modellaufrufe erfordern.
- Latenz: Ein einzelner Agent verarbeitet eine Query in einem sequenziellen Durchlauf. Jeder Agent, der einem System hinzugefügt wird, fügt dem kritischen Pfad jeder Antwort mindestens einen zusätzlichen Modellaufruf hinzu.
## Wann ein einzelner Agent die richtige Antwort ist
Ein einzelner Agent bewältigt die Mehrheit der Business Use Cases, die Organisationen tatsächlich in großem Maßstab deployen. Die Bedingungen, die eine Single-Agent-Architektur begünstigen, sind branchenübergreifend konsistent.
Die Aufgabe ist klar eingegrenzt: Sie hat einen klaren Input, ein definiertes Ziel und ein begrenztes Set an Tools, die nötig sind, um es zu erreichen. Contigos Support-Agent behandelt Kredit-Queries, Compliance-Lookups und Account-Statusprüfungen. Das sind unterschiedliche Aufgaben, aber sie bewegen sich innerhalb einer einzigen Domain und greifen auf ein konsistentes Set an Fähigkeiten zurück.
Die Aufgabe ist repetitiv: Dieselben Arten von Queries kommen regelmäßig an, und das Antwortmuster des Agenten bleibt über sie hinweg stabil. Contigos Kunden fragen nach Kreditwürdigkeit, Antragsanforderungen und Zahlungsoptionen. Der Agent muss nicht für jede Interaktion neue Reasoning-Strategien erfinden.
Die Aufgabe erfordert nicht gleichzeitig tiefes Cross-Domain-Fachwissen: Eine Query, die Finanzanalyse, juristische Auslegung und Software Engineering in demselben Reasoning Loop erfordert, ist eine wirklich andere Herausforderung als eine, die nur Finanzdienstleistungswissen erfordert. Contigos Queries liegen klar in der Finanzdienstleistungs-Domain.
## Single Agent versus Multi-Agent auf einen Blick

## Die Versuchung, zu früh zu skalieren
Das Entwicklungsteam von Contigo GmbH hat etwas wirklich Leistungsfähiges gebaut. Der Support-Agent führt mehrstufige Gespräche, ruft präzise Informationen aus der Wissensdatenbank ab, sorgt für Grounding und geht souverän mit Tool-Fehlern um. Es ist ein funktionierendes, produktionsreifes System.
Die nächste Planungssitzung des Teams bringt sofort einen Vorschlag hervor: den Agenten in spezialisierte Sub-Agenten aufzuteilen. Einen für Kreditprodukte. Einen für Compliance-Anfragen. Einen für die Verwaltung von Kundenkonten. Und einen, der die anderen koordiniert.
Die Leiterin der Compliance-Abteilung stellt eine Frage, die den Raum verstummen lässt:
> Welches Problem löst das Hinzufügen weiterer Agenten konkret, das der aktuelle Agent nicht bewältigen kann?
Niemand hat eine klare Antwort. Der Vorschlag wird zurückgestellt, weil die Begründung für den Bau fehlt. Bevor das Team zusätzliche Koordinationskomplexität einführt, muss es genau verstehen, wann ein einzelner Agent tatsächlich an seine Grenzen stößt. Dieses Verständnis beginnt hier.
## Definition einer Single-Agent-Architektur
In einem Single-Agent-Muster übernimmt ein einziges Sprachmodell die zentrale Denkarbeit für alle Aufgaben. Es bearbeitet jede Anfrage mit demselben Modell, demselben Speicher und demselben Werkzeugsatz. Jede Anfrage durchläuft denselben Denkprozess und verlässt ihn über denselben Schritt der Antworterzeugung.
- Debugging: Erzeugt der Agent eine unerwartete Antwort, gibt es eine einzige Gedankenkette zu prüfen. Der Prompt, die abgerufenen Textabschnitte, die Tool-Ausgabe und die generierte Antwort sind alle Teil einer einzigen, nachvollziehbaren Abfolge. In einem Multi-Agenten-System könnte derselbe Fehler drei oder vier Agenten betreffen, die Zustände untereinander austauschen, und jeder von ihnen könnte die Fehlerquelle sein.
- Kostenvorhersehbarkeit: Ein einzelner Agent führt pro Anfrage eine begrenzte Anzahl von Sprachmodell-Aufrufen aus. Der Token-Verbrauch pro Interaktion ist vorhersehbar und gut steuerbar. Multi-Agenten-Systeme können für dieselbe zugrunde liegende Aufgabe das Zehn- bis Fünfzehnfache an Tokens verbrauchen, weil Koordination, Delegation und Zusammenführung jeweils zusätzliche Modellaufrufe erfordern.
- Latenz: Ein einzelner Agent verarbeitet eine Anfrage in einem sequenziellen Durchlauf. Jeder zusätzliche Agent in einem System fügt dem kritischen Pfad jeder Antwort mindestens einen weiteren Modellaufruf hinzu.
## Wann ein einzelner Agent die richtige Antwort ist
Ein einzelner Agent bewältigt die Mehrheit der geschäftlichen Anwendungsfälle, die Organisationen tatsächlich im großen Stil einsetzen. Die Bedingungen, die für eine Single-Agent-Architektur sprechen, sind branchenübergreifend konsistent.
Die Aufgabe ist gut abgegrenzt: Sie hat eine klare Eingabe, ein definiertes Ziel und einen begrenzten Satz an Tools, die zur Erreichung dieses Ziels nötig sind. Contigos Support-Agent bearbeitet Kreditanfragen, Compliance-Abfragen und Kontostandsprüfungen. Das sind unterschiedliche Aufgaben, die aber innerhalb einer einzigen Domäne liegen und auf einen konsistenten Satz an Fähigkeiten zurückgreifen.
Die Aufgabe ist repetitiv: Dieselben Arten von Anfragen kommen regelmäßig herein, und das Antwortmuster des Agenten bleibt dabei stabil. Contigos Kunden fragen nach Kreditwürdigkeit, Antragsvoraussetzungen und Zahlungsoptionen. Der Agent muss für jede Interaktion keine neuen Denkstrategien entwickeln.
Die Aufgabe erfordert keine tiefgreifende bereichsübergreifende Expertise gleichzeitig: Eine Anfrage, die Finanzanalyse, juristische Auslegung und Softwareentwicklung im selben Denkprozess erfordert, ist eine grundlegend andere Herausforderung als eine, die nur Wissen aus dem Finanzdienstleistungsbereich benötigt. Contigos Anfragen liegen eindeutig im Bereich der Finanzdienstleistungen.
## Single-Agent versus Multi-Agent im Überblick
[TABLE]
  |  | Single-Agent-Architektur | Multi-Agent-Architektur |
  | Komplexität | Niedrig, eine Denkkette zu bauen und zu pflegen | Hoch, erfordert Orchestrierung, Weiterleitung und Zustandsverwaltung |
  | Token-Kosten | Vorhersehbar und pro Anfrage begrenzt | Variabel, kann zehn- bis fünfzehnmal höher liegen |
  | Latenz | Ein sequenzieller Durchlauf pro Anfrage | Jeder zusätzliche Agent fügt dem kritischen Pfad einen Modellaufruf hinzu |
  | Debugging | Eine Gedankenkette zu prüfen | Fehler können überall im Agenten-Netzwerk entstehen |
  | Am besten geeignet für | Fokussierte, domänenspezifische, repetitive Aufgaben | Komplexe bereichsübergreifende Probleme, die spezialisierte parallele Ausführung erfordern |
  | Wo du es in diesem Kurs baust | n8n-Workflow-Canvas | Mehrere AI-Agent-/Workflow-Komponenten; in weiterführenden Agenten-Inhalten behandelt |
> ➡️ Warum das wichtig ist: Alles, was du in Sprint 1, 2 und 3 gebaut hast, ist ein n8n-Single-Agent-Workflow. Zu verstehen, warum eine Single-Agent-Architektur für Contigos Anwendungsfall ausreicht, ist keine rein theoretische Übung. Es ist die Begründung für die architektonischen Entscheidungen, die du bereits getroffen hast.

![image]((notion-hosted file))

## Verständnis prüfen
> 💡 Contigos Entwicklungsteam erwägt, den aktuellen Single-Agenten für denselben Support-Anwendungsfall durch ein Vier-Agenten-System zu ersetzen. Was ist die wichtigste Frage, die vorab beantwortet werden sollte?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8a8da932-fd23-452e-a5e6-6becd7051a33


> 💡 Fazit:
  Der richtige Ausgangspunkt für jede Agenten-Architektur ist das einfachste System, dass das Problem zuverlässig löst. Ein einzelner Agent mit gut konfiguriertem Speicher, Abfrage und Tools bewältigt die Mehrheit der geschäftlichen Anwendungsfälle zu geringeren Kosten, mit geringerer Latenz und höherer Debugging-Freundlichkeit als eine Multi-Agenten-Alternative. Für Contigos Support-Agenten, wie er in diesem Kurs gebaut wurde, besteht keine solche Lücke. Der n8n-Single-Agent-Workflow mit Memory, Retrieval und Tools ist die richtige und ausreichende Architektur.
