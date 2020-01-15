from pyprika.common.utils import auto_init


class GroceryItem:
    """Model for grocery item resource."""

    __slots__ = ['name', 'ingredient', 'recipe_name', 'purchased', 'uid', 'recipe_uid', 'order_flag', 'recipe']

    @staticmethod
    def from_json(grocery_json, recipes):
        """Create model from json."""
        grocery_item = GroceryItem(
            grocery_json.get('name', None),
            grocery_json.get('ingredient', None),
            grocery_json.get('recipe', None),
            grocery_json.get('purchased', False),
            grocery_json.get('uid', None),
            grocery_json.get('recipe_uid', None),
            grocery_json.get('order_flag', None)
        )

        grocery_item.recipe = next((recipe for recipe in recipes if recipe.uid == grocery_item.recipe_uid), None)

        return grocery_item

    def __init__(self, name, ingredient, recipe_name, purchased, uid, recipe_uid, order_flag):
        """Initialize the model."""
        auto_init()
