"""
ShadBot Agent Platform

Orchestration Metrics component for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .agent_performance import AgentPerformanceSummary
from .bottleneck_detection import BottleneckReport
from .pipeline_monitoring import PipelineMonitoringSummary


@dataclass(frozen=True, slots=True)
class CompleteOrchestrationMetrics:
    pipeline_summary: PipelineMonitoringSummary
    agent_summaries: tuple[AgentPerformanceSummary, ...]
    bottleneck_report: BottleneckReport


class OrchestrationMetricsCollector:
    """
    Aggregates all monitoring summaries into a unified metrics report.
    """

    def collect_metrics(
        self,
        pipeline: PipelineMonitoringSummary,
        agents: Sequence[AgentPerformanceSummary],
        bottleneck: BottleneckReport,
    ) -> CompleteOrchestrationMetrics:
        return CompleteOrchestrationMetrics(
            pipeline_summary=pipeline,
            agent_summaries=tuple(agents),
            bottleneck_report=bottleneck,
        )
