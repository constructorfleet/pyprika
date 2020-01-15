from pyprika.common.utils import auto_init


class Category:
    """Model for category resource."""

    __slots__ = ['name', 'uid', 'parent_uid', 'order_flag']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Category(
            json_response.get('name', None),
            json_response.get('uid', None),
            json_response.get('parent_uid', None),
            json_response.get('order_flag', None)
        )

    def __init__(self, name, uid, parent_uid, order_flag):
        """Initialize the model."""
        auto_init()
