# Was sollte der Agent sich merken?

Notion page: https://app.notion.com/p/Was-sollte-der-Agent-sich-merken-3779418319f380ddb454ce1bc029ad26
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Du gehst mit uns ein Kundengespräch durch und klassifizierst jede Information, die der Kunde teilt — du entscheidest, was der Agent sich merken sollte, was er verwerfen sollte und für welche Informationen er vor dem Speichern eine Einwilligung einholen sollte.

## Den Kontext setzen
Das Entwicklungsteam der Contigo GmbH hat bereits geklärt, dass der Support-Agent eine Memory-Funktion braucht. Die schwierigere Frage lautet nun: Welche Informationen sollte der Agent aus einem Kundengespräch tatsächlich dauerhaft behalten?
Das ist aus drei Gründen wichtig: Wenn der Agent zu viel speichert, wird sein Gesprächsverlauf mit irrelevanten Informationen (Noise) überladen und es wird schwieriger, die relevanten Inhalte wiederzufinden. Wenn er zu wenig speichert, verliert er Kontext, den der Kunde bei späteren Interaktionen möglicherweise voraussetzt. Und in einem regulierten Umfeld wie dem EU-Finanzdienstleistungssektor kann das Speichern der falschen Informationen — etwa eines Finanzidentifikators oder einer Gesundheitsangabe — ein Compliance-Risiko darstellen.
Das Ziel dieser Schritt-für-Schritt-Analyse (Walkthroughs) ist es, die Entscheidungslogik sichtbar zu machen, damit du bei einem neuen Gespräch besser einschätzen kannst, welche Informationen gespeichert werden sollten und welche nicht.
## Die drei Kategorien
Du wirst jede relevante Information aus dem Gespräch in eine dieser drei Kategorien einsortieren:
- Merken. Die Information kann sicher gespeichert werden und ist für zukünftige Interaktionen tatsächlich hilfreich. Ihre Speicherung ermöglicht es dem Agenten, den Kunden bei späteren Gesprächen besser zu unterstützen, ohne Datenschutz- oder Compliance-Risiken zu verursachen.
- Verwerfen. Die Information ist nur vorübergehend relevant, für zukünftige Interaktionen nicht hilfreich oder so sensibel, dass ihre Speicherung im Gesprächs-Memory ein unangemessenes Risiko darstellen würde. Manche verworfene Informationen werden an spezialisierte Systeme weitergeleitet, die für die Verarbeitung solcher Daten vorgesehen sind – zum Beispiel an den Kontoänderungsdienst einer Bank. Andere werden nach der aktuellen Interaktion nicht weiter gespeichert.
- Einwilligung einholen. Die Information wäre für zukünftige Interaktionen hilfreich, ist jedoch so persönlich, dass vor der Speicherung ausdrücklich die Zustimmung des Kunden eingeholt werden sollte. Der Agent sollte den Kunden fragen, bevor er die Information dauerhaft im Langzeit-Memory speichert.
![image]((notion-hosted file))

## Das Gespräch
Lies diesen Austausch zwischen einem Contigo-Kunden und dem Support-Agenten durch. Wir kommen fünfmal darauf zurück.
> Agent: Willkommen zurück beim Contigo-Support. Wie kann ich Ihnen heute helfen?
  Kunde: Hallo. Ich muss die IBAN auf meinem Konto für Lastschriften aktualisieren. Die neue lautet DE89 3704 0044 0532 0130 00.
  Agent: Ich kann Ihnen dabei helfen. Könnten Sie zur Verifizierung Ihr Geburtsdatum bestätigen?
  Kunde: Ja, es ist der 14. März 1981. Außerdem möchte ich darauf hinweisen, dass ich in letzter Zeit wirklich frustriert mit der mobilen App bin. Sie stürzt immer wieder ab, wenn ich versuche, meine Kontoauszüge anzusehen.
  Agent: Das tut mir leid. Ich werde das App-Problem protokollieren. Gibt es noch etwas?
  Kunde: Ja. Ich habe mich kürzlich scheiden lassen, deshalb hat sich mein Nachname geändert. Ich heiße jetzt Katarina Brandt, nicht Katarina Fischer. Bitte aktualisieren Sie mein Profil. Außerdem habe ich eine leichte Angststörung, die längere Telefonate manchmal schwierig macht, deshalb bevorzuge ich nach Möglichkeit immer schriftliche Kommunikation.
