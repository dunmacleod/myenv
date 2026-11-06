# Projekt-Briefing — Umsatzprognose bei GreenGarten Versandhandel GmbH

https://app.notion.com/p/Projekt-Briefing-Umsatzprognose-bei-GreenGarten-Versandhandel-GmbH-38e9418319f38019b83dcdb3ac72541f

Für die studentische Projektgruppe. Lesen Sie diesen Brief gemeinsam zu Beginn von Sprint 1.
---
>  Dataset: https://drive.google.com/file/d/1QXbLCA2AyPV0h2XE-sg16dRPDT2k8eox/view?usp=drive_link
## 1. Ausgangslage
GreenGarten Versandhandel GmbH ist ein Berliner Online-Händler für Gartenprodukte (Pflanzen, Saatgut, Werkzeuge, Düngemittel, Töpfe, Bewässerung). Das Unternehmen führt rund 600 aktive Artikel im Sortiment und beliefert Privatkunden im DACH-Raum. Der Jahresumsatz liegt bei etwa 90 Mio. EUR; das Geschäft ist stark saisonal (Pflanzen und Saatgut dominieren im Frühjahr, Bewässerung im Sommer).
Bisher plant der Einkauf Bestellmengen und Lagerbestände per Erfahrungswerte und einfacher Excel-Vorjahresvergleiche. Das funktioniert für bewährte Produkte mit langer Historie, scheitert aber an drei Punkten:
1. Neue Produkte ohne Vorjahreshistorie werden regelmäßig zu pessimistisch oder zu optimistisch bestellt.
1. Marketing-Aktionen und Wettbewerberpreise verändern die Absatzdynamik kurzfristig — die Excel-Logik bildet das nicht ab.
1. Stockouts in der Hochsaison kosten direkten Umsatz; Überbestände binden Kapital und führen zu Abschriften.
Die Geschäftsführung möchte eine monatliche Umsatzprognose pro Produkt, die zum Monatsbeginn aus den bekannten Werten (Preis, geplantes Marketingbudget, Wettbewerberpreis, Lagerbestand, Vormonatsumsatz, Vorjahresumsatz im gleichen Monat) den voraussichtlichen Umsatz des Produkts in diesem Monat schätzt.
## 2. Auftrag an Ihre Gruppe
1. Den Ist-Zustand der Sortiments- und Verkaufsdaten analysieren und die Datenqualität bewerten.
1. Ein Machine Learning Canvas für ein produktbezogenes Umsatzprognose-Modell entwickeln.
1. Die Daten bereinigen, transformieren und visualisieren (besonders die Saisonalität).
1. Ein Regressionsmodell trainieren, das den monatlichen Umsatz pro Produkt vorhersagt.
1. Ihre Erkenntnisse und Empfehlungen für den Einkauf dokumentieren und präsentieren.
## 3. Stakeholder
[TABLE]
  | Person | Rolle | Erwartung an Ihre Gruppe |
  | Dr. Elena Hartmann | Geschäftsführerin (Sponsorin) | Will eine Aussage darüber, wie zuverlässig die Prognose ist und wie viel sie an Lagerkapital und Stockout-Risiko spart |
  | Patrick Zollner | Einkaufsleiter | Will die Prognose monatlich nutzen, um Bestellmengen festzulegen — muss daher die Annahmen verstehen |
  | Mira Bauer | Marketingleiterin | Will sehen, wie stark Marketing-Budget und Kampagnen die Prognose beeinflussen |
