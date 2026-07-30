"""
ShadBot Project Intelligence

Intelligence JSON Serializer
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from typing import cast
from uuid import UUID

from projectintelligence.domain.export.intelligence_export_package import (
    IntelligenceExportPackage,
)


class IntelligenceJsonSerializer:
    """
    Serializes IntelligenceExportPackage into JSON-compatible data.
    """

    def serialize(
        self,
        package: IntelligenceExportPackage,
    ) -> dict[str, object]:
        """
        Convert intelligence package into JSON compatible structure.
        """

        return cast(
            dict[str, object],
            self._convert(asdict(package)),
        )

    def _convert(
        self,
        value: object,
    ) -> object:
        """
        Recursively convert unsupported JSON values.
        """

        if isinstance(value, dict):
            return {str(key): self._convert(item) for key, item in value.items()}

        if isinstance(value, list):
            return [self._convert(item) for item in value]

        if isinstance(value, tuple):
            return [self._convert(item) for item in value]

        if isinstance(value, UUID):
            return str(value)

        if isinstance(value, datetime):
            return value.isoformat()

        return value
