# Tool-Fehler und Endlosschleifen behandeln

Notion page: https://app.notion.com/p/Tool-Fehler-und-Endlosschleifen-behandeln-3779418319f380099057cc7c61cfc543
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Deterministische Schutzmechanismen entwerfen, die verhindern, dass ein Contigo-Agent bei einem Tool-Fehler in eine unendliche Ausführungsschleife gerät, und ein Ausweichprotokoll schreiben, das kontrolliert degradiert, ohne eine Antwort zu erfinden.
> ➡️ Das in dieser Lektion beschriebene Tool-Fehler-Szenario beschreibt Verhalten, das du in der nächsten Lektion konfigurierst, sobald Tools mit deinem Chatflow verbunden sind. Die Design-Entscheidungen, die du hier triffst (der Wert für Max Iterations und die Ausweichanweisung), werden in der nächsten Lektion direkt im Tool-Agent-Node umgesetzt. Erledige die Aufgaben jetzt, damit deine Schutzmechanismen bereitstehen, bevor die Tools live gehen.

## Die Ausgangslage
Contigo GmbHs Kreditstatus-Tool läuft seit zwei Wochen ohne Zwischenfälle im internen Test. Dann, während eines geplanten Wartungsfensters, fällt die Kernbanken-API aus. Das Tool beginnt, bei jedem Aufruf einen generischen 503-Fehler zurückzugeben. Der Agent erhält den Fehler, schlussfolgert, dass er die Anfrage des Kunden noch nicht erfüllt hat, und ruft das Tool erneut auf. Das Tool gibt wieder einen 503-Fehler zurück. Der Agent versucht es erneut. Und erneut. Innerhalb von vier Minuten hat der Agent dreiundsechzig aufeinanderfolgende Tool-Aufrufe gegen eine ausgefallene API getätigt, einen erheblichen Teil des Token-Budgets des Sprints verbraucht und dem Kunden keinerlei Antwort geliefert.
Das Problem: Der Agent hat keine Anweisung dafür, was zu tun ist, wenn diese Tools fehlschlagen. Sein System-Prompt sagt ihm, er solle den Kreditstatus abrufen, bevor er antwortet. Das Tool schlägt immer wieder fehl. Der Agent versucht es immer wieder. Nichts in der Architektur sagt ihm, dass er aufhören soll.
Dieses Fehlerverhalten gehört zu den betrieblich gefährlichsten Risiken beim produktiven Einsatz von Agenten. Es lässt sich jedoch vollständig durch zwei gezielte Maßnahmen verhindern: eine deterministische Iterationsgrenze und ein ausdrückliches Ausweichprotokoll.
## Warum Anweisungen im Sprachmodell allein nicht ausreichen
Die naheliegende Reaktion auf diesen Fehler ist, eine System-Prompt-Anweisung hinzuzufügen: „Schlägt das Tool fehl, höre auf, es erneut zu versuchen, und entschuldige dich beim Kunden." Das ist notwendig, aber nicht ausreichend.
Sprachmodelle sind probabilistisch. Eine Anweisung, nach einem Fehler aufzuhören, verringert die Häufigkeit solcher Schleifen. Unter bestimmten Bedingungen, bei bestimmten Formulierungen der Anfrage oder nach einer bestimmten Abfolge von Tool-Ausgaben kann das Modell jedoch an der Anweisung vorbei argumentieren und das Tool trotzdem erneut aufrufen. Probabilistische Einhaltung ist kein akzeptabler Sicherheitsstandard für ein Produktivsystem, das kundennahe Finanz-Workflows abwickelt.
Die einzige verlässliche Methode, die Ausführung zu begrenzen, liegt auf Infrastrukturebene, also eine harte, deterministische Grenze, die vom Framework selbst durchgesetzt wird, unabhängig vom Schlussfolgern des Modells. In Flowise ist das der Parameter Max Iterations am Agenten-Node. Wird diese Grenze erreicht, beendet das Framework den Ausführungszyklus, unabhängig davon, was das Modell als Nächstes tun würde. Es ist ein Sicherungsmechanismus, den das Modell nicht außer Kraft setzen kann.
> ➡️ Wo das in deinem Chatflow konfiguriert wird: In Flowise befindet sich der Parameter Max Iterations in den zusätzlichen Parametern des Tool-Agent-Nodes. Es ist ein einzelnes Ganzzahlfeld. Ihn zu setzen, bevor du Tools anschließt, ist die richtige Reihenfolge, der Schutzmechanismus sollte stehen, bevor der erste Live-Tool-Aufruf erfolgt.
Der Ausweichmechanismus im System-Prompt bleibt trotzdem erforderlich. Er bestimmt, was der Agent dem Kunden sagt, nachdem der Sicherungsmechanismus ausgelöst hat. Aber die Anweisung allein, ohne die Beschränkung auf Infrastrukturebene, ist keine sichere Architektur.
![image]((notion-hosted file))

