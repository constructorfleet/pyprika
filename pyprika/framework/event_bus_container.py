
class EventBusContainer:
    def __init__(self, bus):
        self._bus = bus

    @property
    def bus(self):
        return self._bus

    def register_listener(self, cls: ):


