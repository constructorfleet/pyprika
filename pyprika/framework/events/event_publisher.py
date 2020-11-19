class EventPublisher:
    """Enables a class to publish events to the bus."""

    def __init__(self, bus):
        self._bus = bus

    def publish_event(self, event_type, *args, **kwargs):
        """Publishes an event to the event bus."""
        self._bus.emit(event_type, *args, **kwargs)

    def publish_cross_thread_event(self, event_type, *args, **kwargs):
        """Publish an event across thread to the event bus."""
        self.publish_event(event_type, *args, threads=True, **kwargs)