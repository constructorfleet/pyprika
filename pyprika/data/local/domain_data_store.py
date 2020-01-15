from datetime import datetime, timedelta


class DomainDataStore:
    """Data store for domain."""

    def __init__(self, fetch_delay=timedelta(hours=2.0)):
        self._last_fetch = None
        self._data = None
        self._fetch_delay = fetch_delay

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

    @property
    def should_fetch(self):
        if not self._last_fetch:
            return True
        return datetime.utcnow() - self._last_fetch > self._fetch_delay
