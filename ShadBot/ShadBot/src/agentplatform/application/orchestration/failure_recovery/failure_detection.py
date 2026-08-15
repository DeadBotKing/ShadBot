"""
ShadBot Agent Platform

Failure Detection component for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class DetectedFailure:
    agent_name: str
    error_message: str
    is_failure: bool


class FailureDetector:
    """
    Detects failed agent executions in a pipeline result set.
    """

    def detect(self, results: Sequence[AgentResult]) -> tuple[DetectedFailure, ...]:
        failures: list[DetectedFailure] = []
        for r in results:
            if not r.success:
                failures.append(
                    DetectedFailure(
                        agent_name=str(r.data.get("agent", "unknown")),
                        error_message=r.message,
                        is_failure=True,
                    )
                )
        return tuple(failures)
