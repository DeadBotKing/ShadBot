"""
ShadBot Project Intelligence

Package Writer
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


class PackageWriter:
    """
    Writes Project Intelligence package artifacts to disk.
    """

    def write(
        self,
        path: Path,
        data: Any,
    ) -> None:
        """
        Write an object as formatted JSON.
        """

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                self._serialize(data),
                file,
                indent=4,
                ensure_ascii=False,
                sort_keys=True,
            )

    def _serialize(
        self,
        value: Any,
    ) -> Any:
        """
        Convert supported objects into JSON-serializable values.
        """

        if is_dataclass(value) and not isinstance(value, type):
            dataclass_value = value

            return self._serialize(
                asdict(dataclass_value),
            )

        if isinstance(
            value,
            dict,
        ):
            return {str(key): self._serialize(item) for key, item in value.items()}

        if isinstance(
            value,
            (list, tuple, set),
        ):
            return [self._serialize(item) for item in value]

        if isinstance(
            value,
            Path,
        ):
            return str(value)

        if hasattr(
            value,
            "isoformat",
        ):
            try:
                return value.isoformat()
            except TypeError:
                pass

        if hasattr(
            value,
            "hex",
        ):
            try:
                return str(value)
            except TypeError:
                pass

        return value