## 4. Die Daten
- Datei: verkaufe.csv
- Umfang: rund 14.400 Beobachtungen — eine Zeile pro (Produkt, Monat) über 24 Monate
- Zeitraum: Januar 2024 bis Dezember 2025
- Encoding: UTF-8 (mit BOM)
### Datenwörterbuch
[TABLE]
  | Spalte | Typ | Beschreibung |
  | produkt_id | Text | Eindeutige Produktkennung (PR-0000 …) |
  | kategorie | Text | Pflanzen, Saatgut, Werkzeuge, Duengemittel, Toepfe, Bewaesserung |
  | hersteller | Text | Marke / Hersteller |
  | monat | Text | Monat der Beobachtung (gemischtes Format: YYYY-MM, MM/YYYY, MM.YYYY) |
  | monat_idx | Ganzzahl | Monatszahl 1–12 (für Saisonalität) |
  | preis_eur | Gemischt | Verkaufspreis in EUR (manche Werte als Text mit €) |
  | wettbewerber_preis_eur | Zahl | Mittlerer Preis vergleichbarer Produkte bei der Konkurrenz |
  | marketingbudget_eur | Zahl | Geplantes Marketingbudget für dieses Produkt in diesem Monat |
  | kampagne_aktiv | Ganzzahl (0/1) | 1 = aktive Verkaufsaktion in diesem Monat |
  | lagerbestand | Gemischt | Lagerbestand zum Monatsbeginn (manche Werte als Text mit Stueck) |
  | bewertungen_durchschnitt | Zahl | Durchschnittliche Sterne-Bewertung (1–5) |
  | bewertungen_anzahl | Ganzzahl | Anzahl Kundenbewertungen |
  | vormonat_umsatz_eur | Zahl | Umsatz dieses Produkts im Vormonat (NaN für den ersten verfügbaren Monat) |
  | letzte_3_monate_umsatz_eur_avg | Zahl | Durchschnittsumsatz der letzten 3 Monate |
  | vorjahr_monat_umsatz_eur | Zahl | Umsatz desselben Monats im Vorjahr (NaN für 2024) |
  | umsatz_eur | Zahl | Zielvariable. Realisierter Umsatz in diesem Monat |
### Wichtiger Hinweis zum zeitlichen Bezug
Alle Merkmale beschreiben Werte, die zum Monatsbeginn bekannt sind: Preis, geplantes Marketingbudget, Wettbewerberpreis, Lagerbestand, Vormonatsumsatz, Vorjahresumsatz. Die Zielvariable umsatz_eur ist das tatsächliche Monatsergebnis. Damit ist das Modell ein echtes Prognosemodell — es nutzt nur Informationen, die zum Vorhersagezeitpunkt bereits vorlagen.
### Wichtiger Hinweis zum Train/Test-Split
Da es sich um Zeitreihendaten handelt, darf der Train/Test-Split nicht zufällig erfolgen. Sonst kommt es zu zeitlicher Datenleckage: Das Modell sieht im Training Beobachtungen aus der Zukunft des Testzeitraums. Empfohlene Aufteilung:
- Training: Beobachtungen aus dem Jahr 2024
- Test: Beobachtungen aus dem Jahr 2025
Diesen Split müssen Sie im Fachgespräch erklären können.
### Hinweise zur Datenqualität
Die Daten kommen aus dem produktiven Warenwirtschafts- und CRM-System und enthalten echte Mängel. Planen Sie Zeit für eine sorgfältige Bereinigung ein.
## 5. Was im Bericht stehen muss
Die vier IHK-Standardkapitel (Ist-Zustand, ML Canvas, Projektplanung & SCRUM, Workflow + Datenmodell + Ergebnisse).
### Hinweis zum „Datenmodell" in Kapitel 4
Da Sie hier mit einer einzelnen Tabelle arbeiten — aber mit zeitlichen Struktur und gelagten Features —, ist mit „Datenmodell" die bereinigte analytische Tabelle gemeint: welche Spalten Sie behalten, welche Lag-Features Sie verwenden, wie Sie mit fehlenden Lag-Werten in den ersten Monaten umgehen, und wie Sie den Train/Test-Split zeitlich vornehmen. Ein klassisches Stern- oder Joinschema ist nicht erforderlich.
## 6. Vorschläge für die ML-Canvas-Felder
[TABLE]
  | Feld | Vorschlag |
  | Value Proposition / Mehrwert | Einkauf erhält monatlich pro Produkt eine Umsatzprognose — bessere Bestellmengen, weniger Stockouts, weniger Überbestände |
  | Data Sources / Datenquellen | Warenwirtschaftssystem (Verkäufe, Lagerbestände, Preise), Marketingsystem (Budgets, Kampagnen), externe Wettbewerbsbeobachtung |
  | Prediction / Vorhersage | Regression: Umsatz pro Produkt im kommenden Monat in EUR |
  | Features / Merkmale | Vormonatsumsatz, gleitender 3-Monats-Durchschnitt, Vorjahresumsatz, Preis, Wettbewerberpreis, Marketingbudget, Kampagne aktiv, Saisonindex, Kategorie |
  | Learning Approach / Lernansatz | Überwachtes Lernen, Regression (z. B. lineare Regression, Decision Tree Regressor, Random Forest) |
  | Evaluation / Überprüfung | RMSE und MAE in EUR; R² als Modellgüte; zeitlicher Train/Test-Split |
  | Decision / Entscheidung | Einkaufsbestellung pro Produkt = Prognose × Sicherheitsfaktor |
  | Impact / Auswirkung | Reduzierte Lagerbindung und vermiedene Stockouts in der Hochsaison |
  | Prediction Timing / Vorhersagezeitpunkt | Monatlich, jeweils zum Monatsanfang |
  | Monitoring & Maintenance / Wartung | Modell halbjährlich neu trainieren; Performance pro Kategorie überwachen |
