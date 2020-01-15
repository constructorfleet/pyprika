from pyprika.common.utils import auto_init


class DataContainer:
    """IoC container for data layer."""
    __slots__ = ['client', 'domain_data_store']

    def __init__(self, client, domain_data_store):
        """Initialize Container."""
        auto_init()
