"""
ShadBot Agent Platform

Result Collector component for 6.5 Result Aggregation.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.results import AgentResult


class ResultCollector:
    """
    Collects agent results from an execution pipeline.
    """

    def collect(self, results: Sequence[AgentResult]) -> tuple[AgentResult, ...]:
        return tuple(results)
