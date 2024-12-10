#!/usr/bin/env python3
"""Module returns random number in a list of float"""
import asyncio
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension:
            Args: None
            Return list type float: numbers from imported module
    """
    return [number async for number in async_generator()]
