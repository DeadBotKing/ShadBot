"""
ShadBot Agent Platform

Result Normalizer component for 6.5 Result Aggregation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Sequence
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class NormalizedAgentOutput:
    agent_name: str
    success: bool
    summary: str
    key_artifacts: tuple[str, ...]
    raw_data: dict[str, Any] = field(default_factory=dict)


class ResultNormalizer:
    """
    Normalizes heterogeneous agent results into standard output models.
    """

    def normalize(self, results: Sequence[AgentResult]) -> tuple[NormalizedAgentOutput, ...]:
        norm: list[NormalizedAgentOutput] = []
        for r in results:
            agent = str(r.data.get("agent", "unknown"))
            artifacts: list[str] = []
            if "generated_files" in r.data:
                artifacts.extend(str(f) for f in r.data["generated_files"])
            if "architecture_plan" in r.data:
                artifacts.append("architecture_plan")
            norm.append(
                NormalizedAgentOutput(
                    agent_name=agent,
                    success=r.success,
                    summary=r.message,
                    key_artifacts=tuple(artifacts),
                    raw_data=dict(r.data),
                )
            )
        return tuple(norm)
