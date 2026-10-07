# Task: populate the "Anatomy of an AI Application" course in MS BackOffice

## Run this where it can work

This task drives the **MS BackOffice web UI in my own logged-in browser**. It
must run in a Remote Control / bridge session on my machine — the same setup
that populated the sibling course. It cannot run in a cloud session: the
`lms.masterschool.com` host is denied by the egress policy there (403 on
CONNECT), and BackOffice authenticates by browser session, not an API key.

Before starting, confirm you have browser control tools available
(`computer:*` / `find` / `javascript_exec`) and that a tab is open on
BackOffice. If not, stop and tell me.

## Target

- Course: **Anatomy of an AI Application**, id `04a68c69-34a2-4bad-ad4a-df814fef79e4`
- Learner view: https://lms.masterschool.com/course/04a68c69-34a2-4bad-ad4a-df814fef79e4?version=1.1
- Editor: https://lms.masterschool.com/course-edit/04a68c69-34a2-4bad-ad4a-df814fef79e4?majorVersion=1&editorTab=content
- A single element is addressed by appending `&elementId=<uuid>`.

## Reference: the already-populated sibling course

Course `d1da346c-4f30-4f96-87b4-99998aa8abfe` is the same course shape, already
populated. Use it to confirm field names, placement and formatting before
touching the target. Its elements read back as:

```json
{"name": "What an AI service is, the FastAPI scaffold, and where latency comes from",
 "deck": "https://docs.google.com/presentation/d/1Cu6uZLWAZNGw",
 "plan": "https://www.notion.so/masterschool/LS-1-What-an-AI-s",
 "t": "45",
 "appnotion": false}
```

(The `deck`/`plan` values above are truncated as captured, not real URLs.)

Its sprint headers render `Live sessions / 3h 0m` and each element's subtitle
renders `Live Session · 45 mins`.

## What to enter

16 live sessions, 4 sprints x 4 sessions, 45 minutes each.

| LS | Sprint | Name | Deck | Plan (Notion) |
|----|--------|------|------|---------------|
| 1 | 1 | Anatomy of an AI application | https://docs.google.com/presentation/d/1GeguWFiNqGYVcm9T06BHW9G001L_H768uev4wNJVraI/edit | https://www.notion.so/masterschool/Anatomy-of-an-AI-application-3ca9418319f380a49ab2c6d132b9fe24 |
| 2 | 1 | Three ways to access a model and the Gemini API | https://docs.google.com/presentation/d/13ZytQ1ZoD_WcUn7byH2Gmus-wZlZva17qj3mKlBbGMU/edit | https://www.notion.so/masterschool/Three-ways-to-access-a-model-and-the-Gemini-API-3d29418319f38086b546f50e57a3164d |
| 3 | 1 | Structured Outputs at the Application Level | https://docs.google.com/presentation/d/1vdPgwh6jfVM6nhxbBfK5RMDafBEqVrGxPlnLfCPR7e4/edit | https://www.notion.so/masterschool/Structured-Outputs-at-the-Application-Level-3d59418319f380f6a5a5cffb7f2fbf77 |
| 4 | 1 | Sprint 1 Checkpoint | https://docs.google.com/presentation/d/1NqRdEN9bizEy6B_0DFjuLDf5v3iD4nYDTdhet_ER0A4/edit | https://www.notion.so/masterschool/Sprint-1-Checkpoint-3d59418319f3803bb535fb1dbed8125d |
| 5 | 2 | Reranking | https://docs.google.com/presentation/d/1IQ6zBLsexKwMwJp_qHfypCDTYkybhnVEDprnKEjbWVA/edit | https://www.notion.so/masterschool/Reranking-3d59418319f3804d951ed61a377093bc |
| 6 | 2 | Hybrid Search | https://docs.google.com/presentation/d/12qHt_vUt335VIF8oq9Z3D3QhYLMR9qWvxO-HtjsNPJw/edit | https://www.notion.so/masterschool/Hybrid-Search-3d59418319f380c381bce9550357e855 |
| 7 | 2 | Query Rewriting | https://docs.google.com/presentation/d/1IjvDJXYQJJCt1VkybOSBpLKlvhJCa09dkbMyHrw2MZE/edit | https://www.notion.so/masterschool/Query-Rewriting-3d59418319f38070bebaeea7f69a1897 |
| 8 | 2 | Sprint 2 Checkpoint | https://docs.google.com/presentation/d/17D5ZKKb_cfRX0qh1-wAnr0ziZ5NBNsPNHGWxDO7cpmE/edit | https://www.notion.so/masterschool/Sprint-2-Checkpoint-3d59418319f380738c0ae40f55532575 |
| 9 | 3 | Multi-step tool reasoning and tool schemas | https://docs.google.com/presentation/d/19_5Gq8tGyYAwerNbvz7kqAlZUNrMGsIuTNUHNoDF7Aw/edit | https://www.notion.so/masterschool/Multi-step-tool-reasoning-and-tool-schemas-3d59418319f3806fbeeef121ff93b573 |
| 10 | 3 | Tool error handling patterns | https://docs.google.com/presentation/d/1EciYQ96rLglh-WbJ1a6vB42Dx80fMoQdazVEWBax3Ag/edit | https://www.notion.so/masterschool/Tool-error-handling-patterns-3d59418319f380ea8c12dc9ca87d6d70 |
| 11 | 3 | MCP first introduction: what it is and how to use it | https://docs.google.com/presentation/d/1MG7xpcEpssa4Tcm0KE5WrYhHR4Au4_PLLRJMFuuwoVU/edit | https://www.notion.so/masterschool/MCP-first-introduction-what-it-is-and-how-to-use-it-3d59418319f380508b9cecf2b230f24f |
| 12 | 3 | Sprint 3 checkpoint | https://docs.google.com/presentation/d/1Bf4_J39jJGs6uB2___5FaUVewhBGe6MOHbmDADGsZ1s/edit | https://www.notion.so/masterschool/Sprint-3-checkpoint-3d59418319f38039bf7dd44fb5715f5f |
| 13 | 4 | Project kickoff and scoping | https://docs.google.com/presentation/d/1NvnGV3Cgh3IePd8NFX0xxPqPrwCpyxMSJe5iUJohysk/edit | https://www.notion.so/masterschool/Project-kickoff-and-scoping-3d59418319f3804f973de522a241fd7a |
| 14 | 4 | Build and edge case testing | https://docs.google.com/presentation/d/1-v2XLnbu1YfkBkNP3pRCZfEPaDRgyLw6e7dWp0KOSG0/edit | https://www.notion.so/masterschool/Build-and-edge-case-testing-3d59418319f3803ea93bd1e05a19fc2c |
| 15 | 4 | Presentation Day | *(none — leave empty)* | https://www.notion.so/masterschool/Presentation-Day-3e99418319f3804e91f4df6affeef557 |
| 16 | 4 | Code Clinic | *(none — leave empty)* | https://www.notion.so/masterschool/Code-Clinic-3e99418319f380ffa25ced5176e6b56e |

