# test-repo-hermes

Local-first agent workflow scaffolding for reproducible LLM automation experiments.

> Working title: this repository began as a Hermes/GitHub workflow validation repo. It is now being shaped into a small open-source sandbox for local LLM agent orchestration and maintainer automation.

## What this project does

`test-repo-hermes` provides a minimal Python CLI and library for turning a plain-language automation goal into a structured local-agent plan:

- break a task into repeatable planning, execution, validation, and review phases;
- generate provider-neutral prompt packets that can be sent to Ollama, OpenAI-compatible local endpoints, or other local LLM runners;
- keep the workflow deterministic enough to test before wiring it to real model calls;
- document the maintenance path for future Hermes/OpenClaw-style local agent tooling.

The current implementation is intentionally small and dependency-free. It is useful as a safe staging ground before adding model adapters, filesystem tools, or GitHub automation.

## Why this matters

Local LLM users often have the model runtime, scripts, and personal automation habits, but lack a simple reproducible workflow layer. This project focuses on the ecosystem gap between "I can call a local model" and "I can safely run repeatable agent workflows that are reviewable, testable, and maintainable."

The long-term direction is self-hosted AI automation that is:

- reproducible across Ollama/OpenAI-compatible local endpoints;
- inspectable before execution;
- friendly to small maintainers and personal infrastructure;
- safe to evolve through issues, tests, pull requests, and release notes.

## Status

Early-stage, under active development. The repository is intentionally small while the project defines its public API, roadmap, and maintenance workflow.

## Getting started

Requirements:

- Python 3.10+
- No third-party dependencies for the current CLI/tests

Clone and run the tests:

```bash
git clone https://github.com/ponzgpt/test-repo-hermes.git
cd test-repo-hermes
python3 -m unittest discover -s tests
```

Generate a local-agent plan:

```bash
python3 -m hermes_workflow.cli "Summarize new GitHub issues and propose labels"
```

Example output:

```json
{
  "objective": "Summarize new GitHub issues and propose labels",
  "backend": "openai-compatible",
  "steps": [
    "Clarify the objective and safety constraints",
    "Collect local context and repository metadata",
    "Draft an execution plan before making changes",
    "Run the smallest useful automation step",
    "Validate output and summarize follow-up work"
  ]
}
```

## Roadmap / planned features

- Add an Ollama adapter that can execute a generated prompt packet against a local model.
- Add an OpenAI-compatible local endpoint adapter for tools such as LM Studio, vLLM, Groq-compatible gateways, and OpenRouter-compatible proxies.
- Add workflow templates for GitHub issue triage, README maintenance, release notes, and security review checklists.
- Add structured run logs so agent decisions can be reviewed after execution.
- Add CI checks and packaging metadata once the public API stabilizes.

## How Codex will be used

Codex is a good fit for this repository because the maintainer work is exactly the kind of repetitive, review-heavy OSS work that benefits from a coding agent:

- issue triage and roadmap grooming;
- pull request review and test suggestions;
- unit test generation for workflow edge cases;
- refactors as the adapter API evolves;
- release notes and changelog drafting;
- lightweight security sweeps before adding filesystem or GitHub automation tools.

Codex will not be used to submit unreviewed model-generated changes directly to `main`. The intended workflow is issue-driven development, reviewed pull requests, and tests for each new automation capability.

## License

MIT. See [LICENSE](LICENSE).
