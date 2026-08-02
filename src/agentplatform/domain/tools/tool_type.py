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

    MARKET_DATA = "market_data"

    DATASET_MANAGER = "dataset_manager"

    MODEL_TRAINER = "model_trainer"
