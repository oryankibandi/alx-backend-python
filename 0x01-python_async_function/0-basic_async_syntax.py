#!/usr/bin/env python3

"""
returns a arndom foat value
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay"""
    random_num = random.uniform(0, max_delay)

    await asyncio.sleep(random_num)

    return random_num
