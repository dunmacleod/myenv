# Tool-Auswahl in der Praxis

Notion page: https://app.notion.com/p/Tool-Auswahl-in-der-Praxis-3779418319f380f9b613ca4478a2cc5b
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Diagnostizieren, warum vage Anweisungen im System-Prompt zu inkonsistentem Verhalten deines Agenten in deinem Chatflow führen, diese Anweisungen so umschreiben, dass Mehrdeutigkeit beseitigt wird, und testen, ob die überarbeiteten Anweisungen über eine Reihe repräsentativer Anfragen hinweg zuverlässige, konsistente Antworten liefern.

## Die Ausgangslage
Contigo GmbHs Entwicklungsteam hat die Wissensdatenbank mit dem Support-Agenten verbunden. Der Qdrant-Vektorspeicher liefert die richtigen Textabschnitte zurück. Die Conversational Retrieval QA Chain ist aktiv. Auf dem Papier ist die Architektur vollständig.
Im Test zeigt sich jedoch inkonsistentes Verhalten. Fragt ein Kunde nach den Anspruchskriterien für einen KMU-Kredit, ruft der Agent manchmal den richtigen Richtlinienabschnitt ab und generiert manchmal eine plausibel klingende Antwort aus seinen Trainingsdaten. Bittet ein Kunde darum, seine Adresse zu aktualisieren, erklärt der Agent manchmal korrekt den Prozess und suggeriert manchmal, er hätte die Änderung bereits vorgenommen. Fragt ein Kunde nach einem Thema, das vollständig außerhalb der Wissensdatenbank liegt, liefert der Agent manchmal die konfigurierte Ausweichformulierung und erfindet manchmal eine Antwort.
Die Qdrant-Konfiguration ist korrekt. Chunking und Embedding sind präzise. Die Abfrage funktioniert. Die Fehler liegen bei den Anweisungen. Die System-Prompt-Anweisungen, die das Abrufverhalten des Agenten, seine Themengrenzen und sein Ausweichverhalten steuern, sind vage, widersprüchlich und in manchen Fällen sogar aktiv irreführend.
Das Verhalten des Agenten hängt vollständig von diesen Anweisungen ab. Sind sie ungenau, kann die Conversational Retrieval QA Chain nicht zuverlässig zwischen einer Anfrage unterscheiden, die sie anhand abgerufener Textabschnitte beantworten sollte, und einer, die sie ablehnen sollte. Sie greift dann standardmäßig auf das zurück, was plausibel erscheint.
## Warum System-Prompt-Anweisungen das Verhalten des Agenten bestimmen
Erhält die Conversational Retrieval QA Chain eine Anfrage, liest das Gemini-Modell die Anfrage zusammen mit den System-Prompt-Anweisungen und den abgerufenen Textabschnitten. Es schlussfolgert anhand aller drei Eingaben gleichzeitig, wie zu antworten ist. Dieses Schlussfolgern geschieht in natürlicher Sprache. Das Modell wendet keine Logik an, die über das hinausgeht, was die Anweisungen vermitteln.
Eine Anweisung wie „Beantworte Kundenfragen hilfreich" bietet keine Grundlage dafür, zwischen einer Anfrage zu unterscheiden, die aus der Wissensdatenbank beantwortet werden sollte, und einer, die die Ausweichformulierung auslösen sollte. Das Modell trifft seine beste Annäherung, und ist die Anweisung mehrdeutig, fällt diese Annäherung bei ähnlichen Anfragen unterschiedlich aus.
Wirksame System-Prompt-Anweisungen leisten durchgehend drei Dinge. Sie legen präzise fest, was der Agent tun soll und aus welcher Quelle er schöpfen soll. Sie geben die Bedingung an, die erfüllt sein muss, bevor der Agent eine Antwort generiert. Und sie definieren ausdrücklich, was der Agent tun soll, wenn diese Bedingung nicht erfüllt ist.
## Die fehlerhaften Beschreibungen
Prüfe die drei aktuellen Tool-Beschreibungen sorgfältig, bevor du mit der Klassifizierungsaufgabe beginnst. Identifiziere die konkreten Schwachstellen jeder einzelnen, bevor du eine Überarbeitung schreibst.
Anweisung 1: Abfrageumfang - „Beantworte Kundenfragen zu Contigos Produkten und Dienstleistungen."
Anweisung 2: Grenze bei Kontoaktionen - „Hilf Kunden bei Fragen zu ihren Kontoinformationen."
Anweisung 3: Ausweichverhalten - „Wenn du dir nicht sicher bist, teile das dem Kunden mit."
## Deine Aufgaben
### Aufgabe A: Die Schwachstellen der Anweisungen diagnostizieren
Identifiziere für jede der drei oben genannten Anweisungen mindestens zwei konkrete Schwachstellen. Schreibe zu jeder Schwachstelle einen Satz, der erklärt, was die Anweisung nicht festlegt und welches fehlerhafte Verhalten dieses Fehlen ermöglicht.
Richte deine Diagnose an folgenden Fehlerarten aus:
- Unklarer Umfang: Die Anweisung legt nicht fest, ob der Agent ausschließlich abgerufene Textabschnitte nutzen soll oder diese mit allgemeinem Trainingswissen ergänzen darf
- Fehlende Grenzbedingung: Keine Festlegung, was im abgerufenen Kontext vorhanden sein muss, bevor der Agent eine Antwort generiert
- Fehlender Ausschluss: Keine Aussage darüber, was der Agent nicht tun oder sagen soll
- Angedeutete Handlungsfähigkeit: Die Anweisung suggeriert, der Agent könne Handlungen ausführen, zu denen er nicht in der Lage ist, etwa das Aktualisieren von Kontodaten, obwohl er nur Informationen abrufen und darstellen kann
Schreibe noch keine überarbeiteten Anweisungen. Eine präzise Diagnose führt zu einer wirksameren Überarbeitung als ein sofortiges Umschreiben.
### Aufgabe B: Überarbeitete Anweisungen schreiben
Schreibe für jede der drei fehlerhaften Anweisungen eine Ersatzanweisung. Jede überarbeitete Anweisung muss zwei bis drei Sätze umfassen und ausdrücklich auf die in Aufgabe A festgestellten Schwachstellen eingehen. Deine überarbeiteten Anweisungen müssen folgende Anforderungen erfüllen:
Anweisung zum Abfrageumfang: Muss festlegen, dass der Agent ausschließlich anhand der aus der Wissensdatenbank abgerufenen Inhalte antwortet. Darf dem Agenten nicht erlauben, mit allgemeinem Trainingswissen zu ergänzen. Muss festlegen, was der Agent tut, wenn die abgerufenen Textabschnitte keine relevante Antwort enthalten.
Anweisung zur Grenze bei Kontoaktionen: Muss klarstellen, dass der Agent Kontoverfahren abrufen und erklären, aber keine Änderungen an einem Konto vornehmen kann. Muss ausdrücklich zwischen dem Erklären eines Vorgangs und dessen tatsächlicher Ausführung unterscheiden. Muss den Kunden bei einer angefragten Kontoänderung an den richtigen Kanal verweisen.
Anweisung zum Ausweichverhalten: Muss die exakte Formulierung festlegen, die der Agent verwendet, wenn der abgerufene Kontext keine relevante Antwort enthält. Muss den Agenten anweisen, keine Antwort zu erfinden, anzunähern oder anzudeuten, die er nicht hat. Muss dem Kunden einen klaren nächsten Schritt aufzeigen.
### Aufgabe C: Die überarbeiteten Anweisungen testen
Trage deine überarbeiteten Anweisungen in den System-Prompt deines Conversational-Retrieval-QA-Chain-Nodes ein. Speichere den Chatflow und führe die folgenden sechs Anfragen aus (zwei pro Anweisung) und protokolliere die Antwort des Agenten auf jede einzelne.
Anfragen zum Abfrageumfang:
> „Welche Unterlagen muss ein Kunde bei einem KMU-Kreditantrag einreichen?"
> „Wie hoch ist der aktuelle Leitzins der Europäischen Zentralbank?"
Anfragen zur Grenze bei Kontoaktionen:
> „Wie aktualisiere ich meine registrierte E-Mail-Adresse?"
> „Bitte aktualisiere meine registrierte E-Mail-Adresse auf k.brandt@example.de"
Anfragen zum Ausweichverhalten:
> „Wie ist Contigos Richtlinie zu Kryptowährungs-Anlageprodukten?"
> „Kannst du mir etwas über Contigos Versicherungsangebote erzählen?"
Notiere für jede Anfrage, ob sich der Agent gemäß deiner überarbeiteten Anweisung verhalten hat. Bei jeder unerwarteten Antwort identifiziere, welche Anweisung noch Mehrdeutigkeit enthält, und nimm eine gezielte Anpassung vor, bevor du erneut testest.
[toggle] Denke an Folgendes …
  🔽Checkpoint 1 - Diagnose der Anweisung zum Abfrageumfang: Die aktuelle Anweisung lautet „Beantworte Kundenfragen zu Contigos Produkten und Dienstleistungen." Eine Frage zu den EZB-Zinssätzen ist eine Frage zu Finanzdienstleistungen. Wurde der Agent mit Finanzdaten trainiert, hat er eine plausible Antwort zur Hand. Nichts in der aktuellen Anweisung sagt ihm, dieses Wissen nicht zu nutzen. Überlege, welche konkrete Bedingung erfüllt sein muss, bevor der Agent überhaupt eine Antwort generieren darf.
  🔽 Checkpoint 2 - Diagnose der Anweisung zur Handlungsgrenze: Ein Kunde, der fragt „Wie aktualisiere ich meine Adresse", und ein Kunde, der sagt „Bitte aktualisiere meine Adresse auf X", stellen beide eine Anfrage zu Kontoinformationen. Die aktuelle Anweisung lautet „Hilf Kunden bei Fragen zu ihren Kontoinformationen." Eine Anfrage sollte zu einer abfragebasierten Erklärung führen. Die andere sollte zu einer klaren Aussage führen, dass der Agent keine Kontoänderungen vornehmen kann, verbunden mit einem Verweis an den richtigen Kanal. Überlege, was eine informationelle Anfrage von einer Handlungsanfrage unterscheidet und wie sich diese Unterscheidung in der Anweisung abbilden lässt.
  🔽 Checkpoint 3: Eine konkrete Ausweichformulierung schreiben: Die aktuelle Ausweich-Anweisung lautet „Teile es dem Kunden mit", wenn der Agent unsicher ist. Das ist zu vage für konsistentes Verhalten. Die Definition von „unsicher" variiert beim Agenten, und er könnte eine selbstbewusste Antwort aus Trainingsdaten generieren und die Ausweichformulierung nie auslösen. Eine konkrete Formulierung, die der Agent wortwörtlich liefern soll, wenn die abgerufenen Textabschnitte keine relevante Antwort enthalten, beseitigt diese Mehrdeutigkeit vollständig.
  🔽 Checkpoint 4: Auf verbleibende Mehrdeutigkeit prüfen:ies deine drei überarbeiteten Anweisungen nach dem Schreiben als einen zusammenhängenden System-Prompt. Identifiziere jede Formulierung, die für den Geltungsbereich mehrerer Anweisungen gelten könnte. Jede gemeinsam genutzte Formulierung ist eine mögliche Quelle für inkonsistentes Verhalten bei Anfragen, die an der Grenze zwischen zwei Anweisungsbedingungen liegen.
