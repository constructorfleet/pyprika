"""Base class for data models."""
from abc import abstractmethod, ABC


class BaseModel(ABC):
    """Abstract base class for unitt of work."""

    @property
    def resource_name(self):
        """Get the name of the resource."""
        return self.__class__.__name__.lower

    @abstractmethod
    async def link_to(self, *args):
        """Link to parent models."""
        pass


