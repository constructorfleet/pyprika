from abc import ABC


class WorkUnit(ABC):
    """Abstract base class for unitt of work."""

    async def perform_work(self):
        """Perform work unit."""
        pass
