# Johnny.Decimal module guide

Use this module when the vault needs stable addresses.

Johnny.Decimal is useful when a folder system has grown too vague and the user needs durable numbered locations for notes, files, and projects. It works well for structured Obsidian vaults, local Git folders, and long-lived knowledge bases.

## What this module provides

- Human-readable guidance for using numbered areas and categories.
- Agent instructions for routing notes into existing numeric ranges.
- A function-calling schema for creating a new Johnny.Decimal folder after confirmation.

## Minimal model

```text
10-19 Operations
20-29 Projects
30-39 Areas
40-49 Resources
90-99 Archive
```

The exact map belongs to the user. The agent can propose structure, but it should not invent permanent top-level categories without confirmation.

## When to use

- The vault has many notes that need stable homes.
- The user wants predictable locations rather than fuzzy tags only.
- Multiple agents or automations need to agree on where files belong.
- The user wants Git diffs to show intentional routing decisions.

## When not to use

- The user only needs quick capture.
- The vault is temporary.
- The user has not approved a top-level numeric map.

## Recommended workflow

1. Ask the agent to inspect the current folder map.
2. Ask it to propose a Johnny.Decimal routing table.
3. Review the proposed numeric ranges.
4. Approve a small number of folders.
5. Let the agent route notes only into approved folders.

Reference: https://johnnydecimal.com/
