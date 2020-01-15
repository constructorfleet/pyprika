"""Specification matching for category."""
from pyprika.common.utils import auto_init
from pyprika.framework.specification.specification import Specification


class CategorySpecification(Specification):
    """Specification on category."""

    __slots__ = ['category']

    def __init__(self, category):
        """Initialize specification."""
        auto_init()

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return self.category in candidate.category_names
