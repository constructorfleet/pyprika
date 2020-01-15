"""Specification matching for recipe duration."""
import re

from pyprika.common.utils import auto_init
from pyprika.framework.specification.specification import Specification

REGEX_HOURS = re.compile(r"(\d*\.\d+|\d+) *(?:\bhour\w?\b)|(?:\bhr\b)", re.RegexFlag.I)
REGEX_MINUTES = re.compile(r"(\d*\.\d+|\d+) +(?:\bmin.*?\b)", re.RegexFlag.I)


class DurationSpecification(Specification):
    """Specification on total cook time."""

    __slots__ = ['duration']

    def __init__(self):
        """Initialize specification."""
        auto_init()

    def is_satisfied_by(self, candidate):
        """Checks if candidate satisfies condition."""
        return self._get_cook_minutes(candidate) <= float(self.duration)

    def _get_cook_minutes(self, candidate):
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
