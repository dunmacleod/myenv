# Setting up the Environment

Notion page: https://app.notion.com/p/Setting-up-the-Environment-3999418319f380eda08ffe61b9e5b7d5
Backed up before n8n migration

> Using OpenRouter instead of Gemini
  Some AI course materials may show Gemini setup directly inside tools like n8n, Flowise, or Cursor. In this program, use your school-provisioned OpenRouter key instead. The workflow logic stays the same, but the model connection may change.
  Before starting, read the setup guide: How-To: Using OpenRouter instead of Gemini 
> 💡 Purpose: This document will show you how to set up your environment for this course. Follow the steps and guidelines given below to set up your environment. 
## Technical Requirements
Before we start, make sure you check the following requirements.
[COLUMN_LIST]
  [COLUMN]
    For Windows:
    1. You need a 64-bit version of Windows 10 (22H2 / build 19045 or higher) or Windows 11 (23H2 or higher), with at least 4 GB of RAM (8 GB recommended) and about 6 GB of free disk space.
    1. Docker Desktop uses WSL 2 (Windows Subsystem for Linux) as its backend, so hardware virtualization must be enabled.
    1. To confirm virtualization is on, go to Task Manager > Performance > CPU, and check at the bottom to ensure that virtualization is enabled.
    Note: If it says Disabled, contact your instructor, but it is very rare that this will occur.
  [COLUMN]
    #### For Mac (Apple):
    1. Docker supports macOS 13 Ventura through 15 Sequoia.
    1. You'll want at least 4 GB of RAM (8 GB recommended).
    1. No WSL equivalent is needed here because Docker Desktop uses Apple's Virtualization framework on modern Macs.
    1. Click the Apple menu → About This Mac. If it says "Apple M1/M2/M3/M4" you have Apple Silicon; if it says "Intel" you have an Intel Mac. This determines which download you use.
> ➡️ 
  #### For Windows Users only (Follow this step first before proceeding below):
  1. Open Open PowerShell as Administrator (Start → Terminal (Admin) or PowerShell (Admin)) and run: wsl --install
  1. This installs the Virtual Machine Platform, the Windows Subsystem for Linux, and a default Ubuntu distro. A reboot is required to complete the installation.
  1. If you already have WSL, run: wsl --update
  1. After rebooting, you can verify with: wsl --version (You need WSL version 2.1.5 or higher).
## Part 1: Docker Desktop Setup
Go to this link: https://www.docker.com/products/docker-desktop/
![image]((notion-hosted file))
Download the appropriate installer.
[COLUMN_LIST]
  [COLUMN]
    #### For Windows:
    From the Docker page you linked, click the Download for Windows button. Pick the build matching your CPU. The standard x64 (AMD64) build for Intel/AMD machines, or the ARM64 build if you have a Snapdragon X / ARM laptop.
  [COLUMN]
    #### For Mac (Apple):
    On the Docker page you linked, click Download for Mac and choose Apple Silicon or Intel Chip to match step 2. You'll get a Docker.dmg file.
![image]((notion-hosted file))
> ➡️ 
  #### Some notes:
  - Use the all-users installation when you install (see the image below).
  - Windows only: If you see during the configuration page, any options of the environment, use WSL 2
  - Mac only: You may see a confirmation to open this app from the internet, say YES or OK. Accept privileged access as well.
  - You may have to reboot your computer.
When you open the desktop tool, select ‘Accept’ for the terms.
![image]((notion-hosted file))
Open Docker Desktop. On the first run you'll be asked to accept the Docker Subscription Service Agreement (free for personal use, education, and small businesses). After this, when you turn it on, wait for the whale icon in the system tray to stop animating. That means the engine is running.
![image]((notion-hosted file))
### Verifying Docker works (both Windows and Mac)
Open a terminal (PowerShell or Command Prompt on Windows, Terminal on Mac) and run:
```plain text
docker --version
docker run hello-world
```
If you see a "Hello from Docker!" message, everything is working
## Part 2: Git Installation and Setup
Go to this weblink for Git: https://git-scm.com/install/ 
For Windows, go to the latest download and install Git.
![image]((notion-hosted file))
Follow the relevant steps to install Git for Mac (Apple).
![image]((notion-hosted file))
Once installed, go to your terminal or command prompt and confirm it is working by copying this message:
```plain text
git –version
```
## Part 3: Installing Flowise and Qdrant
### Set up an account on GitHub
Go to github.com and if you have not done this already, set up an account by going to Sign Up. When signing up, make sure your e-mail address is the same as Docker. You will need this in case you need to acquire any details from the products you are using.
### Install Flowise
Go to the bottom right of the Docker Desktop. You will see the terminal name and icon. Click on this and run this:
```plain text
docker run -d -p 3000:3000 --name flowise -v flowise_data:/root/.flowise flowiseai/flowise:3.0.13
```
It might take a little bit of time. Once it is ready, it will provide you with something like this:
![image]((notion-hosted file))
Click on the port link (3000:3000) and then set up your account. Again, make sure you use the same account name as all the other components.
Go back to the Docker Desktop containers (Flowise) and click on the blue square icon to stop running it. Then click on the start button (angled triangle icon) to restart it again.
### Install Qdrant
In that same terminal, run:
```plain text
docker run -d --name qdrant -p 6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant
```
Allow the changes to occur by selecting yes (Y).
Once running, verify Qdrant is working by opening http://localhost:6333/dashboard in your browser. You should see the Qdrant dashboard.
## Part 4: Gemini API Key Setup
### Generating your Gemini API Key
You will need the Gemini API key to retrieve information from a RAG database. If you already have a Gemini API, you can disregard these steps. But follow these steps if you need a new API key in Gemini.
Navigate to Google AI Studio at aistudio.google.com and sign in with your Google account. At the bottom left-hand navigation panel, you will see a key icon which is the Get API key. Click on this, then click Create API key. 
![image]((notion-hosted file))
Associate the key with a Google Project. Create a new one if this is the first key being generated or you can use the default project. Once created, copy the key immediately. 
![image]((notion-hosted file))
Once this is done, you will see the API key. Make sure you copy all of this and keep it secure.
### Store the key in Flowise
Open your Flowise dashboard at http://localhost:3000. In the left-hand navigation panel, click the Credentials icon. Click Add Credential, search for Gemini, and select it. Name it and paste your API key into the designated field. Click Save.
### OpenRouter API Key
You will have received an API key for OpenRouter. Make sure you never share this with anyone. If you lost they API key or if there are any issues, talk to your ASM.
Open your Flowise dashboard at http://localhost:3000. In the left-hand navigation panel, click the Credentials icon. Click Add Credential, search for Gemini, and select it. Name it and paste your API key into the designated field. Click Save.

> 💡 Once you are done this last step, your environment is fully ready.