# Deine Umgebung einrichten

Notion page: https://app.notion.com/p/Deine-Umgebung-einrichten-f599418319f3837aa3e08111ace24330
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
## Teil 3: Flowise installieren
### Ein Konto auf GitHub einrichten
Gehe zu github.com und richte, falls du das noch nicht getan hast, ein Konto über Sign Up ein. Achte bei der Registrierung darauf, dass deine E-Mail-Adresse dieselbe ist wie bei Docker. Du brauchst das, falls du Details aus den Produkten abrufen musst, die du verwendest.
### Flowise installieren
Gehe unten rechts in Docker Desktop. Dort siehst du den Namen und das Symbol des Terminals. Klicke darauf und führe Folgendes aus:
```plain text
docker run -d -p 3000:3000 --name flowise -v flowise_data:/root/.flowise flowiseai/flowise:3.0.13
```
Das kann ein bisschen dauern. Sobald es bereit ist, bekommst du ungefähr so etwas:
![image]((notion-hosted file))
Klicke auf den Port-Link (3000:3000) und richte dann dein Konto ein. Achte auch hier darauf, denselben Account-Namen wie bei allen anderen Komponenten zu verwenden.
Nutze diesen Command Prompt, wenn du persistenten Speicher behalten möchtest:
```plain text
docker run -d -p 3000:3000 -v flowise_data:/root/.flowise --name flowise flowiseai/flowise
```
Gehe zurück zu den Docker-Desktop-Containern (Flowise) und klicke auf das blaue Quadrat-Symbol, um die Ausführung zu stoppen. Klicke dann auf den Start-Button (schräges Dreieck-Symbol), um es erneut zu starten.
## Teil 4: Gemini API Key einrichten
### Deinen Gemini API Key generieren
Gehe zu Google AI Studio unter aistudio.google.com und melde dich mit deinem Google-Konto an. Unten links im Navigationsbereich siehst du ein Schlüssel-Symbol, das für Get API key steht. Klicke darauf und dann auf Create API key.
![image]((notion-hosted file))
Verknüpfe den Key mit einem Google Project. Erstelle ein neues, wenn dies der erste generierte Key ist, oder nutze das Standardprojekt. Kopiere den Key sofort, sobald er erstellt wurde.
![image]((notion-hosted file))
Sobald das erledigt ist, siehst du den API Key, den Namen des Keys, den Projektnamen und die Projektnummer. Kopiere all diese Informationen und bewahre sie sicher auf. Ich empfehle, sie als .txt-Datei zu speichern.
### Den API Key in Flowise speichern
Öffne dein Flowise-Dashboard unter http://localhost:3000. Klicke im linken Navigationsbereich auf das Credentials-Symbol. Klicke auf Add Credential, suche nach Gemini und wähle es aus. Benenne es und füge deinen API Key in das dafür vorgesehene Feld ein. Klicke auf Save.

> 💡 Sobald du diesen letzten Schritt erledigt hast, ist deine Umgebung vollständig bereit.