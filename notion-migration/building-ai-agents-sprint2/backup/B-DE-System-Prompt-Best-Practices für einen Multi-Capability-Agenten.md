# System-Prompt-Best-Practices für einen Multi-Capability-Agenten

Notion page: https://app.notion.com/p/System-Prompt-Best-Practices-f-r-einen-Multi-Capability-Agenten-3789418319f3805aaabdeebd26fa7da6
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeitest: Du lernst die vier Elemente eines gut gesteuerten System-Prompts kennen. Außerdem erfährst du, warum präzise Anweisungen immer wichtiger werden, je mehr Fähigkeiten der Agent erhält.
## Wo wir stehen
Meridians Agentflow v2 hat jetzt drei Fähigkeiten, die zusammenarbeiten. Der Agent Node führt Reasoning mit Gemini aus. Der Document Store meridian-knowledge liefert fundiertes Wissen aus interner Dokumentation. Der Canvas ist überprüft und gibt präzise Retrieval-Ergebnisse zurück.
Jetzt werden wir Conditional Routing hinzufügen, also die Fähigkeit des Agenten, unterschiedliche Queries basierend auf Regeln oder AI-Reasoning über unterschiedliche Pfade zu senden. Danach wird ein HTTP Node für Live-Datenabfragen verbunden.
Bevor irgendetwas davon hinzugefügt wird, lohnt es sich, eine grundlegende Frage klar zu beantworten: Was genau soll dieser Agent tun, und wie soll er sich verhalten, wenn er an die Grenzen dieser Definition stößt?
Diese Frage braucht eine präzise Antwort, die im System-Prompt codiert ist. Der Grund ist strukturell. Sobald der Agent mehrere Fähigkeiten hat, wird sein Verhalten von allen gleichzeitig geprägt. Unerwartetes Verhalten über mehrere verbundene Komponenten hinweg zu debuggen, ist deutlich schwieriger, als die Anweisungen richtig zu setzen, solange der Build noch überschaubar ist.
## Warum Systemanweisungen Governance sind
Jeder produktionsreife Business-Agent benötigt drei Dinge, die zusammenarbeiten:
[TABLE]
  | Komponente | Was sie liefert |
  | Reasoning Engine | Intelligenz: Gemini liest, führt Reasoning aus und generiert |
  | Fähigkeiten | Power: Der Document Store, Routing Nodes und Tools geben dem Agenten Dinge, die er tun kann |
  | Systemanweisungen | Governance: Die Regeln, die bestimmen, wie Intelligenz und Fähigkeit angewendet werden |
Ohne Governance arbeiten Intelligenz und Fähigkeit ohne Einschränkung. Für Meridians Agenten ist ein ungesteuertes Verhalten kein theoretisches Risiko. Frühere Boundary-Tests haben bereits gezeigt, was passiert, wenn dem Agenten klare Anweisungen fehlen: Er erfindet plausibel klingende Antworten, folgt Override-Versuchen und verliert unter Druck seine definierte Identität.
Ein gut geschriebener System-Prompt verhindert, dass diese Fehler in Produktion auftreten.
## Die vier Elemente eines gesteuerten System-Prompts
### Element 1: Rolle und Persona
Die Rollendefinition sagt dem Modell, wer es ist, wem es dient und wie es kommuniziert. Sie sollte spezifisch genug sein, um über unterschiedliche Interaktionen hinweg konsistentes Verhalten zu erzeugen.
Eine schwache Rollendefinition:
> Du bist ein hilfreicher Assistent.
Das sagt dem Modell nichts Spezifisches. Jedes Verhalten ist damit vereinbar, ein hilfreicher Assistent zu sein.
Eine starke Rollendefinition für Meridian:
> Du bist ein interner Wissens- und Operations-Support-Agent für Meridian Consulting und unterstützt das Consulting-Team der Firma bei seinen Kunden-Engagements in Deutschland, Polen, Tschechien und den nordischen Märkten. Du kommunizierst in einem direkten, präzisen und professionellen Ton, der zu einem Beratungsumfeld passt.
Dies definiert, für wen der Agent arbeitet, wem er dient, den operativen Kontext und den erwarteten Kommunikationsstil. All das prägt das Verhalten konsistent.
### Element 2: Scope und harte Grenzen
Scope definiert, wozu der Agent autorisiert ist. Grenzen definieren, was er unter keinen Umständen tun darf. Der Scope sollte auf die Aufgabenebene definiert werden, nicht auf die Themenebene.
Ein Scope auf Themenebene:
> Beantworte Fragen zur Beratungsarbeit.
Das ist zu breit. Fast jede Frage könnte als relevant für Beratungsarbeit formuliert werden.
Ein Scope auf der Aufgabenebene:
> Relevante Inhalte aus Meridians interner Wissensdatenbank bereitstellen, Fragen zu interner Prozessdokumentation und operativen Playbooks beantworten und komplexe Queries an den zuständigen Specialist innerhalb der Firma routen.
Dies definiert konkrete autorisierte Aktionen, die vorhersagbares, auditierbares Verhalten erzeugen.
Harte Grenzen müssen als Verbote formuliert sein, nicht als Präferenzen.
Eine Präferenz:
> Versuche, nicht über Wettbewerberfirmen zu sprechen.
Das lässt dem Modell Raum zu entscheiden, wann eine Ausnahme gerechtfertigt ist.
Ein Verbot:
> Sprich unter keinen Umständen über Wettbewerberfirmen, Vertraulichkeitsbedingungen von Kunden oder laufende kommerzielle Verhandlungen.
Das schließt diesen Raum vollständig.
### Element 3: Anweisungen zum Capability Routing
Wenn der Agent Fähigkeiten erhält, braucht er klare Anweisungen dazu, wann er welche verwendet und wie er mit den Outputs umgehen soll.
Ohne Routing-Anweisungen trifft der Agent Capability-Entscheidungen allein auf Grundlage semantischer Ähnlichkeit. Das funktioniert, wenn Fähigkeiten klar voneinander getrennt sind, erzeugt aber Routing-Fehler, wenn eine Query plausibel mit mehr als einer Fähigkeit bearbeitet werden könnte. Zum Beispiel könnte ein Consultant, der nach dem Status eines bestimmten Engagements fragt, entweder ein Knowledge-Base-Retrieval oder eine Live-Datenabfrage auslösen. Ohne klare Routing-Anleitung rät der Agent nur.
Routing-Anweisungen sollten festlegen:
- Unter welcher Bedingung jede Fähigkeit aufgerufen wird
- Welche Informationen der Agent haben muss, bevor er sie aufruft
- Wie der Agent mit dem Output umgehen soll
Für Meridians aktuellen Build befindet sich die Routing-Anweisung für die Wissensdatenbank bereits im System-Prompt. Wenn in den kommenden Lektionen neue Fähigkeiten hinzugefügt werden, sollte für jede einzelne gleichzeitig eine Routing-Anweisung ergänzt werden.
### Element 4: Fallback-Verhalten
Die Fallback-Anweisung steuert, was der Agent tut, wenn keine seiner Fähigkeiten die Query lösen kann. Ohne definierten Fallback erzeugt der Agent einen von zwei Fehlermodi: Er generiert eine plausibel klingende Antwort aus Geminis Trainingsdaten, oder er produziert eine vage, wenig hilfreiche Antwort, die dem Consultant keinen nächsten Schritt bietet. Beides ist schlechter als ein ehrlicher, spezifischer Fallback.
Ein schwacher Fallback:
> Ich weiß es nicht.
Das ist ein Ausweichen. Es gibt dem Consultant nichts Nützliches.
Ein starker Fallback für Meridian:
> Ich habe die gesuchte Information nicht in meiner aktuellen Wissensdatenbank. Für diese Query würde ich empfehlen, sich direkt an Meridians Knowledge-Management-Team zu wenden.
Dies benennt die Einschränkung klar, beschreibt sie ehrlich und gibt einen Weg nach vorn.
![image]((notion-hosted file))

