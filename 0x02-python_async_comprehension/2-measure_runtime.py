#!/usr/bin/env python3
"""
Async Comprehension and Parallel execution using asyncio.gather
"""
from typing import List
from time import perf_counter


async_comprehension = __import__(1-async_comprehension).async_comprehension


async def measure_runtime() -> List[float]:
    """
    measure the total runtime and return it.
    """
    start_time = time.perf_counter()
    my_list = [asyncio.create_(async_comprehension()) for i in range(4)])
    result = await asyncio.gather(*my_list)
    total_time = time.perf_counter() -start_time
    return total_time
