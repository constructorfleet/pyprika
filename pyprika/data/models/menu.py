class Menu:
    """Model for the menu resource."""

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Menu(
            json_response.get('name', None),
            json_response.get('notes', None),
            json_response.get('uid', None),
            json_response.get('order_flag', None)
        )
    
    def __init__(self, name, notes, uid, order_flag):
        """Initialize model."""
        self._name = name
        self._notes = notes
        self._uid = uid
        self._order_flag = order_flag

    @property
    def name(self):
        """Get the name of the menu."""
        return self._name

    @property
    def notes(self):
        """Get the notes for the menu."""
        return self._notes
