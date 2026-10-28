# Router- und Evaluator-Muster

Notion page: https://app.notion.com/p/Router-und-Evaluator-Muster-b779418319f382a9993801530c859c9d
Backed up before n8n migration

Am Ende der vorherigen Lektion machte Petra eine Beobachtung, die Selin im Kopf blieb: Das Confidence-Signal, das sie dem Koordinator hinzugefügt hatten, tat etwas anderes als die Routing-Entscheidung. Die Routing-Entscheidung sagte, wohin die Anfrage gesendet werden soll. Das Confidence-Signal sagte, wie sehr man der Routing-Entscheidung vertrauen sollte, bevor man danach handelt. Das sind zwei unterschiedliche Aufgaben, und in der Multi-Agent-Designliteratur haben sie zwei unterschiedliche Namen: Router und Evaluator.
Der Vela-Koordinator erledigt bereits beide Aufgaben in einem Node. Das ist für das aktuelle System in Ordnung. Der Flow ist klein, die Risiken sind moderat, und ein Node, der routet und sich selbst evaluiert, verursacht keine Probleme. Aber zu verstehen, warum diese Aufgaben verschieden sind und was passiert, wenn sie von separaten Nodes übernommen werden, macht den Unterschied zwischen einem Multi-Agent-System, das in der Produktion standhält, und einem, das ständiges Nachjustieren der Anweisungen braucht.
> 💡 Ein Router entscheidet, wohin Arbeit geht. Ein Evaluator entscheidet, ob die Arbeit gut genug ist, bevor sie weitergeht. Von außen sehen sie ähnlich aus (beide sitzen zwischen Agenten), aber sie beantworten unterschiedliche Fragen.

## Das Router-Muster
Ein Router ist ein Node (typischerweise ein Koordinator-Agent oder ein Condition-Node), dessen einzige Aufgabe darin besteht, eine Eingabe zu klassifizieren und sie an den richtigen Handler weiterzuleiten. Der Router beantwortet die Anfrage des Nutzers nicht. Er bewertet keine Qualität. Er liest die Eingabe, wendet eine Entscheidungsregel an und gibt die Eingabe an den passenden nachgelagerten Node weiter.
Der Vela-Koordinator ist ein Router. Er liest eine Kundenanfrage, klassifiziert sie als commercial, technical oder hybrid und leitet sie weiter. Er hat keine Meinung dazu, ob die Anfrage gut formuliert ist, ob der Spezialist sie beantworten kann oder ob die Antwort, die der Spezialist gibt, gut ist. Routing und Antworten sind strikt getrennt.
#### Was ein Router braucht, um gut zu funktionieren
Ein Router ist nur so gut wie seine Klassifizierungslogik. Drei Dinge bestimmen, ob ein Router zuverlässig ist:
Klar abgegrenzte, sich gegenseitig ausschließende Kategorien. Überschneiden sich Kategorien (könnte eine Anfrage plausibel zu mehr als einer gehören), routet der Router inkonsistent, und diese Inkonsistenz ist schwer zu erkennen, weil kein Fehler ausgelöst wird. Die Spezialisierungsdesign-Arbeit von früher in diesem Sprint war im Wesentlichen Vorbereitung für einen zuverlässigen Router: enge, nicht überlappende Verantwortungsbeschreibungen erzeugen Routing-Kategorien, die ein Modell konsistent anwenden kann.
Ein definierter Standardfall für den mehrdeutigen Fall. Jeder Router bekommt irgendwann eine Anfrage, die in keine seiner benannten Kategorien passt. Die hybrid-Kategorie des Vela-Koordinators ist teils eine echte dritte Kategorie und teils ein Standardfall für Anfragen, die nicht eindeutig zu einem der beiden Spezialisten gehören. Diesen Standardfall zu benennen, und zu entscheiden, was damit passiert, ist Teil des Router-Designs.
Keine Side Effects. Ein Router, der die Anfrage verändert, Kontext hinzufügt oder Annahmen darüber trifft, was der nachgelagerte Agent braucht, ist nicht mehr nur ein Router. Er hat begonnen, die Aufgabe des Evaluators oder des Spezialisten zu übernehmen. Der Custom-Function-Node des Vela-Koordinators existiert teilweise aus diesem Grund: Das Formen des Kontexts (das Hinzufügen von context_note, das Entfernen von Routing-Metadaten) wurde aus dem Koordinator in einen dedizierten Node verschoben, damit der Koordinator sauber bleibt.
#### Wann ein Router das richtige Muster ist
- Der Eingaberaum lässt sich in klar unterschiedliche Kategorien aufteilen
- Unterschiedliche Kategorien erfordern tatsächlich unterschiedliche Bearbeitung (unterschiedliche Spezialisten, unterschiedliche Tools, unterschiedliche Antwortposition)
- Die Routing-Entscheidung selbst hat ein niedriges Risiko: Ein Fehlrouting sendet die Anfrage an den falschen Spezialisten, aber das Grenzverhalten des Spezialisten fängt sie ab, und die Anfrage kann neu geroutet werden
#### Wann ein Router allein nicht ausreicht
- Die Kategorien sind unscharf, und die Klassifizierungskonfidenz variiert je nach Eingabe deutlich
- Ein Fehlrouting hat hohe Kosten: Der Spezialist erzeugt eine selbstbewusste, autoritativ klingende, aber falsche Antwort, nach der der Kunde handelt
- Der Eingaberaum enthält Anfragen, die keine definierte Kategorie abdeckt, und der Standardpfad erzeugt schlechte Ergebnisse
In diesen Fällen braucht der Router einen Begleiter: einen Evaluator.
![image]((notion-hosted file))

