"""User recipe book status model."""
from pyprika.framework.models.base_model import BaseModel


class Status(BaseModel):
    """Model for status resource."""

    __slots__ = ['recipes', 'pantry', 'meals', 'menus', 'groceries', 'bookmarks', 'menu_items',
                 'categories']

    @staticmethod
    def from_json(status_json):
        """Create model from json."""
        return Status(
            status_json.get('recipes', 0),
            status_json.get('pantry', 0),
            status_json.get('meals', 0),
            status_json.get('menu', 0),
            status_json.get('groceries', 0),
            status_json.get('bookmarks', 0),
            status_json.get('menuitems', 0),
            status_json.get('categories', 0)
        )

    def __init__(self, recipes, pantry, meals, menus, groceries, bookmarks, menu_items, categories):
        """Initialize the model."""
        self.recipes = recipes
        self.pantry = pantry
        self.meals = meals
        self.menus = menus
        self.groceries = groceries
        self.bookmarks = bookmarks
        self.menu_items = menu_items
        self.categories = categories

    async def link_to(self, *args):
        """Nothing to link to."""
        pass
