# Abgerufene Chunks testen

Notion page: https://app.notion.com/p/Abgerufene-Chunks-testen-3779418319f3808bb5a2ef761239ebcc
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du testest simulierte Abrufergebnisse für verschiedene Suchanfragen, analysierst, wo die semantische Suche unpassende Chunks liefert, und erarbeitest gezielte Optimierungen für die Retrieval-Konfiguration.

## Das Szenario
Die RAG-Pipeline der Contigo GmbH ist konfiguriert, und die Grounding-Anweisung ist vorhanden. Das Compliance-Team hat den System-Prompt freigegeben. Das Entwicklungsteam befindet sich jetzt in der finalen Qualitätssicherungsphase, bevor der Agent in breiteres internes Testing geht.
Der QA-Engineer, der für die Abruf-Evaluierung zuständig ist, äußert Bedenken, die das Team bisher noch nicht systematisch angegangen ist. Die Abruf-Pipeline wurde mit sauberen, präzisen Queries getestet. Aber die Kunden von Contigos schreiben die Queries nicht wie die Entwickler. Sie beschreiben ihre Situationen in natürlicher Sprache, verwenden informelle Formulierungen, beziehen sich auf persönliche Umstände statt auf Policy-Kategorien und stellen manchmal Fragen, die semantisch nah am richtigen Inhalt liegen, ohne dessen Terminologie zu verwenden.
Die Frage des QA-Engineers ist nicht, ob die Pipeline für perfekte Queries funktioniert. Es geht darum, ob sie bei den Anfragen funktioniert, die echte Kunden tatsächlich stellen und was passiert, wenn das nicht der Fall ist.
Diese Evaluierung nutzt simulierte Abruf-Logs, um genau diese Frage zu beantworten. Die Logs zeigen, was Qdrant bei einer Reihe von Test-Queries aus Contigos Wissensdatenbank tatsächlich zurückgeliefert hat. Deine Aufgabe ist es, die Ergebnisse zu prüfen, erfolgreiche und fehlerhafte Abfragen zu identifizieren und die Ursachen dafür zu analysieren.
## Was die Abruf-Evaluation misst
Die Evaluation einer RAG-Pipeline erfordert, zwei unterschiedliche Qualitätsdimensionen zu trennen, die leicht miteinander verwechselt werden.
Abruf-Qualität: Misst, ob die Chunks, die von der Vektordatenbank zurückgegeben werden, für die Query des Nutzers relevant sind. Ein Abruf-Fehler tritt auf, wenn die zurückgegebenen Chunks nicht die Informationen enthalten, die zur Beantwortung der Frage erforderlich sind. Die Abruf-Qualität wird bewertet, bevor die Generierung beginnt.
Generierungsqualität: Misst, ob das Sprachmodell aus den Chunks, die es erhalten hat, eine korrekte, fundierte Antwort erzeugt hat. Ein Generierungsfehler kann selbst dann auftreten, wenn der Abruf erfolgreich ist.
Diese Lektion konzentriert sich ausschließlich auf die Abruf-Qualität.
Die zwei Dimensionen müssen getrennt voneinander bewertet werden: Einen Generierungsfehler als Abruf-Problem zu diagnostizieren oder umgekehrt führt zur falschen Lösung.
## Das Zieldokument
Die Wissensdatenbank enthält einen Abschnitt aus dem 2026 SME Loan Product Guide mit folgendem Inhalt.
Payment Difficulties and Restructuring Options: Die Kunden der Contigo GmbH, die vorübergehende Zahlungsschwierigkeiten haben, können eine Kreditrestrukturierungsvereinbarung beantragen. Dazu müssen die Anträge schriftlich an den zuständigen Kundenbetreuer des Kunden eingereicht werden. Zu den Restrukturierungsoptionen gehören eine Zahlungspause von bis zu drei Monaten, eine vorübergehende Reduzierung der monatlichen Ratenhöhe oder eine Verlängerung der Kreditlaufzeit um bis zu 24 Monate. Eine Restrukturierung ist einmal pro Kreditvertrag möglich. Zu beachten ist, dass die Kunden zum Zeitpunkt der Antragstellung nicht mehr als 60 Tage im Zahlungsrückstand sein dürfen.
Dies ist der Chunk, den dieAbruf-Pipeline für Queries zu Zahlungsschwierigkeiten, verpassten Zahlungen, Kreditrestrukturierung und finanziellen Schwierigkeiten zurückgeben sollte.
Die simulierten Abruf-Logs
Das QA-Team führte fünf Test-Queries gegen die Wissensdatenbank aus. Die Logs unten zeigen, welchen Chunk Qdrant für jede Query zurückgegeben hat.
![image]((notion-hosted file))

## Deine Aufgaben

> 🔥 Template: Contigo Retrieval Evaluation worksheet — erstelle eine Kopie (File → Make a copy) und verwende sie, um jedes der fünf Query-Ergebnisse zu klassifizieren, die Q3- und Q4-Fehler zu diagnostizieren und gezielte Verbesserungen vorzuschlagen.

