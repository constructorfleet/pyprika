import asyncio
import logging
import atexit
import threading

from pyprika.framework.work_unit_base import AsyncWorkUnit

_LOGGER = logging.getLogger(__name__)


class BackgroundRefreshData(AsyncWorkUnit):
    """Unit of work to refresh data in background."""

    __slots__ = ['fetch_data', 'interval_minutes']

    def __init__(self, fetch_data, interval_seconds):
        """Initialize the unit of work."""
        atexit.register(self._exit_handler)

        self.fetch_data = fetch_data
        self.interval_seconds = interval_seconds
        self._running = True
        self._loop = asyncio.get_event_loop()
        self._thread = threading.Thread(target=self._loop_in_thread)
        self._thread.start()

    def _loop_in_thread(self):
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_until_complete(asyncio.ensure_future(self.perform_work()))
        except asyncio.CancelledError:
            pass

    def _exit_handler(self):
        self._running = False

    async def perform_work(self):
        while self._running:
            await self.fetch_data.perform_work()
            await asyncio.sleep(self.interval_seconds)
