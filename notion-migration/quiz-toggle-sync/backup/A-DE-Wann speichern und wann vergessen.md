# Wann speichern und wann vergessen

Notion page: https://app.notion.com/p/Wann-speichern-und-wann-vergessen-3779418319f3806996fbda4b183924d9
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Du entwickelst eine kurze Memory-Retention-Policy in Form von drei Regeln, die ein Agent konsistent anwenden kann. Anschließend testest du diese Regeln anhand neuer Gesprächsdaten aus einem anderen Kontext: HR-Onboarding statt Finanzdienstleistungs-Support. 
Eine Memory-Retention-Policy beschreibt die Regeln dafür, welche Informationen ein Agent speichern, verwerfen oder nur mit Einwilligung behalten darf.


## Den Kontext setzen
Du hast jetzt gesehen, wie einzelne Informationen aus einem Gespräch den Kategorien Merken, Verwerfen und Einwilligung einholen zugeordnet werden. Diese Einordnung allein reicht jedoch nicht aus. Damit ein Agent konsistent handeln kann, braucht er eine Policy – also ein klares Regelwerk, das er auf jedes neue Gespräch anwenden kann, ohne jede Entscheidung von Grund auf neu treffen zu müssen.
In dieser Lektion entwickelst du eine solche Policy selbst und testest sie anschließend anhand neuer Gesprächsdaten aus einem anderen Geschäftskontext. Dieser Kontextwechsel ist wichtig: Eine gute Policy funktioniert nicht nur in einem einzelnen Anwendungsfall, sondern lässt sich auch auf andere Situationen übertragen.

## Was eine Memory-Retention-Policy abdeckt
Eine Memory-Retention-Policy definiert drei Dinge:
- Relevanz. Was qualifiziert Informationen überhaupt dafür, gespeichert zu werden? Nicht alles, was ein Kunde sagt, ist für zukünftige Interaktionen relevant. Die Policy braucht klare Kriterien, um dauerhaft relevante Informationen von vorübergehendem Gesprächskontext zu unterscheiden.
- Datenschutz. Welche Daten dürfen unter keinen Umständen im Memory gespeichert werden? Dazu gehören sensible persönliche Identifikatoren, Finanzzugangsdaten und gesundheitsbezogene Informationen, die durch die DSGVO (das EU-Gesetz zu personenbezogenen Daten) geschützt sind. Daten in dieser Kategorie sollten entweder sofort verworfen oder an ein sicheres System weitergeleitet werden, das für die Verarbeitung solcher Daten vorgesehen ist.
- Einwilligung. Welche Daten sind nützlich genug, um gespeichert zu werden, aber gleichzeitig so persönlich, dass vor der Speicherung die ausdrückliche Zustimmung des Kunden eingeholt werden muss? Der Agent sollte in diesen Fällen nachfragen. Informationen ohne Einwilligung zu speichern, kann das Vertrauen des Kunden beeinträchtigen und unter Umständen gegen gesetzliche Vorgaben verstoßen.

## Wie du an dieser Lektion arbeitest
Du brauchst einen Ort, an dem du deine Antworten schreiben kannst. Wähle eine Option:
>  
  - Empfohlen. Erstelle eine Kopie dieser Google-Sheets-Vorlage — sie ist in drei Tabs strukturiert, die den Teilen A, B und C entsprechen, mit Prompts an den richtigen Stellen und einem Dropdown für die Kategoriespalte.
- Ein leeres Dokument auf deinem Computer.
- Ein Blatt Papier.
Egal, wofür du dich entscheidest: Arbeite die Teile A → B → C der Reihe nach durch. Schau nicht unten in den Antwortschlüssel, bevor du deine eigenen Entscheidungen getroffen hast.

## Teil A — Die Regeln entwerfen
Schreibe ein kurzes Regelbuch. Schreibe für jede der drei oben genannten Kategorien ein oder zwei Sätze, die die Regel klar genug definieren, damit jemand sie implementieren kann.
Deine Regeln sollten spezifisch und handlungsorientiert sein. Vermeide vage Formulierungen wie „nützliche Dinge speichern“ oder „sensible Daten vermeiden“. Eine gute Regel sagt dem Agenten genau, welche Bedingung erfüllt sein muss, bevor eine Aktion ausgeführt wird.
Beispiele für das Maß an Spezifität, das du anstreben solltest:
- „Speichere Informationen nur, wenn sie ein stabiles Kundenattribut beschreiben, das wahrscheinlich länger als sechs Monate korrekt bleibt und verbessert, wie zukünftige Interaktionen personalisiert werden.“
- „Speichere niemals Finanzzugangsdaten, staatliche Identifikatoren oder Daten, die nach DSGVO als besondere Kategorie personenbezogener Daten klassifiziert sind.“
Schreibe je eine Regel für: Relevanz, Datenschutz, Einwilligung.

