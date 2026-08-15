"""
ShadBot Agent Platform

Tool Execution Binding
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)


class ToolExecutor(Protocol):
    """
    Execution contract for tools.
    """

    def execute(
        self,
        payload: dict[str, object],
    ) -> AgentResult:
        """
        Execute tool operation.
        """

        ...


@dataclass(slots=True)
class ToolExecutionBinding:
    """
    Runtime binding between tools and executors.
    """

    executors: dict[
        ToolType,
        ToolExecutor,
    ] = field(
        default_factory=dict,
    )

    def bind(
        self,
        tool_type: ToolType,
        executor: ToolExecutor,
    ) -> None:
        """
        Attach executor to tool.
        """

        if tool_type in self.executors:
            raise ValueError(
                ("Tool executor already " f"registered: {tool_type}"),
            )

        self.executors[tool_type] = executor

    def replace(
        self,
        tool_type: ToolType,
        executor: ToolExecutor,
    ) -> None:
        """
        Replace existing executor.
        """

        self.executors[tool_type] = executor

    def unbind(
        self,
        tool_type: ToolType,
    ) -> None:
        """
        Remove executor binding.
        """

        self.executors.pop(
            tool_type,
            None,
        )

    def resolve(
        self,
        tool_type: ToolType,
    ) -> ToolExecutor | None:
        """
        Resolve executor for tool.
        """

        return self.executors.get(
            tool_type,
        )

    def can_execute(
        self,
        tool_type: ToolType,
    ) -> bool:
        """
        Check execution availability.
        """

        return tool_type in self.executors

    def execute(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> AgentResult:
        """
        Execute tool through bound executor.
        """

        executor = self.resolve(
            tool_type,
        )

        if executor is None:
            return AgentResult(
                success=False,
                message=("No executor bound for tool: " f"{tool_type}"),
            )

        return executor.execute(
            payload,
        )

    def list_bindings(
        self,
    ) -> frozenset[ToolType]:
        """
        Return immutable execution map snapshot.
        """

        return frozenset(
            self.executors.keys(),
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all execution bindings.
        """

        self.executors.clear()
