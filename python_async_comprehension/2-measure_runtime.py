#!/usr/bin/env python3

""" The module """
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the total runtime for 4 tasks """
    start_time = time()

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time()
    return end_time - start_time
