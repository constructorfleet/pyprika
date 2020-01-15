from datetime import datetime


class DomainDataStore:
    """Data store for domain."""

    def __init__(self):
        self._last_fetch = None
        self._data = None

    @property
    def data(self):
        """Get current domain data."""
        return self._data

    @data.setter
    def data(self, value):
        """Update the data store and last fetch time."""
        self._last_fetch = datetime.utcnow()
        self._data = value

    @property
    def last_fetch(self):
        """Get the last fetch time."""
        return self._last_fetch
