# Nachrichtenweitergabe und Handoff-Verträge

Notion page: https://app.notion.com/p/Nachrichtenweitergabe-und-Handoff-Vertr-ge-ffb9418319f3837e89de01d87df3bbcb
Backed up before n8n migration

Nach dem Schema-Mismatch, der den Garantie-Handoff beschädigt hat, beginnt Sofia noch einmal mit einem ordentlichen Vertrag. Bevor sie das vollständige Support-System von Cascadia neu baut, möchte sie den kleinstmöglichen Handoff bauen, der funktionieren könnte: zwei Agenten in Flowise Agentflow V2, mit geteiltem Flow State, der die Absicht und das Reasoning vom ersten Agenten zum zweiten weitergibt.
In diesem Walkthrough baust du genau das. Ein Intake-Agent klassifiziert eine Kundennachricht und schreibt drei Schlüssel in Flow State: die Absicht des Kunden, eine einzeilige Zusammenfassung und einen Grund für den Handoff. Ein Specialist-Agent liest diese Schlüssel und antwortet auf ihrer Grundlage, ohne die ursprüngliche Nachricht erneut zu analysieren. Das ist das kleinste konkrete Beispiel für den Kommunikationsvertrag, den die vorherige Lektion beschrieben hat.
Jeder Multi-Agent-Handoff braucht eine gemeinsame Memory-Ebene, damit Agent B weiß, was Agent A getan hat. Agentflow V2 bietet ein implizites Execution-Thread-Memory sowie einen expliziten globalen Kontext namens Flow State ($flow.state).
- Start-Node-Initialisierung: Ganz am Anfang deiner Canvas muss der Start-Node die Key-Value-Paare (das Vertragsschema), auf die spätere Agenten zugreifen oder die sie aktualisieren, explizit deklarieren und initialisieren.
- Zustandsaktualisierungen (Überschreiben vs. Anhängen): Wenn Daten durch einen Node laufen, kannst du konfigurieren, wie eine Variable aktualisiert wird:
◦ Replace: Überschreibt die Variable (z. B. Aktualisierung von ticket_status oder current_summary).
◦ Append: Wandelt die Variable in ein Array um oder hängt etwas daran an (ideal, um Roh-JSON-Logs oder mehrstufige Analysen über mehrere Agenten hinweg zu sammeln).
Ein robuster Handoff-Vertrag garantiert, dass bei der Übergabe der Ausführung von Agent A an Agent B alle kritischen Informationen (z. B. Absicht, verifizierte Parameter, Roh-Logs) sauber im Graph-Flow gebündelt sind.
## Der Workflow, den du baust
Du baust die kleinste Version von Cascadias Support-Triage: einen Intake-Agent, der eingehende Nachrichten klassifiziert, und einen Specialist-Agent, der den Billing-Branch bearbeitet.
Der Intake-Agent liest die Nachricht eines Kunden und extrahiert das Hauptproblem. Der Specialist-Agent nutzt diesen extrahierten Kontext, um eine fokussiertere Antwort zu schreiben, ohne zum ursprünglichen Nachrichtentext zurückzugehen.
So sieht der Flow aus:
![image]((notion-hosted file))
Das ist ein einfaches Muster für Nachrichtenweitergabe: Der erste Agent bereitet nur den Kontext vor, die endgültige Antwort liefert der zweite Agent.
## Schritt 1: Einen neuen Agentflow-V2-Flow erstellen
Öffne Flowise und erstelle einen neuen Agentflow-V2-Workflow.
![image]((notion-hosted file))
Du kannst ihn Customer Support Triage nennen.
![image]((notion-hosted file))
Der Start-Node steht für den Beginn der Unterhaltung und ist auch der Ort, an dem du den geteilten Zustand definierst, den spätere Nodes verwenden.
Such im Start-Node den Bereich Flow State und leg diese Variablen an:
```json
{ "customer_intent": "", 
	"issue_summary": "", 
	"handoff_reason": "" }
```
![image]((notion-hosted file))
Klick auf Add Flow State, um Variablen zu aktualisieren:
![image]((notion-hosted file))
Diese Variablen sind der Handoff-Vertrag. Sie definieren, was Agent A vorbereiten muss, bevor Agent B fortfahren kann.
> ☝ Bevor du weitermachst, prüf, dass die Variablen im Start-Node existieren und als leere Strings initialisiert sind.
## Schritt 2: Agent A als Intake-Agent hinzufügen
Füg nach dem Start-Node einen Agent-Node hinzu. Da dieser Agent keine Tools braucht, kannst du auch einen LLM-Node wählen. Nenn ihn Intake Agent.
> ☝ Für diese Aufgabe nimmst du am besten ein Gemini- oder OpenAI-LLM, weil lokale Modelle wie Ollama oft keine strukturierte Ausgabe erzeugen. Es gibt einen Workaround über eine Custom Function, die die nötige Struktur zurückgibt, aber der Einfachheit halber nutzt du hier Gemini-Modelle.
Verbinde den Start-Node mit dem Intake Agent.
![image]((notion-hosted file))
Gib dem Intake Agent diese Rolle als System-Nachricht, indem du auf Add Message klickst:
![image]((notion-hosted file))
> 💬 You are an Intake Agent for Cascadia Outfitters' customer support workflow. Your job is not to solve the customer's problem fully. Your job is to analyze the customer's request and prepare a clear handoff for the next agent. Identify:
  - the customer’s main intent with one word (billing, charged, payment, invoice, subscription, other)
  - a short summary of the issue
  - why this case should be handed off to a specialist
  - Return your answer in this structure
  {
  "customer_intent": "",
  "issue_summary": "",
  "handoff_reason": ""
  }
