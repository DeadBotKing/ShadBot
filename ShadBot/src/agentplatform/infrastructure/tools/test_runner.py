"""
ShadBot Agent Platform

Test runner tool.
"""

from __future__ import annotations

import os
import subprocess
import sys


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

        process = subprocess.run(
            [
                sys.executable,
                path,
            ],
            capture_output=True,
            text=True,
        )

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

        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        return {
            "success": process.returncode == 0,
            "return_code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
        }