## Deine Aufgaben
### Aufgabe A: Den Sicherungsmechanismus konfigurieren
Der Tool-Agent-Node, den du hinzufügst, verfügt über einen Parameter Max Iterations in seinen zusätzlichen Parametern. Bevor du dorthin gelangst, entscheide, welchen Wert du setzen wirst, und dokumentiere deine Begründung. Bedenke Folgendes: Dieser Parameter begrenzt die Gesamtzahl der Denk- und Tool-Aufruf-Zyklen, die der Agent ausführen kann, bevor das Framework die Schleife beendet.
Lege einen Wert fest und schreibe zwei bis drei Sätze zur Begründung deiner Wahl. Bedenke dabei:
- Die typische Anzahl an Tool-Aufrufen, die eine legitime mehrstufige Contigo-Anfrage benötigt. Eine Anfrage, die einen Kreditstatus prüft und anschließend eine Folgeabfrage zu Dokumenten auslöst, könnte beispielsweise zwei bis drei Zyklen benötigen
- Den Punkt, an dem wiederholte Aufrufe desselben fehlschlagenden Tools eher auf eine Schleife als auf legitimes mehrstufiges Schlussfolgern hindeuten
- Die Kosten eines zu hoch oder zu niedrig gesetzten Grenzwerts. Ein zu großzügiger Grenzwert erlaubt einen erheblichen Ressourcenverlust, bevor er beendet wird; ein zu enger Grenzwert beendet legitime mehrstufige Anfragen vorzeitig
### Aufgabe B: Die Ausweichanweisung für den System-Prompt schreiben
Entwirf eine zwei bis drei Sätze umfassende Ergänzung für den System-Prompt des Contigo-Agenten, die sein Verhalten regelt, wenn die Max-Iterations-Grenze erreicht wird oder wenn ein Tool bei aufeinanderfolgenden Aufrufen wiederholt einen Fehler zurückgibt. Wenn du in der nächsten Lektion den Tool-Agent-Node hinzufügst, kommt diese Anweisung als neuer Absatz nach deiner bestehenden Grounding-Anweisung in das Feld „System Message". Entwirf sie jetzt, damit du sie direkt kopieren kannst.
Deine Anweisung muss folgende drei Anforderungen erfüllen:
Ehrliches Eingeständnis: Der Agent darf keinen Kreditstatus erfinden, keine plausibel klingende Antwort aus seinen Trainingsdaten generieren und nicht suggerieren, das Tool sei erfolgreich gewesen, obwohl es das nicht war. Der Kunde muss verstehen, dass beim System ein Problem aufgetreten ist.
Keine technischen Details: Die Anweisung muss dem Agenten vorgeben, den Fehler in professioneller, kundengerechter Sprache zu kommunizieren. Fehlercodes, API-Fachbegriffe und Hinweise auf die Infrastruktur dürfen in der kundenseitigen Antwort nicht auftauchen.
Klarer nächster Schritt: Der Agent muss dem Kunden eine konkrete Alternative anbieten, etwa den Verweis an seinen zuständigen Kundenbetreuer oder die direkte Support-Hotline von Contigo.
#### Aufgabe C: Die Schwelle für menschliche Beteiligung bewerten
Nicht jeder Tool-Fehler rechtfertigt einen automatisierten Ausweichmechanismus. Bei Vorgängen mit hohem Risiko ist die angemessene Reaktion auf einen Fehler möglicherweise kein automatisierter Ausweichmechanismus, sondern eine verpflichtende Pause zur menschlichen Überprüfung.
Beantworte die folgenden zwei Fragen:
- Reicht für Contigos Kreditstatus-Tool ein automatisierter Ausweichmechanismus aus, oder erfordert ein Tool-Fehler menschliches Eingreifen? Begründe deine Antwort.
- Ist bei einem hypothetischen Tool zur Kreditauszahlung, das Geld direkt auf das Konto eines Kunden überweist, derselbe automatisierte Ausweichmechanismus angemessen, oder sollte die Architektur einen verpflichtenden Schritt mit menschlicher Beteiligung erzwingen, bevor ein erneuter Versuch oder eine Alternativhandlung erfolgt?

