# Installing n8n and API Setup on Your Computer

Notion page: https://app.notion.com/p/Installing-n8n-and-API-Setup-on-Your-Computer-3669418319f3809e9e48fcc33f0eaed8
Backed up before n8n migration

> 💡 Purpose: set up a local n8n environment with Docker, confirm that your data persists, and prepare an OpenRouter credential without exposing the API key.
## Technical requirements
You need:
- Docker Desktop installed and running.
- At least 4 GB RAM; 8 GB or more is recommended.
- A modern browser.
- The OpenRouter API key provided for the course.
- Git is recommended for later project work, but it is not required to start n8n.
For Windows, Docker Desktop normally uses WSL 2. Make sure virtualization is enabled if Docker reports a WSL or virtualisation problem.
## Part 1: Verify Docker
Open a terminal and run docker --version and then docker run hello-world.
If the second command prints the Docker hello-world message, the engine is working.
> 📸 SCREENSHOT SUGGESTION: terminal showing the Docker version and successful hello-world result.
## Part 2: Create persistent storage for n8n
Run:
docker volume create n8n_data
The volume stores your n8n configuration, workflows, and credentials outside the container lifecycle.
## Part 3: Start n8n
Run:
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
The first run may take a little longer because Docker needs to download the image.
Open http://localhost:5678 and complete the local owner-account setup if n8n asks you to do so.
> 📸 SCREENSHOT SUGGESTION: Docker Desktop showing the n8n container with status Running and port 5678.
> 📸 SCREENSHOT SUGGESTION: the n8n setup or Overview page loaded at localhost:5678. Do not include passwords or API keys.
## Part 4: Start and stop the same container
Stop it with docker stop n8n.
Start it again with docker start n8n.
Check it with docker ps.
Your workflows remain available because they are stored in the n8n_data volume.
## Part 5: Prepare OpenRouter credentials
In the next lesson you will add an OpenRouter Chat Model node.
When the node asks for credentials:
1. Create a new OpenRouter credential.
1. Paste the school-provisioned API key into the API Key field.
1. Save the credential.
1. Never place the raw key in a prompt, Code node, Set/Edit Fields node, or screenshot.
Official documentation:
n8n OpenRouter credentials
> 📸 SCREENSHOT SUGGESTION: saved OpenRouter credential selected in the node, with the secret itself not visible.
## Troubleshooting
localhost:5678 does not open
- Confirm Docker Desktop is running.
- Run docker ps.
- If the n8n container exists but is stopped, run docker start n8n.
- Inspect logs with docker logs n8n.
Port 5678 is already in use
- Stop the other process or container using the port before restarting n8n.
You accidentally deleted the container
- The n8n_data volume still preserves your data. Create the container again using the same volume mount.
> 💡 Takeaway: after this lesson, n8n should run locally at localhost:5678, its data should persist in n8n_data, and you should know how to store the OpenRouter key as an n8n credential rather than embedding it in workflow content.