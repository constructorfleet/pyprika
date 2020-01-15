from pyprika.common.utils import auto_init


class RecipeItem:
    """Model for recipe item resource."""

    __slots__ = ['hash', 'uid']

    @staticmethod
    def from_json(recipe_item_json):
        """Create model from json."""
        return RecipeItem(
            recipe_item_json.get('hash', None),
            recipe_item_json.get('uid', None)
        )

    def __init__(self, hash, uid):
        """Initialize the model."""
        auto_init()
