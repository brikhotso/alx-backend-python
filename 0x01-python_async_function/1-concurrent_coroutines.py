#!/usr/bin/env python3
""" Return the list of all delays."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times with a specified max_delay.
    Returns a list of the wait times.

    Args:
    - n (int): The number of times to call wait_random.
    - max_delay (int): The maximum delay passed to wait_random.

    Returns:
    - List[float]: A list of floats representing the wait times,
    sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
