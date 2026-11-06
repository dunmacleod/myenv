# Projekt-Briefing — Patienten-No-Shows beim Praxisverbund Rhein-Main eG

https://app.notion.com/p/Projekt-Briefing-Patienten-No-Shows-beim-Praxisverbund-Rhein-Main-eG-38e9418319f380c18c57d0f71bef1793

Für die studentische Projektgruppe. Lesen Sie diesen Brief gemeinsam zu Beginn von Sprint 1.
---

>  Dataset: https://drive.google.com/file/d/1XGk3HiyeUisriY8FAAuRrO5m_ftNRF0p/view?usp=drive_link
## 1. Ausgangslage
Der Praxisverbund Rhein-Main eG ist ein Zusammenschluss von 12 Facharztpraxen im Rhein-Main-Gebiet (Frankfurt, Mainz, Wiesbaden, Darmstadt, Hanau, Offenbach) mit den Schwerpunkten Allgemeinmedizin, Kardiologie, Orthopädie, Dermatologie, Gynäkologie, HNO und Augenheilkunde. Pro Werktag werden über alle Praxen verteilt rund 600 Termine vergeben.
Die Praxisleitung beobachtet seit zwei Jahren einen anhaltenden Anstieg sogenannter No-Shows — Patientinnen und Patienten, die einen vereinbarten Termin ohne Absage nicht wahrnehmen. Die aktuelle No-Show-Rate liegt im Verbund bei rund 14 %. Das verursacht erhebliche Kosten: leere Behandlungsplätze, verzögerte Termine für andere Patientinnen, sinkende Auslastung der Behandlungsräume. Die Geschäftsführung schätzt den jährlichen wirtschaftlichen Schaden auf 1,8–2,2 Mio. EUR.
Bisher wird allen Patientinnen und Patienten am Vortag eine SMS-Erinnerung geschickt — aber nicht zuverlässig (technische Probleme, ältere Patientinnen ohne Mobiltelefon). Die Geschäftsführung möchte verstehen, welche Termine ein erhöhtes No-Show-Risiko haben, damit gezielt zusätzliche Maßnahmen ergriffen werden können (z. B. telefonische Rückbestätigung, kürzere Erinnerungsfrist, Doppelbuchung für Hochrisiko-Slots).
## 2. Auftrag an Ihre Gruppe
1. Den Ist-Zustand der Termin- und No-Show-Daten analysieren und die Datenqualität bewerten.
1. Ein Machine Learning Canvas für ein No-Show-Frühwarn-Modell entwickeln.
1. Die Daten bereinigen, transformieren und visualisieren.
1. Ein Klassifikationsmodell trainieren, das zum Buchungszeitpunkt die No-Show-Wahrscheinlichkeit schätzt.
1. Ihre Erkenntnisse und Maßnahmenempfehlungen für die Praxisleitung dokumentieren und präsentieren.
## 3. Stakeholder
[TABLE]
  | Person | Rolle | Erwartung an Ihre Gruppe |
  | Dr. Sabine Reuter | Verbund-Geschäftsführerin (Sponsorin) | Will Klarheit über die Treiber und eine umsetzbare Maßnahmenliste |
  | Tanja Berking | Leiterin Patientenservice | Will eine pragmatische Risiko-Anzeige im Terminkalender — keine Black-Box |
  | Dr. med. Klaus Weidemann | Sprecher der ärztlichen Geschäftsführung | Achtet auf Datenschutz und faire Behandlung aller Patientengruppen |
## 4. Die Daten
- Datei: termine.csv
- Umfang: rund 13.000 Termine aus 24 Monaten
- Zeitraum: Januar 2024 bis Dezember 2025
- Encoding: UTF-8 (mit BOM)
### Datenwörterbuch
[TABLE]
  | Spalte | Typ | Beschreibung |
  | termin_id | Text | Eindeutige Terminkennung |
  | patient_id | Text | Patientennummer (pseudonymisiert) |
  | alter | Ganzzahl | Alter zum Termindatum |
  | geschlecht | Text | weiblich, maennlich, divers |
  | termin_datum | Text (Datum) | Datum des Termins (gemischte Formate) |
  | termin_zeit_uhr | Ganzzahl | Terminstunde (8–18) |
  | termin_wochentag | Text | Mo, Di, Mi, Do, Fr |
  | buchungs_vorlaufzeit_tage | Ganzzahl | Tage zwischen Buchung und Termin |
  | fachrichtung | Text | Fachrichtung (Allgemeinmedizin, …) |
  | praxis_standort | Text | Stadt der Praxis |
  | vorherige_termine_anzahl | Ganzzahl | Anzahl früherer Termine des Patienten im Verbund |
  | vorherige_no_shows_anzahl | Ganzzahl | Anzahl früherer No-Shows des Patienten |
  | entfernung_km | Zahl | Entfernung Wohnort → Praxis in km |
  | erinnerung_gesendet | Ganzzahl (0/1) | 1 = Erinnerungs-SMS versendet |
  | versicherung_typ | Text | Gesetzlich oder Privat |
  | bekannte_diagnose | Ganzzahl (0/1) | 1 = laufende Behandlung wegen chronischer Erkrankung |
  | no_show | Ganzzahl (0/1) | Zielvariable. 1 = Termin nicht wahrgenommen (kein Absage); 0 = erschienen |
