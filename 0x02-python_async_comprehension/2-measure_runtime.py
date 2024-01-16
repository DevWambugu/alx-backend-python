#!/usr/bin/env python3
'''Run 4 coroutines at a go'''

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''utilizes async.gather to run 4 functions
    and return the time taken to finish'''

    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        )
    ending_time = asyncio.get_event_loop().time()
    time_taken = ending_time - start_time
    return time_taken
