"""
ShadBot Agent Platform

Capability types.
"""

from __future__ import annotations

from enum import Enum


class CapabilityType(str, Enum):
    """
    Supported agent capabilities.
    """

    CODE_GENERATION = "code_generation"

    CODE_REFACTORING = "code_refactoring"

    CODE_REVIEW = "code_review"

    TEST_GENERATION = "test_generation"

    DEBUGGING = "debugging"

    ARCHITECTURE_DESIGN = "architecture_design"

    TECHNOLOGY_SELECTION = "technology_selection"

    SYSTEM_ANALYSIS = "system_analysis"

    MARKET_ANALYSIS = "market_analysis"

    FEATURE_ENGINEERING = "feature_engineering"

    MODEL_TRAINING = "model_training"

    MODEL_EVALUATION = "model_evaluation"
