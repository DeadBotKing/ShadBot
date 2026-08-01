"""
ShadBot Project Intelligence

Pytest Detector
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.testing.contracts.test_detector import (
    ITestDetector,
)
from projectintelligence.domain.testing.models.test_framework import (
    TestFramework,
)


class PytestDetector(ITestDetector):
    """
    Detects pytest based testing setup.
    """

    def detect(
        self,
        workspace: Path,
    ) -> list[TestFramework]:
        """
        Detect pytest usage in project.
        """

        indicators = (
            "pytest.ini",
            "pyproject.toml",
            "tox.ini",
            "conftest.py",
        )

        for indicator in indicators:
            if any(
                workspace.rglob(indicator),
            ):
                return [
                    TestFramework(
                        name="pytest",
                        language="Python",
                        manifest=indicator,
                    )
                ]

        return []
