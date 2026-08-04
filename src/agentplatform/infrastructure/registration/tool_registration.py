"""
ShadBot Agent Platform

Default tool registration.
"""

from __future__ import annotations

from agentplatform.application.tooling import ToolRegistry
from agentplatform.domain.tooling import ToolDefinition
from agentplatform.domain.tools import ToolType
from agentplatform.infrastructure.tools.filesystem_tool_adapter import (
    FileSystemToolAdapter,
)
from agentplatform.infrastructure.tools.git_tool_adapter import (
    GitToolAdapter,
)
from agentplatform.infrastructure.tools.test_runner_adapter import (
    TestRunnerAdapter,
)


def register_default_tools(
    registry: ToolRegistry,
) -> ToolRegistry:
    """
    Register built-in agent tools.
    """

    registry.register(
        ToolDefinition(
            name="filesystem",
            tool_type=ToolType.FILE_SYSTEM,
            description="Read and write project files.",
        ),
        FileSystemToolAdapter(),
    )

    registry.register(
        ToolDefinition(
            name="test_runner",
            tool_type=ToolType.TEST_RUNNER,
            description="Execute project tests.",
        ),
        TestRunnerAdapter(),
    )

    registry.register(
        ToolDefinition(
            name="git",
            tool_type=ToolType.GIT,
            description="Inspect git repository state and changes.",
        ),
        GitToolAdapter(),
    )

    return registry
