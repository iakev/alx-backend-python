#!/usr/bin/env python3
"""
Measure time for total execution for some asynchronous routines
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    call wait_n function measure execution time i.e total_time
    return total_time/n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    runtime = time.perf_counter() - start
    return runtime
