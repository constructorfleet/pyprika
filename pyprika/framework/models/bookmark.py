from pyprika.common.utils import auto_init
from pyprika.framework.models.base_model import BaseModel


class Bookmark(BaseModel):
    """Model for bookmark resources."""

    __slots__ = ['url', 'title', 'uid', 'order_flag']

    @staticmethod
    def from_json(bookmark_json):
        """Create model from json."""
        return Bookmark(
            bookmark_json.get('url', None),
            bookmark_json.get('title', None),
            bookmark_json.get('uid', None),
            bookmark_json.get('order_flag', None)
        )

    def __init__(self, url, title, uid, order_flag):
        """Initialize model."""
        auto_init()

    async def link_to(self):
        pass
