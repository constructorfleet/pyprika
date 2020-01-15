"""Unit of work to link related models via relational identifier."""
from pyprika.common.utils import auto_init
from pyprika.framework.work_unit_base import WorkUnit


class LinkModels(WorkUnit):
    """Unit of work linking models via relational ids."""

    __slots__ = ['store_models']

    def __init__(self, store_models):
        """Initialize unit of work."""
        auto_init()

    async def perform_work(self, model_container):
        """Perform work unit."""
        for category in model_container.categories:
            category.link_to(model_container.categories)

        for menu_item in model_container.menu_items:
            menu_item.link_to(model_container.menus, model_container.recipes)

        for meal in model_container.meals:
            meal.link_to(model_container.recipes)

        for grocery_item in model_container.groceries:
            grocery_item.link_to(model_container.recipes)

        return await self.store_models.perform_work(model_container)
