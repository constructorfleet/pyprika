"""Tiny model containing the uid of recipe models."""
from pyprika.framework.models.base_model import BaseModel


class RecipeItem(BaseModel):
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
        self.hash = hash
        self.uid = uid

    async def link_to(self, *args):
        """Nothing to link to."""
        pass
