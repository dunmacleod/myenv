# Warum Orchestrierungsmuster wichtig sind

Notion page: https://app.notion.com/p/Warum-Orchestrierungsmuster-wichtig-sind-ef39418319f382c98f9c81c2b3fb2175
Backed up before n8n migration

## Zweck der Lektion
Die häufigsten Orchestrierungsmuster verstehen, die in AI-Agentensystemen verwendet werden, und erkennen, wann welches Muster nützlich ist. Lernen, wie unterschiedliche Koordinationsstrukturen das Verhalten eines agentischen Workflows beeinflussen.
## Lernergebnisse
Am Ende der Lektion kannst du
- die häufigsten Orchestrierungsmuster identifizieren, die in AI-Systemen verwendet werden
- erklären, wie Informationen durch unterschiedliche Orchestrierungsmuster fließen
- die Stärken und Trade-offs jedes Musters erkennen
- ein passendes Orchestrierungsmuster für ein bestimmtes Problem auswählen
## Einführung
In der vorherigen Lektion hast du Orchestrierung und Choreografie als zwei Ansätze kennengelernt, um Agenten, Tools und Workflows zu koordinieren. Orchestrierung ist jedoch kein einzelnes Design. Es gibt viele Möglichkeiten, zu organisieren, wie Agenten kommunizieren und zusammenarbeiten.
Das Orchestrierungsmuster bestimmt, wie Arbeit durch das System läuft, wie Entscheidungen getroffen werden und wie Ergebnisse kombiniert werden. Das richtige Muster zu wählen, hat oft einen größeren Einfluss auf das Systemverhalten als die Wahl eines anderen Modells.
Orchestrierungstools wie n8n sowie codebasierte Frameworks wie LangGraph, CrewAI und AutoGen können Varianten dieser Muster umsetzen. Ihre Nodes, Schnittstellen und Funktionen unterscheiden sich jedoch.
![image]((notion-hosted file))
## Chaining (sequenziell)
Chaining ist das einfachste Orchestrierungsmuster. Arbeit läuft durch eine feste Sequenz von Agenten oder Schritten, wobei jeder Schritt den Output des vorherigen nutzt.
Beispiel:
> Im gegebenen Workflow identifiziert der Schritt Requirements Analysis die Ziele und Einschränkungen, der Research-Schritt sammelt relevante Informationen, der Schritt Draft Generation erstellt den ersten Inhalt, und der Review-Schritt prüft vor der finalen Lieferung auf Genauigkeit, Qualität und Ausrichtung an den ursprünglichen Anforderungen.
![image]((notion-hosted file))
Jede Phase hat eine klare Verantwortung und gibt ihr Ergebnis an die nächste Phase weiter.
Dieses Muster funktioniert gut, wenn Aufgaben eine natürliche Sequenz haben und jeder Schritt vom vorherigen abhängt.
### Vorteile
>  
  - Leicht zu verstehen
  - Vorhersehbarer Ausführungspfad
  - Einfach zu debuggen

### Einschränkungen
>  
  - Langsam bei großen Workflows
  - Jeder Schritt muss warten, bis der vorherige Schritt abgeschlossen ist
  - Ein Fehler kann die gesamte Kette stoppen

## Parallel
In einem parallelen Muster arbeiten mehrere Agenten gleichzeitig an unterschiedlichen Teilen des Problems.
Beispiel:
> Ein Travel-Planning-Assistant kann gleichzeitig nach Flügen, Hotels und Aktivitäten suchen. Sobald alle Ergebnisse verfügbar sind, werden sie zu einem einzigen Reiseplan kombiniert.
![image]((notion-hosted file))
Da unabhängige Aufgaben gleichzeitig laufen, sind parallele Workflows oft deutlich schneller als sequenzielle Workflows.
### Vorteile
>  
  - Schnellere Ausführung
  - Effiziente Nutzung spezialisierter Agenten
  - Gut für unabhängige Teilaufgaben
### Einschränkungen
>  
  - Erfordert eine Möglichkeit, Ergebnisse zu kombinieren
  - Komplexer als Chaining
  - Höhere Ressourcennutzung
