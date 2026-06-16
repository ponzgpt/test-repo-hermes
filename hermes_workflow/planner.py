"""Deterministic planning helpers for local LLM agent workflows.

The functions in this module do not call a model. They prepare structured
context that can be sent to Ollama, LM Studio, vLLM, or another
OpenAI-compatible local endpoint by a future adapter.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Iterable


DEFAULT_STEPS = (
    "Clarify the objective and safety constraints",
    "Collect local context and repository metadata",
    "Draft an execution plan before making changes",
    "Run the smallest useful automation step",
    "Validate output and summarize follow-up work",
)


@dataclass(frozen=True)
class PromptPacket:
    """Provider-neutral prompt payload for a local LLM backend."""

    system: str
    user: str
    safety_notes: tuple[str, ...]

    def to_messages(self) -> list[dict[str, str]]:
        """Return an OpenAI-compatible chat message list."""
        return [
            {"role": "system", "content": self.system},
            {"role": "user", "content": self.user},
        ]


@dataclass(frozen=True)
class AgentPlan:
    """A reviewable local-agent plan before any tool execution happens."""

    objective: str
    backend: str
    steps: tuple[str, ...]
    prompt_packet: PromptPacket

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-serializable representation."""
        return asdict(self)

    def to_json(self) -> str:
        """Serialize the plan with stable formatting for logs and tests."""
        return json.dumps(self.to_dict(), indent=2, sort_keys=True)


def build_agent_plan(
    objective: str,
    *,
    backend: str = "openai-compatible",
    extra_context: Iterable[str] = (),
) -> AgentPlan:
    """Build a deterministic plan for a local LLM automation task."""
    clean_objective = objective.strip()
    if not clean_objective:
        raise ValueError("objective must not be empty")

    context_lines = tuple(line.strip() for line in extra_context if line.strip())
    context_block = "\n".join(f"- {line}" for line in context_lines)
    user_parts = [
        f"Objective: {clean_objective}",
        "Create a concise execution plan before using tools.",
    ]
    if context_block:
        user_parts.append(f"Available context:\n{context_block}")

    packet = PromptPacket(
        system=(
            "You are a local-first automation agent. Prefer reversible, "
            "inspectable steps and ask before destructive changes."
        ),
        user="\n\n".join(user_parts),
        safety_notes=(
            "Do not execute destructive filesystem or Git operations without approval.",
            "Keep prompts and logs free of secrets.",
            "Validate outputs before applying changes.",
        ),
    )

    return AgentPlan(
        objective=clean_objective,
        backend=backend,
        steps=DEFAULT_STEPS,
        prompt_packet=packet,
    )
