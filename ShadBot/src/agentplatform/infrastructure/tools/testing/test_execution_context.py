"""
ShadBot Agent Platform

Test Execution Context
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .test_framework import TestFramework


@dataclass(frozen=True, slots=True)
class TestExecutionContext:
    """
    Context required for test execution.
    """

    project_id: UUID

    working_directory: str

    framework: TestFramework

    test_path: str | None = None

    arguments: tuple[str, ...] = ()
