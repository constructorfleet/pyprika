from abc import ABC, abstractmethod


class WorkUnit(ABC):
    """Abstract base class for unitt of work."""

    @abstractmethod
    async def perform_work(self, *args, **kwargs):
        """Perform work unit."""
