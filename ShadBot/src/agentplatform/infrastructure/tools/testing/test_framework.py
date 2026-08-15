"""
ShadBot Agent Platform

Test Framework Definition
"""

from __future__ import annotations

from enum import Enum


class TestFramework(str, Enum):
    """
    Supported testing frameworks.
    """

    PYTEST = "pytest"

    UNITTEST = "unittest"

    DJANGO_TEST = "django_test"
