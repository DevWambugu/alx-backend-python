#!/usr/bin/env python
'''1-concurrent_coroutines.py'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    list_of_delays = []
    for delay_time in range(n):
        await wait_random(max_delay)
        list_of_delays.append(float(delay_time))
    list_of_delays.sort()
    return list_of_delays
