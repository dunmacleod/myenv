# Projekt-Briefing — Kreditrisiko-Frühwarnung bei Schwarzwald Kreditkasse AG

https://app.notion.com/p/Projekt-Briefing-Kreditrisiko-Fr-hwarnung-bei-Schwarzwald-Kreditkasse-AG-38e9418319f3801aaa42f9d38987475a

Für die studentische Projektgruppe. Lesen Sie diesen Brief gemeinsam zu Beginn von Sprint 1.
---

>  Dataset: https://drive.google.com/file/d/18wIUJ_tzYQMvhgaoixUDc2wJYtGptcpy/view?usp=drive_link
## 1. Ausgangslage
Schwarzwald Kreditkasse AG ist eine fiktive Regionalbank mit Sitz in Freiburg und 28 Filialen in Baden-Württemberg. Sie vergibt vor allem Konsumkredite an Privatkunden zwischen 500 und 80.000 EUR mit Laufzeiten von 12 bis 84 Monaten. Das Kreditportfolio umfasst rund 60.000 aktive Kredite.
In den letzten drei Geschäftsjahren ist die Ausfallquote von 8 % auf rund 17 % gestiegen. Die Risiko-Abteilung vermutet, dass die bestehende, vor allem auf dem internen Kreditrating basierende Risikoeinschätzung nicht mehr ausreicht: Bestimmte Kombinationen aus Verschuldungsquote, Beschäftigungsstabilität und Kreditzweck werden vom Rating nicht gut abgebildet. Die Folge sind Kreditausfälle in mittlerer sechsstelliger Höhe pro Monat sowie wachsender Aufwand für Mahnungen und Forderungsausfall-Management.
Die Geschäftsführung möchte ein Frühwarn-Modell, das schon bei Kreditantragstellung das Ausfallrisiko zuverlässiger einschätzt als das bisherige Rating allein. Das Modell soll keine Kreditentscheidungen automatisieren, sondern den Risiko-Analystinnen und -Analysten eine zweite, datengetriebene Einschätzung liefern.
## 2. Auftrag an Ihre Gruppe
1. Den Ist-Zustand der Kreditrisiko-Datenlage analysieren und die Datenqualität bewerten.
1. Ein Machine Learning Canvas für ein Kreditrisiko-Frühwarn-Modell entwickeln.
1. Die Daten bereinigen, transformieren und visualisieren.
1. Ein Klassifikationsmodell trainieren, das bei Antragstellung die Ausfallwahrscheinlichkeit schätzt.
1. Ihre Erkenntnisse, Empfehlungen und Ethik-Überlegungen für die Risiko-Abteilung dokumentieren und präsentieren.
## 3. Stakeholder
[TABLE]
  | Person | Rolle | Erwartung an Ihre Gruppe |
  | Dr. Robert Schäfer | Bereichsleiter Risiko (Sponsor) | Will eine zweite Einschätzung neben dem bestehenden Rating, ohne dass das Rating ersetzt wird |
  | Yvonne Pfeifer | Compliance-Officer | Achtet auf rechtliche und ethische Vertretbarkeit jeder Feature-Auswahl |
  | Norbert Lange | Senior Risk-Analyst | Will das Modell pragmatisch im Antragsprozess nutzen — verständliche Begründung pro Antrag muss möglich sein |
