"""Grocery data model."""
from pyprika.framework.models.base_model import BaseModel


class GroceryItem(BaseModel):
    """Model for grocery item resource."""

    __slots__ = ['name', 'ingredient', 'recipe_name', 'purchased', 'uid', 'recipe_uid',
                 'order_flag']

    @staticmethod
    def from_json(grocery_json):
        """Create model from json."""
        return GroceryItem(
            grocery_json.get('name', None),
            grocery_json.get('ingredient', None),
            grocery_json.get('recipe', None),
            grocery_json.get('purchased', False),
            grocery_json.get('uid', None),
            grocery_json.get('recipe_uid', None),
            grocery_json.get('order_flag', None)
        )

    def __init__(self, name, ingredient, recipe_name, purchased, uid, recipe_uid, order_flag):
        """Initialize the model."""
        self.name = name
        self.ingredient = ingredient
        self.recipe_name = recipe_name
        self.purchased = purchased
        self.uid = uid
        self.recipe_uid = recipe_uid
        self.order_flag = order_flag

        self.recipe = None

    async def link_to(self, recipes):
        """Link to transformed recipe model."""
        self.recipe = next((recipe for recipe in recipes if recipe.uid == self.recipe_uid), None)
