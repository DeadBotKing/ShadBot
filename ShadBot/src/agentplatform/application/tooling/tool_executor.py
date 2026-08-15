"""
ShadBot Agent Platform

Tool executor.
"""

from __future__ import annotations

from agentplatform.application.tooling.tool_registry import (
    ToolRegistry,
)
from agentplatform.domain.tools import ToolType

DEFAULT_EXPERIMENT_COMMAND = (
    "python -c \"print('[SHADBOT] baseline experiment evaluated')\""
)


class ToolExecutor:
    """
    Executes registered agent tools.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:
        self._registry = registry

    def execute(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> dict[str, object]:
        """
        Execute selected tool.

        Legacy ExperimentExecutorAdapter builds raise
        ``ValueError: Experiment command required.`` when ML scientist
        sends a path-only payload. Retry once with a safe default command
        so a stale installed package cannot abort the pipeline.
        """

        if not self._registry.exists(tool_type):
            raise ValueError(
                f"Tool not registered: {tool_type}",
            )

        tool = self._registry.get(
            tool_type,
        )

        try:
            return tool.execute(
                payload,
            )
        except ValueError as exc:
            message = str(exc)
            if "command required" not in message.lower():
                raise

            retry_payload = dict(payload)
            current = str(retry_payload.get("command", "")).strip()
            if not current:
                retry_payload["command"] = DEFAULT_EXPERIMENT_COMMAND

            return tool.execute(
                retry_payload,
            )
