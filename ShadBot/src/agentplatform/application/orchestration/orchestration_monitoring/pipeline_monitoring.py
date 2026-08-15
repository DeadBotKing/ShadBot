"""
ShadBot Agent Platform

Pipeline Monitoring component for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class PipelineMonitoringSummary:
    pipeline_id: UUID
    status: str
    total_duration_ms: float
    step_count: int


class PipelineMonitor:
    """
    Monitors overall pipeline execution status and duration.
    """

    def monitor(self, pipeline_id: UUID, total_duration_ms: float, step_count: int, success: bool) -> PipelineMonitoringSummary:
        return PipelineMonitoringSummary(
            pipeline_id=pipeline_id,
            status="SUCCESS" if success else "FAILED",
            total_duration_ms=round(total_duration_ms, 2),
            step_count=step_count,
        )
