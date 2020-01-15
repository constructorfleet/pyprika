"""Create filter specification based on provided inputts."""
import logging

from pyprika import CategorySpecification
from pyprika.domain.specifications.difficulty_specification import DifficultySpecification
from pyprika.domain.specifications.duration_specification import DurationSpecification
from pyprika.domain.specifications.name_specification import NameSpecification
from pyprika.framework.specification.true_specification import TrueSpecification
from pyprika.framework.work_unit_base import WorkUnit

_LOGGER = logging.getLogger(__name__)


def _build_specification(values, spec_type, invert=False):
    if values is None:
        return
    if not isinstance(values, list):
        values = [values]
    specification = TrueSpecification()
    for value in values:
        if invert:
            specification &= ~spec_type(value)
        else:
            specification |= spec_type(value)

    return specification


class CreateFilterSpecification(WorkUnit):
    """Filter recipes unit of work."""

    __slots__ = ['filter_recipes']

    def __init__(self, filter_recipes):
        self.filter_recipes = filter_recipes

    async def perform_work(self,
                           categories=None,
                           not_categories=None,
                           difficulty=None,
                           duration=None,
                           name_like=None,
                           name_not_like=None,
                           limit=10):
        """Perform unit of work."""
        specification = TrueSpecification()
        specification &= _build_specification(categories, CategorySpecification)
        specification &= _build_specification(not_categories, CategorySpecification, True)
        specification &= _build_specification(difficulty, DifficultySpecification)
        specification &= _build_specification(name_like, NameSpecification)
        specification &= _build_specification(name_not_like, NameSpecification, True)
        try:
            float_duration = float(duration)
            specification &= _build_specification([float_duration], DurationSpecification)
        except ValueError:
            _LOGGER.error("Duration is not a float")

        return await self.filter_recipes.perform_work(specification)
