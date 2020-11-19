import asyncio
import logging
import threading
from abc import ABC, abstractmethod
import atexit

_LOGGER = logging.getLogger(__name__)


class AsyncWorkUnit(ABC):
    """Abstract base class for asynchronous unit of work."""

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        """Perform work unit."""


class BackgroundAsyncWorkUnit(AsyncWorkUnit):
    """Abstract base class for background units of work."""

    def __init__(self, auto_start=True):
        """Initialize background worker unit."""
        super(BackgroundAsyncWorkUnit, self).__init__()
        atexit.register(self.stop)
        self._is_running = auto_start
        self._thread = threading.Thread(target=self._worker)
        if auto_start:
            self._thread.start()

    @property
    def is_running(self):
        """Whether the thread is running."""
        return self._is_running

    def start(self):
        if self._is_running:
            return
        self._thread.start()

    def stop(self):
        """Stops the background worker."""
        self._is_running = False
        self._loop.stop()

    def _worker(self, *args, **kwargs):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._loop.run_until_complete(self())
        return

    @abstractmethod
    async def __call__(self):
        """Perform work unit."""
        pass


class WorkUnit(ABC):
    """Abstract base class for unit of work."""

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """Perform work unit."""
