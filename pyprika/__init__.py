"""Library for communicating with Paprika backend servers."""

from datetime import timedelta

from pyprika.data.local.domain_data_store import DomainDataStore
from pyprika.data.remote.paprika_client import PaprikaClient
from pyprika.domain.work_units.backgroud_refresh_data import BackgroundRefreshData
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

    def __init__(self, username, password, fetch_delay=timedelta(hours=2)):
        """Initialize library."""
        self._data_container = DataContainer(
            PaprikaClient(username, password),
            DomainDataStore()
        )

        store_models = StoreModels(self._data_container.domain_data_store)
        link_models = LinkModels(store_models)
        transform_models = TransformModels(link_models)
        fetch_data = FetchData(
            self._data_container.client,
            transform_models,
            self._data_container.domain_data_store
        )
        background_refresh = BackgroundRefreshData(fetch_data, fetch_delay.total_seconds())
        filter_recipes = FilterRecipes(self._data_container.domain_data_store)
        create_filter_specifications = CreateFilterSpecification(filter_recipes)

        self._work_unit_container = WorkUnitContainer(
            background_refresh,
            fetch_data,
            transform_models,
            link_models,
            store_models,
            filter_recipes,
            create_filter_specifications
        )

    def get_all(self):
        return self._data_container.domain_data_store.data

    def get_recipes(
            self,
            categories=None,
            not_categories=None,
            difficulty=None,
            duration=None,
            name_like=None,
            name_not_like=None):
        return self._work_unit_container.create_filter_specifications.perform_work(
            categories=categories,
            not_categories=not_categories,
            difficulty=difficulty,
            duration=duration,
            name_like=name_like,
            name_not_like=name_not_like,
        )
