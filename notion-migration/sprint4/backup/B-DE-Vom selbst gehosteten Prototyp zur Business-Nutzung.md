# Vom selbst gehosteten Prototyp zur Business-Nutzung

Notion page: https://app.notion.com/p/Vom-selbst-gehosteten-Prototyp-zur-Business-Nutzung-3789418319f380a6beb0c485db48fab7
Backed up before n8n migration

> 💡 Das lernst du in dieser Lektion: Du verstehst die vier Infrastruktur-Dimensionen, die einen lokal laufenden Flowise-Prototyp von einem produktionsreifen Deployment unterscheiden. Und du weißt, warum dieser Übergang mehr braucht als nur ein Canvas auf einen Server zu verschieben.

## Die Ausgangslage
Meridians Agent läuft. Das Canvas ist sauber. Der Sicherheits-Stack ist verstanden. Der End-to-End-Test ist bestanden. Die Präsentation wird gerade vorbereitet. Auf dem Laptop eines Entwicklers unter localhost:3000 verarbeitet der Agent Anfragen zuverlässig, ruft präzise Daten aus Qdrant ab und fängt sich elegant ab, wenn der HTTP-Node ausfällt.
Morgen will Meridians CTO den Agenten für das gesamte Consulting-Team freischalten, 43 Personen an den Standorten Berlin, Warschau und Prag. Sie alle sollen den Agenten über den ganzen Arbeitstag hinweg gleichzeitig nutzen können. Schon wenige Stunden nach diesem Rollout wird die aktuelle Architektur versagen. Der Grund liegt nicht in der Logik des Agenten. Der Grund liegt in der Infrastruktur darunter. Sie wurde nie dafür gebaut, gleichzeitige Nutzer zu bewältigen, Zustände dauerhaft über Server-Neustarts hinweg zu halten oder die Observability-Anforderungen eines Systems zu erfüllen, das diagnostiziert werden muss, wenn am Montagmorgen um 9 Uhr etwas schiefläuft.
Das ist das Localhost-Problem. Genau daran scheitern die meisten KI-Agenten-Projekte beim Übergang vom Prototyp zur Produktion.
## Dimension 1: Hosting und skalierbare Infrastruktur
Die aktuelle Flowise-Installation läuft als einzelner Docker-Container auf einer einzigen Maschine. Für die Session-Speicherung nutzt sie eine SQLite-Datenbank, für die Vektor-Speicherung einen lokalen Qdrant-Docker-Container. Beides funktioniert einwandfrei, solange ein einzelner Entwickler isoliert testet. Keins von beidem hält den Anforderungen eines Multi-User-Produktivbetriebs stand.
- Datenbank-Migration: SQLite kann gleichzeitige Schreibzugriffe aus mehreren parallelen Sessions nicht zuverlässig verarbeiten. Der Wechsel zu PostgreSQL bringt gleichzeitigen Zugriff, Connection Pooling und Transaktionsintegrität, die ein Multi-User-Deployment braucht.
- Persistenz des Vector Store: Der lokale Qdrant-Container speichert Vektoren auf einer einzigen Maschine. Eine verwaltete Qdrant-Cloud-Instanz sorgt dafür, dass die Wissensdatenbank unabhängig davon verfügbar bleibt, welche Server-Instanz eine Anfrage bearbeitet, und dass sie Docker-Neustarts übersteht.
- Container-Deployment: Läuft Flowise hinter einem Load Balancer, lässt sich das Deployment horizontal skalieren. Bei wachsender Nutzerzahl kommen einfach weitere Server-Instanzen hinzu, ohne dass sich an der Anwendungs- oder Canvas-Logik etwas ändert.
## Dimension 2: Observability und Monitoring
Fällt ein Agent im Live-Betrieb am Montagmorgen um 9 Uhr aus, muss die Ursache bis 9:30 Uhr gefunden sein. Auf einer lokalen Entwicklungsinstanz öffnet ein Entwickler dafür die Flowise-Ausführungsspur und liest sie manuell durch. Bei 43 gleichzeitigen Nutzern, die täglich Hunderte Spuren erzeugen, ist manuelle Prüfung keine Option mehr.
- Strukturierte Telemetrie: Jeder Agenten-Aufruf muss einen strukturierten Log-Eintrag erzeugen, mit Trace-ID, Prompt, abgerufenen Chunks, Tool-Aufrufen, Antwort und Latenz, der sich in eine Observability-Plattform exportieren lässt. Flowise unterstützt dafür die Integration mit LangSmith, Langfuse und OpenTelemetry-kompatiblen Plattformen.
- Metrik-Dashboards: Monitoring in Produktion braucht automatisierte Dashboards, die Antwortzeit, Token-Kosten pro Session, Fehlerraten des HTTP-Node und Retrieval-Qualität im Blick behalten. Verlässt eine Metrik den definierten Bereich, feuert ein Alert, bevor das Problem die Nutzer erreicht.
- Kontinuierliche Evaluation: Eine automatisierte Evaluationspipeline läuft gegen eine standardisierte Benchmark-Suite, sobald sich System-Prompt, Tool-Beschreibungen oder Document Store ändern. So fallen Performance-Regressionen auf, bevor sie Anfragen in Produktion betreffen.
## Dimension 3: Sicherheit im Produktionsmaßstab
Der Defence-in-Depth-Stack, also Input-Validierung, Least-Privilege-Ausführung, Output-Filterung und Audit-Logging, wurde für ein Deployment mit einer einzigen Instanz entworfen. Im Produktionsmaßstab braucht jede Ebene eine Umsetzung auf Infrastrukturebene.
- Secret Management: Der Gemini-API-Key, der aktuell im Credentials Manager von Flowise liegt, muss in einen dedizierten Secrets Manager migriert werden. Dort wird er im Ruhezustand verschlüsselt, rollenbasiert zugriffsbeschränkt und automatisch rotiert.
- Netzwerk-Isolation: Agenten, die in Produktion mit vertraulichen Kundendaten arbeiten, sollten innerhalb einer Virtual Private Cloud laufen. Das ist eine Netzwerkgrenze, die externen Zugriff auf interne Dienste verhindert und einschränkt, welche Systeme der Agent überhaupt erreichen kann.
- Identity and Access Management: Das aktuelle Setup mit einem einzigen Credential muss durch ein richtiges IAM-System ersetzt werden. Dort wird die Identität jedes Consultants geprüft, Berechtigungen werden auf Tool-Ebene durchgesetzt, und jede Aktion lässt sich im Audit-Log eindeutig zuordnen.
## Dimension 4: Governance und Compliance
Meridians Agent verarbeitet vertrauliche operative Kundendaten aus drei EU-Rechtsräumen. Daraus entstehen regulatorische Pflichten, die die Prototyp-Architektur nicht abdeckt.
- Datenresidenz: Alle Daten, die der Agent verarbeitet, müssen innerhalb der EU bleiben. Um das zu erfüllen, braucht es verwaltete Infrastruktur in Frankfurt oder Amsterdam statt eines Entwickler-Laptops.
- Audit Trails: Jeder Tool-Aufruf, jede Flow-State-Änderung und jede Routing-Entscheidung muss einen fälschungssicheren Log-Eintrag erzeugen, den man im Bedarfsfall abrufen und einer Aufsichtsbehörde vorlegen kann. Die Flowise-Ausführungsspur ist ein Debugging-Werkzeug.
- Incident Response: Ein Produktiv-Deployment braucht einen dokumentierten Prozess für den Fall, dass der Agent eine falsche oder schädliche Ausgabe produziert. Dazu gehört, wer benachrichtigt wird, wie der Vorfall dokumentiert wird und wie das Rollback-Verfahren aussieht.
## Die Lücke zwischen Prototyp und Produktion
[TABLE]
  | Dimension | Aktueller Stand | Anforderung in Produktion |
  | Datenbank | SQLite: eine einzelne Instanz | PostgreSQL: gleichzeitiger Zugriff, Connection Pooling |
  | Vector Store | Lokaler Qdrant-Docker-Container | Verwaltete Qdrant-Cloud-Instanz |
  | Hosting | Einzelner Docker-Container | Load-balanced, horizontal skalierbar |
  | Observability | Manuelle Prüfung der Ausführungsspur | Strukturierte Telemetrie + automatisierte Alerts |
  | Secret Management | Flowise Credentials Manager | Dedizierter Secrets Manager mit Rotation |
  | Identity | Einzelner API-Key | IAM mit Authentifizierung pro Nutzer |
  | Audit Trail | Flowise-Ausführungsspur | Fälschungssicheres strukturiertes Log |
  | Datenresidenz | Entwickler-Laptop | EU-gehostete verwaltete Infrastruktur |
![image]((notion-hosted file))

## Verständnischeck
>  Meridian bringt den Flowise-Agenten auf einen Cloud-Server, ohne die SQLite-Datenbankkonfiguration zu ändern. Innerhalb von zwei Stunden, in denen das gesamte Consulting-Team gleichzeitig zugreift, werden die Session-Daten beschädigt, und mehrere Consultants bekommen Antworten mit Fragmenten aus den Gesprächsverläufen anderer Consultants. Was ist die zutreffendste Erklärung?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/6f20925d-9839-4fb9-b0f3-e9dc4ac53d65


> 💡 Fazit:
  Den Agenten zu bauen macht zwanzig Prozent der Arbeit aus. Die restlichen achtzig Prozent stecken in der Infrastruktur drumherum. Ein Prototyp unter localhost:3000 zeigt, dass die Logik des Agenten funktioniert. Er zeigt nicht, dass sich das System mit echten Kundendaten, echten gleichzeitigen Nutzern und echten regulatorischen Pflichten betrauen lässt.
  Diese Lektion bildet genau diese vier Infrastruktur-Dimensionen ab. Sie zu verstehen, das unterscheidet einen Entwickler, der einen Agenten bauen kann, von einem, der ihn auch in Produktion bringen kann.
