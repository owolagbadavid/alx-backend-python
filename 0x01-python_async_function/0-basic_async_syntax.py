#!/usr/bin/env python3

import asyncio
import random

"""
asynchronous coroutine 
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in none arguments
    and returns a float
    """

    time = random.uniform(0, 10)
    await asyncio.sleep(time)
    return time
