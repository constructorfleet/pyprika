class Recipe:
    """Model for recipe resource."""

    def __init__(self, rating, photo_hash, on_favorites, photo, scale, ingredients, source, hash, source_url,
                 difficulty, categories, photo_url, cook_time, name, created, notes, image_url, prep_time, servings,
                 nutritional_info, uid):
        """Initialize the model."""
        self._rating = rating
        self._photo_hash = photo_hash
        self._on_favorites = on_favorites
        self._photo = photo
        self._uid = uid
        self._scale = scale
        self._ingredients = ingredients
        self._source = source
        self._hash = hash
        self._source_url = source_url
        self._difficulty = difficulty
        self._categories = categories
        self._photo_url = photo_url
        self._cook_time = cook_time
        self._name = name
        self._created = created
        self._notes = notes
        self._image_url = image_url
        self._prep_time = prep_time
        self._servings = servings
        self._nutritional_info = nutritional_info

    @property
    def rating(self):
        """Get the rating of the recipe."""
        return self._rating

    @property
    def photo_hash(self):
        """Get the photo_hash of the recipe."""
        return self._photo_hash

    @property
    def on_favorites(self):
        """Get the on_favorites of the recipe."""
        return self._on_favorites

    @property
    def photo(self):
        """Get the photo of the recipe."""
        return self._photo

    @property
    def uid(self):
        """Get the uid of the recipe."""
        return self._uid

    @property
    def scale(self):
        """Get the scale of the recipe."""
        return self._scale

    @property
    def ingredients(self):
        """Get the ingredients of the recipe."""
        return self._ingredients

    @property
    def source(self):
        """Get the source of the recipe."""
        return self._source

    @property
    def hash(self):
        """Get the hash of the recipe."""
        return self._hash

    @property
    def source_url(self):
        """Get the source_url of the recipe."""
        return self._source_url

    @property
    def difficulty(self):
        """Get the difficulty of the recipe."""
        return self._difficulty

    @property
    def categories(self):
        """Get the categories of the recipe."""
        return self._categories

    @property
    def photo_url(self):
        """Get the photo_url of the recipe."""
        return self._photo_url

    @property
    def cook_time(self):
        """Get the cook_time of the recipe."""
        return self._cook_time

    @property
    def name(self):
        """Get the name of the recipe."""
        return self._name

    @property
    def created(self):
        """Get the created of the recipe."""
        return self._created

    @property
    def notes(self):
        """Get the notes of the recipe."""
        return self._notes

    @property
    def image_url(self):
        """Get the image_url of the recipe."""
        return self._image_url

    @property
    def prep_time(self):
        """Get the prep_time of the recipe."""
        return self._prep_time

    @property
    def servings(self):
        """Get the servings of the recipe."""
        return self._servings

    @property
    def nutritional_info(self):
        """Get the nutritional_info of the recipe."""
        return self._nutritional_info
