#!/usr/bin/env python3
"""
Creating Async Generator using random module
"""
import asyncio
import random


async def async_generator() -> Generator[
int, None, None]:
    """
    Corotine which asynchronously yields 10 random integer.
    """
    for number in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
