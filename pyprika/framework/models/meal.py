from pyprika.common.utils import auto_init


class Meal:
    """Model for a meal resource."""

    __slots__ = ['name', 'type', 'date', 'uid', 'recipe_uid', 'order_flag', 'recipe']

    @staticmethod
    def from_json(meal_json, recipes):
        """Create model from json."""
        meal = Meal(
            meal_json.get('name', None),
            meal_json.get('type', None),
            meal_json.get('date', None),
            meal_json.get('uid', None),
            meal_json.get('recipe_uid', None),
            meal_json.get('order_flag', None)
        )

        meal.recipe = next((recipe for recipe in recipes if recipe.uid == meal.recipe_uid), None)

        return meal

    def __init__(self, name, meal_type, meal_date, uid, recipe_uid, order_flag):
        """Initialize the model."""
        auto_init()
