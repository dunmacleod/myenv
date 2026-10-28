# Quelldokumente auswählen

Notion page: https://app.notion.com/p/Quelldokumente-ausw-hlen-3779418319f38095b3d0cf6028c0c88d
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du bewertest eine Reihe von Dokumenten für deine Business-Wissensdatenbank. Jede Entscheidung begründest du mit klaren Kriterien für Relevanz, Genauigkeit und Sicherheit.
## Das Szenario
Das Entwicklungsteam der Contigo GmbH ist bereit, die Wissensdatenbank aufzubauen, die die Retrieval-Pipeline des Support-Agenten antreiben wird. Das Compliance-Team hat die RAG-Architektur freigegeben. Bevor ein Dokument in die Retrieval-Pipeline gelangt, muss es anhand klarer Aufnahmekriterien bewertet werden. Das Team steht jetzt vor einer Frage, die auf den ersten Blick einfach wirkt: Welche Dokumente gehören tatsächlich in die Wissensdatenbank?
Die Antwort ist wichtiger, als es zunächst scheint. Ein RAG-System ruft Inhalte auf Grundlage semantischer Ähnlichkeit ab. Es findet die Chunks, die der Nutzeranfrage mathematisch am nächsten liegen, und übergibt sie dem Sprachmodell als Kontext. Es hat kein eingebautes Verständnis dafür, ob ein Dokument aktuell, freigegeben oder für die Nutzung gegenüber Kunden geeignet ist. Wenn ein veraltetes Policy-Dokument, ein interner Entwurf oder eine Datei mit sensiblen personenbezogenen Daten in die Wissensdatenbank aufgenommen wird, ruft der Agent daraus mit derselben Sicherheit ab wie aus einer geprüften, aktuellen Policy.
Das Prinzip hier ist einfach:
> ➡️ Die Qualität der Antworten des Agenten ist durch die Qualität der Dokumente begrenzt, auf die er Zugriff hat. Die Dokumentauswahl vor der Ingestion richtig zu machen, ist deutlich einfacher, als Retrieval-Fehler nach dem Deployment zu korrigieren.

## Die drei Kriterien
Bevor du ein Dokument klassifizierst, lege die Kriterien fest, die du konsistent auf alle Kandidaten anwenden wirst.
- Relevanz: Enthält dieses Dokument Informationen, nach denen der Agent gefragt werden wird? Ein Dokument, das korrekt und aktuell ist, aber Themen außerhalb des definierten Scopes des Agenten abdeckt, fügt der Wissensdatenbank Rauschen hinzu, ohne Wert zu schaffen. Irrelevante Chunks konkurrieren beim Abruf mit relevanten und verringern die Präzision.
- Genauigkeit und Aktualität: Sind die Informationen in diesem Dokument korrekt und aktuell? Ein veraltetes Dokument, das der aktuellen Policy widerspricht, ist gefährlicher als ein fehlendes Dokument. Der Agent wird es abrufen, zitieren und Kunden mit scheinbarer Autorität falsche Informationen geben.
- Sicherheit und Angemessenheit: Ist dieses Dokument sicher genug, um in ein System aufgenommen zu werden, das seine Inhalte Kunden oder kundenorientierten Mitarbeitenden anzeigen wird? Dokumente, die personenbezogene Daten, interne Kommunikation, nicht freigegebene Entwürfe oder sensible kommerzielle Informationen enthalten, sollten nicht in einem Abruf-System enthalten sein, es sei denn, es werden Zugriffskontrollen angewendet, die die RAG-Pipeline selbst nicht durchsetzen kann.
![image]((notion-hosted file))
## Die Kandidatendokumente
Contigos Operations-Team hat die folgenden sieben Dateien als Kandidaten für die Wissensdatenbank zusammengestellt. Prüfe jede einzelne sorgfältig, bevor du mit der Klassifizierungsaufgabe beginnst.
1. 2026 SME Loan Product Guide (PDF): Die aktuelle, freigegebene Produktdokumentation zu Kreditlimits, Kriterien für die Kreditwürdigkeit, Zinsspannen und Antragsanforderungen für Contigos SME-Finanzierungsprodukte in Deutschland, Österreich und den Niederlanden.
1. 2023 SME Loan Product Guide (PDF): Eine frühere Version desselben Dokuments. Mehrere Kreditlimits und Eignungsschwellen haben sich seit Veröffentlichung dieser Version geändert.
1. EU Consumer Credit Directive Summary (PDF): Eine zweiseitige interne Zusammenfassung der wichtigsten Pflichten gemäß der EU Consumer Credit Directive, erstellt von Contigos Legal-Team und als für die operative Nutzung freigegeben gekennzeichnet.
1. Client Transaction Export Q1 2026 (CSV): Ein strukturierter Datenexport mit Kundennamen, Kontonummern, Kreditbeträgen und Zahlungshistorien für alle aktiven Konten im ersten Quartal 2026.
1. Internal Slack Export Compliance Channel (TXT): Ein roher Textexport eines Monats interner Slack-Nachrichten aus dem Compliance-Team, einschließlich Diskussionen über regulatorische Interpretationen, ungelöste Fragen und informelle Meinungen einzelner Mitarbeitender.
1. Standard Loan Application Checklist (PDF): Eine einseitige Checkliste der Dokumente, die Kunden mit einem Kreditantrag einreichen müssen, aktualisiert im Januar 2026 und für die Nutzung gegenüber Kunden freigegeben.
1. *Draft Client Communication Template [Netherlands (DOCX)]:** Eine Vorlage für kundenorientierte Schreiben im Zusammenhang mit niederländischen Kreditanträgen, derzeit in rechtlicher Prüfung und noch nicht zur Nutzung freigegeben.
## Deine Aufgaben
> 🔥 
  ### Template: Contigo KB Evaluation worksheet 
  Erstelle eine Kopie und verwende sie, um deine Kriterien und deine sieben Entscheidungen zu Include/Exclude festzuhalten, während du die folgenden Aufgaben bearbeitest.

