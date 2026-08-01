"""
Agent Platform

Agent Role Domain Entity
"""

from __future__ import annotations

from enum import Enum


class AgentRole(str, Enum):
    """
    Defines the responsibility category of an agent.
    """

    ARCHITECT = "architect"

    ENGINEER = "engineer"

    REVIEWER = "reviewer"

    RESEARCHER = "researcher"

    TRADER = "trader"
