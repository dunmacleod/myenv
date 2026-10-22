# Verifying Your Local n8n Environment

Notion page: https://app.notion.com/p/Verifying-Your-Local-n8n-Environment-3669418319f3802d9f02f30fafcce39a
Backed up before n8n migration

> 💡 What you will do in this lesson: verify that your local n8n installation is stable before you begin building AI workflows.
## Why verify before building?
A configuration problem discovered in the middle of an agent exercise is easy to misdiagnose as a prompt or model problem. Before working with AI nodes, confirm the infrastructure layer first.
## Task A: Verify the container
Run docker ps. You should see a container named n8n with port 5678.
If it is stopped, run docker start n8n. If you need more detail, run docker logs n8n.
> 📸 SCREENSHOT SUGGESTION: docker ps showing the running n8n container and its port mapping.
## Task B: Verify the n8n interface
Open http://localhost:5678.
Confirm that:
- the page loads without an error;
- you can open the workflow list or Overview;
- you can create a new workflow;
- the node picker opens when you add a step.
Do not continue until these basics work.
## Task C: Run a non-AI test workflow
1. Create a new workflow.
1. Add a Manual Trigger.
1. Add an Edit Fields (Set) node.
1. Create a text field called status with the value n8n is working.
1. Connect the nodes.
1. Select Execute Workflow.
Inspect the output of the Edit Fields node and confirm the status value is present.
> 📸 SCREENSHOT SUGGESTION: workflow canvas showing Manual Trigger → Edit Fields, both nodes executed successfully.
> 📸 SCREENSHOT SUGGESTION: Output panel of the Edit Fields node showing status: n8n is working.
## Task D: Confirm persistence
Save the workflow as Environment Check.
Stop n8n, start it again, refresh localhost:5678, and confirm that the saved workflow is still there. This verifies that the n8n_data volume is working.
## Task E: Credential readiness
If you already created the OpenRouter credential, confirm that it appears in the credential selector when you add an OpenRouter Chat Model node.
Do not expose the key and do not worry about generating a model response yet. The next lesson will test the model inside a real AI workflow.
## Ready-to-build checklist
- [ ] Docker Desktop is running.
- [ ] docker ps shows the n8n container.
- [ ] localhost:5678 loads.
- [ ] A simple non-AI workflow executes successfully.
- [ ] The test workflow survives a container restart.
- [ ] OpenRouter credentials are available or the course API key is ready to add.
> 💡 Takeaway: separate infrastructure verification from agent debugging. If Docker, n8n, persistence, and basic workflow execution work first, later errors are much easier to localise.