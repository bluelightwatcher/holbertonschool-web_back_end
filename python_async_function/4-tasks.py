#!/usr/bin/env python3
"""function that waits for a random delay"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns a list of deadlines in ascending order,
    using asyncio tasks"""
    gecikme = []
    for _ in range(n):
        notdelay = await wait_random(max_delay)
        gecikme.append(notdelay)
    return sorted(gecikme)
