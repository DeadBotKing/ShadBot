"""
ShadBot Agent Platform

Self improvement application package.
"""

from .improvement_engine import ImprovementEngine
from .learning_improvement_adapter import (
    LearningImprovementAdapter,
)
from .self_improvement_contract import (
    SelfImprovementContract,
)

__all__ = [
    "ImprovementEngine",
    "LearningImprovementAdapter",
    "SelfImprovementContract",
]
