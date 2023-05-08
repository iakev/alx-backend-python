#!/usr/bin/env python3
"""
Illustrting how to execute multiple coroutines ata the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with specified max_delay
    """
    delays = []
    for f in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        result = await f
        delays.append(result)
    return delays
