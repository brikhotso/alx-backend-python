#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time up to max_delay seconds,
    then returns the wait time.

    Args:
    - max_delay (int): The maximum delay time in seconds. Defaults to 10.

    Returns:
    - float: The actual time delayed in seconds.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)

    return wait_time
