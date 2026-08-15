"""
ShadBot Project Intelligence

Runtime Validator
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.runtime.runtime_configuration import (
    RuntimeConfiguration,
)


class RuntimeValidator:
    """
    Validates a RuntimeConfiguration before execution.
    """

    def validate(
        self,
        configuration: RuntimeConfiguration,
    ) -> None:
        """
        Validate the runtime configuration.

        Raises:
            ValueError:
                If the configuration is invalid.
        """

        workspace = configuration.workspace

        self._validate_workspace(
            workspace,
        )

        self._validate_output_directory(
            configuration.resolve_output_directory(),
        )

    def _validate_workspace(
        self,
        workspace: Path,
    ) -> None:
        """
        Validate the workspace path.
        """

        if not workspace.exists():
            raise ValueError(
                f"Workspace does not exist: {workspace}",
            )

        if not workspace.is_dir():
            raise ValueError(
                f"Workspace is not a directory: {workspace}",
            )

        if not workspace.is_absolute():
            raise ValueError(
                "Workspace path must be absolute.",
            )

    def _validate_output_directory(
        self,
        output_directory: Path,
    ) -> None:
        """
        Validate the output directory.
        """

        parent = output_directory.parent

        if not parent.exists():
            raise ValueError(
                f"Output parent directory does not exist: {parent}",
            )

        if not parent.is_dir():
            raise ValueError(
                f"Output parent is not a directory: {parent}",
            )
