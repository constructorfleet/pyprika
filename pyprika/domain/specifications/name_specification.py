"""Specification matching for recipe name."""
from pyprika.framework.specification.specification import Specification


class NameSpecification(Specification):
    """Specification on name."""

    __slots__ = ['name']

    def __init__(self, name):
        """Initialize specification."""
        self.name = name

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return str(self.name).lower() in str(candidate.name).lower()
