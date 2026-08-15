"""
ShadBot Agent Platform

Brain Binding
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.brain import AgentBrain


@dataclass(frozen=True, slots=True)
class BrainBinding:
    """
    Immutable binding between an Agent and its Brain.
    """

    brain: AgentBrain
