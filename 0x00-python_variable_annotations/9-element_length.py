#!/usr/bin/env python3
"""
duck type an iterablt object
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """returns a tuple if items and their length"""
    return [(i, len(i)) for i in lst]
