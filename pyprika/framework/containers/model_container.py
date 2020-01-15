from pyprika.common.utils import auto_init


class ModelContainer:
    """Container for data models."""
    __slots__ = ['bookmarks', 'categories', 'groceries', 'meals', 'menus', 'menu_items', 'pantry', 'recipes', 'status']

    def __init__(self, bookmarks, categories, groceries, meals, menus, menu_items, pantry, recipe, status):
        """Initialize container."""
        auto_init()
