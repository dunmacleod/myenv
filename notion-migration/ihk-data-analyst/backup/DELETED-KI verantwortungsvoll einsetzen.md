# KI verantwortungsvoll einsetzen

https://app.notion.com/p/KI-verantwortungsvoll-einsetzen-38b9418319f380beb778d132d941ba3b

Bevor wir in das eigentliche Thema einsteigen, eine kurze Vorbemerkung zu den Beispielen, die Ihnen in dieser und in den folgenden Lektionen immer wieder begegnen werden.
> 📌 Das laufende Beispiel — NordWind Shop GmbH
  Durch alle Lektionen dieser Reihe begleitet uns ein gemeinsames Beispielunternehmen: die NordWind Shop GmbH, ein fiktiver Hamburger Online-Händler mit rund 80 000 Kund:innen und einem schleichenden Kündigungsproblem. Vier Stakeholder tauchen immer wieder auf: Lara Hoffmann aus dem Marketing wünscht sich ein Frühwarnsystem für gefährdete Kund:innen; Tobias Berg aus dem Customer Success möchte wissen, wen er zuerst anrufen soll; Sven Klein aus der IT entscheidet, wie das Modell technisch integriert wird; Anna Maier, Junior-Analystin, wurde gebeten, einen Prototyp zu bauen.
  NordWind ist ein Lehrbeispiel, nicht Ihr Projekt. Sie und Ihre Gruppe arbeiten an einem von sechs anderen Datensätzen — mit einer anderen Organisation, einem anderen Problem, einer anderen Metrik. Wenn Sie in einer Lektion ein NordWind-Beispiel sehen, behandeln Sie es als Muster: „So sieht dieser Schritt aus, angewendet auf eine konkrete Organisation" — und übertragen Sie es auf das Unternehmen hinter Ihrem eigenen Datensatz.
  Wir verwenden ein durchgängiges Beispiel, weil konkrete Fälle leichter zu verstehen sind als abstrakte Regeln. Der Übersetzungsschritt auf Ihren eigenen Geschäftsfall gehört zu Ihrer Aufgabe.
Nun zum eigentlichen Thema. Stellen Sie sich drei Analyst:innen im NordWind-Team vor. Die erste lässt einen Absatz im Bericht von ChatGPT formulieren, weil ihr formelles Schriftdeutsch schwerfällt. Die zweite lässt sich von Copilot eine Pandas-Funktion erklären, die sie nicht kannte. Die dritte fragt ChatGPT nach einer alternativen Erklärung des Random-Forest-Algorithmus, weil das Lehrbuch zu trocken war. Alle drei haben KI genutzt — und alle drei haben es richtig gemacht.
Ein anderer Fall: eine Person übernimmt einen kompletten Analyse-Absatz mit konkreten Zahlen aus ChatGPT, ohne die Zahlen auf den eigenen Daten verifizieren zu können. Im Fachgespräch fragt die Kommission, woher die Zahlen kommen — und die Antwort fehlt. Das ist nicht KI-Nutzung. Das ist eine Verständnis-Lücke, die KI versteckt hat.

## Lernergebnisse
Nach dieser Lektion können Sie:
- akzeptable KI-Anwendungen (Sprach-Politur, Strukturierung, Syntax-Hilfe, Recherche-Einstieg) von nicht akzeptablen (KI-generierte Analyse-Aussagen, Zahlen oder Interpretationen, die Sie nicht verteidigen können) unterscheiden,
- die fünf pragmatischen Regeln für KI-Einsatz im Projekt anwenden (Verifizieren statt Vertrauen; konventionelle Quellen; KI für Sprache, Sie für Inhalt; KI-Nutzung im Sprint-Log notieren; ohne KI für das Fachgespräch üben).
## Die Grundregel
![image]((notion-hosted file))
Akzeptabel vs. nicht akzeptabel beim KI-Einsatz

> Sie dürfen KI nutzen, sofern Sie alles, was im Bericht steht, selbst erklären können.
Die IHK prüft Ihr Verständnis, nicht den Weg, auf dem Sie es erworben haben. Der Punkt, an dem KI problematisch wird, ist nicht „KI hat einen Satz geschrieben", sondern „KI hat eine Behauptung produziert, die ich nicht verifizieren konnte".