In diesem Austausch tauchen fünf unterschiedliche Datenpunkte auf:
1. Die neue IBAN: DE89 3704 0044 0532 0130 00
1. Das Geburtsdatum: 14 March 1981
1. Die Frustration über die abstürzende mobile App
1. Die rechtliche Namensänderung zu Katarina Brandt
1. Die Präferenz für schriftliche Kommunikation, verbunden mit einer Angststörung
Wir gehen jeden einzelnen Punkt durch und entscheiden, was der Agent damit macht.

## Die fünf Datenpunkte durchgehen
### 1. Die IBAN
Zuerst fragen: Ist das für zukünftige Interaktionen nützlich, und ist es sicher, es im Gesprächs-Memory zu behalten?
Eine IBAN ist ein sensibler Finanzidentifikator. Es gibt keine Version von „zukünftiger Nützlichkeit“, die rechtfertigt, sie in einem Transkriptprotokoll liegen zu lassen. Wenn später jemand Zugriff auf den Gesprächsverlauf erhält — durch ein Leck, eine falsch konfigurierte Berechtigung, einen Export — erhält diese Person Zugriff auf das Konto.
Die Entscheidung: Verwerfen.
Die IBAN wird nicht im Sinne von „vergessen und ignoriert“ fallengelassen. Sie wird direkt an das System übergeben, das tatsächlich Kontoänderungen verarbeitet — einen sicheren Banking-Dienst — und nicht im Gesprächs-Memory behalten. Der Agent verwendet die Information für den vorgesehenen Zweck, leitet sie an das zuständige System weiter und speichert sie anschließend nicht weiter.

### 2. Das Geburtsdatum
Das Geburtsdatum ist nur aus einem einzigen Grund aufgetaucht: Verifizierung. Der Agent hat danach gefragt, der Kunde hat es angegeben, und sobald die Identitätsprüfung bestanden ist, hat der Agent keine weitere Verwendung dafür.
Wenn der Agent es trotzdem speichern würde, hättest du ein personenbezogenes Detail in einem Gesprächsprotokoll ohne zukünftigen Nutzen. Das hat nur Nachteile.
Die Entscheidung: Verwerfen.
Für die Verifizierung verwendet, dann fallengelassen. Dasselbe Muster wie bei der IBAN — einmal für einen bestimmten Zweck berührt, niemals ins Memory geschrieben.

### 3. Die Frustration über die mobile App
Dieser Punkt fühlt sich anders an als die vorherigen beiden — er ist kein sensibler Identifikator. Es ist eine emotionale Reaktion auf ein technisches Problem. Lohnt es sich also, sie zu merken?
Frag dich, wie das nächste Gespräch aussieht, wenn der Agent sich daran erinnert. „Beim letzten Mal haben Sie erwähnt, dass die App abgestürzt ist — passiert das immer noch?“ klingt theoretisch aufmerksam, aber das App-Problem könnte bereits behoben sein oder ein einmaliges Ereignis gewesen sein. Die Frustration war an einen bestimmten Moment gebunden. Sie als dauerhafte Eigenschaft dieses Kunden mitzunehmen — „diese Person ist mit der App unzufrieden“ — führt in der nächsten Interaktion eher in die Irre, als zu helfen.
Die Entscheidung: Verwerfen.
Das App-Problem wird dort erfasst, wo technische Fehlerberichte hingehören – beispielsweise in einem Produktfeedback- oder Ticketsystem, nicht im Memory des Agenten. Die geäußerte Frustration des Kunden ist jedoch an eine konkrete Situation gebunden und sollte daher nicht dauerhaft im Gesprächs-Memory gespeichert werden.

