# Projekt-Briefing — Lieferpünktlichkeit bei Adler Express GmbH

https://app.notion.com/p/Projekt-Briefing-Lieferp-nktlichkeit-bei-Adler-Express-GmbH-38e9418319f380918812f47435be636f

Für die studentische Projektgruppe. Lesen Sie diesen Brief gemeinsam zu Beginn von Sprint 1.
---

>  Dataset: https://drive.google.com/file/d/1zH9LJccPQYwdE1RpyXLX0_lK3UOzcdDm/view?usp=drive_link
## 1. Ausgangslage
Adler Express GmbH ist ein mittelständischer deutscher Paketdienstleister mit Sitz in Hamburg und Niederlassungen in 18 Städten im DACH-Raum. Das Unternehmen beschäftigt rund 1.400 Fahrerinnen und Fahrer und liefert täglich etwa 25.000 Pakete aus — vom Standardpaket bis zur Sperrgut-Lieferung für Industriekunden. Versprochen werden Lieferfenster von 4, 8, 24 oder 48 Stunden, je nach Tarif.
In den letzten 12 Monaten ist die Pünktlichkeitsquote von 87 % auf rund 70 % gefallen. Die Folgen sind spürbar: Kundenreklamationen häufen sich, Rückerstattungen kosten den Betrieb mittlere fünfstellige Beträge pro Monat, und einige Geschäftskunden drohen mit dem Wechsel zur Konkurrenz. Die operative Leitung vermutet mehrere Treiber — längere Strecken, wachsendes Liefervolumen, neue Fahrer in der Probezeit, Wetterextreme — kann aber den Effekt der einzelnen Faktoren nicht quantifizieren.
Die Geschäftsführung möchte ein Frühwarnsystem, das bereits zum Zeitpunkt der Paketannahme abschätzt, mit welcher Wahrscheinlichkeit eine bestimmte Lieferung verspätet ankommt, damit Disposition und Kundenservice gezielt eingreifen können — z. B. durch Umverteilung, frühzeitige Kundeninformation oder eine spätere Zusagezeit.
## 2. Auftrag an Ihre Gruppe
Ihre Aufgabe ist es, einen vollständigen Data-Analytics-Workflow auf den Lieferungsdaten von Adler Express zu konzipieren und umzusetzen:
1. Den Ist-Zustand der Datenlage analysieren und die Datenqualität bewerten.
1. Ein Machine Learning Canvas entwickeln, das ein realistisches Frühwarn-Konzept beschreibt.
1. Die Daten bereinigen, transformieren und visualisieren.
1. Ein Klassifikationsmodell trainieren, das zum Zeitpunkt der Paketannahme die Wahrscheinlichkeit einer Verspätung vorhersagt.
1. Ihre Erkenntnisse und Empfehlungen für die Operations-Leitung dokumentieren und präsentieren.
## 3. Stakeholder
[TABLE]
  | Person | Rolle | Erwartung an Ihre Gruppe |
  | Karim Bashir | Leiter Operations (Sponsor) | Versteht das Problem; will klar quantifizierbar wissen, welche Faktoren die Verspätungen treiben |
  | Inga Strehlow | Leiterin Customer Service | Will frühzeitig erfahren können, welche Lieferungen Risiko-Sendungen sind, um Kunden proaktiv zu informieren |
  | Hendrik Mossmann | Senior-Disponent | Will das Modell pragmatisch in der täglichen Tourenplanung verwenden — kein Black-Box-Ergebnis |
