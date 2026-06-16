# Agent override: GTD triage

Load this instruction when the user wants Hermes to capture and triage tasks using GTD-style workflows.

## Core behavior

All unprocessed tasks go to `00_Inbox.md` as Markdown checkboxes.

## Capture format

```markdown
- [ ] Task text #context
```

Use tags sparingly. Prefer obvious context tags:

- `#home`
- `#computer`
- `#errand`
- `#waiting`
- `#someday`
- `#call`
- `#email`

## Triage rules

- Capture first; clarify later.
- Do not over-classify during capture.
- If an item is vague, preserve the user's words and mark it for clarification.
- If an item has a clear next physical action, propose it.
- If someone else owns the next step, classify as waiting-for.
- If it is not actionable but useful, classify as reference.
- If it might matter later, classify as someday/maybe.

## Mutation policy

- Appending to `00_Inbox.md` is safe.
- Moving or rewriting existing tasks requires a proposed triage plan.
- Deleting completed tasks requires explicit user confirmation.

Use `append_to_inbox` for new capture.
