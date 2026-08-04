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

    REQUIREMENT_ANALYSIS = "requirement_analysis"

    TECHNOLOGY_SELECTION = "technology_selection"

    SYSTEM_ANALYSIS = "system_analysis"

    WORKSPACE_SCAN = "workspace_scan"

    DEPENDENCY_ANALYSIS = "dependency_analysis"

    KNOWLEDGE_GENERATION = "knowledge_generation"

    RUNTIME_MONITORING = "runtime_monitoring"

    VALIDATION = "validation"

    MODEL_TRAINING = "model_training"

    MODEL_EVALUATION = "model_evaluation"

    EXPERIMENT_DESIGN = "experiment_design"

    IMPLEMENTATION = "implementation"

    REFACTORING = "refactoring"

    RESEARCH = "research"

    ARCHITECTURE_UNDERSTANDING = "architecture_understanding"

    TESTING = "testing"
