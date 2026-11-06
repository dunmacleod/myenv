# Workflow, Datenmodell und Ergebnisse

https://app.notion.com/p/Workflow-Datenmodell-und-Ergebnisse-38b9418319f381e8a6b4f12d8ed171dd

Eine Woche vor der Prüfung sitzen viele Gruppen vor dem Bericht und merken: das Modell ist trainiert, das Dashboard gebaut, die Kennzahlen berechnet — aber sie können nicht sauber dokumentieren, wie sie dorthin gekommen sind. Der Quellordner enthält drei Versionen der CSV, zwei alte Notebooks, und niemand weiß mehr, in welcher Reihenfolge was getan wurde.
Kapitel 4 löst dieses Problem. Sie dokumentieren den vollständigen Workflow von der Rohdatei bis zum Ergebnis — sodass jemand anders ihn nachvollziehen könnte. Plus: Sie präsentieren die Ergebnisse selbst, kohärent und ehrlich.
## Lernergebnisse
Nach dieser Lektion können Sie:
- die sieben Workflow-Schritte (Quelle, Import, Bereinigung, Transformation, Analyse, Visualisierung, Export) für ein konkretes Datenprojekt eigenständig dokumentieren,
- erklären, was mit „Datenmodell" in einer Single-Table-Anwendung gemeint ist — und es gegenüber einem Stern- / Joinschema abgrenzen.
💭 Verwandte Vorlage — Kapitel 4 ist in Berichtsvorlage_IHK.docx mit Sub-Headings (4.1 Workflow, 4.2 Datenmodell, 4.3 Ergebnisse, 4.4 Bewertung, 4.5 Visualisierungen) scaffoldet.

## Was Kapitel 4 wert ist
[TABLE]
  | Kennzahl | Wert |
  | Punkte | 20 von 70 |
  | Zielumfang | ca. 3–4 Seiten |
  | Pflicht | Workflow-Dokumentation, kohärentes Datenmodell, präsentierte Ergebnisse, Zuverlässigkeit der Ergebnisse |
Die IHK-Bewertungsrubrik bewertet:
- Ausarbeitung des Workflows — alle Schritte dokumentiert?
- Schlüssigkeit des Datenmodells — ist die analytische Tabelle nachvollziehbar?
- Saubere Dokumentation — lesbar, konsistent, korrekt zitiert?
- Zuverlässigkeit des Ergebnisses — sind die berichteten Zahlen plausibel und bewertet?

## Die sieben Workflow-Schritte
![image]((notion-hosted file))
Die sieben Workflow-Schritte

Ein vollständiger Daten-Workflow besteht aus sieben Schritten. Dokumentieren Sie jeden mit ein bis zwei Absätzen.
[TABLE]
  | # | Schritt | Was Sie dokumentieren |
  | 1 | Quelle | Woher kommen die Daten? Welche Datei, welches System, welcher Zeitraum, welche Lizenz? |
  | 2 | Import | Wie laden Sie die Daten? Encoding, Trennzeichen, erste Validierung. |
  | 3 | Bereinigung | Welche Datenqualitäts-Probleme haben Sie behoben? Pro Problem: Diagnose, Entscheidung, Begründung. |
  | 4 | Transformation | Welche neuen Spalten haben Sie konstruiert (Feature Engineering, Aggregationen, Joins)? |
  | 5 | Analyse / Modellierung | EDA-Ergebnisse, Modelltyp, Trainingsablauf, Train/Test-Split. |
  | 6 | Visualisierung | Welche Charts / Dashboards haben Sie erstellt — und welche Aussage sollen sie transportieren? |
  | 7 | Export / Ergebnis-Übergabe | Wohin gehen die Ergebnisse (CSV, Dashboard, API)? Welcher Stakeholder konsumiert sie? |
Diese sieben Schritte sind kein Ritual — sie sind die Reihenfolge, in der jemand anderes Ihren Workflow neu aufbauen müsste. Wenn Schritt 3 fehlt, scheitert Schritt 4.

## Workflow-Dokumentation — gut vs. schlecht
Schlecht (Ergebnis ohne Schritt):
> „Wir haben die Daten bereinigt und ein Modell trainiert. Die Genauigkeit liegt bei 0,72."
Gut (Schritt mit Diagnose und Entscheidung):
> „Bei der Datenqualitätsprüfung fanden wir 8.020 Zeilen, davon 20 exakte Duplikate (Spalte für Spalte identisch). Wir entfernten diese mit drop_duplicates() und reduzierten den Datensatz auf 8.000 unique Mitarbeitende. Die Duplikate stammen wahrscheinlich aus einem doppelten HR-Export — diese Annahme dokumentierten wir, ohne sie zu verifizieren."
Der zweite Stil zeigt: diagnostiziert, entschieden, begründet, dokumentiert.

