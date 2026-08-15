"""
ShadBot Agent Platform

Command Contract Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from agentplatform.domain.commands import (
    Command,
)
from agentplatform.domain.results import (
    AgentResult,
)

TCommand = TypeVar(
    "TCommand",
    bound=Command,
)


class CommandContract(
    ABC,
    Generic[TCommand],
):
    """
    Base contract for command handlers.
    """

    @property
    @abstractmethod
    def command_name(
        self,
    ) -> str:
        """
        Unique command identifier.
        """

        raise NotImplementedError

    @abstractmethod
    def can_handle(
        self,
        command: TCommand,
    ) -> bool:
        """
        Check command compatibility.
        """

        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        command: TCommand,
    ) -> AgentResult:
        """
        Execute command.
        """

        raise NotImplementedError

    def validate(
        self,
        command: TCommand,
    ) -> bool:
        """
        Default command validation.
        """

        return command.name == self.command_name
