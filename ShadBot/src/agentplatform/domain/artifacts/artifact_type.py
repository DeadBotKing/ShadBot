"""
ShadBot Agent Platform

Generated artifact types.
"""

from __future__ import annotations

from enum import Enum


class ArtifactType(str, Enum):
    """
    Types of generated artifacts.
    """

    SOURCE_CODE = "source_code"

    TEST_CODE = "test_code"

    CONFIGURATION = "configuration"

    DOCUMENTATION = "documentation"