## Routing
Routing führt einen Entscheidungspunkt in den Workflow ein. Ein Router prüft die eingehende Anfrage und wählt den passendsten Agenten aus, der sie bearbeiten soll.
Beispiel:
> Ein Kunde stellt die Frage: „Why was I charged twice this month?" Der Router analysiert die Anfrage und stellt fest, dass es sich um ein Billing-Thema handelt, also wird die Anfrage an den Billing Agent gesendet. Wenn die Frage einen Produktfehler betreffen würde, würde sie an den Technical Agent geroutet. Allgemeine Anfragen würden an den General Support Agent gesendet.
![image]((notion-hosted file))
Der Router bewertet die Eingabe und wählt den passendsten Pfad aus.
>  Anders als bei paralleler Ausführung wird nur ein Branch ausgewählt und ausgeführt.
Viele Customer-Support-Systeme, Helpdesks und AI-Assistenten nutzen Routing, um sicherzustellen, dass Anfragen vom richtigen Experten bearbeitet werden.
### Vorteile
>  
  - Effiziente Nutzung spezialisierter Agenten
  - Neue Fachbereiche lassen sich leicht hinzufügen
  - Reduziert unnötige Arbeit
### Einschränkungen
>  
  - Routing-Fehler wirken sich auf den gesamten Workflow aus
  - Router-Logik muss sorgfältig gepflegt werden
## Iteration
Iteration ermöglicht einem Agenten, seine eigene Arbeit mehrfach zu verbessern, bevor ein finales Ergebnis erzeugt wird.
Statt sofort eine Antwort zu generieren, bewertet das System seinen Fortschritt und führt einen weiteren Durchlauf aus, wenn Verbesserungen nötig sind.
Beispiel:
> Ein Research Agent erstellt einen ersten Plan zur Untersuchung eines Themas. Er sammelt Informationen aus verfügbaren Quellen und übergibt die Ergebnisse dann an einen Evaluation Agent. Der Evaluation Agent prüft, ob die Informationen genau, vollständig und relevant sind. Wenn Lücken oder Qualitätsprobleme gefunden werden, loopt der Workflow zurück zum Research Agent, um zusätzliche Informationen zu sammeln. Dieser Zyklus läuft weiter, bis die Evaluationskriterien erfüllt sind; danach wird ein finaler Bericht erstellt.
[COLUMN_LIST]
  [COLUMN]
    ![image]((notion-hosted file))
    ### Vorteile
    >  
      - Höhere Output-Qualität
      - Unterstützt Selbstkorrektur
      - Fördert tiefere Analyse
  [COLUMN]
    ### Einschränkungen
    >  
      - Höhere Kosten
      - Längere Ausführungszeit
      - Erfordert Evaluationskriterien
## Looping
Looping ähnelt der Iteration, konzentriert sich aber darauf, einen Workflow so lange zu wiederholen, bis eine Bedingung erfüllt ist.
Beispiel:
> Ein Research Agent versucht, eine Frage zur jüngsten Geschäftsentwicklung eines Unternehmens zu beantworten. Er erstellt zuerst eine Suchanfrage, holt relevante Informationen ein und prüft, ob die Ergebnisse genug Beweise für eine Antwort liefern. Sind die Informationen unvollständig oder unklar, erstellt der Agent eine präzisere Suchanfrage und wiederholt den Prozess, bis er genug Informationen gesammelt hat.
![image]((notion-hosted file))
Dieses Muster wird häufig in Retrieval-Augmented-Generation-Systemen (RAG) verwendet, in denen Informationsabruf mehrere Versuche benötigen kann.
>  Anders als Iteration, die einen Prozess typischerweise wiederholt, um einen Output progressiv zu verfeinern oder zu verbessern, konzentriert sich Looping darauf, eine Schrittsequenz zu wiederholen, bis eine bestimmte Bedingung erfüllt ist. Mit anderen Worten: Iteration wird oft zur Verbesserung durch mehrere Durchläufe genutzt, während Looping durch ein Stoppkriterium gesteuert wird, zum Beispiel ausreichend Informationen zu finden, ein Ziel-Konfidenzniveau zu erreichen oder eine Validierungsprüfung zu erfüllen.
[COLUMN_LIST]
  [COLUMN]
    ### Vorteile
    >  
      - Kommt gut mit Unsicherheit zurecht
      - Verbessert die Retrieval-Qualität
      - Kann sich von schwachen Zwischenergebnissen erholen
  [COLUMN]
    ### Einschränkungen
    >  
      - Risiko übermäßiger Wiederholungen
      - Erfordert klare Stoppbedingungen
