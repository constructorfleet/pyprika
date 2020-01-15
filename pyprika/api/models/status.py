class Status:
    """Model for status resource."""

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
    def menuitems(self):
        """Get the number of menuitems."""
        return self.menuitems

    @property
    def categories(self):
        """Get the number of categories."""
        return self.categories
