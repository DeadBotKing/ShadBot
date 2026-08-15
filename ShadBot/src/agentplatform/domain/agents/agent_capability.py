"""
Agent Platform

Agent Capability Domain Entity
"""

from __future__ import annotations

from enum import Enum


class AgentCapability(str, Enum):
    """
    Defines capabilities available to agents.
    """

    ARCHITECTURE_ANALYSIS = "architecture_analysis"

    DESIGN_REVIEW = "design_review"

    DEPENDENCY_ANALYSIS = "dependency_analysis"

    CODE_GENERATION = "code_generation"

    CODE_REFACTORING = "code_refactoring"

    TEST_GENERATION = "test_generation"

    CODE_REVIEW = "code_review"

    BUG_DETECTION = "bug_detection"

    SECURITY_REVIEW = "security_review"

    RESEARCH = "research"

    TRADING_ANALYSIS = "trading_analysis"

    FEATURE_ENGINEERING = "feature_engineering"

    MODEL_EVALUATION = "model_evaluation"
