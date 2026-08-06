"""
ShadBot Agent Platform

Quality validation tool.
"""

from __future__ import annotations

from pathlib import Path

from .terminal_tool import TerminalTool


class QualityValidator:
    """
    Executes enterprise quality validation pipeline.
    """

    def __init__(self) -> None:
        self._terminal = TerminalTool()

    def validate(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Run complete project quality validation.
        """

        checks = {
            "ruff": self._run(
                "ruff check .",
                path,
            ),
            "black": self._run(
                "black --check .",
                path,
            ),
            "mypy": self._run(
                "mypy src",
                path,
            ),
            "pytest": self._run(
                "pytest",
                path,
            ),
        }

        passed = all(item["success"] for item in checks.values())

        return {
            "status": "PASS" if passed else "FAIL",
            "checks": checks,
        }

    def _run(
        self,
        command: str,
        path: Path,
    ) -> dict[str, object]:
        output = self._terminal.execute(
            command,
            str(path),
        )

        return {
            "success": "error" not in output.lower(),
            "output": output,
        }
