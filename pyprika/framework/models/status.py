from pyprika.common.utils import auto_init


class Status:
    """Model for status resource."""

    __slots__ = ['recipes', 'pantry', 'meals', 'menus', 'groceries', 'bookmarks', 'menu_items', 'categories']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Status(
            json_response.get('recipes', 0),
            json_response.get('pantry', 0),
            json_response.get('meals', 0),
            json_response.get('menu', 0),
            json_response.get('groceries', 0),
            json_response.get('bookmarks', 0),
            json_response.get('menuitems', 0),
            json_response.get('categories', 0)
        )

    def __init__(self, recipes, pantry, meals, menus, groceries, bookmarks, menu_items, categories):
        """Initialize the model."""
        auto_init()
