# Projekteinführung

Notion page: https://app.notion.com/p/Projekteinf-hrung-3779418319f380ba9ff7efc6eaca55d8
Backed up before n8n migration

> 💡 In dieser Lektion lernst du das Projekt kennen. Du arbeitest an drei Policies: Memory, Gespräch und Self-Assessment. Damit zeigst du, dass du die Agenten-Memory-Architektur verstehst und sie in deinem Agenten-Workflow anwenden kannst.. Du erstellst eine schriftliche Memory-Policy, führst einen Multi-Turn-Gesprächstest mit deinem konfigurierten Chatflow durch und absolvierst ein Wissensquiz. Alle drei Aufgaben musst du erledigen.

> 🔥 Bevor du startest, kopier dir diese Google-Sheets-Vorlage. Sie hat drei Tabs, die zum Assessment passen: Memory-Policy, Gesprächstestprotokoll und Self-Assessment-Zusammenfassung. Trag jeden Turn aus Aufgabe 2 in die Vorlage ein, bevor du dir das erwartete Verhalten in der Lektion anschaust. Nur so wird daraus eine echte Validierung und keine bloße Bestätigung. Das Wissensquiz aus Aufgabe 3 machst du auf der Plattform, nicht in der Vorlage.


## Kontext
Sprint 1 hat dich durch den gesamten Bogen von Agenten-Memory geführt. Du hast verstanden, warum zustandslose Modelle in Geschäftsgesprächen scheitern. Du hast gelernt, wie sich Memory, Wissensdatenbanken und Tools unterscheiden. Du hast Buffer Memory, Session IDs und Buffer Window Memory. Und du hast die Regeln definiert, die festlegen, was ein Agent speichern sollte und was nicht.
In diesem Assessment führst du diese Teile zusammen. Das Szenario ist der Support-Agent der Contigo GmbH, den du im Laufe des Sprints gebaut und verfeinert hast. Er steht jetzt kurz vor einem Production-Readiness-Review. Bevor er für echte Kunden live gehen kann, braucht das Team einen dokumentierten Nachweis: Memory wurde bewusst entworfen und nicht einfach nur konfiguriert und sich selbst überlassen.


## Aufgabe 1: Memory-Policy validieren
Geh die drei folgenden Policy-Kategorien durch. Schreib für jede Kategorie deine Regel in eigenen Worten auf, bevor du dir die Musterantwort anschaust. Prüf deine Regel anhand der erwarteten Kriterien. Hake den Checkpoint nur ab, wenn deine Regel alle drei aufgeführten Kriterien erfüllt.


Checkpoint 1A: Relevanzregel
Schreib eine Regel aus ein bis zwei Sätzen. Sie soll festlegen, welche Kundeninformationen sich für die Speicherung im Buffer-Window-Memory-Node deines Chatflows qualifizieren. Deine Regel muss so konkret sein, dass ein Entwickler sie direkt in einem System-Prompt umsetzen kann.

> 🔽 Erwartete Antwort: Relevanz
  Eine starke Relevanzregel erfüllt alle drei folgenden Kriterien:
  - Sie legt eine klare, testbare Bedingung fest: Zum Beispiel „Informationen, die der Agent verwenden würde, um die aktuelle oder eine zukünftige Interaktion zu personalisieren, ohne den Kunden zu bitten, sich zu wiederholen“
  - Sie lässt sich konsistent auf verschiedene Datentypen anwenden: Eine angegebene Kommunikationspräferenz, eine offene Fallreferenz und ein Produktinteresse sollten alle nach derselben Regel bestehen oder durchfallen.
  - Sie schließt vorübergehende Daten aus: Der emotionale Zustand eines Kunden, ein einmaliges Verifizierungsdetail oder Informationen, die sich häufig ändern, sollten sich nicht qualifizieren.
  Beispiel für eine starke Regel: Speichere nur Informationen, die sachlich sind, über die Session hinweg stabil bleiben und für die laufende Interaktion des Kunden direkt relevant sind. Der Agent muss sie in einem späteren Turn auch wirklich brauchen können.

  Beispiel für eine schwache Regel: Speichere alles Nützliche, was der Kunde erwähnt.

