"""
ShadBot Agent Platform

Agent Assignment component for 5.8 Planning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.agents import AgentRole
from .execution_planning import PlannedStep


@dataclass(frozen=True, slots=True)
class AssignedStep:
    step: PlannedStep
    assigned_role: AgentRole


class AgentAssigner:
    """
    Assigns appropriate agent roles to planned execution steps.
    """

    def assign(self, steps: Sequence[PlannedStep]) -> tuple[AssignedStep, ...]:
        assigned: list[AssignedStep] = []
        role_map = {
            "architect": AgentRole.ARCHITECT,
            "engineer": AgentRole.ENGINEER,
            "reviewer": AgentRole.REVIEWER,
        }
        for st in steps:
            req = st.subtask.required_role.lower()
            role = role_map.get(req, AgentRole.ENGINEER)
            assigned.append(
                AssignedStep(
                    step=st,
                    assigned_role=role,
                )
            )
        return tuple(assigned)
