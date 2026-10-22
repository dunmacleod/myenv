# API Usage Best Practices

Notion page: https://app.notion.com/p/API-Usage-Best-Practices-3669418319f38031b05ccb6f6dcff26c
Backed up before n8n migration

> 💡 What you will understand by the end of this lesson: how to use model APIs responsibly in n8n, protect credentials, handle common failures, and choose model settings without hard-coding assumptions that may become outdated.
## API access is different from a chat website
A consumer chat interface is designed for a person typing messages manually. An API is designed for software.
In n8n, the workflow calls the model through the OpenRouter Chat Model node. Authentication is handled by an OpenRouter credential stored in n8n.
## 1. Keep credentials out of workflow text
Never paste an API key into a prompt, a Set/Edit Fields value, a Code node, a screenshot, or a shared workflow export.
Create an n8n credential and select it from the node instead.
> 📸 SCREENSHOT SUGGESTION: the OpenRouter credential form in n8n with the API Key field hidden or blurred. Do not show a real key.
## 2. Expect API failures
Common categories include:
- 401 / authentication error: wrong, revoked, or missing key.
- 429 / rate limit: too many requests in a short period or provider quota exceeded.
- Timeout: the provider did not respond within the configured time.
- 5xx / provider error: temporary upstream failure.
The OpenRouter Chat Model node exposes options such as Timeout and Max Retries. Use them deliberately instead of assuming every request succeeds on the first attempt.
> 📸 SCREENSHOT SUGGESTION: OpenRouter Chat Model node with Timeout and Max Retries visible in the options panel.
## 3. Do not build around one permanent model name
OpenRouter exposes models available to your account and n8n loads them dynamically.
Choose the model assigned for the course. If the exact model changes later, the workflow architecture should still work.
Think about the task:
- routine classification or short answers → prefer a fast, cost-efficient model;
- complex reasoning → a stronger model may be justified;
- machine-readable output → use JSON where appropriate.
## 4. Control output size and randomness
Useful settings include:
- Maximum Number of Tokens — caps completion length.
- Sampling Temperature — higher values create more variation but less determinism.
- Response Format — text or JSON where supported.
For operational agents, start conservative: concise outputs and lower randomness are easier to test.
## 5. Treat cost and data as architectural concerns
Before production:
- estimate how many model calls one execution makes;
- keep prompts focused;
- avoid uncontrolled loops;
- log failures and retries;
- send only context that is actually needed;
- use synthetic or approved data during course work.
Before a real deployment, review the provider's data handling terms and your organisation's security requirements.
## Mini-check
- Invalid credential immediately → authentication.
- Works in testing but fails under heavy parallel use → likely rate limiting.
- Prose returned where the next node expects fields → output format or parsing design.
- Screenshot contains the full API key → rotate the key.
> 💡 Takeaway: reliable model integration is not only about getting one successful response. Protect credentials, design for failures, keep settings explicit, and make model choices that can change without forcing a workflow redesign.