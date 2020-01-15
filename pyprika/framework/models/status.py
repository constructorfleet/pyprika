class Status:
    """Model for status resource."""

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
        self._recipes = recipes
        self._pantry = pantry
        self._meals = meals
        self._menus = menus
        self._groceries = groceries
        self._bookmarks = bookmarks
        self._menu_items = menu_items
        self._categories = categories

    @property
    def recipes(self):
        """Get the number of recipes."""
        return self.recipes

    @property
    def pantry(self):
        """Get the number of pantry."""
        return self.pantry

    @property
    def meals(self):
        """Get the number of meals."""
        return self.meals

    @property
    def menus(self):
        """Get the number of menus."""
        return self.menus

    @property
    def groceries(self):
        """Get the number of groceries."""
        return self.groceries

    @property
    def bookmarks(self):
        """Get the number of bookmarks."""
        return self.bookmarks

    @property
    def menu_items(self):
        """Get the number of menu items."""
        return self.menu_items

    @property
    def categories(self):
        """Get the number of categories."""
        return self.categories
