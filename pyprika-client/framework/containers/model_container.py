"""Container for transformed data models."""


class ModelContainer:
    """Container for data models."""
    __slots__ = ['bookmarks', 'categories', 'groceries', 'meals', 'menus', 'menu_items', 'pantry',
                 'recipes', 'status']

    def __init__(self, bookmarks, categories, groceries, meals, menus, menu_items, pantry, recipes,
                 status):
        """Initialize container."""
        self.bookmarks = bookmarks
        self.categories = categories
        self.groceries = groceries
        self.meals = meals
        self.menus = menus
        self.menu_items = menu_items
        self.pantry = pantry
        self.recipes = recipes
        self.status = status
