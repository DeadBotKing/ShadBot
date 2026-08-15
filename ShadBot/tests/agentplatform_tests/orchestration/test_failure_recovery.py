"""
ShadBot Agent Platform

Unit tests for 6.6 Failure Recovery.
"""

from __future__ import annotations

from agentplatform.application.orchestration.failure_recovery import (
    AlternativeRouter,
    FailureClassifier,
    FailureDetector,
    FailureRecoveryService,
    RecoveryStrategySelector,
    RetryManager,
)
from agentplatform.domain.results import AgentResult


def test_failure_detector_finds_failures() -> None:
    res = AgentResult(False, "Connection timeout", data={"agent": "engineer"})
    det = FailureDetector().detect([res])
    assert len(det) == 1
    assert det[0].is_failure is True


def test_failure_classifier_categories() -> None:
    det = FailureDetector().detect([AgentResult(False, "Connection timeout")])[0]
    cls = FailureClassifier().classify(det)
    assert cls.category == "TRANSIENT_NETWORK"
    assert cls.recoverable is True


def test_recovery_strategy_selector_chooses_retry() -> None:
    det = FailureDetector().detect([AgentResult(False, "Connection timeout")])[0]
    cls = FailureClassifier().classify(det)
    strat = RecoveryStrategySelector().select_strategy(cls)
    assert strat.strategy_name == "RETRY_SAME_AGENT"


def test_retry_manager_calculates_delay() -> None:
    det = FailureDetector().detect([AgentResult(False, "Connection timeout")])[0]
    strat = RecoveryStrategySelector().select_strategy(FailureClassifier().classify(det))
    retry = RetryManager().manage_retry(strat, 2)
    assert retry.should_retry is True
    assert retry.delay_seconds == 2.0


def test_failure_recovery_service_recovers() -> None:
    service = FailureRecoveryService()
    pkg = service.recover([AgentResult(False, "Connection timeout")])
    assert pkg.has_failures is True
    assert pkg.validation.valid_recovery_plan is True
