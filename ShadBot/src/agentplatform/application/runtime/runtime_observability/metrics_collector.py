"""
ShadBot Agent Platform

Runtime Metrics Collector component for 7.7 Runtime Observability.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class RuntimeMetric:
    metric_name: str
    value: float
    unit: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class RuntimeMetricsCollector:
    """
    Collects numeric performance and health metrics for the Runtime System.
    """

    def __init__(self) -> None:
        self._metrics: list[RuntimeMetric] = []

    def record_metric(self, name: str, value: float, unit: str = "ms") -> RuntimeMetric:
        m = RuntimeMetric(name, value, unit)
        self._metrics.append(m)
        return m

    def get_metrics(self) -> tuple[RuntimeMetric, ...]:
        return tuple(self._metrics)
