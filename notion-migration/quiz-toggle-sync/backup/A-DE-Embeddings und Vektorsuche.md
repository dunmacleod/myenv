# Embeddings und Vektorsuche

Notion page: https://app.notion.com/p/Embeddings-und-Vektorsuche-3779418319f38013997fe17ca65932d7
Backed up before n8n migration

> 💡 Am Ende dieser Lektion verstehst du, wie Text in eine mathematische Form umgewandelt wird, die Maschinen semantisch durchsuchen können, und warum dies die Grundlage dafür ist, dass RAG-Retrieval über unterschiedliche Query-Formulierungen hinweg funktioniert. 

## Das Problem, an dem Keyword Search scheitert
Das Compliance-Team der Contigo GmbH testet die Abruf-Pipeline mit einer Reihe repräsentativer Kundenanfragen. Die meisten geben die richtigen Chunks zurück. Aber es zeigt sich ein Muster von Fehlern, das das Team nicht durch Anpassung von Chunk-Größe oder Overlap beheben kann.
Ein Kunde fragt:
> „Was passiert, wenn ich meine Kreditrate diesen Monat nicht zahlen kann?“
Das Abruf-System gibt nichts Relevantes zurück. Die richtige Information existiert in der Wissensdatenbank (ein Abschnitt mit dem Titel „Payment Difficulties and Restructuring Options“). Aber die Query des Kunden teilt keine exakten Wörter mit dieser Abschnittsüberschrift oder ihrem Inhalt. Das System findet keine Übereinstimmung, weil es nach Wörtern sucht, nicht nach Bedeutung.
Das ist die grundlegende Einschränkung von Keyword-basierter Suche. Sie gleicht Text anhand des Vorhandenseins bestimmter Zeichen und Wörter ab. Sie hat kein Verständnis von Synonymen, Paraphrasierung oder der konzeptuellen Beziehung zwischen unterschiedlichen Formulierungen derselben Frage. Für einen Support-Agenten, der Kunden bedient, die ihre Fragen auf unvorhersehbare Weise formulieren, ist Keyword Search keine tragfähige Grundlage.
Die Lösung sind Embeddings und Vector Search. Das sind Mechanismen, die es dem Abruf-System ermöglichen, Inhalte auf Grundlage von Bedeutung statt exakter Formulierung zu finden.
## Was sind Embeddings ?
Ein Embedding ist die numerische Darstellung von Text. Ein Embedding-Modell wandelt einen Textabschnitt in einen Vektor um, also in ein Array aus Zahlen. Jede Zahl in diesem Array steht für eine Dimension in einem hochdimensionalen mathematischen Raum.
Ein Beispiel: Der Satz „cannot make my loan repayment“ wird zu einem Vektor wie [0.21, -0.87, 0.44, ...], der aus hunderten von Zahlen bestehen kann. Die Phrase „payment difficulties“ erzeugt ein anderes, aber mathematisch nahe gelegenes Array. Der Ausdruck „office furniture catalogue“ liefert hingegen ein Array, das weit von beiden entfernt liegt. Die Zahlen selbst lassen sich nicht isoliert interpretieren. Entscheidend ist ausschließlich der mathematische Abstand zwischen ihnen.
Die zentrale Eigenschaft von Embeddings ist, dass Texte mit ähnlicher Bedeutung Vektoren erzeugen, die in diesem Raum nah beieinander liegen. Die Aussagen „payment difficulties“ und „cannot make my loan repayment“ erzeugen Vektoren in direkter Nachbarschaft, da das Embedding-Modell die semantische Verwandtschaft dieser Konzepte gelernt hat. Die Phrase „office furniture catalogue“ erzeugt dagegen einen Vektor, der weit von beiden entfernt liegt.
## Wie Chunking und Embeddings zusammenhängen
Chunking und Embeddings funktionieren als sequenzielles Paar.
- Chunking teilt ein Dokument zuerst in kleinere Teile auf. Jeder Chunk wird dann an ein Embedding-Modell übergeben, das ihn in einen numerischen Vektor umwandelt, der seine semantische Bedeutung repräsentiert.
- Die Qualität des Embeddings hängt direkt von der Qualität des Chunks ab. Ein Chunk, der nicht zusammenhängende Themen mischt, erzeugt einen Vektor, der nichts präzise repräsentiert, wodurch es schwieriger wird es präzise abzurufen.
- Zur Anfragezeit wird die Frage des Nutzers mit demselben Modell eingebettet, und der resultierende Vektor wird mit allen gespeicherten Chunk-Vektoren verglichen, um die nächsten semantischen Treffer zu finden.
![image]((notion-hosted file))
Das macht semantische Suche möglich. Das System sucht nach Vektoren, die im Embedding-Raum nahe am Query-Vektor liegen.
Für Contigos Pipeline wird dasselbe Embedding-Modell an zwei Punkten verwendet:
1. Während der Ingestion, um Dokument-Chunks für die Speicherung in Vektoren umzuwandeln
1. Zur Query-Zeit, um die Frage des Kunden in einen Vektor für den Vergleich umzuwandeln
![image]((notion-hosted file))

