"""
ShadBot Agent Platform

Self improvement domain package.
"""

from .improvement_request import ImprovementRequest
from .improvement_result import ImprovementResult
from .improvement_status import ImprovementStatus

__all__ = [
    "ImprovementStatus",
    "ImprovementRequest",
    "ImprovementResult",
]
