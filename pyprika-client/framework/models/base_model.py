"""Base class for data models."""
from abc import abstractmethod, ABC


class BaseModel(ABC):
    """Abstract base class for unitt of work."""

    @abstractmethod
    async def link_to(self, *args):
        """Link to parent models."""
        pass
