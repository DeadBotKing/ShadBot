"""
ShadBot Agent Platform

Agent profile registry.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.profile import AgentProfile


class ProfileRegistry:
    """
    Stores and resolves agent cognitive profiles.
    """

    def __init__(self) -> None:
        self._profiles: dict[
            AgentRole,
            AgentProfile,
        ] = {}

    def register(
        self,
        profile: AgentProfile,
    ) -> None:
        """
        Register agent profile.
        """

        self._profiles[profile.role] = profile

    def get(
        self,
        role: AgentRole,
    ) -> AgentProfile | None:
        """
        Resolve profile by role.
        """

        return self._profiles.get(
            role,
        )

    def exists(
        self,
        role: AgentRole,
    ) -> bool:
        """
        Check profile existence.
        """

        return role in self._profiles

    def all(
        self,
    ) -> tuple[AgentProfile, ...]:
        """
        Return registered profiles.
        """

        return tuple(
            self._profiles.values(),
        )
