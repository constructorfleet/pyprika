class MenuItem:
    """Model for the menu item resource."""

    def __init__(self, name, uid, menu_uid, recipe_uid, order_flag):
        """Initialize model."""
        self._name = name
        self._menu_uid = menu_uid
        self._uid = uid
        self._recipe_uid = recipe_uid
        self._order_flag = order_flag

    @property
    def name(self):
        """Get the name of the menu."""
        return self._name
