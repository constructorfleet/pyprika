"""Menu data model."""
from pyprika.common.utils import auto_init
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
        auto_init()

    async def link_to(self, *args):
        """Nothing to link to."""
        pass
