# Evidenzbewusste Antworten

Notion page: https://app.notion.com/p/Evidenzbewusste-Antworten-3779418319f3803fb21dd4f050ded665
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Einen Grounding-Fehler in einem bereitgestellten RAG-Agenten diagnostizieren, den System-Prompt neu schreiben, um evidenzbewusstes Verhalten durchzusetzen, und ein Fallback-Protokoll definieren, das fehlende Informationen sicher und professionell behandelt.

## Das Szenario
Die RAG-Pipeline der Contigo GmbH ist im internen Testing live. Die Abruf-Konfiguration funktioniert, und für die meisten Queries werden die richtigen Chunks zurückgegeben. Aber das Compliance-Team hat einen kritischen Verhaltensfehler markiert, den die Abruf-Konfiguration allein nicht beheben kann.
Während einer Test-Session fragte ein Compliance Officer den Agenten:
> „Wie hoch ist Contigos freigegebenes Budgetlimit für Kundenbewirtung in den Niederlanden?“
Die Qdrant-Vektordatenbank gab keine relevanten Chunks zurück. Das Thema war noch nicht zur Wissensdatenbank hinzugefügt worden. Statt die Lücke anzuerkennen, antwortete der Agent mit einem selbstbewussten, spezifischen Betrag und stellte ihn als Contigo-Policy dar.
Ein Junior Analyst im Team, dem nicht bewusst war, dass dies ein Test war, leitete den Betrag an einen kundenorientierten Kollegen weiter, der ihn in einem Kundenbriefing verwendete. Das Compliance-Team bemerkte den Fehler, bevor er den Kunden erreichte, aber der Vorfall legte eine strukturelle Schwachstelle offen. Der Agent war mit einer Wissensdatenbank verbunden, war aber nicht darauf beschränkt, sie zu verwenden. Wenn der Abruf fehlschlug, füllte das Sprachmodell die Lücke mit erfundener Spezifität.
Die Grounding-Anweisung im aktuellen System-Prompt lautet:
> „Du bist ein hilfreicher Compliance-Assistent. Lies die abgerufenen Dokumente und nutze sie, um die Fragen des Nutzers zu Contigos Policies zu beantworten. Sei immer höflich und gib eine umfassende Antwort.“
Dieser Prompt ist unzureichend. Er ermutigt das Modell, abgerufene Dokumente zu verwenden, verbietet ihm aber nicht, externes Wissen zu nutzen, wenn Dokumente fehlen. Die Lösung muss aus dem Prompt kommen.
## Warum Prompt-Grounding wichtig ist
Ein Sprachmodell mit einer Vektordatenbank zu verbinden, beschränkt es nicht automatisch auf diese Datenbank. Das Modell behält Zugriff auf alles, was es während des Trainings gelernt hat. Ohne eine strenge Anweisung ist sein Standardverhalten, hilfreich zu sein.
Das ist die zentrale Spannung im Design von RAG-Systemen. Die Abruf-Pipeline ist dafür gebaut, fundierte Evidenz bereitzustellen. Aber das Sprachmodell wird diese Evidenz nur verwenden, wenn es ausdrücklich dazu angewiesen und ausdrücklich daran gehindert wird, anders vorzugehen. Eine schwache Anweisung, die sagt „nutze die Dokumente“, lässt die Möglichkeit offen, sie zu ergänzen. Eine starke Anweisung, die sagt „nutze nur die Dokumente und nichts anderes“, schließt diese Lücke.
In einem regulierten Finanzdienstleistungsumfeld wie Contigos ist der Unterschied zwischen diesen zwei Anweisungen der Unterschied zwischen einem compliant Agenten und einer Haftung.
![image]((notion-hosted file))

