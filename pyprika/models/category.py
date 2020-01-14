class Category:
    """Model for category resource."""
    
    def __init__(self, name, uid,  parent_uid, order_flag):
        """Initialize the model."""
        self._name = name
        self._uid = uid
        self._parent_uid
        self._order_flag
        
    @property
    def name:
        """Get the category name."""
        return self._name

