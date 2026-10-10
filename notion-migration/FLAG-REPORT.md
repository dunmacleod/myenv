# n8n migration — flag report for LMS follow-up

Content from the two **(new, n8n)** draft courses was copied verbatim into the two **live** courses.
No pages were created, moved or deleted: every lesson kept its existing Notion page ID and URL, so all
LMS/campus links into the live courses still resolve. Row counts in all four databases are unchanged.

| | Building AI Agents | Advanced Agent Systems |
|---|---|---|
| Sprint copied | Module A `1-How Agents Remember`, Module B `1-Setting up Flowise and Gemini Stack` | Module A `Sprint 1: Agent Architecture Foundations`, Module B `Sprint1: Agent Communication & Integration Protocols` |
| Lessons in scope | 56 | 45 |
| Bodies replaced | 36 | 40 |
| Skipped — already identical | 12 | 0 |
| Skipped — section pages with no body | 8 | 5 |
| Verified identical to source | 35 of 36 | 38 of 40 |
| Images re-hosted in the live workspace | 103 | 63 |
| Titles renamed | 21 | 4 |
| Internal cross-links remapped to live pages | 0 (none present) | 117 |
| Errors | 0 | 0 |

Backups of every replaced page (JSON + readable Markdown) are in `building-ai-agents/backup/`
and `advanced-agent-systems/backup/`. Notion page history also holds the pre-migration version.

---

## 1. Quiz embeds removed — needs re-adding in the LMS

This is the item with student-visible impact. The new draft pages carry **no** Masterschool campus
quiz embeds, while the live pages did. Per the agreed "copy source exactly" rule they were removed.
**30 embeds across 22 lessons** in Building AI Agents and
**14 across 10 lessons** in Advanced Agent Systems.

### Building AI Agents

