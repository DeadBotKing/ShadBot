"""
ShadBot Agent Platform

Profile application service.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.profile import AgentProfile

from .profile_registry import ProfileRegistry


class ProfileService:
    """
    Manages agent profile lifecycle.
    """

    def __init__(
        self,
        registry: ProfileRegistry | None = None,
    ) -> None:

        self._registry = registry or ProfileRegistry()

    def register(
        self,
        profile: AgentProfile,
    ) -> None:
        """
        Register profile.
        """

        self._registry.register(
            profile,
        )

    def resolve(
        self,
        role: AgentRole,
    ) -> AgentProfile | None:
        """
        Resolve agent profile.
        """

        return self._registry.get(
            role,
        )

    def available(
        self,
    ) -> tuple[AgentProfile, ...]:
        """
        List profiles.
        """

        return self._registry.all()
