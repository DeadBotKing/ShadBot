"""
ShadBot Agent Platform

Profile context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.profile import ProfileService
from agentplatform.domain.agents import AgentRole


class ProfileContextProvider:
    """
    Provides agent profile context.
    """

    def __init__(
        self,
        profile_service: ProfileService,
        role: AgentRole,
    ) -> None:

        self._profile_service = profile_service
        self._role = role

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build profile context.
        """

        profile = self._profile_service.resolve(
            self._role,
        )

        if profile is None:
            return {}

        return {
            "profile_id": str(profile.profile_id),
            "role": profile.role.value,
            "name": profile.name,
            "reasoning_style": profile.reasoning_style,
            "planning_style": profile.planning_style,
            "decision_style": profile.decision_style,
            "reflection_style": profile.reflection_style,
            "validation_style": profile.validation_style,
            "capabilities": [capability.value for capability in profile.capabilities],
        }
