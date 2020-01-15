from pyprika.common.utils import auto_init


class Meal:
    """Model for a meal resource."""

    __slots__ = ['name', 'type', 'date', 'uid', 'recipe_uid', 'order_flag']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Meal(
            json_response.get('name', None),
            json_response.get('type', None),
            json_response.get('date', None),
            json_response.get('uid', None),
            json_response.get('recipe_uid', None),
            json_response.get('order_flag', None)
        )

    def __init__(self, name, meal_type, meal_date, uid, recipe_uid, order_flag):
        """Initialize the model."""
        auto_init()