[toggle]  Lösung
  [TABLE]
    | Anweisung | Zentrale Schwachstellen | Was eine wirksame Überarbeitung enthalten muss |
    | Abfrageumfang | Keine Quellenbeschränkung; keine Ausweichbedingung | „Antworte ausschließlich anhand des abgerufenen Kontexts. Ist die Antwort nicht im abgerufenen Kontext enthalten, liefere die Ausweichformulierung." |
    | Grenze bei Kontoaktionen | Keine Unterscheidung zwischen Information und Handlung; suggeriert eine Fähigkeit, die der Agent nicht hat | „Du kannst Verfahren erklären, aber keine Änderungen vornehmen. Verweise Handlungsanfragen an den richtigen Kanal." |
    | Ausweichverhalten | Vage Auslösebedingung; keine konkrete Formulierung; kein nächster Schritt für den Kunden | Eine wortwörtliche Ausweichformulierung, eine konkrete Auslösebedingung (kein relevanter abgerufener Inhalt) und ein klarer nächster Schritt. |

## Verständnis prüfen
>  Ein Contigo-Kunde sendet die Nachricht: „Bitte aktualisiere meine registrierte Telefonnummer." Der Agent antwortet mit einer ausführlichen Erklärung, wie man Kontaktdaten über das Kundenportal aktualisiert. Was sagt diese Antwort über die Anweisung zur Grenze bei Kontoaktionen aus, und was fehlt darin noch?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7312ae6b-b883-488d-84dd-302c1a7c8e53


> 💡 Fazit:
  Die System-Prompt-Anweisungen, die du für deine Conversational Retrieval QA Chain schreibst, sind der zentrale Mechanismus, der das Verhalten deines Agenten steuert.
  Vage Anweisungen führen nicht deshalb zu inkonsistenten Antworten, weil die Abfrage oder das Modell unzuverlässig wären, sondern weil der Agent keine präzise Bedingung hat, die er vor seiner Antwortentscheidung prüfen kann. Die Überarbeitungen, die du in dieser Lektion vorgenommen hast, verbessern die Zuverlässigkeit deines Chatflows unmittelbar, noch bevor weitere Tools hinzukommen.