![image]((notion-hosted file))
Führ einen kurzen Test mit dieser Nutzernachricht aus:
> 💬 Meine Subscription wurde diesen Monat zweimal berechnet. Kann mir jemand helfen, das zu beheben?
Erwartetes Ergebnis: Der Intake Agent sollte ein Problem im Zusammenhang mit der Subscription erkennen und es klar zusammenfassen.
![image]((notion-hosted file))
## Schritt 3: Die Ausgabe im JSON-Format speichern
Um Flow State zu aktualisieren und Variablen korrekt zuzuordnen, erstellst du zuerst eine strukturierte Ausgabe aus dem Agenten. Klick auf JSON Structured Output und füg Variablen hinzu:
![image]((notion-hosted file))
Das ist die Ausgabe des Agenten. Sie ist noch nicht mit Flow State verbunden, das ordnest du im nächsten Schritt zu. Jedes Feld sollte ein String sein, und du kannst für jedes eine kurze Beschreibung ergänzen.
## Schritt 4: Die Ausgabe des Intake Agent in Flow State speichern
Konfigurier den Intake Agent jetzt so, dass seine Ausgabe Flow State aktualisiert.
Ordne das Ergebnis des Agenten den Variablen zu, die du zuvor erstellt hast:
```json
customer_intent → billing 
issue_summary → user says they were charged twice for the subscription 
handoff_reason → billing specialist needed
```
Öffne deine Agentenkonfiguration erneut und aktualisier Flow State:
![image]((notion-hosted file))
Ordne die Ausgabe des Agenten zu, um den Zustand zu aktualisieren:
![image]((notion-hosted file))
Hier ist output die Ausgabe des Agenten.
## Schritt 5: Agent B als Specialist-Agent hinzufügen
Füg nach dem Intake Agent einen zweiten Agent-Node hinzu. Nenn ihn Specialist Agent. Wie beim vorherigen kann das auch ein LLM-Node sein.
Verbinde den Intake Agent mit dem Specialist Agent.
![image]((notion-hosted file))
Der Specialist Agent baut auf dem Handoff-Vertrag auf, den Agent A erstellt hat, statt bei null anzufangen.
Nutz diesen Prompt als Systemnachricht:
> 💬 A previous intake agent has already analyzed the user request. Do not repeat the intake process and do not ask for information that is already available. Use this handoff context: Customer intent: {{$flow.state.customer_intent}} Issue summary: {{$flow.state.issue_summary}} Handoff reason: {{$flow.state.handoff_reason}} Now write a helpful, focused response to the customer.
Führ dieselbe Testnachricht erneut aus.
> 💬 Meine Subscription wurde diesen Monat zweimal berechnet. Kann mir jemand helfen, das zu beheben?
Erwartetes Ergebnis: Der Specialist Agent sollte antworten, als wäre der Fall bereits triagiert worden.

