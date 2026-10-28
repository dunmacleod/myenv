# Context Drift und Content Exhaustion

Notion page: https://app.notion.com/p/Context-Drift-und-Content-Exhaustion-3779418319f380bc9051d53cee09bb6a
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du verstehst, wie lang laufende Agent-Sessions an Qualität verlieren, wenn sich das Context Window füllt. Du siehst, warum ein großes Context Window dieses Problem nicht löst. Und du verstehst, wie die Buffer-Window-Memory-Konfiguration aus Sprint 1 in die größere Landschaft der Context-Management-Strategien passt, die in Produktivumgebungen eingesetzt werden.

## Der Mythos vom unendlichen Kontext
Der Agent von Contigo GmbH führt Multi-Turn-Gespräche mit Kunden, die bei komplexen Kreditbewertungen oder Compliance-Sessions auf zwanzig bis dreißig Austausche anwachsen können. Bei jedem Turn kommt mehr ins Context Window: Gesprächsverlauf aus dem Buffer Window Memory Node, abgerufene Dokument-Chunks aus der Qdrant-Wissensdatenbank, Tool-Outputs aus dem Loan-Status-Lookup und dem Calculator. Über eine lange Session hinweg wird diese Ansammlung beträchtlich.
Eine verbreitete Annahme ist, dass ein Modell mit großem Context Window dieses Problem vollständig löst. Das stimmt nicht. Forschung zeigt konsistent, dass die Reasoning-Performance mit steigender Input-Länge abnimmt, oft schon lange bevor das angegebene Context Limit erreicht wird. Ein Modell, das einen 200.000-Token-Prompt verarbeitet, reasont nicht so gut wie dasselbe Modell bei einem 10.000-Token-Prompt. Das gilt selbst dann, wenn beide innerhalb des technischen Limits liegen.
Diese Verschlechterung hat einen Namen: Context Drift. Und operativ gehört sie zu den häufigsten und teuersten Fehlermodi in produktiven Agent-Deployments.
## Wie sich Context Drift zeigt
Je voller das Context Window wird, desto stärker verteilt sich die Aufmerksamkeit des Modells über einen immer größeren Input. Dabei zeigen sich drei spezifische Fehlermuster.
- Degraded Reasoning: Der Agent beginnt, seinen System Prompt oder die aktuelle Anweisung des Kunden zu ignorieren. Stattdessen dominiert älterer Inhalt den Kontext rein volumenmäßig. Wechselt ein Kunde vom Thema Privatkredite zu SME-Produkten, stützt der Agent seine Logik manchmal trotzdem weiterhin auf Parameter aus dem Privatkreditbereich. Der Grund: Dieser Inhalt nimmt mehr Platz im Kontext ein als die neue Anfrage.
- Tool Selection Errors: Ein Agent, der bei Turn 5 noch korrekt geroutet hat, kann bei Turn 25 das falsche Tool aufrufen. Der Grund: Die Tool-Beschreibungen werden vom Volumen des angesammelten Verlaufs überlagert. Die Aufmerksamkeit des Modells für die Routing-Anweisungen verdünnt sich, je größer der Kontext wird. Das hängt direkt mit den Fehlermodi Context Dilution und Tool Bloat zusammen, die in einer früheren Lektion behandelt wurden.
- Cost- und Latency-Spikes: Jeder Reasoning-Schritt verarbeitet das gesamte Context Window. Eine Session, die über dreißig Turns von 8.000 auf 80.000 Tokens wächst, erhöht die Tokenkosten jedes einzelnen Schritts um den Faktor zehn und lässt die Latenz proportional mitwachsen. Für Contigos Deployment über Hunderte gleichzeitige Kundensessions hinweg ist diese Kostenvervielfachung operativ erheblich.
![image]((notion-hosted file))

