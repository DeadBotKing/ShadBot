"""
ShadBot Agent Platform

Capability Registry
"""

from __future__ import annotations

from collections.abc import Mapping

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


class CapabilityRegistry:
    """
    Enterprise registry for mapping agent roles
    to their available capabilities.
    """

    def __init__(
        self,
    ) -> None:

        self._role_mapping: dict[
            AgentRole,
            set[AgentCapability],
        ] = {
            AgentRole.ARCHITECT: {
                AgentCapability.ARCHITECTURE_ANALYSIS,
                AgentCapability.DESIGN_REVIEW,
                AgentCapability.DEPENDENCY_ANALYSIS,
            },
            AgentRole.ENGINEER: {
                AgentCapability.CODE_GENERATION,
                AgentCapability.CODE_REFACTORING,
                AgentCapability.TEST_GENERATION,
            },
            AgentRole.REVIEWER: {
                AgentCapability.CODE_REVIEW,
                AgentCapability.SECURITY_REVIEW,
                AgentCapability.BUG_DETECTION,
            },
            AgentRole.RESEARCHER: {
                AgentCapability.RESEARCH,
            },
            AgentRole.PROJECT_INTELLIGENCE: {
                AgentCapability.ARCHITECTURE_ANALYSIS,
                AgentCapability.DESIGN_REVIEW,
                AgentCapability.DEPENDENCY_ANALYSIS,
            },
            AgentRole.QA: {
                AgentCapability.TEST_GENERATION,
                AgentCapability.CODE_REVIEW,
                AgentCapability.BUG_DETECTION,
            },
            AgentRole.RUNTIME_OBSERVER: {
                AgentCapability.BUG_DETECTION,
                AgentCapability.MODEL_EVALUATION,
            },
            AgentRole.ML_SCIENTIST: {
                AgentCapability.FEATURE_ENGINEERING,
                AgentCapability.MODEL_EVALUATION,
            },
            AgentRole.RND: {
                AgentCapability.RESEARCH,
                AgentCapability.FEATURE_ENGINEERING,
                AgentCapability.MODEL_EVALUATION,
            },
        }

    def get_capabilities(
        self,
        role: AgentRole,
    ) -> set[AgentCapability]:
        """
        Get capabilities assigned to role.
        """

        return set(
            self._role_mapping.get(
                role,
                set(),
            ),
        )

    def supports(
        self,
        role: AgentRole,
        capability: AgentCapability,
    ) -> bool:
        """
        Check whether role supports capability.
        """

        return capability in self._role_mapping.get(
            role,
            set(),
        )

    def register_role_mapping(
        self,
        role: AgentRole,
        capabilities: set[AgentCapability],
    ) -> None:
        """
        Register or replace role capability mapping.
        """

        self._role_mapping[role] = set(
            capabilities,
        )

    def remove_capability(
        self,
        role: AgentRole,
        capability: AgentCapability,
    ) -> None:
        """
        Remove capability from role.
        """

        if role in self._role_mapping:
            self._role_mapping[role].discard(
                capability,
            )

    def add_capability(
        self,
        role: AgentRole,
        capability: AgentCapability,
    ) -> None:
        """
        Add capability to role.
        """

        self._role_mapping.setdefault(
            role,
            set(),
        ).add(
            capability,
        )

    def all_mappings(
        self,
    ) -> Mapping[
        AgentRole,
        set[AgentCapability],
    ]:
        """
        Return current capability mapping.
        """

        return {
            role: set(capabilities) for role, capabilities in self._role_mapping.items()
        }

    def roles_for_capability(
        self,
        capability: AgentCapability,
    ) -> set[AgentRole]:
        """
        Find all roles supporting a capability.
        """

        return {
            role
            for role, capabilities in self._role_mapping.items()
            if capability in capabilities
        }

    def has_capability(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check capability existence in registry.
        """

        return any(
            capability in capabilities for capabilities in self._role_mapping.values()
        )

    def all_capabilities(
        self,
    ) -> set[AgentCapability]:
        """
        Return all registered capabilities.
        """

        capabilities: set[AgentCapability] = set()

        for role_capabilities in self._role_mapping.values():
            capabilities.update(
                role_capabilities,
            )

        return capabilities

    def lookup(
        self,
        capability: AgentCapability,
    ) -> set[AgentRole]:
        """
        Runtime capability lookup.

        Alias for roles_for_capability.
        """

        return self.roles_for_capability(
            capability,
        )

    def validate(
        self,
    ) -> dict[str, object]:
        """
        Validate capability registry integrity.
        """

        errors: list[str] = []

        for role, capabilities in self._role_mapping.items():

            if not isinstance(
                role,
                AgentRole,
            ):
                errors.append(
                    f"Invalid role: {role}",
                )

            if not capabilities:
                errors.append(
                    f"Role {role.value} has no capabilities",
                )

            for capability in capabilities:

                if not isinstance(
                    capability,
                    AgentCapability,
                ):
                    errors.append(
                        f"Invalid capability {capability}",
                    )

        return {
            "valid": len(errors) == 0,
            "roles": len(
                self._role_mapping,
            ),
            "capabilities": len(
                self.all_capabilities(),
            ),
            "errors": errors,
        }