## 4. Die Daten
- Datei: kredite.csv
- Umfang: rund 11.000 Kreditanträge mit bekanntem Ausgang
- Zeitraum: Januar 2022 bis Dezember 2025
- Encoding: UTF-8 (mit BOM)
### Datenwörterbuch
### Wichtiger Hinweis zum zeitlichen Bezug
Alle Merkmale beschreiben den Zustand des Antragstellers zum Zeitpunkt der Antragstellung: Einkommen, Beschäftigungsdauer, bestehende Kredite, Rating, Wohnsituation, beantragter Kreditbetrag. Die Zielvariable ausfall ist das beobachtete Ergebnis am Ende der Kreditlaufzeit. Damit ist das Modell ein echtes Frühwarn-Modell — es nutzt nur Informationen, die zur Antragsbearbeitung bereits vorlagen.
## 5. Was im Bericht stehen muss
[TABLE]
  | Spalte | Typ | Beschreibung |
  | kredit_id | Text | Eindeutige Kreditkennung |
  | antrag_datum | Text (Datum) | Datum der Antragstellung (gemischte Formate) |
  | kunden_id | Text | Kundennummer |
  | alter | Ganzzahl | Alter des Antragstellers zum Antragszeitpunkt |
  | nettoeinkommen_monatlich_eur | Zahl | Monatliches Nettoeinkommen in EUR |
  | beschaeftigungsdauer_monate | Ganzzahl | Beschäftigungsdauer im aktuellen Job in Monaten |
  | selbststaendig | Ganzzahl (0/1) | 1 = selbständig, 0 = angestellt |
  | branche | Text | Branche (Industrie, Handel, …) |
  | vorhandene_kredite_anzahl | Ganzzahl | Anzahl bereits laufender Kreditverträge laut interner Bonitätsauskunft (SCHUFA-artige Abfrage). Zählt nur klassische Kreditverträge — keine Leasing- oder Ratenzahlungsverträge.  |
  | kreditbetrag_eur | Gemischt | Beantragter Kreditbetrag in EUR (teilweise als Text mit EUR) |
  | laufzeit_monate | Ganzzahl | Vereinbarte Laufzeit in Monaten |
  | verwendungszweck | Text | Konsum, Auto, Renovierung, Umschuldung, Bildung, Sonstiges |
  | bestehender_kunde_jahre | Zahl | Wie lange ist der Antragsteller bereits Kunde der Bank |
  | kreditrating_intern | Text | Internes Kreditrating: A (beste Bonität) bis F (schlechteste) — teilweise andere Formate |
  | wohnen | Text | Eigentum, Miete, Bei_Eltern |
  | monatliche_raten_andere_kredite_eur | Zahl | Selbstauskunft aus dem Antragsformular: monatliche Belastung durch alle Zahlungsverpflichtungen außerhalb dieses Antrags — inkl. Leasing, finanzierte Käufe, Kreditkarten-Mindestraten, Familiendarlehen. Nicht aus der Bonitätsauskunft.  |
  | ausfall | Ganzzahl (0/1) | Zielvariable. 1 = Kredit wurde innerhalb der Laufzeit nicht vollständig zurückgezahlt; 0 = pünktlich bedient |
Die vier IHK-Standardkapitel (Ist-Zustand, ML Canvas, Projektplanung & SCRUM, Workflow + Datenmodell + Ergebnisse).
### Hinweis zum „Datenmodell" in Kapitel 4
Da Sie hier mit einer einzelnen Tabelle arbeiten, ist mit „Datenmodell" die bereinigte analytische Tabelle gemeint — welche Spalten Sie behalten, welche Quoten Sie als Features neu konstruieren (Verschuldungsquote = monatliche_raten_andere_kredite_eur / nettoeinkommen_monatlich_eur, Kreditquote = kreditbetrag_eur / (nettoeinkommen × laufzeit)), wie Sie das Rating ordinal codieren statt One-Hot.
## 6. Vorschläge für die ML-Canvas-Felder
[TABLE]
  | Feld | Vorschlag |
  | Value Proposition / Mehrwert | Risiko-Analyst erhält pro Antrag eine zweite, datengetriebene Ausfallwahrscheinlichkeit |
  | Data Sources / Datenquellen | Antragsformular, Kundenstammdaten, Bonitätsauskunft (intern), Kreditportfolio-Historie |
  | Prediction / Vorhersage | Klassifikation: Wird dieser Kredit innerhalb der Laufzeit ausfallen — ja/nein |
  | Features / Merkmale | Einkommen, Beschäftigungsdauer, Selbständigkeit, bestehende Kredite, Kreditbetrag, Laufzeit, Rating, Wohnsituation, Verschuldungsquote, Kreditquote |
  | Learning Approach / Lernansatz | Überwachtes Lernen, binäre Klassifikation (logistische Regression, Decision Tree, Random Forest — bevorzugt erklärbare Modelle) |
  | Evaluation / Überprüfung | Recall auf Ausfall ist die Geschäfts-KPI; ROC-AUC für das Ranking; nicht Accuracy |
  | Decision / Entscheidung | Modell-Score > Schwellwert → Antrag zur manuellen Prüfung; Antrag wird nicht automatisch abgelehnt |
  | Impact / Auswirkung | Vermiedene Ausfälle ./. zusätzliche Prüfaufwände ./. Risiko der Diskriminierung |
  | Prediction Timing / Vorhersagezeitpunkt | Zum Zeitpunkt der Antragsbearbeitung |
  | Monitoring & Maintenance / Wartung | Halbjährliches Retraining; Fairness-Monitoring (Ausfall-Rate je Altersgruppe, Region, Geschlecht) |
