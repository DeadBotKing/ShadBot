"""
ShadBot Agent Platform

Behavior Constraints component for 5.7 Profile Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .profile_loader import LoadedProfile


@dataclass(frozen=True, slots=True)
class BehaviorConstraintSet:
    role: str
    forbidden_actions: tuple[str, ...]
    mandatory_guidelines: tuple[str, ...]


class BehaviorConstraints:
    """
    Enforces behavioral guidelines and constraints based on cognitive profile.
    """

    def enforce(self, profile: LoadedProfile) -> BehaviorConstraintSet:
        if profile.role.value == "architect":
            forbidden = ("write_source_code", "modify_production_db")
            mandatory = ("design_clean_architecture", "verify_dependency_rules")
        elif profile.role.value == "engineer":
            forbidden = ("skip_unit_tests", "violate_architecture_contracts")
            mandatory = ("write_production_code", "ensure_test_coverage")
        else:
            forbidden = ("unauthorized_modification",)
            mandatory = ("adhere_to_contracts",)

        return BehaviorConstraintSet(
            role=profile.role.value,
            forbidden_actions=forbidden,
            mandatory_guidelines=mandatory,
        )
