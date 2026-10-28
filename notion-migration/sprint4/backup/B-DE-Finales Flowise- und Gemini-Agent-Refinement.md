# Finales Flowise- und Gemini-Agent-Refinement

Notion page: https://app.notion.com/p/Finales-Flowise-und-Gemini-Agent-Refinement-3789418319f38092aeb2e5f36bfad5bf
Backed up before n8n migration

> 💡 Woran du in dieser Lektion arbeiten wirst: Du diagnostizierst drei production-blocking Failures anhand von Execution Evidence und wendest gezielte Fixes auf Model-Konfiguration, Tool Descriptions und System Prompt an.
  Das machst du in dieser Lektion: Du diagnostizierst anhand der Ausführungsspuren drei Fehler, die den Produktivbetrieb blockieren, und behebst sie gezielt in der Modellkonfiguration, den Tool-Beschreibungen und im System-Prompt.

## Die Ausgangslage
Der interne Agent von Meridian Consulting hat das Sicherheits-Review bestanden und steht jetzt vor der letzten Feinschliffphase vor der Stakeholder-Präsentation. Das Canvas ist konfiguriert. Die vier Sicherheitsebenen sind verstanden. Unter idealen Bedingungen verhält sich der Agent korrekt.
Ein Stresstest vor dem Launch, der einen kompletten Arbeitstag des Consulting-Teams simuliert hat, hat drei Fehler aufgedeckt. Bei allen dreien lässt sich die Ursache klar in den Ausführungsspuren erkennen. Für alle drei gibt es gezielte Fixes, die kein Neubauen des Canvas erfordern. Deine Aufgabe ist es, jede Ursache zu identifizieren und den passenden Fix unabhängig davon umzusetzen.
## Die drei Fehler aus dem Stresstest
### Fehler 1: Latenz und Kosten
Im Stresstest lag die durchschnittliche Antwortzeit bei 18 Sekunden pro Anfrage. Die Token-Kosten pro Session lagen bei rund 0,94 €. Hochgerechnet auf Meridians erwartetes Volumen von 1.000 Sessions im Monat sind das 940 € pro Monat.
Ein Blick in den Agent Node zeigt, welches Modell für jede Interaktion eingestellt ist. Das gilt auch für einfache Begrüßungen, Status-Bestätigungen und kurze Folgeantworten, die kein komplexes Reasoning brauchen.
### Fehler 2: Blockierte Tool-Aufrufe
Im Stresstest wurden elf Anfragen nach dem Engagement-Status falsch geroutet. Statt den HTTP-Node für eine Live-Abfrage aufzurufen, gab der Agent eine generische Antwort aus der Wissensdatenbank zurück. Ein Blick in die Konfiguration des Agent Node zeigt, dass das Feld „Describe Knowledge" aktuell so lautet:
> "Nutze das, um Fragen zu Meridians internen Prozessen und Engagements zu beantworten."
Die Tool-Beschreibung des HTTP-Node lautet:
> "Nutze dieses Tool, um bei Engagement-bezogenen Anfragen zu helfen."
Beide Beschreibungen verwenden das Wort „Engagement". Semantisch kann der Agent die beiden nicht unterscheiden und greift standardmäßig auf die Wissensdatenbank zurück.
### Fehler 3: Halluzination bei Tool-Fehlern
In drei Testsessions gab der HTTP-Node einen 504-Timeout-Fehler zurück. In allen drei Fällen ignorierte der Agent den Fehler und erfand einen Engagement-Status, komplett mit Phasennamen und Meilenstein-Terminen, die in keiner zurückgegebenen Antwort vorkamen. Ein Blick in den System-Prompt des Agent Node zeigt, dass keine Anweisung existiert, die regelt, was der Agent tun soll, wenn der HTTP-Node einen Fehlercode zurückgibt. Der Agent griff standardmäßig auf seine allgemeine Hilfsbereitschaft zurück und füllte die Informationslücke mit einer plausibel klingenden Erfindung.
## Deine Aufgaben
### Aufgabe A: Fehler 1 beheben - Modelloptimierung
Konfiguriere das Modell im Agent Node neu, um das Latenz- und Kostenproblem zu lösen. Dokumentiere deine Lösung und gehe dabei auf Folgendes ein:
- Auf welches Gemini-Modell du wechselst und warum es zu Meridians typischen Consulting-Anfragen passt
- Wie sich die Kosten pro Monat bei 1.000 Sessions voraussichtlich verändern, basierend auf dem relativen Unterschied bei den Token-Kosten zwischen gemini-3.1-flash-lite und deinem gewählten Modell
- Beschreibe in zwei bis drei Sätzen deine Konfigurationsänderung und die erwartete Auswirkung auf den Betrieb
> ➡️ Checkpoint: Meridians Anfragen brauchen vor allem schnelles Retrieval und eine saubere Darstellung fundierter Ergebnisse. Frag dich: Könnte eine kompetente Person diese Anfrage korrekt beantworten, nachdem sie den abgerufenen Inhalt einmal gelesen hat? Wenn ja, brauchst du kein Frontier-Reasoning-Modell. Sieh dir vor deiner Entscheidung den Gemini-Modellvergleich an.

