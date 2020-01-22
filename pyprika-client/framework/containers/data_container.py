"""Data layer container for IoC."""


class DataContainer:
    """IoC container for data layer."""
    __slots__ = ['client', 'domain_data_store']

    def __init__(self, client, domain_data_store):
        """Initialize Container."""
        self.client = client
        self.domain_data_store = domain_data_store
