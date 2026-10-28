# Memory- und State-Fehlermodi

Notion page: https://app.notion.com/p/Memory-und-State-Fehlermodi-0969418319f382589a2981e6d6b3c973
Backed up before n8n migration

An diesem Punkt hat die Vela-Systems-Canvas eine definierte Memory-Architektur: Grenzen zwischen geteiltem und privatem State, Schreib-Ownership pro Schlüssel, einen Recovery-Pfad nach Unterbrechungen und vier Log-Positionen, die einen Trace über die vollständige Ausführungskette erzeugen. Die Architektur ist auf dem Papier solide. Noch nicht getestet sind die spezifischen Arten, wie Memory und State in Produktion typischerweise scheitern. Die Architektur war im Design nicht falsch. Grenzfälle in echter Nutzung machen einfach Lücken sichtbar, die kontrolliertes Testing nicht aufdeckt.
Das Vela-Team bereitet sich darauf vor, das System an dreißig Nutzer zu übergeben. Bevor das passiert, müssen sie eine Reihe von Szenarien durcharbeiten, die die realistische Fehleroberfläche eines Multi-Agent-Systems wie ihres abbilden: Fälle, in denen Memory einen Agenten dazu bringt, irrelevante oder veraltete Ausgabe zurückzugeben, Fälle, in denen State falsches Routing oder stille Duplikation verursacht, und Fälle, in denen die Kombination aus beidem einen Fehler erzeugt, den keines von beiden allein verursacht hätte. Deine Aufgabe in dieser Lektion ist es, diese Szenarien auf der Vela-Canvas durchzuarbeiten und für jedes eine Schutzmaßnahme zu entwerfen.
> 💡 In dieser Lektion identifizierst du Fälle, in denen Memory oder State irrelevantes, veraltetes oder unsicheres Agentenverhalten verursacht, und entwirfst für jeden Fall eine konkrete Schutzmaßnahme.
## Was diese Übung aufbaut
Das Erkennen potenzieller Fehlerquellen ist eine Kernaufgabe des Designs, nicht des Debuggings. Beim Debugging sucht man nach Fehlern, die bereits aufgetreten sind. Ein gutes Design hingegen nimmt diese vorweg und strukturiert das System so, dass die Auswirkungen im Fehlerfall von vornherein minimiert werden.
Die Fehlermodi in dieser Lektion sind keine hypothetischen Grenzfälle, die für die Übung erfunden wurden. Es sind die Kategorien von Memory- und State-Fehlern, die in produktiven Multi-Agent-Systemen wiederholt auftreten. Die Vela-Canvas ist der Kontext, den du gut kennst. Nutze sie, um deine Analyse zu verankern. Aber die Muster, die du hier identifizierst, gelten für jedes Multi-Agent-System, einschließlich deines eigenen Projekts.
Drei Kategorien strukturieren die Übung:
![image]((notion-hosted file))

## Mit Dokumentation arbeiten
Bevor du mit der Szenarioanalyse startest, solltest du dich in der Dokumentation zu Flowise Agentflow V2 mit zwei zentralen Mechanismen vertraut machen. Zum einen mit dem Flow State , also dem gemeinsamen Key-Value-Store, auf den knotenübergreifend schreibend und lesend zugegriffen wird. Zum anderen mit der Konfiguration von Update Flow State innerhalb der Agent-Nodes. Denn unklare Definitionen darüber, was exakt wann geschrieben und von wem gelesen wird, sind der eigentliche Auslöser für alle drei der oben beschriebenen Fehlerkategorien.
[TABLE]
  | Mechanismus | Was er tut | Wo du nachschauen solltest |
  | Flow State | Geteilter Key-Value-Store, der allen Nodes in der Canvas für die Dauer eines Flow-Runs zur Verfügung steht | Flowise-Dokumentation → Agentflow V2 → Flow State |
  | Update Flow State (Agent Node) | Konfiguration, die Key-Value-Paare aus der Ausgabe des Agenten in Flow State schreibt, nachdem der Node abgeschlossen ist | Flowise-Dokumentation → Agentflow V2 → Agent Node → Update Flow State |
  | Kontextfenster | Die Konversationshistorie, die für einen einzelnen Agent-Node innerhalb seiner eigenen Ausführung sichtbar ist, nicht über Nodes hinweg geteilt | Flowise-Dokumentation → Agentflow V2 → Memory |
  | Session-Scope | Die Grenze, innerhalb der Flow-State-Schlüssel persistieren — endet, wenn die Session endet | Flowise-Dokumentation → Agentflow V2 → Sessions |
