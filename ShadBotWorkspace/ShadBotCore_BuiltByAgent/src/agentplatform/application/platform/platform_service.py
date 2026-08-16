from dataclasses import dataclass, field

@dataclass(frozen=True)
class PlatformStatus:
    is_finalized: bool = False

class PlatformService:
    """
    Orchestrates platform finalization and API Gateway (Phase 11).
    """

    def __init__(self):
        self._status = PlatformStatus()

    def finalize_platform(self) -> None:
        """
        Finalizes the platform by setting up the API Gateway and other necessary configurations.
        """
        if not self._status.is_finalized:
            # Placeholder for platform finalization logic
            self._status = PlatformStatus(is_finalized=True)
            print("Platform has been finalized.")
        else:
            raise RuntimeError("Platform is already finalized.")

    def get_platform_status(self) -> bool:
        """
        Returns the current status of the platform.
        """
        return self._status.is_finalized

# Example usage
if __name__ == "__main__":
    platform_service = PlatformService()
    try:
        platform_service.finalize_platform()
        print(f"Platform finalized: {platform_service.get_platform_status()}")
    except RuntimeError as e:
        print(e)