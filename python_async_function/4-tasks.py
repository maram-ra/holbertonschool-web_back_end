#!/usr/bin/env python3
"""Run multiple task-based coroutines concurrently and return their results in order."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        results.append(delay)

    return results