## Das Evaluator-Muster
Ein Evaluator ist ein Node, dessen Aufgabe darin besteht, die Qualität der Ausgabe eines anderen Nodes zu bewerten, bevor entschieden wird, was damit geschieht. Er beantwortet die Anfrage des Nutzers nicht. Er routet nicht die Eingabe. Er liest eine Ausgabe, die bereits erzeugt wurde, und trifft ein Urteil: Ist sie gut genug, um weitergegeben zu werden, oder muss sie überarbeitet, neu geroutet oder markiert werden?
Das Confidence-Signal, das dem Vela-Koordinator in der vorherigen Lektion hinzugefügt wurde, ist ein primitiver Evaluator, weil der Koordinator seine eigene Klassifizierungskonfidenz bewertet, bevor er sich auf eine Routing-Entscheidung festlegt. Ein richtiger Evaluator ist jedoch ein separater Node, nachgelagert vom Agenten, den er evaluiert, mit eigenen Anweisungen und eigener Entscheidungslogik.
> ➡️ Ein Beispiel: Nachdem der Vela Commercial-Agent eine Antwort erzeugt hat, liest ein Evaluator-Node die Antwort und prüft zwei Dinge: Bleibt sie innerhalb der definierten Verantwortung des Commercial-Agent (Preise, Verträge, Billing, Verlängerung), und enthält sie irgendetwas, das nicht in einer kundenorientierten Antwort erscheinen sollte (interne Account-Flags, Systemfehlercodes, Routing-Metadaten)? Bestehen beide Prüfungen, sendet der Evaluator die Antwort an den End-Node. Schlägt eine der Prüfungen fehl, kann der Evaluator zum Hybrid Handler neu routen, eine überarbeitete Antwort anfordern oder eine Graceful-Degradation-Antwort auslösen.

