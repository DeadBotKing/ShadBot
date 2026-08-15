"""
ShadBot Project Intelligence

Service Container
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ServiceContainer:
    """
    Central dependency injection container.

    Responsible for registering and resolving
    application services.
    """

    _services: dict[type, Any]

    def register(
        self,
        service_type: type,
        instance: Any,
    ) -> None:
        """
        Register a service instance.
        """
        self._services[service_type] = instance

    def resolve(
        self,
        service_type: type,
    ) -> Any:
        """
        Resolve a registered service.
        """
        return self._services[service_type]
