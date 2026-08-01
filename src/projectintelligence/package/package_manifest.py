"""
ShadBot Project Intelligence

Package Manifest
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(slots=True, frozen=True)
class PackageManifest:
    """
    Describes a Project Intelligence Package.
    """

    package_version: str = "1.0"

    intelligence_version: str = "1.0"

    schema_version: str = "1.0"

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    generator: str = "ShadBot Project Intelligence"

    format: str = "project-intelligence-package"

    def to_dict(self) -> dict[str, object]:
        """
        Convert the manifest to a JSON-serializable dictionary.
        """

        return {
            "package_version": self.package_version,
            "intelligence_version": self.intelligence_version,
            "schema_version": self.schema_version,
            "generated_at": self.generated_at.isoformat(),
            "generator": self.generator,
            "format": self.format,
        }
