# Deine Umgebung einrichten

Notion page: https://app.notion.com/p/Deine-Umgebung-einrichten-4e99418319f382128f80810f27f78cf1
Backed up before n8n migration

> OpenRouter statt Gemini verwenden
  Einige AI-Kursmaterialien zeigen möglicherweise ein direktes Gemini-Setup in Tools wie n8n, Flowise oder Cursor. In diesem Programm verwendest du stattdessen deinen von Masterschool bereitgestellten OpenRouter-Key. Die Workflow-Logik bleibt gleich, aber die Modellverbindung kann sich ändern.
  Lies vor dem Start den Setup-Guide: How-To: OpenRouter statt Gemini verwenden

> 💡 Zweck: Dieses Dokument zeigt dir, wie du deine Umgebung für diesen Kurs einrichtest. Folge den unten angegebenen Schritten und Richtlinien, um deine Umgebung einzurichten.
## Technische Anforderungen
Bevor wir starten, prüfe bitte die folgenden Anforderungen.
[COLUMN_LIST]
  [COLUMN]
    Für Windows:
    1. Du brauchst eine 64-Bit-Version von Windows 10 (22H2 / Build 19045 oder höher) oder Windows 11 (23H2 oder höher), mit mindestens 4 GB RAM (8 GB empfohlen) und etwa 6 GB freiem Speicherplatz.
    1. Docker Desktop nutzt WSL 2 (Windows Subsystem for Linux) als Backend, daher muss Hardware-Virtualisierung aktiviert sein.
    1. Um zu bestätigen, dass Virtualisierung aktiviert ist, gehe zu Task Manager > Performance > CPU und prüfe unten, ob Virtualization aktiviert ist.
    Hinweis: Wenn dort Disabled steht, kontaktiere deinen Instructor. Es ist aber sehr selten, dass das passiert.
  [COLUMN]
    #### Für Mac (Apple):
    1. Docker unterstützt macOS 13 Ventura bis 15 Sequoia.
    1. Du solltest mindestens 4 GB RAM haben (8 GB empfohlen).
    1. Hier ist kein WSL-Äquivalent nötig, weil Docker Desktop auf modernen Macs Apples Virtualization Framework nutzt.
    1. Klicke auf das Apple-Menü → About This Mac. Wenn dort „Apple M1/M2/M3/M4“ steht, hast du Apple Silicon; wenn dort „Intel“ steht, hast du einen Intel Mac. Das bestimmt, welchen Download du nutzt.
> ➡️ 
  #### Nur für Windows-User (folge zuerst diesem Schritt, bevor du unten weitermachst):
  1. Öffne PowerShell als Administrator (Start → Terminal (Admin) oder PowerShell (Admin)) und führe aus: wsl --install
  1. Dadurch werden die Virtual Machine Platform, das Windows Subsystem for Linux und eine Standard-Ubuntu-Distribution installiert. Ein Neustart ist erforderlich, um die Installation abzuschließen.
  1. Wenn du WSL bereits hast, führe aus: wsl --update
  1. Nach dem Neustart kannst du mit Folgendem prüfen: wsl --version (du brauchst WSL-Version 2.1.5 oder höher).
## Teil 1: Docker Desktop einrichten
Gehe zu diesem Link: https://www.docker.com/products/docker-desktop/
![image]((notion-hosted file))
Lade den passenden Installer herunter.
[COLUMN_LIST]
  [COLUMN]
    #### Für Windows:
    Klicke auf der Docker-Seite, die du verlinkt hast, auf den Button Download for Windows. Wähle den Build, der zu deiner CPU passt. Den Standard-x64-Build (AMD64) für Intel-/AMD-Maschinen oder den ARM64-Build, wenn du einen Snapdragon-X-/ARM-Laptop hast.

  [COLUMN]
    #### Für Mac (Apple):
    Klicke auf der Docker-Seite, die du verlinkt hast, auf Download for Mac und wähle Apple Silicon oder Intel Chip passend zu Schritt 2. Du erhältst eine Docker.dmg-Datei.
![image]((notion-hosted file))
> ➡️ 
  #### Einige Hinweise:
  - Nutze bei der Installation die All-Users-Installation (siehe Bild unten).
  - Nur Windows: Wenn du auf der Konfigurationsseite Optionen zur Umgebung siehst, nutze WSL 2.
  - Nur Mac: Möglicherweise siehst du eine Bestätigung, diese App aus dem Internet zu öffnen. Wähle YES oder OK. Akzeptiere auch privilegierten Zugriff.
  - Möglicherweise musst du deinen Computer neu starten.
