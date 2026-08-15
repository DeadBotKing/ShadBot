"""
ShadBot Agent Platform

Unified service for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from typing import Sequence
from uuid import UUID
from .agent_performance import AgentPerformanceTracker
from .bottleneck_detection import BottleneckDetector
from .execution_monitoring import ExecutionMonitor, ExecutionMonitoringRecord
from .orchestration_metrics import CompleteOrchestrationMetrics, OrchestrationMetricsCollector
from .pipeline_monitoring import PipelineMonitor


class OrchestrationMonitoringService:
    """
    Orchestrates execution monitoring, agent performance tracking, bottleneck detection, and metrics collection.
    """

    def __init__(
        self,
        monitor: ExecutionMonitor | None = None,
        tracker: AgentPerformanceTracker | None = None,
        pipe_monitor: PipelineMonitor | None = None,
        detector: BottleneckDetector | None = None,
        collector: OrchestrationMetricsCollector | None = None,
    ) -> None:
        self._monitor = monitor or ExecutionMonitor()
        self._tracker = tracker or AgentPerformanceTracker()
        self._pipe_monitor = pipe_monitor or PipelineMonitor()
        self._detector = detector or BottleneckDetector()
        self._collector = collector or OrchestrationMetricsCollector()
        self._records: list[ExecutionMonitoringRecord] = []

    def log_execution(self, execution_id: UUID, agent_name: str, duration_ms: float, success: bool) -> ExecutionMonitoringRecord:
        rec = self._monitor.record_execution(execution_id, agent_name, duration_ms, success)
        self._records.append(rec)
        return rec

    def generate_metrics(self, pipeline_id: UUID, total_duration_ms: float, step_count: int, success: bool) -> CompleteOrchestrationMetrics:
        pipe_sum = self._pipe_monitor.monitor(pipeline_id, total_duration_ms, step_count, success)
        agents = tuple(self._tracker.summarize(self._records, name) for name in sorted(set(r.agent_name for r in self._records)))
        bot = self._detector.detect(self._records)
        return self._collector.collect_metrics(pipe_sum, agents, bot)
