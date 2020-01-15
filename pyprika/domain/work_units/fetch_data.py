from pyprika.common.utils import auto_init
from pyprika.framework.work_unit_base import WorkUnit


class FetchData(WorkUnit):
    """Retrieve models unit of work."""

    __slots__ = ['client', 'transform_models', 'domain_data_store']

    def __init__(self, client, transform_models, domain_data_store):
        """Initialize unit of work."""
        auto_init()

    async def perform_work(self):
        """Perform work unit."""
        if not self.domain_data_store.should_fetch:
            return self.domain_data_store.data

        await self.client.fetch_all()
        return await self.transform_models.perform_work(
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
