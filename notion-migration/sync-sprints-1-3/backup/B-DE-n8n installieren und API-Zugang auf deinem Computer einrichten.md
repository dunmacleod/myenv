# n8n installieren und API-Zugang auf deinem Computer einrichten

Notion page: https://app.notion.com/p/n8n-installieren-und-API-Zugang-auf-deinem-Computer-einrichten-3789418319f380a28bccc55d86d6313f
Backed up before n8n migration

> 💡 Ziel: eine lokale n8n-Umgebung mit Docker einrichten, persistente Speicherung prüfen und ein OpenRouter-Credential vorbereiten, ohne den API-Key offenzulegen.
## Technische Voraussetzungen
Du brauchst:
- Docker Desktop, installiert und gestartet.
- Mindestens 4 GB RAM; 8 GB oder mehr werden empfohlen.
- Einen modernen Browser.
- Den für den Kurs bereitgestellten OpenRouter-API-Key.
- Git wird für spätere Projektarbeit empfohlen, ist aber zum Start von n8n nicht erforderlich.
Unter Windows verwendet Docker Desktop normalerweise WSL 2. Falls Docker einen WSL- oder Virtualisierungsfehler meldet, prüfe, ob die Hardware-Virtualisierung aktiviert ist.
## Teil 1: Docker überprüfen
Öffne ein Terminal und führe docker --version und danach docker run hello-world aus.
Wenn der zweite Befehl die Docker-Hello-World-Ausgabe zeigt, funktioniert die Engine.
> 📸 SCREENSHOT-VORSCHLAG: Terminal mit Docker-Version und erfolgreicher hello-world-Ausgabe.
## Teil 2: Persistenten Speicher für n8n erstellen
Führe aus:
docker volume create n8n_data
Dieses Volume speichert n8n-Konfiguration, Workflows und Credentials unabhängig vom Lebenszyklus des Containers.
## Teil 3: n8n starten
Führe aus:
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
Beim ersten Start kann es etwas länger dauern, weil Docker das Image herunterladen muss.
Öffne http://localhost:5678 und richte das lokale Owner-Konto ein, falls n8n dich dazu auffordert.
> 📸 SCREENSHOT-VORSCHLAG: Docker Desktop mit dem Container n8n, Status Running, Port 5678.
> 📸 SCREENSHOT-VORSCHLAG: n8n-Setup oder Übersichtsseite unter localhost:5678. Keine Passwörter oder API-Keys zeigen.
## Teil 4: Denselben Container stoppen und wieder starten
Stoppe ihn mit docker stop n8n.
Starte ihn wieder mit docker start n8n.
Prüfe den Status mit docker ps.
Deine Workflows bleiben erhalten, weil sie im Volume n8n_data gespeichert sind.
## Teil 5: OpenRouter-Credentials vorbereiten
In der nächsten Lektion fügst du eine OpenRouter Chat Model Node hinzu.
Wenn die Node nach Credentials fragt:
1. Erstelle ein neues OpenRouter-Credential.
1. Füge den von der Schule bereitgestellten API-Key in das Feld API Key ein.
1. Speichere das Credential.
1. Lege den rohen Key niemals in einem Prompt, einer Code Node, Set/Edit Fields Node oder einem Screenshot ab.
Offizielle Dokumentation:
n8n OpenRouter Credentials
> 📸 SCREENSHOT-VORSCHLAG: gespeichertes OpenRouter-Credential in der Node; der geheime Schlüssel selbst darf nicht sichtbar sein.
## Fehlerbehebung
localhost:5678 lässt sich nicht öffnen
- Prüfe, ob Docker Desktop läuft.
- Führe docker ps aus.
- Falls der Container n8n existiert, aber gestoppt ist, führe docker start n8n aus.
- Logs anzeigen mit docker logs n8n.
Port 5678 ist bereits belegt
- Stoppe den anderen Prozess oder Container, der den Port verwendet, und starte n8n erneut.
Du hast den Container versehentlich gelöscht
- Das Volume n8n_data enthält deine Daten weiterhin. Erstelle den Container mit demselben Volume-Mount erneut.
> 💡 Takeaway: Nach dieser Lektion sollte n8n lokal unter localhost:5678 laufen, Daten sollten im Volume n8n_data erhalten bleiben und du solltest wissen, wie der OpenRouter-Key als n8n-Credential gespeichert wird.