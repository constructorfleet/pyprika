"""Create filter specifications based on provided inputts."""
import logging

from pyprika.domain.specifications import *
from pyprika.framework.specifications import TrueSpecification
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
            specification = specification or ~spec_type(value)
        else:
            specification = specification and spec_type(value)

    return specification


class CreateFilterSpecification(WorkUnit):
    """Filter recipes unit of work."""

    __slots__ = ['filter_recipes']

    def __init__(self, filter_recipes):
        self.filter_recipes = filter_recipes

    def perform_work(self,
                     categories=None,
                     not_categories=None,
                     difficulty=None,
                     duration=None,
                     name_like=None,
                     name_not_like=None,
                     limit=10):
        """Perform unit of work."""
        specification = TrueSpecification()
        if categories:
            _LOGGER.error("CATEGORIES {}".format(categories))
            specification = specification and _build_specification(categories, CategorySpecification)
        if not_categories:
            specification = specification and _build_specification(not_categories, CategorySpecification, True)
        if difficulty:
            specification = specification and _build_specification(difficulty, DifficultySpecification)
        if name_like:
            specification = specification and _build_specification(name_like, NameSpecification)
        if name_not_like:
            specification = specification and _build_specification(name_not_like, NameSpecification, True)

        if duration:
            try:
                float_duration = float(duration)
                specification = specification and _build_specification([float_duration], DurationSpecification)
            except ValueError:
                _LOGGER.error("Duration is not a float")

        return self.filter_recipes.perform_work(specification)
