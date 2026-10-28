# Deinen Chatflow öffentlich machen

Notion page: https://app.notion.com/p/Deinen-Chatflow-ffentlich-machen-3779418319f3806bbf89d202c63ef742
Backed up before n8n migration

> 💡 Das machst du in dieser Lektion: Du konfigurierst deinen Chatflow für den öffentlichen Zugriff. Mit dem ngrok-Docker-Container erstellst du eine sichere öffentliche URL, die deine lokale Flowise-Instanz nach außen freigibt. Du testest diese URL und bereitest die drei Sharing-Formate vor, die du bei deiner Sprint-4-Präsentation nutzt.

## Warum dieser Schritt jetzt kommt
Der Support-Agent von Contigo GmbH ist vollständig gebaut, getestet und abgesichert. Der letzte Schritt vor der Präsentation ist, ihn auch für Menschen außerhalb deines lokalen Rechners zugänglich zu machen. Deine Flowise-Instanz läuft unter http://localhost:3000, das heißt, nur du kannst darauf zugreifen. Deine Kommilitonen, dein Kursleiter und mögliche externe Prüfer erreichen ihn von ihren eigenen Geräten aus nicht.
Diese Lektion löst genau das. Am Ende ist dein Chatflow über eine öffentliche URL erreichbar, die während deiner Präsentation jeder mit dem Link nutzen kann, ohne dass du auf einen Cloud-Server deployen oder dein lokales Setup verändern musst.
## Die Sharing-Optionen von Flowise
Flowise unterstützt drei Deployment-Kanäle für einen fertigen Chatflow:
- Public Chat URL: Eine vollflächige Chat-Oberfläche, die jeder im Browser öffnen kann.
- Embed Widget: Ein HTML- oder React-Snippet, das eine Chat-Bubble in eine beliebige Webseite einbettet.
- REST API Endpoint: Ein programmatischer Endpoint, um den Chatflow in eine Anwendung zu integrieren.
Für die Sprint-4-Präsentation nutzt du die Public Chat URL. Das ist die einfachste Option, die deinem Publikum eine vollständig interaktive Chat-Oberfläche im Browser gibt. Embed Widget und API Endpoint sind die richtige Wahl, wenn du den Agenten in eine echte Website oder Anwendung integrieren willst.
## Das Problem mit dem lokalen Zugriff
Deine Flowise-Instanz läuft in einem Docker-Container auf deinem lokalen Rechner unter http://localhost:3000. Diese Adresse ist nur von deinem eigenen Rechner aus erreichbar. Niemand sonst kann von außen darauf zugreifen.
Um sie für die Präsentation vorübergehend zugänglich zu machen, nutzt du ngrok. Das ist ein Tunneling-Tool, das eine sichere öffentliche URL erstellt und den gesamten Traffic darüber an deine lokale Flowise-Instanz weiterleitet. Die URL ist temporär: Sie läuft ab, sobald du ngrok stoppst. Für den Präsentationskontext ist das genau passend.
Da es für ngrok ein offizielles Docker Image gibt, brauchst du keine separate Installation. Es läuft als vierter Docker-Container neben Flowise, Qdrant und deinem bestehenden Setup.
### Schritt 1: Ein kostenloses ngrok-Konto anlegen
Geh auf ngrok.com und erstelle ein kostenloses Konto. Navigiere nach der Anmeldung zu deinem ngrok-Dashboard unter dashboard.ngrok.com/get-started/your-authtoken und kopiere deinen Auth Token. Den brauchst du in Schritt 3. Das ist der einzige nötige Setup-Schritt. Alles andere läuft über Docker.
![image]((notion-hosted file))

### Schritt 2: Deine lokale Umgebung starten
Stelle sicher, dass Flowise und Qdrant beide laufen, bevor du den Tunnel erstellst. Führe in deinem Terminal aus:
```powershell
docker start flowise
docker start qdrant
```
Prüfe, ob Flowise unter http://localhost:3000 erreichbar ist, bevor du weitermachst. Lädt die Seite nicht, prüfe, ob Docker Desktop läuft und beide Container aktiv sind.
### Schritt 3: Den ngrok-Tunnel über Docker starten
Führe in einem neuen Terminalfenster den folgenden Befehl aus. Du musst dies nur einmal tun. Ersetze YOUR_AUTH_TOKEN durch das Token, das du aus deinem ngrok-Dashboard kopiert hast:
```powershell
docker run --rm -p 4040:4040 -e NGROK_AUTHTOKEN=PASTE YOUR TOKEN ngrok/ngrok:latest http host.docker.internal:3000
```
> ➡️ Es kann eine Weile dauern, bis alles lädt, das ist normal. In der Zwischenzeit kannst du gern andere Dinge wiederholen oder weiterarbeiten.
Schau in Docker Desktop, dort siehst du, dass ngrok läuft. Öffne http://localhost:4040 in deinem Browser, um das ngrok Inspection Dashboard zu sehen, das alle eingehenden Requests in Echtzeit zeigt. Das ist während der Präsentation praktisch, um zu zeigen, dass der Agent live Traffic empfängt und beantwortet.
Gehe zum Headers-Bereich.
![image]((notion-hosted file))
Scroll runter, bis du den Host-Bereich siehst. Das ist deine öffentliche URL:
![image]((notion-hosted file))
Kopiere den Link und füge ihn in deinen Browser ein. Du siehst dann den folgenden Screen. Klicke auf 'Visit Site', dann wirst du zu Flowise zurückgeleitet. Logge dich in deinen Account ein. Nach dem Login siehst du den Chatbot noch nicht. Das richten wir jetzt ein.

