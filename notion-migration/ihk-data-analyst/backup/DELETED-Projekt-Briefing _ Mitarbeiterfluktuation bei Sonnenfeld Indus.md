# Projekt-Briefing — Mitarbeiterfluktuation bei Sonnenfeld Industries GmbH

https://app.notion.com/p/Projekt-Briefing-Mitarbeiterfluktuation-bei-Sonnenfeld-Industries-GmbH-38e9418319f38082a199f43a162c04c1

Für die studentische Projektgruppe. Lesen Sie diesen Brief gemeinsam zu Beginn von Sprint 1.
---

>  Dataset: https://drive.google.com/file/d/1mNhFHa8fu3o8bLleBoojrU-8wcfKnXkz/view?usp=drive_link
## 1. Ausgangslage
Sonnenfeld Industries GmbH ist ein mittelständisches deutsches Industrieunternehmen mit Sitz in Stuttgart und rund 10.000 Mitarbeitenden in den Bereichen Produktion, Logistik, Vertrieb, IT, Finanzen, Personal und Marketing. Das Unternehmen produziert hochwertige Komponenten für den Maschinenbau und beliefert hauptsächlich Industriekunden im DACH-Raum.
In den letzten beiden Jahren ist die Mitarbeiterfluktuation merklich angestiegen. Die Personalabteilung schätzt die jährliche Kündigungsquote inzwischen auf rund 17 %, während sie zuvor unter 10 % lag. Der Effekt ist branchenuntypisch hoch und verursacht erhebliche Kosten: Neueinstellungen, Onboarding, Wissensverlust, Überlastung der verbleibenden Teams.
Die Geschäftsführung möchte verstehen, welche Faktoren mit erhöhtem Kündigungsrisiko zusammenhängen, und mittelfristig ein einfaches Frühwarnsystem aufbauen, das gefährdete Mitarbeitende rechtzeitig identifiziert, damit die Personalabteilung gezielt intervenieren kann (z. B. Mitarbeitergespräch, Weiterentwicklungsangebot, Anpassung des Arbeitspensums).
## 2. Auftrag an Ihre Gruppe
Ihre Aufgabe ist es, einen vollständigen Data-Analytics-Workflow auf den HR-Daten von Sonnenfeld zu konzipieren und umzusetzen:
1. Den Ist-Zustand der HR-Datenlage analysieren und die Datenqualität bewerten.
1. Ein Machine Learning Canvas entwickeln, das ein realistisches Frühwarn-Konzept beschreibt.
1. Die Daten bereinigen, transformieren und visualisieren.
1. Ein einfaches Klassifikationsmodell trainieren, das vorhersagt, ob ein Mitarbeitender voraussichtlich kündigen wird.
1. Ihre Erkenntnisse und Empfehlungen für die HR-Leitung dokumentieren und präsentieren.
## 3. Stakeholder
[TABLE]
  | Person | Rolle | Erwartung an Ihre Gruppe |
  | Dr. Petra Lindner | Personalleiterin (Sponsorin) | Versteht das Problem; will klare Aussagen darüber, welche Faktoren die Fluktuation treiben |
  | Markus Wagner | Leiter HR-Analytics | Erwartet eine sauber dokumentierte Lösung, die das HR-Team nach Projektende weiterführen kann |
  | Stefanie Voss | Betriebsratsvorsitzende | Achtet auf Datenschutz und faire Modellbildung — keine diskriminierenden Merkmale, keine personenbezogenen Vorhersagen ohne Begründung |
## 4. Die Daten
Sie erhalten eine CSV-Datei mit Mitarbeiterdaten:
- Datei: mitarbeiter.csv
- Umfang: rund 10.000 Mitarbeitende
- Stichtag: 31. Dezember des letzten Geschäftsjahres
- Encoding: UTF-8 (mit BOM)
### Datenwörterbuch
[TABLE]
  | Spalte | Typ | Beschreibung |
  | mitarbeiter_id | Text | Eindeutige Kennung pro Mitarbeitendem (MA-00000 bis MA-09999) |
  | alter | Ganzzahl | Alter zum Stichtag in Jahren |
  | geschlecht | Text | weiblich, männlich, divers |
  | abteilung | Text | Abteilung des Mitarbeitenden zum Stichtag |
  | position | Text | Hierarchieebene zum Stichtag: Junior, Senior, Lead, Manager |
  | eintrittsdatum | Text (Datum) | Datum des Vertragsbeginns |
  | betriebszugehoerigkeit_jahre | Ganzzahl | Vollendete Jahre im Unternehmen zum Stichtag |
  | gehalt_brutto | Gemischt | Jährliches Bruttogehalt in Euro zum Stichtag |
  | ueberstunden_monat | Ganzzahl | Durchschnittliche Überstunden pro Monat im letzten Jahr |
  | zufriedenheit | Ganzzahl | Letzte Mitarbeiterumfrage vor dem Stichtag, Skala 1–5 |
  | abwesenheitstage_jahr | Ganzzahl | Krankheits- und Sonderurlaubstage im letzten Jahr |
  | gekuendigt | Ganzzahl (0/1) | Zielvariable. 1 = der Mitarbeitende hat innerhalb der 12 Monate nach dem Stichtag gekündigt; 0 = weiter beschäftigt |
