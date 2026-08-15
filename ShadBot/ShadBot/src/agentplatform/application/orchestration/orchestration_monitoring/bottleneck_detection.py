"""
ShadBot Agent Platform

Bottleneck Detection component for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .execution_monitoring import ExecutionMonitoringRecord


@dataclass(frozen=True, slots=True)
class BottleneckReport:
    has_bottleneck: bool
    bottleneck_agent: str | None
    bottleneck_duration_ms: float


class BottleneckDetector:
    """
    Detects execution bottlenecks where an agent exceeds normal execution thresholds.
    """

    def detect(self, records: Sequence[ExecutionMonitoringRecord], threshold_ms: float = 1000.0) -> BottleneckReport:
        bottlenecks = [r for r in records if r.duration_ms >= threshold_ms]
        if not bottlenecks:
            return BottleneckReport(False, None, 0.0)
        slowest = sorted(bottlenecks, key=lambda r: r.duration_ms, reverse=True)[0]
        return BottleneckReport(
            has_bottleneck=True,
            bottleneck_agent=slowest.agent_name,
            bottleneck_duration_ms=slowest.duration_ms,
        )
