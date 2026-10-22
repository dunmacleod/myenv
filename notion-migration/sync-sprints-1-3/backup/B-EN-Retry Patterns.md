# Retry Patterns

Notion page: https://app.notion.com/p/Retry-Patterns-3889418319f38032a407cea295af9b0e
Backed up before n8n migration

Sofia adds timeouts, and the workflow stops hanging. But she notices something new: some of the timeouts are on requests that would have succeeded if given one more chance. The shipping API times out, but a moment later it works fine. The warranty database is briefly overloaded, but recovers seconds later. These are not real failures — they are temporary interruptions. Treating them as terminal failures wastes work and frustrates customers whose queries could have been answered on a second attempt.
If every temporary failure caused the entire workflow to stop, many otherwise successful processes would fail unnecessarily.
This is why orchestrated systems use retries. Instead of immediately giving up after a failed step, the workflow attempts the operation again — up to a defined limit — before deciding the failure is real.

## Why retries exist
Many failures in distributed systems are temporary.
Cascadia's warranty-claim workflow illustrates the pattern:
1. A user submits a support request.
1. A Retrieval Agent searches the knowledge base.
1. The knowledge base API temporarily times out.
1. The workflow receives an error.
At this point, the orchestrator has two choices:
- Fail the workflow immediately.
- Try the operation again.
In many real systems, the second attempt succeeds because the underlying problem was temporary.
Retries allow workflows to recover from these short-lived failures without requiring human intervention.
![image]((notion-hosted file))

![image]((notion-hosted file))
## Temporary vs permanent failures
Not every failure should be retried.
A retry makes sense when the failure is likely to disappear on its own.
[COLUMN_LIST]
  [COLUMN]
    > ⏱️ Examples of temporary failures:
      - Network interruptions
      - API timeouts
      - Temporary agent unavailability
      - Rate limiting by an external service
  [COLUMN]
    > ♾️ Examples of permanent failures:
      - Invalid user input
      - Missing required information
      - Incorrect credentials
      - Logic errors in the workflow
Retrying a permanent failure usually wastes time and resources because the result will not change.
A useful question is:
> "If I run exactly the same step again in a few seconds, is there a reasonable chance it will succeed?”

## Common retry strategies
Different systems use different retry policies.
Immediate retry means trying the operation again right after it fails, without any delay. Limited retries involve attempting the operation a fixed number of times before giving up. Retry with delay introduces a short waiting period between attempts, giving the system time to recover. Exponential backoff increases the waiting time after each failure, typically doubling the delay with each attempt.
Exponential backoff is common when working with external APIs because it reduces pressure on an already struggling service. For example:
![image]((notion-hosted file))
## Using a Loop Node for retries
A Loop Node is a workflow component that redirects execution back to an earlier step.
![image]((notion-hosted file))
While loops can be used for many purposes, one common use is implementing retries.
When a step fails, the workflow can:
1. Detect the failure.
1. Check whether another retry is allowed.
1. Loop back to the failed step.
1. Attempt the operation again.
The workflow continues until either:
- The operation succeeds.
- The maximum retry limit is reached.
The Loop Node is therefore not a retry pattern by itself. Instead, it is one of the mechanisms that can be used to implement a retry pattern.

## Key idea
Retries help orchestrated systems remain resilient when failures are temporary.
The goal is not to repeat work forever. The goal is to give a workflow a reasonable opportunity to recover from short-lived problems and continue operating successfully.
When used carefully, retries can dramatically improve reliability without requiring any human intervention.

## Summary
Failures are a normal part of orchestrated systems. However, not every failure means the workflow should stop immediately. Many failures are temporary and may disappear if the operation is attempted again.
Retries are a common resilience pattern that allows workflows to recover from short-lived issues such as network interruptions, API timeouts, or temporarily unavailable agents. Instead of failing immediately, the workflow makes another attempt before giving up.
Not all failures should be retried. Retries are most useful when there is a reasonable chance that the same operation will succeed if it is attempted again later. Permanent problems such as invalid input, missing data, or incorrect credentials usually require a different solution.
A Loop Node is one way to implement retries in an orchestrated workflow. By sending execution back to a previous step, the workflow can attempt an operation again until it either succeeds or reaches a defined retry limit.
The key idea is simple: retries help workflows recover from temporary problems automatically, making orchestrated systems more reliable and resilient.
