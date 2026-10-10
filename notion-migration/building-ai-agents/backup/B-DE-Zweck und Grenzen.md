# Zweck und Grenzen

Notion page: https://app.notion.com/p/Zweck-und-Grenzen-3789418319f38042b6b8dd874b191388
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Klare Systemanweisungen schreiben, die die Rolle, Zielnutzer und Grenzen deines Projektagenten definieren. Anschließend verfeinerst du sie, bis der Agent sich konsistent innerhalb seines definierten Umfangs verhält.

Der Meridians Baseline-Agent ist konfiguriert und läuft. Das Gemini-Modell ist verbunden, der Drei-Node-Flow ist überprüft, und die Zwei-Turn-Validierung wurde bestanden. Die nächste Frage ist trügerisch einfach: Was soll dieser Agent eigentlich tun?
Ohne eine klare Antwort wird der Agent versuchen, alles zu beantworten, was ein Nutzer fragt. Er wird Meinungen zu Themen außerhalb seiner Expertise anbieten, Aufgaben versuchen, für die er nicht zuverlässig ausgestattet ist, und Antworten produzieren, die in Ton, Scope und Genauigkeit inkonsistent sind. Ein Large Language Model ist standardmäßig darauf ausgelegt, hilfreich zu sein. In einem Geschäftskontext wird uneingeschränkte Hilfsbereitschaft schnell zum Haftungsrisiko.
Das Meridians Team hat das auf die harte Tour gelernt. Ein früherer Prototyp, der für die HR-Abteilung eines Kunden gebaut wurde, begann, Fragen zu Gehaltsbenchmarks von Wettbewerbern zu beantworten, rechtliche Interpretationen von Arbeitsverträgen anzubieten und detaillierte Beratung zu einer persönlichen Steuersituation zu geben, die ein Mitarbeiter angesprochen hatte, weil er ihn für einen allgemeinen Assistenten gehalten hatte. Nichts davon lag im Scope. Alles davon verursachte Probleme.
Der System-Prompt ist der Ort, an dem du die Grenze ziehst. In dieser Lektion schreiben wir die Meridians System-Prompt gemeinsam, eine Säule nach der anderen.

## Anatomie eines funktionierenden System-Prompts
Bevor wir einen schreiben, schauen wir uns an, wie ein guter System-Prompt aufgebaut ist. Er adressiert drei Dinge:
1. Rolle und Persona: Wer der Agent ist und wie er kommuniziert
1. Scope: Wobei der Agent helfen darf
1. Grenzen und Eskalation: Was er ablehnen muss und was er stattdessen tun sollte
Diese drei Säulen erscheinen in fast jedem gut gebauten System-Prompt. Sie teilen sich manchmal Sätze (Rolle und Scope können sich überschneiden), aber jede Säule muss vorhanden sein. Wenn eine fehlt, wird das Verhalten des Agenten in diese Richtung abdriften, d.h. eine vage Identität, ausufernder Scope oder stille Ablehnungen ohne Weg nach vorn erstellen.
![image]((notion-hosted file))

Der oben gezeigte Prompt ist das, was du am Ende dieser Lektion geschrieben haben wirst. Wir bauen ihn Säule für Säule auf.
## Schritt 1: Rolle und Persona schreiben
Beginne damit zu entscheiden, wer der Agent ist und wie er spricht.
Ein häufiger erster Versuch sieht so aus:
> "You are a helpful assistant."
Das ist technisch gültig, sagt dem Modell aber fast nichts. Es wird standardmäßig einen generischen, leicht fröhlichen Ton verwenden und jede Anfrage als erlaubt behandeln, weil es keine Ahnung hat, was „hilfreich“ in diesem konkreten Kontext bedeutet.
Vergleiche das mit der Version, die wir verwenden werden:
> "You are Meridian's internal consulting support agent, used by Meridian consultants to find information quickly. Communicate in a direct, professional tone without unnecessary informality or hedging."
Diese Version macht zwei Dinge, die die erste nicht macht. Sie benennt die Aufgabe des Agenten (interner Consulting-Support) und identifiziert seine Nutzer (Meridian-Berater). Außerdem legt sie den Kommunikationston explizit fest (direkt, professionell, ohne Absicherung) wodurch verhindert wird, dass der Agent auf Gesprächsfüller zurückfällt, die ein Berater unter Zeitdruck störend finden wird.
![image]((notion-hosted file))

Jetzt bist du dran: Schreibe deine eigenen zwei Sätze für Rolle und Persona des Meridian-Agenten. Du kannst unsere Version verwenden, sie anpassen oder deine eigene Version schreiben. Mach dir noch keine Gedanken über die anderen Säulen. Die fügen wir als Nächstes hinzu.

