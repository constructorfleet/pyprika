"""Unit of work that filters recipes by a given specification."""
from pyprika.common.utils import auto_init
from pyprika.framework.work_unit_base import WorkUnit


class FilterRecipes(WorkUnit):
    """Filter recipes unit of work."""

    __slots__ = ['domain_data_store']

    def __init__(self, domain_data_store):
        auto_init()

    async def perform_work(self, specification):
        """Perform the unit of work."""
        return [recipe.name for recipe in self.domain_data_store.data.recipes if
                specification.is_satisfied_by(recipe)]
