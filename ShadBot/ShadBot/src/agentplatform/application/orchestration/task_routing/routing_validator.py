"""
ShadBot Agent Platform

Routing Validator component for 6.1 Task Routing.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole


class RoutingValidator:
    """
    Validates if an agent routing decision is sound.
    """

    def validate(self, required_role: AgentRole, candidate_roles: tuple[AgentRole, ...]) -> tuple[bool, str]:
        if not candidate_roles:
            return (False, "No candidate roles in route decision.")
        if required_role not in candidate_roles:
            return (False, "Required role is missing from candidate roles.")
        return (True, "Route decision is valid.")