Checkpoint 1B: Datenschutzregel
Schreibe eine Regel aus ein bis zwei Sätzen, die definiert, was unter keinen Umständen in den Gesprächsverlauf deines Chatflows geschrieben werden darf.
> 🔽 Erwartete Antwort: Datenschutz
  Eine starke Datenschutzregel erfüllt alle drei folgenden Kriterien:
  - Sie nennt spezifische Datenkategorien: Finanzzugangsdaten, staatlich ausgestellte Identifikatoren und Gesundheitsangaben müssen klar genannt werden.
  - Sie legt den korrekten Umgangspfad fest: Sensible Daten müssen entweder über einen sicheren Tool-Aufruf weitergeleitet oder sofort fallengelassen werden; sie dürfen nicht im Gesprächsverlauf verbleiben.
  - Sie verweist auf den regulatorischen Kontext: DSGVO und EU-Finanzdienstleistungsregulierung sind die anwendbaren Rahmenbedingungen für Contigo.
  Beispiel für eine starke Regel: IBANs, Geburtsdaten, nationale Identitätsnummern und Gesundheitsangaben dürfen niemals im Gesprächsverlauf verbleiben. IBANs müssen an ein sicheres Tool übergeben und verworfen werden. Diese Fähigkeit wird dein Chatflow später haben. Gesundheitsangaben müssen sofort fallengelassen werden, es sei denn, der Kunde hat ausdrücklich eingewilligt.
  Beispiel für eine schwache Regel: Speichere keine sensiblen Informationen.

Checkpoint 1C: Einwilligungsregel
Schreib eine Regel aus ein bis zwei Sätzen. Sie soll festlegen, wofür der Agent vor der Speicherung die ausdrückliche Erlaubnis des Kunden braucht, und was er tun soll, wenn der Kunde ablehnt.

> 🔽 Erwartete Antwort: Einwilligung
  Eine starke Einwilligungsregel erfüllt alle drei folgenden Kriterien:
  - Sie beschreibt die Datenkategorie, die zwischen autonomer Speicherung und vollständigem Verbot liegt. Gemeint sind persönliche Präferenzen mit sensiblen Angaben, zum Beispiel Barrierefreiheitsbedürfnisse oder Kommunikationspräferenzen, die mit einer gesundheitlichen Einschränkung zusammenhängen.
  - Sie legt das genaue Agentenverhalten fest: Der Agent muss vor dem Speichern fragen, nicht erst speichern und dann informieren.
  - Sie definiert den Ablehnungspfad: Wenn der Kunde ablehnt, wendet der Agent die Präferenz nur für die aktuelle Session an und schreibt nichts ins Memory.
  Beispiel für eine starke Regel: Speichere Informationen über persönliche Umstände eines Kunden nur, nachdem du ausdrücklich gefragt und eine klare Bestätigung erhalten hast. Wenn der Kunde ablehnt, wende die Präferenz nur innerhalb der aktuellen Session an und schreibe sie nicht ins Memory.
  Beispiel für eine schwache Regel: Frage Kunden, bevor du persönliche Informationen speicherst.

### Aufgabe 2: Chatflow-Gespräch validieren
Führ das folgende Gespräch mit fünf Turns. Prüf nach jedem Turn die Antwort deines Agenten anhand des erwarteten Verhaltens, bevor du weitermachst. Schau dir das erwartete Verhalten erst an, nachdem du die tatsächliche Antwort des Agenten beobachtet und dokumentiert hast. Dieser Test prüft nur das, wofür dein Chatflow in Sprint 1 gebaut wurde: Memory-Recall über Turns hinweg, Session-Isolation und Context-Window-Management.

Turn 1 - Senden: „Hallo, mein Name ist Markus Bauer und meine offene Fallreferenz ist CG-4821. Ich rufe wegen einer Anfrage zur Kreditrestrukturierung an.“
🔽 Erwartetes Verhalten: Turn 1
Der Agent sollte Markus' Namen und Fallreferenz aufgreifen und bestätigen, dass er bei der Restrukturierungsanfrage helfen kann. Die Fallreferenz CG-4821 und der Name sind sachlich, stabil und direkt relevant. Nach der Relevanzregel qualifizieren sie sich für die Speicherung.
✅ Bestanden: Agent erkennt Namen und Fallreferenz an und fährt natürlich fort.
❌ Nicht bestanden: Agent ignoriert die Fallreferenz oder bittet Markus, seinen Namen zu wiederholen.

Turn 2 - Senden: „Ich sollte erwähnen, dass ich eine leichte Hörbeeinträchtigung habe, deshalb bevorzuge ich immer schriftliche Kommunikation statt telefonischer Rückrufe.“
🔽 Erwartetes Verhalten: Turn 2
Diese Angabe ist eine besondere Kategorie personenbezogener Daten nach DSGVO, da sie mit einer gesundheitlichen Einschränkung verbunden ist. Der Agent muss ausdrücklich um Einwilligung bitten, bevor er sie speichert. Er sollte die Präferenz unabhängig von der Entscheidung des Kunden für die aktuelle Session anwenden.
✅ Bestanden: Agent fragt Markus, ob er der Speicherung dieser Präferenz zustimmt, bevor etwas ins Memory geschrieben wird.
❌ Nicht bestanden: Agent speichert die Präferenz ohne Nachfrage oder ignoriert die Angabe vollständig.

Turn 3 - Senden: „Ja, Sie können diese Präferenz speichern.“
🔽 Erwartetes Verhalten: Turn 3
Der Agent hat ausdrückliche Einwilligung erhalten. Er sollte bestätigen, dass die Präferenz vermerkt wurde, und das Gespräch natürlich fortsetzen.
✅ Bestanden: Agent bestätigt die Speicherung und erkennt die Präferenz an.
❌ Nicht bestanden: Agent bestätigt die Speicherung nicht oder erkennt die gegebene Einwilligung nicht an.

