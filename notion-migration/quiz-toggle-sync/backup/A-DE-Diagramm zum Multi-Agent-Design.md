# Diagramm zum Multi-Agent-Design

Notion page: https://app.notion.com/p/Diagramm-zum-Multi-Agent-Design-d2e9418319f38253823281911274ff30
Backed up before n8n migration

Trevi Health ist eine Healthcare-Staffing-Agentur mit Sitz in Mailand. Sie vermittelt Pflegekräfte, Physiotherapeuten und spezialisierte Betreuungskräfte an Krankenhäuser, Privatkliniken und Home-Care-Einrichtungen in Norditalien. Ihr Operations-Team arbeitet mit einer Mischung aus E-Mail, Tabellen und einem leicht angepassten CRM. Sie haben keine AI-Agenten in Produktion.
Ihr Operations Director Marco wurde damit beauftragt zu bewerten, ob ein AI-Agent die Zeit reduzieren könnte, die ihre Koordinatoren damit verbringen, Routineanfragen aus zwei Quellen zu beantworten: Bewerber-Arbeitskräfte (die nach Schichtverfügbarkeit, Vergütungssätzen, Dokumentanforderungen und Vermittlungsstatus fragen) und Kundeneinrichtungen (die nach Kandidaten-CVs, Verfügbarkeitsfenstern, Compliance-Dokumentation und Rechnungsstellung fragen). Beide Gruppen kontaktieren Trevi über denselben gemeinsamen Posteingang.
Marco hat ein erstes Briefing erstellt: ein Agent, ein Posteingang, alles bearbeiten. Das Feedback seines Teams nach einem zweiwöchigen Prototyp lautet, dass der Agent bei Bewerberanfragen gut funktioniert und bei Anfragen von Einrichtungen schlecht, und dass er gelegentlich den Ton verwechselt oder Kandidateninformationen mit Einrichtungskontakten teilt.
Wende dein Wissen aus Sprint 2 an, um ein Multi-Agent-Design-Diagramm für die Anfragebearbeitung von Trevi Health zu erstellen. Verfasse dazu eine schriftliche Designbegründung, wie sie auch in einem echten Architekturreview verlangt würde.
## Womit du arbeitest
Das Trevi-Health-Szenario hat die folgenden bestätigten Eigenschaften:
Anfragequellen:
- Bewerber-Arbeitskräfte: Pflegekräfte, Physios und Spezialisten, die nach Schichten, Vergütung, Dokumenten und Vermittlungsstatus fragen. Erwarteter Ton: warm, beruhigend, praktisch.
- Kundeneinrichtungen: Krankenhäuser und Kliniken, die nach Kandidatenqualifikationen, Compliance-Dokumentation, Planung und Rechnungsstellung fragen. Erwarteter Ton: professionell, präzise, effizient.
Bestätigte Fehlermodi im Single-Agent-Prototyp:
- Antwortqualität für Bewerberanfragen: akzeptabel
- Antwortqualität für Anfragen von Einrichtungen: schlecht; der Agent verwendet bewerberorientierte Sprache und verfehlt einrichtungsspezifische Details
- Informationsgrenzfehler: Der Agent erwähnt gelegentlich personenbezogene Kandidatendaten in Antworten, die an Einrichtungen gerichtet sind
- Routing: Alle Anfragen kommen in einem gemeinsamen Posteingang ohne Vorklassifizierung an
Volumen- und Latenzkontext:
- Ungefähr 60 bis 80 Anfragen pro Tag insgesamt, grob aufgeteilt in 60 % Bewerber und 40 % Einrichtungen
- Anfragen kommen über den Arbeitstag verteilt per E-Mail-Integration an; die Erwartung an die Antwortzeit liegt unter 4 Stunden, nicht in Echtzeit
- Das Operations-Team prüft alle Agentenantworten vor dem Senden (Human-in-the-Loop-Freigabe ist bereits vorhanden)
Einschränkung:
- Trevi Health hat kein Entwicklerteam. Das System muss von einer Nicht-Entwicklerin oder einem Nicht-Entwickler in n8n gebaut werden können. Custom Code ist nur in Code-Nodes akzeptabel.
Behalte diese Fragen im Blick, während du arbeitest:
- Weisen die Hinweise auf Überlastung, Unter-Spezifikation oder beides hin? Deine Diagnose bestimmt, ob ein Multi-Agent-Design gerechtfertigt ist.
- Wo liegt der Informationsgrenzfehler in der Fehlertaxonomie? Ist es ein Qualitätsfehler oder ein Systemfehler, und was bedeutet das für das Fallback-Design?
- Stützt der Latenz- und Volumenkontext den Koordinator-Overhead? Nenn deine Annahme explizit.
- Kommst du zu dem Schluss, dass ein besser spezifizierter Single-Agent das Problem lösen würde, musst du trotzdem ein Multi-Agent-Design-Diagramm als abgelehnte Alternative erstellen, mit dokumentiertem Reasoning dafür, warum es abgelehnt wurde.
## Schnelldiagnose
Beantworte diese Fragen, bevor du dein Diagramm erstellst. Sie testen, ob du das Trevi-Health-Szenario korrekt liest, nicht, ob du Sprint-2-Terminologie auswendig gelernt hast.
### Frage 1
>  Marcos erster Single-Agent-Prototyp bearbeitet Bewerberanfragen gut und Anfragen von Einrichtungen innerhalb derselben Session schlecht. Welche Diagnose passt am präzisesten zu dieser Evidenz?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b6801937-3d63-4552-8857-5ccfcf24abf8
### Frage 2
>  Der Informationsgrenzfehler (personenbezogene Kandidatendaten erscheinen in Antworten an Einrichtungen) lässt sich am besten als welcher Fehlertyp klassifizieren?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/77aa935c-5178-4e9f-b1da-be060680d533
### Frage 3
>  Trevi Healths Human-in-the-Loop-Freigabeschritt (alle Agentenantworten werden vor dem Senden geprüft) lässt sich am besten als welcher Fallback-Strategietyp aus der Lektion zur Fehlerbehandlung beschreiben?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/d62da83d-aa21-4d1e-81dd-cabeab25aa3b
### Frage 4
>  Marco möchte dem System eine dritte Anfragekategorie hinzufügen: interne HR-Anfragen von Trevis eigenem Koordinationsteam (Fragen zu Payroll, Schichtplanung und Compliance-Richtlinien). Er schlägt vor, einen dritten Spezialagenten hinzuzufügen. Welche Prüfung ist vor dem Bau am wichtigsten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/a4c07c6e-3e87-47fe-a0c5-6cb4ee4f5b16
### Frage 5
>  Trevi Healths 4-Stunden-Antwortzeitfenster und der Human-Review-Schritt vor dem Senden machen den Multi-Agent-Koordinator-Overhead im Vergleich zu einem Echtzeit-Chat-System mehr oder weniger akzeptabel. Warum?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/52a14838-73c5-4fef-98bd-4cf68078e7c9
## Verbesserungen vornehmen
> 🔥 Bevor du startest, erstell dir eine Kopie von dieser Vorlage. Sie enthält deine schriftliche Designbegründung (Aufgabe B) und die abgelehnte Alternative (Aufgabe C). Aufgabe A (das Diagramm selbst) zeichnest du separat im Tool deiner Wahl.

