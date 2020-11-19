"""IoC Container for Injecting WorkUnits."""


class WorkUnitContainer:
    """IoC Container for Work Units."""
    __slots__ = ['background_refresh_data', 'fetch_data', 'transform_models', 'link_models',
                 'store_models', 'filter_recipes', 'create_filter_specifications']

    def __init__(self,
                 background_data_refresh,
                 fetch_data,
                 transform_models,
                 link_models,
                 store_models,
                 filter_recipes,
                 create_filter_specifications):
        """Initialize container."""

        self.background_refresh_data = background_data_refresh
        self.fetch_data = fetch_data
        self.transform_models = transform_models
        self.link_models = link_models
        self.store_models = store_models
        self.filter_recipes = filter_recipes
        self.create_filter_specifications = create_filter_specifications
