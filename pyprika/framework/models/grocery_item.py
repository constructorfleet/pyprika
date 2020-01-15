from pyprika.common.utils import auto_init


class GroceryItem:
    """Model for grocery item resource."""

    __slots__ = ['name', 'ingredient', 'recipe', 'purchased', 'uid', 'recipe_uid', 'order_flag']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return GroceryItem(
            json_response.get('name', None),
            json_response.get('ingredient', None),
            json_response.get('recipe', None),
            json_response.get('purchased', False),
            json_response.get('uid', None),
            json_response.get('recipe_uid', None),
            json_response.get('order_flag', None)
        )
    
    def __init__(self, name, ingredient, recipe, purchased, uid, recipe_uid, order_flag):
        """Initialize the model."""
        auto_init()
