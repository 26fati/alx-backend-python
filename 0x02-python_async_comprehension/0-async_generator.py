#!/usr/bin/env python3
"""
This module contains an async generator function called async_generator.

Keyword arguments:
None

Return:
None
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    Use the random module.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)