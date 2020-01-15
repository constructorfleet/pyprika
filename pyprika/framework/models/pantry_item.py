"""Pantry item data model."""
from pyprika.framework.models.base_model import BaseModel


class PantryItem(BaseModel):
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
        self.aisle = aisle
        self.ingredient = ingredient
        self.uid = uid

    async def link_to(self, *args):
        """Nothing to link to."""
        pass
