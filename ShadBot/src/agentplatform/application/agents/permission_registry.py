"""
ShadBot Agent Platform

Capability Permission Registry
"""

from __future__ import annotations

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)

from .capability_permission import (
    CapabilityPermission,
)


class PermissionRegistry:
    """
    Runtime capability permission manager.
    """

    def __init__(
        self,
    ) -> None:

        self._permissions: dict[
            tuple[AgentRole, AgentCapability],
            CapabilityPermission,
        ] = {}

    def register(
        self,
        permission: CapabilityPermission,
    ) -> None:
        """
        Register permission.
        """

        self._permissions[
            (
                permission.role,
                permission.capability,
            )
        ] = permission

    def check(
        self,
        role: AgentRole,
        capability: AgentCapability,
    ) -> bool:
        """
        Check execution permission.
        """

        permission = self._permissions.get(
            (
                role,
                capability,
            ),
        )

        if permission is None:
            return True

        return permission.can_execute()

    def deny(
        self,
        role: AgentRole,
        capability: AgentCapability,
        reason: str,
    ) -> None:
        """
        Disable capability execution.
        """

        self.register(
            CapabilityPermission(
                role=role,
                capability=capability,
                allowed=False,
                reason=reason,
            ),
        )

    def allow(
        self,
        role: AgentRole,
        capability: AgentCapability,
    ) -> None:
        """
        Enable capability execution.
        """

        self.register(
            CapabilityPermission(
                role=role,
                capability=capability,
                allowed=True,
            ),
        )
