# Connecting the Project Agents

Notion page: https://app.notion.com/p/Connecting-the-Project-Agents-38d9418319f38037ba13d11a670815a2
Backed up before n8n migration

Throughout the course, you explored the individual building blocks of the arXiv research assistant — communication protocols in Sprint 1, orchestration patterns in Sprint 2, and resilience patterns in Sprint 3. In the previous Sprint 4 lessons, you extended the baseline agent with a Research Summary Agent, evaluated the extended workflow, and debugged failures across protocol and orchestration layers.
Now it is time to bring those pieces together into the complete project.
In this lesson, you will create the complete arXiv research assistant by assembling the agents and integrations into one orchestrated workflow.
By the end of the lesson, your project should be able to receive a user request, route it to the appropriate specialist, use external tools when needed, recover from temporary failures, and return a response to the user.

## Your task
Create the complete workflow for your arXiv research assistant.
The final workflow should include:
- an Intake Agent
- one or more Specialist Agents
- an orchestration layer
- the MCP-enabled tools required by your project
- agent-to-agent delegation
- retry and fallback logic where appropriate
The exact implementation may differ depending on your project design, but the workflow should demonstrate all of these capabilities working together.

## Step 1: Create the project structure
Start a new AgentFlow for your project.
Create the high-level workflow that represents the complete customer journey, beginning with the user request and ending with the final response.
At this stage, focus on the overall architecture rather than the detailed configuration of each node.

## Step 2: Add the Intake Agent
Add the Intake Agent to your workflow.
This agent should receive the user's request, determine what type of issue is being reported, and prepare the request for delegation.
The Intake Agent should focus on understanding the request rather than solving it.

## Step 3: Add the Specialist Agents
Create the specialist agents required by your project.
For example, your workflow might include agents responsible for:
- Billing
- Technical Support
- Account Management
- Security
Each specialist should have a clearly defined responsibility.
Avoid giving multiple agents overlapping roles whenever possible.

## Step 4: Configure the orchestration
Connect the agents using the orchestration pattern you selected during the project design.
Verify that requests are routed to the correct specialist and that each agent performs only the task assigned to it.
If your workflow contains multiple specialist agents, ensure the orchestration can delegate work appropriately.

## Step 5: Connect the MCP-enabled tools
Connect the MCP-enabled tool or tools required by your project.
Depending on your design, these tools may provide access to external data, documentation, repositories, APIs, or other services.
Verify that the appropriate specialist agent can access the required tool when needed.

## Step 6: Configure agent-to-agent delegation
Configure the workflow so agents can delegate work to one another.
The receiving agent should have enough context to complete its task without asking the user to repeat information that has already been collected.
Each agent should complete its specialized task before returning the result to the workflow.

## Step 7: Add resilience
Review the workflow and identify the steps where failures are most likely to occur.
Where appropriate, add:
- retry logic for temporary failures
- fallback paths when retries are exhausted
- user-friendly responses when recovery is not possible
Not every node requires resilience. Focus on the parts of the workflow where failures would have the greatest impact.

## Step 8: Test the complete workflow
Run your project using several different support requests.
For each request, verify that:
- the Intake Agent correctly understands the request
- the request is delegated to the correct specialist
- MCP-enabled tools are used when appropriate
- agent-to-agent delegation works as expected
- retry and fallback behavior operate correctly
- the user receives a complete response
Test both successful requests and at least one scenario that triggers your resilience logic.

## Common issues
As you test the workflow, you may encounter some common integration problems:
- Requests are routed to the wrong specialist.
- Multiple agents perform the same task.
- MCP tools are connected but never used.
- Context is lost during agent handoff.
- Retry loops never terminate.
- Fallback paths bypass important workflow steps.
If you encounter one of these issues, trace the execution path through your workflow before making changes.

## Summary
You have assembled the complete arXiv research assistant by integrating specialized agents, orchestration, MCP-enabled tools, agent-to-agent delegation, and resilience mechanisms into a single workflow. Rather than developing individual components in isolation, you focused on making the entire system operate as one coordinated solution—a key milestone in building production-ready AI agent systems.
