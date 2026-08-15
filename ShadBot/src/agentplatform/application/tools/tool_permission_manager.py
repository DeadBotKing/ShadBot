"""
ShadBot Agent Platform

Tool Permission Manager
"""

from __future__ import annotations

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)

from .tool_permission import ToolPermission


class ToolPermissionManager:
    """
    Runtime permission manager for tools.
    """

    def __init__(
        self,
    ) -> None:

        self._permissions: dict[
            tuple[AgentRole, AgentCapability],
            ToolPermission,
        ] = {}

    def register(
        self,
        permission: ToolPermission,
    ) -> None:
        """
        Register permission rule.
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
        Validate execution permission.
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
            ToolPermission(
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
            ToolPermission(
                role=role,
                capability=capability,
            ),
        )
