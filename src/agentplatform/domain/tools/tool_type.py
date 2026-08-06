"""
ShadBot Agent Platform

Tool types.
"""

from __future__ import annotations

from enum import Enum


class ToolType(str, Enum):
    """
    Available agent tools.
    """

    FILE_SYSTEM = "file_system"

    TERMINAL = "terminal"

    GIT = "git"

    TEST_RUNNER = "test_runner"

    PROJECT_ANALYZER = "project_analyzer"

    BUILD_RUNNER = "build_runner"

    QUALITY_VALIDATOR = "quality_validator"

    RESEARCH = "research"

    DOCUMENTATION_ANALYSIS = "documentation_analysis"

    TECHNOLOGY_COMPARISON = "technology_comparison"

    EXPERIMENT_TRACKING = "experiment_tracking"

    MODEL_EVALUATION = "model_evaluation"

    EXPERIMENT_DESIGN = "experiment_design"

    MODEL_TRAINING = "model_training"

    MODEL_TRAINER = "model_trainer"

    DATASET_MANAGER = "dataset_manager"

    MARKET_DATA = "market_data"

    EXECUTION_MONITOR = "execution_monitor"

    METRICS_COLLECTOR = "metrics_collector"

    LOG_ANALYZER = "log_analyzer"

    SYSTEM_HEALTH = "system_health"

    CODE_EXECUTION = "code_execution"

    PACKAGE_MANAGER = "package_manager"

    STATIC_ANALYZER = "static_analyzer"

    CODE_SEARCH = "code_search"

    PATCH_APPLIER = "patch_applier"

    DIFF_ANALYZER = "diff_analyzer"

    IMPROVEMENT_LOOP = "improvement_loop"

    EXPERIMENT_EXECUTOR = "experiment_executor"
