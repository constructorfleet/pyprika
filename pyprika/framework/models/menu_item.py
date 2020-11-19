"""Menu item data model."""
from pyprika.framework.models.base_model import BaseModel


class MenuItem(BaseModel):
    """Model for the menu item resource."""

    __slots__ = ['name', 'uid', 'menu_uid', 'recipe_uid', 'order_flag']

    @staticmethod
    def from_json(menu_item_json, menus, recipes):
        """Create model from json."""
        return MenuItem(
            menu_item_json.get('name', None),
            menu_item_json.get('uid', None),
            menu_item_json.get('menu_uid', None),
            menu_item_json.get('recipe_uid', None),
            menu_item_json.get('order_flag', None)
        )

    def __init__(self, name, uid, menu_uid, recipe_uid, order_flag):
        """Initialize model."""
        self.name = name
        self.uid = uid
        self.menu_uid = menu_uid
        self.recipe_uid = recipe_uid
        self.order_flag = order_flag
        self.menu = None
        self.recipe = None

    async def link_to(self, menus, recipes):
        """Link to the associated menu and recipe models."""
        self.menu = next((menu for menu in menus if menu.uid == self.menu_uid), None)
        self.recipe = next((recipe for recipe in recipes if recipe.uid == self.recipe_uid), None)
