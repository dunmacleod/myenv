# Chunking-Strategien

Notion page: https://app.notion.com/p/Chunking-Strategien-3779418319f38090b347d86380564587
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du wählst zwischen Fixed-Size- und semantischen Chunking-Strategien für zwei unterschiedlich strukturierte Dokumenttypen. Jede Entscheidung begründest du anhand der Dokumentstruktur sowie der Queries, die das System unterstützen muss.

## Das Szenario
Das Entwicklungsteam der Contigo GmbH hat die Dokumentauswahl finalisiert und die Dateien für die Ingestion vorbereitet. Bevor ein Dokument in Qdrant gelangt, muss das Team noch eine weitere grundlegende Entscheidung treffen: Wie soll jedes Dokument gechunkt werden?
Der Data Engineer des Teams stellt die Frage in einer Review-Session. Zwei Dokumente stehen bereit zum Einpflegen: der 2026 SME Loan Product Guide und die EU Consumer Credit Directive Summary. Beide sind PDFs. Beide enthalten Finanz- und Regulierungsinhalte. Aber ihre internen Strukturen sind völlig unterschiedlich, und dieselbe Chunking-Strategie auf beide anzuwenden, wäre derselbe Fehler wie generische Verarbeitung anzuwenden.
Das Team muss für jedes Dokument einen Chunking-Ansatz definieren, der seine tatsächliche Struktur, die Arten von Queries, die es unterstützen muss, und die Trade-offs zwischen Chunk-Größe, Overlap und Retrieval-Präzision widerspiegelt.
## Was ist Chunking?
Chunking ist der Prozess, große Dokumente in kleinere, handhabbare Teile aufzuteilen, bevor sie in einer Wissensdatenbank gespeichert werden. Da Sprachmodelle ein begrenztes Context Window haben, können sie ein ganzes Dokument nicht auf einmal verarbeiten. Chunking teilt Inhalte in Segmente auf, die klein genug sind, um als einzelne Vektoren eingebettet und selektiv anhand ihrer Relevanz für eine Query abgerufen zu werden.
Die Größe und Grenzen jedes Chunks wirken sich direkt auf die Abfrage-Qualität aus
- Zu große Chunks verwässern das semantische Signal
- Zu kleine Chunks verlieren den Kontext, der nötig ist, um Fragen korrekt zu beantworten
Gutes Chunking respektiert die natürliche Struktur des Dokuments.
## Die zwei Chunking-Strategien
Bevor du mit der Aufgabe beginnst, prüfe die zwei primären verfügbaren Ansätze.
- Fixed-Size-Chunking: Naives Splitting - Text wird in Segmente mit einer definierten Token- oder Zeichenzahl aufgeteilt, mit einem definierten Overlap zwischen aufeinanderfolgenden Chunks. Die Splits erfolgen an der definierten Grenze, unabhängig davon, ob sie mitten im Satz, mitten in einer Klausel oder an einer natürlichen Inhaltsgrenze liegen. Dieser Ansatz ist schnell zu konfigurieren und konsistent in der Output-Größe, riskiert aber, Kontext an willkürlichen Stellen zu brechen.
Fixed-Size-Chunking funktioniert hervorragend, wenn der Quellinhalt bereits fein untergliedert vorliegt. Kurze, eigenständige Einträge nehmen keinen Schaden, ganz egal, wo die Grenze verläuft.
- Semantisches Chunking: Strukturbewusstes Splitting - .Das System teilt den Text an natürlichen Inhaltsgrenzen auf: bei Überschriften, Absätzen, Themenwechseln oder am Ende einer einzelnen Regelung. Diese Splits folgen der inneren Struktur des Dokuments, statt ihm starre Größenlimits aufzuzwingen. Dieser Ansatz erfordert zwar mehr Konfiguration und erzeugt unterschiedlich große Chunks, bewahrt aber den Zusammenhang komplexer, eng verknüpfter Inhalte.
Ein semantisches Chunking ist notwendig, wenn der Quellinhalt mehrteilige Argumente, querverwiesene Klauseln oder strukturierte Abschnitte enthält, bei denen ein Split mitten im Inhalt die Bedeutung des abgerufenen Chunks zerstören würde.
## Die zwei Dokumente
Dokument 1: 2026 SME Loan Product Guide - Ein 5-seitiges Dokument, das in klar markierte Abschnitte organisiert ist, einen pro Kreditprodukt, jeweils mit Unterabschnitten zu Kriterien für die Kreditwürdigkeit, Zinssatzstrukturen, Antragsanforderungen und Rückzahlungsbedingungen. Inhalte innerhalb jedes Abschnitts sind eng miteinander verknüpft. Die Kriterien für die Kreditwürdigkeit eines Produkts verweisen auf die Zinssatzstruktur im selben Abschnitt. Die Rückzahlungsbedingungen verweisen auf die Antragsanforderungen. Splits über Unterabschnittsgrenzen hinweg würden Chunks erzeugen, die syntaktisch vollständig, aber semantisch unvollständig sind.
Erwartete Query-Typen:
- Produktspezifische Fragen
- Eignungsprüfungen
- Zinsvergleiche
- Nachschlagen von Antragsanforderungen
Dokument 2: EU Consumer Credit Directive Summary - Eine zweiseitige interne Zusammenfassung, die von Contigos Legal-Team erstellt wurde. Das Dokument ist als nummerierte Liste von dreizehn Pflichten organisiert, die jeweils in ein bis drei Sätzen formuliert sind. Jede Pflicht ist eigenständig, verweist nicht auf die anderen und benötigt keinen umgebenden Kontext, um verstanden zu werden. Das Dokument hat keine Querverweise, keine verschachtelten Klauseln und keine miteinander verbundenen Abschnitte.
Erwartete Query-Typen:
- Nachschlagen bestimmter Pflichten
- Prüfungen von Compliance-Anforderungen
- Queries zu regulatorischen Schwellenwerten
## Deine Aufgaben