#### Aufgabe A: Definiere deine Aufnahmekriterien
Schreibe zwei bis drei Sätze, die definieren, was ein Dokument für die Aufnahme in Contigos RAG-Wissensdatenbank qualifiziert. Deine Kriterien sollten spezifisch genug sein, um konsistent auf alle sieben Kandidaten angewendet zu werden; eine Regel, die für jede Datei eine klare Entscheidung erzeugt.
### Aufgabe B: Klassifiziere jedes Dokument
Wende deine Kriterien auf alle sieben Kandidaten an. Entscheide für jedes Dokument, ob es Include oder Exclude ist, und schreibe einen Satz, der erklärt, wie deine Kriterien diese Entscheidung begründen.
Achte besonders auf Dokumente, bei denen die Entscheidung nicht sofort offensichtlich ist. Ein Dokument kann korrekt und relevant sein, aber dennoch ungeeignet für die Aufnahme. Ein Dokument kann für die aktuelle Wissensdatenbank ungeeignet sein, aber in einer anderen Konfiguration angemessen.
- Denke über Folgendes nach …
  🔽 Checkpoint 1: Denke über widersprüchliche Versionen nach - Bedenke, dass dasAbruf-System kein Konzept von „aktuell“ oder „veraltet“ hat. Es gibt Chunks ausschließlich auf Grundlage semantischer Ähnlichkeit zurück. Wenn zwei Versionen desselben Dokuments in der Wissensdatenbank sind und unterschiedliche Beträge für dasselbe Kreditlimit enthalten, ruft der Agent aus beiden ab, und der Kunde erhält die Version, die bei dieser Anfrage zufällig höher bewertet wurde. Es gibt keine Warnung, dass ein Konflikt besteht.
  🔽 Checkpoint 2: Denke über personenbezogene Daten nach - RAG ruft auf Grundlage semantischer Ähnlichkeit ab, nicht nach Dokumenttyp oder Sensibilitätsstufe. Ein Kunde, der nach Account Management fragt, könnte Chunks mit dem Namen, der Kontonummer oder der Finanzhistorie eines anderen Kunden erhalten, wenn diese Daten in der Wissensdatenbank enthalten sind. Nach DSGVO ist das Anzeigen personenbezogener Daten über eine Person in einer Antwort an eine andere Person kein Abruf-Konfigurationsproblem. Es ist ein Datenschutzverstoß.
  🔽 Checkpoint 3: Denke über unstrukturierte informelle Inhalte nach - Denke über den Unterschied zwischen einem formal freigegebenen Policy-Dokument und einer informellen Slack-Nachricht nach, in der ein Compliance Officer über eine regulatorische Interpretation spekuliert. Der Agent kann nicht zwischen beidem unterscheiden. Er ruft auf Grundlage semantischer Relevanz ab. Wenn eine informelle, nicht freigegebene Interpretation abgerufen und einem Kunden als Antwort präsentiert wird, trägt sie dieselbe scheinbare Autorität wie geprüfte Policy-Inhalte.
  🔽 Checkpoint 4: Denke über Entwurfsdokumente nach - Ein Dokument in rechtlicher Prüfung ist nicht zur Nutzung freigegeben. Wenn der Agent es abruft und verwendet, um eine Kundenanfrage zu beantworten, gibt es in der Antwort keinen sichtbaren Hinweis darauf, dass der Inhalt vorläufig war. Aus Kundensicht sieht die Antwort genau so aus wie eine Antwort, die aus einem freigegebenen Dokument stammt.
## Prüfe dein Verständnis
### Frage 1
>  Contigos Wissensdatenbank enthält einen Kreditproduktleitfaden, der veraltet, wenn Zinssätze quartalsweise angepasst werden. Welcher Prozess hält die Wissensdatenbank am effektivsten aktuell, ohne jedes Mal eine vollständige Re-Ingestion zu erfordern?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/43b602fd-bde7-4a93-a132-73e5fdf052bd

### Question 2
>  Ein Contigo-Agent benötigt Zugriff auf den Kreditbetrag und die Zahlungshistorie eines Kunden, um seine Antworten zu personalisieren. Welcher Architekturansatz ermöglicht dies, ohne diese Daten in die RAG-Wissensdatenbank aufzunehmen?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b5a9ddf9-7cd6-4b72-8580-af338db166ae

> 💡 Takeaway: 
  Ein RAG-System ist nur so zuverlässig wie die Dokumente, aus denen es abruft. Die Aufnahme einer veralteten Policy erzeugt ein Risiko für Fehlinformationen. Die Aufnahme personenbezogener Daten erzeugt ein Compliance-Risiko. Die Aufnahme nicht freigegebener Entwürfe erzeugt ein rechtliches Risiko. Keines dieser Risiken ist in der Ausgabe des Agenten sichtbar, bis etwas schiefgeht.