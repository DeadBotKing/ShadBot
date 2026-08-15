"""
ShadBot Agent Platform

Brain self reflection.
"""

from __future__ import annotations

from agentplatform.domain.results import (
    AgentResult,
)


class BrainReflection:
    """
    Analyzes previous execution results.
    """

    def reflect(
        self,
        results: list[AgentResult],
    ) -> dict[str, object]:
        """
        Extract lessons from execution.
        """

        failures = [result.message for result in results if not result.success]

        return {
            "success": len(failures) == 0,
            "failures": failures,
            "lessons": ["Review execution outcome"],
        }
