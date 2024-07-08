#!/usr/bin/env python3
""" Defines task_wait_randomfunction."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.
    Task from the wait_random coroutine function.

    Args:
    - max_delay (int): The maximum delay to pass to wait_random.

    Returns:
    - asyncio.Task: The created asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
