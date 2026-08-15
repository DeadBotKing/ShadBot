"""
ShadBot Agent Platform

Test Runner Tool
"""

from __future__ import annotations

import subprocess

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .test_command_builder import TestCommandBuilder
from .test_execution_context import TestExecutionContext
from .test_framework import TestFramework
from .test_result import TestResult


class TestRunnerTool(ToolContract):
    """
    Executes project tests.
    """

    def __init__(
        self,
        command_builder: TestCommandBuilder,
    ) -> None:

        self._command_builder = command_builder

    @property
    def tool_type(
        self,
    ) -> ToolType:

        return ToolType.TEST_RUNNER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        context = TestExecutionContext(
            project_id=payload["project_id"],
            working_directory=str(
                payload["working_directory"],
            ),
            framework=TestFramework(
                payload["framework"],
            ),
            test_path=payload.get(
                "test_path",
            ),
            arguments=tuple(
                payload.get(
                    "arguments",
                    (),
                ),
            ),
        )

        command = self._command_builder.build(
            framework=context.framework,
            path=context.test_path,
            arguments=context.arguments,
        )

        process = subprocess.run(
            command,
            cwd=context.working_directory,
            capture_output=True,
            text=True,
        )

        result = TestResult(
            success=process.returncode == 0,
            exit_code=process.returncode,
            output=process.stdout,
            errors=process.stderr,
        )

        return {
            "result": result,
            "command": command,
        }