## Wo konfigurierst du das in n8n?
Das Embedding-Modell wird in deinem Build an zwei getrennten Stellen konfiguriert:
- Während der Einpflegung: Im n8n-Ingestion-Workflow am Embeddings-Sub-Node des Qdrant Vector Store, zusammen mit Loader und Text Splitter. Hier wird text-embedding-004 ausgewählt und dein Gemini API-Key authentifiziert. Jeder Chunk, der in der Vektordatenbank gespeichert wird, wird mit diesem Modell eingebettet.
- Zur Query-Zeit: Im n8n-Retrieval-Workflow wird ein kompatibler Embeddings-Sub-Node mit dem Qdrant Retriever oder Retrieval-Tool verbunden. Dieser Node muss dasselbe Modell (text-embedding-004 ) und denselben API-Key verwenden. Wenn die zwei Nodes unterschiedliche Modelle verwenden, befinden sich Query-Vektor und Dokumentvektoren in unterschiedlichen mathematischen Räumen, und Ähnlichkeitswerte werden bedeutungslos.
Du wirst beides konfigurieren, wenn du vor der Antwortgenerierung einen Abruf durchführst. Zu verstehen, dass es sich um getrennte Schritte an unterschiedlichen Stellen handelt, bewahrt dich vor dem häufigsten RAG-Konfigurationsfehler.
## Wie Vector Search funktioniert
Wenn ein Kunde eine Query sendet, passiert innerhalb des Abruf-Schritts die folgende Sequenz.
1. Die Query wird durch das Embedding-Modell geleitet und in einen Vektor umgewandelt.
1. Die Vektordatenbank (Qdrant) berechnet die mathematische Distanz zwischen dem Query-Vektor und jedem gespeicherten Dokumentvektor.
1. Die Chunks, deren Vektoren dem Query-Vektor am nächsten liegen, werden als Retrieval-Ergebnisse zurückgegeben.
Die am häufigsten verwendete Distanzberechnung ist die Kosinusähnlichkeit. Die Kosinusähnlichkeit misst den Winkel zwischen zwei Vektoren statt der absoluten Distanz zwischen ihnen.
Eine Kosinusähnlichkeit von 1 bedeutet, dass die Vektoren in genau dieselbe Richtung zeigen.
Eine Kosinusähnlichkeit von 0 bedeutet, dass die Vektoren orthogonal sind, was bedeutet, dass der Inhalt keine bedeutungsvolle Beziehung zur Query hat. Ein Wert von -1 bedeutet, dass die Vektoren in entgegengesetzte Richtungen zeigen.
Deshalb ruft die Frage des Kunden zu verpassten Rückzahlungen den Abschnitt zu Zahlungsschwierigkeiten ab, obwohl sich keine Wörter überschneiden. Das Embedding-Modell platziert beide Formulierungen nahe beieinander im Vektorraum, die Kosinusähnlichkeit zwischen ihren Vektoren ist hoch, und der richtige Chunk wird zurückgegeben.
![image]((notion-hosted file))


