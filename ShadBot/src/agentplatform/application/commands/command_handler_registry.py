"""
ShadBot Agent Platform

Command Handler Registry
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.commands import (
    CommandContract,
)


@dataclass(slots=True)
class CommandHandlerRegistry:
    """
    Registry for command handlers.
    """

    _handlers: dict[
        str,
        CommandContract,
    ] = field(
        default_factory=dict,
    )

    def register(
        self,
        handler: CommandContract,
    ) -> None:
        """
        Register command handler.
        """

        command_name = handler.command_name

        if command_name in self._handlers:
            raise ValueError(f"Command handler already registered: " f"{command_name}")

        self._handlers[command_name] = handler

    def replace(
        self,
        handler: CommandContract,
    ) -> None:
        """
        Replace existing handler.
        """

        self._handlers[handler.command_name] = handler

    def unregister(
        self,
        command_name: str,
    ) -> None:
        """
        Remove command handler.
        """

        self._handlers.pop(
            command_name,
            None,
        )

    def get(
        self,
        command_name: str,
    ) -> CommandContract | None:
        """
        Resolve handler by command name.
        """

        return self._handlers.get(
            command_name,
        )

    def exists(
        self,
        command_name: str,
    ) -> bool:
        """
        Check handler existence.
        """

        return command_name in self._handlers

    def list_commands(
        self,
    ) -> tuple[str, ...]:
        """
        Return registered commands.
        """

        return tuple(
            self._handlers.keys(),
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all handlers.
        """

        self._handlers.clear()
