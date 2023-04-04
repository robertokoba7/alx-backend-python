#!/usr/bin/env python3
"""
Async Comprehension and Parallel execution using asyncio.gather
"""
from typing import List
from time import perf_counter


# async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__(1-async_comprehension).async_comprehension


async def measure_runtime() -> float:
    """
    measure the total runtime and return it.
    """
    start_time = asyncio.default_timer()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    elapse = asyncio.default_timer()
    return elapse - start_time

print(asyncio.run(measure_runtime()))