## Der fehlerhafte Prompt
Die oben beschriebene erfundene Antwort ist ein fiktives Fehlerszenario und keine Voraussetzung für die Aufgabe. Dein eigener Agent könnte die Frage bereits korrekt behandeln. Teste hier den RAG-Agenten aus dem vorherigen Abschnitt, prüfe Qdrant-Tool-Aufrufe und Quellen und bewerte, wie zuverlässig die Anweisungen unbelegte Aussagen verhindern. Ein System-Prompt garantiert kein Grounding; unterscheide anhand der Execution-Logs zwischen Retrieval- und Generierungsfehlern.
Prüfe den aktuellen System-Prompt sorgfältig, bevor du mit der Aufgabe beginnst.
> „Du bist ein hilfreicher Compliance-Assistent. Lies die abgerufenen Dokumente und nutze sie, um die Fragen des Nutzers zu Contigos Policies zu beantworten. Sei immer höflich und gib eine umfassende Antwort.“
Identifiziere die konkreten Schwächen in diesem Prompt, bevor du deinen Ersatz schreibst. Eine präzise Diagnose dessen, was fehlt, führt zu einer wirksameren Überarbeitung als ein allgemeines Umschreiben.
## Deine Aufgaben
> 🔥 Template: Contigo Prompt Grounding worksheet — erstelle eine Kopie (File → Make a copy) und verwende sie, um deine Diagnose festzuhalten, deinen überarbeiteten Prompt zu entwerfen und zu prüfen und anschließend das Verhalten des Agenten bei jeder der drei Test-Queries zu dokumentieren.

#### Aufgabe A: Den Prompt-Fehler diagnostizieren
Identifiziere mindestens drei konkrete Schwächen im aktuellen System-Prompt, die den oben beschriebenen Grounding-Fehler ermöglichen. Schreibe für jede Schwäche einen Satz, der erklärt, was der Prompt nicht spezifiziert und welches Verhalten diese Auslassung ermöglicht. Schreibe den Prompt noch nicht um. Konzentriere dich vollständig auf die Diagnose. Eine schwache Diagnose erzeugt eine schwache Überarbeitung.
### Aufgabe B: Den überarbeiteten System-Prompt entwerfen
Schreibe einen Ersatz-System-Prompt für den Contigo-Compliance-Agenten. Dein Prompt muss zwischen vier und sechs Sätzen lang sein und alle drei Schwächen, die du in Aufgabe A identifiziert hast, ausdrücklich adressieren. Dein überarbeiteter Prompt muss die folgenden drei Elemente enthalten:
- Eine strenge Evidenzbeschränkung: Eine klare Anweisung, dass der Agent ausschließlich aus dem bereitgestellten abgerufenen Kontext antworten darf. Die Beschränkung muss als Verbot formuliert sein, nicht als Präferenz.
- Ein Fallback-Protokoll: Eine knappe Anweisung, die die exakte Formulierung angibt, die der Agent ausgeben muss, wenn der abgerufene Kontext die Antwort nicht enthält. Die Formulierung sollte professionell sein, die Einschränkung ehrlich anerkennen und den Kunden an eine geeignete Alternative verweisen.
- Eine Scope-Definition: Eine kurze Aussage darüber, was der Agent ist und worüber er autorisiert ist zu antworten. Ohne Scope-Definition hat das Modell keinen Rahmen, um zu entscheiden, ob eine Query innerhalb seines Aufgabenbereichs liegt oder außerhalb davon.
### Aufgabe C: Den überarbeiteten Prompt testen
Gib deinen überarbeiteten Prompt in das Feld System Message deines Agenten ein und führe die folgenden drei Test-Queries aus. Dokumentiere die Antwort des Agenten auf jede Query und bewerte, ob er sich gemäß deinem Prompt verhält.
Test 1: In-Domain-Query mit abrufbarer Antwort:
> „Welche Dokumente muss ein Kunde mit einem Privatkreditantrag einreichen?“
Erwartetes Verhalten: Der Agent ruft den relevanten Checklist-Chunk ab und antwortet spezifisch daraus.
Test 2: Out-of-Domain-Query ohne abrufbare Antwort:
> „Wie hoch ist Contigos freigegebenes Budget für Kundenbewirtung in den Niederlanden?“
Erwartetes Verhalten: Der Agent gibt deine definierte Fallback-Formulierung aus.
Test 3: Boundary-Query, die in-domain klingt
> „Basierend auf üblicher EU-Finanzdienstleistungspraxis, wie lange wäre eine typische Kreditbearbeitungszeit?“
Erwartetes Verhalten: Der Agent erkennt, dass „übliche EU-Finanzdienstleistungspraxis“ außerhalb des abgerufenen Kontexts liegt, und ergänzt nicht mit Trainingsdaten. Wenn er mit einer allgemeinen Zahl antwortet, muss die Evidenzbeschränkung verstärkt werden.
[toggle] Denke über Folgendes nach …
  🔽 Checkpoint 1: Das Vollständigkeitsproblem diagnostizieren - Der Agent nannte einen Betrag, der in keinem abgerufenen Chunk vorkommt. Das bedeutet, dass der System-Prompt das Modell nicht daran hindert, abgerufene Inhalte mit allgemeinem Trainingswissen zu ergänzen. Die Grounding-Anweisung muss ausdrücklicher und restriktiver sein.
  🔽 Checkpoint 2: Ein wirksames Verbot schreiben - Wenn abgerufene Chunks keine relevanten Informationen enthalten, generiert das Modell standardmäßig aus allgemeinem Training, statt die Lücke anzuerkennen. Ein gut entworfener System-Prompt gibt dem Agenten eine ausdrückliche Fallback-Formulierung, die er verwenden soll, wenn der abgerufene Kontext nicht ausreicht, um sicher zu antworten.
  🔽 Checkpoint 3: Die Fallback-Formulierung entwerfen - Grounding-Beschränkungen und Tonalitätsvorgaben schließen sich nicht gegenseitig aus. Ein System-Prompt kann ausdrücklich festlegen, dass das Modell auf abgerufene Inhalte beschränkt ist, und gleichzeitig angeben, wie Antworten formuliert sein sollten und welcher Kommunikationsstil von einem Contigo-Support-Agenten erwartet wird.
  🔽 Checkpoint 4: Test 3 handhaben - Wenn der Agent nach der Aktualisierung des System-Prompts weiterhin eine selbstbewusste Antwort zurückgibt, gibt es zwei Stellen, an denen du nachsehen solltest. Prüfe zuerst, ob die Grounding-Anweisung eindeutig genug ist, dass das Modell sie nicht locker interpretieren kann. Prüfe zweitens, ob die abgerufenen Chunks versehentlich Inhalte enthalten, die der Query nahe genug sind, um eine Antwort auszulösen.

