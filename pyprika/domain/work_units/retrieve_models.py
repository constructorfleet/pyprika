from pyprika.common.utils import auto_init
from pyprika.framework.work_unit_base import WorkUnit


class RetrieveModels(WorkUnit):
    """Retrieve models unit of work."""

    __slots__ = ['client', 'transform_models']

    def __init__(self, client, transform_models):
        """Initialize unit of work."""
        auto_init()

    async def perform_work(self):
        """Perform work unit."""
        await self.client.fetch_all()
        await self.transform_models.perform_work(
            bookmarks=self.client.get_bookmarks(),
            categories=self.client.get_categories(),
            groceries=self.client.get_groceries(),
            meals=self.client.get_meals(),
            menus=self.client.get_menus(),
            menu_items=self.client.get_menu_items(),
            pantry_items=self.client.get_pantry_items(),
            recipes=self.client.get_recipes(),
            status=self.client.get_status()
        )