## 4. Die Daten
Sie erhalten eine CSV-Datei mit Lieferdaten der letzten zwei Jahre:
- Datei: lieferungen.csv
- Umfang: rund 12.000 Lieferungen
- Zeitraum: 1. Januar 2024 bis 31. Dezember 2025
- Encoding: UTF-8 (mit BOM)
### Datenwörterbuch
[TABLE]
  | Spalte | Typ | Beschreibung |
  | lieferung_id | Text | Eindeutige Kennung pro Lieferung (LF-000000 …) |
  | abhol_datum | Text (Datum) | Datum der Paketabholung |
  | abhol_wochentag | Text | Wochentag der Abholung (Mo–So) |
  | abhol_zeit_uhr | Ganzzahl | Stunde der Abholung (0–23) |
  | start_plz | Text | Postleitzahl Versender (5-stellig, kann führende Null haben) |
  | ziel_plz | Text | Postleitzahl Empfänger (5-stellig) |
  | strecke_km | Ganzzahl | Strecke in Kilometern |
  | paket_groesse | Text | klein, mittel, gross |
  | paket_gewicht_kg | Zahl | Gewicht des Pakets in kg |
  | fahrzeug_typ | Text | Transporter, LKW_klein, LKW_gross |
  | fahrer_id | Text | Eindeutige Kennung pro Fahrer |
  | fahrer_erfahrung_jahre | Ganzzahl | Berufserfahrung des Fahrers in Jahren |
  | wetter | Text | Wetterprognose zum Abholzeitpunkt: sonnig, bewoelkt, regen, schnee, sturm |
  | verkehr_prognose | Text | Verkehrsprognose: niedrig, mittel, hoch |
  | versprochene_zustellung_stunden | Ganzzahl | Versprochenes Lieferfenster in Stunden: 4, 8, 24 oder 48 |
  | verspaetet | Ganzzahl (0/1) | Zielvariable. 1 = Lieferung kam nach dem versprochenen Fenster an; 0 = pünktlich |
### Wichtiger Hinweis zum zeitlichen Bezug
Alle Merkmale beschreiben den Zustand der Lieferung zum Zeitpunkt der Paketannahme: Strecke, geplantes Fahrzeug, vorgesehener Fahrer, Wettervorhersage, Verkehrsprognose, versprochenes Lieferfenster. Die Zielvariable verspaetet beschreibt den tatsächlichen Ausgang. Damit ist das Modell ein echtes Frühwarn-Modell — es nutzt nur Informationen, die zum Vorhersagezeitpunkt bereits bekannt waren. Diese Trennung müssen Sie im Fachgespräch erklären können.
### Hinweise zur Datenqualität
Die Daten kommen aus dem produktiven Dispositionssystem und haben echte Mängel. Planen Sie Zeit für eine sorgfältige Bereinigung ein.
## 5. Was im Bericht stehen muss
Sie schreiben vier Kapitel, wie es die IHK-Prüfungsordnung verlangt:
- Kapitel 1 — Ist-Zustand (10 Punkte)
- Kapitel 2 — ML Canvas (10 Punkte)
- Kapitel 3 — Projektplanung und SCRUM-Dokumentation (30 Punkte)
- Kapitel 4 — Workflow, Datenmodell und Ergebnisse (20 Punkte)
### Hinweis zum „Datenmodell" in Kapitel 4
Da Sie hier mit einer einzelnen Tabelle arbeiten, ist mit „Datenmodell" die bereinigte analytische Tabelle gemeint — welche Spalten Sie behalten, welche Sie neu konstruieren (z. B. ein Feature wie paket_zu_fahrzeug_quote oder tour_volumen_kategorie) und wie die Typen festgelegt sind. Ein klassisches Stern- oder Joinschema ist nicht erforderlich.
## 6. Vorschläge für die ML-Canvas-Felder
[TABLE]
  | Feld | Vorschlag |
  | Value Proposition / Mehrwert | Disposition erkennt Risiko-Lieferungen schon vor Abfahrt und kann gegensteuern |
  | Data Sources / Datenquellen | Dispositionssystem (Lieferaufträge, Fahrzeuge, Fahrer), externe Wetter- und Verkehrs-API |
  | Prediction / Vorhersage | Klassifikation: Wird diese Lieferung im versprochenen Fenster ankommen — ja/nein |
  | Features / Merkmale | z. B. Strecke, Paketgewicht, Fahrzeugauslastung, Fahrererfahrung, Wetter, Verkehr, versprochene Zustellung — Ihre EDA zeigt, welche Merkmale tragen |
  | Learning Approach / Lernansatz | Überwachtes Lernen, binäre Klassifikation (z. B. logistische Regression, Decision Tree, Random Forest) |
  | Evaluation / Überprüfung | Recall auf der Klasse verspaetet = 1 ist die geschäftliche KPI; ROC-AUC für das Ranking; nicht Accuracy |
  | Decision / Entscheidung | Risiko-Score > Schwellwert → Disposition prüft Tour, ggf. zusätzliches Fahrzeug, ggf. Kunde informieren |
  | Impact / Auswirkung | Vermiedene Verspätungen sparen Rückerstattungen, Kundenservice-Aufwand und Kundenabwanderung |
  | Prediction Timing / Vorhersagezeitpunkt | Zum Zeitpunkt der Paketannahme, also vor Tourenstart |
  | Monitoring & Maintenance / Wartung | Quartalsweise neu trainieren; Drift-Monitoring auf Wetter-/Verkehrslage |
