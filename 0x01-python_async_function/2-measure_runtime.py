#!/usr/bin/env python3

"""
Measures runtime
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures runtime"""

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()

    return (stop - start)/n
