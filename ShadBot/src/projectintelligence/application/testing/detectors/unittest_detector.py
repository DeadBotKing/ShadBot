"""
ShadBot Project Intelligence

Unittest Detector
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.domain.testing.models.test_framework import (
    TestFramework,
)


class UnittestDetector:
    """
    Detects Python unittest usage.
    """

    def detect(
        self,
        workspace: Path,
    ) -> list[TestFramework]:
        """
        Detect unittest based tests.
        """

        tests_directory = workspace / "tests"

        if not tests_directory.exists():
            return []

        for file in tests_directory.rglob("*.py"):
            content = file.read_text(
                encoding="utf-8",
            )

            if "unittest" in content:
                return [
                    TestFramework(
                        name="unittest",
                        language="Python",
                        manifest=str(
                            file.relative_to(workspace),
                        ),
                    )
                ]

        return []
