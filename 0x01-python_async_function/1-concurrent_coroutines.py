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
    delays: List[float] = [] #  Define an empty list called delays to store the float values
    tasks: List = [] # Define an empty list called tasks to store the tasks

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay)) # Create a new task using wait_random() and add it to tasks
        tasks.append(task)
        tasks.append(task)

    for task in asyncio.as_completed(tasks): # Loop over the tasks as they are completed

        delay = await task # Wait for the task to complete and store the result in delay
        delays.append(delay) # Add the delay value to the delays list

    return sorted(delays) # Sorted the delays in ascending order
