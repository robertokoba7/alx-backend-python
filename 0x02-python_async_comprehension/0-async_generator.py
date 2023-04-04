#!/usr/bin/env python3
"""
Creating Async Generator using random module
"""
import asyncio
import random


async def async_generator() -> AsyncGenerator[int, None]
  """
    Corotine that takes no args
    """
   try:
        for number in range(10):
            await asyncio.sleep(1)
            yield random.randint(0, 10)
    except GeneratorExit:
        pass
