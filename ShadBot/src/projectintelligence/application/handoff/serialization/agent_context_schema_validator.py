"""
ShadBot Project Intelligence

Agent Context Schema Validator
"""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import validate

from projectintelligence.application.handoff.serialization.agent_context_serializer import (
    AgentContextSerializer,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class AgentContextSchemaValidator:
    """
    Validates serialized Agent Context payloads
    against the official contract schema.
    """

    def __init__(
        self,
        schema_path: Path,
    ) -> None:
        self._schema_path = schema_path
        self._serializer = AgentContextSerializer()

    def validate_package(
        self,
        package: AgentContextPackage,
    ) -> None:
        """
        Validate an Agent Context package.
        """

        payload = self._serializer.serialize(
            package,
        )

        with self._schema_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            schema = json.load(
                file,
            )

        validate(
            instance=payload,
            schema=schema,
        )
