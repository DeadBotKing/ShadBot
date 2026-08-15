"""
ShadBot Agent Platform

Git Repository Tool
"""

from __future__ import annotations

import subprocess

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .git_command_builder import (
    GitCommandBuilder,
)
from .git_execution_context import (
    GitExecutionContext,
)
from .git_operation import GitOperation
from .git_result import (
    GitResult,
)


class GitRepositoryTool(ToolContract):
    """
    Executes git repository operations.
    """

    def __init__(
        self,
        command_builder: GitCommandBuilder,
    ) -> None:

        self._command_builder = command_builder

    @property
    def tool_type(
        self,
    ) -> ToolType:

        return ToolType.GIT

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        context = GitExecutionContext(
            project_id=payload["project_id"],
            repository_path=str(
                payload["repository_path"],
            ),
            operation=GitOperation(
                payload["operation"],
            ),
            arguments=tuple(
                payload.get(
                    "arguments",
                    (),
                ),
            ),
        )

        command = self._command_builder.build(
            context.operation,
            context.arguments,
        )

        process = subprocess.run(
            command,
            cwd=context.repository_path,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        result = GitResult(
            success=process.returncode == 0,
            exit_code=process.returncode,
            output=process.stdout,
            error=process.stderr,
        )

        return {
            "result": result,
            "command": command,
        }
