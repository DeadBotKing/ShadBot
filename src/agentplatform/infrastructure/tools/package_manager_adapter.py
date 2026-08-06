"""
ShadBot Agent Platform

Package manager tool adapter.
"""

from __future__ import annotations

import subprocess

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class PackageManagerAdapter(ToolContract):
    """
    Manage project packages.
    """

    @property
    def tool_type(self) -> ToolType:
        return ToolType.PACKAGE_MANAGER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        package = str(
            payload.get("package", ""),
        )

        action = str(
            payload.get("action", "install"),
        )

        if action == "install":

            command = f"pip install {package}"

        elif action == "remove":

            command = f"pip uninstall -y {package}"

        else:
            raise ValueError(
                f"Unsupported package action: {action}",
            )

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "errors": result.stderr,
        }