## Was akzeptabel ist
[TABLE]
  | Anwendung | Beispiel | Warum akzeptabel |
  | Sprach- und Stil-Polish | „Bitte vereinfache diesen Absatz auf einen klaren Wirtschaftston." | Sie haben den Inhalt; KI hilft bei der Form. |
  | Strukturierung | „Wie würde man dieses Kapitel typischerweise gliedern?" | Sie behalten die Inhalts-Hoheit. |
  | Syntax-Hilfe | „Wie ist die korrekte Pandas-Syntax für eine Median-Imputation pro Gruppe?" | KI ersetzt das Lehrbuch, Sie verstehen den Code. |
  | Recherche-Einstieg | „Welche Evaluation-Metriken sind bei imbalanced classes üblich, und welche Nachteile haben sie?" | KI gibt einen Überblick; Sie validieren ihn an Ihren Daten. |
  | Beispiele und Übungen | „Gib mir drei Beispiele, wie Salary mit Position interagieren könnte." | KI hilft beim Denkprozess. |
  | Übersetzung schwieriger Begriffe | „Wie sagt man „class imbalance" auf Deutsch?" | Sprachliche Stütze. |
  | Erklären-Lassen unbekannter Konzepte | „Erkläre mir Permutationsbasierte Feature Importance in zwei Sätzen." | Lernhilfe. |

## Was nicht akzeptabel ist
[TABLE]
  | Anwendung | Beispiel | Warum problematisch |
  | Konkrete Analyse-Aussagen aus KI übernehmen | „Welche Features sind bei NordWind die Treiber?" → Antwort 1:1 in den Bericht | Sie können die Behauptung nicht verifizieren — sie ist nicht aus Ihrer Analyse. |
  | Zahlen aus KI in den Bericht schreiben | „Welcher Recall ist bei Churn-Modellen üblich?" → 0,72 in den Bericht | Die Zahl ist nicht Ihre — Sie können sie im Fachgespräch nicht verteidigen. |
  | Vollständige Kapitel generieren lassen | „Schreibe mir Kapitel 4 für dieses Projekt." | Kein eigenes Verständnis. Stilistisch oft erkennbar. |
  | Code 1:1 ohne Verständnis verwenden | KI generiert eine ML-Pipeline, Sie führen sie aus, ohne zu wissen, was sie tut. | Im Fachgespräch nicht verteidigbar. |
  | Ergebnis-Interpretationen erfinden lassen | „Was bedeutet ROC-AUC = 0,72 in diesem Kontext?" → Antwort direkt übernommen | Die Interpretation hängt am Geschäftskontext, den Sie kennen — nicht KI. |
  | KI als Quelle zitieren | „Laut ChatGPT…" | KI ist keine zitierfähige Quelle. |

## Wie die Prüfungskommission das testet
Die Kommission stellt im Fachgespräch keine direkten Fragen wie „Haben Sie KI verwendet?". Sie stellt Fragen, die genauere Antworten verlangen, als KI-generierter Text typischerweise liefert. Beispiele:
- „Warum haben Sie genau diesen Schwellwert gewählt?" (KI-Text nennt meist einen typischen, nicht den, den Sie selbst hergeleitet haben.)
- „Wie verändert sich das Ergebnis, wenn Sie X weglassen?" (KI hat Ihre konkreten Daten nicht — kann das nicht beantworten.)
- „Bitte führen Sie mich durch Ihren Workflow." (KI kann den Workflow beschreiben — aber nicht den, den Sie gebaut haben, mit den Eigenheiten Ihres Datensatzes.)
- „Warum verwendet das Modell bewertungen_durchschnitt nicht so stark, wie Sie es erwartet hätten?" (Erfordert ehrliches Selbst-Beobachten Ihrer Analyse.)
Wenn die Antworten zu generisch klingen, geht die Kommission tiefer. Die Antwort „Das hat ChatGPT geschrieben, ich erkläre Ihnen das, wenn Sie mir den Code zeigen" ist ein sofortiges rotes Signal.

## Pragmatische Regeln für den Projekt-Alltag
### Regel 1 — Verifizieren statt vertrauen
Wenn KI Ihnen eine Zahl oder eine Behauptung liefert, prüfen Sie sie auf Ihren Daten bevor sie in den Bericht geht. Beispiel:
KI: „Bei imbalanced classes ist Recall = 0,4 ein gutes Ergebnis."
Sie: Schauen Sie auf Ihre eigenen Test-Daten. Was zeigt Ihr Confusion-Matrix? Verifizieren Sie auf Ihrer eigenen Stichprobe, bevor Sie eine Aussage über Ihren konkreten Datensatz machen.

