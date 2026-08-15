"""
ShadBot Agent Platform

Unified service for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult
from .alternative_routing import AlternativeRoute, AlternativeRouter
from .failure_classification import ClassifiedFailure, FailureClassifier
from .failure_detection import DetectedFailure, FailureDetector
from .recovery_strategy import RecoveryStrategy, RecoveryStrategySelector
from .recovery_validation import RecoveryValidationResult, RecoveryValidator
from .retry_management import RetryDecision, RetryManager


@dataclass(frozen=True, slots=True)
class RecoveryPlanPackage:
    has_failures: bool
    failures: tuple[ClassifiedFailure, ...]
    strategies: tuple[RecoveryStrategy, ...]
    retries: tuple[RetryDecision, ...]
    alternative_routes: tuple[AlternativeRoute, ...]
    validation: RecoveryValidationResult


class FailureRecoveryService:
    """
    Orchestrates detection, classification, strategy selection, retry management, alternative routing, and validation.
    """

    def __init__(
        self,
        detector: FailureDetector | None = None,
        classifier: FailureClassifier | None = None,
        selector: RecoveryStrategySelector | None = None,
        retry_mgr: RetryManager | None = None,
        router: AlternativeRouter | None = None,
        validator: RecoveryValidator | None = None,
    ) -> None:
        self._detector = detector or FailureDetector()
        self._classifier = classifier or FailureClassifier()
        self._selector = selector or RecoveryStrategySelector()
        self._retry_mgr = retry_mgr or RetryManager()
        self._router = router or AlternativeRouter()
        self._validator = validator or RecoveryValidator()

    def recover(self, results: Sequence[AgentResult], current_attempt: int = 1) -> RecoveryPlanPackage:
        detected = self._detector.detect(results)
        if not detected:
            return RecoveryPlanPackage(
                has_failures=False,
                failures=(),
                strategies=(),
                retries=(),
                alternative_routes=(),
                validation=RecoveryValidationResult(True, "No failures to recover."),
            )

        classified = tuple(self._classifier.classify(f) for f in detected)
        strategies = tuple(self._selector.select_strategy(c) for c in classified)
        retries = tuple(self._retry_mgr.manage_retry(s, current_attempt) for s in strategies)
        routes = tuple(self._router.reroute(s) for s in strategies)
        val = self._validator.validate(retries[0] if retries else RetryDecision(False, 1, 0.0))

        return RecoveryPlanPackage(
            has_failures=True,
            failures=classified,
            strategies=strategies,
            retries=retries,
            alternative_routes=routes,
            validation=val,
        )