| Module | Lang | Lesson | Live page | Removed quiz URL |
|---|---|---|---|---|
| A | EN | Introduction to n8n | [open](https://app.notion.com/p/Introduction-to-Flowise-36c9418319f3801cb4eadc8b4518971f) | `https://app.masterschool.com/campus/multi-choice-question/7f4de909-ab10-4b9d-8782-8b736cdc9179` |
| A | DE | Einführung in Flowise | [open](https://app.notion.com/p/Einf-hrung-in-Flowise-3779418319f380ea99fcf1f781cb6d1b) | `https://app.masterschool.com/campus/multi-choice-question/b1994c12-c811-4412-9e10-6cae3d22a608` |
| A | EN | Context-window Management | [open](https://app.notion.com/p/Context-window-Management-3669418319f380c2b5a1c98b08a2d64e) | `https://app.masterschool.com/campus/multi-choice-question/d452570f-8d0d-46d4-b71b-e65e1a0a35d4` |
| A | EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/014a6fcb-0cd1-4e49-9ea7-bf568e69fee7` |
| A | DE | Context-Window-Management | [open](https://app.notion.com/p/Context-Window-Management-3779418319f380b8b427c33444001093) | `https://app.masterschool.com/campus/multi-choice-question/773365c6-1c21-43c9-bc81-053921f21463` |
| A | DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/e0fae8ad-f0c8-412c-bc82-0be11cda56cd` |
| A | EN | Memory Best Practices | [open](https://app.notion.com/p/Memory-Best-Practices-3669418319f380ceaf6cfc32055e0f26) | `https://app.masterschool.com/campus/multi-choice-question/7486b98a-16cc-4bf1-b8bb-de8327ae6ff8` |
| A | DE | Best Practices für Memory | [open](https://app.notion.com/p/Memory-Best-Practices-3779418319f3801cb3c8d7f41e467fe8) | `https://app.masterschool.com/campus/multi-choice-question/70486b01-e24a-4ab1-b969-464671e71314` |
| A | EN | Persistent Memory: What Production Looks Like | [open](https://app.notion.com/p/Persistent-Memory-What-Production-Looks-Like-3669418319f380d5801ac7386f80ee5f) | `https://app.masterschool.com/campus/multi-choice-question/a8463410-1029-4d4e-a47e-338cf6643c2a` |
| A | DE | Persistent Memory: Wie Production aussieht | [open](https://app.notion.com/p/Persistent-Memory-Wie-Production-aussieht-3779418319f3805080bbedb5f1c6e466) | `https://app.masterschool.com/campus/multi-choice-question/23725f3f-6e09-4b36-bdbb-201cca00b015` |
| B | EN | Testing and Handling Edge Cases | [open](https://app.notion.com/p/Testing-and-Handling-Edge-Cases-3669418319f3808a92d3e98347ab12c6) | `https://app.masterschool.com/campus/multi-choice-question/184959d4-7b5b-4c2a-9970-d455a3f66604` |
| B | DE | Edge Cases testen und behandeln | [open](https://app.notion.com/p/Edge-Cases-testen-und-behandeln-3789418319f38090a06bd079da141789) | `https://app.masterschool.com/campus/multi-choice-question/3de1bf6b-cd21-42a1-8312-045fea01db69` |
| B | EN | The n8n Interface | [open](https://app.notion.com/p/The-Flowise-Interface-3669418319f3800ba25ad33db386851b) | `https://app.masterschool.com/campus/multi-choice-question/133f1b95-0463-45df-b1fc-dd3736f1a23e` |
| B | DE | Die n8n-Oberfläche | [open](https://app.notion.com/p/Die-Flowise-Oberfl-che-3789418319f380ab9000f5a81eb96a64) | `https://app.masterschool.com/campus/multi-choice-question/6efafc44-1c44-49a0-9406-fc26cd4a0afd` |
| B | EN | Your First AI-Powered n8n Workflow | [open](https://app.notion.com/p/First-AI-Powered-Agentflow-v2-3669418319f38082ae3ef82ece0ce65b) | `https://app.masterschool.com/campus/multi-choice-question/3a22830f-d34d-415d-9612-c2de1a9c1627` |
| B | DE | Dein erster KI-gestützter n8n-Workflow | [open](https://app.notion.com/p/Erster-Gemini-gest-tzter-Agentflow-v2-3789418319f3806fa588f57b9f1eacb8) | `https://app.masterschool.com/campus/multi-choice-question/8f4dfde2-7dbd-4c94-a202-b8ff140e500a` |
| B | EN | n8n and AI Agent Checkpoint | [open](https://app.notion.com/p/Flowise-and-AI-Agent-Checkpoint-3669418319f380468657c791cf3e8aab) | `https://app.masterschool.com/campus/multi-choice-question/89c0f8ed-4c70-4b6a-8802-0428574f5db9` |
| B | EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/650527fe-ae9d-46fd-8cb5-f2154ed3d2b6` |
| B | EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/aa5fe3b7-7f5e-49b2-8bc6-4b916923c623` |
| B | EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/f8df0c78-b566-4e64-9ea1-2ecdeafcda5e` |
| B | DE | n8n- und KI-Agenten-Checkpoint | [open](https://app.notion.com/p/Flowise-und-Gemini-Agenten-Checkpoint-3789418319f38062ad29f4755eae397a) | `https://app.masterschool.com/campus/multi-choice-question/fdf8bee4-ccfd-488d-ace0-979cda7f64e9` |
| B | DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/667dd559-beb8-4036-8051-31b82b9ac60e` |
| B | DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/804d931d-b428-492c-98a2-cdcb69a1c3c1` |
| B | DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/cc55e01c-d5b4-45e4-9af5-1f6e175bcac0` |
| B | EN | n8n, OpenRouter, and the AI Stack | [open](https://app.notion.com/p/Flowise-OpenRouter-and-Gemini-Stack-3669418319f38016bf6eef4efd60b760) | `https://app.masterschool.com/campus/multi-choice-question/77c31602-446c-474f-bc67-17d9fe211962` |
| B | DE | n8n, OpenRouter und der KI-Stack | [open](https://app.notion.com/p/Flowise-und-Gemini-Stack-3789418319f38044ad03f6374b5df510) | `https://app.masterschool.com/campus/multi-choice-question/3e31c67a-14a9-4883-8f33-da319e108a7c` |
| B | EN | API Usage Best Practices | [open](https://app.notion.com/p/API-usage-best-practices-3669418319f38031b05ccb6f6dcff26c) | `https://app.masterschool.com/campus/multi-choice-question/2c158824-591c-4042-849e-1de8394862a8` |
| B | DE | Best Practices für API-Nutzung | [open](https://app.notion.com/p/Best-Practices-f-r-API-Nutzung-3789418319f380b8be94c5ab4f157674) | `https://app.masterschool.com/campus/multi-choice-question/f92ddeec-e485-4aa6-85b0-aee8c3db46fd` |
| B | EN | Verifying Your Local n8n Environment | [open](https://app.notion.com/p/Verifying-your-local-environment-3669418319f3802d9f02f30fafcce39a) | `https://app.masterschool.com/campus/multi-choice-question/bc5f1d6e-27ce-4737-8208-28ee7b0c5d82` |
| B | DE | Deine lokale n8n-Umgebung überprüfen | [open](https://app.notion.com/p/Deine-lokale-Umgebung-berpr-fen-3789418319f38080a767f0b162a255e8) | `https://app.masterschool.com/campus/multi-choice-question/dae61ac1-4a5c-4f82-94e6-69e3f6b34e98` |

### Advanced Agent Systems

| Module | Lang | Lesson | Live page | Removed quiz URL |
|---|---|---|---|---|
| A | EN | Common architecture mistakes | [open](https://app.notion.com/p/Common-architecture-mistakes-3849418319f380c0a203c1da9d6781bf) | `https://app.masterschool.com/campus/multi-choice-question/5397f76c-6169-4249-9124-ac63df8268d5` |
| A | DE | Häufige Architekturfehler | [open](https://app.notion.com/p/H-ufige-Architekturfehler-bbe9418319f38300879f0159bd050711) | `https://app.masterschool.com/campus/multi-choice-question/12bbb391-2b35-4cc8-9953-db9932970586` |
| A | EN | Practical architecture patterns | [open](https://app.notion.com/p/Practical-architecture-patterns-3849418319f3807997f0fbe3b024f6bd) | `https://app.masterschool.com/campus/multi-choice-question/d9030af1-3cc8-4129-92dd-3e8fed6b8aa4` |
| A | DE | Praktische Architekturmuster | [open](https://app.notion.com/p/Praktische-Architekturmuster-6d59418319f38275b57181c29cf2bdd5) | `https://app.masterschool.com/campus/multi-choice-question/7d9db5bc-8ba6-4d1b-b53a-e91531f4eb9b` |
| B | EN | What A2A is and when it matters | [open](https://app.notion.com/p/What-A2A-is-and-when-it-matters-37e9418319f3802c989cea08cecef902) | `https://app.masterschool.com/campus/multi-choice-question/90896912-752b-4872-9d5f-6a13fa4e15df` |
| B | DE | Was A2A ist und wann es relevant wird | [open](https://app.notion.com/p/Was-A2A-ist-und-wann-es-relevant-wird-efd9418319f383f58223015d972a787a) | `https://app.masterschool.com/campus/multi-choice-question/2040e9e9-5212-4b7d-98db-2740a2a9476a` |
| B | EN | What MCP is and the problem it solves | [open](https://app.notion.com/p/What-MCP-is-and-the-problem-it-solves-37e9418319f3807dab30cea98d38d2b5) | `https://app.masterschool.com/campus/multi-choice-question/83293b5d-051f-4818-91c2-3a75451acf74` |
| B | DE | Was MCP ist und welches Problem es löst | [open](https://app.notion.com/p/Was-MCP-ist-und-welches-Problem-es-l-st-6409418319f38213af3401d82131e353) | `https://app.masterschool.com/campus/multi-choice-question/3e5c66c1-c6bd-44c6-90eb-3e452ddf315e` |
| B | EN | Why agents need structured communication | [open](https://app.notion.com/p/Why-agents-need-structured-communication-37e9418319f3805bb423fcdd5799e88f) | `https://app.masterschool.com/campus/multi-choice-question/4c73dd47-d335-4c6f-9ff7-2e9172e6608f` |
| B | EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/4f6c7631-92f2-4a58-a52c-26fa71f75b1d` |
| B | EN |  |  | `https://app.masterschool.com/campus/multi-choice-question/d89b4fa7-1ad5-41b9-9852-d581c1532823` |
| B | DE | Warum Agenten strukturierte Kommunikation brauchen | [open](https://app.notion.com/p/Warum-Agenten-strukturierte-Kommunikation-brauchen-c539418319f3836ca161817f320d5f74) | `https://app.masterschool.com/campus/multi-choice-question/140275a8-e1b7-413e-840c-ad49de56e90a` |
| B | DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/85cf10fe-77db-47ea-8b28-a519fbcea4a1` |
| B | DE |  |  | `https://app.masterschool.com/campus/multi-choice-question/a3140898-e8ff-41a1-8098-dd435177ee26` |

---

## 2. Titles renamed

Page IDs are unchanged, so existing links still work, but the URL *slug* now reflects the new title.
Anywhere the LMS displays or hardcodes a lesson name, these need updating.

### Building AI Agents (21)

| Module | Lang | Was (live) | Now |
|---|---|---|---|
| A | EN | Implementing Short Term Memory in Flowise | **Implementing Short Term Memory in n8n** |
| A | EN | Introduction to Flowise | **Introduction to n8n** |
| A | EN | Agent Memory Node and Thread IDs in Flowise | **Agent Memory and Session IDs in n8n** |
| A | DE | Memory Best Practices | **Best Practices für Memory** |
| B | EN | Agent Instructions and Behavior | **Agent Instructions and Behaviour** |
| B | EN | Visual Agent Builder Fundamentals | **n8n Workflow Builder Fundamentals** |
| B | EN | The Flowise Interface | **The n8n Interface** |
| B | DE | Die Flowise-Oberfläche | **Die n8n-Oberfläche** |
| B | EN | First AI-Powered Agentflow v2 | **Your First AI-Powered n8n Workflow** |
| B | DE | Erster Gemini-gestützter Agentflow v2 | **Dein erster KI-gestützter n8n-Workflow** |
| B | EN | Flowise and AI Agent Checkpoint | **n8n and AI Agent Checkpoint** |
| B | DE | Flowise- und Gemini-Agenten-Checkpoint | **n8n- und KI-Agenten-Checkpoint** |
| B | EN | Meet the module project — Meridian Consulting | **Meet the Module Project — Meridian Consulting** |
| B | EN | Introduction to Flowise  | **Introduction to n8n** |
| B | EN | Flowise, OpenRouter, and Gemini Stack | **n8n, OpenRouter, and the AI Stack** |
| B | DE | Flowise- und Gemini-Stack | **n8n, OpenRouter und der KI-Stack** |
| B | EN | API usage best practices | **API Usage Best Practices** |
| B | EN | Installing Flowise and API Setup in your Computer | **Installing n8n and API Setup on Your Computer** |
| B | DE | Flowise installieren und API-Setup auf deinem Computer einrichten | **n8n installieren und API-Zugang auf deinem Computer einrichten** |
| B | EN | Verifying your local environment | **Verifying Your Local n8n Environment** |
| B | DE | Deine lokale Umgebung überprüfen | **Deine lokale n8n-Umgebung überprüfen** |

### Advanced Agent Systems (4)

| Module | Lang | Was (live) | Now |
|---|---|---|---|
| A | EN | Designing a single-agent system end to end | **Build Vela’s first agent in n8n** |
| A | DE | Ein Single-Agent-System Ende-zu-Ende entwerfen | **Velas ersten Agenten in n8n bauen** |
| B | EN | Connecting an MCP tool to a Flowise agent | **Connecting an MCP tool to an n8n agent** |
| B | DE | Ein MCP-Tool mit einem Flowise-Agenten verbinden | **Ein MCP-Tool mit einem n8n-Agenten verbinden** |

Worth a look: `Agent Instructions and Behavior` → `Agent Instructions and Behaviour` is only a
US→UK spelling change, and `Visual Agent Builder Fundamentals` → `n8n Workflow Builder Fundamentals`
now names the tool in a section title. Both came from the draft course as-is.

---

## 3. Stale "Flowise" wording still in the new content

These titles came from the draft course still saying Flowise, even though their bodies are now n8n.
They were copied verbatim as agreed, so they still need fixing at source and here:

| Course | Module | Lang | Title (unchanged, still says Flowise) |
|---|---|---|---|
| Building AI Agents | A | DE | Einführung in Flowise |
| Building AI Agents | A | DE | Agent-Memory-Node und Thread-IDs in Flowise |

Also still Flowise-named, in the database itself rather than a page: the Building AI Agents
Module B sprint is called **`1-Setting up Flowise and Gemini Stack`**. I left it alone because it is a
shared select option on the whole database. Say the word and I'll rename it.

---

## 4. Lessons that lost screenshots

The new draft page has noticeably fewer images than the live page had. Most likely screenshots
not yet retaken for n8n.

| Course | Module | Lang | Lesson | Images now | Images before |
|---|---|---|---|---|---|
| Building AI Agents | B | EN | Purpose and Boundaries | 1 | 4 |
| Building AI Agents | B | DE | Zweck und Grenzen | 1 | 4 |
| Building AI Agents | B | EN | Installing n8n and API Setup on Your Computer | 0 | 9 |
| Building AI Agents | B | DE | n8n installieren und API-Zugang auf deinem Computer einrichten | 0 | 9 |
| Advanced Agent Systems | A | EN | Setting up your Environment | 3 | 9 |
| Advanced Agent Systems | A | DE | Deine Umgebung einrichten | 3 | 9 |
| Advanced Agent Systems | A | EN | Build Vela’s first agent in n8n | 3 | 7 |
| Advanced Agent Systems | A | DE | Velas ersten Agenten in n8n bauen | 3 | 8 |
| Advanced Agent Systems | B | EN | Connecting an MCP tool to an n8n agent | 3 | 7 |
| Advanced Agent Systems | B | DE | Ein MCP-Tool mit einem n8n-Agenten verbinden | 3 | 7 |
| Advanced Agent Systems | B | EN | Message passing and handoff contracts | 5 | 18 |
| Advanced Agent Systems | B | DE | Nachrichtenweitergabe und Handoff-Verträge | 6 | 18 |

The sharpest one is **Installing n8n and API Setup on Your Computer** (EN+DE): an install guide that
now has 0 screenshots where the Flowise version had 9.

---

## 5. Lessons where the text shrank by more than 40%

Mostly a deliberate rewrite into the tighter newer format — these pages generally have *more*
headings than before, so the material is restructured rather than cut. Listed for a content check.

| Course | Module | Lang | Lesson | Words now | Words before |
|---|---|---|---|---|---|
| Building AI Agents | B | EN | Purpose and Boundaries | 767 | 1683 |
| Building AI Agents | B | DE | Zweck und Grenzen | 728 | 1660 |
| Building AI Agents | B | EN | Testing and Handling Edge Cases | 519 | 1116 |
| Building AI Agents | B | DE | Edge Cases testen und behandeln | 491 | 1079 |
| Building AI Agents | B | DE | Dein erster KI-gestützter n8n-Workflow | 626 | 1061 |
| Building AI Agents | B | EN | n8n and AI Agent Checkpoint | 488 | 941 |
| Building AI Agents | B | DE | n8n- und KI-Agenten-Checkpoint | 486 | 940 |
| Building AI Agents | B | DE | n8n, OpenRouter und der KI-Stack | 562 | 1035 |
| Building AI Agents | B | EN | API Usage Best Practices | 490 | 854 |
| Building AI Agents | B | DE | Best Practices für API-Nutzung | 434 | 820 |
| Building AI Agents | B | EN | Installing n8n and API Setup on Your Computer | 464 | 1067 |
| Building AI Agents | B | DE | n8n installieren und API-Zugang auf deinem Computer einrichten | 430 | 947 |
| Building AI Agents | B | EN | Verifying Your Local n8n Environment | 395 | 692 |
| Building AI Agents | B | DE | Deine lokale n8n-Umgebung überprüfen | 360 | 674 |
| Advanced Agent Systems | A | DE | Orchestrierung, Kommunikation und Zustandsverwaltung | 770 | 1306 |
| Advanced Agent Systems | A | EN | Common architecture mistakes | 865 | 1727 |
| Advanced Agent Systems | A | DE | Häufige Architekturfehler | 782 | 1646 |

---

## 6. Known cosmetic deviation (Notion API limit)

3 callouts across the two courses had **no icon** in the draft. The Notion API cannot create or keep
an icon-less callout — it forces the default 💡. Everything else on those pages matched exactly.

- Building AI Agents — A EN **Short-term vs. long-term memory** — [open](https://app.notion.com/p/Short-term-vs-long-term-memory-3669418319f380eaa97fcfbecf83d649) · ['[27]callout.icon: null != "💡"']
- Advanced Agent Systems — A EN **Selecting the right pattern for a use case** — [open](https://app.notion.com/p/Selecting-the-right-pattern-for-a-use-case-3849418319f38024b1e0ea3b87ec9620) · ['[30]callout.icon: null != "💡"']
- Advanced Agent Systems — A DE **Das richtige Muster für einen Use Case auswählen** — [open](https://app.notion.com/p/Das-richtige-Muster-f-r-einen-Use-Case-ausw-hlen-eec9418319f382429dd5816a5e76ed12) · ['[25]callout.icon: null != "💡"']

To remove the 💡 someone has to click the icon off in the Notion UI on those three blocks.

---

## 7. Data quirk noticed, not touched

In Advanced Agent Systems Module A, the live course's Sprint-1 tree has 27 lessons but only 26 carry
the `Sprint 1: Agent Architecture Foundations` value — one DE lesson sits under a Sprint-1 parent while
its own Sprint field says something else (Module A Sprint 4 shows 5 DE rows against the draft's 4).
It did not affect the copy, which went by tree position, but the Sprint field is worth correcting.

## What I did not change

- No pages created, deleted, moved or re-parented; no page IDs or URLs changed
- Sprint/Language/Notes/Translation-review fields untouched — only page bodies and the titles listed above
- Other sprints (2, 3, 4) in all four databases untouched
- The draft (new, n8n) courses were not modified
