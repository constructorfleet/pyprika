"""Unit of work to store retrieved data in local data store."""
from pyprika.framework.work_unit_base import WorkUnit


class RetrieveModel(WorkUnit):
    """Performs retrieval of domain module unit of work."""

    __slots__ = ['model_container']

    def __init__(self, model_container):
        """Initialize the unit of work."""
        self.domain_data_store = domain_data_store

    async def __call__(self, model_container):
        """Perform unit of work."""
        self.domain_data_store.data = model_container
        return model_container
