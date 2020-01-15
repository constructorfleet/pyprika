class Meal:
    """Model for a meal resource."""
    
    def __init__(self, name, meal_type, meal_date, uid, recipe_uid, order_flag):
        """Initialize the model."""
        self._name = name
        self._meal_type = meal_type
        self._meal_date = meal_date
        self._uid = uid
        self._recipe_uid = recipe_uid
        self._order_flag = order_flag
        
    @property
    def name(self):
        """Get the name of the meal."""
        return self._name
        
    @property
    def meal_type(self):
        """Get the type of meal."""
        return self._meal_type
        
    @property
    def meal_date(self):
        """Get the date of the meal."""
        return self._meal_date

