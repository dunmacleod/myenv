# Comparison Evidence

Notion page: https://app.notion.com/p/Comparison-Evidence-3789418319f3800495ced33d257b812f
Backed up before n8n migration

> 💡 Darum geht es in diesem Assessment: Du erstellst einen strukturierten Plattformvergleich und eine schriftliche Begründung, mit der ein technischer Stakeholder die Entscheidung für Flowise gegen realistische Alternativen bewerten kann.

## Die Ausgangslage
Der CTO von Meridian Consulting hat sich das interne Agenten-Projekt angeschaut und stellt vor der finalen Freigabe eine pointierte Frage:
> "We built this in Flowise. Why Flowise specifically? Could we have achieved the same result in Langflow, Copilot Studio, or Google AI Studio? Would any of those have been a better fit for our team and our clients?”
Eine berechtigte Frage. Plattform-Entscheidungen zu Projektbeginn wirken sich langfristig aus, und zwar auf Wartung, Team-Kompetenzen, Ökosystem-Kompatibilität und Governance-Aufwand. Ein Team, das nicht erklären kann, warum es sich für eine Plattform entschieden hat, hat die Entscheidung nicht sorgfältig genug geprüft.
Deine Aufgabe ist es, die Beweisführung zu liefern, die die Frage des CTOs beantwortet: eine konkrete Analyse dazu, wie der Meridian-Consulting-Agent auf jeder der vier Plattformen anders gebaut, gewartet und gesteuert worden wäre, und warum Flowise angesichts von Meridians tatsächlichen Rahmenbedingungen die richtige Wahl war. Ein genereller Plattformvergleich reicht dafür nicht.
## Meridians Rahmenbedingungen: Die Bewertungskriterien
Bevor du Plattformen vergleichst, leg die Kriterien fest, die der Vergleich abdecken muss. Das hier sind Meridians tatsächliche Rahmenbedingungen aus dem Projekt.
[TABLE]
  | Rahmenbedingung | Detail |
  | Engineering-Ökosystem | Meridians Entwicklungsteam arbeitet vor allem mit JavaScript und TypeScript. Python-Data-Engineers gibt es im Team nicht. |
  | Anpassungstiefe | Der Agent brauchte individuelle JavaScript-Logik für die Engagement-Status-Abfrage im HTTP Node und den Retry-Zähler im Custom Function Node. Für beides reichten Standard-Node-Konfigurationen nicht aus. |
  | Self-Hosting-Anforderung | Meridian verarbeitet vertrauliche operative Kundendaten. Die gesamte Infrastruktur muss selbst gehostet werden. Keine externe verwaltete Plattform darf echte Kundendaten verarbeiten, ohne dass es dafür einen expliziten vertraglichen Auftragsverarbeitungsvertrag gibt. |
  | Governance-Aufwand | Meridian arbeitet aktuell nicht innerhalb eines Microsoft-365-Ökosystems. SharePoint, Teams und Azure AD sind nicht Teil des Technologie-Stacks der Firma. |
  | Prototyping versus Produktion | Der Agent brauchte in der Bauphase schnelle Iteration, danach einen stabilen, kontrollierten Weg in die Produktion. |
## Bevor du startest: Plattform-Referenzlektüre
Bevor du die Vergleichsmatrix ausfüllst, sieh dir für jede Plattform die folgende offizielle Dokumentation an. Du musst nicht alles lesen. Konzentrier dich auf die Architekturübersicht, die Deployment-Optionen und die Integrationsmöglichkeiten der jeweiligen Plattform.
Langflow
- Übersicht und Grundkonzepte: docs.langflow.org
- Self-Hosting-Optionen: docs.langflow.org/deployment-overview
Microsoft Copilot Studio
- Übersicht: learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
- Governance und Sicherheit: learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance
- Deployment-Optionen: learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
Google AI Studio
- Übersicht: ai.google.dev/gemini-api/docs/ai-studio-quickstart
- Datenschutz und Nutzungsbedingungen: ai.google.dev/gemini-api/terms
- Unterschied zwischen AI Studio und der Gemini Enterprise Agent Platform: cloud.google.com/vertex-ai/generative-ai/docs/migrate/migrate-google-ai
Flowise (zur Orientierung)
- Self-Hosting-Optionen: docs.flowiseai.com/configuration/deployment
> ➡️ Lesehinweis: Konzentrier dich bei jeder Plattform auf drei Fragen:
  - Lässt sie sich selbst hosten? Falls ja, was braucht es dafür?
  - Welche Anpassungsmechanismen bietet sie für nicht standardmäßige Logik?
  - Welche Governance-Funktionen bietet sie, und welche Voraussetzungen brauchen diese Funktionen?
  Diese drei Fragen decken sich direkt mit Meridians Bewertungskriterien und reichen aus, um die Matrix sauber auszufüllen.

