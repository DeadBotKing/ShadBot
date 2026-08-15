"""
ShadBot Agent Platform

Agent Profile Loading component for 5.7 Profile Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from agentplatform.domain.agents import AgentRole


@dataclass(frozen=True, slots=True)
class LoadedProfile:
    role: AgentRole
    cognitive_style: str
    risk_tolerance: str
    focus_areas: tuple[str, ...]


class ProfileLoader:
    """
    Loads cognitive profile for a specified agent role.
    """

    def load(self, role: AgentRole) -> LoadedProfile:
        styles = {
            AgentRole.ARCHITECT: ("system_architect", "low", ("architecture", "scalability")),
            AgentRole.ENGINEER: ("pragmatic_engineer", "medium", ("implementation", "clean_code")),
            AgentRole.REVIEWER: ("critical_reviewer", "low", ("quality", "security")),
        }
        style, risk, focus = styles.get(role, ("general_agent", "medium", ("execution",)))
        return LoadedProfile(
            role=role,
            cognitive_style=style,
            risk_tolerance=risk,
            focus_areas=focus,
        )
