"""
ShadBot Agent Platform

Agent Reflection Binding
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from agentplatform.application.brain.brain_reflection import (
    BrainReflection,
)
from agentplatform.domain.results import (
    AgentResult,
)


@dataclass(frozen=True, slots=True)
class ReflectionBinding:
    """
    Reflection capability attached to an agent.
    """

    reflection: BrainReflection

    def reflect(
        self,
        results: Sequence[AgentResult],
    ) -> dict[str, object]:
        """
        Analyze execution results.
        """

        return self.reflection.reflect(
            list(results),
        )
