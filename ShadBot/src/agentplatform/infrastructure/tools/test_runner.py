"""
ShadBot Agent Platform

Test runner tool.
"""

from __future__ import annotations

import os
import subprocess
import sys

# Hard ceiling so a wedged child process can never hang the pipeline.
_SUBPROCESS_TIMEOUT_SECONDS = int(os.getenv("SHADBOT_SUBPROCESS_TIMEOUT", "600"))


class TestRunner:
    """
    Executes Python validation commands.
    """

    def run_python_file(
        self,
        path: str,
    ) -> dict[str, object]:
        """
        Execute a Python file and return result.
        """

        if os.environ.get("PYTEST_CURRENT_TEST"):
            return {
                "success": True,
                "return_code": 0,
                "stdout": f"[TEST RUNNER] skipped nested python execution for {path}",
                "stderr": "",
                "skipped": True,
            }

        try:
            process = subprocess.run(
                [
                    sys.executable,
                    path,
                ],
                capture_output=True,
                text=True,
                timeout=_SUBPROCESS_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "return_code": -1,
                "stdout": "",
                "stderr": (
                    f"Execution of {path} timed out after "
                    f"{_SUBPROCESS_TIMEOUT_SECONDS}s."
                ),
                "timed_out": True,
            }

        return {
            "success": process.returncode == 0,
            "return_code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
        }

    def run_pytest(
        self,
        path: str | None = None,
    ) -> dict[str, object]:
        """
        Execute pytest.
        """

        if os.environ.get("PYTEST_CURRENT_TEST"):
            return {
                "success": True,
                "return_code": 0,
                "stdout": "[TEST RUNNER] skipped nested pytest to prevent recursion",
                "stderr": "",
                "skipped": True,
                "path": path,
            }

        command = [
            sys.executable,
            "-m",
            "pytest",
        ]

        if path:
            command.append(path)

        try:
            process = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_SUBPROCESS_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "return_code": -1,
                "stdout": "",
                "stderr": (
                    f"pytest timed out after {_SUBPROCESS_TIMEOUT_SECONDS}s."
                ),
                "timed_out": True,
            }

        return {
            "success": process.returncode in (0, 5),
            "return_code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
        }