![image]((notion-hosted file))

### Schritt 4: Die Public Chat URL deines Chatflows abrufen
Öffne dein Flowise-Dashboard unter http://localhost:3000. Öffne deinen Chatflow-Canvas. Klicke oben rechts auf das API-Endpoint-Symbol.
![image]((notion-hosted file))

Schalte den Toggle für Make Public ein. Gehe zum Tab Share Chatbot, und du siehst einen teilbaren Link im Format: http://localhost:3000/chatbot/YOUR-CHATFLOW-ID
![image]((notion-hosted file))
Der alphanumerische Code (FlowiseID) ist dein teilbarer Link.
Öffne einen Browser und füge Folgendes ein:
```html
ngrok browser URL/chatbot/FlowiseID
```
Es sieht dann so aus:
![image]((notion-hosted file))
> ⚠️  Wichtig: Schließe dieses Terminal-Fenster während der Präsentation nicht. Stoppt der ngrok-Container, funktioniert die öffentliche URL sofort nicht mehr. Im kostenlosen ngrok-Plan ändert sich die öffentliche URL bei jedem Neustart des Tunnels. Erzeuge sie deshalb erst unmittelbar vor der Präsentation und teile sie dann.

### Schritt 5: Die öffentliche URL testen
Öffne die öffentliche URL in einem anderen Browser, oder bitte jemanden, sie auf einem anderen Gerät zu öffnen.
- Sende eine Testnachricht: "What documents do I need for an SME loan application?"
- Erwartetes Verhalten: Der Agent antwortet mit einer konkreten Antwort aus der Qdrant-Wissensdatenbank. Der vollständige Chatflow (Memory, Retrieval, Tools und Guardrails) ist über die öffentliche URL genauso aktiv und erreichbar wie auf deiner lokalen Canvas.
✅ Bestanden: Die öffentliche URL lädt korrekt und der Agent antwortet wie erwartet.
❌ Nicht bestanden: Lädt die URL nicht, prüfe, ob ngrok noch in deinem Terminal läuft und ob Flowise unter http://localhost:3000 erreichbar ist. Lädt die URL, antwortet der Agent aber nicht, prüfe, ob Qdrant unter http://localhost:6333/dashboard läuft.
### Schritt 6: Öffentlichen Zugriff nach der Präsentation schließen
Sobald deine Präsentation vorbei ist, stoppe den ngrok-Container mit Ctrl+C in dem Terminal-Fenster, in dem er läuft. Das schließt die öffentliche URL sofort und entfernt jeden externen Zugriff auf deine lokale Flowise-Instanz.
> ➡️ Warum das wichtig ist: Dein Chatflow verarbeitet Kundendaten von Contigo. Lässt du den öffentlichen Tunnel nach der Präsentation offen, ist dein Agent unerwünschten Anfragen ausgesetzt. Ngrok zu stoppen ist ein einziger Tastendruck, der dieses Risiko komplett beseitigt.

## Checkliste: Vor der Präsentation bestätigen
Geh diese Checkliste direkt vor Beginn der Präsentation durch. Die ngrok-URL ändert sich bei jedem Neustart, deshalb musst du sie am Präsentationstag frisch generieren.
- [ ] Docker Desktop geöffnet und läuft
- [ ] docker start flowise bestätigt
- [ ] docker start qdrant bestätigt
- [ ] Flowise unter http://localhost:3000 erreichbar
- [ ] ngrok-Docker-Container mit korrektem Auth Token gestartet
- [ ] Öffentliche ngrok-URL im Terminal-Output sichtbar
- [ ] ngrok Inspection Dashboard unter http://localhost:4040 erreichbar
- [ ] Public-Chatflow-URL konstruiert, indem localhost:3000 durch die ngrok-URL ersetzt wurde
- [ ] Öffentliche URL in einem zweiten Browser getestet, Agent antwortet korrekt
- [ ] ngrok-Terminalfenster für die Dauer der Präsentation offen gehalten
- [ ] ngrok unmittelbar nach Ende der Präsentation mit Ctrl+C gestoppt
Aktualisierte Startsequenz für jede Session
Ab jetzt sieht deine vollständige Startsequenz für jede Session, auch am Präsentationstag, so aus:

1. Docker Desktop öffnen
1. docker start flowise
1. docker start qdrant
1. Nur für die Präsentation: den ngrok-Docker-Befehl in einem neuen Terminalfenster ausführen
  1. docker run --rm -p 4040:4040 -e NGROK_AUTHTOKEN=YOUR_AUTH_TOKEN ngrok/ngrok:latest http host.docker.internal:3000
1. http://localhost:3000 für Flowise öffnen
1. http://localhost:6333/dashboard öffnen, um zu prüfen, dass Qdrant läuft
1. Nur für die Präsentation: http://localhost:4040 öffnen, um zu prüfen, dass der ngrok-Tunnel aktiv ist

> 💡 Fazit:
  Deinen Chatflow öffentlich zugänglich zu machen, verwandelt einen lokalen Build in ein vorführbares Produkt. Der ngrok-Docker-Container gibt dir mit einem einzigen Befehl eine temporäre öffentliche URL.
  Die drei Sharing-Formate, die dir jetzt zur Verfügung stehen, entsprechen den drei Deployment-Wegen eines produktiven Chatflows. Über genau diese Wege würde er echte Nutzer erreichen.
