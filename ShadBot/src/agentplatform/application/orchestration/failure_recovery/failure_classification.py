"""
ShadBot Agent Platform

Failure Classification component for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from .failure_detection import DetectedFailure


@dataclass(frozen=True, slots=True)
class ClassifiedFailure:
    failure: DetectedFailure
    category: str
    recoverable: bool


class FailureClassifier:
    """
    Classifies failure severity and recoverability.
    """

    def classify(self, failure: DetectedFailure) -> ClassifiedFailure:
        msg = failure.error_message.lower()
        if "timeout" in msg or "network" in msg or "connection" in msg:
            return ClassifiedFailure(failure, "TRANSIENT_NETWORK", True)
        if "attribute" in msg or "type" in msg or "syntax" in msg:
            return ClassifiedFailure(failure, "CODE_DEFECT", True)
        return ClassifiedFailure(failure, "FATAL_ERROR", False)
