from pyprika.common.utils import auto_init
from pyprika.framework.models.base_model import BaseModel


class Meal(BaseModel):
    """Model for a meal resource."""

    __slots__ = ['name', 'type', 'date', 'uid', 'recipe_uid', 'order_flag']

    @staticmethod
    def from_json(meal_json):
        """Create model from json."""
        return Meal(
            meal_json.get('name', None),
            meal_json.get('type', None),
            meal_json.get('date', None),
            meal_json.get('uid', None),
            meal_json.get('recipe_uid', None),
            meal_json.get('order_flag', None)
        )

    def __init__(self, name, meal_type, meal_date, uid, recipe_uid, order_flag):
        """Initialize the model."""
        auto_init()
        self.recipe = None

    async def link_to(self, recipes):
        self.recipe = next((recipe for recipe in recipes if recipe.uid == self.recipe_uid), None)
