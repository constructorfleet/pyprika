import asyncio
import logging
import threading

from pyprika.framework.work_unit_base import AsyncWorkUnit

_LOGGER = logging.getLogger(__name__)


class BackgroundRefreshData(AsyncWorkUnit):
    """Unit of work to refresh data in background."""

    __slots__ = ['fetch_data', 'interval_minutes']

    def __init__(self, fetch_data, interval_seconds):
        """Initialize the unit of work."""
        self._loop = asyncio.get_event_loop()
        self._thread = threading.Thread(target=self._loop_in_thread)
        self._thread.start()

        self.fetch_data = fetch_data
        self.interval_seconds = interval_seconds
        self._is_running = False
        self._task = None
        asyncio.set_event_loop(self._loop)

    def _loop_in_thread(self):
        while True:
            try:
                self._loop.run_until_complete(asyncio.ensure_future(self.perform_work()))
            except asyncio.CancelledError:
                continue

    async def perform_work(self):
        _LOGGER.warning("PERFORMING WORK")
        while True:
            _LOGGER.warning("FETCHING DATA")
            await self.fetch_data.perform_work()
            _LOGGER.warning("GOING TO SLEEP")
            await asyncio.sleep(self.interval_seconds)