### Aufgabe B: Fehler 2 beheben - Wissensdatenbank-Beschreibung und Tool-Beschreibung schärfen
Schreibe sowohl das Feld „Describe Knowledge" in der Knowledge-Konfiguration des Agent Node als auch die Tool-Beschreibung des HTTP-Node neu, um die Routing-Mehrdeutigkeit zu beseitigen, die zu den elf fehlgeschlagenen Aufrufen geführt hat. Beide überarbeiteten Beschreibungen müssen diese Anforderungen erfüllen:
- Feld „Describe Knowledge": Beschreibe genau, welche dokumentierten Inhalte die Wissensdatenbank enthält. Mach klar, dass sie statische interne Richtlinien, Prozesse und Vorgaben abdeckt. Länge: zwei bis drei Sätze.
- Tool-Beschreibung des HTTP-Node: Beschreibe genau, welche Live-Daten das Tool zurückgibt. Nenne die konkrete Bedingung, die erfüllt sein muss, bevor das Tool aufgerufen wird, zum Beispiel eine konkrete Account-Referenz oder eine explizite Anfrage nach dem aktuellen Live-Status. Grenze das Tool klar von der Wissensdatenbank ab. Länge: zwei bis drei Sätze.
> ➡️ Checkpoint: Die Routing-Fehler sind entstanden, weil beide Beschreibungen eine Sprache verwendet haben, die auf dieselbe Anfrage passen konnte. Schau dir an, was ein Live-API-Aufruf strukturell braucht, das eine Dokumentenabfrage nicht braucht. Eine Anfrage mit „account 1" oder einer Account-Referenz ist strukturell etwas anderes als eine allgemeine Frage zu einer Richtlinie. Bau die Aufrufbedingung um genau dieses Signal herum.

### Aufgabe C: Fehler 3 beheben - Anweisung zur Fehlerbehandlung
Schreib eine Ergänzung von zwei bis drei Sätzen für den System-Prompt des Agent Node, die festlegt, wie sich der Agent verhält, wenn der HTTP-Node einen Fehlercode zurückgibt.
Deine Anweisung muss alle drei Anforderungen erfüllen:
- Keine Erfindungen: Der Agent darf keinen plausiblen Status generieren, wenn der HTTP-Node keinen zurückgegeben hat
- Ehrliche Rückmeldung: Der Consultant muss verstehen, dass die Information gerade nicht verfügbar ist
- Konkreter nächster Schritt: Der Agent muss eine konkrete Alternative anbieten und den Consultant nicht ohne Lösung stehen lassen
> ➡️ Checkpoint: Eine vage Anweisung wie „Rate nicht" sagt dem Agenten, was er nicht tun soll, lässt aber offen, was er stattdessen tun soll. Ein probabilistisches Modell tendiert von sich aus zur Hilfsbereitschaft und erzeugt trotzdem eine plausible Fortsetzung. Schreibst du die genaue Fallback-Formulierung direkt in die Anweisung, hat der Agent eine konkrete Ausgabe, die er produzieren kann. Baue drei Elemente ein: die Information als nicht verfügbar kennzeichnen, keinen Eindruck erwecken, dass ein Ergebnis gefunden wurde, und den Consultant zu einem konkreten nächsten Schritt weiterleiten.

### Aufgabe D: Alle drei Fixes testen
Teste jedes Fehlerszenario einzeln. Kombiniere sie nicht in einer einzigen Session. Sonst kannst du nicht mehr isolieren, welcher Fix noch nicht funktioniert.
Test für Fix 1 - Schick eine einfache Begrüßung: Hello, I am preparing for a client meeting this afternoon
- Vergleiche die Antwortzeit mit der ursprünglichen Baseline von 18 Sekunden vor dem Fix.
- Bestätige, dass sich das im Agent Node angezeigte Modell geändert hat.
Test für Fix 2 - Schick eine Anfrage mit einer konkreten Account-Referenz: Can you check the current engagement status for account 1?
- Bestätige, dass der Flow zum HTTP-Node routet und nicht Inhalte aus der Wissensdatenbank zurückgibt.
Test für Fix 3 - Ändere die URL des HTTP-Node vorübergehend auf einen ungültigen Endpunkt: https://jsonplaceholder.typicode.com/invalid/9999
- Schick: Can you check the engagement status for the Krauss account?
- Bestätige, dass der Agent deine konfigurierte Fallback-Formulierung ausgibt, ganz ohne erfundene Engagement-Details.
- Stell nach dem Testen die richtige URL wieder her: https://jsonplaceholder.typicode.com/todos/1
## Verständnischeck
>  Meridians Agent bekommt vom Engagement-Status-Tool einen 504-Timeout und antwortet: "The ENG-1041 engagement is currently in active delivery with a Q3 milestone review scheduled."  Das Tool hat diesen Status nie zurückgegeben. Welche System-Prompt-Anweisung hätte diese konkrete Antwort am zuverlässigsten verhindert?

  [EMBED] https://app.masterschool.com/campus/multi-choice-question/b7bf43f1-e18b-49e3-838e-daa0917e349e

> 💡 Fazit:
  Beim Feinschliff in Produktion geht es darum, Fehlerarten aus dem System zu entfernen. Die drei Fixes aus dieser Lektion, Modelloptimierung, präzisere Beschreibungen und eine Anweisung zur Fehlerbehandlung, adressieren jeweils einen konkreten, belegten Fehler aus den Ausführungsspuren. Gezielte Fixes auf Basis von Trace-Daten sind deutlich zuverlässiger als iteratives Prompt-Tweaking nach Bauchgefühl.