### Wichtiger Hinweis zum zeitlichen Bezug
Alle Merkmale sind zum Buchungszeitpunkt bekannt: Patientenmerkmale, Termindetails, geplante Erinnerung, bisherige Historie. Die Zielvariable no_show ist das tatsächliche Ergebnis. Damit ist das Modell ein echtes Frühwarn-Modell.
## 5. Was im Bericht stehen muss
Die vier IHK-Standardkapitel.
### Hinweis zum „Datenmodell" in Kapitel 4
Einzelne Tabelle. Mit „Datenmodell" ist die bereinigte analytische Tabelle gemeint — welche Spalten bleiben, welche neu konstruiert werden (z. B. ein Feature wie no_show_quote_bisher = vorherige_no_shows_anzahl / max(vorherige_termine_anzahl, 1)), wie typenkonsistent gearbeitet wird.
## 6. Vorschläge für die ML-Canvas-Felder
[TABLE]
  | Feld | Vorschlag |
  | Value Proposition / Mehrwert | Patientenservice erkennt vor dem Termin Hochrisiko-Buchungen und kann gezielt eingreifen |
  | Data Sources / Datenquellen | Praxissystem (Termine, Patienten, Diagnosen), Kommunikationssystem (SMS-Erinnerungen) |
  | Prediction / Vorhersage | Klassifikation: Wird der Patient zum Termin erscheinen — ja/nein |
  | Features / Merkmale | Vorherige No-Shows, Buchungs-Vorlaufzeit, Entfernung, Erinnerung, Termin-Zeit, Alter, Diagnose-Status, Fachrichtung |
  | Learning Approach / Lernansatz | Überwachtes Lernen, binäre Klassifikation |
  | Evaluation / Überprüfung | Recall auf No-Show ist die KPI; ROC-AUC für Ranking; nicht Accuracy |
  | Decision / Entscheidung | Score > Schwellwert → telefonische Rückbestätigung am Vortag |
  | Impact / Auswirkung | Vermiedene No-Shows × durchschnittlicher Umsatz pro Termin |
  | Prediction Timing / Vorhersagezeitpunkt | Beim Buchen, ggf. erneut am Vortag |
  | Monitoring & Maintenance / Wartung | Quartalsweises Retraining; Performance pro Fachrichtung überwachen |
## 7. Mögliche Leitfragen
- Welche Fachrichtungen haben die höchste No-Show-Rate?
- Wie stark hängt No-Show von der Buchungs-Vorlaufzeit ab?
- Bringt die SMS-Erinnerung messbare Verbesserung?
- Ist die Entfernung ein Treiber?
- Welche Patienten-Historie schlägt am stärksten durch?
## 8. Ethik-Hinweis zur Modellbildung
Patientendaten sind besonders schützenswert. Diskutieren Sie und dokumentieren Sie im Bericht:
- geschlecht sollte standardmäßig nicht als Modell-Feature verwendet werden (Diskriminierungsrisiko). Wenn doch, mit klarer Begründung.
- alter ist sachlich relevant (jüngere Patienten haben statistisch häufiger No-Shows), aber bei der Maßnahmenwahl müssen alle Altersgruppen fair behandelt werden — kein „Wir investieren weniger in junge Patienten."
- versicherung_typ ist sachlich relevant für die Praxisverwaltung, aber dürfte nicht in der Entscheidung über Kontaktanstrengung verwendet werden.
- Das Modell darf keine medizinische Entscheidung beeinflussen — nur die Organisations-Maßnahme (Erinnerung, Doppelbuchung).
## 9. Empfohlene Aufgabenverteilung pro Sprint
### Sprint 1
- Brief lesen, Datensatz herunterladen
- Datenqualitätsprüfung
- Werkzeuge aufsetzen
- Kapitel 1 (Ist-Zustand) schreiben
- 3–5 User Stories formulieren
- ML-Canvas-Felder Value Proposition und Data Sources befüllen
- Sprint-Log starten
### Sprint 2
- Daten bereinigen (Datumsformate, Typos in fachrichtung und versicherung_typ, fehlende Werte, Duplikate, Ausreißer in buchungs_vorlaufzeit_tage)
- Vollständiges ML Canvas
- Explorative Datenanalyse (No-Show-Rate pro Fachrichtung, Vorlaufzeit-Verteilung, Effekt der Erinnerung)
- Ethik-Diskussion im Sprint-Log dokumentieren
- Workflow-Dokumentation beginnen
### Sprint 3
- Klassifikationsmodell trainieren
- Feature Importance auswerten
- Dashboard / Visualisierungen
- Kapitel 3 und 4 ausarbeiten
- Bericht entwerfen und abgeben
### Finalisierungsphase
- Bericht-Feinschliff
- Live-Demo einüben
- Gruppenpräsentation und Fachgespräch üben
## 10. Werkzeug-Empfehlung
- Tableau für Dashboards
- Python für Bereinigung und Modellierung
- SQL für aggregierte Auswertungen
- Google Sheets für Sprint-Log 
## 11. Erfolgskriterien
- Daten sauber bereinigt und der Cleaning-Schritt dokumentiert
- ML Canvas alle 10 Felder kohärent
- Klassifikationsmodell trainiert und sinnvoll evaluiert
- Klare Aussage über No-Show-Treiber im Praxisverbund
- Ethik-Diskussion im Bericht
- Jedes Gruppenmitglied verteidigt seine Sektion eigenständig
### Wann ist die IHK-Prüfung bestanden?
Wie in den anderen Briefs: ≥ 50 % unabhängig im schriftlichen Bericht (70 Punkte) UND in der mündlichen Prüfung (30 Punkte). Beide Teile müssen einzeln bestanden werden.
Viel Erfolg.