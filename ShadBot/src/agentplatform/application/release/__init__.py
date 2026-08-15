"""
ShadBot Agent Platform

Phase 12 Production Freeze V1.0 module.
"""

from .architecture_freeze import ArchitectureFreezeManager, ArchitectureFreezeReport
from .contract_freeze import ContractFreezeManager, ContractFreezeReport
from .integration_verifier import FullIntegrationVerifier, IntegrationVerificationReport
from .production_governance import ProductionGovernanceManager, ProductionGovernancePackage
from .release_manager import EnterpriseReleaseManager, EnterpriseReleasePackage
from .release_service import ProductionReleaseService

__all__ = [
    "IntegrationVerificationReport",
    "FullIntegrationVerifier",
    "ArchitectureFreezeReport",
    "ArchitectureFreezeManager",
    "ContractFreezeReport",
    "ContractFreezeManager",
    "ProductionGovernancePackage",
    "ProductionGovernanceManager",
    "EnterpriseReleasePackage",
    "EnterpriseReleaseManager",
    "ProductionReleaseService",
]
