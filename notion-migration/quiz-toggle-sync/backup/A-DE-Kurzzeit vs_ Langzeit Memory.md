# Kurzzeit vs. Langzeit Memory

Notion page: https://app.notion.com/p/Kurzzeit-vs-Langzeit-Memory-3779418319f380158a0af7f2776522ac
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Den Unterschied zwischen Kurzzeit-Memory (Session Memory) und Langzeit-Memory (Persistent Memory) und weißt, wann beide beim Entwurf eines Business-Agenten eingesetzt werden.

## Eine andere Art des Vergessens
Der Support-Agent der Contigo GmbH hat jetzt Memory konfiguriert. Innerhalb eines einzelnen Gesprächs funktioniert er gut, indem er sich Kontonummern merkt, verfolgt, was besprochen wurde, und vermeidet, mitten in der Session Fragen zu wiederholen. Das Team betrachtet ihn als Erfolg.
Dann beginnen die Beschwerden von wiederkehrenden Kunden.
> Kunde 1: Ich habe meine bevorzugte Korrespondenzsprache schon vor drei Wochen angegeben, und jetzt musste ich sie erneut nennen.
> Kunde 2: Ein Kreditsachbearbeiter hat in einer früheren Session eine Dokumentenabweichung markiert, und jetzt gibt es im neuen Gespräch keine Spur davon.
> Kunde 3: Ein Kunde mit einer langen Beziehung zu Ihrem Unternehmen hat dutzende Male mit dem Agenten interagiert und wurde jedes Mal wie ein Fremder behandelt, wenn er zurückkehrt.
Der Agent ist nicht mehr zustandslos. Aber zwischen Sessions ist er amnesisch. Der Agent ist nicht mehr zustandslos. Das bedeutet, der Agent kann sich innerhalb einer Session erinnern, verliert dieses Wissen jedoch zwischen einzelnen Gesprächen. Das ist ein anderes Problem und erfordert eine andere Lösung.

## Kurzzeit-Memory: Was passiert innerhalb einer Session?
Kurzzeit-Memory, auch Session-Kontext oder Arbeitsgedächtnis genannt, speichert die Informationen aus dem aktuellen Gespräch. Während Nutzer und Agent Nachrichten austauschen, bleibt der bisherige Gesprächsverlauf im Kontextfenster (Context Window) des Modells verfügbar und wird bei jeder neuen Nachricht berücksichtigt. Dadurch kann das Modell Zusammenhänge erkennen, auf frühere Informationen Bezug nehmen und über mehrere Gesprächsschritte hinweg konsistent reagieren.
Dieses Memory ist ephemer – es bleibt also nur während der aktiven Session erhalten. Sobald das Gespräch endet, wird der gespeicherte Kontext verworfen. Beginnt der Nutzer später eine neue Unterhaltung, stehen diese Informationen nicht mehr zur Verfügung und werden nicht automatisch übernommen.
Kurzzeit-Memory ist das richtige Tool für Aufgaben, die nur innerhalb eines einzelnen Gesprächs Kontinuität erfordern: nachverfolgen, was bereits eingereicht wurde, einen mehrstufigen Prozess verwalten oder redundante Fragen mitten in der Session vermeiden. Es ist schnell, erfordert keine externe Infrastruktur und funktioniert in den meisten Agent-Frameworks direkt out of the box.

![image]((notion-hosted file))
## Langzeit-Memory: Was bleibt über Sessions hinweg erhalten?
Langzeit-Memory speichert Informationen über die Grenzen einer einzelnen Session hinaus. Statt sich auf das Context Window zu verlassen, schreibt Langzeit-Memory wichtige Fakten in eine externe Datenbank. Das kann eine relationale Datenbank, ein Vector Store oder ein schneller Key-Value Store sein. Wenn ein Nutzer zurückkehrt, fragt der Agent diese Datenbank ab, ruft relevante Informationen ab und injiziert sie in die neue Session, bevor das Gespräch beginnt.
Dadurch kann sich ein Contigo-Agent z.B. merken, dass ein bestimmter Kunde englische Korrespondenz bevorzugt, dass sein Konto im Februar zur Prüfung markiert wurde oder dass sein Kreditantrag derzeit bewertet wird.
Langzeit-Memory erfordert bewusste Designentscheidungen: welche Informationen es wert sind, gespeichert zu werden, wie lange sie aufbewahrt werden sollen, wer darauf zugreifen kann und wie Konflikte zwischen alten und neuen Daten gelöst werden. Dabei geht es um Datenschutz, Compliance und Data Governance. Das ist im EU-Finanzdienstleistungskontext, in dem Contigo tätig ist, wichtig.
![image]((notion-hosted file))

## Wo werden beide eingesetzt?
[TABLE]
  |  | Kurzzeit-Memory | Langzeit-Memory |
  | Speicherort | Context Window (innerhalb des aktiven Prompts) | Externe Datenbank (außerhalb des Modells) |
  | Lebensdauer | Nur für die Dauer der aktiven Session | Bleibt über mehrere Sessions hinweg bestehen |
  | Am besten geeignet für | Mehrstufige Aufgaben, Kontinuität mitten in der Session | Nutzerpräferenzen, Verlauf, laufende Fälle |
  | Primäres Risiko | Context Window füllt sich, ältere Inhalte fallen heraus | Veraltete, falsche oder sensible Daten speichern |

## Verständnis prüfen
>  Ein wiederkehrender Contigo-Kunde erwartet, dass sich der Agent an seine bevorzugte Sprache aus dem letzten Monat erinnert. Welche Art von Memory macht das möglich?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/fe5822d3-81c1-472d-b555-b5dfd731adc4

> 💡 Takeaway: 
  Kurzzeit-Memory sorgt für einen konsistenten Gesprächsverlauf innerhalb einer laufenden Unterhaltung. Langzeit-Memory ermöglicht es dem Agenten, Informationen über mehrere Gespräche hinweg zu behalten und so langfristig personalisierte Interaktionen zu führen. Beide Formen von Memory erfüllen unterschiedliche Aufgaben und sind wichtige Bausteine einer gut gestalteten Agentenarchitektur.