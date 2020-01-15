from pyprika.common.utils import auto_init
from pyprika.framework.models.base_model import BaseModel


class Recipe(BaseModel):
    """Model for recipe resource."""

    __slots__ = ['rating', 'photo_hash', 'on_favorites', 'photo', 'scale', 'ingredients', 'source', 'hash',
                 'source_url', 'difficulty', 'categories', 'photo_url', 'cook_time', 'name', 'created', 'notes',
                 'image_url', 'prep_time', 'servings', 'nutritional_info', 'uid']

    @staticmethod
    def from_json(recipe_json):
        """Create model from json."""
        return Recipe(
            recipe_json.get('rating', None),
            recipe_json.get('photo_hash', None),
            recipe_json.get('on_favorites', False),
            recipe_json.get('photo', None),
            recipe_json.get('scale', None),
            recipe_json.get('ingredients', None),
            recipe_json.get('source', None),
            recipe_json.get('hash', None),
            recipe_json.get('source_url', None),
            recipe_json.get('difficulty', None),
            recipe_json.get('categories', None),
            recipe_json.get('photo_url', None),
            recipe_json.get('cook_time', None),
            recipe_json.get('name', None),
            recipe_json.get('created', None),
            recipe_json.get('notes', None),
            recipe_json.get('image_url', None),
            recipe_json.get('prep_time', None),
            recipe_json.get('servings', None),
            recipe_json.get('nutritional_info', None),
            recipe_json.get('uid', None)
        )

    def __init__(self, rating, photo_hash, on_favorites, photo, scale, ingredients, source, hash, source_url,
                 difficulty, categories, photo_url, cook_time, name, created, notes, image_url, prep_time, servings,
                 nutritional_info, uid):
        """Initialize the model."""
        auto_init()

    async def link_to(self, categories):
        linked_categories = []
        for category_name in self.categories:
            linked_categories.append(
                next((category for category in categories if category.name == category_name), category_name))

        setattr(self, 'categories', linked_categories)
