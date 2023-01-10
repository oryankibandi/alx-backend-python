#!/usr/bin/env python3

"""
returns the list of all the delays in ascending order
"""


import typing
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ return the list of all the delays"""
    tasks: typing.Iterable = []
    results: typing.Iterable = []

    for i in range(0, n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for item in asyncio.as_completed(tasks):
        res = await item
        results.append(res)

    return results