## Warum das für die Abfrage-Qualität wichtig ist
Die Qualität semantischer Suche hängt von drei Faktoren ab, die das Entwicklungsteam kontrolliert.
- Wahl des Embedding-Modells: Verschiedene Modelle erzeugen unterschiedliche Vektorräume. Für Contigos n8n-Pipeline nutze einen verfügbaren Embeddings-Sub-Node und ein zum Qdrant-Index passendes Modell; der Modellname und die Vektordimension müssen beim Schreiben und Suchen übereinstimmen. Für ein mehrsprachiges Deployment, das Deutschland, Österreich und die Niederlande abdeckt, ist text-embedding-004 geeignet, da es mehrsprachige semantische Ähnlichkeit out of the box unterstützt.
- Chunk-Qualität: Ein Embedding repräsentiert die Bedeutung des Textes, den es erhält. Ein Chunk, der mehrere nicht zusammenhängende Themen mischt, erzeugt einen Vektor, der keines dieser Themen präzise repräsentiert. Die Chunking-Entscheidungen, die du zuvor getroffen hast, bestimmen direkt, wie genau deine Vektoren die Inhalte der Wissensdatenbank repräsentieren. Schlechte Chunks erzeugen unpräzise Vektoren. Unpräzise Vektoren erzeugen schlechte Abrufe. Die zwei Probleme sind dasselbe Problem.
- Query-Formulierung: Eine sehr kurze oder mehrdeutige Query erzeugt einen weniger präzisen Vektor, weil dem Embedding-Modell weniger semantische Information zur Verfügung steht. Deshalb kann ein n8n-Retrieval-Workflow Folgefragen, bevor sie die Vektordatenbank erreichen. Für Queries, die bereits gut formuliert eintreffen, ist kein Umschreiben erforderlich. Für Queries, die vage oder kontextabhängig eintreffen, macht die Reformulierung das Retrieval präzise.
## Keyword Search versus Vector Search
[TABLE]
  |  | Keyword Search | Vector Search |
  | Matching-Mechanismus | Exakter Wort- oder Zeichenabgleich | Mathematische Nähe im Embedding-Raum |
  | Umgang mit Synonymen | Nur wenn ausdrücklich programmiert | Automatisch: ähnliche Bedeutungen clustern zusammen |
  | Umgang mit Paraphrasierung | Scheitert, wenn exakte Begriffe nicht vorhanden sind | Gelingt: Bedeutung bleibt über Formulierungen hinweg erhalten |
  | Geeignet für | Strukturierte Daten mit bekannter Terminologie | Unstrukturierter Text mit variierter natürlicher Sprache |
  | Contigo-Anwendungsfall | Ungeeignet für die Bearbeitung von Kundenanfragen | Grundlage der RAG-Retrieval-Pipeline |
## Verständnis prüfen
> 💡 Ein Contigo-Kunde fragt: „Welche Optionen habe ich, wenn ich finanzielle Schwierigkeiten habe?“ Der richtige Chunk trägt den Titel „Payment Difficulties and Restructuring Options“. Zwischen der Query und dem Chunk-Titel überschneiden sich keine Wörter. Warum ruft Vector Search trotzdem den richtigen Chunk ab?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/248e0e64-5ac2-46a0-a7d3-4feca9264983

> 💡 Takeaway: 
  Embeddings sind die Übersetzungsschicht zwischen menschlicher Sprache und maschineller Suche. Indem Text in der Vektoren umgewandelt werden, die nach Bedeutung clustern, kann die Abruf-Pipeline den richtigen Inhalt finden, selbst wenn der Kunde seine Frage so formuliert, dass sie keine Wörter mit dem Quelldokument teilt.
  In n8n hängt diese Flexibilität davon ab, dass dasselbe Embedding-Modell im Ingestion-Workflow und beim Abruf konsistent konfiguriert wird. Eine einzige Abweichung zwischen diesen zwei Konfigurationspunkten reicht aus, damit die gesamte Abfrage-Pipeline bedeutungslose Ergebnisse zurückgibt.