"""
ShadBot Agent Platform

Reflection context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.brain.brain_reflection import (
    BrainReflection,
)
from agentplatform.domain.results import AgentResult


class ReflectionContextProvider:
    """
    Provides reflection context.
    """

    def __init__(
        self,
        reflection: BrainReflection,
        results: list[AgentResult],
    ) -> None:

        self._reflection = reflection
        self._results = results

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build reflection context.
        """

        return self._reflection.reflect(
            self._results,
        )
