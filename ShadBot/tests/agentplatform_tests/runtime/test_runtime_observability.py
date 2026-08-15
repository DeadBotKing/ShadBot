"""
ShadBot Agent Platform

Unit tests for 7.7 Runtime Observability.
"""

from __future__ import annotations

from agentplatform.application.runtime.runtime_observability import (
    ExecutionTraceTracker,
    PerformanceMonitor,
    RuntimeEventLogger,
    RuntimeHealthAssessor,
    RuntimeMetricsCollector,
    RuntimeObservabilityServiceLayer,
)


def test_metrics_collector_records_metrics() -> None:
    m = RuntimeMetricsCollector().record_metric("agent.exec", 120.5)
    assert m.metric_name == "agent.exec"
    assert m.value == 120.5


def test_execution_trace_tracker_logs_events() -> None:
    ev = ExecutionTraceTracker().log_event("AgentRuntime", "START", "OK")
    assert ev.component == "AgentRuntime"
    assert ev.action == "START"


def test_event_logger_records_level() -> None:
    log = RuntimeEventLogger().log("WARN", "High latency")
    assert log.level == "WARN"
    assert "latency" in log.message


def test_performance_monitor_calculates_snapshot() -> None:
    collector = RuntimeMetricsCollector()
    collector.record_metric("m1", 100.0)
    collector.record_metric("m2", 300.0)
    snap = PerformanceMonitor().analyze(collector.get_metrics())
    assert snap.avg_metric_value == 200.0
    assert snap.max_metric_value == 300.0


def test_runtime_observability_service_layer_inspects_system() -> None:
    service = RuntimeObservabilityServiceLayer()
    service.record_activity("BrainRuntime", "reason", 150.0, "INFO", "OK")
    pkg = service.inspect_system()
    assert pkg.health.is_healthy is True
    assert len(pkg.metrics) == 1
    assert len(pkg.traces) == 1
