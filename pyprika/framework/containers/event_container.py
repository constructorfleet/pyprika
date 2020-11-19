"""Container for event types and busses."""


class EventContainer:
    """Event bus and event types container."""

    __slots__ = ['publishers', 'subscribers', 'event_types']

    def __init__(
            self,
            publishers=None,
            subscribers=None,
            event_types=None):
        self.publishers = publishers or {}
        self.subscribers = subscribers or {}
        self.event_types = event_types or {}

    def add_publisher
