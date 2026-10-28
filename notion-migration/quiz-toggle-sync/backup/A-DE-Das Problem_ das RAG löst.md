# Das Problem, das RAG löst

Notion page: https://app.notion.com/p/Das-Problem-das-RAG-l-st-3779418319f380728519d5d1dcc8ee9a
Backed up before n8n migration

> 💡 Was du am Ende dieser Lektion verstehen wirst: Warum Standard-Sprachmodelle ohne externe Daten unzuverlässige Antworten erzeugen und wie Retrieval-Augmented Generation dieses Problem für Business-Agenten löst.

## Eine neue Art von Fehler
Der Support-Agent der Contigo GmbH nutzt Memory, Session-Isolation und eine durchdachte Retention-Policy. In Multi-Turn-Gesprächen über vertraute Themen arbeitet er zuverlässig. Doch sobald Kunden nach speziellen Kreditprodukten, aktuellen Zinssätzen oder internen Compliance-Verfahren fragen, scheitert er.
Der Agent antwortet selbstbewusst. Seine Antworten klingen flüssig und professionell, sind aber komplett falsch.
Ein Beispiel: Ein Kunde erkundigt sich nach der Kreditobergrenze im „SME-Finanzierungsprogramm“ von Contigo. Der Agent nennt eine Zahl aus dem allgemeinen Finanzkontext seines Trainings. Das tatsächliche Limit bei Contigo weicht jedoch ab. Der Kunde handelt auf Basis der falschen Information. Das Compliance-Team stuft das Gespräch sofort als schweren Vorfall ein.
Hier liegt ein reines Wissensproblem vor, das Memory allein nicht löst.
## Warum Sprachmodelle halluzinieren
Ein Large Language Model lernt bis zu einem festen Stichtag aus riesigen Textmengen. Nach dem Training friert dieses Wissen ein. Das Modell greift nicht auf Informationen nach seinem Trainings-Cutoff zu, besitzt keinen Einblick in interne Betriebsdaten und bemerkt eigene Wissenslücken nicht.
Fehlt dem Modell die Antwort, stoppt es nicht. Stattdessen berechnet es die wahrscheinlichste Fortsetzung des Prompts. Das Ergebnis ist eine flüssige, selbstbewusst klingende und frei erfundene Antwort: eine Halluzination.
Bei einem normalen Consumer-Chatbot wirkt das peinlich. Für einen Finanzdienstleister unter EU-Aufsicht bedeutet es ein erhebliches Haftungsrisiko. Contigo darf keinen Agenten einsetzen, der Kreditbedingungen erfindet, Compliance-Schwellenwerte vortäuscht oder Produktregeln falsch wiedergibt.
## Was RAG leistet
Retrieval-Augmented Generation (RAG) löst genau dieses Problem. Statt auf das erstarrte Wissen des Modells zu vertrauen, verbindet RAG den Agenten bei jeder Anfrage mit einer externen, aktuellen Wissensdatenbank.
Das System arbeitet in drei Schritten. Geht eine Kundenanfrage ein, durchsucht das System die Datenbank nach passenden Chunks. Es fügt diese Textbausteine als Kontext in den Prompt ein. Das Sprachmodell generiert seine Antwort nun auf Basis dieser gelieferten Fakten statt aus dem allgemeinen Trainingsspeicher.
Das Ergebnis ist ein Agent, der auf Grundlage von Evidenz antwortet statt auf Grundlage von Annäherung. Wenn ein Contigo-Kunde nach dem SME-Kreditlimit fragt, ruft der Agent die aktuelle Produktdokumentation ab, liest den tatsächlichen Betrag und antwortet korrekt. Wenn die Information nicht in der Wissensdatenbank enthalten ist, kann der Agent angewiesen werden, dies ausdrücklich zu sagen, statt eine Antwort zu erfinden.
![image]((notion-hosted file))

## Was RAG für Contigo verändert
Die praktischen Auswirkungen für Contigos Agenten sind in drei Dimensionen erheblich.
- Genauigkeit: Antworten werden in den tatsächlichen Inhalten von Contigos Dokumenten verankert statt in dem, was die Trainingsdaten des Sprachmodells zufällig über Finanzdienstleistungen im Allgemeinen enthalten haben.
- Aktualität: Die Wissensdatenbank kann aktualisiert werden, wenn sich Produkte ändern, Zinssätze angepasst werden oder Compliance-Anforderungen sich weiterentwickeln. Das Modell selbst muss nicht neu trainiert werden.
- Auditierbarkeit: Da Antworten mit bestimmten abgerufenen Dokumenten verbunden sind, wird es möglich nachzuvollziehen, welches Quellenmaterial eine bestimmte Antwort informiert hat. In einem regulierten Umfeld ist diese Nachverfolgbarkeit ein Compliance-Asset.
[TABLE]
  |  | Ohne RAG | Mit RAG |
  | Wissensquelle | Eingefrorene Trainingsdaten | Externe, aktualisierbare Wissensdatenbank |
  | Antwort auf unbekannte Anfragen | Halluzinierte plausible Antwort | Ruft Evidenz ab oder gibt an, dass die Information fehlt |
  | Domänenspezifität | Allgemeiner Finanzdienstleistungskontext | Contigos tatsächliche Produkte und Richtlinien |
  | Auditierbarkeit | Kann keine Quellen zitieren | Kann auf spezifische abgerufene Dokumente verweisen |
## Verständnis prüfen
>  Ein Contigo-Kunde fragt den Support-Agenten nach dem aktuellen SME-Kreditlimit. Der Agent antwortet selbstbewusst mit einem falschen Betrag, der in keinem Contigo-Dokument zu finden ist. Was ist die wahrscheinlichste Ursache?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/e7b23c89-191d-4a86-aaa1-dfa20a2db54f

> 💡 Takeaway:
  Memory gibt einem Agenten Kontinuität. RAG gibt ihm Genauigkeit. Ein Business-Agent, der ein kohärentes Gespräch führen kann, aber nicht auf das tatsächliche Wissen der Organisation zugreifen kann, ist trotzdem in dem Moment unzuverlässig, in dem es am meisten zählt: wenn ein Kunde eine spezifische Frage stellt, die nur das Unternehmen korrekt beantworten kann. 