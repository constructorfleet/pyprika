"""Menu data model."""
from pyprika.framework.models.base_model import BaseModel


class Menu(BaseModel):
    """Model for the menu resource."""

    __slots__ = ['name', 'notes', 'uid', 'order_flag']

    @staticmethod
    def from_json(mean_json):
        """Create model from json."""
        return Menu(
            mean_json.get('name', None),
            mean_json.get('notes', None),
            mean_json.get('uid', None),
            mean_json.get('order_flag', None)
        )

    def __init__(self, name, notes, uid, order_flag):
        """Initialize model."""
        self.name = name
        self.notes = notes
        self.uid = uid
        self.order_flag = order_flag

    async def link_to(self, *args):
        """Nothing to link to."""
        pass
