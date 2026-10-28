# Designing a sequential workflow

Notion page: https://app.notion.com/p/Designing-a-sequential-workflow-37f9418319f380fa80f8fb6b9f4d8c6b
Backed up before n8n migration

At Cascadia, most support requests move through a predictable series of steps — classify the message, look up the order, check the warranty, draft a response. Each step depends on the one before it. Sofia knows she does not need agents talking to each other on the fly for this. She needs a sequential workflow: one step finishes, then the next begins, using the output of the previous step.
Sequential orchestration — also called chaining — is the simplest orchestration pattern and the natural starting point when tasks have clear dependencies. This lesson shows how sequential workflows behave, when they fit, and where they run into limits.
In n8n, a sequential workflow is built by connecting nodes in execution order. Each node receives items from the previous node; downstream nodes access earlier outputs with expressions. Use an explicit field such as request_type or draft_response when a later step needs a prior result. 

## The core idea
Sequential orchestration follows a simple rule:
> One step finishes before the next step begins.
Each agent receives information, performs its task, and passes the result forward.
Think of it as a relay race.
The first runner completes their section and hands the baton to the second runner. The second runner cannot start until they receive the baton.
The same principle applies to agents.
![image]((notion-hosted file))

## Example: processing a customer request
Imagine a company receives a customer support ticket.
The workflow might look like this:
1. Request Analyzer identifies the type of request.
1. Priority Agent determines urgency.
1. Response Agent drafts a response.
1. Review Agent checks quality.
1. Final Response is returned to the customer.
Each step requires information from the previous one.
The Response Agent cannot create a reply until the request has been analyzed.
The Review Agent cannot review a response that does not yet exist.
![image]((notion-hosted file))

## How information flows
One reason sequential workflows are popular is that the flow of information is easy to follow.
Each step receives:
- The original request
- Previous outputs
- Shared workflow state
It then adds new information before passing everything forward.
In n8n, node outputs are available to downstream steps as execution data. A Set (Edit Fields) node can store named fields, and expressions can reference data from earlier nodes. Do not assume all agents share one implicit memory object. Inspect the input and output of each node in Executions.
Example State Evolution
[TABLE]
  | Step | State |
  | User Request | "My order hasn't arrived." |
  | After Analyzer | + Category = Shipping Issue |
  | After Priority Agent | + Priority = High |
  | After Response Agent | + Draft Response |
  | After Review Agent | + Approved Response |

## Why sequential orchestration is popular
Sequential workflows offer several advantages.
### Predictability
The execution path is known in advance.
You always know which step runs next.

### Easier Debugging
If something goes wrong, you can inspect each stage individually.
This makes troubleshooting much easier than in highly dynamic systems.

### Incremental Refinement
Each agent focuses on a single responsibility.
Instead of solving the entire problem at once, the system improves the result step by step.

![image]((notion-hosted file))

## When sequential orchestration works best
Sequential orchestration is most effective when tasks have clear dependencies.
Good examples include:
- Customer support workflows
- Document review pipelines
- Data extraction followed by validation
- Content generation followed by quality checks
- Multi-step approval processes
A useful test is:
> "Can the next step start before the previous step finishes?"
If the answer is no, a sequential workflow is probably appropriate.

## Limitations
Sequential workflows are simple, but they are not always the fastest option.
Because each step waits for the previous one to finish:
- Execution time increases as more steps are added.
- A failure early in the chain can block the entire workflow.
- Independent tasks cannot be processed simultaneously.
These limitations are why more advanced orchestration patterns exist, but sequential workflows remain the foundation for many production systems.

## Check for Understanding
### Question 1
>  A legal document review workflow at Cascadia has these steps:
  1. Extract text from a PDF contract.
  1. Identify clauses.
  1. Check clauses against company policies.
  1. Generate a compliance report.
  Why is sequential orchestration appropriate here?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/dbc0dac7-4cb7-4af1-a278-292f440e6509

## Summary
Sequential orchestration is the natural pattern when tasks have clear dependencies. It is predictable, easy to debug, and easy to extend one step at a time — but it is also the slowest when steps could otherwise happen in parallel. In the next lesson, we look at hierarchical orchestration, where a coordinator sits above the specialists rather than in a line with them.
