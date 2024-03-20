#!/usr/bin/env python3
"""
 a measure_runtime coroutine that will execute
 async_comprehension four times in parallel
 using asyncio.gather.

measure_runtime should measure the total r
untime and return it.

"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.

    """
    first_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    total = end_time - first_time
    return total
