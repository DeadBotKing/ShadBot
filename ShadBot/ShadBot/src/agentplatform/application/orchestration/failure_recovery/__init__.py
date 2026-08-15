"""
ShadBot Agent Platform

6.6 Failure Recovery module.
"""

from .alternative_routing import AlternativeRoute, AlternativeRouter
from .failure_classification import ClassifiedFailure, FailureClassifier
from .failure_detection import DetectedFailure, FailureDetector
from .failure_recovery_service import FailureRecoveryService, RecoveryPlanPackage
from .recovery_strategy import RecoveryStrategy, RecoveryStrategySelector
from .recovery_validation import RecoveryValidationResult, RecoveryValidator
from .retry_management import RetryDecision, RetryManager

__all__ = [
    "DetectedFailure",
    "FailureDetector",
    "ClassifiedFailure",
    "FailureClassifier",
    "RecoveryStrategy",
    "RecoveryStrategySelector",
    "RetryDecision",
    "RetryManager",
    "AlternativeRoute",
    "AlternativeRouter",
    "RecoveryValidationResult",
    "RecoveryValidator",
    "RecoveryPlanPackage",
    "FailureRecoveryService",
]
