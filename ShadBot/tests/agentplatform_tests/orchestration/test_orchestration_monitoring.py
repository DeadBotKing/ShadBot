"""
ShadBot Agent Platform

Unit tests for 6.7 Orchestration Monitoring.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.orchestration.orchestration_monitoring import (
    AgentPerformanceTracker,
    BottleneckDetector,
    ExecutionMonitor,
    OrchestrationMonitoringService,
    PipelineMonitor,
)


def test_execution_monitor_records_duration() -> None:
    rec = ExecutionMonitor().record_execution(uuid4(), "architect", 150.0, True)
    assert rec.agent_name == "architect"
    assert rec.status == "COMPLETED"


def test_agent_performance_tracker_summarizes() -> None:
    monitor = ExecutionMonitor()
    recs = [
        monitor.record_execution(uuid4(), "architect", 100.0, True),
        monitor.record_execution(uuid4(), "architect", 200.0, True),
    ]
    summary = AgentPerformanceTracker().summarize(recs, "architect")
    assert summary.total_runs == 2
    assert summary.avg_duration_ms == 150.0
    assert summary.success_rate == 1.0


def test_bottleneck_detector_finds_slowest() -> None:
    monitor = ExecutionMonitor()
    recs = [
        monitor.record_execution(uuid4(), "architect", 500.0, True),
        monitor.record_execution(uuid4(), "engineer", 1500.0, True),
    ]
    bot = BottleneckDetector().detect(recs, threshold_ms=1000.0)
    assert bot.has_bottleneck is True
    assert bot.bottleneck_agent == "engineer"


def test_orchestration_monitoring_service_logs_and_reports() -> None:
    service = OrchestrationMonitoringService()
    service.log_execution(uuid4(), "architect", 250.0, True)
    metrics = service.generate_metrics(uuid4(), 250.0, 1, True)
    assert metrics.pipeline_summary.status == "SUCCESS"
    assert len(metrics.agent_summaries) == 1
    assert metrics.agent_summaries[0].agent_name == "architect"
