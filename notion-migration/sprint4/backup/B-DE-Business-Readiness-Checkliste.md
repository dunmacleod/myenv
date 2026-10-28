# Business-Readiness-Checkliste

Notion page: https://app.notion.com/p/Business-Readiness-Checkliste-3829418319f3802fb41acad446f3f576
Backed up before n8n migration

> 💡 Das schließt du am Ende dieser Lektion ab: Du weist nach, dass du einen Prototyp-Agenten gegen Produktionsanforderungen prüfen, architektonische Fehler erkennen und gezielte Fixes vorschlagen kannst. Damit wendest du das gesamte Kurs-Framework auf einen Agenten an, den du nicht selbst gebaut hast.

## Darum geht es in diesem Assessment
Meridians Agent ist überarbeitet, abgesichert, End-to-End getestet, und die Plattform-Entscheidung ist dokumentiert. Das Team bereitet sich auf das finale Stakeholder-Review vor.
Vor diesem Review muss noch eine weitere Fähigkeit unter Beweis gestellt werden. Im Consulting-Alltag wird Meridians Team regelmäßig gebeten, KI-Systeme zu bewerten, die sie nicht selbst entworfen haben. Einen Agenten zu auditieren, den man nicht selbst gebaut hat, also seine Architektur gegen bekannte Fehlerarten zu lesen und gezielte Fixes vorzuschlagen, ist genauso wichtig wie die Fähigkeit, selbst einen zu bauen.
Dieses Assessment wendet das gesamte Kurs-Framework auf einen anderen Prototyp an: einen E-Commerce-Customer-Success-Agenten, den ein anderes Team unter anderen Rahmenbedingungen gebaut hat.
## Der Agenten-Prototyp
Sieh dir das folgende Architektur-Dokument für einen neu prototypisierten E-Commerce-Customer-Success-Agenten an. Er soll auf der zentralen kundenseitigen Website eines Unternehmens laufen, das Kunden in Deutschland und den Niederlanden bedient.
### Agenten-Profil: E-Commerce-Customer-Success-Agent
[TABLE]
  | Komponente | Aktuelle Konfiguration |
  | Zweck | Kundenanliegen zu Bestellungen, Retouren und Produktempfehlungen lösen |
  | Memory-Strategie | Gibt bei jedem Turn den kompletten, ungefilterten Gesprächsverlauf in den Prompt des Sprachmodells |
  | Retrieval-Strategie | Standard-semantische Suche gegen Produktkatalog und Retouren-Richtlinien-PDFs, ohne Metadaten-Filterung, ohne Prüfung des Quelldatums, ohne Logik zur Konfliktauflösung |
  | Tool-Konfiguration | Zwanzig API-Tools, darunter check_inventory, issue_refund, send_email, update_shipping_address, apply_discount, cancel_order, alle gleichzeitig in der Tools-Konfiguration des Agent Node geladen, bei jeder Anfrage |
  | Sicherheitskonfiguration | System-Prompt enthält: „Teile niemals personenbezogene Kundendaten mit anderen Kunden." Keine Input-Validierung, kein Output-Filter, keine Least-Privilege-Konfiguration bei den Tool-Credentials |
  | Testprotokoll | Entwicklungsteam hat zwanzig Anfragen über zwei Stunden manuell getestet, bevor der Agent für produktionsreif erklärt wurde |