Machine-readable copy of the same table:
`course-population/ls-manifest.csv` on branch `claude/hopeful-mayer-3dhy3b`
of `github.com/dunmacleod/myenv` (columns: `ls,sprint,name,duration_min,deck,plan`).

## Rules

1. **Enter the URLs exactly as written.** They are already normalised:
   decks have no `?usp=drivesdk` / `ouid=` parameters; plans use the
   `www.notion.so/masterschool/<Slug>-<32-hex-id>` form, not `app.notion.com/p/...`.
2. **LS15 and LS16 have no deck.** Leave the deck field empty. Do not
   substitute a placeholder or reuse another deck. (Confirmed intentional —
   matches `Code Clinic` in the sibling course.)
3. **Duration is 45 for all 16.**
4. **Do not create, rename or reorder anything not in the table.** If the
   sprint blocks do not already exist, stop and ask before creating them.
5. **Do not publish or bump the course version.** Leave it on `majorVersion=1`
   in draft. I will review and publish.
6. If an element already has a value that differs from the table, **stop and
   report it** rather than overwriting — it may be deliberate.

## Method

Work one element at a time, and verify as you go rather than entering all 16
and checking at the end:

1. Open the editor URL above and read the existing structure first. Report
   what is already there before changing anything.
2. For each row: open the element, set name, deck, plan and duration, save.
3. After each save, read the field values back out of the page (the
   `javascript_exec` approach used on the sibling course) and compare against
   the table. A field that silently failed to save is the main failure mode.
4. Keep a running checklist of LS1–LS16 as done / mismatched / skipped.

## Verification before you report done

- All 16 elements present, in order, correct sprint.
- Every subtitle renders `Live Session · 45 mins`.
- Each of the 4 sprint headers totals **3h 0m**.
- 14 deck links populated, LS15/LS16 deck empty.
- Spot-open 2–3 deck links and 2–3 plan links and confirm they resolve to the
  right lesson (not a 404 or the wrong LS).

## Open question — ask me, don't guess

The sibling course's LS1 carries a field `appnotion: false`. I don't know what
it does and it is **not** in the table. If the editor exposes it, leave it at
its default and tell me what you see.

## Report back

The LS1–LS16 checklist, anything you stopped on, and anything that read back
differently from what you entered.