## Teil B — Deine Regeln anwenden
Contigos HR-Onboarding-Agent hat fünf Datenpunkte aus einem Gespräch mit einem neuen Mitarbeiter in seiner ersten Woche extrahiert. Wende deine Regeln aus Teil A auf jedes Element an. Klassifiziere es als Merken, Verwerfen / Weiterleiten oder Einwilligung einholen und schreibe einen Satz, der erklärt, wie deine Regel die Entscheidung begründet.
1. „Ich möchte alle internen Mitteilungen lieber auf Englisch statt auf Deutsch erhalten.“
1. „Mein Notfallkontakt ist mein Partner, Stefan Krause, und seine Nummer ist +49 151 2345 6789.“
1. „Ich habe eine chronische Rückenbeschwerde und werde einen ergonomischen Arbeitsplatz benötigen.“
1. „Meine Bankverbindungsdaten für die Gehaltsabrechnung lauten: IBAN DE44 2004 1155 0534 3400 00.“
1. „Ich arbeite morgens am besten und würde alle Trainingssessions gerne vor 12:00 Uhr haben.“

## Teil C — Jede Entscheidung konkret machen
Klassifizierung allein sagt dem Agenten nicht, was er als Nächstes tun soll. Mache für jedes Element aus Teil B je nach zugewiesener Kategorie eine konkrete Sache:
- Für Merken-Elemente. Schreibe den Satz, den der Agent in der nächsten Interaktion mit dieser Person verwenden könnte, um zu zeigen, dass er die Information sinnvoll und nützlich behalten hat. Beispiel: „Ich habe Ihre Präferenz für englische Kommunikation vermerkt — ich werde auch künftig Englisch verwenden.“
- Für Verwerfen / Weiterleiten-Elemente. Nenne die Art von System, das diese Daten stattdessen enthalten sollte (z. B. HR-Profilsystem, Gehaltsabrechnungssystem, sicherer Verifizierungsdienst), und schreibe einen Satz, der erklärt, warum dieses System der richtige Ort dafür ist — und das Gesprächs-Memory des Agenten nicht.
- Für Einwilligung einholen-Elemente. Schreibe die exakte ein- oder zweisätzige Anfrage, die der Agent an die Person richten sollte, bevor er die Information speichert.
Hier wird aus Klassifizierung eine operative Entscheidung. Nicht nur „in welche Kategorie fällt das?“, sondern „was tut oder sagt der Agent als Nächstes wortwörtlich?“

## Checkpoints
Nutze diese, wenn du unsicher bist oder Orientierung brauchst.
1. Deine Relevanzregel testen. Überlege, ob die Information in sechs Monaten noch korrekt und nützlich wäre. Wenn sie sich wahrscheinlich häufig ändert oder schnell irrelevant wird, gehört sie vermutlich nicht ins Langzeit-Memory. Frag dich: Würde der Agent diese Information in einer zukünftigen Interaktion tatsächlich nutzen oder würde sie lediglich zusätzliches Rauschen erzeugen?
1. Deine Datenschutzregel testen. Überlege, was passieren würde, wenn ohne Autorisierung auf das Memory-Protokoll zugegriffen würde. Finanzzugangsdaten und Gesundheitsdaten bergen das höchste Risiko. Nach DSGVO sind gesundheitsbezogene Angaben besondere Kategorien personenbezogener Daten — sie erfordern eine ausdrückliche Rechtsgrundlage, bevor sie irgendwo gespeichert werden dürfen, auch im Gesprächs-Memory.
1. Deine Einwilligungsregel testen. Überlege, wie sich eine Person fühlen würde, wenn sie erfahren würde, dass diese Information ohne ihr Wissen gespeichert wurde. Wenn die Antwort „unwohl“ oder „überrascht“ lautet, gehört die Information wahrscheinlich in die Kategorie „Einwilligung einholen“ und sollte nicht ohne Zustimmung gespeichert werden.



