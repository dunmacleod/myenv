# Verifying your local environment

Notion page: https://app.notion.com/p/Verifying-your-local-environment-3669418319f3802d9f02f30fafcce39a
Backed up before n8n migration

>  This lesson uses Gemini as the main example, but the underlying API usage logic applies broadly to other AI models and providers as well. Focus on the principles: structuring requests clearly, handling responses reliably, managing errors, and designing workflows that can be adapted to different model APIs.
> 💡 What you will work on in this lesson: Independently verify that your local Flowise environment is running correctly and that your Gemini API key is authenticating without errors before building begins.

## Why verification comes before building
Meridian Consulting's development team has installed Flowise, generated their API key, and stored it in the credentials manager. The temptation at this point is to open the canvas and start connecting nodes. That temptation should be resisted.
A broken environment discovered mid-build is significantly more disruptive than one caught before a single node has been placed. Configuration errors, credential issues, and invalid API keys all produce symptoms that are easy to misread as agent logic problems when they are actually setup problems. Verifying the environment first eliminates that category of confusion entirely.
Your task is to confirm two things:
- Your local Flowise instance is running and the dashboard is accessible
- Your API keys are active and authenticating correctly inside Flowise

## What you have been given
Local Flowise access: Your Flowise server should already be running from the previous lesson. 
If it is not running, then check the following:
- Confirm Docker Desktop is open and running. Look for the whale icon in your system tray
- Open a terminal and run docker ps to confirm the Flowise container is listed as running.
- If the container is not running, start it with docker start flowise
- If the container does not exist, rerun the full docker run command from the previous lesson.

## Useful references:
- Flowise documentation and troubleshooting: docs.flowiseai.com
- Flowise GitHub repository and open issues: github.com/FlowiseAI/Flowise
- Google AI Studio for key management: aistudio.google.com
- Gemini API reference documentation: ai.google.dev/api

## Your tasks
### Task A: Access and verify Flowise from your laptop
Navigate to http://localhost:3000 in your browser. Confirm the Flowise dashboard loads and that you can see the left-hand navigation panel. Click Agentflows and confirm the section opens without errors.
Document what you observe:
- Whether the dashboard loaded successfully
- Whether the Agentflows section opened correctly
- Any errors you encountered
Do not proceed to Task B until the Flowise dashboard is fully accessible.

### Task B: Validate the Gemini API key
Build a minimal test canvas in Agentflow v2 to confirm your credential is working:
1. Click Agentflows in the left navigation, then click + Add New.
1. On the canvas, you will already see a Start Node. Add an Agent Node, and a Direct Reply Node and connect them in sequence.
1. In the Agent Node settings, double click and open the Model section. Select Google Gemini and add your credential details.
1. Set the model to what you chose. Select Save.
1. Click the chat icon and send: Hello
If the agent responds, the key is active and authenticating correctly. If it returns an error, use the following to diagnose:
- 401 error: The key is invalid, inactive, or was not copied correctly.
- 429 error: The free tier rate limit has been exceeded; wait one minute and retry.
- 403 error: The key has a restriction blocking this type of request; check key settings in Google AI Studio.
- No response at all: Confirm all three nodes are connected by visible edges and the canvas has been saved before testing.
Document your test message and the response you received. If the key returns an error, diagnose and resolve it using the error code guidance and references above before moving to the next lesson.
![image]((notion-hosted file))

## Check for Understanding
>  A Meridian developer opens http://localhost:3000 and the page does not load. Docker Desktop is installed. What is the most likely cause and correct first step?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/bc5f1d6e-27ce-4737-8208-28ee7b0c5d82

> 💡 Takeaway: 
  Verifying the environment is the first real test of your setup. An agent that fails because of an infrastructure problem looks identical to one that fails because of a logic problem. 
  Catching setup issues now before a single business rule has been written into the canvas is what keeps debugging fast and focused for the rest of the course.
