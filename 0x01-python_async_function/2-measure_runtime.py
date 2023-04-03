#!/usr/bin/env python3
"""
 measures the total execution time
"""
import asyncio
import time
from typing import List
from wait_n import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    the function measures the total time used for execution
    wait_n. return value is a float.
    """

    # Get the start time
    start_time = time.time()
    # Call the wait_n coroutine to get the delays
    delays: List[float] = await wait_n(n, max_delay)
    # Get the end time
    end_time = time.time()
    # Total execution time
    total_time = end_time - start_time
    # return value: average execution time per task
    return total_time / n
