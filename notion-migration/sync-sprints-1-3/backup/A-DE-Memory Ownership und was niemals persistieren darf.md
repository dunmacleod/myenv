# Memory Ownership und was niemals persistieren darf

Notion page: https://app.notion.com/p/Memory-Ownership-und-was-niemals-persistieren-darf-37f9418319f382b98a4e8116b00f850c
Backed up before n8n migration

Petra hatte es im wöchentlichen Ops-Review markiert. Ein Kunde aus den Niederlanden hatte den Vela-Agenten nach einer Lieferverzögerung gefragt und dabei den Namen seines Logistikkontakts sowie eine Referenznummer aus einem internen Beschaffungssystem genannt. Eine ganz normale Supportanfrage. Der Agent hatte sie sauber bearbeitet. Zwei Sessions später stellte dann ein anderes Mitglied desselben Kundenteams eine völlig andere Frage zur Lieferantenkoordination, und der Agent erwähnte in seiner Antwort von sich aus den Namen des Logistikkontakts und die Beschaffungsreferenz. Gefragt hatte ihn danach niemand. Er hatte es sich einfach gemerkt.
Als sensibel markiert war die Information nicht. Niemand hatte entschieden, dass sie persistieren soll. Sie landete während der ersten Session einfach in allMessages und tauchte in der zweiten wieder auf, weil die Memory-Konfiguration das zuließ.
Das ist das Ownership-Problem. In der letzten Lektion ging es darum, welche Agenten geteilte Memory überhaupt lesen dürfen. Diese Lektion legt eine zweite Ebene drauf: Wer ist dafür verantwortlich, was gespeichert wird? Und welche Informationen dürfen über den einen Turn hinaus, in dem sie entstanden sind, keine Spur mehr hinterlassen?
> ➡️ allMessages ist eine Memory-Type-Einstellung auf dem Agent-Node in Flowise Agentflow V2. Sie weist den Agenten an, bei jeder Ausführung die vollständige Konversationshistorie in das Kontextfenster des Modells zu übergeben.

