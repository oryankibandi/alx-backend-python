#!/usr/bin/env python3

"""Measures the runtime of four coroutines"""


import asyncio
import typing
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of four coroutines"""
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop = time.time()

    return stop - start
