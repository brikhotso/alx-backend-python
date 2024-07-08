#!/usr/bin/env python3
""" Measures the total execution time for wait_n func."""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures and returns the average time per call of the wait_n function.

    Args:
    - n (int): The number of times to call wait_n.
    - max_delay (int): The maximum delay argument to pass to wait_n.

    Returns:
    - float: The average time taken per call of wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - start_time
    return total_time / n
