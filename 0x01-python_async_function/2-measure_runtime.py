#!/usr/bin/env python3
"""measures the total execution time
for wait_n(n, max_delay), and returns total_time / n"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """ takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    """
    time_before = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_after = time.time()
    total = time_after - time_before
    return total / n
