#!/usr/bin/env python3
"""
Async Comprehension and Parallel execution to asyncio.gather.
"""
from async_generator import async_generator, async_comprehension
from random import uniform
from typing import List
from time import perf_counter


async def measure_runtime() -> float:
    """
    `measure_runtime` coroutine uses `asyncio.gather` to run four instances
    """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    elapse = perf_counter()
    return elapse - start_time
