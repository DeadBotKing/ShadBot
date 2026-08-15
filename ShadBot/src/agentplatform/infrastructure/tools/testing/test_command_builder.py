"""
ShadBot Agent Platform

Test Command Builder
"""

from __future__ import annotations

from .test_framework import TestFramework


class TestCommandBuilder:
    """
    Builds execution commands for test frameworks.
    """

    def build(
        self,
        *,
        framework: TestFramework,
        path: str | None = None,
        arguments: tuple[str, ...] = (),
    ) -> list[str]:

        if framework == TestFramework.PYTEST:

            command = [
                "pytest",
            ]

        elif framework == TestFramework.UNITTEST:

            command = [
                "python",
                "-m",
                "unittest",
            ]

        elif framework == TestFramework.DJANGO_TEST:

            command = [
                "python",
                "manage.py",
                "test",
            ]

        else:

            raise ValueError(
                "Unsupported test framework",
            )

        if path:
            command.append(
                path,
            )

        command.extend(
            arguments,
        )

        return command
