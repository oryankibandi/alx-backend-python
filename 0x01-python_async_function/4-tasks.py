#!/usr/bin/env python3

"""
returns the list of all the delays in ascending order
"""


import typing
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ return the list of all the delays"""
    tasks: typing.List[float] = []

    for i in range(0, n):
        task: float = task_wait_random(max_delay)
        tasks.append(task)

    completed_tasks: typing.Iterable[int] = []

    for item in asyncio.as_completed(tasks):
        res = await item
        print(res)
        completed_tasks.append(res)

    return completed_tasks