Die Referenz oben ist keine Checkliste zum Kopieren. Sie ist ein Hinweis auf die Dokumentation, die du offen haben solltest, während du jedes Szenario durcharbeitest. Die Analyse in jedem Szenario verlangt, dass du darüber nachdenkst, welcher Mechanismus beteiligt ist, nicht nur, was das Symptom ist.
## Deine Aufgabe
> 🔥 Bevor du beginnst, erstelle eine Kopie von dieser Vorlage. Sie spiegelt die Struktur dieser Lektion wider: ein Tab pro Szenario, mit Kontext, Kategorie, Mechanismus, Leitfragen und einem Feld für die Schutzmaßnahme, plus ein kurzes Checkpoint-Sheet.
Arbeite die fünf Szenarien unten durch. Für jedes Szenario:
1. Identifiziere die Fehlerkategorie (Stale Memory, State Contamination oder Unsafe Persistence).
1. Beschreibe, was der Vela-Nutzer erleben würde, wie die Ausgabe aussieht und warum sie falsch ist.
1. Identifiziere den konkreten Mechanismus auf der Vela-Canvas, der den Fehler ermöglicht.
1. Entwirf eine konkrete Schutzmaßnahme, eine spezifische Änderung an der Canvas-Konfiguration, an der Memory-Architektur oder am Schreibverhalten des Agenten, die den Fehler verhindert oder eindämmt.
Schreibe deine Schutzmaßnahme als konkrete Designentscheidung: nicht „eine Prüfung hinzufügen", sondern „der Classifier-Node setzt query_type auf null zurück, bevor er einen neuen Wert schreibt, sodass ein fehlgeschlagener Schreibvorgang immer ein erkennbares null statt einer veralteten Klassifizierung erzeugt."
Ziel ist eine Reihe von fünf Schutzmaßnahmen-Entscheidungen, die du direkt in deine Integrationsarbeit in der nächsten Lektion übernehmen kannst.
### Szenario 1: Der Classifier setzt query_type zwischen Anfragen in derselben Session nicht zurück
Ein Vela-Nutzer sendet zwei Anfragen in derselben Session. Die erste ist eine Account-Anfrage, die der Classifier korrekt als account klassifiziert. Der Classifier schreibt query_type: "account" in Flow State und routet zu Specialist B. Der Spezialist gibt eine korrekte Antwort zurück.
Derselbe Nutzer sendet unmittelbar danach eine zweite Anfrage: „Any open support tickets for that client?" Das ist eine Supportanfrage. Die korrekte Klassifizierung ist support, was zu Specialist A routen sollte.
Aber das LLM des Classifier erzeugt bei der Verarbeitung einer kurzen Folgefrage in einer schnellen Session einen fehlerhaften Output. Der Update-Flow-State-Schritt wird für die zweite Anfrage nicht korrekt ausgeführt. query_type in Flow State enthält weiterhin "account" aus der ersten Anfrage.
Der Condition Node liest query_type: "account" und routet erneut zu Specialist B. Specialist B bearbeitet Account-Anfragen. Er gibt Account-Informationen für denselben Kunden zurück, nicht die Support-Ticket-Historie, nach der der Nutzer gefragt hatte.
Fragen zur Orientierung deiner Analyse:
- Welcher Flow-State-Schlüssel steht im Zentrum dieses Fehlers?
- An welchem Punkt in der Ausführungssequenz sollte der Schlüssel zurückgesetzt werden?
- Auf welchen Wert sollte er zurückgesetzt werden, und welcher Node ist für diesen Reset verantwortlich?
- Wie hilft dir das Log an Position 1 (aus der vorherigen Lektion), diesen Fehler nachträglich zu erkennen?
### Szenario 2: Ein Spezialagent schreibt eine Zusammenfassung in Flow State, die von der nächsten Anfrage gelesen wird
Die Vela-Canvas ist so konfiguriert, dass Specialist B nach jeder von ihm bearbeiteten Anfrage eine kurze Account-Zusammenfassung in einen Flow-State-Schlüssel namens last_account_summary schreibt. Das wurde aus Bequemlichkeit hinzugefügt. Die Idee war, dass die Zusammenfassung vom finalen Reply-Node referenziert werden könnte, um denselben Inhalt nicht erneut zusammenzufassen.
Ein Nutzer sendet eine Anfrage zu Client A. Specialist B läuft und schreibt last_account_summary: "Client A — renewal due Q3, no open tickets" in Flow State.
Derselbe Nutzer sendet später in derselben Session eine Anfrage zu Client B. Client B ist ein völlig anderer Account. Der Classifier klassifiziert dies korrekt als Account-Anfrage und routet zu Specialist B. Specialist B läuft und erzeugt eine Antwort zu Client B. Aber der finale Reply-Node liest last_account_summary aus Flow State und dieser Schlüssel enthält weiterhin die Zusammenfassung zu Client A von früher in der Session.
Die Antwort auf die Anfrage zu Client B enthält einen eingebetteten Hinweis auf das Verlängerungsdatum von Client A.
Fragen zur Orientierung deiner Analyse:
- Ist das ein Stale-Memory-Fehler, ein State-Contamination-Fehler oder beides?
- Was ist das Write-Ownership-Problem im ursprünglichen Design?
- Wie sollte last_account_summary gescoped werden, um Cross-Query-Contamination innerhalb einer Session zu verhindern?
- Wenn du dich entscheidest, den Schlüssel beizubehalten, welche Reset-Regel würde ihn sicher machen?
### Szenario 3: Ein persistenter Memory Store wird mit session-spezifischem Inhalt beschrieben
Das Vela-Team hat der Canvas eine Qdrant-Collection hinzugefügt, um Customer-Account-Notes zu speichern. Eine persistente Memory, die Agenten über Sessions hinweg abfragen können. Während einer Supportanfrage tippt ein Vela-Nutzer Folgendes: „The client mentioned in our last call that they are considering cancellation. Route this to the account team."
Der Support-Spezialist-Agent schreibt gemäß seinem System-Prompt die vollständige Eingabe des Nutzers als Notiz, die mit dem Kundenaccount verknüpft ist, in die Qdrant-Collection. Die Notiz persistiert über Sessions hinweg.
Drei Tage später bearbeitet ein anderer Vela-Nutzer denselben Kundenaccount. Er führt eine Account-Anfrage aus. Specialist B ruft die gespeicherten Notizen aus Qdrant ab. Die abgerufene Notiz enthält die wortgetreue Eingabe des ersten Nutzers (einschließlich der Phrase „considering cancellation"), die vor drei Tagen korrekt war, inzwischen aber gelöst wurde. Die Antwort des zweiten Nutzers an den Kunden wird durch einen veralteten und nun falschen Status beeinflusst.
Fragen zur Orientierung deiner Analyse:
- Zu welcher Kategorie gehört dieser Fehler, und was macht ihn ernster als eine Contamination innerhalb der Session?
- Welche Eigenschaft persistenter Memory macht diesen Fehler möglich, selbst wenn die Session-Architektur korrekt ist?
- Was sollte die Schreibregel für die Qdrant-Collection über den Inhalt von Notizen festlegen, insbesondere darüber, was nicht geschrieben werden darf?
- Welcher Ablauf- oder Invalidation-Mechanismus würde das Risiko veralteter persistenter Notizen reduzieren?
### Szenario 4: Zwei gleichzeitige Sessions schreiben in denselben Flow-State-Schlüssel
Zwei Vela-Nutzer führen gleichzeitig Anfragen aus. User A sendet eine Account-Anfrage. Der Classifier schreibt query_type: "account" in Flow State. Fast im selben Moment sendet User B eine Supportanfrage. Der Classifier für die Session von User B schreibt query_type: "support" in Flow State.
Beide Sessions schreiben in einen Flow-State-Schlüssel, der nicht nach Session-ID namespaced ist. Es gibt nur einen query_type-Schlüssel auf der Canvas, geteilt über alle Sessions hinweg.
Der Condition Node von User A liest query_type und erhält "support", den Wert, den die Session von User B geschrieben hat. User A wird zu Specialist A statt zu Specialist B geroutet. Specialist A bearbeitet eine Supportanfrage im Namen des Account-Kontexts von User A. Die Antwort ist falsch für die ursprüngliche Frage von User A.
Fragen zur Orientierung deiner Analyse:
- Welcher konkrete Mechanismus erlaubt es dem Schreibvorgang von User B, den Wert von User A zu überschreiben?
- Wie verhindert Session-Namespacing eines Flow-State-Schlüssels diesen Fehler?
- Schreibe das Namespaced-Key-Pattern auf, das du für query_type auf der Vela-Canvas verwenden würdest, und identifiziere, welcher Node es schreibt und welcher Node es liest.
- Kann dieser Fehler aus dem Log an Position 1 erkannt werden? Wonach würdest du suchen?
### Szenario 5: Ein Recovery-Pfad stellt State auf den falschen sicheren State zurück
Die Vela-Canvas hat einen Recovery-Pfad: Wenn ein Spezialagent scheitert, nachdem der Classifier bereits query_type in Flow State geschrieben hat, recovered das System, indem es query_type auf null zurücksetzt und zurück zum Classifier routet.
Während einer Session scheitert Specialist C mitten in der Ausführung. Der Recovery-Pfad wird aktiviert. Er setzt query_type auf null zurück, soweit korrekt. Aber er liest auch last_routed_agent aus Flow State (einen Schlüssel, der aufzeichnet, welcher Spezialist zuletzt lief) und schreibt diesen Wert als Diagnosemeldung in die Antwort: „Routing to support agent was interrupted. Please re-send your query."
Das Problem: last_routed_agent enthält den Wert "specialist_c" aus der aktuellen Session, korrekt. Aber die Diagnosemeldung sagt „support agent", also Specialist A, nicht Specialist C (der Eskalationsanfragen bearbeitet). Das Label war im Reply-Template hardcodiert und passt nicht zum tatsächlichen Wert in last_routed_agent.
Ein zweites Problem: last_routed_agent wird nach dem Recovery-Pfad nicht zurückgesetzt. Eine nachfolgende Anfrage in derselben Session liest last_routed_agent: "specialist_c", obwohl die neue Anfrage noch nicht klassifiziert und geroutet wurde. Wenn irgendetwas in der Canvas last_routed_agent als Eingabe für eine Entscheidung liest, liest es einen veralteten Wert.
Fragen zur Orientierung deiner Analyse:
- Dieses Szenario umfasst zwei separate fehlgeschlagene Schutzmaßnahmen. Benenne beide klar.
- Für den ersten Fehler: Was ist die korrekte Designregel für nutzerseitige Diagnosemeldungen, die Flow-State-Werte referenzieren?
- Für den zweiten Fehler: An welchem Punkt in der Recovery-Sequenz sollte last_routed_agent zurückgesetzt werden, und auf welchen Wert?
- Wie interagiert ein Completion-Signal (ein statusSchlüssel) mit last_routed_agent, um diesen Fehler besser erkennbar zu machen?
## Hinweise
[toggle] Nutze diese, wenn du sie brauchst.
  - Wenn ein Flow-State-Schlüssel von mehr als einem Node gelesen und nur von einem geschrieben wird, ist der Fehler wahrscheinlich ein Timing- oder Reset-Problem; frage, wann der Schreibvorgang relativ zum Lesevorgang passiert.
  - Wenn ein Schlüssel Informationen aus einer früheren Anfrage in eine neue Anfrage trägt, ist der Fix fast immer ein Reset bei Session-Start oder Query-Start; nicht eine Änderung daran, wer ihn liest.
  - Wenn ein Schlüssel in einen persistenten Store geschrieben wird, frage, ob der Inhalt session-spezifisch oder account-level ist; nur account-level, zeitstabiler Inhalt gehört in einen persistenten Store.
  - Wenn zwei Sessions denselben Schlüsselnamen teilen, ist der Fix Namespacing nach Session-ID; der Schlüsselname wird zu query_type:{session_id} statt einem einzelnen globalen query_type.
  - Wenn eine Recovery-Nachricht einen Flow-State-Wert referenziert, muss der Nachrichtentext zur Laufzeit aus dem tatsächlichen Schlüsselwert abgeleitet werden, nicht im Template hardcodiert sein.

>  
  ### 🔥 AI nutzen, wenn du feststeckst
  Wenn du ein Szenario durcharbeitest und den konkreten Mechanismus, der den Fehler verursacht, nicht identifizieren kannst, ist ein sinnvoller Workflow:
  1. Benenne zuerst das Symptom in einfacher Sprache: „Der Nutzer erhielt die Antwort des falschen Spezialisten."
  1. Verfolge einen Schritt zurück: „Was hat der Condition Node gelesen, um diese Routing-Entscheidung zu treffen?"
  1. Frage, wo dieser Wert geschrieben wurde und wann.
  1. Bitte dann AI, deine Diagnose zu bestätigen: „In Flowise Agentflow V2, if a Flow State key is written by the Classifier and then read by a Condition Node, what happens to that key value if the Classifier's Update Flow State step fails to execute? Does the Condition Node read the previous value or null?"
  Nutze AI, um den Mechanismus zu klären, nicht um die Diagnose für dich zu erledigen. Die Schutzmaßnahme, die du entwirfst, muss in deinem eigenen Reasoning über die Canvas verankert sein. Eine AI-generierte Schutzmaßnahme, die du nicht verstehst, wird in deiner Projektverteidigung nicht standhalten.

## Checkpoints
Prüfe deine Schutzmaßnahme bei jedem Szenario anhand dieser Fragen:
- [ ] Ist die Schutzmaßnahme eine konkrete Designentscheidung (mit einem spezifischen Node, Schlüssel, Wert oder einer Konfiguration), oder ist sie noch ein allgemeines Prinzip? Ein allgemeines Prinzip ist keine Schutzmaßnahme.
- [ ] Verhindert die Schutzmaßnahme den Fehler, begrenzt sie den Schaden oder macht sie den Fehler erkennbar? Benenne, was sie tut. Eine einzelne Schutzmaßnahme muss nicht alle drei leisten.
- [ ] Führt die Schutzmaßnahme ein neues Risiko ein, zum Beispiel einen Reset, der zu früh feuert und einen Schlüssel löscht, den ein anderer Node noch braucht?
- [ ] Kann der Fehler über die vier Log-Positionen erkannt werden, die in der vorherigen Lektion entworfen wurden? Wenn ja, welche Position würde ihn sichtbar machen, und wonach würdest du im Log suchen?
Wenn eine Schutzmaßnahme ein neues Risiko einführt, das du nicht lösen kannst, notiere es explizit. Ein dokumentierter Tradeoff ist besser als eine Schutzmaßnahme, die ein verstecktes Problem erzeugt.
## Zusammenfassung
Fehlerquellen rechtzeitig vor der Integration vorauszusehen, macht den Unterschied zwischen einem System, das im Labor funktioniert, und einem, das der Realität standhält. Die fünf Szenarien dieser Lektion repräsentieren exakt jene Memory- und State-Fehler, die in produktiven Multi-Agent-Systemen auftreten: Stale Memory (durch falsches Reset-Timing), State Contamination (innerhalb einer Session), Unsafe Persistence (in einem Shared Store), Key Collision (bei parallelen Sessions) sowie Recovery-Pfade, die einen veralteten State laden.
Jede deiner entworfenen Schutzmaßnahmen ist eine konkrete Designentscheidung für die Vela-Analyse und bereitet die Integration deines eigenen Projekts vor. In der nächsten Lektion wendest du die Architekturentscheidungen der Sprints 1 bis 3 auf deine eigene Canvas an – und nutzt die Fehlerszenarien von heute als Maßstab, um deine Integration auf Herz und Nieren zu prüfen.