[toggle] Antwortschlüssel — Klassifizierungen für Teil B
  [TABLE]
    | Datenpunkt | Kategorie | Begründung |
    | Präferenz für englische Kommunikation | Merken | Stabil, sachlich, direkt nützlich für die Personalisierung zukünftiger Interaktionen, ohne Datenschutzbedenken auszulösen. |
    | Notfallkontaktdaten | Verwerfen / Weiterleiten | Ein sensibler persönlicher Identifikator, der in ein strukturiertes HR-System gehört, nicht ins Gesprächs-Memory. |
    | Chronische Rückenbeschwerde | Einwilligung einholen | Gesundheitsangaben sind besondere Kategorien personenbezogener Daten nach DSGVO — der Agent muss vor dem Speichern nachfragen, auch wenn die daraus folgende ergonomische Präferenz nützlich ist. |
    | Gehaltsabrechnungs-IBAN | Verwerfen / Weiterleiten | Finanzzugangsdaten dürfen niemals im Gesprächs-Memory liegen. An das Gehaltsabrechnungssystem weiterleiten. |
    | Präferenz für Training am Morgen | Merken | Stabil, nützlich für die Planung zukünftiger Sessions und nicht sensibel genug, um Einwilligung zu erfordern. |
[toggle] Antwortschlüssel — Beispielausgaben für Teil C
  Merken-Elemente
  - Englische Kommunikation: „Willkommen zurück — ich werde unsere Gespräche weiterhin auf Englisch führen, wie Sie es bevorzugen.“
  - Training am Morgen: „Ich habe vermerkt, dass Sie morgens am besten arbeiten, deshalb priorisiere ich Trainingsslots vor 12:00 Uhr, wenn wir das nächste Mal planen.“
  Verwerfen / Weiterleiten-Elemente
  - Notfallkontakt → HR-Profilsystem. Dieses System hält Notfallkontaktdaten strukturiert, gesichert und auditierbar. Gesprächs-Memory verfügt nicht über Zugriffskontrollen, die für diese Daten geeignet sind.
  - Gehaltsabrechnungs-IBAN → Gehaltsabrechnungssystem. Es ist darauf ausgelegt, Finanzzugangsdaten mit angemessener Verschlüsselung und Zugriffskontrollen zu verarbeiten. Ein Transkriptprotokoll ist das nicht.
  Einwilligung einholen-Elemente
  - Rückenbeschwerde: „Danke, dass Sie mir das mitgeteilt haben. Möchten Sie, dass ich Ihren Bedarf an einem ergonomischen Arbeitsplatz vermerke, damit zukünftige Onboarding-Schritte ihn berücksichtigen? Da dies ein gesundheitsbezogenes Detail betrifft, möchte ich vor dem Speichern Ihre Erlaubnis einholen.“

## Verständnis prüfen
### Frage 1
>  Ein Contigo-Kunde legt während einer routinemäßigen Kontoanfrage unerwartet eine medizinische Erkrankung offen. Welche Antwort beschreibt am besten, wie ein gut entworfenes Regelbuch zur Memory-Retention damit umgehen sollte?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7e0cbd1e-db6c-4c8e-88c3-f25e1f2b9371

### Frage 2
>  Contigo muss gegenüber EU-Regulierungsbehörden nachweisen, dass sein Agent die Einwilligung von Kunden rechtmäßig handhabt. Welcher Ansatz erzeugt am effektivsten einen auditierbaren Nachweis von Einwilligungsentscheidungen?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/982e6ec3-1f44-48e6-b474-9d0b8cfbb1cf

> 💡 Takeaway: 
  Eine Memory-Retention-Policy ist eine bewusste Designentscheidung und keine Standardeinstellung. Sie legt fest, welche Informationen ein Agent speichern soll, welche er speichern darf und welche er unter keinen Umständen speichern sollte. Ohne klare Regeln speichert ein Agent alles, was in einem Gespräch erwähnt wird – sowohl nützliche als auch sensible Informationen. In regulierten Kontexten ist das nicht nur unachtsam, sondern kann erhebliche Datenschutz- und Compliance-Risiken mit sich bringen.
  Beachte außerdem, dass die Regeln, die du formuliert hast, bewusst kurz gehalten sind. Das ist ein Vorteil: Eine Policy, die sich nicht in wenigen klaren Sätzen beschreiben lässt, wird wahrscheinlich nicht konsistent über Tausende von Gesprächen hinweg angewendet.