## Wie deine Sprint-1-Konfiguration das adressiert
Der konfigurierte Buffer Window Memory Node arbeitet mit einem Sliding-Window-Ansatz. Er behält nur die letzten K Nachrichtenpaare im aktiven Kontext und verwirft alles Ältere. Das begrenzt direkt, wie viel Gesprächsverlauf bei jedem Prompt-Turn injiziert wird.
Die Window Size, die du gewählt hast, war ein bewusster Trade-off. Ein zu kleines Window verwirft wichtigen Kontext zu früh. Die Fallreferenz eines Kunden aus Turn 1 kann bei Turn 7 schon außerhalb des aktiven Windows liegen. Ein zu großes Window führt einen Kontext-Druck wieder ein, weil es mehr Verlauf behält, als für den aktuellen Turn wirklich nötig ist.
Contigos typische Support-Gespräche sind Produktfragen, Eligibility-Anfragen und Status-Checks. Für diese Fälle ist die von dir konfigurierte Window Size der richtige und ausreichende Mechanismus. Sie hält den aktiven Kontext fokussiert, ohne die Gesprächskontinuität zu verlieren, die den Agenten überhaupt erst nützlich macht.
## Vier Strategien für das Context-Management
Deine Sliding-Window-Konfiguration ist eine von vier Strategien, mit denen sich Kontext in Produktivumgebungen managen lässt. Die anderen drei zu kennen, ordnet deinen aktuellen Build in die größere Landschaft ein und bereitet dich auf komplexere Deployments vor.
#### Strategie 1: Sliding Window (deine aktuelle Umsetzung)
- Nur die letzten N Turns werden vollständig behalten. Ältere Turns werden verworfen. Der System Prompt und die aktuellen Task-Anweisungen sind immer präsent, egal wie viele Turns vergangen sind. Einfach zu konfigurieren und direkt über deinen Buffer Window Memory Node umgesetzt.
- Einschränkung: Wichtige Informationen vom Anfang einer langen Session, etwa eine Fallreferenz oder eine genannte Präferenz, können außerhalb des Windows landen und komplett verloren gehen.
#### Strategie 2: Kompression und Zusammenfassung
- Statt rohe Tool-Outputs und vollständige Gesprächstranskripte zu behalten, komprimiert das System älteren Inhalt. Eine Serie von fünf Austauschen zur Kreditwürdigkeit wird zu zwei Sätzen zusammengefasst, die das Ergebnis festhalten, ohne das ausführliche Hin und Her. Die Zusammenfassung ersetzt den rohen Verlauf, hält das Context Window schlank und bewahrt trotzdem den wesentlichen Inhalt.
- Einschränkung: Zusammenfassen braucht einen zusätzlichen Modellaufruf und kostet dadurch Zeit und Geld. Die Zusammenfassung ist eine Annäherung, bei der einzelne Details verloren gehen können.
#### Strategie 3: Token Budgeting
- Feste Token-Kontingente sind für System Prompt, Tool Schemas und Generation Headroom reserviert. Verlauf und abgerufener Inhalt füllen nur das, was übrig bleibt. Nähert sich das Budget der Grenze, wird zuerst der Inhalt mit der niedrigsten Priorität verworfen. Meist sind das ältere Gesprächsturns, nicht abgerufene Chunks oder System-Anweisungen.
- Einschränkung: Erfordert sorgfältige Kalibrierung. Ein zu knappes Budget verwirft wichtigen Kontext. Ein zu großzügiges Budget führt Kontext-Druck wieder ein.
#### Strategie 4: Tiered Memory
- Jüngere Turns liegen in einem schnellen Working Memory, vergleichbar mit deinem Buffer Window Memory Node. Ältere Turns werden in einem Vector Store archiviert und nur abgerufen, wenn sie semantisch relevant für die aktuelle Anfrage sind. Das aktive Context Window bleibt klein. Der vollständige Verlauf bleibt zugänglich, ohne dauerhaft Platz im Prompt zu belegen.
- Einschränkung: Deutlich komplexer umzusetzen. Braucht einen persistenten Vector Store, der für Long-Term-Memory-Retrieval konfiguriert ist. Das wäre eine andere Nutzung von Qdrant als die Wissensdatenbank-Konfiguration aus Sprint 2.
Contigos Support-Use-Case besteht aus kurzen bis mittellangen, fokussierten Gesprächen. Kontinuität innerhalb der Session ist dabei wichtig, ein Verlauf über mehrere Sessions hinweg aber nicht nötig. Für diesen Fall ist Sliding Window die richtige und ausreichende Strategie.
## Verständnischeck
>  Ein Contigo-Agent bearbeitet eine 25-Turn-Compliance-Session bis Turn 15 korrekt, beginnt dann aber ab Turn 16 seine Grounding-Anweisung zu ignorieren und erfindet bis Turn 25 regulatorische Zahlen. Während der Session wurden keine Konfigurationsänderungen vorgenommen. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b4e0fe40-67ac-4a34-895d-ffd339abca8e


> 💡 Fazit:
  Der Kontext ist ein Budget und kein Lagerhaus. Jeder Token, der in den Prompt injiziert wird, konkurriert um die Aufmerksamkeit des Modells. Die Buffer-Window-Memory-Konfiguration, die du in Sprint 1 gebaut hast, ist dein zentraler Mechanismus für dieses Budget. Sie hält den aktiven Kontext auf das fokussiert, was der aktuelle Turn wirklich braucht.
  Die drei zusätzlichen Strategien aus Produktivumgebungen zu kennen, ordnet deinen aktuellen Build realistisch ein. Er ist die richtige und ausreichende Architektur für Contigos Support-Use-Case, und gleichzeitig der Ausgangspunkt für anspruchsvolleres Context-Management, sobald die Deployment-Größe es verlangt.
