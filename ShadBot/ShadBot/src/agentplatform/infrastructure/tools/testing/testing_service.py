"""
ShadBot Agent Platform

Testing Service
"""

from __future__ import annotations

from .test_runner_tool import TestRunnerTool


class TestingService:
    """
    Application service for testing execution.
    """

    def __init__(
        self,
        runner: TestRunnerTool,
    ) -> None:

        self._runner = runner

    def run(
        self,
        request: dict[str, object],
    ) -> dict[str, object]:

        return self._runner.execute(
            request,
        )
