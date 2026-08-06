"""
ShadBot Agent Platform

Agent brain profile definition.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import AgentRole


@dataclass(frozen=True, slots=True)
class BrainProfile:
    """
    Defines cognitive identity of an agent.
    """

    role: AgentRole

    reasoning_style: str

    planning_style: str

    decision_style: str

    reflection_style: str

    validation_style: str
