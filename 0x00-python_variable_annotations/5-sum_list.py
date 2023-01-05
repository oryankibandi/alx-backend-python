#!/usr/bin/env python3
"""
sums a list of floats
"""


import typing


def sum_list(input_list: typing.List[float]) -> float:
    """takes a list input_list of floats as
    argument and returns their sum as a float"""

    tot: float = 0.0

    for item in input_list:
        tot += item

    return tot