### Aufgabe 1: Das Business-Readiness-Audit schreiben
Verfasse einen strukturierten Audit-Bericht von rund 250 bis 300 Wörtern, der alle fünf Dimensionen unten abdeckt. Zu jeder Dimension gehört ein konkreter architektonischer Fix.
- Memory-Einschränkungen: Erkläre, warum der komplette ungefilterte Gesprächsverlauf bei jedem Turn im großen Maßstab zu Leistungseinbußen führt. Nenne, welche Memory-Management-Strategie das ersetzen sollte und welche Konfigurationsänderung in den Memory-Einstellungen des Agent Node diese Strategie umsetzt.
- Retrieval-Einschränkungen: Erkläre, warum einfache semantische Suche ohne Metadaten-Filterung oder Konfliktauflösung nicht ausreicht für einen Agenten, der Kunden in zwei EU-Rechtsräumen mit potenziell widersprüchlichen Richtlinienversionen bedient. Nenne, welche Retrieval-Erweiterung (Prüfung des Quelldatums, Metadaten-Filterung oder eine Anweisung zur Konfliktauflösung) die kritischste Lücke schließt.
- Tool-Einschränkungen: Identifiziere, welche konkrete Fehlerart entsteht, wenn zwanzig Tools gleichzeitig in der Tools-Konfiguration des Agent Node geladen sind. Benenne genau, welche Verschlechterung im Reasoning auftritt, wenn das Modell aus einer großen Registry mit überlappenden Tool-Beschreibungen auswählen muss. Nenne, wie die Tool-Registry umstrukturiert werden sollte.
- Sicherheits-Einschränkungen: Erkläre, warum eine einzelne System-Prompt-Anweisung als einzige Datenschutzkontrolle nicht ausreicht für einen kundenseitigen Agenten, der unter der DSGVO personenbezogene Kundendaten verarbeitet. Nenne zwei architektonische Kontrollen, eine auf der Input-Ebene und eine auf der Output-Ebene, die ergänzt werden müssen, damit die Sicherheitsarchitektur produktionstauglich wird.
- Test-Einschränkungen: Erkläre, warum zwanzig von Entwicklern geschriebene Anfragen über zwei Stunden keine ausreichende Validierung sind für einen Agenten, der täglich Tausende Kundeninteraktionen bewältigen soll. Nenne, welcher Mechanismus zur kontinuierlichen Evaluation implementiert werden muss, etwa was er testet und wie oft er läuft.
### Aufgabe 2: Wissens-Quiz
### Frage 1
>  Ein E-Commerce-Agent gibt bei jedem Turn den kompletten ungefilterten Gesprächsverlauf in den Prompt des Sprachmodells. Nach fünfzehn Austauschen sinkt die Antwortqualität deutlich, und der Agent fängt an, seine System-Prompt-Anweisungen zu ignorieren. Was ist die zutreffendste Erklärung?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/3399902e-02c5-43a4-87e8-cf752383465c

### Frage 2
>  Ein Agent mit zwanzig API-Tools ruft bei einfachen Anfragen oft das falsche Tool auf, zum Beispiel löst er send_email aus, obwohl der Nutzer nur seinen Bestellstatus prüfen wollte. Welche architektonische Änderung löst dieses Routing-Problem am direktesten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8529c2fa-c306-4c9b-88d0-9186e246a3a6

### Frage 3
>  Ein Kundensupport-Agent für Nutzer in Deutschland und den Niederlanden ruft zwei widersprüchliche Chunks zur Retouren-Richtlinie ab. Einer nennt ein 14-Tage-Rückgabefenster aus einem Dokument von 2023, der andere ein 30-Tage-Fenster aus einem Update von 2025. Der Agent addiert beide Werte und sagt dem Kunden, er habe 44 Tage Zeit für die Rückgabe. Welche zwei Änderungen würden diesen Fehler am direktesten verhindern?
[EMBED] https://app.masterschool.com/campus/multi-choice-question/b2a38d37-2be3-4b4a-a32e-6a078e7496ec

### Frage 4
>  Ein Entwicklungsteam erklärt seinen Agenten nach zwei Stunden manuellem Testen mit zwanzig selbst geschriebenen Anfragen für produktionsreif. Der Agent wird in Produktion gebracht und scheitert innerhalb von 48 Stunden an Kundenanfragen, die das Team nie getestet hat. Welche Testlücke erklärt dieses Ergebnis am direktesten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/8de67070-5436-4f75-9a1e-dc9156ba7a1e


> 💡 Fazit:
  Die Audit-Fähigkeit, die du hier entwickelt hast, also die Architektur eines Agenten gegen bekannte Fehlerarten zu lesen und gezielte Fixes vorzuschlagen, lässt sich direkt auf Meridians Consulting-Arbeit übertragen, wenn KI-Systeme bewertet werden, die Kunden selbst gebaut haben. Ein Team, das einen Agenten auditieren kann, den es nicht selbst gebaut hat, ist deutlich wertvoller als eines, das nur Agenten bauen kann, die es selbst entworfen hat. Jede Fehlerart in diesem Prototyp ist in irgendeiner Form auch beim Meridian-Build aufgetaucht. Sie in einer unbekannten Architektur zu erkennen, ist der Beleg dafür, dass das Kurs-Framework wirklich verinnerlicht wurde.