> 🔥 Template: Contigo Chunking Strategy worksheet — erstelle eine Kopie (File → Make a copy) und verwende sie, um deine Strategiewahl für jedes Dokument festzuhalten, die Parameter zu konfigurieren und den Transcript Case durchzuarbeiten.

#### Aufgabe A: Weise die Chunking-Strategie zu und begründe sie
Bestimme für jedes der zwei Dokumente, welche Chunking-Strategie am besten geeignet ist (Fixed-Size oder semantisch), und schreibe zwei bis drei Sätze, die deine Wahl begründen. Deine Begründung sollte auf die Struktur des Dokuments und die Arten von Queries verweisen, die es unterstützen muss, nicht nur auf die allgemeinen Eigenschaften der Strategie.
### Aufgabe B: Konfiguriere die Parameter
Für das Dokument, für das du Fixed-Size-Chunking gewählt hast, schlage eine konkrete Chunk-Größe in Tokens und einen Overlap-Wert vor. Begründe beide Zahlen. Berücksichtige die durchschnittliche Länge eines einzelnen Eintrags im Dokument, das Risiko, eine bedeutungsvolle Einheit über zwei Chunks hinweg zu teilen, und die Kosten, redundante Inhalte durch Overlap zu speichern.
Für das Dokument, für das du semantisches Chunking gewählt hast, identifiziere das strukturelle Merkmal, das du als Chunking-Grenze verwenden würdest, und erkläre, warum diese Grenze die Bedeutung des Inhalts für die erwarteten Query-Typen bewahrt.
### Aufgabe C: Bewerte einen Grenzfall
Ein drittes Dokument wurde der Ingestion-Warteschlange hinzugefügt: ein Transcript einer aufgezeichneten Kunden-Q&A-Session, die von Contigos Produktteam durchgeführt wurde. Das Transcript ist 1.000 Wörter lang, hat keine Überschriften oder Strukturmarker und enthält eine Mischung aus Produktfragen, Off-Topic-Abschweifungen und unvollständigen Sätzen, bei denen das Audio unklar war.
Identifiziere zwei konkrete Herausforderungen, die dieses Dokument für beide Chunking-Strategien darstellt. Schlage einen Pre-Processing-Schritt vor, den das Team vor dem Chunking anwenden sollte, um die Qualität der erzeugten Chunks zu verbessern.

