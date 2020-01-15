from pyprika.common.utils import auto_init


class Bookmark:
    """Model for bookmark resources."""

    __slots__ = ['url', 'title', 'uid', 'order_flag']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Bookmark(
            json_response.get('url', None),
            json_response.get('title', None),
            json_response.get('uid', None),
            json_response.get('order_flag', None)
        )

    def __init__(self, url, title, uid, order_flag):
        """Initialize model."""
        auto_init()
