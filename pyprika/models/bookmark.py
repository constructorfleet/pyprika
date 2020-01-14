class Bookmark:
    """Model for bookmark resources."""
    
    def __init__(self, url, title, uid, order_flag):
        """Initialize model."""
        self._url = url
        self._title = title
        self._uid = uid
        self._order_flag = order_flag
        
    @property
    def url(self):
        """Get the bookmark's url."""
        return self._url
        
    @property
    def title(self):
        """Get the bookmark's title."""
        return self._bookmark

