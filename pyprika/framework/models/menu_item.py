from pyprika.common.utils import auto_init


class MenuItem:
    """Model for the menu item resource."""

    __slots__ = ['name', 'uid', 'menu_uid', 'recipe_uid', 'order_flag', 'menu', 'recipe']

    @staticmethod
    def from_json(menu_item_json, menus, recipes):
        """Create model from json."""
        menu_item = MenuItem(
            menu_item_json.get('name', None),
            menu_item_json.get('uid', None),
            menu_item_json.get('menu_uid', None),
            menu_item_json.get('recipe_uid', None),
            menu_item_json.get('order_flag', None)
        )

        menu_item.menu = next((menu for menu in menus if menu.uid == menu_item.menu_uid), None)
        menu_item.recipe = next((recipe for recipe in recipes if recipe.uid == menu_item.recipe_uid), None)

        return menu_item

    def __init__(self, name, uid, menu_uid, recipe_uid, order_flag):
        """Initialize model."""
        auto_init()
