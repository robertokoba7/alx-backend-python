#!/usr/bin/env python3
"""
function that takes an integer `max_delay` and returns a `asyncio.task`.
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Type[asyncio.Task]:
    """
    Create asycio.Task object that runs wait_random with max_delay
    """

    # Create an asyncio.Task object to return wait_random with max_delay
    task = asyncio.create_task(wait_random(max_delay))

    # Return the asyncio.Task object
    return task
