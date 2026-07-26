"""
ShadBot Project Intelligence

File Collector
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


class FileCollector:
    """
    Collects file paths from a sequence of filesystem paths.
    """

    def collect(
        self,
        paths: Iterable[Path],
    ) -> list[Path]:
        """
        Return only file entries.
        """

        return [path for path in paths if path.is_file()]
