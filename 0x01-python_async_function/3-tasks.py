#!/usr/bin/env python3
"""
Contains a regular function that returns an asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    takes in max_delay createsa  Task from wait_random
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
