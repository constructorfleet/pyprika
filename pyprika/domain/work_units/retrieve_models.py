from pyprika.common.utils import auto_init
from pyprika.framework.containers.model_container import ModelContainer
from pyprika.framework.work_unit_base import WorkUnit


class RetrieveModelsUnit(WorkUnit):
    """Retrieve models unit of work."""

    __slots__ = ['client', 'link_models']

    def __init__(self, client, link_models):
        """Initialize unit of work."""
        auto_init()

    async def perform_work(self):
        """Perform work unit."""
        await self.client.fetch_all()
