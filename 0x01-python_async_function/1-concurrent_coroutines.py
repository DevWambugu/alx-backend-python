#!/usr/bin/env python
'''1-concurrent_coroutines.py
'''


import asyncio
from typing import List
import bisect
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''spawns wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values)
    sorted in ascending order'''
    tasks = []
    delays = []
    for delay_time in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        delay = await task
        insertion_index = bisect.bisect(delays, delay)
        delays.insert(insertion_index, delay)

    return delays
