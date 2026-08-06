"""
ShadBot Agent Platform

Tool Execution Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from agentplatform.domain.agents import AgentRole

from .tool_permission_manager import ToolPermissionManager
from .tool_registry import ToolRegistry


@dataclass(frozen=True, slots=True)
class ToolExecutionResult:
    """
    Standard tool execution result.
    """

    success: bool

    tool_name: str

    output: Any = None

    error: str | None = None


class ToolExecutionEngine:
    """
    Executes tools for runtime agents.
    """

    def __init__(
        self,
        registry: ToolRegistry,
        permission_manager: ToolPermissionManager,
    ) -> None:

        self._registry = registry

        self._permission_manager = permission_manager

    def execute(
        self,
        *,
        role: AgentRole,
        tool_name: str,
        **kwargs: Any,
    ) -> ToolExecutionResult:
        """
        Execute requested tool.
        """

        tool = self._registry.get(
            tool_name,
        )

        if tool is None:

            return ToolExecutionResult(
                success=False,
                tool_name=tool_name,
                error="Tool not found",
            )

        if not self._permission_manager.check(
            role,
            tool.definition.capability,
        ):

            return ToolExecutionResult(
                success=False,
                tool_name=tool_name,
                error="Permission denied",
            )

        if not tool.is_available():

            return ToolExecutionResult(
                success=False,
                tool_name=tool_name,
                error="Tool unavailable",
            )

        if not tool.validate_input(
            **kwargs,
        ):

            return ToolExecutionResult(
                success=False,
                tool_name=tool_name,
                error="Invalid input",
            )

        try:

            result = tool.execute(
                **kwargs,
            )

            return ToolExecutionResult(
                success=True,
                tool_name=tool_name,
                output=result,
            )

        except Exception as exc:

            return ToolExecutionResult(
                success=False,
                tool_name=tool_name,
                error=str(exc),
            )
