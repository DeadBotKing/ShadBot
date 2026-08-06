"""
ShadBot Agent Platform

Tool Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from agentplatform.domain.tools import Tool


class ToolContract(ABC):
    """
    Base contract for executable tools.
    """

    @property
    @abstractmethod
    def definition(
        self,
    ) -> Tool:
        """
        Return tool metadata.
        """

        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        **kwargs: Any,
    ) -> Any:
        """
        Execute tool operation.
        """

        raise NotImplementedError

    def validate_input(
        self,
        **kwargs: Any,
    ) -> bool:
        """
        Validate execution input.

        Default implementation accepts input.
        """

        return True

    def is_available(
        self,
    ) -> bool:
        """
        Check tool availability.
        """

        return self.definition.can_execute()