## 7. Mögliche Leitfragen für die Analyse
- Welche Kategorien sind am stärksten saisonal?
- Wie stark beeinflusst Marketingbudget den Umsatz?
- Welche Hersteller / welche Preislagen liefern den größten Umsatzbeitrag?
- Wie genau ist die Prognose pro Kategorie? Ist sie für Bewässerung im Sommer schwerer als für Saatgut im Frühjahr?
- Welches Merkmal trägt im Modell den größten Beitrag — und ist das geschäftlich plausibel?
## 8. Ethik- und Risiko-Hinweis
In dieser Domäne gibt es keine direkten Personenmerkmale, dafür aber ein anderes Risiko: Prognosemodelle für den Einkauf können fehlerhafte Bestellentscheidungen auslösen. Wenn das Modell systematisch unterschätzt, entstehen Stockouts (Umsatzverlust). Überschätzt es, bindet sich Kapital und es drohen Abschriften. Diskutieren Sie im Bericht (Kapitel 4) die Modellunsicherheit und schlagen Sie eine konservative Nutzung vor (z. B. Sicherheitsmarge auf die Prognose).
## 9. Empfohlene Aufgabenverteilung pro Sprint
### Sprint 1 — Setup und Problemdefinition
- Brief lesen, Datensatz herunterladen
- Datenqualitätsprüfung
- Werkzeuge aufsetzen
- Kapitel 1 (Ist-Zustand) schreiben
- 3–5 User Stories formulieren
- ML-Canvas-Felder Value Proposition und Data Sources befüllen
- Sprint-Log starten
### Sprint 2 — Bereinigung und Canvas
- Daten bereinigen (Datumsformate, Tippfehler in kategorie, Währungstext in preis_eur, lagerbestand als Text mit Einheit, fehlende Werte in Lag-Features, Duplikate, Ausreißer im Umsatz)
- Vollständiges ML Canvas
- Explorative Datenanalyse: Saisonalität pro Kategorie visualisieren
- Workflow-Dokumentation beginnen
- Sprint-1-Retrospektive, Sprint 2 planen
### Sprint 3 — Analyse, Modellierung, Bericht
- Regressionsmodell trainieren (zeitlicher Split!)
- Feature Importance auswerten
- Prognosegüte pro Kategorie auswerten
- Dashboard / Visualisierungen erstellen
- Kapitel 3 und 4 ausarbeiten
- Bericht entwerfen und abgeben
- Präsentationsfolien vorbereiten
### Finalisierungsphase
- Bericht-Feinschliff, Fazit, Ausblick
- Live-Demo einüben
- Gruppenpräsentation und Fachgespräch üben
## 10. Werkzeug-Empfehlung
- Tableau für Dashboards (besonders die saisonalen Heatmaps)
- Python für Bereinigung, EDA, Modellierung
- SQL für aggregierte Auswertungen
- Google Sheets für Sprint-Log 
## 11. Erfolgskriterien
Ihr Projekt ist erfolgreich, wenn am Ende:
- Die Daten sauber bereinigt sind und der gesamte Cleaning-Schritt dokumentiert ist
- Der Train/Test-Split zeitlich erfolgt und das im Bericht erklärt ist
- Das ML Canvas alle 10 Felder kohärent ausfüllt
- Mindestens ein Regressionsmodell trainiert und mit sinnvollen Metriken (RMSE, MAE, R²) bewertet wurde
- Eine klare, business-orientierte Aussage darüber existiert, welche Merkmale die Prognose tragen
- Jedes Gruppenmitglied seine Sektion eigenständig im Fachgespräch verteidigen kann
### Wann ist die IHK-Prüfung bestanden?
Die IHK bewertet zwei Prüfungsteile unabhängig voneinander:
- Schriftlicher Projektbericht (70 Punkte): Kapitel 1 (10) + Kapitel 2 (10) + Kapitel 3 (30) + Kapitel 4 (20).
- Mündliche Prüfung (30 Punkte): Gruppenpräsentation und Live-Demo (Inhalt & Struktur 16 + Sprache 8 + Präsenz 6 = 30) sowie individuelles Fachgespräch.
Sie bestehen, wenn Sie in beiden Teilen jeweils mindestens 50 % der Punkte erreichen.
Viel Erfolg.