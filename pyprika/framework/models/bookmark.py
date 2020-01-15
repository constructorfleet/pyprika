from pyprika.common.utils import auto_init


class Bookmark:
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