Wenn du das Desktop-Tool öffnest, wähle „Accept“ für die Bedingungen.
![image]((notion-hosted file))
Öffne Docker Desktop. Beim ersten Start wirst du aufgefordert, das Docker Subscription Service Agreement zu akzeptieren (kostenlos für persönliche Nutzung, Bildung und kleine Unternehmen). Warte danach beim Einschalten, bis das Wal-Symbol in der System Tray nicht mehr animiert ist. Das bedeutet, dass die Engine läuft.
![image]((notion-hosted file))
### Prüfen, ob Docker funktioniert (Windows und Mac)
Öffne ein Terminal (PowerShell oder Command Prompt unter Windows, Terminal auf dem Mac) und führe aus:
```plain text
docker --version
docker run hello-world
```
Wenn du eine „Hello from Docker!“-Nachricht siehst, funktioniert alles.
## Teil 2: Git installieren und einrichten
Gehe zu diesem Weblink für Git: https://git-scm.com/install/
Für Windows gehst du zum neuesten Download und installierst Git.
![image]((notion-hosted file))
Folge den passenden Schritten, um Git für Mac (Apple) zu installieren.
![image]((notion-hosted file))
Öffne nach der Installation dein Terminal oder deinen Command Prompt und bestätige, dass es funktioniert, indem du diesen Befehl kopierst:
```plain text
git –version
```
## Teil 3: n8n und Qdrant installieren
### Ein Konto auf GitHub einrichten
Gehe zu github.com und richte, falls du das noch nicht getan hast, ein Konto über Sign Up ein. Achte bei der Registrierung darauf, dass deine E-Mail-Adresse dieselbe ist wie bei Docker. Du brauchst das, falls du Details aus den Produkten abrufen musst, die du verwendest.
### n8n installieren
Wir führen n8n lokal mit Docker aus. Das bedeutet, dass n8n auf deinem Computer läuft und du über deinen Browser auf die Benutzeroberfläche zugreifst.
Stelle sicher, dass Docker Desktop läuft.
Öffne ein Terminal (PowerShell oder Command Prompt unter Windows, Terminal auf dem Mac) und führe aus:
```plain text
docker volume create n8n_data
```
Dadurch wird ein Docker-Volume erstellt, in dem n8n deine Workflows, Credentials und weitere Konfigurationen speichert.
Starte jetzt n8n:
```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```
Docker lädt das n8n-Image beim ersten Ausführen herunter. Das kann einige Minuten dauern.
Sobald der Container läuft, öffne http://localhost:5678.
Du solltest den n8n-Setup-Bildschirm sehen. Erstelle dein lokales n8n-Owner-Konto und schließe die Ersteinrichtung ab.
![image]((notion-hosted file))
### Prüfen, ob n8n läuft
Öffne in Docker Desktop Containers. Du solltest einen Container namens n8n sehen. Der Status sollte Running sein.
Du kannst es auch im Terminal überprüfen:
```bash
docker ps
```
![image]((notion-hosted file))
Du solltest den n8n-Container mit Port 5678 sehen. Öffne http://localhost:5678 erneut und bestätige, dass die n8n-Oberfläche geladen wird.

### n8n starten und stoppen
Du musst nicht jedes Mal einen neuen Container erstellen, wenn du n8n verwendest.
Zum Stoppen:
```bash
docker stop n8n
```
Zum erneuten Starten:
```bash
docker start n8n
```
Deine Workflows und Einstellungen bleiben erhalten, da sie im Docker-Volume n8n_data gespeichert werden.
### Qdrant installieren
Führe in demselben Terminal Folgendes aus:
```plain text
docker run -d --name qdrant -p 6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant
```
Erlaube die Änderungen, indem du Ja (Y) auswählst.
Sobald Qdrant läuft, prüfe, ob es funktioniert, indem du http://localhost:6333/dashboard in deinem Browser öffnest. Du solltest das Qdrant-Dashboard sehen.
![image]((notion-hosted file))
## Teil 4: Gemini API Key einrichten
### Deinen Gemini API Key generieren
Du benötigst den Gemini API Key, um Informationen aus einer RAG-Datenbank abzurufen. Wenn du bereits eine Gemini API hast, kannst du diese Schritte überspringen. Folge diesen Schritten, wenn du einen neuen API Key in Gemini benötigst.
Öffne Google AI Studio unter aistudio.google.com und melde dich mit deinem Google-Konto an. Unten links in der Navigationsleiste siehst du ein Schlüssel-Symbol: Get API key. Klicke darauf und anschließend auf Create API key.
![image]((notion-hosted file))
Verknüpfe den Key mit einem Google Project. Erstelle ein neues, wenn dies der erste generierte Key ist, oder nutze das Standardprojekt. Kopiere den Key sofort, sobald er erstellt wurde.
![image]((notion-hosted file))
Sobald das erledigt ist, siehst du den API Key. Kopiere ihn vollständig und bewahre ihn sicher auf.
### Schlüssel in Flowise speichern
Öffne dein Flowise-Dashboard unter http://localhost:3000. Klicke in der linken Navigationsleiste auf das Credentials-Symbol. Klicke auf Add Credential, suche nach Gemini und wähle es aus. Benenne den Eintrag und füge deinen API Key in das dafür vorgesehene Feld ein. Klicke auf Save.
### OpenRouter API Key
Du hast einen API Key für OpenRouter erhalten. Teile ihn niemals mit anderen Personen. Wenn du den API Key verloren hast oder es Probleme gibt, sprich mit deinem ASM.
Öffne dein Flowise-Dashboard unter http://localhost:3000. Klicke in der linken Navigationsleiste auf das Credentials-Symbol. Klicke auf Add Credential, suche nach Gemini und wähle es aus. Benenne den Eintrag und füge deinen API Key in das dafür vorgesehene Feld ein. Klicke auf Save.

> 💡 Sobald du diesen letzten Schritt erledigt hast, ist deine Umgebung vollständig bereit.