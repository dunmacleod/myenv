# Tools zu einem einzelnen Agenten hinzufügen

Notion page: https://app.notion.com/p/Tools-zu-einem-einzelnen-Agenten-hinzuf-gen-3779418319f3803b9ef9d5b760708a19
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Wie Tools einen n8n AI Agent über Retrieval und Textgenerierung hinaus erweitern und wie der Agent entscheidet, wann ein Tool benötigt wird.

## Die Grenze von reinem RAG
Contigo GmbHs Support-Agent kann bereits Fragen mithilfe der Wissensbasis beantworten, die du in Sprint 2 verbunden hast. Er kann Kreditprodukte, Anspruchsvoraussetzungen und Antragsanforderungen anhand abgerufener Belege erklären.
Einige Kundenanfragen benötigen jedoch mehr als Informationen:
> „Kannst du den aktuellen Status des Antrags APP-7741 prüfen?"
Die Wissensbasis kann den Antragsprozess erklären, kennt aber nicht den aktuellen Status eines bestimmten Antrags. Diese Information liegt in einem Live-System. Um zuverlässig zu antworten, benötigt der Agent ein Tool, das dieses System abfragen kann.
Das ist der Unterschied zwischen Retrieval und Tool-Nutzung. RAG verschafft dem Agenten Zugriff auf dokumentiertes Wissen. Tools geben ihm Zugriff auf Fähigkeiten wie Live-Abfragen, Berechnungen, APIs, Datenbanken und deterministische Workflows.

## Was Tools sind
Ein Tool ist eine Fähigkeit, die der AI Agent während der Bearbeitung einer Anfrage aufrufen kann.
Für Contigo sind drei typische Kategorien relevant:
- Informations-Tools: Fragen Live- oder strukturierte Daten ab, zum Beispiel einen Dienst für den Antragsstatus.
- Aktions-Tools: Starten eine kontrollierte Operation in einem anderen System oder Workflow.
- Berechnungs-Tools: Führen deterministische Berechnungen aus, statt das Sprachmodell näherungsweise rechnen zu lassen.
In n8n werden tool-fähige Nodes mit dem Tool-Eingang des AI Agent verbunden. In diesem Sprint behältst du das Qdrant-Retrieval-Tool aus Sprint 2 und ergänzt einen Calculator sowie ein Workflow-Tool für eine simulierte Kreditstatusabfrage.

## Die Tool-Schleife des Agenten
Ein Agent mit Tools durchläuft wiederholt folgende Entscheidungen:
1. Reason: Bestimmen, welche Information oder Aktion benötigt wird.
1. Act: Ein passendes Tool auswählen und die erforderlichen Eingaben übergeben.
1. Observe: Das Ergebnis des Tools lesen.
1. Fortsetzen oder antworten: Falls nötig ein weiteres Tool aufrufen oder die finale Antwort erzeugen.
Beispiel:
1. Der Kunde fragt nach dem Status von APP-7741.
1. Der AI Agent erkennt, dass dafür Live-Antragsdaten nötig sind.
1. Er ruft das Kreditstatus-Tool mit APP-7741 auf.
1. Das Tool liefert einen strukturierten Status.
1. Der Agent erklärt dem Kunden das Ergebnis.
Das Modell sollte nicht jedes verbundene Tool aufrufen. Es sollte nur das Tool wählen, dessen Beschreibung und Eingabeanforderungen zur Anfrage passen.

> ➡️ So passt das zu deinem n8n-Build: Du ersetzt den AI Agent aus Sprint 1 und 2 nicht. Derselbe Workflow Chat Trigger → AI Agent bleibt der Kern. OpenRouter Chat Model, Simple Memory und das Qdrant-Retrieval-Tool bleiben verbunden; Sprint 3 erweitert die Tool-Verbindungen des AI Agent.

## Warum Tool-Beschreibungen wichtig sind
Der AI Agent wählt Tools anhand ihrer Namen, Beschreibungen, Eingabeschemata, der System Message und des aktuellen Gesprächs. Wenn zwei Tools vage oder überlappend beschrieben sind, kann das Modell das falsche Tool aufrufen oder ein Tool verwenden, obwohl keines nötig ist.
Eine starke Tool-Beschreibung sagt deshalb klar:
- was das Tool kann;
- wann es verwendet werden soll;
- welche Eingabe erforderlich ist;
- wofür es nicht verwendet werden darf.
Das übst du in den nächsten Lektionen gezielt.

## RAG und Agenten mit Tools
[TABLE]
  |  | Retrieval-Fähigkeit | Zusätzliche Tool-Fähigkeit |
  | Hauptzweck | Aus indexierten Dokumenten antworten | Live-Daten, deterministische Logik oder externe Operationen nutzen |
  | Contigo-Beispiel | „Welche Dokumente werden für einen KMU-Kredit benötigt?" | „Wie ist der Status des Antrags APP-7741?" |
  | n8n-Umsetzung | AI Agent + Qdrant-Retrieval-Tool | Derselbe AI Agent + zusätzliche Tool-Verbindungen |

## Check for Understanding
> 💡 Ein Contigo-Kunde fragt den Support-Agenten nach dem aktuellen Status eines konkreten Antrags. Der Agent ruft eine Richtlinienseite mit üblichen Bearbeitungszeiten ab, kann aber den tatsächlichen Status nicht nennen. Welche Fähigkeit fehlt?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bf6c2b9e-4f18-47cb-911d-654ec5cfd2df

> 💡 Takeaway: RAG gibt dem Agenten dokumentiertes Wissen. Tools erweitern denselben n8n AI Agent um Fähigkeiten, die nicht in statischen Dokumenten enthalten sind. Gute Architektur beginnt mit einem einzelnen Agenten und einem kleinen, klar beschriebenen Toolset, bevor weitere Agenten oder zusätzliche Orchestrierung eingeführt werden.