import asyncio
import logging
import atexit
import threading

from pyprika.framework.work_unit_base import BackgroundAsyncWorkUnit

_LOGGER = logging.getLogger(__name__)


class BackgroundRefreshData(BackgroundAsyncWorkUnit):
    """Unit of work to refresh data in background."""

    __slots__ = ['fetch_data', 'interval_minutes']

    def __init__(
            self,
            fetch_data,
            interval_seconds,
            autostart=True,
    ):
        """Initialize the unit of work."""
        self.fetch_data = fetch_data
        self.interval_seconds = interval_seconds
        super().__init__(autostart)
        atexit.register(self.stop)

    async def __call__(self):
        while self.is_running:
            await self.fetch_data()
            await asyncio.sleep(self.interval_seconds)
