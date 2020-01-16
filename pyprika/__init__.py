"""Library for communicating with Paprika backend servers."""

import asyncio
import sched
import time
from datetime import timedelta

from pyprika.data.local.domain_data_store import DomainDataStore
from pyprika.data.remote.paprika_client import PaprikaClient
from pyprika.domain.work_units.create_filter_specification import CreateFilterSpecification
from pyprika.domain.work_units.fetch_data import FetchData
from pyprika.domain.work_units.filter_recipes import FilterRecipes
from pyprika.domain.work_units.link_models import LinkModels
from pyprika.domain.work_units.store_models import StoreModels
from pyprika.domain.work_units.transform_models import TransformModels
from pyprika.framework.containers.data_container import DataContainer
from pyprika.framework.containers.work_unit_container import WorkUnitContainer


class Pyprika:
    """Main entry point to library."""

    def __init__(self, username, password, fetch_delay=timedelta(hours=2), auto_fetch=True):
        """Initialize library."""
        self._fetch_event_id = -1
        self._auto_fetch = auto_fetch
        self._fetch_delay = fetch_delay.total_seconds()
        self._data_container = DataContainer(
            PaprikaClient(username, password),
            DomainDataStore(fetch_delay)
        )

        store_models = StoreModels(self._data_container.domain_data_store)
        link_models = LinkModels(store_models)
        transform_models = TransformModels(link_models)
        fetch_data = FetchData(
            self._data_container.client,
            transform_models,
            self._data_container.domain_data_store
        )
        filter_recipes = FilterRecipes(self._data_container.domain_data_store)
        create_filter_specifications = CreateFilterSpecification(filter_recipes)

        self._work_unit_container = WorkUnitContainer(
            fetch_data,
            transform_models,
            link_models,
            store_models,
            filter_recipes,
            create_filter_specifications
        )

        _ = asyncio.get_event_loop().run_until_complete(
            self._work_unit_container.fetch_data.perform_work())
        self._fetch_schedule = sched.scheduler(time.time, time.sleep)

        if auto_fetch:
            self._fetch()

    def _fetch(self):
        def fetch(schedule):
            self._fetch_event_id = self._fetch_schedule.enter(self._fetch_delay, 1, fetch,
                                                              (schedule,))

        self._fetch_event_id = self._fetch_schedule.enter(self._fetch_delay, 1, fetch,
                                                          (self._fetch_schedule,))
        self._fetch_schedule.run()

    async def get_all(self):
        return await self._work_unit_container.fetch_data.perform_work()

    async def get_recipes(
            self,
            categories=None,
            not_categories=None,
            difficulty=None,
            duration=None,
            name_like=None,
            name_not_like=None):
        return await self._work_unit_container.create_filter_specifications.perform_work(
            categories=categories,
            not_categories=not_categories,
            difficulty=difficulty,
            duration=duration,
            name_like=name_like,
            name_not_like=name_not_like,
        )

    def set_auto_fetch(self, enabled):
        """Enable or disable auto fetch."""
        if self._auto_fetch and not enabled and self._fetch_event_id != -1:
            self._fetch_schedule.cancel(self._fetch_event_id)
        elif not self._auto_fetch and enabled:
            self._fetch()

        self._auto_fetch = enabled
