"""Local in-memory data store."""


class DomainDataStore:
    """Data store for domain."""

    def __init__(self):
        """Initialize the data store."""
        self._data = None

    @property
    def data(self):
        """Get current domain data."""
        return self._data

    @data.setter
    def data(self, value):
        """Update the data store and last fetch time."""
        self._data = value
