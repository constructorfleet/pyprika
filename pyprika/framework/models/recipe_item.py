from pyprika.common.utils import auto_init


class RecipeItem:
    """Model for recipe item resource."""

    __slots__ = ['hash', 'uid']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return RecipeItem(
            json_response.get('hash', None),
            json_response.get('uid', None)
        )

    def __init__(self, hash, uid):
        """Initialize the model."""
        auto_init()
