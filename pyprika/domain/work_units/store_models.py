from pyprika.common.utils import auto_init
from pyprika.framework.work_unit_base import WorkUnit


class StoreModels(WorkUnit):
    """Performs data store update unit of work."""

    __slots__ = ['domain_data_store']

    def __init__(self, domain_data_store):
        """Initialize the unit of work."""
        auto_init()

    async def perform_work(self, model_container):
        self.domain_data_store.data = model_container
        return model_container
