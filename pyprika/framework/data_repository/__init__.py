from abc import ABC, abstractmethod

DATA_LOCATION_LOCAL = 'local'
DATA_LOCATION_REMOTE = 'remote'


class DataRepository:
    """Base class for data repositories."""

    def __init__(self, data_location):
        """Initialize repository."""
        self._location = data_location


    @abstractmethod
    async def get(self):
        """Retrieve items from repository."""
        pass

    @abstractmethod
    async def save(self):
        """Save items to repository,"""

    async def login(self, username, password, **kwargs):
        """Authenticate against the repository."""
        return True

    async def logout(self):
        """Log out of the repository"""
        return True

    @property
    def is_authenticated(self):
        """Whether we are authenticated with the repository."""