### 4. Die rechtliche Namensänderung
Eine Namensänderung ist für zukünftige Interaktionen eindeutig relevant. Der Agent muss wissen, wie er den Kunden künftig ansprechen soll. Auf den ersten Blick scheint dies also ein klarer Fall für die Kategorie „Merken“ zu sein.
Aber stopp. Wo gehört eine Namensänderung hin? Sie gehört in das offizielle Profil des Kunden — den autoritativen Datensatz, den die Bank für diesen Kunden führt. Wenn der Agent „der Name des Kunden ist jetzt Katarina Brandt“ nur in sein eigenes Gesprächs-Memory schreibt, hast du eine Schattenversion der Wahrheit erzeugt, die vom offiziellen Datensatz abweichen kann. Die nächste Agenteninstanz oder das nächste System, das mit diesem Kunden arbeitet, sieht die Aktualisierung nicht, es sei denn, sie liest zufällig dasselbe Gesprächsprotokoll.
Die Entscheidung: Aus dem Gesprächs-Memory verwerfen. An das System weiterleiten, das das offizielle Kundenprofil enthält.
Das ist der subtile Punkt. „Verwerfen“ bedeutet nicht „diese Information ist unwichtig“ — es bedeutet „diese Information gehört nicht speziell ins Gesprächs-Memory“. Manche Dinge werden gerade deshalb aus dem Memory verworfen, weil sie wichtig genug sind, um an einen zuverlässigeren Ort zu gehören.
Allerdings stellt sich die Frage: Wo gehört eine Namensänderung eigentlich hin? Sie gehört in das offizielle Kundenprofil – also in den maßgeblichen Datensatz, den die Bank für diesen Kunden führt. Wenn der Agent die Information „Der Name des Kunden lautet jetzt Katarina Brandt“ lediglich in seinem Gesprächs-Memory speichert, entsteht eine zweite Informationsquelle, die von den offiziellen Kundendaten abweichen kann. Andere Agenten oder Systeme sehen die Aktualisierung möglicherweise nicht, sofern sie nicht auf denselben Gesprächsverlauf zugreifen.
Die Entscheidung: Nicht im Gesprächs-Memory speichern. Stattdessen sollte die Information an das System weitergeleitet werden, das das offizielle Kundenprofil verwaltet.
Hier zeigt sich ein wichtiger Unterschied: „Verwerfen“ bedeutet nicht, dass eine Information unwichtig ist. Es bedeutet lediglich, dass sie nicht im Gesprächs-Memory gespeichert werden sollte. Manche Informationen werden gerade deshalb nicht im Gesprächs-Memory gespeichert, weil sie wichtig genug sind, um an einer zuverlässigeren und zentralen Stelle verwaltet zu werden.

### 5. Die Kommunikationspräferenz
Der Kunde hat angegeben, dass er schriftliche Kommunikation bevorzugt, und erklärt auch den Grund dafür: eine leichte Angststörung.
Wenn der Agent sich diese Präferenz merkt, können zukünftige Interaktionen standardmäßig über schriftliche Kanäle erfolgen, ohne dass der Kunde seine Präferenz erneut erklären muss. Das verbessert die Nutzererfahrung spürbar und macht diese Information zu einem starken Kandidaten für die Kategorie „Merken“.
Allerdings gibt es einen wichtigen Aspekt zu beachten: Der Grund für diese Präferenz ist eine Gesundheitsangabe. Nach der Datenschutz-Grundverordnung (DSGVO) gelten Gesundheitsdaten als besondere Kategorien personenbezogener Daten und unterliegen besonderen Schutzanforderungen. Das bedeutet, dass solche Informationen nicht ohne Weiteres gespeichert werden dürfen. Vor einer Speicherung muss der Kunde ausdrücklich zustimmen.
Die Entscheidung: Einwilligung einholen.
Der Agent sollte etwa so antworten:
> „Danke, dass Sie mir das mitgeteilt haben. Möchten Sie, dass ich Ihre Präferenz für schriftliche Kommunikation vermerke, damit zukünftige Interaktionen standardmäßig darauf ausgerichtet sind? Da dies ein gesundheitsbezogenes Detail betrifft, möchte ich vor dem Speichern Ihre Erlaubnis einholen.“
Wenn der Kunde zustimmt, kann die Präferenz gespeichert werden. Lehnt er dies ab, sollte der Agent die Präferenz während der aktuellen Interaktion berücksichtigen, sie jedoch nicht dauerhaft speichern.

