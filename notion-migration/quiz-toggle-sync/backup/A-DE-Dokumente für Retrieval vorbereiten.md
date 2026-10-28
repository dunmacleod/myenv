# Dokumente für Retrieval vorbereiten

Notion page: https://app.notion.com/p/Dokumente-f-r-Retrieval-vorbereiten-3779418319f3801b88eadaba00bf3911
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du entwirfst eine Strategie, mit der du zwei strukturell unterschiedliche Dateitypen aufbereitest. Du analysierst, warum eine generische Verarbeitung bei beiden scheitert, und schlägst passende Ansätze vor. So bewahrst du die Bedeutung der Inhalte und machst sie für das Retrieval optimal nutzbar.

## Das Szenario
Die Kuratierung der Wissensdatenbank der Contigo GmbH ist abgeschlossen. Das Team hat die Dokumente ausgewählt, die in die Abruf-Pipeline gehören, und diejenigen ausgeschlossen, die nicht hineingehören. Der nächste Schritt ist die Vorbereitung dieser Dokumente für die Ingestion, und genau hier wird ein häufiger und kostspieliger Fehler gemacht.
Ein Junior Developer im Team schlägt eine einfache Lösung vor:
- Jedes ausgewählte Dokument durch denselben Text Splitter laufen lassen, alles in 500-Wort-Blöcke schneiden, die Blöcke embedden und sie in Qdrant laden. Das ist schnell, konsistent und erfordert keine dokumentenspezifische Konfiguration.
Die Compliance-Leiterin widerspricht sofort. Sie hat diesen Ansatz schon früher scheitern sehen. Beim letzten Mal, als ein Team generisches Chunking auf ein rechtliches Compliance-Dokument angewendet hat, hat das Abruf-System eine kritische Klausel über zwei Chunks hinweg geteilt
- Chunk 1 - Die Bedingung erschien in einem Chunk
- Chunk 2 - Die Konsequenz
Der Agent rief nur den ersten Chunk ab, gab Kunden eine unvollständige Interpretation der Policy, und der Fehler blieb drei Wochen lang unentdeckt. Das Team braucht eine Vorbereitungsstrategie, die die Struktur jedes Dokumenttyps berücksichtigt, nicht nur sein Dateiformat.
## Die zwei Dokumente
Contigos Team bereitet zwei der ausgewählten Dateien für die Ingestion vor.
1. Dokument 1: Der 2026 SME Loan Product Guide (PDF) - Ein 5-seitiges Dokument, das mit klaren Abschnittsüberschriften, Unterabschnitten für jedes Produkt sowie detaillierten Kriterien für die Kreditwürdigkeit, Zinssatztabellen und Antragsanforderungen strukturiert ist. Der Inhalt ist dicht und miteinander verbunden; Kriterien für die Kreditwürdigkeit in einem Abschnitt verweisen auf Zinsstrukturen in einem anderen, und die Antragsanforderungen variieren abhängig vom Kredittyp, der weiter oben im Dokument beschrieben wurde.
1. Dokument 2: Die Standard Loan Application Checklist (PDF) - Ein einseitiges Dokument, das zwölf Punkte auflistet, die Kunden mit einem Kreditantrag einreichen müssen. Jeder Punkt ist ein kurzer, eigenständiger Eintrag; ein Bullet Point mit einem Label und einer Ein-Satz-Beschreibung. Es gibt keine Querverweise, keine verschachtelten Klauseln und keine Abhängigkeit zwischen den Punkten.
![image]((notion-hosted file))
## Deine Aufgaben

> 🔥 Template: Contigo Document Preparation worksheet — erstelle eine Kopie (File → Make a copy) und verwende sie, um deine Diagnose zu Dokument 1, deinen Ansatz für Dokument 2 und deinen Umgang mit der Vergleichstabelle festzuhalten.

#### Aufgabe A: Diagnostiziere das Scheitern generischen Chunkings bei Dokument 1
Der vorgeschlagene Ansatz des Junior Developers wendet einen festen 500-Wort-Text-Splitter auf den SME Loan Product Guide an, ohne seine Abschnittsstruktur zu berücksichtigen. Identifiziere zwei konkrete Arten, wie dieser Ansatz die Nützlichkeit des Dokuments für Abfragen beschädigen würde. Überlege, was passiert, wenn eine Chunk-Grenze mitten in einer Klausel liegt, und was passiert, wenn ein abgerufener Chunk auf Inhalte aus einem Abschnitt verweist, den der Chunk nicht enthält.
Schlage anschließend einen besseren Vorbereitungsansatz für dieses Dokument vor. Dein Vorschlag sollte angeben, welches strukturelle Merkmal des Dokuments du als Chunking-Grenze verwenden würdest, und erklären, warum diese Grenze die Bedeutung des Inhalts besser bewahrt als eine feste Wortanzahl.
### Aufgabe B: Bestimme den richtigen Ansatz für Dokument 2
Die Kreditantrags-Checkliste hat eine grundsätzlich andere Struktur als der Produktleitfaden. Dieselbe Chunking-Logik auf beide Dokumente anzuwenden, ist nicht angemessen, aber der Grund ist nicht sofort offensichtlich.
Beschreibe, wie du die Checkliste für die Ingestion vorbereiten würdest. Überlege, ob jeder Checklisteneintrag sein eigener Chunk sein sollte, ob die Einträge gruppiert werden sollten und welche Metadaten du jedem Chunk zuordnen würdest, um ein genaues Abrufen zu unterstützen. Erkläre, wie eine Kundenanfrage wie „Was muss ich mit meinem Kreditantrag einreichen?“ idealerweise mit den von dir erstellten Chunks interagieren sollte.
### Aufgabe C: Identifiziere das Strukturproblem bei tabellarischen Daten
Contigos Team erwägt außerdem, ob es eine strukturierte Produktvergleichstabelle aufnehmen soll. In Form das ein Abschnitt des Produktleitfadens, des Kreditlimits, der Zinssätze und Eignungsschwellen für fünf verschiedene Produkte in einem Side-by-Side-Tabellenformat darstellt.
Wenn ein Standard-Text-Splitter eine Tabelle verarbeitet, liest er typischerweise zeilenweise und verkettet den Text sequenziell, wodurch die Spaltenbeziehungen verloren gehen, die den Daten ihre Bedeutung geben. Erkläre, was der Agent abrufen würde, wenn diese Tabelle mit einem generischen Text-Splitter verarbeitet würde, und schlage einen alternativen Ansatz für den Umgang mit tabellarischen Inhalten in einer RAG-Pipeline vor.