#### Was ein Evaluator braucht, um gut zu funktionieren
- Ein spezifisches, testbares Kriterium. Ein Evaluator, der prüft „ist das eine gute Antwort?", wird scheitern, denn „gut" ist nicht testbar. Ein Evaluator, der prüft „enthält diese Antwort eines der folgenden Muster: [Liste], ja oder nein", lässt sich dagegen testen und liefert konsistentere Ergebnisse.
- Eine klare Aktion für jedes Urteil. Die Aufgabe des Evaluators ist nicht abgeschlossen, wenn er ein Urteil erzeugt. Er muss mit diesem Urteil etwas tun: die Ausgabe weitergeben, sie zur Überarbeitung zurücksenden, zu einem Fallback routen oder für Human Review markieren. Ein Evaluator ohne definierte Aktion für den Fehlerfall ist keine Fallback-Strategie, sondern eine Qualitätsprüfung ohne Konsequenz.
- Sein eigener Fehlermodus ist mitgedacht. Ein Evaluator ist ein LLM-Node, kann also falsche Urteile fällen, in einen Timeout laufen oder eine fehlerhafte Ausgabe zurückgeben. Ein Multi-Agent-System mit einem Evaluator, der selbst unbemerkt scheitert, ist komplexer und nicht zuverlässiger als eines ganz ohne Evaluator. Der Evaluator braucht deshalb einen eigenen Fallback, typischerweise einen konservativen: Kann der Evaluator kein Urteil erzeugen, behandelst du die Ausgabe als fehlgeschlagen und routest zum Fallback-Pfad.
#### Wann ein Evaluator das richtige Muster ist
- Die Qualität der Ausgabe eines Spezialisten ist variabel und unvorhersehbar
- Eine falsche Ausgabe, die den Kunden erreicht, hat hohe Kosten (Reputation, Vertrauen, Compliance)
- Die Prüfungen, die Qualität definieren, sind spezifisch genug, um in einem Evaluator-Prompt kodiert zu werden
- Die zusätzlichen Kosten und die zusätzliche Latenz eines LLM-Aufrufs sind angesichts der Risiken akzeptabel
#### Wann ein Evaluator Komplexität ohne Nutzen hinzufügt
- Die Ausgabequalität des Spezialisten ist bereits hoch und konsistent
- Die Qualitätskriterien sind zu vage, um zuverlässig kodiert zu werden
- Der Evaluator führt mehr Fehlermodi ein, als er verhindert
- Die zusätzliche Latenz ist für den Use Case nicht akzeptabel
[TABLE]
  |  | Router | Evaluator |
  | Frage, die er beantwortet | Wohin soll diese Eingabe gehen? | Ist diese Ausgabe gut genug, um weitergegeben zu werden? |
  | Liest | Die Eingabe (die Anfrage des Nutzers) | Die Ausgabe (die Antwort eines Spezialisten) |
  | Position im Flow | Vor dem Spezialisten | Nach dem Spezialisten |
  | Fehlermodus | Fehlrouting; Eingabe geht an den falschen Handler | False Pass; schlechte Ausgabe freigegeben; False Fail; gute Ausgabe abgelehnt |
  | Kosten | Ein zusätzlicher LLM-Aufruf am Anfang | Ein zusätzlicher LLM-Aufruf am Ende |
  | Wann hinzufügen | Kategorien sind klar unterscheidbar; Routing-Fehler ist behebbar | Ausgabequalität ist variabel; Qualitätsfehler ist kostspielig |
![image]((notion-hosted file))

