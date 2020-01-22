"""Unit of work to store retrieved data in local data store."""
from pyprika.framework.work_unit_base import AsyncWorkUnit


class StoreModels(AsyncWorkUnit):
    """Performs data store update unit of work."""

    __slots__ = ['domain_data_store']

    def __init__(self, domain_data_store):
        """Initialize the unit of work."""
        self.domain_data_store = domain_data_store

    async def perform_work(self, model_container):
        """Perform unit of work."""
        self.domain_data_store.data = model_container
        return model_container
