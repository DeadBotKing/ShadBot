"""
Agent Platform

Agent Role Domain Entity
"""

from __future__ import annotations

from enum import Enum


class AgentRole(str, Enum):

    ARCHITECT = "architect"

    ENGINEER = "engineer"

    REVIEWER = "reviewer"

    RESEARCHER = "researcher"

    PROJECT_INTELLIGENCE = "project_intelligence"

    QA = "qa"

    RUNTIME_OBSERVER = "runtime_observer"

    ML_SCIENTIST = "ml_scientist"

    RND = "rnd"
