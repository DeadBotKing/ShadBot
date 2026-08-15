"""
ShadBot Agent Platform

Agent Performance Tracking component for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .execution_monitoring import ExecutionMonitoringRecord


@dataclass(frozen=True, slots=True)
class AgentPerformanceSummary:
    agent_name: str
    total_runs: int
    success_rate: float
    avg_duration_ms: float


class AgentPerformanceTracker:
    """
    Tracks historical performance metrics per agent role.
    """

    def summarize(self, records: Sequence[ExecutionMonitoringRecord], agent_name: str) -> AgentPerformanceSummary:
        agent_recs = [r for r in records if r.agent_name == agent_name]
        total = len(agent_recs)
        if total == 0:
            return AgentPerformanceSummary(agent_name, 0, 0.0, 0.0)
        successes = sum(1 for r in agent_recs if r.status == "COMPLETED")
        avg_dur = sum(r.duration_ms for r in agent_recs) / total
        return AgentPerformanceSummary(
            agent_name=agent_name,
            total_runs=total,
            success_rate=round(successes / total, 2),
            avg_duration_ms=round(avg_dur, 2),
        )