![image]((notion-hosted file))
## Schritt 6: Eine einfache Routing-Entscheidung hinzufügen
Mach den Handoff jetzt realistischer.
Füge zwischen dem Intake Agent und dem Specialist Agent einen Condition-Node hinzu. Gib ihm einen passenden Titel.
![image]((notion-hosted file))
Der Condition-Node sollte prüfen, ob das Problem Billing-bezogen ist. Wir prüfen den Flow-State-Wert in customer_intent.

![image]((notion-hosted file))
Du kannst den zweiten Branch hinzufügen, der mit einem Direct-Reply-Node verbunden ist.
Dort kannst du folgende Ausgabe hinzufügen:
> 💬 Thank you for reaching out. Based on the information provided, your request does not appear to be related to billing.
  To ensure your inquiry is handled by the most appropriate team, we have forwarded it to the relevant specialist. They will review your case and get back to you as soon as they become available.
  Thank you for your patience and understanding.
![image]((notion-hosted file))
Und dein finaler Agent Flow sollte so aussehen:
![image]((notion-hosted file))
Pass den Prompt in deinem Specialist Agent an, da er jetzt nur noch für Billing-Probleme zuständig ist:
> 💬 You are a Billing Specialist Agent.
  You ONLY handle billing-related issues such as:
  - double charges
  - payment failures
  - invoices
  - subscription billing
  - refunds
  - account charges
  A previous Intake Agent has already analyzed the request and prepared a handoff for you.
  Use the following handoff information:
  Customer Intent:
  {{ $flow.state.customer_intent }}
  Issue Summary:
  {{ $flow.state.issue_summary }}
  Handoff Reason:
  {{ $flow.state.handoff_reason }}
  Instructions:
  - Assume the intake analysis is correct.
  - Do not repeat the intake process.
  - Do not ask for information that is already available in the handoff.
  - Focus only on resolving the billing issue.
  - If additional information is needed, ask concise follow-up questions.
  - Provide a clear explanation and next steps.
  - If the issue is not billing-related, politely state that it falls outside your scope.
  Response structure:
  Issue Assessment:
  [brief explanation of the billing issue]
  Recommended Action:
  [specific next step]
  Additional Information Needed:
  [question(s) if required, otherwise "None"]
## Schritt 7: Den Handoff-Vertrag testen
Nutz diesen Test-Prompt:
```plain text
My invoice says I paid for the Pro plan, but my account still shows the Basic plan.
```
Prüf drei Dinge:
Erstens sollte der Intake Agent die Absicht korrekt erkennen.
Zweitens sollte Flow State den extrahierten Handoff-Kontext enthalten.
Drittens sollte der Specialist Agent diesen Kontext verwenden, statt alles von Grund auf neu zu analysieren.
## Zusammenfassung
Du hast einen einfachen Zwei-Agenten-Handoff in Flowise Agentflow V2 gebaut. Der erste Agent hat die Nutzeranfrage analysiert, nützlichen Kontext in Flow State gespeichert und die Kontrolle über den Graphen an den nächsten Agenten weitergegeben. Der zweite Agent hat diesen Kontext genutzt, um eine fokussiertere Antwort zu erzeugen.
Das ist die Grundlage vorhersehbarer Multi-Agent-Koordination: Agenten übergeben strukturierten Kontext über einen expliziten Handoff-Vertrag, statt eine Unterhaltung blind fortzusetzen.
