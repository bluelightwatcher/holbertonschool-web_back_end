#!/usr/bin/env python3
"""function that measures the runtime of executing concurrent coroutines"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        notdelay = await wait_random(max_delay)
        delays.append(notdelay)
    return sorted(delays)
