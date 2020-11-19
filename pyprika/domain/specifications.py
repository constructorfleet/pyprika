"""Specifiations for filtering ittems."""
import re

from pyprika.framework.specifications import Specification

REGEX_HOURS = re.compile(r"(\d*\.\d+|\d+) *(?:\bhour\w?\b)|(?:\bhr\b)", re.RegexFlag.I)
REGEX_MINUTES = re.compile(r"(\d*\.\d+|\d+) +(?:\bmin.*?\b)", re.RegexFlag.I)


def _get_cook_minutes(candidate):
    """Get the cook time in minutes."""
    hours = 0.0
    minutes = 0.0
    for recipe_time in [candidate.cook_time, candidate.prep_time]:
        if recipe_time:
            hour_match = REGEX_HOURS.match(recipe_time)
            minute_match = REGEX_MINUTES.match(recipe_time)
            if hour_match and hour_match.group(1):
                hours += float(hour_match.group(1))
            if minute_match and minute_match.group(1):
                minutes += float(minute_match.group(1))

    return hours * 60 + minutes


class CategorySpecification(Specification):
    """Specification on category."""

    __slots__ = ['category']

    def __init__(self, category):
        """Initialize specifications."""
        self.category = category

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return str(self.category).lower() in [str(name).lower() for name in
                                              candidate.category_names]


class DifficultySpecification(Specification):
    """Specification on difficulty."""

    __slots__ = ['difficulty']

    def __init__(self, difficulty):
        """Initialize specifications."""
        self.difficulty = difficulty

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return str(self.difficulty).lower() in str(candidate.difficulty).lower()


class NameSpecification(Specification):
    """Specification on name."""

    __slots__ = ['name']

    def __init__(self, name):
        """Initialize specifications."""
        self.name = name

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return str(self.name).lower() in str(candidate.name).lower()


class DurationSpecification(Specification):
    """Specification on total cook time."""

    __slots__ = ['duration']

    def __init__(self, duration):
        """Initialize specifications."""
        self.duration = duration

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return _get_cook_minutes(candidate) <= float(self.duration)
