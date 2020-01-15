class RecipeItem:
    """Model for recipe item resource."""

    def __init__(self, hash, uid):
        """Initialze the model."""
        self._hash = hash
        self._uid = uid
