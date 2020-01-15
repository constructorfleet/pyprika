class PantryItem:
    """Model for pantry item resource."""

    def __init__(self, aisle, ingredient, uid):
        """Initialize the model."""
        self._aisle = aisle
        self._ingredient = ingredient,
        self._uid = uid

    @property
    def aisle(self):
        """Get the aisle for the pantry item."""
        return self._aisle

    @property
    def ingredient(self):
        """Get the ingredient for the pantry item."""
        return self._ingredient
