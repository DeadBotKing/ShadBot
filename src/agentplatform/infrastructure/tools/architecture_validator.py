"""
ShadBot Agent Platform

Architecture validation tool.
"""

from __future__ import annotations

from pathlib import Path


class ArchitectureValidator:
    """
    Validates project architecture rules.
    """

    def validate(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Validate enterprise architecture constraints.
        """

        issues: list[str] = []

        required_directories = [
            "domain",
            "application",
            "infrastructure",
        ]

        for directory in required_directories:
            if not (path / directory).exists():
                issues.append(
                    f"Missing required layer: {directory}",
                )

        forbidden_locations = [
            "domain",
        ]

        for layer in forbidden_locations:
            layer_path = path / layer

            if layer_path.exists():
                for file_path in layer_path.rglob("*.py"):
                    content = file_path.read_text(
                        encoding="utf-8",
                    )

                    if "infrastructure" in content:
                        issues.append(
                            f"Dependency violation: {file_path}",
                        )

        return {
            "status": "PASS" if not issues else "FAIL",
            "issues": issues,
        }