### Wichtiger Hinweis zum zeitlichen Bezug
Alle Merkmale (alter, gehalt_brutto, ueberstunden_monat, zufriedenheit, abwesenheitstage_jahr usw.) beschreiben den Zustand der Person zum Stichtag. Die Zielvariable gekuendigt beschreibt, ob diese Person in den 12 Monaten nach dem Stichtag gekündigt hat. Dadurch ist das Modell ein echtes Frühwarn-Modell — es nutzt nur Informationen, die zum Vorhersagezeitpunkt bereits bekannt waren. Diese Trennung müssen Sie im Fachgespräch erklären können.
### Hinweise zur Datenqualität
Die Daten kommen aus dem produktiven HR-System und haben echte Mängel. Planen Sie Zeit für eine sorgfältige Bereinigung ein — Ergebnisse, die auf ungeprüften Daten basieren, sind im Fachgespräch nicht verteidigbar.
## 5. Was im Bericht stehen muss
Sie schreiben vier Kapitel, wie es die IHK-Prüfungsordnung verlangt:
- Kapitel 1 — Ist-Zustand (10 Punkte): Wie ist die aktuelle Lage bei Sonnenfeld? Welche Analytics-Prozesse existieren bereits in der Personalabteilung? Warum ist dieses Projekt relevant?
- Kapitel 2 — ML Canvas (10 Punkte): Alle 10 Felder, kohärent, geschäftsorientiert.
- Kapitel 3 — Projektplanung und SCRUM-Dokumentation (30 Punkte): Sprint-Log, User Stories, Meilensteine, Retrospektiven.
- Kapitel 4 — Workflow, Datenmodell und Ergebnisse (20 Punkte): Vollständige Workflow-Dokumentation von Import bis Export, kohärentes Datenmodell, sauber präsentierte Ergebnisse.
### Hinweis zum „Datenmodell" in Kapitel 4
Da Sie hier nur mit einer einzelnen Tabelle arbeiten, ist mit „Datenmodell" die bereinigte analytische Tabelle gemeint — also welche Spalten Sie behalten, welche neu konstruieren (z. B. ein Feature wie gehaltsquartil oder tenure_band), wie die Spalten aufeinander aufbauen und welche Typen Sie verwenden. Ein klassisches Stern- oder Joinschema ist hier nicht erforderlich.
## 6. Vorschläge für die ML-Canvas-Felder
Diese Vorschläge sind Startpunkte — Sie passen sie an, sobald Sie die Daten besser kennen.
[TABLE]
  | Feld | Vorschlag |
  | Value Proposition / Mehrwert | HR-Team erkennt frühzeitig Mitarbeitende mit erhöhtem Kündigungsrisiko und kann gezielt intervenieren |
  | Data Sources / Datenquellen | HR-System (Stammdaten, Eintrittsdatum, Gehalt), Zeiterfassung (Überstunden, Abwesenheit), jährliche Mitarbeiterumfrage (Zufriedenheit) |
  | Prediction / Vorhersage | Klassifikation: Wird ein Mitarbeitender in den nächsten 12 Monaten kündigen — ja oder nein |
  | Features / Merkmale | z. B. Zufriedenheit, Überstunden, Betriebszugehörigkeit, Alter, Abteilung — Ihr EDA-Ergebnis zeigt, welche Merkmale das Signal tragen |
  | Learning Approach / Lernansatz | Überwachtes Lernen, binäre Klassifikation (z. B. logistische Regression, Decision Tree, Random Forest) |
  | Evaluation / Überprüfung | Recall (Anteil der erkannten Kündigungen) ist wichtiger als Accuracy, da die Klasse gekuendigt = 1 unterrepräsentiert ist |
  | Decision / Entscheidung | Bei Risiko-Score > Schwellwert: HR-Gespräch und individuelle Maßnahmen |
  | Impact / Auswirkung | Senkung der Fluktuationsquote um X Prozentpunkte spart pro Jahr Y € an Such- und Onboarding-Kosten |
  | Prediction Timing / Vorhersagezeitpunkt | Monatlich oder quartalsweise, basierend auf den jeweils aktuellen Daten |
  | Monitoring & Maintenance / Wartung | Modell jährlich neu trainieren; Performance gegen tatsächliche Kündigungsrate prüfen |
