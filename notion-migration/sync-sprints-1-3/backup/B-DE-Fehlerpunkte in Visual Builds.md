# Fehlerpunkte in Visual Builds

Notion page: https://app.notion.com/p/Fehlerpunkte-in-Visual-Builds-3789418319f3800190efff70943ef15c
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du verstehst, wo und warum Agentflow-v2-Architekturen scheitern und wie sich Fehler in einem Node über den gesamten Graphen fortpflanzen.

## Ausgangslage
Meridians Agent lief zwei Wochen lang fehlerfrei durch die internen Tests. Zwei Tage nach dem Rollout für das gesamte Consulting-Team fing er an zu scheitern. Die Canvas sah in beiden Fällen identisch aus. Der Unterschied lag in der Vielfalt und dem Volumen echter Anfragen, die gleichzeitig jede Ecke der Konfiguration trafen. Visuelle Builder verstecken Komplexität. Solange alles läuft, ist das ein Produktivitätsgewinn. Sobald etwas kaputtgeht, sieht das anders aus. Der Fehler sitzt dann oft nicht im Node selbst, sondern in den Verbindungen dazwischen, die auf der Canvas trivial wirken. Deshalb ist es wichtig zu verstehen, wo Agentflow-v2-Architekturen strukturell anfällig sind. Sprint 3 bringt schließlich Loops, Iterationen und Freigabe-Checkpoints in Meridians Canvas und macht das Verständnis nur noch relevanter.
## Die vier Fehlerquellen
### Fehlerquelle 1: Prompt-Fehler
Der System-Prompt bestimmt, wie sich der Agent verhält. Ist er unklar oder unvollständig, füllt der Agent die Lücke mit Geminis allgemeinen Trainingsdaten. Die Antwort klingt autoritativ. Sie stimmt aber nicht. Es wird kein Fehler ausgelöst. Der Agent liefert einfach eine selbstbewusste, falsche Antwort, die genauso aussieht wie eine richtige.
### Fehlerquelle 2: Retrieval-Fehler
Der Document Store liefert Chunks, die inhaltlich nah am Thema der Anfrage liegen. Diese Chunks enthalten aber nicht die Information, die für eine korrekte Antwort nötig wäre. Der Agent Node hält das für ausreichend und baut die Antwort auf dem falschen Material auf. Kein Node stürzt dabei ab. Der Fehler ist semantischer Natur und fällt erst auf, wenn man die Antwort mit dem tatsächlichen Dokumenteninhalt vergleicht.
Ein verwandtes Problem tritt auf, wenn der Qdrant-Vektorspeicher nach einem Update von Meridians Playbooks nicht neu “upserted” wird. Dann greift der Agent mit voller Überzeugung auf veraltete Inhalte zurück, und die Canvas zeigt keinerlei Hinweis darauf, dass etwas nicht stimmt.
### Fehlerquelle 3: Tool- und HTTP-Fehler
Liefert der HTTP Node einen Fehler statt Daten, erfindet Agent Node B ohne explizites Failure Handling entweder einen Status oder schreibt einen falschen Wert in den Flow State. Der Flow State ist ein Key-Value-Store zur Laufzeit, auf den alle Nodes innerhalb einer Ausführung zugreifen. Ein erfundener Wert in $flow.state.status_response steht sofort jedem Node zur Verfügung, der im weiteren Verlauf auf diesen Key zugreift. Die Kontamination ist strukturell und passiert sofort.
In Sprint 3 übernimmt der Loop Node die Retry-Logik für fehlgeschlagene HTTP-Calls. Der Parameter Max Loop Count legt fest, wie oft die Loop innerhalb eines einzelnen Workflow-Runs maximal ausgeführt werden darf, und schützt so vor Endlosschleifen. Der Standardwert liegt bei 5. Fehlt beim Erreichen des Limits ein konfigurierter Exit-Pfad, bricht die Loop ab, ohne eine sinnvolle Antwort zurückzugeben.
### Fehlerquelle 4: Memory-Fehler
Ein Context Bleed entsteht, wenn Details aus einer früheren Account-Diskussion in eine spätere überschwappen, etwa weil Action Items falsch zugeordnet oder Einschränkungen aus einem Engagement auf ein anderes übertragen werden. Je länger die Conversation läuft, desto wahrscheinlicher wird das, und die Routing-Entscheidungen werden schlechter.
## Wie Fehler sich fortpflanzen
Fehler bleiben selten auf den Node beschränkt, in dem sie entstehen. Ein Retrieval-Fehler erzeugt falschen Content, mit dem Agent Node A weiterarbeitet. Diese Antwort landet im Session Memory. Im nächsten Turn wird sie als gesicherte Tatsache eingespeist. Jeder Schritt verstärkt den Fehler zusätzlich. Deshalb sind Fehler in Produktion oft schwerwiegender, als isolierte Tests vermuten lassen. Testet man einzelne Nodes nur mit sauberen Inputs, bleiben die Fehlerarten unsichtbar, die erst durch das Zusammenspiel entstehen.
![image]((notion-hosted file))

## Verständnischeck
>  Meridians Agent ruft einen veralteten Policy-Chunk ab und erzeugt daraus eine Antwort. Der Agent Node speichert dies im Session Memory. Was passiert im nächsten Turn?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a65adbc7-37b9-45c2-960b-5ed2860ae044

> 💡 Fazit:
  Agentflow-v2-Builds scheitern an den Verbindungen zwischen den Nodes. Ein Prompt-Fehler produziert selbstbewusste, falsche Antworten. Ein Retrieval-Fehler vergiftet das Context Window. Ein Tool-Fehler löst Loops oder eine Kontamination des Flow State aus.
  Ein Memory-Fehler verstärkt all das über mehrere Turns hinweg. Diese vier Fehlerkategorien zu erkennen, ist das Diagnose-Framework für Sprint 3. Dort eröffnen Loops, Iterationen und Freigabe-Checkpoints neue Wege, wie jede einzelne davon auftreten kann.
