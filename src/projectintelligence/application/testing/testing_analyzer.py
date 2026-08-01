"""
ShadBot Project Intelligence

Testing Analyzer
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import UUID

from projectintelligence.application.testing.detectors.pytest_detector import (
    PytestDetector,
)
from projectintelligence.application.testing.detectors.unittest_detector import (
    UnittestDetector,
)
from projectintelligence.domain.testing.testing_context import (
    TestingContext,
)


@dataclass(slots=True)
class TestingAnalyzer:
    """
    Analyzes project testing intelligence.
    """

    pytest_detector: PytestDetector
    unittest_detector: UnittestDetector

    def analyze(
        self,
        workspace: Path,
        project_id: UUID,
    ) -> TestingContext:
        """
        Analyze project testing capabilities.
        """

        context = TestingContext(
            project_id=project_id,
        )

        detectors = (
            self.pytest_detector,
            self.unittest_detector,
        )

        for detector in detectors:
            frameworks = detector.detect(
                workspace,
            )

            for framework in frameworks:
                context.detected_frameworks.append(
                    framework.name,
                )

        tests_directory = workspace / "tests"

        if tests_directory.exists():
            context.test_directories.append(
                str(
                    tests_directory.relative_to(workspace),
                ),
            )

            context.test_files = [
                str(path.relative_to(workspace))
                for path in tests_directory.rglob("test_*.py")
            ]

            context.total_tests = len(
                context.test_files,
            )

        return context
