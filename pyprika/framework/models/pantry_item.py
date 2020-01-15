from pyprika.common.utils import auto_init


class PantryItem:
    """Model for pantry item resource."""

    __slots__ = ['aisle', 'ingredient', 'uid']

    @staticmethod
    def from_json(pantry_item_json):
        """Create model from json."""
        return PantryItem(
            pantry_item_json.get('aisle', None),
            pantry_item_json.get('ingredient', None),
            pantry_item_json.get('uid', None)
        )

    def __init__(self, aisle, ingredient, uid):
        """Initialize the model."""
        auto_init()
