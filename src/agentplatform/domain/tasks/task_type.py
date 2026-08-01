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