## Hierarchie
Hierarchie führt einen Supervisor ein, der mehrere Worker Agents koordiniert.
Statt dass alle Agenten direkt miteinander kommunizieren, entscheidet der Supervisor, wer als Nächstes arbeiten soll, prüft Outputs und kombiniert Ergebnisse.
Beispiel:
> Ein Customer-Support-Workflow erhält eine Nutzerfrage. Zuerst bestimmt ein Intent-Classification Agent, ob die Anfrage Billing, technischen Support oder Account Management betrifft. Der Output wird dann an einen spezialisierten Agenten für diese Kategorie übergeben, der eine Antwort generiert. Jeder Schritt hängt vom Output des vorherigen Schritts ab und bildet dadurch eine Chain.
![image]((notion-hosted file))
Der Supervisor steuert den Workflow und stellt sicher, dass die Worker am Gesamtziel ausgerichtet bleiben.
Dieses Muster ist in fortgeschrittenen Multi-Agent-Systemen verbreitet, weil es Spezialisierung ermöglicht und gleichzeitig zentrale Koordination beibehält.
### Vorteile
>  
  - Bewältigt komplexe Projekte
  - Klare Trennung von Verantwortlichkeiten
  - Einfachere Koordination vieler Agenten
### Einschränkungen
>  
  - Komplexeres Design
  - Zusätzlicher Kommunikations-Overhead
  - Supervisor wird zu einer kritischen Komponente
## Vergleich der Muster
Unterschiedliche Muster lösen unterschiedliche Koordinationsprobleme.
[TABLE]
  | Muster | Am besten geeignet für |
  | Chaining | Sequenzielle Aufgaben mit klaren Abhängigkeiten |
  | Parallel | Unabhängige Aufgaben, die gleichzeitig laufen können |
  | Routing | Anfragen an Spezialisten weiterleiten |
  | Iteration | Qualität durch mehrere Durchläufe verbessern |
  | Looping | Wiederholte Retrieval- oder Validierungszyklen |
  | Hierarchie | Große Multi-Agent-Systeme mit spezialisierten Rollen |
Es gibt kein universell bestes Muster. Die richtige Wahl hängt von der Aufgabe, der Anzahl der beteiligten Agenten und dem erforderlichen Koordinationsniveau ab.
## Quiz
Frage 1
>  Cascadia baut einen Customer-Support-Assistenten. Billing-Fragen sollten an einen Billing-Spezialisten gehen, technische Fragen an einen technischen Spezialisten und allgemeine Fragen an einen General Support Agent. Welches Orchestrierungsmuster passt am besten?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/df11184b-e540-4a62-85bd-c82219f49902
## Zusammenfassung
Nicht alle Agentensysteme koordinieren Arbeit auf dieselbe Weise. Manche Systeme geben Arbeit durch eine feste Sequenz weiter, andere verteilen Arbeit parallel. Wieder andere routen Anfragen an Spezialisten oder nutzen einen Supervisor, um Agententeams zu koordinieren.
Diese Orchestrierungsmuster zu verstehen lohnt sich. Sie sind die Bausteine für fortgeschrittenere Agentensysteme. Baust du weiter an Workflows, kombinierst du oft mehrere Muster miteinander. Ein realer Agent nutzt vielleicht Routing für die Auswahl eines Spezialisten. Er setzt parallele Ausführung ein, um Informationen zu sammeln. Am Ende verbessert er mit Iteration das finale Ergebnis, bevor er antwortet.
Das gewählte Muster prägt das Verhalten des Systems. Das gilt oft schon lange, bevor die Modellqualität zum limitierenden Faktor wird.