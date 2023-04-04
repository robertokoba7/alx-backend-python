#!/usr/bin/env python3
"""
Creating Async Generator using random module
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
  """
    Corotine which asynchronously yields 10 random integer in the given range
    """
   try:
        for number in range(10):
            await asyncio.sleep(1)
            yield random.uniform(0, 10)
    except GeneratorExit:
        pass
