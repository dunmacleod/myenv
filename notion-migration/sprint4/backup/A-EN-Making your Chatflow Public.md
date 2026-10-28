# Making your Chatflow Public

Notion page: https://app.notion.com/p/Making-your-Chatflow-Public-3689418319f3808899adfe3b7b53bcd2
Backed up before n8n migration

> 💡 What you will do in this lesson: Configure your Chatflow for public access, create a secure public URL using the ngrok Docker container to expose your local Flowise instance, test the public URL, and prepare the three sharing formats you will use during your Sprint 4 presentation.

## Why this step comes now
Contigo GmbH's support agent is fully built, tested, and secured. The final step before the presentation is making it accessible to people outside your local machine. Your Flowise instance runs at http://localhost:3000 which means only you can access it. Your classmates, instructor, and any external reviewers cannot reach it from their own devices.
This lesson solves that. By the end, your Chatflow will be accessible via a public URL that anyone with the link can use during your presentation without requiring you to deploy to a cloud server or change your local setup.

## Understanding Flowise's sharing options
Flowise supports three deployment channels for a completed Chatflow:
- Public chat URL: A full-page chat interface anyone can open in their browser.
- Embed widget: An HTML or React snippet that embeds a chat bubble into any webpage.
- REST API endpoint: A programmatic endpoint for integrating the Chatflow into an application.
For the Sprint 4 presentation you will use the public chat URL. This is the simplest option that gives your audience a full interactive chat interface in their browser. The embed widget and API endpoint are the correct options for integrating the agent into a real website or application

## The local access problem
Your Flowise instance is running inside a Docker container on your local machine at http://localhost:3000. This address is only reachable from your own machine. No one else can connect to it from outside.
To make it temporarily accessible for the presentation you will use ngrok. This is a tunneling tool that creates a secure public URL and forwards all traffic through it to your local Flowise instance. The URL is temporary (it expires when you stop ngrok) which is appropriate for a presentation context.
Since ngrok has an official Docker image, no separate installation is required. It runs as a fourth Docker container alongside Flowise, Qdrant, and your existing setup.

### Step 1: Create a free ngrok account
Go to ngrok.com and create a free account. Once signed in, navigate to your ngrok dashboard at dashboard.ngrok.com/get-started/your-authtoken and copy your auth token. You will need this in Step 3. This is the only setup step required. Everything else runs through Docker.
![image]((notion-hosted file))

### Step 2: Start your local environment
Make sure Flowise and Qdrant are both running before creating the tunnel. In your terminal run:
```powershell
docker start flowise
docker start qdrant
```
Verify Flowise is accessible at http://localhost:3000 before proceeding. If it does not load, check that Docker Desktop is running and both containers are active.

### Step 3: Start the ngrok tunnel via Docker
In a new terminal window, run the following command. You only need to do this once. Replace YOUR_AUTH_TOKEN with the token you copied from your ngrok dashboard:
```powershell
docker run --rm -p 4040:4040 -e NGROK_AUTHTOKEN=PASTE YOUR TOKEN ngrok/ngrok:latest http host.docker.internal:3000
```
> ➡️ It might take a while to load which is normal. You can continue to review or work on other items while the installation occurs. 
Check the Docker Desktop and you will see that ngrok is working. Go to the  http://localhost:4040 in your browser to see the ngrok inspection dashboard, which shows all incoming requests in real time. This is useful during the presentation to demonstrate that the agent is receiving and responding to live traffic.
Go to the Headers section.
![image]((notion-hosted file))
Look down until you see the host section. This is your public URL:
![image]((notion-hosted file))
Copy and paste the link to your browser. You will see the screen below. Select ‘Visit Site’ and you will be redirected back to the Flowise. Login to your account. Once you login, you will not see the chatbot yet. We need to set this up.
![image]((notion-hosted file))

### Step 4: Get your Chatflow's public chat URL
Open your Flowise dashboard at http://localhost:3000. Open your Chatflow canvas. In the top right corner click the API Endpoint icon.
![image]((notion-hosted file))
Turn the toggle on for Make Public. Go to the Share Chatbot tab and you will see a shareable link in the format: http://localhost:3000/chatbot/YOUR-CHATFLOW-ID
![image]((notion-hosted file))
The alphanumeric code (FlowiseID) is your shareable link.
Open a browser and paste the following:
```html
ngrok browser URL/chatbot/FlowiseID
```
It will then appear as follows:
![image]((notion-hosted file))
> ⚠️  Important: Do not close this terminal window during the presentation. If the ngrok container stops, the public URL stops working immediately. On the free ngrok plan, the public URL changes every time you restart the tunnel. Generate it immediately before the presentation and share it then.

### Step 5: Test the public URL
Open the public URL in a different browser or ask someone on a different device to open it. 
- Send a test message: "What documents do I need for an SME loan application?"
- Expected behaviour: The agent responds with a specific answer drawn from the Qdrant knowledge base. The full Chatflow (memory, retrieval, tools, and guardrails) is active and accessible through the public URL exactly as it is on your local canvas.
✅ Pass: Public URL loads correctly and agent responds as expected.
❌ Fail: If the URL does not load, check that ngrok is still running in your terminal and that Flowise is accessible at http://localhost:3000. If the URL loads but the agent fails to respond, check that Qdrant is running at http://localhost:6333/dashboard.

### Step 6: Close public access after the presentation
After your presentation is complete, stop the ngrok container by pressing Ctrl+C in the terminal window where it is running. This immediately closes the public URL and removes all external access to your local Flowise instance.
> ➡️ Why this matters: Your Chatflow processes Contigo client data. Leaving a public tunnel open after the presentation exposes your agent to unsolicited queries. Stopping ngrok is a one-keystroke action that eliminates that exposure entirely.

## Checklist: Confirm before the presentation
Run through this checklist immediately before the presentation begins. The ngrok URL changes on every restart so it must be generated fresh on the day.
- [ ] Docker Desktop open and running
- [ ] docker start flowise confirmed
- [ ] docker start qdrant confirmed
- [ ] Flowise accessible at http://localhost:3000
- [ ] ngrok Docker container started with correct auth token
- [ ] ngrok public URL visible in terminal output
- [ ] ngrok inspection dashboard accessible at http://localhost:4040
- [ ] Public Chatflow URL constructed by replacing localhost:3000 with ngrok URL
- [ ] Public URL tested in a second browser — agent responding correctly
- [ ] ngrok terminal window kept open for the duration of the presentation
- [ ] ngrok stopped with Ctrl+C immediately after presentation ends

Updated session startup sequence
From this point forward your full startup sequence for any session — including presentation day — is:
1. Open Docker Desktop
1. docker start flowise
1. docker start qdrant
1. For presentation only: run the ngrok Docker command in a new terminal window
  1. docker run --rm -p 4040:4040 -e NGROK_AUTHTOKEN=YOUR_AUTH_TOKEN ngrok/ngrok:latest http host.docker.internal:3000
1. Open http://localhost:3000 for Flowise
1. Open http://localhost:6333/dashboard to verify Qdrant is running
1. For presentation only: open http://localhost:4040 to verify the ngrok tunnel is active

> 💡 Takeaway: 
  Making your Chatflow publicly accessible transforms a local build into a demonstrable product. The ngrok Docker container gives you a temporary public URL in one command. 
  The three sharing formats you now have available represent the three deployment paths a production Chatflow would take to reach real users.