[toggle] Denke über Folgendes nach …
  - Checkpoint 1: Denke über Querverweise nach - Der SME Loan Product Guide verweist in drei verschiedenen Abschnitten auf dieselbe Eignungsschwelle. Wenn ein fester Text-Splitter ohne Overlap über diese Abschnitte hinweg schneidet, enthält jeder Chunk nur einen Teil des Gesamtbildes. Wenn ein Kunde eine Frage stellt, die alle drei im Kontext erfordert, ruft der Agent den Chunk ab, der bei der Ähnlichkeit am höchsten bewertet wurde. Der Kunde erhält eine Teilantwort, die vollständig wirkt.
  - Checkpoint 2: Denke über Chunk-Overlap nach - Overlap fügt eine definierte Anzahl von Tokens hinzu, die zwischen aufeinanderfolgenden Chunks geteilt werden, und reduziert dadurch das Risiko, eine bedeutungstragende Einheit an der Grenze zu teilen. Bei einem dichten rechtlichen oder finanziellen Dokument kann ein kleiner Overlap dennoch mitten in einer Klausel schneiden, während ein großer Overlap erhebliche Mengen redundanter Inhalte über viele Chunks hinweg speichert. Der richtige Overlap-Wert ist die kleinste Anzahl, die kritische Klauselgrenzen intakt hält.
  - Checkpoint 3: Denke über tabellarische Daten nach - Ein Text-Splitter liest eine Tabelle sequenziell und verliert die Spaltenbeziehungen, die den Daten ihre Bedeutung geben. Ein Chunk, der aus einer fünfspaltigen Zinssatztabelle entsteht, könnte lauten: „SME Standard 5,2% SME Plus 4,8% SME Flex 5,5%“, ohne Header, die anzeigen, wofür diese Zahlen stehen. Wenn ein Kunde nach dem Zinssatz für SME Plus fragt, ruft der Agent diesen Chunk ab und hat keine zuverlässige Möglichkeit, den richtigen Wert aus der Zeichenkette verketteter Werte zu isolieren.
  - Checkpoint 4: Denke über Metadaten nach - Jeder Chunk, der in der Vektordatenbank gespeichert wird, trägt Metadaten neben seinem Vektor. Die semantische Ähnlichkeitssuche findet Chunks, die der Query mathematisch nahe sind, aber zwei Chunks aus unterschiedlichen Abschnitten des Produktleitfadens könnten bei derselben Anfrage ähnlich abschneiden. Ein Metadatenfeld „section“ gibt dem Abruf-System einen zusätzlichen Filter: Wenn es in der Query um Kriterien für die Kreditwürdigkeit geht, können Chunks, die mit dem Eignungsabschnitt getaggt sind, gegenüber Chunks aus dem Abschnitt zur Zinsstruktur priorisiert werden, die zufällig ähnlich bewertet wurden.

## Überprüfe dein Verständnis
### Frage 1
>  Contigo veröffentlicht den Leitfaden für KMU-Kreditprodukte für das zweite Quartal 2026. Die Version für das erste Quartal verbleibt neben der neuen Version in Qdrant. Was ist das größte Risiko dieses Fehlers bei der Versionsverwaltung?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/f0ddc358-54e6-40d3-a562-5ab0149c2a85

### Frage 2
>  Das Entwicklungsteam von Contigo prüft, ob der Leitfaden für KMU-Kreditprodukte mit einer überarbeiteten Chunking-Strategie erneut eingelesen werden soll. Welches Kriterium rechtfertigt eine vollständige erneute Einlesung am stärksten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/ecfc81c4-910c-4587-a9ef-a9d8ff5ae34a

> 💡 Takeaway: 
  Dokumentvorbereitung ist eine Designentscheidung, die bestimmt, wie viel von der Bedeutung des Dokuments den Aufnahme-Prozess übersteht. Eine Chunk-Grenze an der falschen Stelle zerstört Kontext. Eine als sequenzieller Text verarbeitete Tabelle verliert ihre Struktur vollständig. Die Investition in eine korrekte Dokumentvorbereitung vor der Aufnahme zahlt sich jedes Mal aus, wenn der Agent präzise abruft.