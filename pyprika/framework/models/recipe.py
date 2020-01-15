from pyprika.common.utils import auto_init


class Recipe:
    """Model for recipe resource."""

    __slots__ = ['rating', 'photo_hash', 'on_favorites', 'photo', 'scale', 'ingredients', 'source', 'hash',
                 'source_url', 'difficulty', 'categories', 'photo_url', 'cook_time', 'name', 'created', 'notes',
                 'image_url', 'prep_time', 'servings', 'nutritional_info', 'uid']

    @staticmethod
    def from_json(json_response):
        """Create model from json."""
        return Recipe(
            json_response.get('rating', None),
            json_response.get('photo_hash', None),
            json_response.get('on_favorites', False),
            json_response.get('photo', None),
            json_response.get('scale', None),
            json_response.get('ingredients', None),
            json_response.get('source', None),
            json_response.get('hash', None),
            json_response.get('source_url', None),
            json_response.get('difficulty', None),
            json_response.get('categories', None),
            json_response.get('photo_url', None),
            json_response.get('cook_time', None),
            json_response.get('name', None),
            json_response.get('created', None),
            json_response.get('notes', None),
            json_response.get('image_url', None),
            json_response.get('prep_time', None),
            json_response.get('servings', None),
            json_response.get('nutritional_info', None),
            json_response.get('uid', None)
        )

    def __init__(self, rating, photo_hash, on_favorites, photo, scale, ingredients, source, hash, source_url,
                 difficulty, categories, photo_url, cook_time, name, created, notes, image_url, prep_time, servings,
                 nutritional_info, uid):
        """Initialize the model."""
        auto_init()
