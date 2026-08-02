"""
ShadBot Agent Platform

Runtime execution model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.results import AgentResult


@dataclass(slots=True)
class RuntimeExecution:
    """
    Stores one runtime execution lifecycle.
    """

    results: list[AgentResult] = field(
        default_factory=list,
    )

    retry_count: int = 0

    def add_results(
        self,
        results: list[AgentResult],
    ) -> None:
        """
        Append execution results.
        """

        self.results.extend(results)
