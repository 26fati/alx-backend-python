#!/usr/bin/python3
"""
     an asynchronous coroutine
     that takes in an integer argument
     (max_delay, with a default value of 10)
    """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
    in ascending order without using sort() because of concurrency.
    """
    lst = []
    sorted_list = []
    for _ in range(n):
        lst.append(wait_random(max_delay))
    for future in asyncio.as_completed(lst):
        result = await future  # Await the result of each completed future
        sorted_list.append(result)
    return sorted_list
