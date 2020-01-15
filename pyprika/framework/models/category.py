from pyprika.common.utils import auto_init


class Category:
    """Model for category resource."""

    __slots__ = ['name', 'uid', 'parent_uid', 'order_flag', 'parent_category']

    @staticmethod
    def from_json(category_json):
        """Create model from json."""
        return Category(
            category_json.get('name', None),
            category_json.get('uid', None),
            category_json.get('parent_uid', None),
            category_json.get('order_flag', None)
        )

    @staticmethod
    def assign_parent_category(category, categories):
        """Assign the parent category object to category."""
        category.parent_category = next(
            (parent_category for parent_category in categories if parent_category.uid == category.parent_uid), None)

    def __init__(self, name, uid, parent_uid, order_flag):
        """Initialize the model."""
        auto_init()
