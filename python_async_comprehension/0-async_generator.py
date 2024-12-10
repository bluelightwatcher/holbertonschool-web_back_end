#!/usr/bin/env python3
"""Module creates an async generator"""
import asyncio
import random


async def async_generator():
    """Yield a random number, 10 times, with a 1-second delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
