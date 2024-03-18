#!/usr/bin/env python3
"""Contains a method that spawns Tasks n times with a
specified delay between each call."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with a specified delay
    between each call.
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    """
    lst = []
    sorted_list = []
    for _ in range(n):
        lst.append(task_wait_random(max_delay))
    for future in asyncio.as_completed(lst):
        result = await future  # Await the result of each completed future
        sorted_list.append(result)
    return sorted_list