### Regel 2 — Quellen für KI-Aussagen, die Sie nicht prüfen können
Wenn KI Ihnen einen Konzept-Hinweis liefert, den Sie nicht direkt auf Ihren Daten testen können (z. B. „Class-weight = balanced ist eine gängige Strategie"), suchen Sie eine konventionelle Quelle (Lehrbuch, Dokumentation, Fachartikel) und zitieren Sie diese im Bericht — nicht die KI.

### Regel 3 — KI für Sprache, Sie für Inhalte
Eine pragmatische Aufgabenteilung:
[TABLE]
  | KI macht gut | Sie machen besser |
  | Stilistische Verbesserung | Inhaltliche Entscheidungen |
  | Sprachliche Formulierung | Wahl der Methode |
  | Strukturvorschläge | Interpretation der Ergebnisse |
  | Syntax-Hilfe | Geschäftskontext |
  | Erste Recherche-Schritte | Validierung an konkreten Daten |

### Regel 4 — Wenn Sie KI verwenden, dokumentieren Sie es
Nicht in den Bericht — aber in Ihrem Sprint-Log in der Notizen-Spalte. Beispiel: „Den Einleitungssatz haben wir mit ChatGPT formuliert, inhaltlich basiert er auf der Datenqualitätstabelle aus Sprint 1."
Falls die Kommission fragt, können Sie ehrlich antworten: „Ja, den Stil haben wir mit KI gepolisht. Die Inhalte sind aus unserer EDA, hier zum Beispiel ist die zugrunde liegende Tabelle aus Sprint-Log Tag 5."

### Regel 5 — Üben Sie ohne KI für das Fachgespräch
Bei Übungssituationen und im echten Fachgespräch müssen Sie ohne KI-Hilfe antworten. Bereiten Sie sich so vor, dass Sie ohne externe Hilfe Ihre Sektionen erklären können.

## Das Verständnis-Kriterium
In der Finalisierungs-Woche prüfen Sie Ihr Verständnis selbst oder in der Gruppe mit Fragen wie:
- „Erklären Sie den Workflow."
- „Begründen Sie diese Entscheidung."
- „Was würden Sie heute anders machen?"
Wenn die Antworten nicht aus Ihrem eigenen Verständnis kommen, fällt das in den drei Gruppen-Check-ins oder am Projektstand auf. Tutor:innen können auf dieser Grundlage ein Nicht-bereit feststellen und dies an Masterschool kommunizieren. Das ist ein bewusst eingebauter Schutzmechanismus, der Sie und die IHK-Beziehung der MSIT schützt.

## Wie Sie eine produktive KI-Routine aufbauen
Eine Empfehlung, die in vielen Kohorten funktioniert hat:
1. Inhalt zuerst. Bauen Sie Ihren Workflow, machen Sie Ihre Analyse, schreiben Sie eine erste Skizze des Kapitels in eigenen Worten — auch wenn der Stil noch ruppig ist.
1. Dann KI für Politur. Wenn der Inhalt steht, lassen Sie KI bei Sprache und Struktur helfen.
1. Lesen Sie das Ergebnis laut. Klingt es nach Ihnen? Wenn nein: anpassen, bis es nach Ihnen klingt.
1. Üben Sie das Erklären ohne den Text vor sich. Was Sie nicht ohne Text erklären können, gehört nicht in den Bericht.

## Die häufigsten Fehler — und wie man sie vermeidet
[TABLE]
  | Fehler | Korrektur |
  | KI-generierte Behauptung ohne Datenbezug im Bericht | Behauptung an Ihrer EDA verifizieren oder weglassen |
  | Stil ist plötzlich auffällig „akademisch" und passt nicht zum restlichen Bericht | KI-Output in eigenen Worten paraphrasieren |
  | Ein konkretes Detail (Zahl, Studie, Statistik) klingt zu rund | Auf Quelle prüfen — KI erfindet manchmal Zahlen |
  | Sie können einen eigenen Absatz nicht ohne Folie erklären | Absatz umschreiben, bis Sie ihn frei erklären können |

## Zusammenfassung
KI ist im IHK-Projekt ein erlaubtes und produktives Werkzeug — solange Sie alles, was im Bericht steht, selbst verstehen und im Fachgespräch verteidigen können. Akzeptabel sind Sprach-Polish, Strukturhilfe, Syntax-Lookup, Konzept-Erklärungen und Recherche-Einstieg. Nicht akzeptabel sind konkrete Analyse-Aussagen, Zahlen oder Interpretationen, die nicht aus Ihren eigenen Daten kommen. 
Die Prüfungskommission testet das nicht direkt, sondern durch Fragen, die nur aus Ihrem konkreten Datensatz beantwortet werden können. Schreiben Sie Inhalt zuerst in eigenen Worten, lassen Sie KI dann polishen, und üben Sie das Erklären ohne Stütze. In der nächsten Lektion sprechen wir darüber, wie Sie die Arbeit in Ihrer Dreier-Gruppe so aufteilen, dass die IHK-Pflicht der individuellen Sichtbarkeit erfüllt ist.