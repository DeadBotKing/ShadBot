"""
ShadBot Agent Platform

Performance Monitoring component for 7.7 Runtime Observability.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .metrics_collector import RuntimeMetric


@dataclass(frozen=True, slots=True)
class PerformanceSnapshot:
    avg_metric_value: float
    max_metric_value: float
    metric_count: int


class PerformanceMonitor:
    """
    Analyzes runtime metrics for performance anomalies.
    """

    def analyze(self, metrics: Sequence[RuntimeMetric]) -> PerformanceSnapshot:
        if not metrics:
            return PerformanceSnapshot(0.0, 0.0, 0)
        vals = [m.value for m in metrics]
        return PerformanceSnapshot(
            avg_metric_value=round(sum(vals) / len(vals), 2),
            max_metric_value=max(vals),
            metric_count=len(vals),
        )