## Deine Aufgaben
### Aufgabe A: Die Plattform-Vergleichsmatrix ausfüllen
Nutze Meridians fünf Bewertungskriterien als Spaltenüberschriften und füll die Matrix unten aus, indem du beschreibst, wie jede Plattform bei jedem Kriterium abschneidet. Schreib pro Zelle ein bis zwei Sätze. Sei konkret genug, um die tatsächliche Architektur der jeweiligen Plattform widerzuspiegeln.
[TABLE]
  | Platform | Engineering ecosystem | Customisation depth | Self-hosting | Governance overhead | Prototyping vs production |
  | Flowise |  |  |  |  |  |
  | Langflow |  |  |  |  |  |
  | Copilot Studio |  |  |  |  |  |
  | Google AI Studio |  |  |  |  |  |
> ➡️ Checkpoint 1 - Langflow und das Engineering-Ecosystem: Langflow basiert auf Python und legt den zugrunde liegenden Python-Code jeder Komponente offen. Meridians Team arbeitet mit JavaScript und TypeScript. Überleg dir, welche praktische Konsequenz dieser Mismatch hat, wenn individuelle Tool-Logik geschrieben oder angepasst werden muss, und wie sich das im Vergleich zum Schreiben von individuellem JavaScript im Custom Function Node von Flowise verhält.
> ➡️ Checkpoint 2 - Copilot Studio und der Governance-Aufwand: Der Governance-Vorteil von Copilot Studio besteht darin, dass es Azure Active Directory, rollenbasierte Zugriffskontrollen und Data-Loss-Prevention-Richtlinien automatisch übernimmt. Dieser Vorteil greift aber nur, wenn die Organisation bereits im Microsoft-Ökosystem arbeitet. Meridian nutzt weder SharePoint noch Teams noch Azure AD. Was bringt das Governance-Versprechen für dieses Deployment also tatsächlich?
> ➡️ Checkpoint 3 - Google AI Studio und Prototyping versus Produktion: Google AI Studio ist für schnelles Prototyping und Prompt-Experimente gedacht. Es bietet weder VPC-Isolation noch vertragliche SLAs noch die Audit-Trail-Infrastruktur, die eine Beratung mit vertraulichen Kundendaten braucht. Überleg dir, was der Migrationspfad von AI Studio in die Produktion konkret bedeutet, und vergleich das mit dem Weg von einem selbst gehosteten Flowise-Prototyp zu einem Flowise-Deployment in Produktion.
> ➡️ Checkpoint 4 - Flowise-Limitation für Absatz 3 in Aufgabe B: Flowise basiert auf Node.js und läuft aktuell als einzelner Docker-Container. Überleg dir, wo die Infrastruktur-Grenzen dieses Standard-Deployments mit nur einer Instanz liegen, wenn Meridians Consulting-Team wächst und die Zahl gleichzeitiger Sessions steigt, und wie der Weg zum Upgrade aussieht.

### Aufgabe B: Das Begründungspapier zur Plattform schreiben
Nutze deine ausgefüllte Matrix als Beleg und schreib ein dreiabsätziges Begründungspapier an Meridians CTO, das erklärt, warum Flowise für dieses konkrete Projekt die richtige Plattform-Wahl war.
#### Absatz 1: Warum Flowise zu Meridians Rahmenbedingungen passte
- Beziehe dich auf mindestens drei der fünf Bewertungskriterien. Begründe jedes Argument mit Meridians konkreter Situation, nicht mit generischen Plattform-Stärken.
- Zum Beispiel: „Meridians Entwicklungsteam arbeitet mit JavaScript und TypeScript. Damit ist der Custom Function Node von Flowise der naheliegende Erweiterungsmechanismus für die individuelle Retry-Logik und die Engagement-Status-Abfrage, die der Agent brauchte, ganz ohne Sprachwechsel im Kontext."
#### Absatz 2: Warum die Alternativen weniger geeignet waren
- Geh nacheinander auf alle drei alternativen Plattformen ein. Nenne für jede den einen wichtigsten Grund, warum sie für Meridian konkret die schlechtere Wahl gewesen wäre.
- Beim Argument zu Copilot Studio geht es zum Beispiel nicht darum, dass die Plattform schlecht ist. Ihre Governance-Vorteile setzen eine bestehende Microsoft-365-Infrastruktur voraus, die Meridian nicht hat. Die Lizenzkosten bringen für dieses Deployment also keinen entsprechenden Governance-Nutzen.
#### Absatz 3: Eine anerkannte Einschränkung
- Eine starke architektonische Begründung erkennt auch an, was die gewählte Plattform nicht gut kann. Identifiziere eine echte Einschränkung von Flowise für Meridians konkreten Anwendungsfall, eine Einschränkung, die entweder beim Bauen sichtbar wurde oder relevant wird, sobald der Agent skaliert. Erklär, wie du damit umgehen würdest, wenn das Projekt über diesen Sprint hinaus weiterläuft.

> 💡 Fazit:
  Eine Plattform-Begründung, die sich nicht gegen Alternativen verteidigen lässt, ist bloß eine Vorliebe. Die Vergleichsmatrix erzwingt genau die ehrliche, kriterienbasierte Bewertung, die eine architektonische Entscheidung von einer Standardwahl unterscheidet. Zu dokumentieren, warum die Alternativen weniger geeignet waren, ist genauso wichtig wie zu dokumentieren, warum die gewählte Plattform gut passte. Denn erst die Alternativen-Analyse macht das Argument für einen technischen Stakeholder glaubwürdig, der auch anders hätte entscheiden können.