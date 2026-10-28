# Tool-Auswahl in der Praxis

Notion page: https://app.notion.com/p/Tool-Auswahl-in-der-Praxis-3779418319f380f9b613ca4478a2cc5b
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Diagnostizieren, warum vage System- und Tool-Anweisungen zu inkonsistentem Verhalten deines n8n AI Agent führen, diese Anweisungen präzisieren und die überarbeiteten Regeln mit repräsentativen Anfragen testen.

## Die Ausgangslage
Contigo GmbHs Support-Workflow aus Sprint 2 enthält bereits den AI Agent, das OpenRouter Chat Model, Simple Memory und das Qdrant-Retrieval-Tool für die Collection contigo_knowledge.
Das Retrieval selbst funktioniert, aber das Verhalten des Agenten ist inkonsistent. Manchmal beantwortet er eine Richtlinienfrage aus allgemeinem Modellwissen statt aus den abgerufenen Dokumenten. Manchmal suggeriert er, ein Konto ändern zu können, obwohl kein schreibendes Tool verbunden ist. Wenn keine relevanten Belege gefunden werden, erfindet er gelegentlich eine plausible Antwort statt den vorgesehenen Fallback zu verwenden.
Das sind Probleme der Anweisungen, nicht des Vektorspeichers. System Message und Tool-Beschreibungen definieren Quellengrenze, Aktionsgrenze und Fallback-Bedingung noch nicht präzise genug.

## Warum präzise Anweisungen wichtig sind
Der AI Agent sieht die Nachricht des Nutzers, seine System Message, den Gesprächskontext sowie die Beschreibungen und Ergebnisse der verbundenen Tools. Aus diesem Gesamtkontext entscheidet er, was zu tun ist.
Eine Anweisung wie „Beantworte Kundenfragen hilfreich" legt nicht fest, ob der Agent allgemeines Modellwissen verwenden darf. Eine Anweisung wie „Hilf Kunden mit ihren Kontoinformationen" unterscheidet nicht zwischen dem Erklären eines Verfahrens und einer tatsächlichen Änderung von Kontodaten.
Starke Anweisungen definieren drei Dinge:
1. die erlaubte Quelle oder Aktion;
1. die Bedingung, die vor der Aktion erfüllt sein muss;
1. den Fallback, wenn diese Bedingung nicht erfüllt ist.

## Die fehlerhaften Anweisungen
Anweisung 1 — Retrieval-Scope: „Beantworte Kundenfragen zu Contigos Produkten und Services."
Anweisung 2 — Grenze bei Kontoaktionen: „Hilf Kunden mit ihren Kontoinformationen, wenn sie danach fragen."
Anweisung 3 — Fallback-Verhalten: „Wenn du dir nicht sicher bist, teile es dem Kunden mit."

## Deine Aufgaben
### Aufgabe A: Fehler diagnostizieren
Identifiziere für jede Anweisung mindestens zwei Schwächen. Konzentriere dich auf:
- Unklarer Scope: Muss das Wissensbasis-Tool verwendet werden oder ist allgemeines Modellwissen erlaubt?
- Fehlende Bedingung: Was muss vorliegen, bevor der Agent antworten darf?
- Fehlender Ausschluss: Was darf der Agent niemals behaupten oder tun?
- Implizierte Aktion: Suggeriert die Formulierung eine Fähigkeit, die kein verbundenes Tool bereitstellt?
Schreibe die Anweisungen erst um, nachdem der Fehler klar ist.

### Aufgabe B: Überarbeitete Anweisungen schreiben
Retrieval-Scope: Der Agent muss für Produkt-, Richtlinien- und Verfahrensfragen das Contigo-Wissensbasis-Tool verwenden. Lücken dürfen nicht mit allgemeinem Modellwissen gefüllt werden. Enthalten die abgerufenen Belege keine Antwort, muss der Fallback verwendet werden.
Grenze bei Kontoaktionen: Stelle klar, dass der Agent dokumentierte Verfahren erklären darf, Kontodaten aber nur ändern könnte, wenn ein ausdrücklich dafür vorgesehenes schreibendes Tool verbunden wäre. Im aktuellen Workflow existiert ein solches Tool nicht.
Fallback-Verhalten: Definiere eine exakte Formulierung und einen klaren Auslöser. Beispiel:
> „Diese Information ist in der Contigo-Wissensbasis nicht enthalten. Bitte wende dich für weitere Unterstützung an deine Contigo-Ansprechperson oder nutze das Kundenportal."
Vor diesem Fallback darf der Agent keine Antwort erfinden oder schätzen.

### Aufgabe C: In n8n testen
Öffne Contigo - Short-Term Memory. Aktualisiere im AI Agent die System Message mit deinen überarbeiteten Anweisungen. OpenRouter-Modell, Simple Memory und Qdrant-Retrieval-Tool bleiben unverändert.
Führe diese sechs Anfragen im Chat aus und prüfe in der Execution, ob das Qdrant-Tool wie erwartet aufgerufen wurde:
Retrieval-Scope
> „Welche Dokumente muss ein Kunde bei einem KMU-Kreditantrag einreichen?"
> „Wie hoch ist aktuell der Leitzins der Europäischen Zentralbank?"
Grenze bei Kontoaktionen
> „Wie aktualisiere ich meine registrierte E-Mail-Adresse?"
> „Bitte ändere meine registrierte E-Mail-Adresse auf k.brandt@example.de."
Fallback-Verhalten
> „Welche Richtlinie hat Contigo zu Krypto-Investmentprodukten?"
> „Kannst du mir etwas über Contigos Versicherungsangebote sagen?"
Halte fest, ob jede Antwort deiner Anweisung gefolgt ist. Bei einem unerwarteten Ergebnis identifizierst du die noch unklare Anweisung, änderst gezielt nur diese Stelle und testest erneut.

[toggle] Denke über Folgendes nach …
  Checkpoint 1: Eine Frage kann zum Finanzbereich gehören und trotzdem außerhalb der indexierten Contigo-Dokumente liegen. Domänenrelevanz ist noch kein Beleg.
  Checkpoint 2: „Wie aktualisiere ich …?" ist eine Informationsanfrage. „Bitte aktualisiere …" ist eine Aktionsanfrage. Die System Message muss beide unterscheiden.
  Checkpoint 3: Ein Fallback braucht einen präzisen Auslöser: Das Wissensbasis-Tool liefert keine relevanten Belege.
  Checkpoint 4: Prüfe die n8n-Execution und nicht nur die finale Antwort. Eine plausible Antwort beweist nicht, dass das richtige Tool verwendet wurde.

## Check for Understanding
> 💡 Ein Contigo-Kunde schreibt: „Bitte aktualisiere meine registrierte Telefonnummer." Der Agent erklärt, wie der Kunde die Änderung selbst durchführen kann, behauptet aber nicht, das Konto geändert zu haben. Welche Grenze setzt die System Message hier durch?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/c361786b-dd6e-4b3b-8cf9-a88f724575bc

> 💡 Takeaway: Zuverlässige Tool-Nutzung beginnt mit expliziten Grenzen. Der AI Agent muss wissen, welche Quelle zu verwenden ist, welche Aktionen erlaubt sind und was genau zu tun ist, wenn die erforderlichen Belege oder Fähigkeiten fehlen.