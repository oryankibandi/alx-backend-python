#!/usr/bin/env python3
"""
returns a tuple
"""


from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """returns a tuple"""
    sq: float = v ** 2
    return (k, sq)