Du hast das Trevi-Health-Szenario diagnostiziert und bestätigt, dass das Multi-Agent-Design gerechtfertigt ist. Jetzt erstellst du die Abgabe.
### Aufgabe A: Multi-Agent-Design-Diagramm
Erstell ein Diagramm des vorgeschlagenen Trevi-Health-Multi-Agent-Systems.
Dein Diagramm muss zeigen:
- Jeden Agenten oder Node im System und seinen Namen
- Die Eingabequelle (der gemeinsame Posteingang) und das Ausgabeziel (die Review-Queue des Operations-Teams)
- Die Richtung des Informationsflusses zwischen Nodes, dargestellt mit Pfeilen
- Den Routing-Entscheidungspunkt und worauf er routet
- Die Informationsgrenze zwischen Bewerber-Spezialist und Einrichtungs-Spezialist, explizit im Diagramm markiert
- Mindestens einen Fallback-Pfad
Format: Du kannst dieses Diagramm in jedem Tool erstellen, egal ob n8n-Canvas, Zeichentool, Dokumentdiagramm oder handgezeichnet und fotografiert. Wichtig ist, dass alle erforderlichen Elemente vorhanden und lesbar sind. Beschrifte jeden Node und jede Verbindung.
### Aufgabe B: Schriftliche Designbegründung
Schreib neben dem Diagramm eine kurze Designbegründung (maximal 400 Wörter), die die folgenden vier Punkte abdeckt. Das ist das Dokument, das Marco zu einem Design Review mitbringen würde.
B1: Diagnose und Begründung. Sag in zwei bis drei Sätzen, warum die Fehler des Single-Agent-Prototyps ein Multi-Agent-Design rechtfertigen statt einer besseren Single-Agent-Spezifikation. Beziehe dich auf die konkreten Fehlermodi, die du im Abschnitt Schnelldiagnose identifiziert hast.
B2: Agentenrollen und Verantwortlichkeiten. Formulier die Verantwortung jedes Spezialagenten in jeweils einem Satz. Wend dabei den Designstandard aus der Lektion zur Koordination zweier Spezialagenten an: kein „und" in der Verantwortungsbeschreibung, und die Grenze muss explizit benannt werden.
B3: Informationsgrenze. Erklär in zwei bis drei Sätzen, wie das Multi-Agent-Design die Informationsgrenze zwischen Bewerber- und Einrichtungsdaten erzwingt, die verhindert, dass personenbezogene Kandidatendaten in Antworten an Einrichtungen erscheinen.
B4: Fallback-Strategie. Identifizier den folgenreichsten Fehlermodus im Trevi-Design (nicht unbedingt den wahrscheinlichsten) und beschreib in zwei bis drei Sätzen die Fallback-Strategie dafür. Du kannst jeden der vier Strategietypen aus der Fehlerbehandlung nutzen. Nenn, welchen Typ du verwendest und welchen Tradeoff du dafür in Kauf nimmst.
### Aufgabe C: Abgelehnte Alternative (falls zutreffend)
Bist du während der Schnelldiagnose zu dem Schluss gekommen, dass ein besser spezifizierter Single-Agent das Problem lösen könnte, schreib eine einabsätzige Erklärung, warum das Multi-Agent-Design die abgelehnte Alternative ist. Deine Erklärung muss den Informationsgrenzfehler ausdrücklich adressieren: warum eine Single-Agent-Architektur die Grenze auch mit verbesserten Anweisungen nicht zuverlässig erzwingen kann.
Bist du zu dem Schluss gekommen, dass das Multi-Agent-Design die richtige Wahl ist (was die Evidenz stützt), überspring Aufgabe C und notier in einem Satz, dass die Single-Agent-Alternative geprüft und mit Begründung abgelehnt wurde.
## Abschlussprüfung
Prüf vor dem Einreichen deines Diagramms und deiner Begründung Folgendes:
- [ ] Enthält dein Diagramm jedes erforderliche Element aus Aufgabe A? Prüf die Liste Punkt für Punkt, die Markierung der Informationsgrenze oder ein Fallback-Pfad sind die zwei häufigsten Auslassungen.
- [ ] Ist die Verantwortungsbeschreibung jedes Spezialisten frei von „und"? Lies jede Aussage laut vor. Braucht sie „und", um vollständig zu sein, ist der Scope zu breit.
- [ ] Adressiert deine Erklärung der Informationsgrenze den Mechanismus, nicht nur die Absicht? „Die Agenten werden getrennt gehalten" ist Absicht. „Der Bewerber-Spezialist-Kontext enthält keine Facility-Account-Daten, und der Handoff des Koordinators übergibt nur die Kundenanfrage, keinen Kandidatendatensatz" ist Mechanismus.
- [ ] Ist der Fallback konkret genug, um ihn zu bauen? Zum Beispiel erzeugt ein n8n-Node Set (Edit Fields) bei fehlender Klassifizierung einen sicheren route_key; der Switch-Fallback führt dann zu einer Rückfrage. Behaupte keine tatsächlich versandte Eskalation ohne autorisierte Integration.
- [ ] Bleibt deine Begründung innerhalb von 400 Wörtern? Prägnanz ist Teil der bewerteten Fähigkeit; eine Designbegründung, die 800 Wörter braucht, um ihren Fall zu machen, ist nicht klar genug geschrieben.
## Zusammenfassung
Du hast das vollständige Sprint-2-Toolkit auf ein Szenario angewendet, das du vorher nicht kanntest. Das Diagnoseframework, der Spezialisierungsdesign-Standard, die Fehlertaxonomie und das Router-/Evaluator-Vokabular erscheinen alle in diesem Assessment als Werkzeuge, die auf ein konkretes Problem mit einer konkreten Evidenzbasis angewendet werden.
Das Trevi-Health-Szenario besitzt eine Realitätsnähe, die der Vela-Walkthrough nicht vollständig erreichen konnte: Die Verletzung von Informationsgrenzen ist ein echtes Compliance- und Vertrauensproblem. Personenbezogene Kandidatendaten in eine Antwort an eine Einrichtung zu integrieren, ist die Art von Fehler, die eine Kundenbeziehung beendet. Das Multi-Agent-Design adressiert dieses Problem strukturell und nicht nur instruktional. Genau dieses Argument müssen Diagramm und Begründung gemeinsam vermitteln.