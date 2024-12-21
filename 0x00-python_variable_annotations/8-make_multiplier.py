#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that multiplies a float by multiplier.
    """
    def multipliers(n):
        """
        multiply two number
        """
        return n * multiplier
    return multipliers
