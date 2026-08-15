"""
ShadBot Agent Platform

Execution Monitoring component for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ExecutionMonitoringRecord:
    execution_id: UUID
    agent_name: str
    duration_ms: float
    status: str
    timestamp: str


class ExecutionMonitor:
    """
    Monitors individual agent execution durations and status.
    """

    def record_execution(self, execution_id: UUID, agent_name: str, duration_ms: float, success: bool) -> ExecutionMonitoringRecord:
        return ExecutionMonitoringRecord(
            execution_id=execution_id,
            agent_name=agent_name,
            duration_ms=duration_ms,
            status="COMPLETED" if success else "FAILED",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
