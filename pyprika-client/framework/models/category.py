"""Category data model."""
from pyprika.framework.models.base_model import BaseModel


class Category(BaseModel):
    """Model for category resource."""

    __slots__ = ['name', 'uid', 'parent_uid', 'order_flag']

    @staticmethod
    def from_json(category_json):
        """Create model from json."""
        return Category(
            category_json.get('name', None),
            category_json.get('uid', None),
            category_json.get('parent_uid', None),
            category_json.get('order_flag', None)
        )

    def __init__(self, name, uid, parent_uid, order_flag):
        """Initialize the model."""
        self.name = name
        self.uid = uid
        self.parent_uid = parent_uid
        self.order_flag = order_flag
        self.parent_category = None

    async def link_to(self, categories):
        """Link categories to parents."""
        self.parent_category = next(
            (parent_category for parent_category in categories if
             parent_category.uid == self.parent_uid), None)