## Verständnis prüfen
Frage 1
> 💡 Contigos Agent liefert täglich Hunderte von Fallback-Antworten, wenn Queries nicht aus der Wissensdatenbank gelöst werden können. Welcher Prozess nutzt die Fallback-Häufigkeit am effektivsten als Signal für Wissensdatenbanklücken?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/201bb0a4-c4a1-4a71-a7b9-626479138748

Frage 2
> 💡 Contigos System-Prompt weist den Agenten an, ausschließlich aus abgerufenem Kontext zu antworten. Eine ausgefeilte adversariale Eingabe bringt das Modell dazu, an dieser Anweisung vorbei zu argumentieren und seine Antwort mit Trainingsdaten zu ergänzen. Welcher architektonische Mechanismus bietet am zuverlässigsten eine zweite Grounding-Durchsetzungsschicht, die unabhängig von der Anweisungsbefolgung des Modells ist?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/4f777829-be64-44c1-98a1-196a99b6a831


> 💡 Takeaway: 
  Abruf und Grounding sind zwei getrennte Probleme, die zwei getrennte Lösungen erfordern. Der Abruf wird durch die Pipeline-Architektur gelöst (den Vector Store, das Embedding-Modell und die Top-K-Konfiguration). Das Grounding wird durch den System-Prompt gelöst.
  Eine gut konfigurierte Abruf-Pipeline, die mit einem schwach geschriebenen System-Prompt verbunden ist, ist weiterhin ein nicht geerdeter Agent. Beides muss korrekt sein, damit das System vertrauenswürdig ist.