Turn 4 - Senden: „Gut. Können Sie mir bezüglich Fall CG-4821 sagen, wie ich heiße und weswegen ich angerufen habe?“
🔽 Erwartetes Verhalten: Turn 4
Dieser Turn testet den Memory-Recall über mehrere Turns hinweg. Der Agent muss Markus Bauer und CG-4821 aus seinem Arbeits-Memory abrufen, ohne dass Markus sie wiederholen muss. Diese Angaben wurden in Turn 1 festgelegt. Das zeigt, dass dein Buffer-Window-Memory-Node den Gesprächsverlauf korrekt behält und einspeist.
✅ Bestanden: Agent ruft den Namen und die Fallreferenz korrekt ab, ohne nachzufragen.
❌ Nicht bestanden: Agent bittet Markus, eine der beiden Informationen zu wiederholen, oder kann sie nicht abrufen.

Turn 5 - Senden: „Und nur zur Bestätigung — werden Sie mich telefonisch oder schriftlich kontaktieren?“
🔽 Erwartetes Verhalten: Turn 5
Dieser Turn testet, ob die mit Einwilligung gespeicherte Präferenz aus Turn 2 und Turn 3 korrekt angewendet wird. Der Agent sollte schriftliche Kommunikation bestätigen und dabei auf die gespeicherte Präferenz Bezug nehmen, ohne Markus zu bitten, sie zu wiederholen.
✅ Bestanden: Agent bestätigt schriftliche Kommunikation und zeigt damit, dass die gespeicherte Präferenz korrekt integriert ist.
❌ Nicht bestanden: Agent verweist nicht auf die gespeicherte Präferenz, bittet Markus, sie zu wiederholen, oder wählt standardmäßig telefonischen Kontakt.

### Selbstbewertungsrubrik
Nach den sechs Runden nimmst du dein Ergebnis unter die Lupe. Nutze dafür einfach dieses Bewertungsraster:
[TABLE]
  | Ergebnis | Kriterien |
  | ✅ Vollständig bestanden | Alle fünf Turns bestanden. Memory-Recall, Einwilligungshandhabung und Session-Verhalten sind korrekt implementiert. |
  | ⚠️ Teilweise bestanden | Drei oder vier Turns bestanden. Identifiziere, welche Kategorie fehlgeschlagen ist, und überarbeite die relevante System-Prompt-Anweisung, bevor du zu Sprint 2 übergehst. |
  | ❌ Überarbeitung erforderlich | Zwei oder weniger Turns bestanden. Überprüfe deine Buffer-Window-Memory-Konfiguration und den System-Prompt, bevor du erneut testest. Fahre nicht mit Sprint 2 fort, bis dies gelöst ist. |

## Aufgabe 3: Wissensquiz
Hier warten vier Fragen auf dich. Gehe die Optionen am besten in Ruhe durch, bevor du dich entscheidest.
### Frage 1
>  Ein Contigo-Kunde gibt während eines Gesprächs seine IBAN an. Dein aktueller Chatflow hat noch keine Tool-Verbindungen. Was ist gemäß Memory-Best-Practices derzeit das korrekte Verhalten des Agenten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/6a91f354-008a-49b0-ac46-231afa2502c6

### Frage 2
>  Was ist der Hauptzweck der Konfiguration einer eindeutigen Session ID im Buffer-Window-Memory-Node deines Chatflows?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/507c27b2-5ce3-42d8-bd81-53a5cce663fa

### Frage 3
>  Du hast für den Contigo-Agenten eine Buffer-Window-Memory-Größe von 4 eingestellt. Ein Kunde gibt seine Fallreferenz in Turn 1 an und fragt in Turn 7 danach. Der Agent kann sie nicht abrufen. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d85f4afc-1002-48bc-9ba3-59f13ddfc133

### Frage 4
>  Ein Contigo-Agent speichert den emotionalen Zustand eines Kunden „frustriert und ungeduldig“ aus Turn 3, und dieser bleibt bis Turn 8 im aktiven Fenster. Welche zwei Memory-Best-Practice-Regeln verletzt dies am deutlichsten? Wähle alle zutreffenden Antworten aus.
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/98be04d0-1632-4d35-9325-9beee8da0623

## Assessment abgeschlossen
Hast du die drei Aufgaben gemeistert? Dann steht Sprint 2 nichts mehr im Weg. Die Memory-Grundlage, die du hier validiert hast, sichert deine nächsten Schritte ab. Die Wissensdatenbank und die RAG-Pipeline des kommenden Sprints funktionieren nämlich nur dann reibungslos, wenn sie auf einer stabilen, klar definierten Memory-Schicht aufsetzen.