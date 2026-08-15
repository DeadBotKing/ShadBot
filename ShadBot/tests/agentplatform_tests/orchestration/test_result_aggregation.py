"""
ShadBot Agent Platform

Unit tests for 6.5 Result Aggregation.
"""

from __future__ import annotations

from agentplatform.application.orchestration.result_aggregation import (
    ConflictResolver,
    FinalResultBuilder,
    ResultAggregationService,
    ResultCollector,
    ResultEvaluator,
    ResultNormalizer,
)
from agentplatform.domain.results import AgentResult


def test_result_collector_returns_results() -> None:
    res = AgentResult(True, "ok", data={"agent": "architect"})
    assert len(ResultCollector().collect([res])) == 1


def test_result_normalizer_extracts_agent() -> None:
    res = AgentResult(True, "ok", data={"agent": "architect", "generated_files": ["a.py"]})
    norm = ResultNormalizer().normalize([res])
    assert norm[0].agent_name == "architect"
    assert "a.py" in norm[0].key_artifacts


def test_result_evaluator_calculates_ratio() -> None:
    norm = ResultNormalizer().normalize([AgentResult(True, "ok"), AgentResult(False, "err")])
    ev = ResultEvaluator().evaluate(norm)
    assert ev.all_successful is False
    assert ev.success_ratio == 0.5


def test_result_aggregation_service_aggregates_all() -> None:
    service = ResultAggregationService()
    pkg, rep = service.aggregate([AgentResult(True, "ok", data={"agent": "architect"})])
    assert pkg.success is True
    assert "PASSED" in rep