## Das Muster, das sichtbar wird
Beachte, was bei den fünf Elementen passiert ist:
[TABLE]
  | Datenpunkt | Kategorie | Grund |
  | IBAN | Verwerfen | Sensibler Finanzidentifikator — gehört in ein sicheres Banking-System, nicht in ein Transkript |
  | Geburtsdatum | Verwerfen | Einmalig zur Verifizierung verwendet, kein zukünftiger Nutzen |
  | App-Frustration | Verwerfen | Vorübergehende emotionale Reaktion, an einen Moment gebunden, geringer zukünftiger Signalwert |
  | Rechtliche Namensänderung | Verwerfen | Gehört ins offizielle Kundenprofil, nicht ins Memory |
  | Kommunikationspräferenz | Einwilligung einholen | Wirklich nützlich, betrifft aber Gesundheitsdaten nach DSGVO |

Nichts in diesem Gespräch fällt eindeutig in die Kategorie „Merken“. Das ist keine Besonderheit dieses Beispiels – in regulierten Kontexten ist das eher die Regel als die Ausnahme. Die meisten Informationen, die Kunden teilen, gehören entweder an eine zentralere und zuverlässigere Stelle als das Gesprächs-Memory des Agenten, sind zu sensibel für eine Speicherung oder erfordern zuvor die ausdrückliche Einwilligung des Kunden.
Die zugrunde liegende Entscheidungslogik lautet:
- Wenn es ein System gibt, das für diese Art von Daten gebaut ist (ein Banking-Dienst, ein CRM, ein Verifizierungsdienst) — dann gehört es dorthin, nicht ins Memory.
- Wenn es vorübergehend oder an einen einzelnen Moment gebunden ist — nach dem aktuellen Turn verwerfen.
- Wenn es für zukünftige Interaktionen wirklich nützlich und nicht sensibel ist — merken.
- Wenn es nützlich, aber persönlich ist, insbesondere besondere Kategorien personenbezogener Daten nach DSGVO — zuerst Einwilligung einholen.

## Verständnis prüfen
### Frage 1
>  Ein Contigo-Agent wird angewiesen, sich alles Nützliche zu merken, was ein Kunde erwähnt. Was ist mit der Zeit die wahrscheinlichste Folge?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/dd55eb9f-aa07-409f-b398-123488a4f88f

### Frage 2
>  Ein Kunde teilt dem Contigo-Agenten mit, dass sich sein rechtlicher Name geändert hat. Wo sollte diese Information erfasst werden und warum?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cb390527-fcbf-41a1-b36c-f8b9b7f06a35

> 💡 Takeaway: 
  Zu entscheiden, welche Informationen ein Agent speichern soll, ist eine bewusste Designentscheidung und keine Standardeinstellung. Das Memory eines Agenten speichert grundsätzlich alles, was durch ein Gespräch fließt, sofern keine Regeln festlegen, was gespeichert werden darf und was nicht. Es kann nicht selbst beurteilen, welche Informationen sensibel, relevant oder nützlich sind. Diese Entscheidung triffst du.
  Beachte, dass in diesem Szenario kaum eine Information eindeutig in die Kategorie „Merken“ gefallen ist. Das ist nicht ungewöhnlich. In regulierten Kontexten werden die meisten Informationen entweder an spezialisierte Systeme weitergeleitet, nicht dauerhaft gespeichert oder nur mit ausdrücklicher Einwilligung des Kunden gespeichert.
  Die Standardeinstellung sollte daher nicht sein, möglichst viel zu speichern, sondern bewusst zu entscheiden, welche Informationen tatsächlich im Memory des Agenten landen sollten.