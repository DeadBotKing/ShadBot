"""
ShadBot Agent Platform

Unified service for Phase 12 Production Freeze V1.0.
"""

from __future__ import annotations

from .architecture_freeze import ArchitectureFreezeManager
from .contract_freeze import ContractFreezeManager
from .integration_verifier import FullIntegrationVerifier
from .production_governance import ProductionGovernanceManager
from .release_manager import EnterpriseReleaseManager, EnterpriseReleasePackage


class ProductionReleaseService:
    """
    Orchestrates integration verification, architecture freeze, contract freeze, and V1.0 release packaging.
    """

    def __init__(self) -> None:
        self.verifier = FullIntegrationVerifier()
        self.arch_mgr = ArchitectureFreezeManager()
        self.cont_mgr = ContractFreezeManager()
        self.gov_mgr = ProductionGovernanceManager()
        self.release_mgr = EnterpriseReleaseManager()

    def execute_release_freeze(self) -> EnterpriseReleasePackage:
        integ = self.verifier.verify_all()
        arch = self.arch_mgr.freeze()
        cont = self.cont_mgr.freeze_contracts()
        gov = self.gov_mgr.establish()
        return self.release_mgr.release_v1(integ, arch, cont, gov)

    def get_release_summary(self) -> dict[str, object]:
        pkg = self.execute_release_freeze()
        return pkg.to_dict()
