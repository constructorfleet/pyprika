from pyprika.common.utils import auto_init


class Menu:
    """Model for the menu resource."""

    __slots__ = ['name', 'notes', 'uid', 'order_flag']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Menu(
            json_response.get('name', None),
            json_response.get('notes', None),
            json_response.get('uid', None),
            json_response.get('order_flag', None)
        )

    def __init__(self, name, notes, uid, order_flag):
        """Initialize model."""
        auto_init()