## 7. Mögliche Leitfragen für die Analyse
- Welche Strecken-Kategorien (kurz / mittel / lang) haben die höchste Verspätungsrate?
- Wie stark wirkt sich das Wetter aus?
- Spielt die Fahrzeug-Wahl im Verhältnis zum Paketgewicht eine Rolle?
- Welche versprochenen Lieferfenster sind am schwierigsten einzuhalten?
- Welche Merkmale haben im Modell die größte Bedeutung — und ist das operativ plausibel?
## 8. Ethik-Hinweis zur Modellbildung
Die Spalte fahrer_id ist im Datensatz enthalten, weil sie für interne Auswertungen relevant ist (z. B. „welcher Fahrer hat überdurchschnittlich viele Spätankünfte"). Sie sollte aber nicht direkt als Eingangsmerkmal in das Modell einfließen: Eine personenbezogene Vorhersage könnte als Leistungsbewertung missbraucht werden und ist mitbestimmungspflichtig. Das Merkmal fahrer_erfahrung_jahre ist sachlich gerechtfertigt und darf verwendet werden. Diskutieren Sie diese Entscheidung in der Gruppe und dokumentieren Sie sie im Bericht.
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
- Daten bereinigen (Datumsformate, Typos in fahrzeug_typ und paket_groesse, PLZ mit führender Null, fehlende Werte, Duplikate, Ausreißer)
- Vollständiges ML Canvas
- Explorative Datenanalyse
- Workflow-Dokumentation beginnen
- Sprint-1-Retrospektive, Sprint 2 planen
### Sprint 3 — Analyse, Modellierung, Bericht
- Klassifikationsmodell trainieren
- Feature Importance auswerten
- Dashboard / Visualisierungen erstellen
- Kapitel 3 und 4 ausarbeiten
- Bericht entwerfen und abgeben
- Präsentationsfolien vorbereiten
### Finalisierungsphase — Polieren und Üben
- Bericht-Feinschliff
- Persönliches Fazit und Ausblick ergänzen
- Live-Demo einüben
- Gruppenpräsentation und Fachgespräch üben
## 10. Werkzeug-Empfehlung
- Tableau für Dashboards und finale Visualisierungen
- Python für Bereinigung, EDA und Modellierung
- SQL für aggregierte Auswertungen (SQLite, DuckDB oder Postgres — Ihre Wahl)
- Google Sheets für Sprint-Log 
## 11. Erfolgskriterien
Ihr Projekt ist erfolgreich, wenn am Ende:
- Die Daten sauber bereinigt und der gesamte Cleaning-Schritt dokumentiert ist
- Das ML Canvas alle 10 Felder kohärent ausfüllt
- Mindestens ein einfaches Klassifikationsmodell trainiert und sinnvoll evaluiert wurde
- Eine klare, business-orientierte Aussage darüber existiert, welche Faktoren mit Verspätungen zusammenhängen
- Jedes Gruppenmitglied seine Sektion eigenständig im Fachgespräch verteidigen kann
### Wann ist die IHK-Prüfung bestanden?
Die IHK bewertet zwei Prüfungsteile unabhängig voneinander:
- Schriftlicher Projektbericht (70 Punkte): Kapitel 1 (10) + Kapitel 2 (10) + Kapitel 3 (30) + Kapitel 4 (20).
- Mündliche Prüfung (30 Punkte): Gruppenpräsentation und Live-Demo (Inhalt & Struktur 16 + Sprache 8 + Präsenz 6 = 30) sowie individuelles Fachgespräch.
Sie bestehen, wenn Sie in beiden Teilen jeweils mindestens 50 % der Punkte erreichen.
Viel Erfolg.
