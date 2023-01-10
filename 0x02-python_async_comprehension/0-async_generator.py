#!/usr/bin/env python3
"""loops 10 times waiting 1 second everytime"""


import asyncio
import typing
import random


async def async_generator() -> typing.Generator:
    """loops 10 times waiting 1 second everytime"""
    for i in range(10):
        val = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield (val)
