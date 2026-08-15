"""
ShadBot Agent Platform

Unified service for 7.7 Runtime Observability.
"""

from __future__ import annotations

from dataclasses import dataclass
from .event_logging import RuntimeEventLogger, RuntimeLogEntry
from .execution_trace import ExecutionTraceEvent, ExecutionTraceTracker
from .health_assessment import RuntimeHealthAssessor, RuntimeHealthReport
from .metrics_collector import RuntimeMetric, RuntimeMetricsCollector
from .performance_monitoring import PerformanceMonitor, PerformanceSnapshot


@dataclass(frozen=True, slots=True)
class CompleteObservabilityPackage:
    health: RuntimeHealthReport
    performance: PerformanceSnapshot
    metrics: tuple[RuntimeMetric, ...]
    logs: tuple[RuntimeLogEntry, ...]
    traces: tuple[ExecutionTraceEvent, ...]


class RuntimeObservabilityServiceLayer:
    """
    Orchestrates metrics collection, trace tracking, event logging, performance monitoring, and health assessment.
    """

    def __init__(
        self,
        metrics: RuntimeMetricsCollector | None = None,
        trace: ExecutionTraceTracker | None = None,
        logger: RuntimeEventLogger | None = None,
        monitor: PerformanceMonitor | None = None,
        assessor: RuntimeHealthAssessor | None = None,
    ) -> None:
        self._metrics = metrics or RuntimeMetricsCollector()
        self._trace = trace or ExecutionTraceTracker()
        self._logger = logger or RuntimeEventLogger()
        self._monitor = monitor or PerformanceMonitor()
        self._assessor = assessor or RuntimeHealthAssessor()

    def record_activity(self, component: str, action: str, duration_ms: float, level: str = "INFO", message: str = "OK") -> None:
        self._metrics.record_metric(f"{component}.{action}", duration_ms)
        self._trace.log_event(component, action, "OK" if level == "INFO" else level)
        self._logger.log(level, f"{component}: {message}")

    def inspect_system(self) -> CompleteObservabilityPackage:
        all_m = self._metrics.get_metrics()
        perf = self._monitor.analyze(all_m)
        errs = sum(1 for l in self._logger.get_logs() if l.level == "ERROR")
        health = self._assessor.assess(perf, errs)
        return CompleteObservabilityPackage(
            health=health,
            performance=perf,
            metrics=all_m,
            logs=self._logger.get_logs(),
            traces=self._trace.get_events(),
        )