## Memory Ownership in einem Multi-Agent-System
In einem Single-Agent-System ist Ownership klar. Ein Agent schreibt, derselbe Agent liest, und er ist für beides verantwortlich. In einem Multi-Agent-System verschwimmt das. Der LLM Classifier schreibt query_type in $flow.state. Der Commercial-Agent liest es. Wem gehört dieser Schlüssel? Wer leert ihn, wenn er veraltet ist? Wer entscheidet, ob er in die nächste Session mitgenommen wird?
Der Node, der einen Wert schreibt, bekommt dadurch nicht automatisch die Ownership dafür. Das ist eine Designentscheidung. Ohne eine explizite Entscheidung gehört jedes Informationselement im System effektiv niemandem. Das heißt: Niemand leert es, niemand auditiert es, und niemand bemerkt es, wenn es zum Problem wird.
Eine brauchbare Arbeitsdefinition: Der Agent, der einen Wert in geteilte Memory schreibt, ist dafür verantwortlich, bis ein anderer Agent explizit als Consumer benannt wird.
Der verantwortliche Agent ist für drei Dinge zuständig:
- Den Wert im richtigen Format zum richtigen Zeitpunkt schreiben
- Dokumentieren, was der Wert bedeutet und was ein nachgelagerter Agent damit tun sollte
- Keine Werte schreiben, die eigentlich privat in seinem eigenen Kontext bleiben sollten
Genau diesen letzten Punkt hat Petras Markierung sichtbar gemacht. Kein Agent war als Owner des Logistikkontakts und der Beschaffungsreferenz benannt worden. Sie sind einfach als Nebeneffekt einer ganz normalen Konversation in allMessages gelandet, ohne dass das jemand bewusst so entschieden hätte.
## Was niemals persistieren darf
Manche Arten von Informationen gehören nur in den einen Agenten-Turn, in dem sie entstehen. Danach sollten sie verschwinden. Ob eine Information technisch als sensibel gilt, ist dabei nebensächlich. Zwei Fragen zählen: Könnte ein späterer Agent sie beim Lesen richtig einordnen und nutzen? Und schafft ihre bloße Anwesenheit ein Risiko, das größer ist als der Nutzen, sie aufzubewahren?
Vier Kategorien, die routinemäßig nicht persistieren sollten:
- Flüchtige Identifikatoren. Temporäre Codes, Einmal-Token, Session-Referenznummern und ähnliche Werte. Sie gelten nur für einen bestimmten Moment. Behält ein Agent ein Session-Token über dessen Ablauf hinaus und gibt es an einen nachgelagerten Agenten weiter, kann der versuchen, ein ungültiges Credential zu nutzen. Schlimmer noch: Es könnte sogar funktionieren, obwohl es längst hätte widerrufen werden sollen.
- Abgeleitete Annahmen. Werte, die der Agent berechnet oder abgeleitet hat, statt sie aus einer zuverlässigen Quelle zu holen. Der Confidence Score des LLM Classifier ist so ein Wert. Die interne Tier-Annahme des Commercial-Agent auch. Abgeleitete Werte passen genau zu dem Moment, in dem sie entstanden sind. Später können sie falsch sein, zum Beispiel in einem anderen Kontext, in einer neuen Session oder wenn sich der zugrunde liegende Zustand geändert hat. Genau das ist die Ursache für die typischen „Stale Data"-Bugs im Memory: Abgeleitete Werte werden wie Fakten behandelt und gespeichert.
- Beiläufig freiwillig mitgeteilte personenbezogene Informationen. Zum Beispiel der Name eines Kunden, der Name eines internen Kontakts oder eine Referenz auf ein Drittsystem. Diese Info taucht in einer Supportanfrage auf, gehört aber nicht zu den strukturierten Daten, für die der Agent eigentlich gebaut wurde. Velas Agent war nicht dafür gebaut, Beschaffungsreferenzen oder Logistikkontakte zu speichern. Trotzdem landeten sie in allMessages, einfach weil nichts das verhindert hat.
- Konversationsinterner Arbeitskontext. Zum Beispiel Zwischenzusammenfassungen, die ein Agent für seine eigene Antwort geschrieben hat. Oder Hypothesen, die er kurz durchgespielt und wieder verworfen hat. Oder interne Einordnungen, die er nur fürs Routing gebraucht hat. Das sind Verarbeitungsartefakte, keine Informationen, die das System weitertragen muss.
![image]((notion-hosted file))
Das Muster ist bei allen vier Kategorien gleich: Die Information stimmt und hilft in dem Moment, in dem sie entsteht. Bleibt sie länger im System, wächst das Risiko, dass sie missbraucht, falsch interpretiert oder in einem späteren Kontext falsch angewendet wird.
## Das auf die Vela-Canvas anwenden
> 🔥 Bevor du startest, kopier dir diese Vorlage. Sie folgt dem Aufbau dieser Lektion: ein Tab, um die vier „darf nicht persistieren"-Kategorien auf der Vela-Canvas durchzugehen, und ein Tab, um die Spalte zur Persistenzentscheidung in die Boundary Map deines Projekts einzutragen.

Geh zurück zu deiner Sprint-2-Canvas. Such dir für jede der vier Kategorien von oben mindestens ein konkretes Beispiel aus deiner aktuellen Canvas, das dazu passt.
Arbeite für jedes Beispiel diese Fragen durch:
1. Wo wird die Information derzeit gespeichert ($flow.state, allMessages oder beides)?
1. Welcher Agent oder Node hat sie geschrieben?
1. Gibt es einen Grund, warum die Info den Turn überleben muss, in dem sie entstanden ist? Nenn den Grund, oder sag ehrlich: den gibt's nicht.
1. Soll sie nicht persistieren, wie gehst du damit um? Drei Optionen: gar nicht erst in geteilte Memory schreiben. Oder in einen Flow-State-Schlüssel schreiben und dokumentieren, dass er als turn-scoped gilt. Oder in allMessages schreiben und dem nachgelagerten Agenten per System-Prompt sagen, dass er das in Antworten nicht erwähnen soll.
Für jede Canvas gibt es nicht die eine richtige Antwort. Was die richtige Behandlung ist, hängt davon ab, wofür das System gebaut ist. Bei der Übung geht es darum, die Kategorie zu erkennen und die Optionen durchzuspielen.
## Wende das auf dein Projekt an
Erweitere die Memory Boundary Map aus der letzten Lektion um eine dritte Spalte: Persistenzentscheidung.
Trag für jedes Informationselement in deiner Boundary Map eine von drei Entscheidungen ein:
- Über Sessions hinweg persistieren: Die Info ist für künftige Interaktionen wertvoll. Sie aufzubewahren ist eine bewusste, sinnvolle Entscheidung.
- Session-scoped: Die Info ist innerhalb der Session nützlich, soll aber nicht darüber hinaus. Flow State passt, ein persistenter Store nicht.
- Turn-scoped: Die Info gilt nur für den einen Agenten-Turn, in dem sie entsteht. Sie gehört an keinen geteilten Ort. Muss sie trotzdem geschrieben werden, zum Beispiel weil die Routing-Logik es braucht, dann dokumentier klar: turn-scoped, nachgelagerte Agenten sollen sie nicht referenzieren.
Schreib für jedes turn-scoped Element einen Satz dazu, wie du verhinderst, dass es persistiert. Zum Beispiel indem du es gar nicht erst in geteilte Memory schreibst, eine System-Prompt-Anweisung setzt oder einen Clearing-Schritt danach einbaust.
Mit dieser Spalte ist der Memory-Boundary-Teil deiner Sprint-3-Abgabe komplett. Du hast jetzt drei Dimensionen für jedes Informationselement dokumentiert: ob es geteilt oder privat ist, wem es gehört, und wie lange es leben darf.

