from abc import ABC


class Nameable(ABC):
    """Interface for named classes."""

    def __init__(self, item_name):
        self._name = item_name

    @property
    def name(self):
        """Get the name of the item."""
        return self._name