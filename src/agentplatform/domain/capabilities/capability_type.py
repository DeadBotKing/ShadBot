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

    RUNTIME_ANALYSIS = "runtime_analysis"

    FAILURE_ANALYSIS = "failure_analysis"

    PERFORMANCE_ANALYSIS = "performance_analysis"

    ANOMALY_DETECTION = "anomaly_detection"

    SECURITY_ANALYSIS = "security_analysis"

    STYLE_ANALYSIS = "style_analysis"

    COVERAGE_ANALYSIS = "coverage_analysis"

    REGRESSION_ANALYSIS = "regression_analysis"

    HYPERPARAMETER_SEARCH = "hyperparameter_search"

    MODEL_IMPROVEMENT = "model_improvement"

    RETRAINING = "retraining"

    EXPERIMENT_TRACKING = "experiment_tracking"

    IDEA_GENERATION = "idea_generation"

    PROTOTYPE_DEVELOPMENT = "prototype_development"

    EXPERIMENT_EXECUTION = "experiment_execution"

    TECHNOLOGY_RESEARCH = "technology_research"

    FEASIBILITY_ANALYSIS = "feasibility_analysis"

    INNOVATION_ANALYSIS = "innovation_analysis"

    IMPROVEMENT_LOOP = "improvement_loop"

    PROJECT_ANALYSIS = "project_analysis"

    DOCUMENTATION_ANALYSIS = "documentation_analysis"
