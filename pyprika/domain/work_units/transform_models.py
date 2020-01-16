"""Uni of work that transforms JSON data to data models."""
from pyprika.framework.containers.model_container import ModelContainer
from pyprika.framework.models.bookmark import Bookmark
from pyprika.framework.models.category import Category
from pyprika.framework.models.grocery_item import GroceryItem
from pyprika.framework.models.meal import Meal
from pyprika.framework.models.menu import Menu
from pyprika.framework.models.menu_item import MenuItem
from pyprika.framework.models.pantry_item import PantryItem
from pyprika.framework.models.recipe import Recipe
from pyprika.framework.models.status import Status
from pyprika.framework.work_unit_base import AsyncWorkUnit


class TransformModels(AsyncWorkUnit):
    """Unit of work to create domain models."""

    __slots__ = ['link_models']

    def __init__(self, link_models):
        """Initialize unit of work."""
        self.link_models = link_models

    async def perform_work(self, bookmarks, categories, groceries, meals, menus, menu_items,
                           pantry_items, recipes,
                           status):
        """Perform unit of work."""
        model_container = ModelContainer(
            [Bookmark.from_json(bookmark) for bookmark in bookmarks],
            [Category.from_json(category) for category in categories],
            [GroceryItem.from_json(grocery_item) for grocery_item in groceries],
            [Meal.from_json(meal) for meal in meals],
            [Menu.from_json(menu) for menu in menus],
            [MenuItem.from_json(menu_item) for menu_item in menu_items],
            [PantryItem.from_json(pantry_item) for pantry_item in pantry_items],
            [Recipe.from_json(recipe) for recipe in recipes],
            Status.from_json(status)
        )
        return await self.link_models.perform_work(model_container)
