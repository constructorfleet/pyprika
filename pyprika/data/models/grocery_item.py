class GroceryItem:
    """Model for grocery item resource."""

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
        self._name = name
        self._ingredient = ingredient
        self._recipe = recipe
        self._purchased = purchased
        self._uid = uid
        self._recipe_uid = recipe_uid
        self._order_flag = order_flag
        
    @property
    def name(self):
        """Get the name of the grocery item."""
        return self._name
        
    @property
    def ingredient(self):
        """Get the name of the ingredient."""
        return self._ingredient
        
    @property
    def recipe(self):
        """Name of the recipe."""
        return self._recipe
        
    @property
    def aisle(self):
        """Get the aisle of the grocery item."""
        return self._aisle
        
    @property
    def is_purchased(self):
        """Get whether the grocery item is purchased."""
        return self._purchased
 
