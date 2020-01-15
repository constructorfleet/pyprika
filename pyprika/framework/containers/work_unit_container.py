from pyprika.common.utils import auto_init


class WorkUnitContainer:
    """IoC Container for Work Units."""
    __slots__ = ['fetch_data', 'transform_models', 'link_models', 'store_models']

    def __init__(self, fetch_data, transform_models, link_models, store_models):
        """Initialize container."""
        auto_init()