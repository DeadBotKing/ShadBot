"""
ShadBot Agent Platform

Environment Analyzer
"""

from __future__ import annotations

import platform
from pathlib import Path

from .environment_profile import (
    EnvironmentProfile,
)
from .environment_understanding_result import (
    EnvironmentUnderstandingResult,
)


class EnvironmentAnalyzer:
    """
    Understands execution environment.

    Responsible for:
    - OS detection
    - runtime awareness
    - workspace environment context

    Does not:
    - modify workspace
    - execute commands
    - analyze source code
    """

    def analyze(
        self,
        workspace_path: Path,
    ) -> EnvironmentUnderstandingResult:
        """
        Analyze environment.
        """

        profile = EnvironmentProfile(
            operating_system=platform.system(),
            workspace_path=workspace_path,
            languages=(),
            frameworks=(),
            tools=(),
            runtime_versions={},
        )

        return EnvironmentUnderstandingResult(
            profile=profile,
            detected=True,
            confidence=1.0,
        )
