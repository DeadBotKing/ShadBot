"""
ShadBot Agent Platform

Command Dispatcher
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.commands import (
    Command,
    CommandContract,
)
from agentplatform.domain.results import (
    AgentResult,
)


@dataclass(slots=True)
class CommandDispatcher:
    """
    Dispatches commands to registered handlers.
    """

    handlers: dict[str, CommandContract]

    def dispatch(
        self,
        command: Command,
    ) -> AgentResult:
        """
        Dispatch command execution.
        """

        handler = self._resolve_handler(
            command,
        )

        if handler is None:
            return AgentResult(
                success=False,
                message=(f"No handler registered " f"for command: {command.name}"),
            )

        if not handler.validate(
            command,
        ):
            return AgentResult(
                success=False,
                message=(f"Command validation failed: " f"{command.name}"),
            )

        try:
            return handler.execute(
                command,
            )

        except Exception as exc:
            return AgentResult(
                success=False,
                message=str(exc),
            )

    def register(
        self,
        handler: CommandContract,
    ) -> None:
        """
        Register command handler.
        """

        self.handlers[handler.command_name] = handler

    def unregister(
        self,
        command_name: str,
    ) -> None:
        """
        Remove command handler.
        """

        self.handlers.pop(
            command_name,
            None,
        )

    def _resolve_handler(
        self,
        command: Command,
    ) -> CommandContract | None:
        """
        Resolve handler by command name.
        """

        return self.handlers.get(
            command.name,
        )
