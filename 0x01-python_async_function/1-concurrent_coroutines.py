#!/usr/bin/env python3
"""
spawn multiple coroutines  return the list of all the delays in ascending order
"""
import asyncio
import random
from typing import List


wait_random = __import__(
  '0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
     return the list of all the delays which is a float values
    """
    delay: List[float] = []
    task: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):

        delay = await task
        delays.append(delay)

    return delays
