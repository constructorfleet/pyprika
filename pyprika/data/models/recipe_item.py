class RecipeItem:
    """Model for recipe item resource."""

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return RecipeItem(
            json_response.get('hash', None),
            json_response.get('uid', None)
        )

    def __init__(self, hash, uid):
        """Initialze the model."""
        self._hash = hash
        self._uid = uid
