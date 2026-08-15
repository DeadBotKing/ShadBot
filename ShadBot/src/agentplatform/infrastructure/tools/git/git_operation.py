"""
ShadBot Agent Platform

Git Operations
"""

from __future__ import annotations

from enum import Enum


class GitOperation(str, Enum):
    """
    Supported git operations.
    """

    STATUS = "status"

    DIFF = "diff"

    LOG = "log"

    BRANCH = "branch"

    ADD = "add"

    COMMIT = "commit"

    CHECKOUT = "checkout"
