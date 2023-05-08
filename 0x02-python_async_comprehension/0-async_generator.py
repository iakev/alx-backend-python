#!/usr/bin/env python3
"""
Contains a coroutine that usues async generator
"""
import asyncio
import random


async def async_generator():
    """
    async generator that yields a random number btn 0 and 10
    """
    random.seed()
    i = 0
    while i < 10:
        result = random.uniform(0, 10)
        yield result
        i += 1
        await asyncio.sleep(1)