>  
  ### 🔥 AI nutzen, wenn du feststeckst
  Was turn-scoped ist und was nicht, ist manchmal wirklich schwer zu erkennen. Bist du dir bei einem Informationselement unsicher, beschreib es der AI möglichst genau:
  - Was die Information ist und woher sie kommt
  - Welcher Agent sie erzeugt hat und welcher Agent sie als Nächstes lesen könnte
  - Was ein zukünftiger Agent damit tun würde, wenn sie noch verfügbar wäre
  Zum Beispiel: „In a Flowise multi-agent system, the first agent is a classifier that assigns a confidence score to each query. Should that confidence score persist to the next session? What could go wrong if it does?"
  Nutz die Antwort, um die Grenzfälle durchzudenken. Die finale Entscheidung triffst du selbst. Denn die Persistenzentscheidung für dein Projekt hängt von Kontext ab, den die AI nicht komplett sehen kann.

## Achte auf
- Denk dran, dass allMessages nur das Wichtige behält. In Wirklichkeit speichert allMessages alles, was in der Konversation gesagt wurde: beiläufige Erwähnungen, Classifier-Ausgaben, internes Reasoning, das sich das Modell vor der Antwort zurechtgelegt hat, und jede Info, die ein Kunde geteilt hat, selbst wenn der Agent sie gar nicht brauchte. Es gibt keine automatische Filterung. Was in der Konversation vorkam, steht in der Historie.
- „Es gab keine Beschwerde" als Beweis nehmen, dass die Retention okay ist. Beim Vela-Fall mit dem Logistikkontakt kam auch keine Beschwerde, dafür aber eine Antwort, die niemand wollte. Die meisten Retentionsprobleme bleiben unsichtbar, bis sie in einer Ausgabe an den Nutzer auftauchen. Keine Beschwerde heißt nicht, dass deine Persistenzentscheidungen stimmen.
- Geteilten Zustand zu aggressiv leeren. Das ist der andere Fehler. Markierst du alles als turn-scoped, können die Agenten gar nicht mehr koordinieren. Wird zum Beispiel query_type gelöscht, bevor der Condition-Node ihn liest, bricht die ganze Routing-Logik. Die eigentliche Frage lautet: Was muss mindestens persistieren, und für wie lange?
## Zusammenfassung
Memory Ownership und Persistenz-Scope sind zwei Seiten derselben Designentscheidung. Ownership legt fest, welcher Agent für einen Wert verantwortlich ist: wer ihn schreibt, wofür er steht und wer ihn als Nächstes lesen soll. Persistenz-Scope legt fest, wie lange dieser Wert bestehen darf: nur den aktuellen Turn, die aktuelle Session, oder über Sessions hinweg.
Die Vela-Canvas zeigt, was passiert, wenn keine der beiden Fragen geklärt ist: Informationen, die eigentlich turn-scoped gehört hätten, bestehen über mehrere Sessions und tauchten in einer völlig unabhängigen Antwort wieder auf. Um das zu verhindern, musst du für jedes Informationselement in deinem System zwei Dinge festlegen: wem es gehört, und wie lange es bleiben darf.
Die nächste Lektion bringt State ins Spiel, ein verwandtes, aber eigenständiges Konzept. Memory hält fest, was ein Agent aus vergangenen Interaktionen weiß. State hält fest, wo das System gerade in seiner aktuellen Ausführung steht. Diese Unterscheidung prägt, wie du den Handoff von einem Agenten zum nächsten gestaltest.