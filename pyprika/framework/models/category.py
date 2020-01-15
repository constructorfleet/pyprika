class Category:
    """Model for category resource."""

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Category(
            json_response.get('name', None),
            json_response.get('uid', None),
            json_response.get('_parent_uid', None),
            json_response.get('order_flag', None)
        )

    def __init__(self, name, uid, parent_uid, order_flag):
        """Initialize the model."""
        self._name = name
        self._uid = uid
        self._parent_uid = parent_uid
        self._order_flag = order_flag

    @property
    def name(self):
        """Get the category name."""
        return self._name
