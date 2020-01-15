from pyprika.common.utils import auto_init


class MenuItem:
    """Model for the menu item resource."""

    __slots__ = ['name', 'uid', 'menu_uid', 'recipe_uid', 'order_flag']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return MenuItem(
            json_response.get('name', None),
            json_response.get('uid', None),
            json_response.get('menu_uid', None),
            json_response.get('recipe_uid', None),
            json_response.get('order_flag', None)
        )

    def __init__(self, name, uid, menu_uid, recipe_uid, order_flag):
        """Initialize model."""
        auto_init()
