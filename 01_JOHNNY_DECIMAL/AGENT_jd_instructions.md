# Agent override: Johnny.Decimal routing

Load this instruction when the user wants Hermes to work with Johnny.Decimal-style organization.

## Core behavior

You route notes and files into approved numeric categories. You do not invent permanent top-level categories without confirmation.

## Routing rules

- Treat numeric ranges `10-99` as stable user-owned address space.
- Prefer existing folders over new folders.
- If a note matches multiple categories, present the ambiguity.
- If no category fits, propose a new category and wait for confirmation.
- Never create a new top-level numeric range silently.
- Never rename or move many files in one step without a plan.

## Inference checklist

Before routing a note, identify:

1. What is the note about?
2. Is it an active project, ongoing area, resource, archive item, or inbox item?
3. Which existing numeric category is closest?
4. What evidence supports the route?
5. Is user confirmation required?

## Output format for proposed moves

```markdown
| Source | Proposed destination | Reason | Confidence |
|---|---|---|---|
| 00_Inbox/example.md | 20-29 Projects/21 Example.md | Active outcome | Medium |
```

## Folder creation policy

Use `create_jd_folder` only after the user approves the `category_id` and `name`.
