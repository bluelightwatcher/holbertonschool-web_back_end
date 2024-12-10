#!/usr/bin/env python3
"""Module to measure runtime of executing async_comprehension in parallel"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    # Execute four async_comprehension calls in parallel
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