## Schritt 2: Den Scope definieren
Sobald der Agent weiß, wer er ist, muss er wissen, wobei er helfen darf. Beim Scope gehen die meisten Prompts schief, weil es verlockend ist, etwas zu schreiben, das selbstbewusst klingt, aber eigentlich nichts aussagt.
Ein vager Scope:
> "Help with consulting work."
Was umfasst das? Preismodelle für Kunden? Persönliche Karriereberatung für den Berater? Detaillierte Analyse einer kürzlichen Übernahme durch einen Wettbewerber? Ohne Spezifität wird der Agent annehmen, dass alles erlaubt ist.
Ein spezifischer Scope:
> "You can answer questions about Meridian's active client accounts, internal process documentation, and operational playbooks."
Der Unterschied ist, dass die zweite Version konkrete Inhaltsbereiche benennt. Ein Berater, der den Prompt liest, kann vorhersagen, ob seine Frage im Scope liegt oder außerhalb davon. Der Agent kann das ebenfalls.

![image]((notion-hosted file))
Eine Faustregel: Wenn eine Scope-Aussage jeden Business-Agenten in jeder Branche beschreiben könnte, ist sie zu vage. Spezifität sollte aus den tatsächlichen Inhalten kommen, auf die der Agent Zugriff hat, und aus den tatsächlichen Aufgaben, bei denen seine Nutzer Hilfe brauchen.
Jetzt bist du dran: Füge den Sätzen zur Rolle und Persona, die du in Schritt 1 geschrieben hast, einen Scope-Satz hinzu.

## Schritt 3: Grenzen und Eskalation schreiben
Die dritte Säule sagt dem Agenten, was er ablehnen soll und was er tun soll, wenn er ablehnt. Diese Säule wird besonders oft komplett übersprungen, und genau deshalb beginnen Agenten, Fragen zu rechtlichen Interpretationen und Gehaltsbenchmarks von Wettbewerbern zu beantworten.
Eine vage Grenze:
> "Refuse if you can't answer."
Eine spezifische Grenze mit Eskalation:
> "You cannot provide legal interpretations, HR advice, or competitor intelligence. If a consultant asks about these areas, briefly explain that the topic is outside your scope and suggest they contact Meridian's legal counsel, HR partner, or the firm's competitive intelligence lead, whichever is most relevant."
Die zweite Version macht drei Dinge. Sie benennt spezifische Ablehnungskategorien. Sie sagt dem Agenten, was er tun soll, statt einfach zu stoppen (die Grenze erklären). Und sie bietet Eskalationswege, damit der Berater nicht ohne nächste Schritte hängen bleibt.

![image]((notion-hosted file))
Beachte, dass „die Grenze erklären und einen Kontakt vorschlagen“ ein viel nützlicheres Verhalten ist als „nicht antworten“. Eine stille Ablehnung wirkt kaputt; eine kurze Erklärung mit Weiterleitung wirkt wie ein hilfreicher Kollege.
Jetzt bist du dran: Füge Sätze zu Grenzen und Eskalation hinzu, um deinen Prompt-Entwurf zu vervollständigen.

## Schritt 4: Den Prompt zusammensetzen und eingeben
Dein vollständiger Prompt sollte jetzt vier bis sechs Sätze umfassen und alle drei Säulen abdecken. So sieht die vollständig zusammengesetzte Meridian-Version aus:
> "You are Meridian's internal consulting support agent, used by Meridian consultants to find information quickly. Communicate in a direct, professional tone without unnecessary informality or hedging. You can answer questions about Meridian's active client accounts, internal process documentation, and operational playbooks. You cannot provide legal interpretations, HR advice, or competitor intelligence. If a consultant asks about these areas, briefly explain that the topic is outside your scope and suggest they contact Meridian's legal counsel, HR partner, or the firm's competitive intelligence lead, whichever is most relevant."
Dieser Prompt ist konkret genug, dass zwei verschiedene Entwickler, die ihn lesen, ungefähr dasselbe Verhalten vom Agenten erwarten würden. Das ist der Maßstab.
So gibst du ihn in deinen Canvas ein:
1. Klicke auf den Agent Node auf deinem Agentflow-v2-Canvas, um seine Einstellungen zu öffnen.
1. Suche das Feld System Prompt. Es enthält den Platzhaltertext aus dem vorherigen Walkthrough.
1. Ersetze den Platzhalter durch deinen vollständig zusammengesetzten Prompt.
1. Speichere den Flow über das Speichersymbol oben rechts im Canvas.

