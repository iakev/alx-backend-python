#!/usr/bin/env python3
"""
Contains an async coroutine that executes
four times in parallel an async comprehension
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    measures total runtime and returns it
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    runtime = time.perf_counter() - start
    return runtime