## 7. Mögliche Leitfragen für die Analyse
- Welche Verwendungszwecke haben die höchste Ausfallquote?
- Wie stark korreliert das interne Rating mit dem tatsächlichen Ausfall?
- Welche Verschuldungsquote ist ein „kritischer" Schwellwert?
- Verhält sich das Risiko von selbständigen Antragstellern anders als von Angestellten?
- Welche Merkmale tragen im Modell den meisten Beitrag — und sind sie geschäftlich plausibel und ethisch vertretbar?
## 8. Ethik-Hinweis zur Modellbildung — besonders wichtig in dieser Domäne
Die Daten enthalten Merkmale, deren Verwendung als Modell-Feature rechtlich und ethisch problematisch sein kann:
- alter — könnte indirekt diskriminieren (z. B. ältere Antragsteller systematisch schlechter ranken).
- wohnen — der Status "Bei_Eltern" korreliert mit jüngerem Alter; die Verwendung kann altersdiskriminierend wirken.
- branche — bestimmte Branchen sind sozial markiert; Vorsicht ist geboten.
- selbststaendig — sachlich gerechtfertigt (andere Einkommensvolatilität), aber sollte konservativ verwendet werden.
Im Bericht (Kapitel 4) muss Ihre Gruppe explizit dokumentieren, welche dieser Merkmale Sie ins Modell aufnehmen, welche Sie ausschließen, und warum. Eine Modellempfehlung ohne diese Diskussion ist im Fachgespräch nicht verteidigbar. Die Compliance-Officerin Yvonne Pfeifer ist im Stakeholder-Set genannt, weil dieser Punkt geprüft wird.
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
- Daten bereinigen (Datumsformate, Currency-Text in kreditbetrag_eur, Tippfehler in verwendungszweck, mehrere Rating-Formate, fehlende Werte, Duplikate, Ausreißer)
- Engineered features: schulden_einkommen_quote, kreditquote, ordinale Rating-Variable
- Vollständiges ML Canvas
- Explorative Datenanalyse — besonders Ausfall-Rate nach Rating und Verschuldung
- Erste Ethik-Diskussion in der Gruppe und im Sprint-Log dokumentieren
- Workflow-Dokumentation beginnen
- Sprint-1-Retrospektive, Sprint 2 planen
### Sprint 3
- Klassifikationsmodell trainieren (Empfehlung: erklärbare Modelle wie logistische Regression)
- Feature Importance auswerten — mit Permutationsverfahren, nicht nur Impurity
- Fairness-Auswertung pro Altersgruppe und Branche
- Kapitel 3 und 4 ausarbeiten (Ethik-Diskussion in Kapitel 4!)
- Bericht entwerfen und abgeben
- Präsentationsfolien vorbereiten
### Finalisierungsphase
- Bericht-Feinschliff, Fazit, Ausblick
- Live-Demo einüben
- Gruppenpräsentation und Fachgespräch üben
## 10. Werkzeug-Empfehlung
- Tableau für Visualisierungen
- Python für Bereinigung, Feature Engineering, Modellierung
- SQL für aggregierte Auswertungen
- Google Sheets für Sprint-Log 
## 11. Erfolgskriterien
Ihr Projekt ist erfolgreich, wenn am Ende:
- Die Daten sauber bereinigt und der gesamte Cleaning-Schritt dokumentiert ist
- Mindestens ein engineered ratio feature (Verschuldungsquote oder Kreditquote) verwendet wurde
- Das Rating ordinal codiert ist (nicht nur One-Hot)
- Das ML Canvas alle 10 Felder kohärent ausfüllt
- Mindestens ein Klassifikationsmodell trainiert und mit Recall/ROC-AUC bewertet wurde
- Eine explizite, dokumentierte Ethik-Diskussion zur Feature-Auswahl im Bericht steht
- Jedes Gruppenmitglied seine Sektion eigenständig im Fachgespräch verteidigen kann
### Wann ist die IHK-Prüfung bestanden?
Die IHK bewertet zwei Prüfungsteile unabhängig voneinander:
- Schriftlicher Projektbericht (70 Punkte): Kapitel 1 (10) + Kapitel 2 (10) + Kapitel 3 (30) + Kapitel 4 (20).
- Mündliche Prüfung (30 Punkte): Gruppenpräsentation und Live-Demo (Inhalt & Struktur 16 + Sprache 8 + Präsenz 6 = 30) sowie individuelles Fachgespräch.
Sie bestehen, wenn Sie in beiden Teilen jeweils mindestens 50 % der Punkte erreichen.
Viel Erfolg.