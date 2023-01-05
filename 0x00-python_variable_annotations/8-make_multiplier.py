#!/usr/bin/env python3
"""
takes a float multiplier as argument and returns a
function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """returns a
    function that multiplies a float by multiplier"""

    def inner(multiply: float):
        return multiplier * multiply

    return inner
