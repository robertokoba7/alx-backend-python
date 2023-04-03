#!/usr/bin/env python3
"""
spawn multiple coroutines & return the list of all delays in ascending order
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
     return list of all delays which is a float values
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):

        delay = await task
        delays.append(delay)

    return sorted(delays)
