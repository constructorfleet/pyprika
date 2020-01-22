"""Recipe data model."""

from pyprika.framework.models.base_model import BaseModel


class Recipe(BaseModel):
    """Model for recipe resource."""

    __slots__ = ['rating', 'photo_hash', 'on_favorites', 'photo', 'scale', 'ingredients', 'source',
                 'hash', 'directions', 'source_url', 'difficulty', 'category_uids', 'photo_url',
                 'cook_time', 'name', 'created', 'notes', 'image_url', 'prep_time', 'servings',
                 'nutritional_info', 'uid', 'categories']

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
            recipe_json.get('uid', None),
            recipe_json.get('directions', None)
        )

    def __init__(self, rating, photo_hash, on_favorites, photo, scale, ingredients, source, hash,
                 source_url, difficulty, category_uids, photo_url, cook_time, name, created, notes,
                 image_url, prep_time, servings, nutritional_info, uid, directions):
        """Initialize the model."""
        self.rating = rating
        self.photo_hash = photo_hash
        self.on_favorites = on_favorites
        self.photo = photo
        self.scale = scale
        self.ingredients = ingredients
        self.source = source
        self.hash = hash
        self.source_url = source_url
        self.difficulty = difficulty
        self.category_uids = category_uids
        self.photo_url = photo_url
        self.cook_time = cook_time
        self.name = name
        self.created = created
        self.notes = notes
        self.image_url = image_url
        self.prep_time = prep_time
        self.servings = servings
        self.nutritional_info = nutritional_info
        self.uid = uid
        self.directions = directions

    async def link_to(self, categories):
        """Link to associated categories."""
        linked_categories = []
        for category_uid in self.category_uids:
            linked_category = next(
                (category for category in categories if category.uid == category_uid), None)
            if not linked_category:
                continue
            linked_categories.append(linked_category)

        setattr(self, 'categories', linked_categories)

    @property
    def category_names(self):
        """Get a list of category names."""
        return [category.name for category in self.categories]

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.category_names)
