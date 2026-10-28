# Memory vs. Wissensdatenbank vs. Tools

Notion page: https://app.notion.com/p/Memory-vs-Wissensdatenbank-vs-Tools-3779418319f3809e887ee90d8dbed2cf
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Die drei Kernkomponenten eines Business-Agenten (Memory, Wissensdatenbank und Tools) und warum sie unterschiedliche Zwecke erfüllen. Du wirst in diesem Sprint nicht alle drei bauen, aber wenn du jetzt verstehst, wie sie zusammenpassen, wird jede einzelne Komponente leichter zu konfigurieren sein, wenn du so weit bist.
> 📝 Ein Hinweis zum Umfang: Dieser Sprint konzentriert sich auf Memory. Wissensdatenbanken wirst du in Sprint 2 konfigurieren und Tools in Sprint 3. Diese Lektion stellt alle drei Komponenten vor, damit du sehen kannst, wie sie zusammenpassen, aber von dir wird nicht erwartet, dass du diese Woche etwas anderes als Memory baust oder konfigurierst.

## Drei Dinge, die ähnlich aussehen, es aber nicht sind
Während die Contigo GmbH ihre Agenten weiterentwickelt, stößt das Team immer wieder auf dasselbe Problem: Memory, Wissensdatenbank und externe Tools werden miteinander verwechselt. Entwickler speichern Richtliniendokumente im Gesprächs-Memory. Andere verwenden die Wissensdatenbank, um Nutzerpräferenzen nachzuverfolgen. Ein Team vermischt Live-API-Aufrufe mit Dokumentenabruf auf eine Weise, die das System unvorhersehbar und schwer zu debuggen macht.
Die Grundursache ist in jedem Fall dieselbe: Die drei Kernkomponenten eines Business-Agenten (Memory, Wissensdatenbank und Tool-State) werden als austauschbar behandelt, aber das sind sie nicht. Jede erfüllt einen eigenen Zweck, der sicherstellt, dass Agenten zuverlässig, wartbar und leichter vertrauenswürdig sind.
Diese Lektion zieht diese Grenzen klar.
## Memory (Woran sich der Agent über das Gespräch erinnert)
Memory verfolgt den Verlauf und Kontext einer laufenden Interaktion.
> ❓ 
  #### Memory beantwortet die Frage: Welche Informationen hat mir der Nutzer bereits gegeben, und was wurde im Gespräch bereits festgelegt?”
In einem Contigo-Supportgespräch enthält Memory Dinge wie die Kontonummer, die der Kunde zu Beginn der Session angegeben hat, die Schritte, die in einem Kreditantragsprozess bereits abgeschlossen wurden, oder die Tatsache, dass der Kunde eine Kontaktaufnahme per E-Mail statt per Telefon bevorzugt. Bei Memory geht es um den Nutzer und die Interaktion. Es kann kurzfristig sein (nur während der aktiven Session) oder langfristig (über Sessions hinweg).
## Wissensdatenbank (Was der Agent aus vertrauenswürdigen Quellen abruft)
Eine Wissensdatenbank ist eine Sammlung von Dokumenten oder Datensätzen, die der Agent durchsuchen kann, wenn er sachliche Informationen benötigt. Statt sich auf das allgemeine Training des Sprachmodells zu verlassen, ruft der Agent Inhalte aus verifizierten Quellen ab, um seine Antworten auf verlässliche Informationen zu stützen. Das wirst du in Sprint 2 bauen.
Für Contigo könnte die Wissensdatenbank die Kriterien des Unternehmens für die Kreditwürdigkeit, regulatorische Compliance-Richtlinien nach EU-Finanzrecht oder interne Produktdokumentation enthalten. Dieser Inhalt ist statisch oder semi-statisch (er ändert sich selten und gilt für alle Nutzer gleichermaßen, nicht speziell für einen einzelnen Kunden).
> ❓ 
  #### Die Wissensdatenbank beantwortet die Frage: Welche offiziellen Fakten oder Regeln brauche ich, um eine genaue, fundierte Antwort zu geben?

## Tool-State (Was der Agent in externen Systemen ausführt)
Tools ermöglichen es einem Agenten, über die reine Textgenerierung hinaus Aktionen auszuführen, zum Beispiel ein Live-System abzufragen, ein Formular einzureichen oder einen Workflow auszulösen. Das wirst du in Sprint 3 bauen. Durch das Aufrufen externer APIs oder Dienste kann ein Agent eine Live-Datenbank abfragen, ein Formular einreichen, einen Workflow auslösen, eine Benachrichtigung senden oder eine Transaktion verarbeiten.
Für Contigo könnte der Einsatz von Tools bedeuten, den aktuellen Kontostand eines Kunden über die Core-Banking-API zu prüfen, einen Kreditantrag an das Verarbeitungssystem zu übermitteln oder ein Compliance-Problem in der Case-Management-Plattform zu markieren. Das sind reale Aktionen, die den Zustand externer Systeme verändern, nicht nur Antworten, die aus gespeicherten oder abgerufenen Informationen erzeugt werden, Aktionen mit Auswirkungen auf externe Systeme.
> ❓ 
  #### Tool-State beantwortet die Frage: Welche externe Aktion muss ich ausführen, um das abzuschließen, worum der Nutzer bittet?

## Warum die Trennung wichtig ist
[TABLE]
  |  | Memory | Wissensdatenbank | Tool-State |
  | Was es enthält | Gesprächsverlauf und Nutzerkontext | Autoritative Dokumente und Richtlinien | Live-Systemverbindungen und API-Integrationen |
  | Wie oft es sich ändert | Bei jedem Gesprächs-Turn | Selten | In Echtzeit |
  | Contigo-Beispiel | Bevorzugte Sprache des Kunden und offene Fälle | EU-Regelungen zur Kreditwürdigkeit | Einreichen eines Kreditantrags über die Banking-API |
  | Risiko bei falscher Nutzung | Datenschutzverletzungen, Überladener Kontext | Halluzination durch veraltete Dokumente | Unbeabsichtigte reale Aktionen oder Datenoffenlegung |
Diese drei Komponenten getrennt zu halten, ist eine Voraussetzung dafür, Agenten zu bauen, die sicher, auditierbar und wartbar sind. Ein Agent, der Memory mit Wissensdatenbank vermischt, wird Schwierigkeiten haben, die richtigen Informationen zu finden. Ein Agent, der Wissensdatenbank mit Tool-Nutzung vermischt, handelt möglicherweise auf Grundlage von Dokumenten, statt Live-Systeme abzufragen, oder umgekehrt.

![image]((notion-hosted file))
## Verständnis prüfen
>  Ein Contigo-Agent muss die aktuellen Kriterien des Unternehmens für die Kreditwürdigkeit abrufen, um eine Kundenfrage zu beantworten. Welche Komponente sollte er verwenden?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e47cf7cc-3dc5-4375-9592-448aa520a280

> 💡 Takeaway: 
  Memory, Wissensdatenbank und Tool-State sind drei unterschiedliche Komponenten mit drei unterschiedlichen Aufgaben. Memory verfolgt das Gespräch. Die Wissensdatenbank fundiert die Antwort mit verifizierten Fakten. Tools führen Aktionen in der realen Welt aus. Ein zuverlässiger Business-Agent hält diese Dinge getrennt. Dieser Sprint behandelt Memory. Die anderen beiden Komponenten werden in den folgenden Sprints gebaut.
