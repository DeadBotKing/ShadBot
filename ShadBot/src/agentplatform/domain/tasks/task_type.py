"""
ShadBot Agent Platform

Task types for agent execution.
"""

from __future__ import annotations

from enum import Enum


class TaskType(str, Enum):
    """
    Types of tasks that agents can execute.
    """

    ANALYSIS = "analysis"

    DESIGN = "design"

    IMPLEMENTATION = "implementation"

    REVIEW = "review"

    RESEARCH = "research"

    TRADING_ANALYSIS = "trading_analysis"

    MODEL_TRAINING = "model_training"

    FULL_LIFECYCLE = "full_lifecycle"

    ALL_AGENTS = "all_agents"

    ENTERPRISE_SUITE = "enterprise_suite"

    ARCHITECTURE_DESIGN = "architecture_design"

    QA = "qa"

    BUGFIX = "bugfix"

    REFACTOR = "refactor"

    SECURITY_AUDIT = "security_audit"

    SYSTEM_INTEGRATION = "system_integration"

    COPILOT = "copilot"

    DOCUMENTATION = "documentation"

    OPTIMIZATION = "optimization"

    FEATURE = "feature"

    TESTING = "testing"

    DEPLOYMENT = "deployment"

    @classmethod
    def _missing_(cls, value: object) -> TaskType:
        """
        Graceful fallback for custom or unmapped task types.
        """
        return cls.IMPLEMENTATION
