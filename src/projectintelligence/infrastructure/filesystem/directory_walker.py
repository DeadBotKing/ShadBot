"""
ShadBot Project Intelligence

Directory Walker
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path


class DirectoryWalker:
    """
    Traverses a workspace directory and yields all paths.

    This component is intentionally unaware of ignore rules,
    language detection, or file filtering.
    """

    def walk(
        self,
        root: Path,
    ) -> Iterator[Path]:
        """
        Yield every file and directory under the given root.
        """

        yield from root.rglob("*")
