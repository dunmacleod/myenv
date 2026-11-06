# Sprint-Log Template — Datenbank-Schema

https://app.notion.com/p/Sprint-Log-Template-Datenbank-Schema-38b9418319f380e1a307ce0dae863bfa

Empfohlene Spalten (Property-Namen und -Typen). Die Bezeichnungen können Sie an Ihre Spracheinstellung anpassen; entscheidend sind die Typen.
[TABLE]
  | Spalte | Typ | Beschreibung |
  | Sprint | Auswahl (Select) | Sprint 1, Sprint 2, Sprint 3, Finalisierung |
  | User Story | Text (oder Relation zu einer User-Story-DB) | Die zugehörige User Story, z. B. „Als Vertriebsleiterin möchte ich…" |
  | Aufgabe | Titel (Title) | Kurze, handlungsorientierte Aufgabenbeschreibung |
  | Verantwortlich | Person | Eine Person pro Aufgabe |
  | Status | Auswahl | Zu erledigen, In Bearbeitung, Erledigt, Blockiert, Verschoben |
  | Definition of Done | Text | Was bedeutet „erledigt" für genau diese Aufgabe — üblicherweise ein Satz |
  | Blocker | Text | Wird nur gefüllt, wenn Status = Blockiert |
  | Entscheidung | Text | Während der Aufgabe getroffene Entscheidungen (eine Zeile) |
  | Anpassungen | Text | Planänderungen während des Sprints |
  | Sprint-Tag | Datum | Tag, an dem die Aufgabe in den Sprint kam |
  | Erledigt-Tag | Datum | Tag, an dem die Aufgabe abgeschlossen wurde |
  | Notizen | Text | Freie Notizen |

## Empfohlene Ansichten
[TABLE]
  | Name der Ansicht | Filter | Sortierung | Zweck |
  | Heute | Status = In Bearbeitung und Verantwortlich = ich | nach Aufgabe | Tagesfokus |
  | Sprint-Board | nach Sprint | gruppiert nach Status | Sprint-Planung und Standup |
  | Erledigt | Status = Erledigt | nach Erledigt-Tag absteigend | Sprint-Review und Rohmaterial für Kapitel 3 |
  | Blocker | Status = Blockiert | nach Sprint-Tag absteigend | Was muss entblockt werden |
  | Retro | nach Sprint | nach gefülltem Anpassungen | Sprint-Retrospektive |

## User Stories (optionale Unter-Datenbank)
Wenn Sie eine separate Datenbank für User Stories anlegen möchten:
[TABLE]
  | Spalte | Typ |
  | Story | Titel — „Als <Rolle> möchte ich <Ziel>, damit <Nutzen>" |
  | Stakeholder | Auswahl |
  | Priorität | Auswahl — Hoch / Mittel / Niedrig |
  | Sprint | Relation zum Sprint-Log |
  | Status | Auswahl — Backlog / Aktiv / Abgeschlossen |
Für die meisten Gruppen reicht eine einzelne Sprint-Log-Datenbank. User Stories können im Textfeld User Story direkt an der jeweiligen Aufgabe stehen.

## Beispiele zum Ausfüllen (gut vs. schlecht)
Gute Aufgabe: Datenqualitätsprüfung auf mitarbeiter.csv durchführen
Schlechte Aufgabe: Daten anschauen (zu vage — wer macht konkret was?)

Gute Definition of Done: Tabelle mit allen 7 Datenqualitäts-Issues erstellt und in Kapitel 1 verlinkt
Schlechte Definition of Done: Daten sind sauber (Erfolgskriterium ist nicht messbar)

Gute Entscheidung: Wir verwenden Median-Imputation für fehlende Werte in zufriedenheit, weil die Verteilung schief ist und Mean das Ergebnis verzerren würde.
Schlechte Entscheidung: Median ist besser (keine Begründung — Kapitel 3 braucht das Warum)