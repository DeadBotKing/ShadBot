"""
ShadBot Agent Platform

Project knowledge types.
"""

from __future__ import annotations

from enum import Enum


class KnowledgeType(str, Enum):
    """
    Types of knowledge extracted from projects.
    """

    ARCHITECTURE = "architecture"

    DEPENDENCY = "dependency"

    FRAMEWORK = "framework"

    LANGUAGE = "language"

    CONVENTION = "convention"

    DECISION = "decision"

    LESSON = "lesson"

    ISSUE = "issue"

    RECOMMENDATION = "recommendation"

    PROJECT_STATE = "project_state"
