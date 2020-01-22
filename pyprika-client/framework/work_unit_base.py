from abc import ABC, abstractmethod


class AsyncWorkUnit(ABC):
    """Abstract base class for asynchronous unit of work."""

    @abstractmethod
    async def perform_work(self, *args, **kwargs):
        """Perform work unit."""


class WorkUnit(ABC):
    """Abstract base class for unit of work."""

    @abstractmethod
    def perform_work(self, *args, **kwargs):
        """Perform work unit."""