## Das „Datenmodell"-Sektion in Kapitel 4
In den meisten Kursdatensätzen arbeiten Sie mit einer einzelnen Tabelle (single-table). Mit „Datenmodell" ist hier nicht ein Stern- oder Joinschema gemeint, sondern die bereinigte analytische Tabelle — also welche Spalten Sie am Ende haben, was sie bedeuten, welche Typen sie tragen.
Tabelle, die in Kapitel 4 stehen sollte:
[TABLE]
  | Spalte | Typ | Bedeutung | Herkunft |
  | kunde_id | string | eindeutige Kunden-ID | Original |
  | bestellfrequenz_90d | int | Anzahl Bestellungen letzte 90 Tage | konstruiert aus bestellungen.csv |
  | umsatz_30d | float | Umsatz letzte 30 Tage in EUR | konstruiert aus bestellungen.csv |
  | support_tickets_anzahl | int | offene + geschlossene Tickets | aus support_tickets.csv |
  | gekuendigt | int (0/1) | Zielvariable | aus Bestellverhalten abgeleitet |
Wenn Sie neue Features konstruiert haben, beschreiben Sie kurz, warum Sie sie konstruiert haben.

## Die Ergebnis-Sektion
Hier zeigen Sie der Prüfungskommission, was Ihr Modell konkret leistet. Vier Bestandteile:
### 4.3.1 Modell-Performance
In den passenden Metriken (siehe Lektion 4). Beispiel:
> „Auf dem Test-Set (n = 2.000, stratifiziert) erreicht der Random-Forest-Klassifikator mit class_weight='balanced' eine ROC-AUC von 0,72 und einen Recall auf der Churn-Klasse von 0,43. Bei einem Schwellwert von 0,5 liegt die Precision der Churn-Klasse bei 0,34. Die Wahl der Hauptmetrik (Recall) folgt der geschäftlichen Priorität, möglichst viele tatsächliche Kündigungen früh zu erkennen — Fehlalarme sind weniger kostspielig als verpasste Churn-Fälle."

### 4.3.2 Baseline-Vergleich
Wo wären Sie ohne Ihr Modell? Beispiel:
> „Die Mehrheitsklassen-Baseline (immer „kein Churn" vorhersagen) erreicht eine Accuracy von 0,83 — bei einer Recall der Churn-Klasse von 0,00. Unser Modell liegt mit 0,72 ROC-AUC deutlich über dieser Baseline und liefert vor allem die operativ wichtige Recall."

### 4.3.3 Feature Importance
Top-Treiber, mit Plausibilitäts-Check und ggf. Caveat:
> „Die drei wichtigsten Features (permutationsbasiert) sind Zufriedenheit, Überstunden und Betriebszugehörigkeit. Diese Reihenfolge ist geschäftlich plausibel: niedrige Zufriedenheit ist ein direkter Frühindikator. Auffällig ist, dass gehalt_brutto in der impurity-basierten Importance auf Platz 2 erscheint, jedoch in der permutationsbasierten Auswertung auf Platz 8 zurückfällt — Gehalt korreliert mit Position, und Position trägt das eigentliche Signal."

### 4.3.4 Visualisierungen
Beschreiben Sie das wichtigste Dashboard / die wichtigste Visualisierung und fügen Sie 1–2 Screenshots ein.

## Was Sie typisch Punkte kostet
- Ergebnisse ohne Workflow. Sie zeigen Metriken, aber nicht, wie Sie dahin gekommen sind.
- Workflow ohne Entscheidungen. Sie listen Schritte, aber nicht warum Sie sie so gemacht haben.
- Accuracy bei imbalanced classes als Hauptmetrik.
- Keine Baseline. Ein Wert ist erst aussagekräftig im Vergleich zu einer Alternative.
- Feature Importance ohne Caveat bei Random Forest mit kontinuierlichen Variablen.
- Datenmodell-Sektion fehlt oder wird durch eine Spaltenliste ersetzt, ohne Bedeutung zu erklären.

## Was die Prüfungskommission im Fachgespräch fragt
- „Bitte führen Sie mich in 90 Sekunden durch Ihren Workflow — von der Rohdatei bis zum Modell-Output."
- „Welche Datenqualitätsprobleme haben Sie gefunden, und wie haben Sie sie behandelt?"
- „Warum diese Train/Test-Aufteilung?"
- „Welches Merkmal trägt im Modell den größten Beitrag — und ist das geschäftlich plausibel?"
- „Hätten Sie mehr Zeit gehabt — welche eine Verbesserung am Modell hätte den größten Effekt?"
Diese Fragen sind direkt aus Kapitel 4 ableitbar. Wenn Ihr Bericht solide ist, fallen Ihnen die Antworten leicht.

## Summary
Kapitel 4 ist 20 Punkte wert und dokumentiert in sieben Workflow-Schritten, wie Sie zu Ihren Ergebnissen gekommen sind. Plus: die bereinigte analytische Tabelle als „Datenmodell", die Ergebnisse mit Baseline-Vergleich und Plausibilitäts-Check der Feature Importance, und eine ehrliche Bewertung der Modellqualität. 
Wenn eine Kollegin mit Ihrem Bericht den Workflow nachbauen könnte und Ihre Wahl der Metrik versteht, haben Sie das Kapitel erfüllt. In der nächsten Lektion: wie Sie diesen Inhalt auf Deutsch und in IHK-Formatierung in den Bericht bringen.