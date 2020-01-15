from pyprika.common.utils import auto_init
from pyprika.framework.containers.model_container import ModelContainer
from pyprika.framework.work_unit_base import WorkUnit


class LinkModelsUnit(WorkUnit):
    """Unit of work linking models via relational ids."""

    __slots__ = ['client']

    def __init__(self, client):
        """Initialize unit of work."""
        auto_init()

    async def perform_work(self):
        """Perform work unit."""
        return ModelContainer(

        )