## Wie ein vollständiger Meridian-System-Prompt jetzt aussieht
Die vier Elemente zusammen ergeben einen System-Prompt, der spezifisch genug ist, um das Verhalten über alle aktuellen und kommenden Fähigkeiten des Agenten hinweg konsistent zu steuern:
> Du bist ein interner Wissens- und Operations-Support-Agent für Meridian Consulting und unterstützt das Consulting-Team der Firma bei seinen Kunden-Engagements in Deutschland, Polen und Tschechien. Du kommunizierst in einem direkten, präzisen und professionellen Ton, der zu einem Beratungsumfeld passt.
  Du bist autorisiert, relevante Inhalte aus Meridians interner Wissensdatenbank bereitzustellen, Fragen zu interner Prozessdokumentation und operativen Playbooks zu beantworten und komplexe Queries an den zuständigen Specialist innerhalb der Firma zu routen.
  Sprich unter keinen Umständen über Wettbewerberfirmen, Vertraulichkeitsbedingungen von Kunden oder laufende kommerzielle Verhandlungen. Beantworte unter keinen Umständen Fragen zu Meridians kommerzieller Performance, Aktienkurs oder Eigentümerstruktur.
  Wenn ein Consultant nach Meridians internen Policies, Verfahren, Eskalationsregeln, Projektklassifizierung, Knowledge-Sharing-Anforderungen oder regionalen operativen Richtlinien fragt, rufe die relevanten Informationen aus deiner Wissensdatenbank ab, bevor du antwortest. Verankere deine Antwort immer in den abgerufenen Inhalten.
  Wenn keine deiner Fähigkeiten die Query lösen kann, antworte mit: Ich habe die gesuchte Information nicht in meiner aktuellen Wissensdatenbank. Für diese Query würde ich empfehlen, sich direkt an Meridians Knowledge-Management-Team zu wenden.
Dieser Prompt wird erweitert, wenn Conditional Routing und ein Live-Daten-Tool hinzugefügt werden. Jede neue Fähigkeit erhält ihre eigene Routing-Anweisung, die zum bestehenden Prompt hinzugefügt wird, während die Rolle, der Scope, die Grenzen und der Fallback unverändert bleiben.
## Verständnis prüfen
>  Meridians Agent ist sowohl mit dem Document Store meridian-knowledge als auch mit einem HTTP Node für Live-Engagement-Daten verbunden. Ein Consultant fragt: „Kannst du den aktuellen Status meines Engagements prüfen?“ Der Agent ruft einen Chunk aus der Wissensdatenbank zu Projektklassifizierungsstufen ab und antwortet damit, statt das Live-Daten-Tool abzufragen. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/6389de40-2a62-4d5b-84f1-877a9fa15232


> 💡 Takeaway: 
  Ein System-Prompt ist das Regelwerk. Die vier Elemente sind der Mechanismus, der das Verhalten des Agenten über jede Query hinweg, die er jemals erhalten wird, vorhersagbar, auditierbar und sicher macht.
  Wenn Meridians Agent in den kommenden Lektionen neue Fähigkeiten erhält, bekommt jede davon eine Routing-Anweisung, die zu diesem Framework hinzugefügt wird. Das Framework selbst bleibt stabil.