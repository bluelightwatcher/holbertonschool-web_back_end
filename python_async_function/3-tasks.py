#!/usr/bin/env python3
"""function that take an integer and returns a asyncio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio Task to run wait_random with the given max_delay."""
    return asyncio.create_task(wait_random(max_delay))
