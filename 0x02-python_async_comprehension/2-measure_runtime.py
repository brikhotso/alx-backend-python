#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
import typing
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four comprehensions running concurrently """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return (end - start)
