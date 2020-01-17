"""Unit of work that filters recipes by a given specifications."""
import logging

from pyprika.framework.work_unit_base import WorkUnit

_LOGGER = logging.getLogger(__name__)


class FilterRecipes(WorkUnit):
    """Filter recipes unit of work."""

    __slots__ = ['domain_data_store']

    def __init__(self, domain_data_store):
        self.domain_data_store = domain_data_store

    def perform_work(self, specification):
        """Perform the unit of work."""
        _LOGGER.warning("Recipes: {}".format(len(self.domain_data_store.data.recipes)))
        return [recipe for recipe in self.domain_data_store.data.recipes if
                specification.is_satisfied_by(recipe)]
