# Project submission information

Notion page: https://app.notion.com/p/Project-submission-information-3f09418319f381539574ea2c09ac3da8
Backed up before n8n migration

This page is the authoritative checklist for the general AI Capstone submission. It covers the artefacts every learner submits, whether the project was completed individually or in a group and whether the workflow runs locally or is externally hosted.
External hosting is optional. A working execution, complete evidence, and publication of the portfolio artefacts are required.
## 1. Tasks
Four sprints of work, each producing artefacts that build on the last. The submission draws on all four.
1. Sprint 1 — Problem scoping and design. Choose a business problem, or a fallback option, and scope it. Define measurable success criteria. Decide which concepts the build needs (RAG, agent, agentic workflow, human-in-the-loop) and which implementation path fits. Produce the architecture and the build plan, and take them through peer review.
1. Sprint 2 — Building the core system. Set up the environment and connect every data source, real or clearly labelled synthetic. Build a thin working slice end to end, iterate until it is reliable, and integrate the AI components the architecture called for. Run the mid-build checkpoint of 5–10 diagnostic cases and adjust the plan against what it shows.
1. Sprint 3 — Completing, governing and evaluating. Add safety, reliability and human-oversight layers. Run the formal evaluation of at least 10 distinct scenarios with the complete record. Identify the top failure mode and write the improvement plan. Complete the governance work: EU AI Act classification, data protection decisions, and the responsible-AI checklist. Publish the project artefacts to GitHub.
1. Sprint 4 — Showcase and reflection. Calculate the ROI with measurements and assumptions kept visibly separate. Write the one-page business case. Prepare the presentation, the live demonstration, and your answers to the business and technical questions it will invite.
## 2. Confirm the project is complete
Before packaging the submission, confirm that the final workflow:
- runs end to end on a representative input;
- produces the expected output;
- matches the exported workflow JSON;
- has completed governance and security checks;
- has formal evaluation evidence from at least 10 distinct scenarios;
- contains no exposed credential, API key, private token, or confidential record.
## 3. Project artefacts
### Technical artefacts
Include:
- the exported n8n workflow .json;
- the GitHub repository link;
- the README/project description;
- the final architecture diagram;
- screenshots or a short demo recording showing successful execution;
- import/review instructions for the workflow;
- an optional hosted-system link, only if you chose external hosting.
The architecture diagram must show the actual components and data flow in the final workflow. A table or numbered list may support it, but does not replace it.
### Evidence and reasoning
Include:
- the formal test-scenario record with all required fields;
- the evaluation report;
- the top failure mode and improvement plan;
- the responsible-AI, privacy, security, and governance evidence relevant to the project;
- the ROI calculation and one-page business case;
- known limitations and any disclosed mock or synthetic-data assumptions.
Keep measurements distinct from assumptions. Clearly label synthetic inputs, remaining mocks, unquantifiable costs, and any optional feature that was not completed.
### Written summary
A short PDF of one to two pages that ties the whole project together. Include:
- a one-paragraph problem framing — what the business problem is and why it was worth automating;
- a one-paragraph solution overview — what the workflow does and what shape it has;
- two or three bullets naming the most interesting decisions you made across the four sprints, each with the alternative you considered and rejected;
- a one-paragraph reflection on what your testing revealed and one limitation you could not fully resolve.
The summary is for someone who has not seen your presentation. It should read independently.
## 4. Presentation
Target 5–7 minutes for the presentation itself, plus Q&A. Your instructor confirms the exact slot for the session.
The presentation must include:
- the problem and why it matters;
- a live demonstration of the workflow;
- the final architecture diagram;
- the build and governance decisions worth defending;
- evaluation results, including the top failure mode;
- the business case, limitations, and next improvement.
Prepare a safe fallback screenshot or recording in case the live environment fails. The fallback supports the presentation but does not replace preparation of the working demonstration.
## 5. Quality expectations
The project is evaluated through the presentation and the credibility of the supporting evidence. Reviewers look for:
- a clear, appropriately scoped problem;
- a working and explainable workflow;
- an accurate architecture diagram;
- complete and credible testing evidence;
- honest conclusions and limitations;
- responsible treatment of data, access, secrets, and human oversight;
- a defensible business case;
- the ability to explain and defend the major decisions.
Code Clinic attendance, extra artefacts beyond the required list, and decorative slide polish are not graded requirements.
## 6. Preparation checklist
Complete these before the live session. Do not leave any item for the session itself.
- [ ] The workflow runs and the evidence shows the input, execution, and output.
- [ ] The exported .json matches the final workflow.
- [ ] The GitHub repository is public and complete.
- [ ] The README includes the problem, solution, architecture, review/run instructions, evidence, and limitations.
- [ ] The architecture diagram matches the workflow as built.
- [ ] The formal evaluation contains at least 10 complete test records.
- [ ] The evaluation report, business case, ROI, and improvement plan are included.
- [ ] The presentation includes a live demonstration and fits the target range.
- [ ] Every required file is attached in Codio, and every submitted GitHub or optional hosted-system link opens in a private browser window.
- [ ] No secret or private record is exposed.
## 7. Submit in Codio
Submit the complete project package through the Course 6 submission activity in Codio, following the same submission process used for the other programme projects.
Include the written project summary as a PDF of approximately 1–2 pages. Upload the required files and provide the GitHub repository link and any optional hosted-system link in the fields provided by the Codio activity.
Before submitting, reopen the Codio submission and confirm that every required file is attached and every link is complete. Test the GitHub repository and any optional hosted-system link in a private or incognito browser window.
Do not include credentials, API keys, private tokens, private organisational records, or any other secret in the workflow export, repository, screenshots, or documents.
Follow any operational instruction supplied by your instructor without changing the required artefact list above.
## Final check
Before you present, read through your architecture diagram and the evaluation report and ask these questions. They are the questions a reviewer will ask during your defense.
- Can you trace one representative input through the diagram from trigger to output, naming what each component does to it?
- Does the diagram match the workflow as it stands now, not as it stood when you designed it?
- Can you say what the system does when the input is malformed, an integration fails, or the AI component is not confident — and point to where that is built?
- Can you name one test that changed your design, and say what it changed?
- Can you state your top failure mode out loud without softening it, and say what you would do about it next?
- If someone asks why you chose this approach over a simpler one, do you have a specific property of your business problem to point at, rather than a general principle?
If any of these produce hesitation, that is useful information. Spend the time before the session on whichever hesitated most.
## Summary
Your submission should let a reviewer verify three things without guessing: the workflow works, the evidence supports your claims, and you understand the decisions and limitations well enough to defend them. Package only confirmed artefacts and keep optional hosting clearly separate from the required Capstone evidence.