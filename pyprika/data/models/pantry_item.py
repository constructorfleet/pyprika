class PantryItem:
    """Model for pantry item resource."""

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return PantryItem(
            json_response.get('aisle', None),
            json_response.get('ingredient', None),
            json_response.get('uid', None)
        )

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