## Schritt 5: Die Prompt-Grenze testen
Öffne die integrierte Chat-Oberfläche und führe zwei Testanfragen aus: eine innerhalb deines definierten Scopes, eine außerhalb davon.
In-Scope-Anfrage (etwas, wobei der Agent helfen sollte):
> "Can you summarise the operational playbook for new client onboarding?"
Der Agent sollte in dem direkten, professionellen Ton antworten, den du definiert hast. Die genaue Formulierung wird variieren, aber die Form einer guten Antwort ist: fokussiert, ohne unnötige Einleitung und fundiert in der Art von Prozessdokumentation, die deine Scope-Aussage erlaubt.
Out-of-Scope-Anfrage (etwas, das der Agent ablehnen sollte):
> "What's the average salary for a Senior Consultant at our two biggest competitors?"
Der Agent sollte erklären, dass Competitive Intelligence außerhalb seines Scopes liegt, und den Berater an den Competitive Intelligence Lead verweisen. Er sollte nicht versuchen, mit allgemeinem Wissen oder erfundenen Zahlen zu antworten.
Wenn der Agent die Out-of-Scope-Anfrage beantwortet, ohne die Grenze anzuerkennen, muss der Abschnitt zu Grenzen in deinem Prompt überarbeitet werden. Die häufigste Lösung ist, die Ablehnungskategorien expliziter zu machen (benenne sie, statt nur darauf anzuspielen) und erneut zu testen.

## Jetzt bist du dran eine Variante für Partner-Level-Consultants zuschreiben
Du bist den Meridian-Prompt mit uns durchgegangen. Wende nun dieselbe Logik auf eine leicht andere Version desselben Agenten an.
Die Meridians Führung möchte eine separate Variante dieses Agenten nur für Partner-Level-Consultants. Die Partner brauchen zusätzlichen Zugriff: Sie können Fragen zu Prospective-Client-Pipelines und Pricing Strategy stellen. Das sind Bereiche, die der reguläre Agent ablehnen muss.
Schreibe den System-Prompt für diese Partner-Level-Variante um:
- Behalte dieselbe Rolle und Persona bei.
- Erweitere den Scope, sodass Prospective-Client-Pipelines und Pricing Strategy explizit enthalten sind.
- Passe die Grenzen an, sodass diese Bereiche nicht mehr abgelehnt werden, rechtliche und HR-Themen aber weiterhin außerhalb des Scopes bleiben.
Gib deinen Partner-Varianten-Prompt in den Canvas ein (als Ersatz für die vorherige Version), speichere und teste ihn mit einer Anfrage, die jetzt im Scope liegen sollte („Give me the current pipeline status for prospective client X“), und einer, die weiterhin abgelehnt werden sollte (eine beliebige rechtliche oder HR-Anfrage).

## Checkpoints
Bevor du weitermachst, gehe diese Punkte durch:
1. Rollenklarheit: Lies deinen finalen Prompt laut vor, als wärst du der Agent, der ihn zum ersten Mal erhält. Ist sofort offensichtlich, wer du bist und wie du kommunizieren solltest?
1. Scope-Spezifität: Könnte ein Meridian-Berater nur durch Lesen deines Prompts vorhersagen, ob eine bestimmte Frage im Scope liegt oder außerhalb davon? Falls nicht, ist der Scope noch zu vage.
1. Eskalationsverhalten: Als dein Agent die Out-of-Scope-Anfrage im Test abgelehnt hat, hat er erklärt, warum, und eine Weiterleitung angeboten? Oder hat er einfach gestoppt?
1. Länge und Klarheit: Der Bereich von vier bis acht Sätzen ist eine Orientierung, keine harte Regel. Wenn dein Prompt länger ist, aber jeder Satz Gewicht hat, ist das in Ordnung. Wenn er sechs Sätze hat, aber zwei davon dasselbe sagen, kürze ihn.

> 💡 Takeaway: 
  Ein System-Prompt ist die wichtigste einzelne Konfigurationsentscheidung in einem Business-Agenten. Ihn gut zu schreiben ist keine kreative Übung. Er ist eine Stellenbeschreibung für den Agenten, und es gelten dieselben Regeln. Vage Stellenbeschreibungen erzeugen inkonsistente Mitarbeitende. Vage System-Prompts erzeugen inkonsistente Agenten.
  Eine spezifität in der Rolle, des Scope und der Grenzen gibt dir Vorhersagbarkeit zurück. Und die Zeit, die du investierst, um den Prompt vor dem Testen richtig hinzubekommen, ist immer geringer als die Zeit, die du später mit dem Debugging unerwarteten Verhaltens nach dem Deployment verbringen würdest.
