"""Specification matching for recipe difficulty."""
from pyprika.framework.specification.specification import Specification


class DifficultySpecification(Specification):
    """Specification on difficulty."""

    __slots__ = ['difficulty']

    def __init__(self, difficulty):
        """Initialize specification."""
        self.difficulty = difficulty

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return str(self.difficulty).lower() in str(candidate.difficulty).lower()
