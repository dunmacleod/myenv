# Custom Logic with Custom Function Node

Notion page: https://app.notion.com/p/Custom-Logic-with-Custom-Function-Node-3669418319f380c5b881e1093a363bbe
Backed up before n8n migration

> ⚠️ What you will work on in this lesson: Understand what the Custom Function Node does, when to use it, and how it has been used throughout the Meridian build.

## Setting the scene
Throughout Sprint 2 and Sprint 3, the Custom Function Node has appeared at key moments in the Meridian canvas — incrementing the retry counter in the Loop Node lesson and parsing the engagement list in the Iteration Node lesson. In both cases it handled a specific transformation that no other node could perform cleanly.
This lesson steps back and explains the Custom Function Node as a concept (what it is, when it is the right tool, and what its boundaries are) before students apply it more independently in the Sprint 3 assessment.

## What the Custom Function Node does
The Custom Function Node provides a mechanism for executing custom server-side JavaScript code within the workflow. It allows writing and running arbitrary JavaScript snippets, offering an effective way to implement complex data transformations, bespoke business logic, or interactions with resources not directly supported by other standard nodes.
In practical terms: When the visual nodes cannot do what the workflow needs, the Custom Function Node fills the gap with code.

### How it works
The Custom Function Node runs JavaScript on the Flowise server. It has access to three categories of data:
1. Input Variables: Values explicitly passed into the function from the canvas.
```javascript
// If you define an input variable called "retryCount"
// it is accessible as $retryCount inside the function
const count = parseInt($retryCount) || 0;
```
1. Flow context: Default variables always available.
```javascript
$flow.input        // the user's original message
$flow.sessionId    // current session ID
$flow.state        // the entire Flow State object
```
1. Flow State keys: Individual state values.
```javascript
$flow.state.retry_count
$flow.state.engagement_list
$flow.state.status_response
```
The function must return a string value at the end of its execution. If the output is a number, array, or object, it must be converted to a string before returning: 
```javascript
return String(count + 1);           // number to string
return JSON.stringify(dataArray);   // array to string
```

## When to use it
The Custom Function Node is the right choice in four situations:
[TABLE]
  | Situation | Example from the Meridian build |
  | Counter or arithmetic logic | Incrementing retry_count in the Loop Node lesson |
  | Data parsing or transformation | Parsing the engagement list JSON in the Iteration Node lesson |
  | String manipulation | Extracting a specific field from an API response |
  | Conditional logic too complex for the Condition Node | Evaluating multiple fields from Flow State simultaneously |
It is not the right choice when a standard node already handles the task. Using a Custom Function Node to make an HTTP call when the HTTP Node exists, or to retrieve from a Document Store when the Retriever Node exists, adds unnecessary complexity and makes the canvas harder to read.

## What it cannot do
Two important points to make:
- It cannot create new Flow State keys. New keys cannot be created by operational nodes, only pre-defined keys can be updated. All keys the Custom Function Node writes to must be initialised in the Start Node first.
- It cannot return non-string values directly. The output socket of the Custom Function Node always produces a string. If a downstream node expects a number or a parsed object, the transformation must happen in that downstream node, not in the Custom Function Node's return value.

### How it connects to Flow State
The Custom Function Node can both read from and write to Flow State:
Reading:
```javascript
const currentCount = parseInt($flow.state.retry_count) || 0;
```
Writing via Update Flow State:
After the function runs, the Update Flow State configuration maps the output to a pre-defined key:
[TABLE]
  | Key | Value |
  | retry_count | {{ customFunctionAgentflow_0.output }} |
This is the pattern used in the Retry Logic with Loop Node lesson, where the function returns the incremented count as a string and Update Flow State writes it back to retry_count for the Condition Node to read.

## Check for Understanding
>  A Custom Function Node returns the number 3 directly without converting it to a string. What happens?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/cd9e6ff6-d775-4ae0-aacd-b28526a7470d


> 💡 Takeaway: 
  The Custom Function Node is the escape hatch for logic that the visual node palette cannot handle. It is powerful precisely because it is unrestricted. That power comes with one firm limitation: always return a string. Every other node on the canvas expects string output from the Custom Function Node, and silent type mismatches are one of the harder failure modes to diagnose in a running flow.
