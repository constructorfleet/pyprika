"""Unit of work to link related models via relational identifier."""
from pyprika.framework.work_unit_base import AsyncWorkUnit


class LinkModels(AsyncWorkUnit):
    """Unit of work linking models via relational ids."""

    __slots__ = ['store_models']

    def __init__(self, store_models):
        """Initialize unit of work."""
        self.store_models = store_models

    async def perform_work(self, model_container):
        """Perform work unit."""
        for category in model_container.categories:
            await category.link_to(model_container.categories)

        for menu_item in model_container.menu_items:
            await menu_item.link_to(model_container.menus, model_container.recipes)

        for meal in model_container.meals:
            await meal.link_to(model_container.recipes)

        for grocery_item in model_container.groceries:
            await grocery_item.link_to(model_container.recipes)

        for recipe in model_container.recipes:
            await recipe.link_to(model_container.categories)

        return await self.store_models.perform_work(model_container)
