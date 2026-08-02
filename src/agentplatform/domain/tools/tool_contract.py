"""
ShadBot Agent Platform

Tool execution contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.tools.tool_type import ToolType


class ToolContract(ABC):
    """
    Base contract for executable tools.
    """

    @property
    @abstractmethod
    def tool_type(
        self,
    ) -> ToolType:
        """
        Tool identifier.
        """

        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        """
        Execute tool.
        """

        raise NotImplementedError
