#!/usr/bin/env python3
"""
Contains an async comprehension utilizing an async generator
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns 10 random numbers using an async comprehension
    over an async generator
    """
    return [i async for i in async_generator()]
