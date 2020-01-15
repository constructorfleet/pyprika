class Menu:
    """Model for the menu resource."""
    
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