## Router und Evaluator zusammen
Die zwei Muster schließen sich nicht gegenseitig aus. Ein ausgereiftes Multi-Agent-System hat oft beides: einen Router am Anfang, der Eingaben an den richtigen Spezialisten weiterleitet, und einen Evaluator am Ende, der die Ausgabe des Spezialisten prüft, bevor sie den Kunden erreicht.
Das Vela-System, wie es in der vorherigen Lektion gebaut wurde, hat einen Router (den Koordinator und den Condition-Node), aber keinen Evaluator. Das ist der richtige Ausgangspunkt: Einen Evaluator hinzuzufügen, bevor der Router zuverlässig funktioniert, führt Komplexität ein, ohne die Daten zu haben, um ihn zu kalibrieren. Der typische Fortschritt sieht so aus:
1. Bau den Router. Test ihn mit einer repräsentativen Stichprobe von Eingaben. Miss die Fehlrouting-Rate.
1. Ist die Fehlrouting-Rate akzeptabel, liefer ohne Evaluator aus: Das Grenzverhalten in jedem Spezialisten fängt Grenzfälle bereits ab.
1. Ist die Ausgabequalität nach korrektem Routing variabel, füg nachgelagert bei dem Spezialisten mit der höchsten Qualitätsvarianz einen Evaluator hinzu.
1. Ist die Routing-Konfidenz für einen Anfragetyp dauerhaft niedrig, füg vorgelagert (vor dem Spezialisten) einen Confidence-Evaluator hinzu. Das entspricht genau dem Confidence-Signal, das in der vorherigen Lektion bereits näherungsweise eingeführt wurde.
#### Das kombinierte Muster in der Praxis
Entscheidet sich das Vela-Team, einen Evaluator hinzuzufügen, wäre die wertvollste Platzierung nach dem Commercial-Agent, nicht nach dem Technical-Agent und nicht nach dem Hybrid Handler. Der Grund: Die Domäne des Commercial-Agent (Preise, Verträge, Billing) enthält Informationen, die echten geschäftlichen Schaden anrichten können, wenn sie dem Kunden falsch mitgeteilt werden. Eine falsche technische Antwort über API-Verhalten ist behebbar, der Kunde kann sie testen und feststellen, dass sie falsch war. Eine falsche Preisangabe oder ein falsch zitierter Vertragsbegriff dagegen könnte der Kunde bereits umgesetzt haben, bevor er korrigiert wird. Weil die Konsequenz eines Qualitätsfehlers hier hoch ist, verdient der Evaluator seine Kosten.
## Zwischen den Mustern wählen
Der häufigste Fehler im Multi-Agent-Design besteht darin, beide Muster reflexartig hinzuzufügen und Router sowie Evaluator als Standardarchitektur zu behandeln, die angeblich jedes Multi-Agent-System braucht. Das stimmt nicht. Beide fügen einen LLM-Aufruf, Latenz und eine neue Fehleroberfläche hinzu. Die Frage ist immer, ob der Nutzen für Zuverlässigkeit oder Qualität diese Kosten im konkreten System rechtfertigt.
Nutz das als grobe Entscheidungshilfe:
- Füg einen Router hinzu, wenn der Eingaberaum klar unterschiedliche Kategorien hat, die unterschiedliche Bearbeitung erfordern, und ein einzelner Agent, der alle bearbeitet, überlastet wäre.
- Füg einen Evaluator hinzu, wenn die Ausgabequalität nach dem Routing variabel ist und die Kosten eines Qualitätsfehlers, der den Kunden erreicht, hoch genug sind, um einen zusätzlichen LLM-Aufruf und zusätzliche Latenz zu rechtfertigen.
- Füg beides hinzu, wenn der Eingaberaum vielfältig ist, Routing-Fehler häufig sind und die Ausgabequalität korrekt gerouteter Spezialisten weiterhin variabel ist. Das ist die komplexeste Konfiguration und sollte erst gebaut werden, nachdem einfachere Konfigurationen getestet und als unzureichend befunden wurden.
- Füg keines von beidem hinzu, wenn ein einzelner, gut spezifizierter Agent den gesamten Eingaberaum mit akzeptabler Qualität bearbeitet. Routing und Evaluation zu einem System hinzuzufügen, das sie nicht braucht, erzeugt Komplexität ohne Nutzen. Genau der Fehler, den das Vela-Team vermieden hat, indem es die Multi-Agent-Komplexität vor dem Bau bewertet hat.
## Zusammenfassung
Zwei Muster, zwei Fragen, zwei Positionen im Flow. Ein Router sitzt vor der Arbeit und beantwortet: Wohin gehört diese Eingabe? Ein Evaluator sitzt nach der Arbeit und beantwortet: Ist diese Ausgabe gut genug, um ausgeliefert zu werden? Beide fügen LLM-Aufrufe und Latenz hinzu, und keines der beiden sollte ohne einen konkreten, testbaren Grund eingebaut werden.
Das Vela-System hat einen Router. Das Team hat jetzt den Wortschatz und das Entscheidungsframework, um zu entscheiden, ob es einen Evaluator braucht und wo dieser platziert werden sollte, falls ja. Diese Entscheidung gehört zum Sprint-2-Assessment: die vollständige Multi-Agent-Architektur für den Projektagenten entwerfen, mit Agentenrollen, Verantwortlichkeiten, Koordinationsansatz und den Mustern, die das System zusammenhalten, wenn Eingaben mehrdeutig sind oder Ausgaben nicht ausreichen.
## Quiz
### Frage 1
>  Das Vela-Team fügt nach dem Technical-Agent einen neuen Node hinzu, der die Antwort des Technical-Agent liest und prüft, ob sie interne Systemfehlercodes enthält, die nicht in einer kundenorientierten Nachricht erscheinen sollten. Findet er einen, entfernt er den Fehlercode und ersetzt ihn durch eine Erklärung in einfacher Sprache, bevor er die Antwort an den End-Node weitergibt. Welches Muster implementiert dieser Node?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a781120c-8e2a-4438-b2b6-655f51d0dd7a
### Frage 2
>  Nach zwei Wochen in Produktion prüft das Vela-Team seine Daten. Der Koordinator routet etwa 4 % der Anfragen falsch, hauptsächlich Grenzfälle, die Preise und technische Symptome in derselben Nachricht erwähnen. Der Commercial-Agent und der Technical-Agent bearbeiten ihre korrekt gerouteten Anfragen beide gut, mit hohen Kundenzufriedenheitswerten. Welche Ergänzung des Systems ist durch diese Daten am stärksten gerechtfertigt?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/3af841ff-098f-460e-8b4b-0ef652c729c0