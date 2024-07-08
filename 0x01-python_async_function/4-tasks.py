#!/usr/bin/env python3
""" Return the list of all delays."""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with a specified max_delay.
    Returns a list of the wait times.

    Args:
    - n (int): The number of times to call task_wait_random.
    - max_delay (int): The maximum delay passed to task_wait_random.

    Returns:
    - List[float]: A list of floats representing the wait times,
    sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
