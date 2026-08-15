"""
ShadBot Project Intelligence

Knowledge Rule Severity Domain Value
"""

from __future__ import annotations

from enum import StrEnum


class RuleSeverity(StrEnum):
    """
    Represents the importance level of a knowledge finding.
    """

    INFO = "info"

    WARNING = "warning"

    ERROR = "error"

    CRITICAL = "critical"
