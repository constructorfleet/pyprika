from pyprika.common.utils import auto_init


class PantryItem:
    """Model for pantry item resource."""

    __slots__ = ['aisle', 'ingredient', 'uid']

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
        auto_init()
