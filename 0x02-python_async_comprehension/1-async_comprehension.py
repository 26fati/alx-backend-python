#!/usr/bin/env python3
"""
This module contains a function that
performs an asynchronous comprehension.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Perform an asynchronous comprehension.

    Returns:
        A list of floats generated
        by the async generator.

    """
    results = [i async for i in async_generator()]
    return results
