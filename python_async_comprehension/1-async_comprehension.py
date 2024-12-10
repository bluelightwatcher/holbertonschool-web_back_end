#!/usr/bin/env python3
"""Module returns random number in a list of float"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async_comprehension:
            Args: None
            Return list type float: numbers from imported module
    """
    return [number async for number in async_generator()]
