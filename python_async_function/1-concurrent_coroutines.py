#!/usr/bin/env python3
"""Run multiple coroutines concurrently and return their results in order."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return list of delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