#### Aufgabe A: Abruf-Erfolg und -Fehler bewerten
Prüfe alle fünf Query-Ergebnisse. Klassifiziere das Abruf-Ergebnis für jede Query als eines der folgenden:
- Success: Der richtige Chunk wurde mit ausreichender Ähnlichkeit zurückgegeben, um eine korrekte Antwort zu unterstützen
- Partial success: Ein angrenzender oder verwandter Chunk wurde zurückgegeben, der einige relevante Informationen enthält, aber zentrale Inhalte vermissen lässt
- Failure: Ein falscher oder irrelevanter Chunk wurde zurückgegeben
Schreibe für jeden Fehler oder Teilerfolg ein bis zwei Sätze, die erklären, warum die semantische Abweichung aufgetreten ist. Berücksichtige, wie das Vokabular der Query im Vergleich zum Vokabular des Ziel-Chunks aussieht und ob der zurückgegebene Chunk oberflächliche Ähnlichkeit mit der Query teilt, ohne ihrer Absicht zu entsprechen.
### Aufgabe B: Die Abruf-Fehler diagnostizieren
Die Queries 3 und 4 gaben falsche Chunks zurück, obwohl sie semantisch mit dem Zielinhalt verwandt waren. Diagnostiziere bitte jeden Fehler konkret.
Erkläre für Query 3, warum die Formulierung „take a break from paying“ semantisch weit vom Vokabular des Ziel-Chunks entfernt ist, und identifiziere, welcher Begriff in der Query den Abruf möglicherweise in Richtung des Kreditantragsabschnitts gezogen hat.
Erkläre für Query 4, warum eine Business-Kontext-Query über ein „difficult quarter“ und „flexibility“ möglicherweise einen höheren Ähnlichkeitswert für den Abschnitt zu Kriterien für die Kreditwürdigkeit erzeugt hat als für den Abschnitt zu Zahlungsschwierigkeiten.
### Aufgabe C: Abruf-Verbesserungen vorschlagen
Schlage für jede der drei nicht erfolgreichen Queries eine konkrete Verbesserung vor, um den Abruf-Fehler zu adressieren. Deine Vorschläge müssen aus den folgenden Kategorien stammen:
- Query-Rewriting: Die Query des Kunden in standardisierte Terminologie reformulieren, bevor sie die Vektordatenbank erreicht.
- Verbesserung der Chunk-Metadaten: Metadatenfelder zum Ziel-Chunk hinzufügen, die seine Abrufbarkeit für unterschiedliche Query-Formulierungen verbessern.
- Erweiterung der Wissensdatenbank: Ergänzende Inhalte zur Wissensdatenbank hinzufügen, die die Vokabularlücke zwischen Kundenformulierung und Dokumentterminologie überbrücken.
Erkläre für jeden Vorschlag konkret, wie die Verbesserung den diagnostizierten Fehler adressiert.

[toggle] Denke über Folgendes nach …
  🔽 Checkpoint 1: Ähnlichkeitswerte verstehen - Wenn zwei von drei abgerufenen Chunks relevant sind und einer nicht, liegt das Problem meist an der Grenze zwischen den Inhaltsabschnitten. Überlege, ob der irrelevante Chunk genug oberflächliche Terminologie mit der Query teilt, um hoch zu scoren, obwohl er kontextuell falsch ist.
  🔽 Checkpoint 2: Query 3 diagnostizieren - Eine vage Query erzeugt einen unpräzisen Vektor, weil das Embedding-Modell wenig semantischen Inhalt hat, mit dem es arbeiten kann. Query-Rewriting bedeutet, den spezifischen Produktnamen, den Bedingungstyp und den Kontext hinzuzufügen, den der Kunde impliziert, aber nicht ausgesprochen hat, ohne zu verändern, wonach er tatsächlich gefragt hat.
  🔽 Checkpoint 3: Query 4 diagnostizieren - Wenn zwei Dokumentversionen ähnliche Terminologie teilen, kann semantische Ähnlichkeit allein nicht zwischen ihnen unterscheiden. Der Payload-Index, den du während der Einrichtung erstellt hast, ist der Mechanismus, der den Abruf ermöglicht, das nach einem spezifischen Metadatenfeldwert filtert, statt sich allein auf den Ähnlichkeitswert zu verlassen.
  🔽 Checkpoint 4: Query 5 bewerten - Wenn die Fallback-Formulierung bei einer eindeutig in-scope Query ausgelöst wird, funktioniert die Abruf-Pipeline korrekt. Sie hat nichts Relevantes gefunden, das sie zurückgeben kann. Das Problem ist nicht der Abruf, sondern die Abdeckung. Überlege, ob die Wissensdatenbank überhaupt ein Dokument enthält, das dieses Thema adressiert.
## Verständnis prüfen
Frage 1
>  Contigos QA-Team schrieb fünf Test-Queries basierend auf erwarteten Kundenformulierungen. Echte Kunden-Queries in Produktion verwenden Sprache, die das Team nicht vorhergesehen hat. Welcher Prozess erweitert das Abruf-Testset am effektivsten mit Produktionsdaten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/908c6151-302c-45e1-a355-da072b3e5222

Frage 2
>  Die Contigo evaluiert, ob ein Query-Rewriting-Schritt vor dem Abruf hinzugefügt werden soll. Die Wissensdatenbank ist relativ stabil, und die Kunden erwarten schnelle Antwortzeiten. Welches Kriterium bestimmt am genauesten, ob Query-Rewriting für dieses spezifische Deployment gerechtfertigt ist?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/97bd716f-722f-4ccc-94d8-d2217ed9f4cb


> 💡 Takeaway: 
  Die Abruf-Qualität kann nicht von einer funktionierenden Pipeline abgeleitet werden. Sie muss systematisch über die Bandbreite der Formulierungen hinweg getestet werden, die echte Nutzer tatsächlich produzieren werden.
  Ein System, das von Entwicklern geschriebene Queries korrekt abruft, aber von den Kunden geschriebenen Queries scheitert, kann kein zuverlässiges System sein. Die Lücke zwischen diesen zwei Query-Stilen ist der Ort, an dem die meisten Abruf-Fehler auftreten.
