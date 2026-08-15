"""
ShadBot Agent Platform

Runtime Health Assessment component for 7.7 Runtime Observability.
"""

from __future__ import annotations

from dataclasses import dataclass
from .performance_monitoring import PerformanceSnapshot


@dataclass(frozen=True, slots=True)
class RuntimeHealthReport:
    is_healthy: bool
    status: str
    assessment_note: str


class RuntimeHealthAssessor:
    """
    Assesses overall runtime system health from performance snapshots and error logs.
    """

    def assess(self, snapshot: PerformanceSnapshot, error_count: int = 0) -> RuntimeHealthReport:
        healthy = (error_count == 0) and (snapshot.max_metric_value < 5000.0)
        status = "HEALTHY" if healthy else "DEGRADED"
        note = "All runtime metrics within normal thresholds." if healthy else f"Degraded performance or errors detected (errors: {error_count})."
        return RuntimeHealthReport(
            is_healthy=healthy,
            status=status,
            assessment_note=note,
        )
