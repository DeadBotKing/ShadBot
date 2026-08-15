"""
ShadBot Agent Platform

Brain validation capability.
"""

from __future__ import annotations

from collections.abc import Sequence

from agentplatform.domain.results import (
    AgentResult,
)


class BrainValidation:
    """
    Responsible for validating agent execution results.
    """

    def validate(
        self,
        results: Sequence[AgentResult],
    ) -> dict[str, object]:
        """
        Validate execution results.
        """

        failed_results = [result for result in results if not result.success]

        return {
            "passed": len(failed_results) == 0,
            "total_results": len(results),
            "failed_results": len(failed_results),
            "failures": [result.message for result in failed_results],
        }
