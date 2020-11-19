"""Local in-memory data store."""
import logging

_LOGGER = logging.getLogger(__name__)

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
        _LOGGER.warning('New Data {0}'.format(str(value)))
        self._data = value