[toggle] Denke über Folgendes nach …
  🔽 Checkpoint 1: Denke über die Struktur des Produktleitfadens nach - Chunking auf Abschnittsebene packt Kriterien für die Kreditwürdigkeit, Zinssatzstruktur und Rückzahlungsbedingungen in einen Chunk. Überlege, ob das produktspezifischen Queries dient. Grenzen auf Unterabschnittsebene erzeugen kleinere Chunks, aber präziseres abrufen, wenn Kunden nach einem Aspekt eines Produkts fragen.
  🔽 Checkpoint 2: Denke über Overlap bei Fixed-Size-Chunks nach - Jede Verpflichtung steht für sich allein und umfasst im Schnitt 60 Tokens. Bei einer Chunk-Größe von 150 Tokens passen zwei Verpflichtungen problemlos hinein und es bleibt sogar noch Platz. Da keine Verpflichtung von den angrenzenden Einträgen abhängt, reicht ein kleiner oder gar kein Overlap hier völlig aus.
  🔽 Checkpoint 3: Denke über das Q&A-Transcript nach - Das Chunking eines Transcripts mit Off-Topic-Abschweifungen und unvollständigen Sätzen bettet Rauschen zusammen mit bedeutungsvollem Inhalt ein. Das Abruf-System kann nicht zwischen ihnen unterscheiden. Überlege vor dem Chunking, welche Transformation irrelevantes Material entfernt, ohne die echten Fragen und Antworten zu verwerfen.
  🔽 Checkpoint 4: Denke über variable Chunk-Größen nach - Semantisches Chunking respektiert Inhaltsgrenzen, erzeugt aber variable Größen. Ein dichter Abschnitt kann das Token-Limit des Embedding-Modells überschreiten. Prüfe bevor du zu Fixed-Size-Splitting zurückkehrst, ob der Abschnitt natürliche interne Grenzen wie Unterklauseln, nummerierte Punkte oder Absatzumbrüche enthält.

## Überprüfe dein Verständnis
Frage 1
>  Contigos Wissensdatenbank enthält Dokumente auf Deutsch, Englisch und Niederländisch. Ein Berater stellt eine Query auf Deutsch, die das Abrufen eines relevanten Chunks aus der niederländischen regulatorischen Zusammenfassung erfordert. Welcher Faktor bestimmt am direktesten, ob der richtige Chunk abgerufen wird?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/fac4216d-c5ec-4e6a-9c95-2343bbe70403

Frage 2
>  Der SME Loan Product Guide wird im nächsten Quartal mit überarbeiteten Zinssätzen aktualisiert. Wann sollte Contigos Team die Chunking-Strategie überdenken, statt die bestehende Konfiguration auf die neue Version anzuwenden?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/583fce50-148b-4b71-9236-a0cf4b28ceb9


> 💡 Takeaway: 
  Eine Chunking-Strategie ist eine Designentscheidung, die für jedes Dokument anhand seiner Struktur und der Queries getroffen werden muss, die es unterstützen soll. Eine Strategie, die gut für eine nummerierte Liste eigenständiger Pflichten funktioniert, erzeugt kaputte, unvollständige Chunks, wenn sie auf einen dicht querverwiesenen Produktleitfaden angewendet wird.
  Triffst du diese Entscheidung richtig, bevor du die Dokumente einpflegst, arbeitet die Retrieval-Pipeline über die gesamte Lebensdauer dieser Wissensdatenbank präzise.
