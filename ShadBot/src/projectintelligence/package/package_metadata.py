"""
ShadBot Project Intelligence

Package Metadata
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID


@dataclass(slots=True, frozen=True)
class PackageMetadata:
    """
    Runtime metadata for generated intelligence package.
    """

    project_id: UUID

    project_name: str

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    engine_version: str = "1.0"

    package_type: str = "intelligence"

    def to_dict(self) -> dict[str, object]:
        """
        Convert metadata to JSON-compatible data.
        """

        return {
            "project_id": str(self.project_id),
            "project_name": self.project_name,
            "generated_at": self.generated_at.isoformat(),
            "engine_version": self.engine_version,
            "package_type": self.package_type,
        }