[toggle] Bedenke Folgendes …
  🔽 Checkpoint 1: Den Wert für Max Iterations festlegen - Eine legitime mehrstufige Anfrage braucht genug Iterationen, um ihre Arbeit abzuschließen. Ein Schleifen-Fehler muss abgefangen werden, bevor er das Token-Budget aufbraucht. Zwischen diesen beiden Zahlen sollte dein Wert für Max Iterations liegen.
  🔽 Checkpoint 2: Das Problem der probabilistischen Einhaltung - Eine System-Prompt-Anweisung verringert die Häufigkeit von Schleifen. Eine Max-Iterations-Grenze stoppt sie, unabhängig davon, wozu das Modell gelangt. Das eine ist probabilistische Einhaltung. Das andere ist ein harter Stopp. Überlege bei einem kundennahen Agenten im Finanzdienstleistungsbereich, welches Risikoprofil akzeptabel ist.
  🔽 Checkpoint 3: Die Schwelle für menschliche Beteiligung festlegen - Nicht jeder Fehler hat dieselbe Konsequenz. Eine fehlgeschlagene Statusabfrage ist für den Kunden unangenehm. Eine fehlgeschlagene Geldüberweisung hat finanzielle und regulatorische Folgen. Das Risiko des Vorgangs bestimmt, ob eine menschliche Überprüfung angemessen ist.
## Verständnis prüfen
>  Ein Contigo-Agent erreicht seine Max-Iterations-Grenze nach fünf aufeinanderfolgenden 503-Fehlern des Kreditstatus-Tools. Der System-Prompt enthält keine Ausweichanweisung. Was ist das wahrscheinlichste Verhalten des Agenten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/2178ed17-5d4f-4303-9c64-0b2cf853050e


> 💡 Fazit:
  Deterministische Schutzmechanismen und probabilistische Anweisungen erfüllen unterschiedliche Zwecke. Die Max-Iterations-Grenze garantiert, dass die Schleife stoppt. Die Ausweichanweisung regelt, was passiert, nachdem sie gestoppt hat.
  Zusammen stellen sie sicher, dass der Kunde eine professionelle, ehrliche Antwort erhält statt einer erfundenen Antwort oder einer rohen Fehlermeldung. Beides ist für einen produktionsreifen Agenten in einem regulierten Finanzdienstleistungsumfeld erforderlich, und beides muss entworfen werden, bevor das erste Tool angeschlossen wird, nicht erst, nachdem ein Fehler zeigt, dass sie fehlen.

## Checkliste für die nächste Lektion
Stelle sicher, dass Folgendes erledigt ist, bevor du zur nächsten Lektion übergehst.
Aus der vorherigen Lektion:
- [ ] Drei überarbeitete System-Prompt-Anweisungen geschrieben und dokumentiert: Abfrageumfang, Grenze bei Kontoaktionen und Ausweichverhalten
- [ ] Sechs Testanfragen vorbereitet (zwei pro Anweisung) mit dem jeweils erwarteten Verhalten des Agenten notiert
- [ ] Verbleibende Überschneidungen zwischen den Anweisungen identifiziert und behoben
Aus dieser Lektion:
- [ ] Wert für Max Iterations festgelegt und schriftlich begründet
- [ ] Ausweich-Anweisung für den System-Prompt entworfen, die ein ehrliches Eingeständnis, keine technischen Details und einen klaren nächsten Schritt für den Kunden abdeckt
- [ ] Schwelle für menschliche Beteiligung beim Kreditstatus-Tool bewertet und deine Schlussfolgerung dokumentiert