#!/usr/bin/env python3
"""
sums a list of integers and floats
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """sums a list of integers and floats"""
    tot: float = 0.0

    for item in mxd_lst:
        tot += item

    return tot
