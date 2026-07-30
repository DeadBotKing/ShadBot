"""
ShadBot Project Intelligence

JSON Export Writer
"""

from __future__ import annotations

import json
from pathlib import Path


class JsonExportWriter:
    """
    Writes JSON export artifacts to filesystem.
    """

    def write(
        self,
        data: dict[str, object],
        destination: Path,
    ) -> None:
        """
        Persist JSON data into filesystem.
        """

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