## 7. Mögliche Leitfragen für die Analyse
- Welche Abteilungen haben die höchste Fluktuationsrate?
- Hängt die Zufriedenheit mit Überstunden oder Position zusammen?
- Wie verteilt sich die Betriebszugehörigkeit bei Kündigenden vs. Bleibenden?
- Gibt es Hinweise auf systematische Unterschiede bei Gehalt oder Alter zwischen Abteilungen?
- Welche Merkmale haben im Modell die größte Bedeutung — und ist das geschäftlich plausibel?
## 8. Ethik-Hinweis zur Modellbildung
Die Spalte geschlecht ist im Datensatz enthalten, weil Sie sich im Fachgespräch zu fairer Modellbildung äußern können sollten — nicht weil Sie sie automatisch als Eingangsmerkmal in das Modell einbauen müssen. Ein Frühwarn-Modell, das Mitarbeitende anhand des Geschlechts klassifiziert, ist rechtlich und ethisch problematisch und wird vom Betriebsrat zurückgewiesen. Diskutieren Sie in Ihrer Gruppe bewusst, ob geschlecht ein Feature des Modells sein soll, und begründen Sie Ihre Entscheidung im Bericht (Kapitel 4) sowie im Fachgespräch.
## 9. Empfohlene Aufgabenverteilung pro Sprint
Diese Verteilung ist ein Vorschlag — passen Sie sie an die Stärken Ihrer Gruppe an. Bewahren Sie aber die Sichtbarkeit jeder Person im Bericht und im Fachgespräch.
### Sprint 1 — Setup und Problemdefinition
- Brief lesen, Datensatz herunterladen, erstmals öffnen
- Datenqualitätsprüfung: fehlende Werte, Formate, Duplikate, Ausreißer identifizieren
- Werkzeuge aufsetzen (Tableau, Python, gemeinsames SQL-Tool)
- Kapitel 1 (Ist-Zustand) schreiben
- 3–5 User Stories formulieren
- ML-Canvas-Felder Value Proposition und Data Sources befüllen
- Sprint-Log starten
### Sprint 2 — Bereinigung und Canvas
- Daten bereinigen: Datumsformate vereinheitlichen, Tippfehler in abteilung normalisieren, gehalt_brutto als Zahl parsen, fehlende Werte sinnvoll behandeln, Duplikate entfernen, Ausreißer bewerten
- Vollständiges ML Canvas (alle 10 Felder)
- Explorative Datenanalyse (Verteilungen, Korrelationen, Auffälligkeiten)
- Workflow-Dokumentation für Kapitel 4 beginnen
- Sprint-1-Retrospektive, Sprint 2 planen
### Sprint 3 — Analyse, Modellierung, Bericht
- Klassifikationsmodell trainieren (Empfehlung: einfaches Modell wie logistische Regression oder Random Forest)
- Feature Importance auswerten
- Dashboard / Visualisierungen für die Präsentation erstellen
- Kapitel 3 (Projektplanung) und Kapitel 4 (Workflow + Ergebnisse) ausarbeiten
- Bericht entwerfen, Bericht abgeben
- Präsentationsfolien vorbereiten
### Finalisierungsphase — Polieren und Üben
- Letzter Bericht-Feinschliff
- Persönliches Lernergebnis-Fazit und Ausblick ergänzen
- Live-Demo des Workflows einüben
- Gruppenpräsentation und Fachgespräch üben
## 10. Werkzeug-Empfehlung
Ihre Gruppe entscheidet selbst über den Werkzeug-Mix. Pragmatische Empfehlung:
- Tableau für Dashboards und finale Visualisierungen
- Python für Bereinigung, EDA und Modellierung (auch einfache Skripte sind ok)
- SQL für aggregierte Auswertungen (SQLite, DuckDB oder Postgres — Ihre Wahl)
- Google Sheets für Sprint-Log 
Wer kein Python möchte, kann die Bereinigung auch in Tableau Prep oder Excel lösen — das Ergebnis muss aber im Bericht und in der Demo nachvollziehbar dokumentiert sein.
## 11. Erfolgskriterien
Ihr Projekt ist erfolgreich, wenn am Ende:
- Die Daten sauber bereinigt sind und der gesamte Cleaning-Schritt dokumentiert ist
- Das ML Canvas alle 10 Felder kohärent ausfüllt
- Mindestens ein einfaches Klassifikationsmodell trainiert und sinnvoll evaluiert wurde
- Eine klare, business-orientierte Aussage darüber existiert, welche Faktoren mit Fluktuation zusammenhängen
- Jedes Gruppenmitglied seine Sektion eigenständig im Fachgespräch verteidigen kann
### Wann ist die IHK-Prüfung bestanden?
Die IHK bewertet zwei Prüfungsteile unabhängig voneinander:
- Schriftlicher Projektbericht (70 Punkte): Kapitel 1 (10) + Kapitel 2 (10) + Kapitel 3 (30) + Kapitel 4 (20).
- Mündliche Prüfung (30 Punkte): Gruppenpräsentation und Live-Demo (Inhalt & Struktur 16 + Sprache 8 + Präsenz 6 = 30) sowie individuelles Fachgespräch.
Sie bestehen, wenn Sie in beiden Teilen jeweils mindestens 50 % der Punkte erreichen. Ein hervorragender Bericht rettet kein schwaches Fachgespräch und umgekehrt — bereiten Sie beide Teile gleichermaßen vor.
Viel Erfolg.