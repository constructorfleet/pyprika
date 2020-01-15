"""IoC Container for Injecting WorkUnits."""


class WorkUnitContainer:
    """IoC Container for Work Units."""
    __slots__ = ['fetch_data', 'transform_models', 'link_models', 'store_models', 'filter_recipes',
                 'create_filter_specifications']

    def __init__(self,
                 fetch_data,
                 transform_models,
                 link_models,
                 store_models,
                 filter_recipes,
                 create_filter_specifications):
        """Initialize container."""
        self.fetch_data = fetch_data
        self.transform_models = transform_models
        self.link_models = link_models
        self.store_models = store_models
        self.filter_recipes = filter_recipes
        self.create_filter_specifications = create_filter_specifications
