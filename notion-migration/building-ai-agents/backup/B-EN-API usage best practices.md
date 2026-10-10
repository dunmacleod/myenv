# API usage best practices

Notion page: https://app.notion.com/p/API-usage-best-practices-3669418319f38031b05ccb6f6dcff26c
Backed up before n8n migration

>  This lesson uses Gemini as the main example, but the underlying API usage logic applies broadly to other AI models and providers as well. Focus on the principles: structuring requests clearly, handling responses reliably, managing errors, and designing workflows that can be adapted to different model APIs.
> 💡 What you will understand by the end of this lesson: How the Gemini API works in a business context, what rate limits and cost structures apply, and how to make responsible model selection decisions before building anything.
## Before you generate a single API key
Meridian Consulting's development team is ready to start building. Before anyone creates credentials or connects a model node in Flowise, the team lead calls a brief alignment session. The reason is straightforward: in previous projects, developers have jumped straight into configuration without understanding the rules of the platform they are building on. The result has been unexpected billing spikes, agents that crash under load because they hit rate limits mid-conversation, and one incident where a prototype running an uncontrolled loop consumed an entire month's API budget in forty minutes.
Understanding how the Gemini API works (its pricing model, its rate limits, its data handling policies, and when to use it versus a consumer subscription) is part of the necessary preparations before starting any project. 

## API integration versus consumer subscription
The first distinction the team needs to make is between two different ways of accessing Gemini.
1. AI web applications are designed for individual users having manual conversations. It is useful for exploration and one-off queries, but it cannot be embedded into applications, cannot be triggered programmatically, and cannot be integrated into a Flowise node graph.
1. The OpenRouter and Gemini API are the developer-facing programmatic interface. It is what allows Meridian's Flowise agent to send a prompt, receive a structured response, call a tool, and chain multiple reasoning steps together without human intervention. Any agentic workflow requires the API. The consumer interface is irrelevant once building begins.

## Rate limits: Designing around the boundaries
The Gemini API enforces rate limits that vary by model and pricing tier. Exceeding these limits causes the API to reject requests and return a 429 error which, in a live agent workflow, means the agent fails mid-conversation.
On the free tier, the limits are generous enough for development and testing but insufficient for production traffic. Gemini 2.5 Flash and Gemini 2.5 Flash-Lite are available on the free tier with request limits suitable for development and testing. Gemini 2.5 Pro is available on the free tier but with more conservative limits, making it unsuitable for agentic workflows that require rapid sequential calls. This course uses Gemini 2.5 Flash and Flash-Lite on the free tier, which provide sufficient headroom for development, building, and testing throughout all four sprints.
For Meridian's production deployment, where multiple consultants may query the agent simultaneously throughout the working day, a paid tier with higher rate limits will be necessary. Planning for this before deployment is a basic operational responsibility.

## Cost structure: Model selection as a financial decision
The Gemini API charges per token. Each unit of text processed, whether input or output. The choice of model has a direct and significant impact on operational cost.
Gemini 2.5 Flash costs approximately $0.30 per million input tokens and $2.50 per million output tokens. Gemini 2.5 Pro costs approximately $1.25 per million input tokens and $10.00 per million output tokens for standard prompts making it significantly more expensive for routine queries. Gemini 2.5 Flash-Lite is the most cost-efficient option at $0.10 per million input tokens and $0.40 per million output tokens, making it well-suited for high-frequency, lightweight steps within a larger workflow where deep reasoning is not required.
[TABLE]
  | Model | Input cost per 1M tokens (USD) | Output cost per 1M tokens (USD) | Best suited for |
  | Gemini 2.5 Flash-Lite | ~$0.10 | ~$0.40 | High-volume, routine queries |
  | Gemini 2.5 Flash | ~$0.30 | ~$2.50 | Standard agentic workflows |
  | Gemini 2.5 Pro | ~$1.25 | ~$10.00 | Complex, long-document reasoning |
> 💻 For current model specifications and up-to-date pricing, refer to the official Gemini API documentation at the following:
  - Gemini Models: ai.google.dev/gemini-api/docs/models 
  - Gemini Pricing: ai.google.dev/gemini-api/docs/pricing

## Data privacy on the free tier
One consideration that matters particularly for Meridian is the data handling policy on the free tier. Content processed through the Gemini API on the free tier may be used by Google to improve its models. This suits development with test data. For a consultancy handling sensitive client operational data, this is unacceptable.
Upgrading to a paid tier removes this data usage. Content processed on paid tiers is not used for model training. For any deployment handling real client data, the paid tier is not optional. This is a decision that should be made before the first real document is loaded into the system, not after.

## Check for Understanding
>  Meridian's agent is running on the Gemini API free tier and begins failing mid-conversation during peak usage hours. What is the most likely cause?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/2c158824-591c-4042-849e-1de8394862a8

> 💡 Takeaway: 
  The Gemini API is the programmatic interface that makes agentic workflows possible, but it operates within boundaries that must be understood before building begins. Rate limits determine how many requests the agent can make per minute and per day before the API begins rejecting them. Model selection determines what it costs to run. Data handling policies determine whether it is safe to process real client data. 
  Getting these decisions right before the first node is connected saves significant operational pain later.
