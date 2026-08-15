from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class GitCommit:
    """
    Represents a Git commit.

    This model is immutable and contains commit metadata only.
    """

    hash: str
    short_hash: str
    author: str
    email: str
    message: str
    date: datetime
